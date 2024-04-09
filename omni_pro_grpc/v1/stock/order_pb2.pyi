from typing import ClassVar as _ClassVar
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from omni_pro_grpc.common import base_pb2 as _base_pb2
from omni_pro_grpc.v1.stock import channel_pb2 as _channel_pb2
from omni_pro_grpc.v1.stock import state_pb2 as _state_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ObjectDefault(_message.Message):
    __slots__ = ["id", "name", "code"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    code: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...

class Order(_message.Message):
    __slots__ = ["id", "name", "sale_id", "order_sql_id", "channel", "state", "active", "external_id", "object_audit"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SALE_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_SQL_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    sale_id: int
    order_sql_id: int
    channel: _channel_pb2.Channel
    state: _state_pb2.State
    active: _wrappers_pb2.BoolValue
    external_id: str
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[int] = ...,
        name: _Optional[str] = ...,
        sale_id: _Optional[int] = ...,
        order_sql_id: _Optional[int] = ...,
        channel: _Optional[_Union[_channel_pb2.Channel, _Mapping]] = ...,
        state: _Optional[_Union[_state_pb2.State, _Mapping]] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        external_id: _Optional[str] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...
