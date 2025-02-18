from dataclasses import dataclass, field

from omni_pro_base.microservice import MicroService
from omni_pro_base.util import generate_hash
from omni_pro_grpc.grpc_function.base import RPCFuncionBase

__all__ = ["MethodRPCFunction"]


@dataclass(slots=True)
class MethodRPCFunction(RPCFuncionBase):

    service_id: str = field(default=MicroService.SAAS_MS_UTILITIES.value, init=False)
    module_grpc: str = field(default="v1.utilities.method_grpc_pb2_grpc", init=False)
    stub_classname: str = field(default="MethodGrpcServiceStub", init=False)
    module_pb2: str = field(default="v1.utilities.method_grpc_pb2", init=False)
    cache: bool = field(default=False, init=False)

    def read(self, params):
        self.event.update(
            dict(
                rpc_method="MethodGrpcRead",
                request_class="MethodGrpcReadRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event) + (self.event,)

    def read_method_rpc(self, params: dict):
        return self.read(params)

    def create(self, params):
        self.event.update(
            dict(
                rpc_method="MethodGrpcCreate",
                request_class="MethodGrpcCreateRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event) + (self.event,)

    def create_method_rpc(self, params: dict):
        return self.create(params)

    def update(self, params):
        self.event.update(
            dict(
                rpc_method="MethodGrpcUpdate",
                request_class="MethodGrpcUpdateRequest",
                params={"context": self.context} | params,
            )
        )
        return self.client.call_rpc_fuction(self.event) + (self.event,)

    def update_method_rpc(self, params: dict):
        return self.update(params)

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
