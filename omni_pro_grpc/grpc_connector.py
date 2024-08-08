import hashlib
import importlib

import grpc
from google.protobuf.message import Message as MessageResponse
from grpc._channel import Channel
from grpc.experimental import _insecure_channel_credentials
from omni_pro_base.config import Config
from omni_pro_base.logger import configure_logger
from omni_pro_base.util import nested
from omni_pro_grpc.util import MessageToDict, format_request
from omni_pro_redis.redis import RedisManager

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
        return hashlib.sha256(str(payload).encode()).hexdigest()


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
            options = options + [("grpc.ssl_target_name_override", "omni.pro")] or [
                ("grpc.ssl_target_name_override", "omni.pro")
            ]

        target = self.get_target(service_id, tennat)
        super().__init__(target, () if options is None else options, credentials, compression)

    def get_target(self, service_id, tennat):
        redis = RedisManager(
            host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB, redis_ssl=Config.REDIS_SSL
        )
        return redis.get_load_balancer_name(service_id, tennat)


class GRPClient(object):
    def __init__(self, service_id: str):
        self.service_id = service_id

    def call_rpc_fuction(self, event: Event, cache=False, *args, **kwargs):
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
        self.tennat = nested(event, "params.context.tenant")
        with OmniChannel(
            self.service_id,
            options=[
                ("grpc.max_receive_message_length", 100 * 1024 * 1024),
                ("grpc.max_send_message_length", 100 * 1024 * 1024),
            ],
            *args,
            **kwargs,
            tennat=self.tennat,
        ) as channel:
            stub = event.get("service_stub")
            stub_classname = event.get("stub_classname")
            path_module = "omni_pro_grpc"
            module_grpc = importlib.import_module(f"{path_module}.{event.get('module_grpc')}")
            stub = getattr(module_grpc, stub_classname)(channel)
            request_class = event.get("request_class")
            module_pb2 = importlib.import_module(f"{path_module}.{event.get('module_pb2')}")
            if cache and self.validate_method_read(event.get("rpc_method")):
                resul_cache = self.get_cache(event, module_pb2)
                if resul_cache:
                    return resul_cache, True

            request = format_request(event.get("params"), request_class, module_pb2)
            # Instance the method rpc que recibe el request
            response = getattr(stub, event.get("rpc_method"))(request)
            if cache and self.validate_method_read(event.get("rpc_method")):
                self.save_cache(event, response)
            success = True
            if hasattr(response, "response_standard"):
                success = response.response_standard.status_code in range(200, 300)
            return response, success

    def get_cache(self, event: Event, module_pb2) -> MessageResponse:
        """
        Validates the cache for a given event.

        Args:
            event (Event): The event to validate the cache for.
            module_pb2 (ModuleType): The module_pb2 module.

        Returns:
            Message formatted request if the cache is valid, None otherwise.
        """
        self.redis_cache = self.set_cache_redis()
        hash_key = event.get_hash_256()
        data = self.redis_cache.get_cache(hash_key)
        if data:
            response_class_name = data.pop("response_class_name")
            return format_request(data, response_class_name, module_pb2)

    def set_cache_redis(self):
        from omni.pro.database.redis import RedisCache

        """
        Sets up and returns a RedisCache object based on the configuration retrieved from RedisManager.

        Returns:
            RedisCache: The RedisCache object configured with the appropriate host, port, db, and redis_ssl settings.
        """
        redis = RedisManager(
            host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB, redis_ssl=Config.REDIS_SSL
        )
        config = redis.get_resource_config(Config.SAAS_REDIS_CACHE, self.tennat)
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
        hash_key = event.get_hash_256()
        response_class_name = message.__class__.__name__
        data = MessageToDict(message)
        data["response_class_name"] = response_class_name
        self.redis_cache.save_cache(hash_key, data)

    def validate_method_read(self, method: str) -> bool:
        """
        Validates if the given method is a read method.

        Args:
            method (str): The method to be validated.

        Returns:
            bool: True if the method is a read method, False otherwise.
        """
        return "Read" in method
