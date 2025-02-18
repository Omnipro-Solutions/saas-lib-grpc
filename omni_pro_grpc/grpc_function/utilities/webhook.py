from dataclasses import dataclass, field

from omni_pro_base.microservice import MicroService
from omni_pro_grpc.grpc_function.base import RPCFuncionBase

__all__ = ["WebhookRPCFucntion"]


@dataclass(slots=True)
class WebhookRPCFucntion(RPCFuncionBase):

    service_id: str = field(default=MicroService.SAAS_MS_UTILITIES.value, init=False)
    module_grpc: str = field(default="v1.utilities.webhook_pb2_grpc", init=False)
    stub_classname: str = field(default="WebhookServiceStub", init=False)
    module_pb2: str = field(default="v1.utilities.webhook_pb2", init=False)

    def create(self, params):
        self.event.update(
            dict(
                rpc_method="WebhookCreate",
                request_class="WebhookCreateRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event) + (self.event,)

    def create_webhook(self, params: dict):
        return self.create(params)

    def update(self, params):
        self.event.update(
            dict(
                rpc_method="WebhookUpdate",
                request_class="WebhookUpdateRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event) + (self.event,)

    def update_webhook(self, params: dict):
        return self.update(params)

    def read(self, params):
        self.event.update(
            dict(
                rpc_method="WebhookRead",
                request_class="WebhookReadRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event, cache=self.cache) + (self.event,)

    def read_webhook(self, params: dict):
        return self.read(params)
