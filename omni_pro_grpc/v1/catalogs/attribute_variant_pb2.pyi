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

class AttributeVariant(_message.Message):
    __slots__ = ["id", "attribute", "sequence", "external_id", "active", "object_audit"]
    ID_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    attribute: _struct_pb2.Struct
    sequence: int
    external_id: str
    active: _wrappers_pb2.BoolValue
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        attribute: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        sequence: _Optional[int] = ...,
        external_id: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class AttributeVariantCreateRequest(_message.Message):
    __slots__ = ["attribute_code", "sequence", "external_id", "context"]
    ATTRIBUTE_CODE_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    attribute_code: str
    sequence: int
    external_id: str
    context: _base_pb2.Context
    def __init__(
        self,
        attribute_code: _Optional[str] = ...,
        sequence: _Optional[int] = ...,
        external_id: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AttributeVariantCreateResponse(_message.Message):
    __slots__ = ["response_standard", "attribute_variant"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_VARIANT_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    attribute_variant: AttributeVariant
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        attribute_variant: _Optional[_Union[AttributeVariant, _Mapping]] = ...,
    ) -> None: ...

class AttributeVariantReadRequest(_message.Message):
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

class AttributeVariantReadResponse(_message.Message):
    __slots__ = ["response_standard", "meta_data", "attribute_variants"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_VARIANTS_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    attribute_variants: _containers.RepeatedCompositeFieldContainer[AttributeVariant]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        attribute_variants: _Optional[_Iterable[_Union[AttributeVariant, _Mapping]]] = ...,
    ) -> None: ...

class AttributeVariantUpdateRequest(_message.Message):
    __slots__ = ["attribute_variant", "context"]
    ATTRIBUTE_VARIANT_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    attribute_variant: AttributeVariant
    context: _base_pb2.Context
    def __init__(
        self,
        attribute_variant: _Optional[_Union[AttributeVariant, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AttributeVariantUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "attribute_variant"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_VARIANT_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    attribute_variant: AttributeVariant
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        attribute_variant: _Optional[_Union[AttributeVariant, _Mapping]] = ...,
    ) -> None: ...

class AttributeVariantDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class AttributeVariantDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
