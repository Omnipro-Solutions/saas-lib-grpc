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
from omni_pro_grpc.v1.clients import address_pb2 as _address_pb2
from omni_pro_grpc.v1.clients import type_document_pb2 as _type_document_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Client(_message.Message):
    __slots__ = [
        "id",
        "name",
        "first_name",
        "last_name",
        "document_type",
        "document",
        "mobile",
        "phone",
        "prefix_phone",
        "prefix_mobile",
        "email",
        "country",
        "addresses",
        "active",
        "external_id",
        "properties",
        "is_parent",
        "parent",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    MOBILE_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    PREFIX_PHONE_FIELD_NUMBER: _ClassVar[int]
    PREFIX_MOBILE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    IS_PARENT_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    first_name: str
    last_name: str
    document_type: _type_document_pb2.TypeDocument
    document: str
    mobile: str
    phone: str
    prefix_phone: str
    prefix_mobile: str
    email: str
    country: _base_pb2.Object
    addresses: _containers.RepeatedCompositeFieldContainer[_address_pb2.Address]
    active: _wrappers_pb2.BoolValue
    external_id: str
    properties: _struct_pb2.Struct
    is_parent: _wrappers_pb2.BoolValue
    parent: Client
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        first_name: _Optional[str] = ...,
        last_name: _Optional[str] = ...,
        document_type: _Optional[_Union[_type_document_pb2.TypeDocument, _Mapping]] = ...,
        document: _Optional[str] = ...,
        mobile: _Optional[str] = ...,
        phone: _Optional[str] = ...,
        prefix_phone: _Optional[str] = ...,
        prefix_mobile: _Optional[str] = ...,
        email: _Optional[str] = ...,
        country: _Optional[_Union[_base_pb2.Object, _Mapping]] = ...,
        addresses: _Optional[_Iterable[_Union[_address_pb2.Address, _Mapping]]] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        external_id: _Optional[str] = ...,
        properties: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        is_parent: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        parent: _Optional[_Union[Client, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class ClientCreateRequest(_message.Message):
    __slots__ = [
        "name",
        "first_name",
        "last_name",
        "document_type_id",
        "document",
        "mobile",
        "phone",
        "prefix_phone",
        "prefix_mobile",
        "email",
        "addresses_ids",
        "country",
        "external_id",
        "properties",
        "is_parent",
        "parent_id",
        "context",
    ]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    MOBILE_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    PREFIX_PHONE_FIELD_NUMBER: _ClassVar[int]
    PREFIX_MOBILE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ADDRESSES_IDS_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    IS_PARENT_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    first_name: str
    last_name: str
    document_type_id: str
    document: str
    mobile: str
    phone: str
    prefix_phone: str
    prefix_mobile: str
    email: str
    addresses_ids: _containers.RepeatedScalarFieldContainer[str]
    country: _base_pb2.Object
    external_id: str
    properties: _struct_pb2.Struct
    is_parent: _wrappers_pb2.BoolValue
    parent_id: str
    context: _base_pb2.Context
    def __init__(
        self,
        name: _Optional[str] = ...,
        first_name: _Optional[str] = ...,
        last_name: _Optional[str] = ...,
        document_type_id: _Optional[str] = ...,
        document: _Optional[str] = ...,
        mobile: _Optional[str] = ...,
        phone: _Optional[str] = ...,
        prefix_phone: _Optional[str] = ...,
        prefix_mobile: _Optional[str] = ...,
        email: _Optional[str] = ...,
        addresses_ids: _Optional[_Iterable[str]] = ...,
        country: _Optional[_Union[_base_pb2.Object, _Mapping]] = ...,
        external_id: _Optional[str] = ...,
        properties: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        is_parent: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        parent_id: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class ClientCreateResponse(_message.Message):
    __slots__ = ["response_standard", "client"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    client: Client
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        client: _Optional[_Union[Client, _Mapping]] = ...,
    ) -> None: ...

class ClientReadRequest(_message.Message):
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

class ClientReadResponse(_message.Message):
    __slots__ = ["response_standard", "meta_data", "clients"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    CLIENTS_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    clients: _containers.RepeatedCompositeFieldContainer[Client]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        clients: _Optional[_Iterable[_Union[Client, _Mapping]]] = ...,
    ) -> None: ...

class ClientUpdateRequest(_message.Message):
    __slots__ = ["client", "context"]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    client: Client
    context: _base_pb2.Context
    def __init__(
        self,
        client: _Optional[_Union[Client, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class ClientUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "client"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    client: Client
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        client: _Optional[_Union[Client, _Mapping]] = ...,
    ) -> None: ...

class ClientDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class ClientDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class ClientSyncByHashRequest(_message.Message):
    __slots__ = ["info", "shipping_address", "billing_address", "context"]
    INFO_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BILLING_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    info: _struct_pb2.Struct
    shipping_address: _struct_pb2.Struct
    billing_address: _struct_pb2.Struct
    context: _base_pb2.Context
    def __init__(
        self,
        info: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        shipping_address: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        billing_address: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class ClientSyncByHashResponse(_message.Message):
    __slots__ = ["data_client", "response_standard"]
    DATA_CLIENT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    data_client: _struct_pb2.Struct
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        data_client: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...
