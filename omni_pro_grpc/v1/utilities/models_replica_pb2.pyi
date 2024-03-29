from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from omni_pro_grpc.common import base_pb2 as _base_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ModelsReplicaRequest(_message.Message):
    __slots__ = ["code", "date_start", "date_end", "context"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DATE_START_FIELD_NUMBER: _ClassVar[int]
    DATE_END_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    code: str
    date_start: _timestamp_pb2.Timestamp
    date_end: _timestamp_pb2.Timestamp
    context: _base_pb2.Context
    def __init__(
        self,
        code: _Optional[str] = ...,
        date_start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        date_end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class ModelsReplicaResponse(_message.Message):
    __slots__ = ["response_standard", "models_replica"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    MODELS_REPLICA_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    models_replica: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        models_replica: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ...,
    ) -> None: ...
