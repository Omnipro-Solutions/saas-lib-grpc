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

class Attribute(_message.Message):
    __slots__ = [
        "id",
        "code",
        "name",
        "attribute_type",
        "is_common",
        "active",
        "external_id",
        "extra_attribute",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_COMMON_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    code: str
    name: str
    attribute_type: str
    is_common: _wrappers_pb2.BoolValue
    active: _wrappers_pb2.BoolValue
    external_id: str
    extra_attribute: _struct_pb2.Struct
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        code: _Optional[str] = ...,
        name: _Optional[str] = ...,
        attribute_type: _Optional[str] = ...,
        is_common: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        external_id: _Optional[str] = ...,
        extra_attribute: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class AttributeCreateRequest(_message.Message):
    __slots__ = ["code", "name", "attribute_type", "is_common", "extra_attribute", "external_id", "context"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_COMMON_FIELD_NUMBER: _ClassVar[int]
    EXTRA_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    code: str
    name: str
    attribute_type: str
    is_common: _wrappers_pb2.BoolValue
    extra_attribute: _struct_pb2.Struct
    external_id: str
    context: _base_pb2.Context
    def __init__(
        self,
        code: _Optional[str] = ...,
        name: _Optional[str] = ...,
        attribute_type: _Optional[str] = ...,
        is_common: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        extra_attribute: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        external_id: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AttributeCreateResponse(_message.Message):
    __slots__ = ["response_standard", "attribute"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    attribute: Attribute
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        attribute: _Optional[_Union[Attribute, _Mapping]] = ...,
    ) -> None: ...

class AttributeReadRequest(_message.Message):
    __slots__ = ["id", "group_by", "sort_by", "fields", "filter", "paginated", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    group_by: _containers.RepeatedCompositeFieldContainer[_base_pb2.GroupBy]
    sort_by: _base_pb2.SortBy
    fields: _base_pb2.Fields
    filter: _base_pb2.Filter
    paginated: _base_pb2.Paginated
    context: _base_pb2.Context
    def __init__(
        self,
        id: _Optional[str] = ...,
        group_by: _Optional[_Iterable[_Union[_base_pb2.GroupBy, _Mapping]]] = ...,
        sort_by: _Optional[_Union[_base_pb2.SortBy, _Mapping]] = ...,
        fields: _Optional[_Union[_base_pb2.Fields, _Mapping]] = ...,
        filter: _Optional[_Union[_base_pb2.Filter, _Mapping]] = ...,
        paginated: _Optional[_Union[_base_pb2.Paginated, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AttributeReadResponse(_message.Message):
    __slots__ = ["response_standard", "meta_data", "attributes", "context"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    attributes: _containers.RepeatedCompositeFieldContainer[Attribute]
    context: _base_pb2.Context
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        attributes: _Optional[_Iterable[_Union[Attribute, _Mapping]]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AttributeUpdateRequest(_message.Message):
    __slots__ = ["attribute", "context"]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    attribute: Attribute
    context: _base_pb2.Context
    def __init__(
        self,
        attribute: _Optional[_Union[Attribute, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AttributeUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "attribute"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    attribute: Attribute
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        attribute: _Optional[_Union[Attribute, _Mapping]] = ...,
    ) -> None: ...

class AttributeDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class AttributeDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
