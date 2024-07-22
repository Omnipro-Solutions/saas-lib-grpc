from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from omni_pro_grpc.common import base_pb2 as _base_pb2
from omni_pro_grpc.v1.utilities import method_grpc_pb2 as _method_grpc_pb2
from omni_pro_grpc.v1.utilities import model_pb2 as _model_pb2
from omni_pro_grpc.v1.utilities import ms_pb2 as _ms_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Action(_message.Message):
    __slots__ = [
        "id",
        "name",
        "code",
        "model",
        "microservice",
        "url",
        "view",
        "token",
        "active",
        "external_id",
        "apply_if_filter",
        "grpc_method",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MICROSERVICE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    APPLY_IF_FILTER_FIELD_NUMBER: _ClassVar[int]
    GRPC_METHOD_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    code: str
    model: _model_pb2.Model
    microservice: _ms_pb2.Microservice
    url: str
    view: str
    token: str
    active: _wrappers_pb2.BoolValue
    external_id: str
    apply_if_filter: str
    grpc_method: _method_grpc_pb2.MethodGrpc
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        model: _Optional[_Union[_model_pb2.Model, _Mapping]] = ...,
        microservice: _Optional[_Union[_ms_pb2.Microservice, _Mapping]] = ...,
        url: _Optional[str] = ...,
        view: _Optional[str] = ...,
        token: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        external_id: _Optional[str] = ...,
        apply_if_filter: _Optional[str] = ...,
        grpc_method: _Optional[_Union[_method_grpc_pb2.MethodGrpc, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class ActionCreateRequest(_message.Message):
    __slots__ = [
        "name",
        "code",
        "model_id",
        "microservice_id",
        "url",
        "view",
        "token",
        "apply_if_filter",
        "grpc_method_id",
        "active",
        "external_id",
        "context",
    ]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    MICROSERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    APPLY_IF_FILTER_FIELD_NUMBER: _ClassVar[int]
    GRPC_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    code: str
    model_id: str
    microservice_id: str
    url: str
    view: str
    token: str
    apply_if_filter: str
    grpc_method_id: str
    active: _wrappers_pb2.BoolValue
    external_id: str
    context: _base_pb2.Context
    def __init__(
        self,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        model_id: _Optional[str] = ...,
        microservice_id: _Optional[str] = ...,
        url: _Optional[str] = ...,
        view: _Optional[str] = ...,
        token: _Optional[str] = ...,
        apply_if_filter: _Optional[str] = ...,
        grpc_method_id: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        external_id: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class ActionCreateResponse(_message.Message):
    __slots__ = ["action", "response_standard"]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    action: Action
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        action: _Optional[_Union[Action, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class ActionReadRequest(_message.Message):
    __slots__ = ["group_by", "sort_by", "fields", "filter", "paginated", "id", "context"]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    group_by: _containers.RepeatedCompositeFieldContainer[_base_pb2.GroupBy]
    sort_by: _base_pb2.SortBy
    fields: _base_pb2.Fields
    filter: _base_pb2.Filter
    paginated: _base_pb2.Paginated
    id: str
    context: _base_pb2.Context
    def __init__(
        self,
        group_by: _Optional[_Iterable[_Union[_base_pb2.GroupBy, _Mapping]]] = ...,
        sort_by: _Optional[_Union[_base_pb2.SortBy, _Mapping]] = ...,
        fields: _Optional[_Union[_base_pb2.Fields, _Mapping]] = ...,
        filter: _Optional[_Union[_base_pb2.Filter, _Mapping]] = ...,
        paginated: _Optional[_Union[_base_pb2.Paginated, _Mapping]] = ...,
        id: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class ActionReadResponse(_message.Message):
    __slots__ = ["actions", "meta_data", "response_standard"]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedCompositeFieldContainer[Action]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        actions: _Optional[_Iterable[_Union[Action, _Mapping]]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class ActionUpdateRequest(_message.Message):
    __slots__ = ["action", "context"]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    action: Action
    context: _base_pb2.Context
    def __init__(
        self,
        action: _Optional[_Union[Action, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class ActionUpdateResponse(_message.Message):
    __slots__ = ["action", "response_standard"]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    action: Action
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        action: _Optional[_Union[Action, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class ActionDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class ActionDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class CallActionRequest(_message.Message):
    __slots__ = ["action_id", "instances", "context"]
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    action_id: str
    instances: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    context: _base_pb2.Context
    def __init__(
        self,
        action_id: _Optional[str] = ...,
        instances: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class CallActionResponse(_message.Message):
    __slots__ = ["response", "response_standard"]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response: _struct_pb2.Struct
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...
