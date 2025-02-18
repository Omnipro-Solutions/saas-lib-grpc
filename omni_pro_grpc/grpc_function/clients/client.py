from dataclasses import dataclass, field

from omni_pro_base.microservice import MicroService
from omni_pro_grpc.grpc_function.base import RPCFuncionBase

__all__ = ["ClientRPCFunction"]


@dataclass(slots=True)
class ClientRPCFunction(RPCFuncionBase):

    service_id: str = field(default=MicroService.SAAS_MS_CLIENT.value, init=False)
    module_grpc: str = field(default="v1.clients.client_pb2_grpc", init=False)
    stub_classname: str = field(default="ClientsServiceStub", init=False)
    module_pb2: str = field(default="v1.clients.client_pb2", init=False)

    def read(self, params: dict):
        self.event.update(
            dict(
                rpc_method="ClientRead",
                request_class="ClientReadRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event, cache=self.cache) + (self.event,)

    def read_client(self, params: dict):
        return self.read(params)
