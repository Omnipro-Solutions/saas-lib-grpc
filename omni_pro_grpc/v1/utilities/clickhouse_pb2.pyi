from typing import ClassVar as _ClassVar
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from omni_pro_grpc.common import base_pb2 as _base_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterWebhookClickHouseRequest(_message.Message):
    __slots__ = ["context"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    def __init__(self, context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...) -> None: ...

class RegisterWebhookClickHouseResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
