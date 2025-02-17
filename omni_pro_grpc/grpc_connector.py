import datetime
import hashlib
import importlib
import math

import grpc
from google.protobuf.message import Message as MessageResponse
from grpc._channel import Channel
from grpc.experimental import _insecure_channel_credentials
from omni_pro_base.config import Config
from omni_pro_base.logger import configure_logger
from omni_pro_base.util import function_thread_controller, nested
from omni_pro_grpc.util import MessageToDict, format_request
from omni_pro_redis.redis import RedisCache, RedisManager

logger = configure_logger(name=__name__)


class Event(dict):
    def __init__(
        self,
        module_grpc: str,
        stub_classname: str,
        rpc_method: str,
        module_pb2: str,
        request_class: str,
        params: dict = {},
    ):
        super().__init__()
        self["module_grpc"] = module_grpc
        self["stub_classname"] = stub_classname
        self["rpc_method"] = rpc_method
        self["module_pb2"] = module_pb2
        self["request_class"] = request_class
        self["params"] = params

    def get_hash_256(self) -> str:
        """
        Generates a SHA-256 hash for the given payload.

        Returns:
            str: The SHA-256 hash of the payload.
        """

        payload = {
            "rpc_method": self.get("rpc_method"),
            "module_pb2": self.get("module_pb2"),
            "request_class": self.get("request_class"),
            "params": self.get("params"),
        }
        module_grpc = self.get("module_grpc") + "."
        return module_grpc + hashlib.sha256(str(payload).encode()).hexdigest()


class OmniChannel(Channel):
    def __init__(
        self,
        service_id,
        credentials=None,
        options=None,
        compression=None,
        tennat=None,
    ):
        if not Config.DEBUG:
            credentials = credentials or grpc.ssl_channel_credentials()
            if credentials is None or credentials._credentials is _insecure_channel_credentials:
                raise ValueError(
                    "secure_channel cannot be called with insecure credentials." + " Call insecure_channel instead."
                )
            credentials = credentials._credentials
            options = options + [("grpc.ssl_target_name_override", Config.GRPC_SSL_NAME)] or [
                ("grpc.ssl_target_name_override", Config.GRPC_SSL_NAME)
            ]

        target = self.get_target(service_id, tennat)
        super().__init__(target, () if options is None else options, credentials, compression)

    def get_target(self, service_id, tennat):
        redis = RedisManager(
            host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB, redis_ssl=Config.REDIS_SSL
        )
        return redis.get_load_balancer_name(service_id, tennat)


