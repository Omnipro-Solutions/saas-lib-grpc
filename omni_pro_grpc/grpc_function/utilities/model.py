from dataclasses import dataclass, field

from omni_pro_base.microservice import MicroService
from omni_pro_grpc.grpc_function.base import RPCFuncionBase

__all__ = ["ModelRPCFucntion"]


@dataclass(slots=True)
class ModelRPCFucntion(RPCFuncionBase):

    service_id: str = field(default=MicroService.SAAS_MS_UTILITIES.value, init=False)
    module_grpc: str = field(default="v1.utilities.model_pb2_grpc", init=False)
    stub_classname: str = field(default="ModelsServiceStub", init=False)
    module_pb2: str = field(default="v1.utilities.model_pb2", init=False)

    def create(self, params):
        self.event.update(
            dict(
                rpc_method="ModelCreate",
                request_class="ModelCreateRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event) + (self.event,)

    def register_model(self, params: dict):
        return self.create(params)

    def update(self, params):
        self.event.update(
            dict(
                rpc_method="ModelUpdate",
                request_class="ModelUpdateRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event) + (self.event,)

    def updated_model(self, params: dict):
        return self.update(params)

    def read(self, params):
        self.event.update(
            dict(
                rpc_method="ModelRead",
                request_class="ModelReadRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event, self.cache) + (self.event,)

    def read_model(self, params: dict):
        return self.read(params)
