from omni_pro_base.microservice import MicroService
from omni_pro_grpc.grpc_connector import Event, GRPClient


class ModelRPCFucntion(object):
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
        return self.client.call_rpc_fuction(self.event) + (self.event,)


class EventRPCFucntion(object):
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
        self.module_grpc = "v1.utilities.event_pb2_grpc"
        self.stub_classname = "EventServiceStub"
        self.module_pb2 = "v1.utilities.event_pb2"

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
        return self.client.call_rpc_fuction(self.event) + (self.event,)

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
    def __init__(self, context: dict) -> None:
        from omni_pro_base.microservice import MicroService
        from omni_pro_grpc.grpc_connector import Event, GRPClient

        """
        :param context: context with tenant and user\n
        Example:
        ```
        context = {"tenant": "tenant_code", "user": "user_name"}
        ```
        """
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

    def read_webhook(self, params: dict):
        self.event.update(
            dict(
                rpc_method="WebhookRead",
                request_class="WebhookReadRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event) + (self.event,)