class GRPClient(object):
    def __init__(self, service_id: str, timeout: float = 0):
        self.service_id = service_id
        self.timeout = timeout

    def call_rpc_fuction(self, event: Event, cache=False, store_cache=False, *args, **kwargs):
        # logger.info(f"This function is deprecated, use call_rpc_function instead.")
        return self.call_rpc_function(event, cache, store_cache, *args, **kwargs)

    def call_rpc_function(self, event: Event, cache=False, store_cache=False, *args, **kwargs):
        """
        function to call rpc function
        :param event: Event with params to call rpc function
        ```
        event = Event(
            module_grpc="v1.users.user_pb2_grpc",
            stub_classname="UsersServiceStub",
            rpc_method="UserRead",
            module_pb2="v1.users.user_pb2",
            request_class="UserReadRequest",
            params={"id": "64adc0477be3ec5e9160b16e", "context": {"tenant": "SPLA", "user": "admin"}},
        )
        response, success = GRPClient(service_id=Config.SERVICE_ID).call_rpc_fuction(event)
        ```
        """
        path_module = kwargs.pop("path_module", "omni_pro_grpc")
        self.tenant = kwargs.pop("tenant", nested(event, "params.context.tenant"))
        with OmniChannel(
            self.service_id,
            options=[
                ("grpc.max_receive_message_length", 100 * 1024 * 1024),
                ("grpc.max_send_message_length", 100 * 1024 * 1024),
            ],
            *args,
            **kwargs,
            tennat=self.tenant,
        ) as channel:
            stub = event.get("service_stub")
            self.stub_classname = event.get("stub_classname")
            self.module_grpc = importlib.import_module(f"{path_module}.{event.get('module_grpc')}")
            stub = getattr(self.module_grpc, self.stub_classname)(channel)
            request_class = event.get("request_class")
            module_pb2 = importlib.import_module(f"{path_module}.{event.get('module_pb2')}")
            self.redis_cache = self.set_cache_redis()

            if cache:
                resul_cache = self.get_cache(event, module_pb2, stub, *args, **kwargs)
                if resul_cache:
                    return resul_cache, True

            request = format_request(event.get("params"), request_class, module_pb2)

            if (rpc_method := event.get("rpc_method")) in ("Login",):
                response, cookies = self._execute_grpc_with_cookies(rpc_method, stub, request)
                success = self._is_successful_response(response)
                self._save_cache(event, response, store_cache, module_pb2, *args, **kwargs)
                return response, success, cookies

            response = getattr(stub, rpc_method)(request, timeout=self.timeout if self.timeout else None)
            success = self._is_successful_response(response)
            self._save_cache(event, response, store_cache, module_pb2, *args, **kwargs)
            return response, success

    def _is_successful_response(self, response):
        """
        Determines if the given response is successful.
        Args:
            response: The response object to check. It is expected to have an attribute
                      `response_standard` with a `status_code` attribute.
        Returns:
            bool: True if the response is considered successful (status code in the range 200-299),
                  False otherwise.
        """

        success = True
        if hasattr(response, "response_standard"):
            success = response.response_standard.status_code in range(200, 300)
        return success

    def _save_cache(self, event, response, store_cache, module_pb2, *args, **kwargs):
        """
        Handles caching of gRPC responses based on the provided event and conditions.
        Args:
            event (dict): The event data containing details such as the RPC method.
            response (Any): The response data to be cached.
            store_cache (bool): Flag indicating whether to store the cache.
            module_pb2 (module): The protocol buffer module used for updating the cache.
            *args: Additional arguments for cache update.
            **kwargs: Additional keyword arguments for cache update.
        Returns:
            None
        """

        if store_cache:
            self.save_cache(event, response)

        if not self.validate_method_read(event.get("rpc_method")):
            self.update_cache_cud(event, module_pb2, *args, **kwargs)

    def _execute_grpc_with_cookies(self, rpc_method, stub, request):
        """
        Ejecuta una llamada RPC y extrae cookies si el método es "Login".
        """

        response, call = getattr(stub, rpc_method).with_call(request)
        cookies = self._extract_cookies_from_metadata(call.initial_metadata())

        return response, cookies

    def _extract_cookies_from_metadata(self, metadata):
        """
        Extrae las cookies del metadata de la respuesta gRPC.
        """
        return [value for key, value in (metadata or []) if key.lower() == "set-cookie"]

    def get_cache(self, event: Event, module_pb2, stub, *args, **kwargs) -> MessageResponse:
        """
        Validates the cache for a given event.

        Args:
            event (Event): The event to validate the cache for.
            module_pb2 (ModuleType): The module_pb2 module.

        Returns:
            Message formatted request if the cache is valid, None otherwise.
        """
        try:
            hash_key = event.get_hash_256()
            data = self.redis_cache.get_cache(hash_key)
            if data:
                response_class_name = data.get("info").get("response_class")
                data_cache = data.get("cache")

                self.update_cache(hash_key, data, event, module_pb2, *args, **kwargs)

                return format_request(data_cache, response_class_name, module_pb2)
        except Exception as e:
            logger.error(f"Error getting cache: {e}")
            pass

    def set_cache_redis(self):
        """
        Sets up and returns a RedisCache object based on the configuration retrieved from RedisManager.

        Returns:
            RedisCache: The RedisCache object configured with the appropriate host, port, db, and redis_ssl settings.
        """
        redis = RedisManager(
            host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB, redis_ssl=Config.REDIS_SSL
        )
        config = redis.get_resource_config(Config.SAAS_REDIS_CACHE, self.tenant)
        return RedisCache(
            host=config.get("host"), port=config.get("port"), db=config.get("db"), redis_ssl=config.get("redis_ssl")
        )

    def save_cache(self, event: Event, message: MessageResponse):
        """
        Saves the cache for the given event and message response.

        Args:
            event (Event): The event object.
            message (MessageResponse): The message response object.

        Returns:
            None
        """
        try:
            hash_key = event.get_hash_256()
            response_class_name = message.__class__.__name__
            data_cache = MessageToDict(message)
            data = {
                "cache": data_cache,
                "info": {
                    "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "response_class": response_class_name,
                    "count": 1,
                    "max_request": 5,
                    "history_request": [datetime.datetime.timestamp(datetime.datetime.now())],
                    "umbral_interval": 1,
                },
                "event": dict(event),
            }

            self.redis_cache.save_cache(hash_key, data)
        except Exception as e:
            logger.error(f"Error saving cache: {e}")
            pass

    def validate_method_read(self, method: str) -> bool:
        """
        Validates if the given method is a read method.

        Args:
            method (str): The method to be validated.

        Returns:
            bool: True if the method is a read method, False otherwise.
        """
        return "Read" in method

    @function_thread_controller.run_thread_controller
    def update_cache(self, hash_key: str, data: dict, event: Event, module_pb2, forced=False, *args, **kwargs):
        """
        Updates the cache with the given data.
        Args:
            hash_key (str): The key used to identify the cache entry.
            data (dict): The data to be stored in the cache.
            event (Event): The event triggering the cache update.
            module_pb2: The module_pb2 object.
        Raises:
            None
        Returns:
            None
        """
        try:
            with OmniChannel(
                self.service_id,
                options=[
                    ("grpc.max_receive_message_length", 100 * 1024 * 1024),
                    ("grpc.max_send_message_length", 100 * 1024 * 1024),
                ],
                *args,
                **kwargs,
                tennat=self.tenant,
            ) as channel:
                if forced:
                    self.update_cache_forced(event, module_pb2, channel)

                elif data.get("info").get("count") == data.get("info").get("max_request"):
                    new_cache = self.request_to_ms(event, module_pb2, None, channel)

                    data["info"]["max_request"] = self.increment_max_request(
                        data["info"]["history_request"],
                        data["info"]["max_request"],
                        data["info"]["umbral_interval"],
                    )
                    data["info"]["count"] = 1
                    data["info"]["history_request"] = [datetime.datetime.timestamp(datetime.datetime.now())]
                    if self.validate_response_hash(data["cache"], new_cache):
                        self.redis_cache.save_cache(hash_key, data, expire=False)
                    else:
                        data["cache"] = new_cache
                        self.redis_cache.save_cache(hash_key, data)
                else:
                    data["info"]["count"] = data["info"]["count"] + 1  # Increment count
                    data["info"]["history_request"].append(datetime.datetime.timestamp(datetime.datetime.now()))
                    data["info"]["umbral_interval"] = self.average_interval(data["info"]["history_request"])
                    self.redis_cache.save_cache(hash_key, data, expire=False)

        except Exception as e:
            logger.error(f"Error updating cache: {e}")
            pass

    def increment_max_request(self, timestamps: list[float], max_request: int, umbral_interval: float) -> int:
        """
        Calculates the incremented value of max_request based on the average interval and a threshold interval.

        Args:
            timestamps (list[float]): A list of timestamps.
            max_request (int): The current value of max_request.
            umbral_interval (float): The threshold interval.

        Returns:
            int: The incremented value of max_request.
        """

        average_interval = self.average_interval(timestamps)
        smoothing = 0.5

        if average_interval <= umbral_interval:
            increment = 1 + smoothing * math.exp(1 / average_interval)
            # max_request = min(int(max_request * incremento), 100)
            max_request = int(max_request * increment)

        return max_request

    def average_interval(self, timestamps: list[float]) -> float:
        """
        Calculates the average interval between timestamps.

        Args:
            timestamps (list[float]): A list of timestamps.

        Returns:
            float: The average interval between timestamps.
        """
        intervals = [timestamps[i] - timestamps[i - 1] for i in range(1, len(timestamps))]
        return sum(intervals) / len(intervals)

    def validate_response_hash(self, cache, new_cache):
        """
        Validates the response hash by comparing the SHA256 hash of the cache and new_cache.

        Args:
            cache: The cache value to be compared.
            new_cache: The new_cache value to be compared.

        Returns:
            True if the SHA256 hash of cache and new_cache are equal, False otherwise.
        """
        if hashlib.sha256(str(cache).encode()).hexdigest() == hashlib.sha256(str(new_cache).encode()).hexdigest():
            return True
        return False

    # @function_thread_controller.run_thread_controller
    def update_cache_cud(self, event: Event, module_pb2, *args, **kwargs):
        """
        Updates the cache for CUD operations and others services.

        Args:
            event (Event): The event object.
            module_pb2: The module_pb2 object.
            stub: The stub object.

        Returns:
            None
        """
        try:
            self.update_cache(None, None, event, module_pb2, True, *args, **kwargs)
        except Exception as e:
            logger.error(f"Error updating cache: {e}")
            pass

    def request_to_ms(self, event: Event, module_pb2, rpc_method, channel):
        """
        Sends a request to a microservice and returns the response.
        Args:
            event (Event): The event containing the request details.
            module_pb2 (module): The protocol buffer module for the request.
            rpc_method (str): The RPC method to call. If None, it will be retrieved from the event.
            channel (grpc.Channel): The gRPC channel to use for the request.
        Returns:
            dict: The response from the microservice, converted to a dictionary.
        """

        rpc_method = event.get("rpc_method") if rpc_method is None else rpc_method
        request = format_request(event.get("params"), event.get("request_class"), module_pb2)
        stub = getattr(self.module_grpc, self.stub_classname)(channel)
        response = getattr(stub, rpc_method)(request)
        new_cache = MessageToDict(response)
        return new_cache

    def update_cache_forced(self, event: Event, module_pb2, channel):
        """
        Updates the cache forcefully for a given event by re-fetching data from the microservice.
        Args:
            event (Event): The event object containing details to be processed.
            module_pb2: The protocol buffer module used for serialization and deserialization.
            channel: The gRPC channel used to communicate with the microservice.
        Returns:
            None
        """

        def parse_datetime(data):
            return datetime.datetime.strptime(list(data.values())[0]["info"]["created_at"], "%Y-%m-%d %H:%M:%S")

        prefix_hash_key = event.get("module_grpc")
        list_data = self.redis_cache.get_keys_with_prefix(prefix_hash_key)

        list_data_sorted = sorted(list_data, key=parse_datetime)

        for data in list_data_sorted:
            hash_key, data = list(data.keys())[0], list(data.values())[0]
            event_forced = Event(**data.get("event"))
            new_cache = self.request_to_ms(event_forced, module_pb2, None, channel)
            if not self.validate_response_hash(data["cache"], new_cache):
                data["cache"] = new_cache
                self.redis_cache.save_cache(hash_key, data)
