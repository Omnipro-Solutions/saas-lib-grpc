import unittest
from unittest.mock import MagicMock, patch

from omni_pro_grpc.grpc_function import (EventRPCFucntion, MethodRPCFunction,
                                         MicroServiceRPCFunction,
                                         MirrorModelRPCFucntion,
                                         ModelRPCFucntion,
                                         TemplateNotificationRPCFucntion,
                                         WebhookRPCFucntion)


class TestGrpcFunction(unittest.TestCase):

    @patch("omni_pro_grpc.grpc_connector.GRPClient.call_rpc_fuction")
    @patch("omni_pro_grpc.grpc_connector.Event.update")
    @patch(
        "omni_pro_grpc.grpc_connector.GRPClient.__init__", return_value=None
    )  # Evitamos la inicialización real del cliente
    def test_register_model(self, mock_grpc_client_init, mock_event_update, mock_call_rpc_fuction):
        # Simulamos el resultado de la llamada gRPC
        mock_call_rpc_fuction.return_value = ("mock_response", True)

        # Creamos la instancia de ModelRPCFucntion
        context = {"tenant": "tenant_code", "user": "user_name"}
        model_rpc = ModelRPCFucntion(context=context)

        # Definimos los parámetros de prueba
        params = {"model_data": "test_data"}

        # Llamamos al método register_model
        result = model_rpc.register_model(params=params)

        # Verificamos que el evento se haya actualizado correctamente
        expected_event_update = {
            "rpc_method": "ModelCreate",
            "request_class": "ModelCreateRequest",
            "params": {"context": context, "model_data": "test_data"},
        }
        mock_event_update.assert_called_once_with(expected_event_update)

        # Verificamos que call_rpc_fuction fue llamado
        mock_call_rpc_fuction.assert_called_once_with(model_rpc.event)

        # Verificamos el resultado
        self.assertEqual(result[0], "mock_response")
        self.assertTrue(result[1])

    @patch("omni_pro_grpc.grpc_connector.GRPClient.call_rpc_fuction")
    @patch("omni_pro_grpc.grpc_connector.Event.update")
    @patch(
        "omni_pro_grpc.grpc_connector.GRPClient.__init__", return_value=None
    )  # Evitamos la inicialización real del cliente
    def test_updated_model(self, mock_grpc_client_init, mock_event_update, mock_call_rpc_fuction):
        # Simulamos el resultado de la llamada gRPC
        mock_call_rpc_fuction.return_value = ("mock_response", True)

        # Creamos la instancia de ModelRPCFucntion
        context = {"tenant": "tenant_code", "user": "user_name"}
        model_rpc = ModelRPCFucntion(context=context)

        # Definimos los parámetros de prueba
        params = {"model_data": "updated_data"}

        # Llamamos al método updated_model
        result = model_rpc.updated_model(params=params)

        # Verificamos que el evento se haya actualizado correctamente
        expected_event_update = {
            "rpc_method": "ModelUpdate",
            "request_class": "ModelUpdateRequest",
            "params": {"context": context, "model_data": "updated_data"},
        }
        mock_event_update.assert_called_once_with(expected_event_update)

        # Verificamos que call_rpc_fuction fue llamado
        mock_call_rpc_fuction.assert_called_once_with(model_rpc.event)

        # Verificamos el resultado
        self.assertEqual(result[0], "mock_response")
        self.assertTrue(result[1])

    @patch("omni_pro_grpc.grpc_connector.GRPClient.call_rpc_fuction")
    @patch("omni_pro_grpc.grpc_connector.Event.update")
    @patch(
        "omni_pro_grpc.grpc_connector.GRPClient.__init__", return_value=None
    )  # Evitamos la inicialización real del cliente
    def test_read_model(self, mock_grpc_client_init, mock_event_update, mock_call_rpc_fuction):
        # Simulamos el resultado de la llamada gRPC
        mock_call_rpc_fuction.return_value = ("mock_response", True)

        # Creamos la instancia de ModelRPCFucntion
        context = {"tenant": "tenant_code", "user": "user_name"}
        model_rpc = ModelRPCFucntion(context=context, cache=True)

        # Definimos los parámetros de prueba
        params = {"filter_key": "filter_value"}

        # Llamamos al método read_model
        result = model_rpc.read_model(params=params)

        # Verificamos que el evento se haya actualizado correctamente
        expected_event_update = {
            "rpc_method": "ModelRead",
            "request_class": "ModelReadRequest",
            "params": {"context": context, "filter_key": "filter_value"},
        }
        mock_event_update.assert_called_once_with(expected_event_update)

        # Verificamos que call_rpc_fuction fue llamado con el flag cache
        mock_call_rpc_fuction.assert_called_once_with(model_rpc.event, True)

        # Verificamos el resultado
        self.assertEqual(result[0], "mock_response")
        self.assertTrue(result[1])

    @patch("omni_pro_grpc.grpc_connector.GRPClient.call_rpc_fuction")
    @patch("omni_pro_grpc.grpc_connector.Event.update")
    @patch(
        "omni_pro_grpc.grpc_connector.GRPClient.__init__", return_value=None
    )  # Evitamos la inicialización real del cliente
    def test_read_event(self, mock_grpc_client_init, mock_event_update, mock_call_rpc_fuction):
        # Simulamos el resultado de la llamada gRPC
        mock_call_rpc_fuction.return_value = ("mock_response", True)

        # Creamos la instancia de EventRPCFucntion
        context = {"tenant": "tenant_code", "user": "user_name"}
        event_rpc = EventRPCFucntion(context=context, cache=True)

        # Definimos los parámetros de prueba
        params = {"filter_key": "filter_value"}

        # Llamamos al método read_event
        result = event_rpc.read_event(params=params)

        # Verificamos que el evento se haya actualizado correctamente
        expected_event_update = {
            "rpc_method": "EventRead",
            "request_class": "EventReadRequest",
            "params": {"context": context, "filter_key": "filter_value"},
        }
        mock_event_update.assert_called_once_with(expected_event_update)

        # Verificamos que call_rpc_fuction fue llamado con el flag cache
        mock_call_rpc_fuction.assert_called_once_with(event_rpc.event, cache=True)

        # Verificamos el resultado
        self.assertEqual(result[0], "mock_response")
        self.assertTrue(result[1])

    @patch("omni_pro_grpc.grpc_connector.GRPClient.call_rpc_fuction")
    @patch("omni_pro_grpc.grpc_connector.Event.update")
    @patch(
        "omni_pro_grpc.grpc_connector.GRPClient.__init__", return_value=None
    )  # Evitamos la inicialización real del cliente
    def test_register_event(self, mock_grpc_client_init, mock_event_update, mock_call_rpc_fuction):
        # Simulamos el resultado de la llamada gRPC
        mock_call_rpc_fuction.return_value = ("mock_response", True)

        # Creamos la instancia de EventRPCFucntion
        context = {"tenant": "tenant_code", "user": "user_name"}
        event_rpc = EventRPCFucntion(context=context)

        # Definimos los parámetros de prueba
        params = {"event_data": "test_data"}

        # Llamamos al método register_event
        result = event_rpc.register_event(params=params)

        # Verificamos que el evento se haya actualizado correctamente
        expected_event_update = {
            "rpc_method": "EventCreate",
            "request_class": "EventCreateRequest",
            "params": {"context": context, "event_data": "test_data"},
        }
        mock_event_update.assert_called_once_with(expected_event_update)

        # Verificamos que call_rpc_fuction fue llamado
        mock_call_rpc_fuction.assert_called_once_with(event_rpc.event)

        # Verificamos el resultado
        self.assertEqual(result[0], "mock_response")
        self.assertTrue(result[1])

    @patch("omni_pro_grpc.grpc_connector.GRPClient.call_rpc_fuction")
    @patch("omni_pro_grpc.grpc_connector.Event.update")
    @patch(
        "omni_pro_grpc.grpc_connector.GRPClient.__init__", return_value=None
    )  # Evitamos la inicialización real del cliente
    def test_create_webhook(self, mock_grpc_client_init, mock_event_update, mock_call_rpc_fuction):
        # Simulamos el resultado de la llamada gRPC
        mock_call_rpc_fuction.return_value = ("mock_response", True)

        # Creamos la instancia de WebhookRPCFucntion
        context = {"tenant": "tenant_code", "user": "user_name"}
        webhook_rpc = WebhookRPCFucntion(context=context)

        # Definimos los parámetros de prueba
        params = {"webhook_data": "test_data"}

        # Llamamos al método create_webhook
        result = webhook_rpc.create_webhook(params=params)

        # Verificamos que el evento se haya actualizado correctamente
        expected_event_update = {
            "rpc_method": "WebhookCreate",
            "request_class": "WebhookCreateRequest",
            "params": {"context": context, "webhook_data": "test_data"},
        }
        mock_event_update.assert_called_once_with(expected_event_update)

        # Verificamos que call_rpc_fuction fue llamado
        mock_call_rpc_fuction.assert_called_once_with(webhook_rpc.event)

        # Verificamos el resultado
        self.assertEqual(result[0], "mock_response")
        self.assertTrue(result[1])

    @patch("omni_pro_grpc.grpc_connector.GRPClient.call_rpc_fuction")
    @patch("omni_pro_grpc.grpc_connector.Event.update")
    @patch(
        "omni_pro_grpc.grpc_connector.GRPClient.__init__", return_value=None
    )  # Evitamos la inicialización real del cliente
    def test_update_webhook(self, mock_grpc_client_init, mock_event_update, mock_call_rpc_fuction):
        # Simulamos el resultado de la llamada gRPC
        mock_call_rpc_fuction.return_value = ("mock_response", True)

        # Creamos la instancia de WebhookRPCFucntion
        context = {"tenant": "tenant_code", "user": "user_name"}
        webhook_rpc = WebhookRPCFucntion(context=context)

        # Definimos los parámetros de prueba
        params = {"webhook_data": "updated_data"}

        # Llamamos al método update_webhook
        result = webhook_rpc.update_webhook(params=params)

        # Verificamos que el evento se haya actualizado correctamente
        expected_event_update = {
            "rpc_method": "WebhookUpdate",
            "request_class": "WebhookUpdateRequest",
            "params": {"context": context, "webhook_data": "updated_data"},
        }
        mock_event_update.assert_called_once_with(expected_event_update)

        # Verificamos que call_rpc_fuction fue llamado
        mock_call_rpc_fuction.assert_called_once_with(webhook_rpc.event)

        # Verificamos el resultado
        self.assertEqual(result[0], "mock_response")
        self.assertTrue(result[1])

    @patch("omni_pro_grpc.grpc_connector.GRPClient.call_rpc_fuction")
    @patch("omni_pro_grpc.grpc_connector.Event.update")
    @patch(
        "omni_pro_grpc.grpc_connector.GRPClient.__init__", return_value=None
    )  # Evitamos la inicialización real del cliente
    def test_read_webhook(self, mock_grpc_client_init, mock_event_update, mock_call_rpc_fuction):
        # Simulamos el resultado de la llamada gRPC
        mock_call_rpc_fuction.return_value = ("mock_response", True)

        # Creamos la instancia de WebhookRPCFucntion
        context = {"tenant": "tenant_code", "user": "user_name"}
        webhook_rpc = WebhookRPCFucntion(context=context, cache=True)

        # Definimos los parámetros de prueba
        params = {"filter_key": "filter_value"}

        # Llamamos al método read_webhook
        result = webhook_rpc.read_webhook(params=params)

        # Verificamos que el evento se haya actualizado correctamente
        expected_event_update = {
            "rpc_method": "WebhookRead",
            "request_class": "WebhookReadRequest",
            "params": {"context": context, "filter_key": "filter_value"},
        }
        mock_event_update.assert_called_once_with(expected_event_update)

        # Verificamos que call_rpc_fuction fue llamado con el flag cache
        mock_call_rpc_fuction.assert_called_once_with(webhook_rpc.event, cache=True)

        # Verificamos el resultado
        self.assertEqual(result[0], "mock_response")
        self.assertTrue(result[1])

    @patch("omni_pro_grpc.grpc_connector.GRPClient.call_rpc_fuction")
    @patch("omni_pro_grpc.grpc_connector.Event.update")
    @patch(
        "omni_pro_grpc.grpc_connector.GRPClient.__init__", return_value=None
    )  # Evitamos la inicialización real del cliente
    def test_read_method_rpc(self, mock_grpc_client_init, mock_event_update, mock_call_rpc_fuction):
        # Simulamos el resultado de la llamada gRPC
        mock_call_rpc_fuction.return_value = ("mock_response", True)

        # Creamos la instancia de MethodRPCFunction
        context = {"tenant": "tenant_code", "user": "user_name"}
        method_rpc = MethodRPCFunction(context=context)

        # Definimos los parámetros de prueba
        params = {"filter_key": "filter_value"}

        # Llamamos al método read_method_rpc
        result = method_rpc.read_method_rpc(params=params)

        # Verificamos que el evento se haya actualizado correctamente
        expected_event_update = {
            "rpc_method": "MethodGrpcRead",
            "request_class": "MethodGrpcReadRequest",
            "params": {"context": context, "filter_key": "filter_value"},
        }
        mock_event_update.assert_called_once_with(expected_event_update)

        # Verificamos que call_rpc_fuction fue llamado
        mock_call_rpc_fuction.assert_called_once_with(method_rpc.event)

        # Verificamos el resultado
        self.assertEqual(result[0], "mock_response")
        self.assertTrue(result[1])

    @patch("omni_pro_grpc.grpc_connector.GRPClient.call_rpc_fuction")
    @patch("omni_pro_grpc.grpc_connector.Event.update")
    @patch(
        "omni_pro_grpc.grpc_connector.GRPClient.__init__", return_value=None
    )  # Evitamos la inicialización real del cliente
    def test_create_method_rpc(self, mock_grpc_client_init, mock_event_update, mock_call_rpc_fuction):
        # Simulamos el resultado de la llamada gRPC
        mock_call_rpc_fuction.return_value = ("mock_response", True)

        # Creamos la instancia de MethodRPCFunction
        context = {"tenant": "tenant_code", "user": "user_name"}
        method_rpc = MethodRPCFunction(context=context)

        # Definimos los parámetros de prueba
        params = {"method_data": "test_data"}

        # Llamamos al método create_method_rpc
        result = method_rpc.create_method_rpc(params=params)

        # Verificamos que el evento se haya actualizado correctamente
        expected_event_update = {
            "rpc_method": "MethodGrpcCreate",
            "request_class": "MethodGrpcCreateRequest",
            "params": {"context": context, "method_data": "test_data"},
        }
        mock_event_update.assert_called_once_with(expected_event_update)

        # Verificamos que call_rpc_fuction fue llamado
        mock_call_rpc_fuction.assert_called_once_with(method_rpc.event)

        # Verificamos el resultado
        self.assertEqual(result[0], "mock_response")
        self.assertTrue(result[1])

    @patch("omni_pro_grpc.grpc_connector.GRPClient.call_rpc_fuction")
    @patch("omni_pro_grpc.grpc_connector.Event.update")
    @patch(
        "omni_pro_grpc.grpc_connector.GRPClient.__init__", return_value=None
    )  # Evitamos la inicialización real del cliente
    def test_update_method_rpc(self, mock_grpc_client_init, mock_event_update, mock_call_rpc_fuction):
        # Simulamos el resultado de la llamada gRPC
        mock_call_rpc_fuction.return_value = ("mock_response", True)

        # Creamos la instancia de MethodRPCFunction
        context = {"tenant": "tenant_code", "user": "user_name"}
        method_rpc = MethodRPCFunction(context=context)

        # Definimos los parámetros de prueba
        params = {"method_data": "updated_data"}

        # Llamamos al método update_method_rpc
        result = method_rpc.update_method_rpc(params=params)

        # Verificamos que el evento se haya actualizado correctamente
        expected_event_update = {
            "rpc_method": "MethodGrpcUpdate",
            "request_class": "MethodGrpcUpdateRequest",
            "params": {"context": context, "method_data": "updated_data"},
        }
        mock_event_update.assert_called_once_with(expected_event_update)

        # Verificamos que call_rpc_fuction fue llamado
        mock_call_rpc_fuction.assert_called_once_with(method_rpc.event)

        # Verificamos el resultado
        self.assertEqual(result[0], "mock_response")
        self.assertTrue(result[1])

    @patch("omni_pro_grpc.grpc_connector.GRPClient.call_rpc_fuction")
    @patch("omni_pro_grpc.grpc_connector.Event.update")
    @patch("omni_pro_base.util.generate_hash")
    @patch(
        "omni_pro_grpc.grpc_connector.GRPClient.__init__", return_value=None
    )  # Evitamos la inicialización real del cliente
    def test_create_or_update(
        self, mock_grpc_client_init, mock_generate_hash, mock_event_update, mock_call_rpc_fuction
    ):
        # Creamos un objeto simulando una respuesta válida para read_method_rpc
        method_grpc_mock = MagicMock()
        method_grpc_mock.name = "test_method"
        method_grpc_mock.code = "test_code"
        method_grpc_mock.module_grpc = "module_grpc"
        method_grpc_mock.class_name = "class_name"
        method_grpc_mock.module_pb2 = "module_pb2"
        method_grpc_mock.microservice.id = "microservice_id"
        method_grpc_mock.method = "method_name"
        method_grpc_mock.request = "request_class"

        # Simulamos la respuesta de read_method_rpc
        mock_call_rpc_fuction.side_effect = [
            (MagicMock(method_grpcs=[method_grpc_mock]), True),  # Respuesta de read_method_rpc
            ("mock_response", True),  # Respuesta de create_method_rpc/update_method_rpc
        ]

        # Simulamos el resultado de generate_hash
        mock_generate_hash.side_effect = ["hash_code_1", "hash_code_2"]  # Diferentes para testear el hash

        # Creamos la instancia de MethodRPCFunction
        context = {"tenant": "tenant_code", "user": "user_name"}
        method_rpc = MethodRPCFunction(context=context)

        # Definimos los parámetros de prueba
        params = {
            "filter": {"filter_key": "filter_value"},
            "data": {"name": "new_name", "code": "new_code", "microservice_id": "1234"},
        }

        # Llamamos al método create_or_update
        result = method_rpc.create_or_update(params=params)

        # Verificamos que el evento se haya actualizado correctamente para read_method_rpc
        mock_event_update.assert_any_call(
            {
                "rpc_method": "MethodGrpcRead",
                "request_class": "MethodGrpcReadRequest",
                "params": {"context": context, "filter_key": "filter_value"},
            }
        )

        # Verificamos que call_rpc_fuction fue llamado correctamente dos veces (para lectura y creación/actualización)
        self.assertEqual(mock_call_rpc_fuction.call_count, 2)

        # Verificamos el resultado de create_or_update
        self.assertEqual(result[0], "mock_response")
        self.assertTrue(result[1])

    @patch("omni_pro_grpc.grpc_connector.GRPClient.call_rpc_fuction")
    @patch("omni_pro_grpc.grpc_connector.Event.update")
    @patch(
        "omni_pro_grpc.grpc_connector.GRPClient.__init__", return_value=None
    )  # Evitamos la inicialización real del cliente
    def test_read_ms(self, mock_grpc_client_init, mock_event_update, mock_call_rpc_fuction):
        # Simulamos el resultado de la llamada gRPC
        mock_call_rpc_fuction.return_value = ("mock_response", True)

        # Creamos la instancia de MicroServiceRPCFunction
        context = {"tenant": "tenant_code", "user": "user_name"}
        ms_rpc = MicroServiceRPCFunction(context=context)

        # Definimos los parámetros de prueba
        params = {"filter_key": "filter_value"}

        # Llamamos al método read_ms
        result = ms_rpc.read_ms(params=params)

        # Verificamos que el evento se haya actualizado correctamente
        expected_event_update = {
            "rpc_method": "MicroserviceRead",
            "request_class": "MicroserviceReadRequest",
            "params": {"context": context, "filter_key": "filter_value"},
        }
        mock_event_update.assert_called_once_with(expected_event_update)

        # Verificamos que call_rpc_fuction fue llamado correctamente
        mock_call_rpc_fuction.assert_called_once_with(ms_rpc.event)

        # Verificamos el resultado
        self.assertEqual(result[0], "mock_response")
        self.assertTrue(result[1])

    @patch("omni_pro_grpc.grpc_connector.GRPClient.call_rpc_fuction")
    @patch("omni_pro_grpc.grpc_connector.Event.update")
    @patch(
        "omni_pro_grpc.grpc_connector.GRPClient.__init__", return_value=None
    )  # Evitamos la inicialización real del cliente
    def test_create_mirror_model(self, mock_grpc_client_init, mock_event_update, mock_call_rpc_fuction):
        # Simulamos un objeto protobuf con el atributo DESCRIPTOR
        mock_protobuf_response = MagicMock()
        mock_protobuf_response.DESCRIPTOR = MagicMock()

        # Simulamos el resultado de la llamada gRPC
        mock_call_rpc_fuction.return_value = (mock_protobuf_response, True)

        # Creamos la instancia de MirrorModelRPCFunction
        context = {"tenant": "tenant_code", "user": "user_name"}
        mirror_rpc = MirrorModelRPCFucntion(context=context, micorservice="test_service")

        # Definimos los parámetros de prueba
        params = {"model_data": "multi_update_data"}

        # Llamamos al método multi_update_model
        result = mirror_rpc.multi_update_model(params=params)

        # Verificamos que el evento se haya actualizado correctamente
        expected_event_update = {
            "rpc_method": "MultiUpdateMirrorModel",
            "request_class": "MultiCreateOrMultiUpdateMirrorModelRequest",
            "params": {"context": context, "model_data": "multi_update_data"},
        }
        mock_event_update.assert_called_once_with(expected_event_update)

        # Verificamos que call_rpc_fuction fue llamado correctamente
        mock_call_rpc_fuction.assert_called_once_with(mirror_rpc.event)

        # Verificamos que el resultado es un diccionario generado a partir del protobuf
        self.assertIsInstance(result, dict)

    @patch("omni_pro_grpc.grpc_connector.GRPClient.call_rpc_fuction")
    @patch("omni_pro_grpc.grpc_connector.Event.update")
    @patch(
        "omni_pro_grpc.grpc_connector.GRPClient.__init__", return_value=None
    )  # Evitamos la inicialización real del cliente
    def test_updated_model(self, mock_grpc_client_init, mock_event_update, mock_call_rpc_fuction):
        # Simulamos un objeto protobuf con el atributo DESCRIPTOR
        mock_protobuf_response = MagicMock()
        mock_protobuf_response.DESCRIPTOR = MagicMock()

        # Simulamos el resultado de la llamada gRPC
        mock_call_rpc_fuction.return_value = (mock_protobuf_response, True)

        # Creamos la instancia de MirrorModelRPCFunction
        context = {"tenant": "tenant_code", "user": "user_name"}
        mirror_rpc = MirrorModelRPCFucntion(context=context, micorservice="test_service")

        # Definimos los parámetros de prueba
        params = {"model_data": "updated_data"}

        # Llamamos al método updated_model
        result = mirror_rpc.updated_model(params=params)

        # Verificamos que el evento se haya actualizado correctamente
        expected_event_update = {
            "rpc_method": "UpdateMirrorModel",
            "request_class": "CreateOrUpdateMirrorModelRequest",
            "params": {"context": context, "model_data": "updated_data"},
        }
        mock_event_update.assert_called_once_with(expected_event_update)

        # Verificamos que call_rpc_fuction fue llamado correctamente
        mock_call_rpc_fuction.assert_called_once_with(mirror_rpc.event)

        # Verificamos que el resultado es un diccionario generado a partir del protobuf
        self.assertIsInstance(result, dict)

    @patch("omni_pro_grpc.grpc_connector.GRPClient.call_rpc_fuction")
    @patch("omni_pro_grpc.grpc_connector.Event.update")
    @patch(
        "omni_pro_grpc.grpc_connector.GRPClient.__init__", return_value=None
    )  # Evitamos la inicialización real del cliente
    def test_multi_update_model(self, mock_grpc_client_init, mock_event_update, mock_call_rpc_fuction):
        # Simulamos el resultado de la llamada gRPC
        mock_protobuf_response = MagicMock()
        mock_protobuf_response.DESCRIPTOR = MagicMock()

        mock_call_rpc_fuction.return_value = (mock_protobuf_response, True)

        # Creamos la instancia de MirrorModelRPCFunction
        context = {"tenant": "tenant_code", "user": "user_name"}
        mirror_rpc = MirrorModelRPCFucntion(context=context, micorservice="test_service")

        # Definimos los parámetros de prueba
        params = {"model_data": "multi_update_data"}

        # Llamamos al método multi_update_model
        result = mirror_rpc.multi_update_model(params=params)

        # Verificamos que el evento se haya actualizado correctamente
        expected_event_update = {
            "rpc_method": "MultiUpdateMirrorModel",
            "request_class": "MultiCreateOrMultiUpdateMirrorModelRequest",
            "params": {"context": context, "model_data": "multi_update_data"},
        }
        mock_event_update.assert_called_once_with(expected_event_update)

        # Verificamos que call_rpc_fuction fue llamado correctamente
        mock_call_rpc_fuction.assert_called_once_with(mirror_rpc.event)

        # Verificamos el resultado
        self.assertIsInstance(result, dict)

    @patch("omni_pro_grpc.grpc_connector.GRPClient.call_rpc_fuction")
    @patch("omni_pro_grpc.grpc_connector.Event.update")
    @patch(
        "omni_pro_grpc.grpc_connector.GRPClient.__init__", return_value=None
    )  # Evitamos la inicialización real del cliente
    def test_read_mirror_model(self, mock_grpc_client_init, mock_event_update, mock_call_rpc_fuction):
        # Simulamos el resultado de la llamada gRPC
        mock_protobuf_response = MagicMock()
        mock_protobuf_response.DESCRIPTOR = MagicMock()

        mock_call_rpc_fuction.return_value = (mock_protobuf_response, True)

        # Creamos la instancia de MirrorModelRPCFunction
        context = {"tenant": "tenant_code", "user": "user_name"}
        mirror_rpc = MirrorModelRPCFucntion(context=context, micorservice="test_service")

        # Definimos los parámetros de prueba
        params = {"model_filter": "filter_value"}

        # Llamamos al método read_mirror_model
        result = mirror_rpc.read_mirror_model(params=params)

        # Verificamos que el evento se haya actualizado correctamente
        expected_event_update = {
            "rpc_method": "ReadMirrorModel",
            "request_class": "ReadMirrorModelRequest",
            "params": {"context": context, "model_filter": "filter_value"},
        }
        mock_event_update.assert_called_once_with(expected_event_update)

        # Verificamos que call_rpc_fuction fue llamado correctamente
        mock_call_rpc_fuction.assert_called_once_with(mirror_rpc.event)

        # Verificamos el resultado
        self.assertIsInstance(result, dict)

    @patch("omni_pro_grpc.grpc_connector.GRPClient.call_rpc_fuction")
    @patch("omni_pro_grpc.grpc_connector.Event.update")
    @patch(
        "omni_pro_grpc.grpc_connector.GRPClient.__init__", return_value=None
    )  # Evitamos la inicialización real del cliente
    def test_register_webhook_mirror_model(self, mock_grpc_client_init, mock_event_update, mock_call_rpc_fuction):
        # Simulamos el resultado de la llamada gRPC
        mock_protobuf_response = MagicMock()
        mock_protobuf_response.DESCRIPTOR = MagicMock()

        mock_call_rpc_fuction.return_value = ("mock_response", True)

        # Creamos la instancia de MirrorModelRPCFunction
        context = {"tenant": "tenant_code", "user": "user_name"}
        mirror_rpc = MirrorModelRPCFucntion(context=context, micorservice="test_service")

        # Definimos los parámetros de prueba
        params = {"webhook_data": "test_webhook"}

        # Llamamos al método register_webhook_mirror_model
        result = mirror_rpc.register_webhook_mirror_model(params=params)

        # Verificamos que el evento se haya actualizado correctamente
        expected_event_update = {
            "rpc_method": "RegisterWebhookMirrorModel",
            "request_class": "RegisterWebhookMirrorModelRequest",
            "params": {"context": context, "webhook_data": "test_webhook"},
        }
        mock_event_update.assert_called_once_with(expected_event_update)

        # Verificamos que call_rpc_fuction fue llamado correctamente
        mock_call_rpc_fuction.assert_called_once_with(mirror_rpc.event)

        # Verificamos el resultado
        self.assertEqual(result[0], "mock_response")

    @patch("omni_pro_grpc.grpc_connector.GRPClient.call_rpc_fuction")
    @patch("omni_pro_grpc.grpc_connector.Event.update")
    @patch(
        "omni_pro_grpc.grpc_connector.GRPClient.__init__", return_value=None
    )  # Evitamos la inicialización real del cliente
    def test_register_method_grpc(self, mock_grpc_client_init, mock_event_update, mock_call_rpc_fuction):
        # Simulamos el resultado de la llamada gRPC
        mock_protobuf_response = MagicMock()
        mock_protobuf_response.DESCRIPTOR = MagicMock()

        mock_call_rpc_fuction.return_value = ("mock_response", True)

        # Creamos la instancia de MirrorModelRPCFunction
        context = {"tenant": "tenant_code", "user": "user_name"}
        mirror_rpc = MirrorModelRPCFucntion(context=context, micorservice="test_service")

        # Definimos los parámetros de prueba
        params = {"grpc_data": "grpc_method_data"}

        # Llamamos al método register_method_grpc
        result = mirror_rpc.register_method_grpc(params=params)

        # Verificamos que el evento se haya actualizado correctamente
        expected_event_update = {
            "rpc_method": "RegisterMethodGrpc",
            "request_class": "RegisterMethodGrpcRequest",
            "params": {"context": context, "grpc_data": "grpc_method_data"},
        }
        mock_event_update.assert_called_once_with(expected_event_update)

        # Verificamos que call_rpc_fuction fue llamado correctamente
        mock_call_rpc_fuction.assert_called_once_with(mirror_rpc.event)

        # Verificamos el resultado
        self.assertEqual(result[0], "mock_response")

    @patch("omni_pro_grpc.grpc_connector.GRPClient.call_rpc_fuction")
    @patch("omni_pro_grpc.grpc_connector.Event.update")
    @patch(
        "omni_pro_grpc.grpc_connector.GRPClient.__init__", return_value=None
    )  # Evitamos la inicialización real del cliente
    def test_template_notification_render(self, mock_grpc_client_init, mock_event_update, mock_call_rpc_fuction):
        # Simulamos un objeto protobuf con el atributo DESCRIPTOR
        mock_protobuf_response = MagicMock()
        mock_protobuf_response.DESCRIPTOR = MagicMock()

        # Simulamos el resultado de la llamada gRPC
        mock_call_rpc_fuction.return_value = (mock_protobuf_response, True)

        # Creamos la instancia de TemplateNotificationRPCFunction
        context = {"tenant": "tenant_code", "user": "user_name"}
        template_rpc = TemplateNotificationRPCFucntion(context=context, timeout=5)

        # Definimos los parámetros de prueba
        params = {"template_id": "123", "notification_data": {"key": "value"}}

        # Llamamos al método template_notification_render
        result = template_rpc.template_notification_render(params=params)

        # Verificamos que el evento se haya actualizado correctamente
        expected_event_update = {
            "rpc_method": "TemplateNotificationRender",
            "request_class": "TemplateNotificationRenderRequest",
            "params": {"context": context, "template_id": "123", "notification_data": {"key": "value"}},
        }
        mock_event_update.assert_called_once_with(expected_event_update)

        # Verificamos que call_rpc_fuction fue llamado correctamente
        mock_call_rpc_fuction.assert_called_once_with(template_rpc.event)

        # Verificamos que el resultado es un diccionario generado a partir del protobuf
        self.assertIsInstance(result, dict)

if __name__ == "__main__":
    unittest.main()