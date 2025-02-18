from dataclasses import dataclass, field

from google.protobuf import json_format
from omni_pro_base.microservice import MicroService
from omni_pro_grpc.grpc_function.base import RPCFuncionBase

__all__ = ["TemplateNotificationRPCFucntion"]


@dataclass(slots=True)
class TemplateNotificationRPCFucntion(RPCFuncionBase):

    service_id: str = field(default=MicroService.SAAS_MS_UTILITIES.value, init=False)
    module_grpc: str = field(default="v1.utilities.template_notification_pb2_grpc", init=False)
    stub_classname: str = field(default="TemplateNotificationServiceStub", init=False)
    module_pb2: str = field(default="v1.utilities.template_notification_pb2", init=False)
    cache: bool = field(default=False, init=False)
    timeout: int = 0

    def template_notification_render(self, params: dict):
        """
        Renders a notification template by sending a request to the RPC server.

        This method constructs an RPC request to render a notification template using the specified
        parameters. It merges the provided parameters with the current context and sends the request
        to the server. The response is then formatted into a dictionary for easy access.

        Args:
            params (dict): A dictionary containing parameters for rendering the notification template.

        Returns:
            dict: A dictionary representation of the RPC response, including all fields
                  (default and non-default) while preserving the original protobuf field names.

        Raises:
            Exception: Propagates any exceptions that occur during the RPC call.
        """
        self.event.update(
            dict(
                rpc_method="TemplateNotificationRender",
                request_class="TemplateNotificationRenderRequest",
                params={"context": self.context} | params,
            )
        )
        response, success, event = self.client.call_rpc_fuction(self.event) + (self.event,)
        return json_format.MessageToDict(
            response, preserving_proto_field_name=True, including_default_value_fields=True
        )
