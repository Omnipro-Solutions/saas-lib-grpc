import importlib
import unittest
from datetime import datetime
from unittest.mock import MagicMock, patch

from google.protobuf import struct_pb2
from omni_pro_grpc.util import MessageToDict, format_datetime_to_iso, format_request, model_to_proto, to_value


class TestUtil(unittest.TestCase):

    def test_message_to_dict(self):
        # Simular un mensaje Protobuf
        message = MagicMock()
        message.DESCRIPTOR = MagicMock()  # Para simular que es un objeto Protobuf

        # Simular el resultado de MessageToDict
        result = MessageToDict(message, default_values=True)
        self.assertIsInstance(result, dict)

    @patch("google.protobuf.json_format.ParseDict")
    def test_format_request(self, mock_parse_dict):
        # Crear un diccionario simulado para datos
        data = {"field1": "value1", "field2": 2}

        # Crear una estructura proto simulada
        proto = MagicMock()

        # Simular la estructura interna de Protobuf
        mock_request = MagicMock()
        proto.TestRequest.return_value = mock_request

        # Establecer el comportamiento de json_format.ParseDict
        mock_parse_dict.return_value = mock_request

        # Llamar a format_request
        result = format_request(data, "TestRequest", proto)

        # Verificar que ParseDict fue llamado correctamente
        mock_parse_dict.assert_called_once_with(data, mock_request)

        # Verificar que el resultado es el esperado
        self.assertEqual(result, mock_request)

    def test_to_value_dict(self):
        data = {"_id": "123", "name": "test"}
        expected_value = struct_pb2.Value()
        result = to_value(data)
        self.assertIsInstance(result, struct_pb2.Value)
        self.assertIn("id", result.struct_value.fields)

    def test_to_value_list(self):
        data = [1, 2, 3]
        result = to_value(data)
        self.assertIsInstance(result, struct_pb2.Value)
        self.assertIsInstance(result.list_value, struct_pb2.ListValue)

    def test_format_datetime_to_iso(self):
        dt = datetime(2023, 8, 22, 14, 30, 0)
        formatted = format_datetime_to_iso(dt)
        self.assertEqual(formatted, "2023-08-22T14:30:00Z")

    def test_model_to_proto(self):
        class TestModel:
            field1 = "value1"
            field2 = "value2"

        model = TestModel()
        fields = ["field1", "field2"]
        proto = MagicMock()

        # Simular la importación dinámica del proto
        with unittest.mock.patch("importlib.import_module") as mock_import_module:
            mock_import_module.return_value = MagicMock()
            result = model_to_proto(model, fields, serialize_proto="test_module.TestProto")
            self.assertTrue(mock_import_module.called)
            self.assertIsInstance(result, MagicMock)


if __name__ == "__main__":
    unittest.main()
