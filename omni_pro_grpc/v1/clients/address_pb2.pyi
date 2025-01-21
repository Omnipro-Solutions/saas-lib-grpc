from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from omni_pro_grpc.common import base_pb2 as _base_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Address(_message.Message):
    __slots__ = [
        "id",
        "country_id",
        "code",
        "name",
        "type_address",
        "street",
        "street2",
        "mobile",
        "phone",
        "prefix_phone",
        "prefix_mobile",
        "lat",
        "lng",
        "zip_code",
        "territory_matrixes",
        "active",
        "external_id",
        "client_id",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STREET_FIELD_NUMBER: _ClassVar[int]
    STREET2_FIELD_NUMBER: _ClassVar[int]
    MOBILE_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    PREFIX_PHONE_FIELD_NUMBER: _ClassVar[int]
    PREFIX_MOBILE_FIELD_NUMBER: _ClassVar[int]
    LAT_FIELD_NUMBER: _ClassVar[int]
    LNG_FIELD_NUMBER: _ClassVar[int]
    ZIP_CODE_FIELD_NUMBER: _ClassVar[int]
    TERRITORY_MATRIXES_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    country_id: str
    code: str
    name: str
    type_address: str
    street: str
    street2: str
    mobile: str
    phone: str
    prefix_phone: str
    prefix_mobile: str
    lat: str
    lng: str
    zip_code: str
    territory_matrixes: _struct_pb2.ListValue
    active: bool
    external_id: str
    client_id: str
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        country_id: _Optional[str] = ...,
        code: _Optional[str] = ...,
        name: _Optional[str] = ...,
        type_address: _Optional[str] = ...,
        street: _Optional[str] = ...,
        street2: _Optional[str] = ...,
        mobile: _Optional[str] = ...,
        phone: _Optional[str] = ...,
        prefix_phone: _Optional[str] = ...,
        prefix_mobile: _Optional[str] = ...,
        lat: _Optional[str] = ...,
        lng: _Optional[str] = ...,
        zip_code: _Optional[str] = ...,
        territory_matrixes: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        active: bool = ...,
        external_id: _Optional[str] = ...,
        client_id: _Optional[str] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class AddressCreateRequest(_message.Message):
    __slots__ = [
        "client_id",
        "country_id",
        "code",
        "name",
        "type_address",
        "street",
        "street2",
        "mobile",
        "phone",
        "prefix_phone",
        "prefix_mobile",
        "lat",
        "lng",
        "zip_code",
        "territory_matrixes",
        "external_id",
        "context",
    ]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STREET_FIELD_NUMBER: _ClassVar[int]
    STREET2_FIELD_NUMBER: _ClassVar[int]
    MOBILE_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    PREFIX_PHONE_FIELD_NUMBER: _ClassVar[int]
    PREFIX_MOBILE_FIELD_NUMBER: _ClassVar[int]
    LAT_FIELD_NUMBER: _ClassVar[int]
    LNG_FIELD_NUMBER: _ClassVar[int]
    ZIP_CODE_FIELD_NUMBER: _ClassVar[int]
    TERRITORY_MATRIXES_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    country_id: str
    code: str
    name: str
    type_address: str
    street: str
    street2: str
    mobile: str
    phone: str
    prefix_phone: str
    prefix_mobile: str
    lat: str
    lng: str
    zip_code: str
    territory_matrixes: _struct_pb2.ListValue
    external_id: str
    context: _base_pb2.Context
    def __init__(
        self,
        client_id: _Optional[str] = ...,
        country_id: _Optional[str] = ...,
        code: _Optional[str] = ...,
        name: _Optional[str] = ...,
        type_address: _Optional[str] = ...,
        street: _Optional[str] = ...,
        street2: _Optional[str] = ...,
        mobile: _Optional[str] = ...,
        phone: _Optional[str] = ...,
        prefix_phone: _Optional[str] = ...,
        prefix_mobile: _Optional[str] = ...,
        lat: _Optional[str] = ...,
        lng: _Optional[str] = ...,
        zip_code: _Optional[str] = ...,
        territory_matrixes: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        external_id: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AddressCreateResponse(_message.Message):
    __slots__ = ["response_standard", "address"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    address: Address
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        address: _Optional[_Union[Address, _Mapping]] = ...,
    ) -> None: ...

class AddressUpdateRequest(_message.Message):
    __slots__ = ["client_id", "address", "context"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    address: Address
    context: _base_pb2.Context
    def __init__(
        self,
        client_id: _Optional[str] = ...,
        address: _Optional[_Union[Address, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AddressUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "address"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    address: Address
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        address: _Optional[_Union[Address, _Mapping]] = ...,
    ) -> None: ...

class AddressDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class AddressDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class AddressReadRequest(_message.Message):
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

class AddressReadResponse(_message.Message):
    __slots__ = ["response_standard", "meta_data", "addresses"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    addresses: _containers.RepeatedCompositeFieldContainer[Address]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        addresses: _Optional[_Iterable[_Union[Address, _Mapping]]] = ...,
    ) -> None: ...
