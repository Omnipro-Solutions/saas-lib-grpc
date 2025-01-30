from typing import ClassVar as _ClassVar
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from omni_pro_grpc.common import base_pb2 as _base_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Task(_message.Message):
    __slots__ = ["task_id", "task_name", "task_params", "ignored", "status", "state"]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_NAME_FIELD_NUMBER: _ClassVar[int]
    TASK_PARAMS_FIELD_NUMBER: _ClassVar[int]
    IGNORED_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    task_name: str
    task_params: _struct_pb2.Struct
    ignored: _wrappers_pb2.BoolValue
    status: str
    state: str
    def __init__(
        self,
        task_id: _Optional[str] = ...,
        task_name: _Optional[str] = ...,
        task_params: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        ignored: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        status: _Optional[str] = ...,
        state: _Optional[str] = ...,
    ) -> None: ...

class TaskInvokeRequest(_message.Message):
    __slots__ = ["task_name", "task_params"]
    TASK_NAME_FIELD_NUMBER: _ClassVar[int]
    TASK_PARAMS_FIELD_NUMBER: _ClassVar[int]
    task_name: str
    task_params: _struct_pb2.Struct
    def __init__(
        self, task_name: _Optional[str] = ..., task_params: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...
    ) -> None: ...

class TaskInvokeResponse(_message.Message):
    __slots__ = ["response_standard", "task"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    task: Task
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        task: _Optional[_Union[Task, _Mapping]] = ...,
    ) -> None: ...
