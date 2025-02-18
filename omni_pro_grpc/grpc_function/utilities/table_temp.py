from dataclasses import dataclass, field

from omni_pro_base.microservice import MicroService
from omni_pro_grpc.grpc_function.base import RPCFuncionBase

__all__ = ["TableTempRPCFunction"]


@dataclass(slots=True)
class TableTempRPCFunction(RPCFuncionBase):

    service_id: str = field(default=MicroService.SAAS_MS_UTILITIES.value, init=False)
    module_grpc: str = field(default="v1.utilities.table_temp_pb2_grpc", init=False)
    stub_classname: str = field(default="TableTempServiceStub", init=False)
    module_pb2: str = field(default="v1.utilities.table_temp_pb2", init=False)

    def create(self, params):
        self.event.update(
            dict(
                rpc_method="TableTempCreate",
                request_class="TableTempCreateRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event) + (self.event,)

    def update(self, params):
        self.event.update(
            dict(
                rpc_method="TableTempUpdate",
                request_class="TableTempUpdateRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event) + (self.event,)

    def read(self, params):
        self.event.update(
            dict(
                rpc_method="TableTempRead",
                request_class="TableTempReadRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event, self.cache) + (self.event,)
