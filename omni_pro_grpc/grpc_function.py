from google.protobuf import json_format
from omni_pro_base.microservice import MicroService
from omni_pro_base.util import generate_hash
from omni_pro_grpc.grpc_connector import Event, GRPClient


class ModelRPCFucntion(object):
    def __init__(self, context: dict, cache: bool = False) -> None:
        """
        :param context: context with tenant and user\n
        Example:
        ```
        context = {"tenant": "tenant_code", "user": "user_name"}
        ```
        """
        self.context = context
        self.cache = cache
        self.service_id = MicroService.SAAS_MS_UTILITIES.value
        self.module_grpc = "v1.utilities.model_pb2_grpc"
        self.stub_classname = "ModelsServiceStub"
        self.module_pb2 = "v1.utilities.model_pb2"

        self.event: Event = Event(
            module_grpc=self.module_grpc,
            stub_classname=self.stub_classname,
            module_pb2=self.module_pb2,
            rpc_method=None,
            request_class=None,
        )

        self.client: GRPClient = GRPClient(self.service_id)

    def register_model(self, params: dict):
        self.event.update(
            dict(
                rpc_method="ModelCreate",
                request_class="ModelCreateRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event) + (self.event,)

    def updated_model(self, params: dict):
        self.event.update(
            dict(
                rpc_method="ModelUpdate",
                request_class="ModelUpdateRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event) + (self.event,)

    def read_model(self, params: dict):
        self.event.update(
            dict(
                rpc_method="ModelRead",
                request_class="ModelReadRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event, self.cache) + (self.event,)


class EventRPCFucntion(object):
    def __init__(self, context: dict, cache: bool = False) -> None:
        """
        :param context: context with tenant and user\n
        Example:
        ```
        context = {"tenant": "tenant_code", "user": "user_name"}
        ```
        """
        self.context = context
        self.service_id = MicroService.SAAS_MS_UTILITIES.value
        self.module_grpc = "v1.utilities.event_pb2_grpc"
        self.stub_classname = "EventServiceStub"
        self.module_pb2 = "v1.utilities.event_pb2"
        self.cache = cache

        self.event: Event = Event(
            module_grpc=self.module_grpc,
            stub_classname=self.stub_classname,
            module_pb2=self.module_pb2,
            rpc_method=None,
            request_class=None,
        )

        self.client: GRPClient = GRPClient(self.service_id)

    def read_event(self, params: dict):
        self.event.update(
            dict(
                rpc_method="EventRead",
                request_class="EventReadRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event, cache=self.cache) + (self.event,)

    def register_event(self, params: dict):
        self.event.update(
            dict(
                rpc_method="EventCreate",
                request_class="EventCreateRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event) + (self.event,)


class WebhookRPCFucntion(object):

    def __init__(self, context: dict, cache: bool = False) -> None:
        """
        :param context: context with tenant and user\n
        Example:
        ```
        context = {"tenant": "tenant_code", "user": "user_name"}
        ```
        """
        self.cache = cache
        self.context = context
        self.service_id = MicroService.SAAS_MS_UTILITIES.value
        self.module_grpc = "v1.utilities.webhook_pb2_grpc"
        self.stub_classname = "WebhookServiceStub"
        self.module_pb2 = "v1.utilities.webhook_pb2"

        self.event: Event = Event(
            module_grpc=self.module_grpc,
            stub_classname=self.stub_classname,
            module_pb2=self.module_pb2,
            rpc_method=None,
            request_class=None,
        )

        self.client: GRPClient = GRPClient(self.service_id)

    def create_webhook(self, params: dict):
        self.event.update(
            dict(
                rpc_method="WebhookCreate",
                request_class="WebhookCreateRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event) + (self.event,)

    def update_webhook(self, params: dict):
        self.event.update(
            dict(
                rpc_method="WebhookUpdate",
                request_class="WebhookUpdateRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event) + (self.event,)

    def read_webhook(self, params: dict):
        self.event.update(
            dict(
                rpc_method="WebhookRead",
                request_class="WebhookReadRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event, cache=self.cache) + (self.event,)


class MethodRPCFunction(object):
    def __init__(self, context: dict) -> None:
        """
        :param context: context with tenant and user\n
        Example:
        ```
        context = {"tenant": "tenant_code", "user": "user_name"}
        ```
        """
        self.context = context
        self.service_id = MicroService.SAAS_MS_UTILITIES.value
        self.module_grpc = "v1.utilities.method_grpc_pb2_grpc"
        self.stub_classname = "MethodGrpcServiceStub"
        self.module_pb2 = "v1.utilities.method_grpc_pb2"

        self.event: Event = Event(
            module_grpc=self.module_grpc,
            stub_classname=self.stub_classname,
            module_pb2=self.module_pb2,
            rpc_method=None,
            request_class=None,
        )

        self.client: GRPClient = GRPClient(self.service_id)

    def read_method_rpc(self, params: dict):
        self.event.update(
            dict(
                rpc_method="MethodGrpcRead",
                request_class="MethodGrpcReadRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event) + (self.event,)

    def create_method_rpc(self, params: dict):
        self.event.update(
            dict(
                rpc_method="MethodGrpcCreate",
                request_class="MethodGrpcCreateRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event) + (self.event,)

    def update_method_rpc(self, params: dict):
        self.event.update(
            dict(
                rpc_method="MethodGrpcUpdate",
                request_class="MethodGrpcUpdateRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event) + (self.event,)

    def create_or_update(self, params: dict):
        filters = params.pop("filter", {})
        resp, success, _e = self.read_method_rpc(filters)
        if success:
            data = params.pop("data")
            if resp.method_grpcs:
                method_rpc = resp.method_grpcs[0]
                data_rpc = {
                    "name": method_rpc.name,
                    "code": method_rpc.code,
                    "module_grpc": method_rpc.module_grpc,
                    "class_name": method_rpc.class_name,
                    "module_pb2": method_rpc.module_pb2,
                    "microservice_id": str(method_rpc.microservice.id),
                    "method": method_rpc.method,
                    "request": method_rpc.request,
                }
                hash_code = generate_hash(data_rpc)
                hash_code_data = generate_hash(data)
                if hash_code == hash_code_data:
                    return type("Response", (object,), {"method_grpc": method_rpc})(), success, _e
                data["microservice"] = {"id": data.pop("microservice_id", None)}
                return self.update_method_rpc({"method_grpc": data | {"id": method_rpc.id}})
            else:
                return self.create_method_rpc(data)
        return resp, success, _e


class MicroServiceRPCFunction(object):

    def __init__(self, context: dict) -> None:
        """
        :param context: context with tenant and user\n
        Example:
        ```
        context = {"tenant": "tenant_code", "user": "user_name"}
        ```
        """
        self.context = context
        self.service_id = MicroService.SAAS_MS_UTILITIES.value
        self.module_grpc = "v1.utilities.ms_pb2_grpc"
        self.stub_classname = "MicroserviceServiceStub"
        self.module_pb2 = "v1.utilities.ms_pb2"

        self.event: Event = Event(
            module_grpc=self.module_grpc,
            stub_classname=self.stub_classname,
            module_pb2=self.module_pb2,
            rpc_method=None,
            request_class=None,
        )

        self.client: GRPClient = GRPClient(self.service_id)

    def read_ms(self, params: dict):
        self.event.update(
            dict(
                rpc_method="MicroserviceRead",
                request_class="MicroserviceReadRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event) + (self.event,)


class MirrorModelRPCFucntion(object):
    def __init__(self, context: dict, micorservice: str, timeout: float = 0) -> None:
        """
        :param context: context with tenant and user\n
        Example:
        ```
        context = {"tenant": "tenant_code", "user": "user_name"}
        ```
        """
        self.context = context
        self.service_id = micorservice
        self.module_grpc = "v1.utilities.mirror_model_pb2_grpc"
        self.stub_classname = "MirrorModelServiceStub"
        self.module_pb2 = "v1.utilities.mirror_model_pb2"
        self.timeout = timeout

        self.event: Event = Event(
            module_grpc=self.module_grpc,
            stub_classname=self.stub_classname,
            module_pb2=self.module_pb2,
            rpc_method=None,
            request_class=None,
        )

        self.client: GRPClient = GRPClient(self.service_id, self.timeout)

    def create_mirror_model(self, params: dict):
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

    def updated_model(self, params: dict):
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

    def read_mirror_model(self, params: dict):
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


class TemplateNotificationRPCFucntion(object):
    def __init__(self, context: dict, timeout: float = 0) -> None:
        """
        :param context: context with tenant and user\n
        Example:
        ```
        context = {"tenant": "tenant_code", "user": "user_name"}
        ```
        """
        self.context = context
        self.service_id = MicroService.SAAS_MS_UTILITIES.value
        self.module_grpc = "v1.utilities.template_notification_pb2_grpc"
        self.stub_classname = "TemplateNotificationServiceStub"
        self.module_pb2 = "v1.utilities.template_notification_pb2"
        self.timeout = timeout

        self.event: Event = Event(
            module_grpc=self.module_grpc,
            stub_classname=self.stub_classname,
            module_pb2=self.module_pb2,
            rpc_method=None,
            request_class=None,
        )

        self.client: GRPClient = GRPClient(self.service_id, self.timeout)

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


class UserRPCFunction(object):

    def __init__(self, context: dict, cache: bool = False) -> None:
        """
        :param context: context with tenant and user\n
        Example:
        ```
        context = {"tenant": "tenant_code", "user": "user_name"}
        ```
        """
        self.context = context
        self.cache = cache
        self.service_id = MicroService.SAAS_MS_USER.value
        self.module_grpc = "v1.users.user_pb2_grpc"
        self.stub_classname = "UsersServiceStub"
        self.module_pb2 = "v1.users.user_pb2"

        self.event: Event = Event(
            module_grpc=self.module_grpc,
            stub_classname=self.stub_classname,
            module_pb2=self.module_pb2,
            rpc_method=None,
            request_class=None,
        )

        self.client: GRPClient = GRPClient(self.service_id)

    def create_action(self, params: dict):
        self.event.update(
            dict(
                rpc_method="ActionCreate",
                request_class="ActionCreateRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event) + (self.event,)
