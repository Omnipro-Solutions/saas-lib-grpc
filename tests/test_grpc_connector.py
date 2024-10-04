import hashlib
import unittest
from unittest.mock import ANY, MagicMock, call, patch

from omni_pro_grpc.grpc_connector import Event, GRPClient, OmniChannel, RedisCache
from omni_pro_grpc.v1.users.user_pb2 import UserReadRequest


class TestGrpcConnector(unittest.TestCase):

    def setUp(self):
        self.module_grpc = "v1.users.user_pb2_grpc"
        self.stub_classname = "UsersServiceStub"
        self.rpc_method = "UserRead"
        self.module_pb2 = "v1.users.user_pb2"
        self.request_class = "UserReadRequest"
        self.params = {"id": "64adc0477be3ec5e9160b16e", "context": {"tenant": "SPLA", "user": "admin"}}

        self.event = Event(
            self.module_grpc,
            self.stub_classname,
            self.rpc_method,
            self.module_pb2,
            self.request_class,
            self.params,
        )

        self.grpc_client = GRPClient(service_id="service_id_test")

        self.event_cache = MagicMock(spec=Event)
        self.module_pb2_cache = MagicMock()
        self.data = {"cache": {}, "info": {"count": 0, "max_request": 5, "history_request": [], "umbral_interval": 0}}

        self.grpc_client.redis_cache = MagicMock()
        self.channel = MagicMock()
        self.module_grpc_client = MagicMock()
        self.grpc_client.module_grpc = self.module_grpc_client
        self.grpc_client.stub_classname = self.stub_classname

    def test_event_initialization(self):
        self.assertEqual(self.event["module_grpc"], self.module_grpc)
        self.assertEqual(self.event["stub_classname"], self.stub_classname)
        self.assertEqual(self.event["rpc_method"], self.rpc_method)
        self.assertEqual(self.event["module_pb2"], self.module_pb2)
        self.assertEqual(self.event["request_class"], self.request_class)
        self.assertEqual(self.event["params"], self.params)

    def test_event_get_hash_256(self):
        payload = {
            "rpc_method": self.rpc_method,
            "module_pb2": self.module_pb2,
            "request_class": self.request_class,
            "params": self.params,
        }
        module_grpc_with_dot = self.module_grpc + "."
        expected_hash = module_grpc_with_dot + hashlib.sha256(str(payload).encode()).hexdigest()

        self.assertEqual(self.event.get_hash_256(), expected_hash)

    @patch("omni_pro_redis.redis.RedisManager.get_load_balancer_name")
    def test_omni_channel_secure(self, mock_get_load_balancer_name):
        mock_get_load_balancer_name.return_value = "mocked_load_balancer_name"

        channel = OmniChannel(service_id="test_service_id", tennat="test_tennat")

        self.assertEqual(channel.target, "mocked_load_balancer_name")

    @patch("omni_pro_grpc.grpc_connector.Config.DEBUG", True)
    @patch("omni_pro_redis.redis.RedisManager.get_load_balancer_name")
    def test_omni_channel_debug_true(self, mock_get_load_balancer_name):
        mock_get_load_balancer_name.return_value = "mocked_load_balancer_name"

        channel = OmniChannel(service_id="test_service_id", tennat="test_tennat")

        self.assertEqual(channel.target, "mocked_load_balancer_name")
        self.assertFalse(hasattr(channel, "credentials"))

    @patch("omni_pro_grpc.grpc_connector.Config.DEBUG", False)
    @patch("omni_pro_redis.redis.RedisManager.get_load_balancer_name")
    @patch("omni_pro_grpc.grpc_connector.grpc.ssl_channel_credentials")
    def test_omni_channel_invalid_credentials(self, mock_ssl_channel_credentials, mock_get_load_balancer_name):
        mock_get_load_balancer_name.return_value = "mocked_load_balancer_name"

        mock_ssl_channel_credentials.return_value = None

        with self.assertRaises(ValueError):
            OmniChannel(service_id="test_service_id", tennat="test_tennat")

    @patch("omni_pro_redis.redis.RedisManager.get_load_balancer_name")
    def test_omni_channel_get_target_secure(self, mock_get_load_balancer_name):
        mock_get_load_balancer_name.return_value = "mocked_load_balancer_name"

        channel = OmniChannel(service_id="test_service_id", tennat="test_tennat")

        self.assertEqual(
            channel.get_target(service_id="test_service_id", tennat="test_tennat"), "mocked_load_balancer_name"
        )

    @patch("omni_pro_grpc.grpc_connector.grpc.insecure_channel")
    def test_grpc_client_secure(self, mock_insecure_channel):
        mock_insecure_channel.return_value = MagicMock()
        client = GRPClient(service_id="test_service_id", timeout=10.0)

        self.assertIsNotNone(client.service_id)
        self.assertIsNotNone(client.timeout)

    @patch("omni_pro_grpc.grpc_connector.OmniChannel")
    @patch("importlib.import_module")
    @patch.object(GRPClient, "set_cache_redis")
    @patch.object(GRPClient, "get_cache")
    @patch.object(GRPClient, "validate_method_read")
    @patch.object(GRPClient, "save_cache")
    @patch.object(GRPClient, "update_cache_cud")
    def test_grpc_client_call_rpc_function(
        self,
        mock_update_cache_cud,
        mock_save_cache,
        mock_validate_method_read,
        mock_get_cache,
        mock_set_cache_redis,
        mock_import_module,
        mock_omni_channel,
    ):

        grpc_client = GRPClient(service_id="test_service_id")

        mock_channel = MagicMock()
        mock_omni_channel.return_value.__enter__.return_value = mock_channel

        mock_stub_class = MagicMock()
        mock_import_module.return_value = MagicMock()
        mock_import_module.return_value.UsersServiceStub = mock_stub_class

        mock_stub_instance = MagicMock()
        mock_stub_class.return_value = mock_stub_instance
        mock_response = MagicMock()
        mock_response.response_standard.status_code = 200
        mock_stub_instance.UserRead.return_value = mock_response

        mock_validate_method_read.return_value = True
        mock_get_cache.return_value = None

        request = UserReadRequest(id="64adc0477be3ec5e9160b16e", context={"tenant": "SPLA", "user": "admin"})

        with patch("google.protobuf.json_format.ParseDict", return_value=request):
            response, success = grpc_client.call_rpc_fuction(self.event, cache=True)

        mock_omni_channel.assert_called_once_with(
            grpc_client.service_id,
            options=[
                ("grpc.max_receive_message_length", 100 * 1024 * 1024),
                ("grpc.max_send_message_length", 100 * 1024 * 1024),
            ],
            tennat="SPLA",
        )

        mock_stub_class.assert_called_once_with(mock_channel)
        mock_stub_instance.UserRead.assert_called_once_with(request)

        mock_validate_method_read.assert_has_calls([call("UserRead"), call("UserRead")])
        mock_save_cache.assert_called_once_with(self.event, mock_response)
        mock_update_cache_cud.assert_called_once_with(self.event, mock_import_module.return_value, mock_stub_instance)

        self.assertEqual(response, mock_response)
        self.assertTrue(success)

    @patch("omni_pro_grpc.grpc_connector.OmniChannel")
    @patch("importlib.import_module")
    @patch.object(GRPClient, "set_cache_redis")
    @patch.object(GRPClient, "update_cache_cud")
    def test_grpc_client_call_rpc_function_no_cache(
        self, mock_update_cache_cud, mock_set_cache_redis, mock_import_module, mock_omni_channel
    ):

        grpc_client = GRPClient(service_id="test_service_id")

        mock_channel = MagicMock()
        mock_omni_channel.return_value.__enter__.return_value = mock_channel

        mock_stub_class = MagicMock()
        mock_import_module.return_value = MagicMock()
        mock_import_module.return_value.UsersServiceStub = mock_stub_class

        mock_stub_instance = MagicMock()
        mock_stub_class.return_value = mock_stub_instance
        mock_response = MagicMock()

        mock_response.response_standard.status_code = 200
        mock_stub_instance.UserRead.return_value = mock_response

        request = UserReadRequest(id="64adc0477be3ec5e9160b16e", context={"tenant": "SPLA", "user": "admin"})

        with patch("google.protobuf.json_format.ParseDict", return_value=request):
            response, success = grpc_client.call_rpc_fuction(self.event, cache=False)

        mock_omni_channel.assert_called_once_with(
            grpc_client.service_id,
            options=[
                ("grpc.max_receive_message_length", 100 * 1024 * 1024),
                ("grpc.max_send_message_length", 100 * 1024 * 1024),
            ],
            tennat="SPLA",
        )

        mock_stub_class.assert_called_once_with(mock_channel)
        mock_stub_instance.UserRead.assert_called_once_with(request)

        mock_update_cache_cud.assert_called_once_with(self.event, mock_import_module.return_value, mock_stub_instance)

        self.assertEqual(response, mock_response)
        self.assertTrue(success)

    @patch.object(GRPClient, "get_cache")
    def test_grpc_client_get_cache(self, mock_get_cache):
        self.event_cache.get_hash_256.return_value = "fake_hash"

        mock_get_cache.return_value = {"info": {"response_class": "TestResponseClass"}, "cache": {"key": "value"}}

        response = self.grpc_client.get_cache(self.event_cache, self.module_pb2_cache, self.stub_classname)

        mock_get_cache.assert_called_once_with(self.event_cache, self.module_pb2_cache, self.stub_classname)

        self.assertEqual(response, mock_get_cache.return_value)

    @patch.object(GRPClient, "set_cache_redis")
    def test_grpc_client_set_cache_redis(self, mock_set_cache_redis):
        mock_set_cache_redis.return_value = {"host": "localhost", "port": 6379, "db": 0, "redis_ssl": False}

        self.event_cache.get_hash_256.return_value = "fake_hash"

        response = self.grpc_client.set_cache_redis()

        mock_set_cache_redis.assert_called_once_with()

        self.assertEqual(response, mock_set_cache_redis.return_value)

    @patch.object(GRPClient, "save_cache")
    def test_grpc_client_save_cache(self, mock_save_cache):
        self.event_cache.get_hash_256.return_value = "fake_hash"
        response = MagicMock()

        self.grpc_client.save_cache(self.event_cache, response)

        mock_save_cache.assert_called_once_with(self.event_cache, response)

    @patch.object(GRPClient, "update_cache")
    def test_grpc_client_update_cache(self, mock_update_cache):
        self.event_cache.get_hash_256.return_value = "fake_hash"
        response = MagicMock()

        self.grpc_client.update_cache(self.event_cache, response)

        mock_update_cache.assert_called_once_with(self.event_cache, response)

    @patch.object(GRPClient, "update_cache")
    def test_grpc_client_update_cache_forced(self, mock_update_cache):
        self.event_cache.get_hash_256.return_value = "fake_hash"
        response = MagicMock()

        self.grpc_client.update_cache(self.event_cache, response, forced=True)

        mock_update_cache.assert_called_once_with(self.event_cache, response, forced=True)

        self.assertEqual(self.grpc_client.redis_cache, self.grpc_client.redis_cache)

    def test_increment_max_request_below_threshold(self):
        timestamps = [1000.0, 1001.0, 1002.0]
        max_request = 5
        umbral_interval = 1.0

        result = self.grpc_client.increment_max_request(timestamps, max_request, umbral_interval)

        self.assertGreater(result, max_request)

    def test_increment_max_request_above_threshold(self):
        timestamps = [1000.0, 1010.0, 1020.0]
        max_request = 5
        umbral_interval = 0.1

        result = self.grpc_client.increment_max_request(timestamps, max_request, umbral_interval)

        self.assertEqual(result, max_request)

    def test_average_interval(self):
        timestamps = [1000.0, 1005.0, 1010.0]

        result = self.grpc_client.average_interval(timestamps)

        self.assertEqual(result, 5.0)

    def test_average_interval_single_timestamp(self):
        timestamps = [1000.0]

        with self.assertRaises(ZeroDivisionError):
            self.grpc_client.average_interval(timestamps)

    def test_validate_response_hash_equal(self):
        cache = {"key": "value"}
        new_cache = {"key": "value"}

        result = self.grpc_client.validate_response_hash(cache, new_cache)

        self.assertTrue(result)

    def test_validate_response_hash_not_equal(self):
        cache = {"key": "value"}
        new_cache = {"key": "different_value"}

        result = self.grpc_client.validate_response_hash(cache, new_cache)

        self.assertFalse(result)

    @patch("omni_pro_grpc.grpc_connector.GRPClient.update_cache_cud")
    @patch("omni_pro_grpc.grpc_connector.RedisManager")
    def test_grpc_client_update_cache_cud(self, mock_redis_manager, mock_update_cache):
        mock_redis_instance = MagicMock()
        mock_redis_manager.return_value = mock_redis_instance

        self.grpc_client.redis_cache = mock_redis_instance
        self.grpc_client.update_cache_cud(self.event, MagicMock(), MagicMock())

        mock_update_cache.assert_called_once_with(self.event, ANY, ANY)
        self.assertIs(self.grpc_client.redis_cache, mock_redis_instance)

    @patch("omni_pro_grpc.grpc_connector.MessageToDict")
    @patch("omni_pro_grpc.grpc_connector.format_request")
    def test_request_to_ms(self, mock_format_request, mock_message_to_dict):
        mock_response = MagicMock()
        mock_stub_method = MagicMock(return_value=mock_response)

        mock_stub_class = MagicMock()
        setattr(self.grpc_client.module_grpc, self.stub_classname, mock_stub_class)

        mock_stub_instance = MagicMock()
        setattr(mock_stub_instance, self.rpc_method, mock_stub_method)
        mock_stub_class.return_value = mock_stub_instance

        mock_request = MagicMock()
        mock_format_request.return_value = mock_request

        mock_message_to_dict.return_value = {"response_key": "response_value"}

        result = self.grpc_client.request_to_ms(self.event, self.module_pb2, None, self.channel)

        mock_stub_method.assert_called_once_with(mock_request)

        mock_format_request.assert_called_once_with(self.params, self.request_class, self.module_pb2)

        mock_message_to_dict.assert_called_once_with(mock_response)

        self.assertEqual(result, {"response_key": "response_value"})


if __name__ == "__main__":
    unittest.main()
