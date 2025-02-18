from dataclasses import dataclass, field

from omni_pro_grpc.grpc_connector import Event, GRPClient

__all__ = ["RPCFuncionBase"]


@dataclass(slots=True)
class RPCFuncionBase(object):

    context: dict
    cache: bool = False
    timeout = float = 0
    service_id: str = field(init=False)
    module_grpc: str = field(init=False)
    stub_classname: str = field(init=False)
    module_pb2: str = field(init=False)
    event: Event = field(init=False)
    client: GRPClient = field(init=False)

    def read(self, *args, kwarg):
        raise NotImplementedError()

    def create(self, *args, kwarg):
        raise NotImplementedError()

    def update(self, *args, kwarg):
        raise NotImplementedError()

    def delete(self, *args, kwarg):
        raise NotImplementedError()

    def __post_init__(self):
        self.event: Event = Event(
            module_grpc=self.module_grpc,
            stub_classname=self.stub_classname,
            module_pb2=self.module_pb2,
            rpc_method=None,
            request_class=None,
        )
        self.client: GRPClient = GRPClient(service_id=self.service_id, timeout=self.timeout)
