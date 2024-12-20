from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from omni_pro_grpc.common import base_pb2 as _base_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class CreateOrUpdateMirrorModelRequest(_message.Message):
    __slots__ = ["model_path", "model_data", "context"]
    MODEL_PATH_FIELD_NUMBER: _ClassVar[int]
    MODEL_DATA_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    model_path: str
    model_data: _struct_pb2.Struct
    context: _base_pb2.Context
    def __init__(
        self,
        model_path: _Optional[str] = ...,
        model_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class CreateOrUpdateCreateMirrorResponse(_message.Message):
    __slots__ = ["model_data", "response_standard"]
    MODEL_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    model_data: _struct_pb2.Struct
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        model_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class ReadMirrorModelRequest(_message.Message):
    __slots__ = ["model_path", "protobuf", "group_by", "sort_by", "fields", "filter", "paginated", "id", "context"]
    MODEL_PATH_FIELD_NUMBER: _ClassVar[int]
    PROTOBUF_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    model_path: str
    protobuf: _wrappers_pb2.BoolValue
    group_by: _containers.RepeatedCompositeFieldContainer[_base_pb2.GroupBy]
    sort_by: _base_pb2.SortBy
    fields: _base_pb2.Fields
    filter: _base_pb2.Filter
    paginated: _base_pb2.Paginated
    id: str
    context: _base_pb2.Context
    def __init__(
        self,
        model_path: _Optional[str] = ...,
        protobuf: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        group_by: _Optional[_Iterable[_Union[_base_pb2.GroupBy, _Mapping]]] = ...,
        sort_by: _Optional[_Union[_base_pb2.SortBy, _Mapping]] = ...,
        fields: _Optional[_Union[_base_pb2.Fields, _Mapping]] = ...,
        filter: _Optional[_Union[_base_pb2.Filter, _Mapping]] = ...,
        paginated: _Optional[_Union[_base_pb2.Paginated, _Mapping]] = ...,
        id: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class ReadMirrorModelResponse(_message.Message):
    __slots__ = ["mirror_models", "response_standard"]
    MIRROR_MODELS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    mirror_models: _struct_pb2.ListValue
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        mirror_models: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DeleteMirrorModelRequest(_message.Message):
    __slots__ = ["model_path", "id", "context"]
    MODEL_PATH_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    model_path: str
    id: str
    context: _base_pb2.Context
    def __init__(
        self,
        model_path: _Optional[str] = ...,
        id: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class DeleteMirrorModelResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class RegisterWebhookMirrorModelRequest(_message.Message):
    __slots__ = ["context"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    def __init__(self, context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...) -> None: ...

class RegisterWebhookMirrorModelResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class RegisterMethodGrpcRequest(_message.Message):
    __slots__ = ["filter", "context"]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    filter: _base_pb2.Filter
    context: _base_pb2.Context
    def __init__(
        self,
        filter: _Optional[_Union[_base_pb2.Filter, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class RegisterMethodGrpcResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class MultiCreateOrMultiUpdateMirrorModelRequest(_message.Message):
    __slots__ = ["model_path", "data", "context"]
    MODEL_PATH_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    model_path: str
    data: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    context: _base_pb2.Context
    def __init__(
        self,
        model_path: _Optional[str] = ...,
        data: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class MultiCreateOrMultiUpdateMirrorModelResponse(_message.Message):
    __slots__ = ["data", "response_standard"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        data: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class MultiDeleteMirrorModelRequest(_message.Message):
    __slots__ = ["model_path", "id", "context"]
    MODEL_PATH_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    model_path: str
    id: _containers.RepeatedScalarFieldContainer[str]
    context: _base_pb2.Context
    def __init__(
        self,
        model_path: _Optional[str] = ...,
        id: _Optional[_Iterable[str]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class MultiDeleteMirrorModelResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
