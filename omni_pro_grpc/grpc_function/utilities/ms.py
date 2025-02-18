from dataclasses import dataclass, field

from omni_pro_base.microservice import MicroService
from omni_pro_grpc.grpc_function.base import RPCFuncionBase

__all__ = ["MicroServiceRPCFunction"]


@dataclass(slots=True)
class MicroServiceRPCFunction(RPCFuncionBase):

    service_id: str = field(default=MicroService.SAAS_MS_UTILITIES.value, init=False)
    module_grpc: str = field(default="v1.utilities.ms_pb2_grpc", init=False)
    stub_classname: str = field(default="MicroserviceServiceStub", init=False)
    module_pb2: str = field(default="v1.utilities.ms_pb2", init=False)
    cache: bool = field(default=False, init=False)

    def read(self, params):
        self.event.update(
            dict(
                rpc_method="MicroserviceRead",
                request_class="MicroserviceReadRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event) + (self.event,)

    def read_ms(self, params: dict):
        return self.read(params)
