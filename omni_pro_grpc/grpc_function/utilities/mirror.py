from dataclasses import dataclass, field

from google.protobuf import json_format
from omni_pro_grpc.grpc_function.base import RPCFuncionBase

__all__ = ["MirrorModelRPCFucntion"]


@dataclass(slots=True)
class MirrorModelRPCFucntion(RPCFuncionBase):

    module_grpc: str = field(default="v1.utilities.mirror_model_pb2_grpc", init=False)
    stub_classname: str = field(default="MirrorModelServiceStub", init=False)
    module_pb2: str = field(default="v1.utilities.mirror_model_pb2", init=False)
    cache: bool = field(default=False, init=False)
    micorservice: str
    timeout: int = 0

    def __post_init__(self):
        self.service_id = self.micorservice

    def create(self, params):
        self.event.update(
            dict(
                rpc_method="CreateMirrorModel",
                request_class="CreateOrUpdateMirrorModelRequest",
                params={"context": self.context} | params,
            )
        )
        response, success, event = self.client.call_rpc_fuction(self.event) + (self.event,)
        return json_format.MessageToDict(
            response, preserving_proto_field_name=True, including_default_value_fields=True
        )

    def create_mirror_model(self, params: dict):
        return self.create(params)

    def update(self, params):
        self.event.update(
            dict(
                rpc_method="UpdateMirrorModel",
                request_class="CreateOrUpdateMirrorModelRequest",
                params={"context": self.context} | params,
            )
        )
        response, success, event = self.client.call_rpc_fuction(self.event) + (self.event,)
        return json_format.MessageToDict(
            response, preserving_proto_field_name=True, including_default_value_fields=True
        )

    def updated_model(self, params: dict):
        return self.update(params)

    def multi_update_model(self, params: dict):
        """
        Updates the model with multiple parameters by sending a request to the RPC server.

        This method prepares an RPC request to update or create multiple models in a mirror system
        using the provided parameters. It combines the given parameters with the context and sends
        the request to the server. The response is then formatted into a dictionary for easy access.

        Args:
            params (dict): A dictionary containing the parameters for the update or create operation.

        Returns:
            dict: A dictionary representation of the RPC response, including all fields
                (default and non-default) while preserving the original protobuf field names.

        Raises:
            Exception: Propagates any exceptions that occur during the RPC call.
        """
        self.event.update(
            dict(
                rpc_method="MultiUpdateMirrorModel",
                request_class="MultiCreateOrMultiUpdateMirrorModelRequest",
                params={"context": self.context} | params,
            )
        )
        response, success, event = self.client.call_rpc_fuction(self.event) + (self.event,)
        return json_format.MessageToDict(
            response, preserving_proto_field_name=True, including_default_value_fields=True
        )

    def read(self, params):
        self.event.update(
            dict(
                rpc_method="ReadMirrorModel",
                request_class="ReadMirrorModelRequest",
                params={"context": self.context} | params,
            )
        )
        response, success, event = self.client.call_rpc_fuction(self.event) + (self.event,)
        return json_format.MessageToDict(
            response, preserving_proto_field_name=True, including_default_value_fields=True
        )

    def read_mirror_model(self, params: dict):
        return self.read(params)

    def register_webhook_mirror_model(self, params: dict):
        self.event.update(
            dict(
                rpc_method="RegisterWebhookMirrorModel",
                request_class="RegisterWebhookMirrorModelRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event) + (self.event,)

    def register_method_grpc(self, params: dict):
        self.event.update(
            dict(
                rpc_method="RegisterMethodGrpc",
                request_class="RegisterMethodGrpcRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event) + (self.event,)
