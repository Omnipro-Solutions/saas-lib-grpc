from typing import ClassVar as _ClassVar
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from omni_pro_grpc.common import base_pb2 as _base_pb2
from omni_pro_grpc.v1.stock import integration_operation_pb2 as _integration_operation_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class PickingIntegrationOperation(_message.Message):
    __slots__ = ["id", "picking_id", "integration_operation", "status", "active", "message"]
    ID_FIELD_NUMBER: _ClassVar[int]
    PICKING_ID_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_OPERATION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    id: int
    picking_id: int
    integration_operation: _integration_operation_pb2.IntegrationOperation
    status: str
    active: _wrappers_pb2.BoolValue
    message: str
    def __init__(
        self,
        id: _Optional[int] = ...,
        picking_id: _Optional[int] = ...,
        integration_operation: _Optional[_Union[_integration_operation_pb2.IntegrationOperation, _Mapping]] = ...,
        status: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        message: _Optional[str] = ...,
    ) -> None: ...
