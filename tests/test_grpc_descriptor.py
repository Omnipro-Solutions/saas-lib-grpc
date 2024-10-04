import unittest
from unittest.mock import MagicMock, patch

from omni_pro_grpc.grpc_descriptor import OmniServerDescriptor


class TestGrpcDescriptor(unittest.TestCase):

    @patch("omni_pro_grpc.grpc_descriptor.OmniChannel")
    def test_describe_server(self, mock_channel):
        mock_channel.return_value.__enter__.return_value = MagicMock()

        microservice = MagicMock()
        microservice.code = "microservice_code"
        context = {"tenant": "tenant"}

        result = OmniServerDescriptor.describe_server(microservice, context)

        self.assertEqual(result, [])

        mock_channel.assert_called_once_with(
            microservice.code,
            options=[
                ("grpc.max_receive_message_length", 100 * 1024 * 1024),
                ("grpc.max_send_message_length", 100 * 1024 * 1024),
            ],
            tennat=context["tenant"],
        )

    @patch("omni_pro_redis.redis.RedisManager.get_resource_config", return_value={"mock_config": "value"})
    @patch(
        "omni_pro_redis.redis.RedisManager.get_load_balancer_config", return_value={"lb_name": "mocked_load_balancer"}
    )
    @patch("omni_pro_redis.redis.RedisCache.__init__", return_value=None)
    @patch("grpc._channel._UnaryUnaryMultiCallable.__call__", return_value=MagicMock())  # Simulación de llamada gRPC
    @patch("omni_pro_grpc.grpc_descriptor.DescriptorPool")
    @patch("omni_pro_grpc.grpc_descriptor.ProtoReflectionDescriptorDatabase.get_services")
    @patch("omni_pro_grpc.grpc_descriptor.OmniChannel")
    def test_describe_server_resturns_list_services(
        self,
        mock_channel,
        mock_get_services,
        mock_descriptor_pool,
        mock_grpc_call,
        mock_redis_cache_init,
        mock_get_load_balancer_config,
        mock_get_resource_config,
    ):
        mock_redis_cache_instance = MagicMock()
        mock_redis_cache_instance.port = 6379
        mock_redis_cache_instance.host = "localhost"
        mock_redis_cache_instance.db = 0

        mock_redis_cache_init.return_value = None
        with patch("omni_pro_redis.redis.RedisCache", return_value=mock_redis_cache_instance):
            mock_channel.return_value.__enter__.return_value = MagicMock()

            mock_get_services.return_value = ["service1", "service2"]

            mock_service1_desc = MagicMock()
            mock_service1_desc.name = "service1"
            mock_service1_desc.file.name = "service1.proto"

            mock_service2_desc = MagicMock()
            mock_service2_desc.name = "service2"
            mock_service2_desc.file.name = "service2.proto"

            mock_method1 = MagicMock()
            mock_method1.name = "TestMethod1"
            mock_method1.input_type.name = "TestRequest1"
            mock_service1_desc.methods = [mock_method1]

            mock_method2 = MagicMock()
            mock_method2.name = "TestMethod2"
            mock_method2.input_type.name = "TestRequest2"
            mock_service2_desc.methods = [mock_method2]

            mock_descriptor_pool.return_value.FindServiceByName.side_effect = lambda service_name: (
                mock_service1_desc
                if service_name == "service1"
                else (
                    mock_service2_desc
                    if service_name == "service2"
                    else KeyError(f"Couldn't find service {service_name}")
                )
            )

            microservice = MagicMock()
            microservice.code = "microservice_code"
            context = {"tenant": "tenant"}

            result = OmniServerDescriptor.describe_server(microservice, context)

            self.assertIsInstance(result, list)
            self.assertGreater(len(result), 0)

            self.assertTrue(any("service1" in d["info"]["module_pb2"] for d in result))
            self.assertTrue(any("service2" in d["info"]["module_pb2"] for d in result))

            mock_channel.assert_called_once_with(
                microservice.code,
                options=[
                    ("grpc.max_receive_message_length", 100 * 1024 * 1024),
                    ("grpc.max_send_message_length", 100 * 1024 * 1024),
                ],
                tennat=context["tenant"],
            )

            mock_get_services.assert_called_once()

    @patch("omni_pro_grpc.grpc_function.MicroServiceRPCFunction.read_ms")
    @patch("omni_pro_grpc.grpc_descriptor.OmniServerDescriptor.describe_server")
    def test_register(self, mock_describe_server, mock_read_ms):
        mock_microservice = MagicMock()
        mock_read_ms.return_value = [MagicMock(microservices=[mock_microservice])]

        mock_describe_server.return_value = [{"service_name": "test_service"}]

        filters = {"filter_key": "filter_value"}
        context = {"tenant": "test_tenant"}

        result = OmniServerDescriptor.register(filters=filters, context=context)

        mock_describe_server.assert_called_once_with(microservice=mock_microservice, context=context)

        mock_read_ms.assert_called_once_with(params=filters)

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["service_name"], "test_service")

    @patch("omni_pro_redis.redis.RedisManager.get_tenant_codes")
    @patch("omni_pro_redis.redis.RedisManager.get_user_admin")
    @patch("omni_pro_grpc.grpc_function.MicroServiceRPCFunction.read_ms")
    @patch("omni_pro_grpc.grpc_descriptor.OmniServerDescriptor.describe_server")
    @patch("omni_pro_redis.redis.RedisManager.__init__", return_value=None)
    def test_run(self, mock_redis_init, mock_describe_server, mock_read_ms, mock_get_user_admin, mock_get_tenant_codes):
        mock_get_tenant_codes.return_value = ["tenant1", "tenant2"]
        mock_get_user_admin.return_value = {"id": "admin_user"}

        mock_microservice = MagicMock()
        mock_read_ms.return_value = [MagicMock(microservices=[mock_microservice])]

        mock_describe_server.return_value = [{"service_name": "test_service"}]

        result = OmniServerDescriptor.run()

        mock_get_tenant_codes.assert_called_once_with(pattern="*", exlcudes_keys=["SETTINGS"])
        mock_get_user_admin.assert_called()

        mock_read_ms.assert_called_once_with(params={"filter": {}})

        mock_describe_server.assert_called()

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["service_name"], "test_service")


if __name__ == "__main__":
    unittest.main()
