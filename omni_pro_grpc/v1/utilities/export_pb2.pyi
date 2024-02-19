from omni_pro_grpc.common import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExportModelRequest(_message.Message):
    __slots__ = ["model_name", "export_to", "export_type_file", "fields", "context"]
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPORT_TO_FIELD_NUMBER: _ClassVar[int]
    EXPORT_TYPE_FILE_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    model_name: str
    export_to: str
    export_type_file: str
    fields: _containers.RepeatedScalarFieldContainer[str]
    context: _base_pb2.Context
    def __init__(self, model_name: _Optional[str] = ..., export_to: _Optional[str] = ..., export_type_file: _Optional[str] = ..., fields: _Optional[_Iterable[str]] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...) -> None: ...

class ExportModelResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
