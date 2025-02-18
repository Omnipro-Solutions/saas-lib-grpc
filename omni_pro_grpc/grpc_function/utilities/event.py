from dataclasses import dataclass, field

from omni_pro_base.microservice import MicroService
from omni_pro_grpc.grpc_function.base import RPCFuncionBase

__all__ = ["EventRPCFucntion"]


@dataclass(slots=True)
class EventRPCFucntion(RPCFuncionBase):

    service_id: str = field(default=MicroService.SAAS_MS_UTILITIES.value, init=False)
    module_grpc: str = field(default="v1.utilities.event_pb2_grpc", init=False)
    stub_classname: str = field(default="EventServiceStub", init=False)
    module_pb2: str = field(default="v1.utilities.event_pb2", init=False)

    def read(self, params):
        self.event.update(
            dict(
                rpc_method="EventRead",
                request_class="EventReadRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event, cache=self.cache) + (self.event,)

    def read_event(self, params: dict):
        return self.read(params)

    def create(self, params):
        self.event.update(
            dict(
                rpc_method="EventCreate",
                request_class="EventCreateRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event) + (self.event,)

    def register_event(self, params: dict):
        return self.create(params)
