from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from omni_pro_grpc.common import base_pb2 as _base_pb2
from omni_pro_grpc.v1.catalogs import attribute_pb2 as _attribute_pb2
from omni_pro_grpc.v1.catalogs import attribute_variant_pb2 as _attribute_variant_pb2
from omni_pro_grpc.v1.catalogs import group_pb2 as _group_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Family(_message.Message):
    __slots__ = [
        "id",
        "name",
        "code",
        "attribute_as_label",
        "attribute_as_image",
        "variants",
        "groups",
        "external_id",
        "active",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_AS_LABEL_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_AS_IMAGE_FIELD_NUMBER: _ClassVar[int]
    VARIANTS_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    code: str
    attribute_as_label: _attribute_pb2.Attribute
    attribute_as_image: _attribute_pb2.Attribute
    variants: _containers.RepeatedCompositeFieldContainer[_attribute_variant_pb2.AttributeVariant]
    groups: _containers.RepeatedCompositeFieldContainer[_group_pb2.Group]
    external_id: str
    active: _wrappers_pb2.BoolValue
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        attribute_as_label: _Optional[_Union[_attribute_pb2.Attribute, _Mapping]] = ...,
        attribute_as_image: _Optional[_Union[_attribute_pb2.Attribute, _Mapping]] = ...,
        variants: _Optional[_Iterable[_Union[_attribute_variant_pb2.AttributeVariant, _Mapping]]] = ...,
        groups: _Optional[_Iterable[_Union[_group_pb2.Group, _Mapping]]] = ...,
        external_id: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class FamilyCreateRequest(_message.Message):
    __slots__ = [
        "name",
        "code",
        "attribute_as_label_id",
        "attribute_as_image_id",
        "variant_ids",
        "group_ids",
        "external_id",
        "context",
    ]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_AS_LABEL_ID_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_AS_IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    VARIANT_IDS_FIELD_NUMBER: _ClassVar[int]
    GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    code: str
    attribute_as_label_id: str
    attribute_as_image_id: str
    variant_ids: _containers.RepeatedScalarFieldContainer[str]
    group_ids: _containers.RepeatedScalarFieldContainer[str]
    external_id: str
    context: _base_pb2.Context
    def __init__(
        self,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        attribute_as_label_id: _Optional[str] = ...,
        attribute_as_image_id: _Optional[str] = ...,
        variant_ids: _Optional[_Iterable[str]] = ...,
        group_ids: _Optional[_Iterable[str]] = ...,
        external_id: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class FamilyCreateResponse(_message.Message):
    __slots__ = ["response_standard", "family"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    family: Family
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        family: _Optional[_Union[Family, _Mapping]] = ...,
    ) -> None: ...

class FamilyReadRequest(_message.Message):
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

class FamilyReadResponse(_message.Message):
    __slots__ = ["response_standard", "meta_data", "families", "context"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    FAMILIES_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    families: _containers.RepeatedCompositeFieldContainer[Family]
    context: _base_pb2.Context
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        families: _Optional[_Iterable[_Union[Family, _Mapping]]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class FamilyUpdateRequest(_message.Message):
    __slots__ = ["family", "context"]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    family: Family
    context: _base_pb2.Context
    def __init__(
        self,
        family: _Optional[_Union[Family, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class FamilyUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "family"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    family: Family
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        family: _Optional[_Union[Family, _Mapping]] = ...,
    ) -> None: ...

class FamilyDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class FamilyDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
