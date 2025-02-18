from dataclasses import dataclass, field

from omni_pro_base.microservice import MicroService
from omni_pro_grpc.grpc_function.base import RPCFuncionBase

__all__ = ["UserRPCFunction"]


@dataclass(slots=True)
class UserRPCFunction(RPCFuncionBase):

    service_id: str = field(default=MicroService.SAAS_MS_USER.value, init=False)
    module_grpc: str = field(default="v1.users.user_pb2_grpc", init=False)
    stub_classname: str = field(default="UsersServiceStub", init=False)
    module_pb2: str = field(default="v1.users.user_pb2", init=False)

    def create(self, params: dict):
        self.event.update(
            dict(
                rpc_method="ActionCreate",
                request_class="ActionCreateRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event) + (self.event,)

    def create_action(self, params: dict):
        return self.create(params)
