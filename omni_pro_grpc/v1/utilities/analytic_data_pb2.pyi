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

class AnalyticData(_message.Message):
    __slots__ = [
        "id",
        "name",
        "code",
        "description",
        "query_template",
        "filters",
        "sort_field_name",
        "sort_order",
        "record_limit_data_visibility",
        "group_field_name",
        "active",
        "external_id",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    QUERY_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    SORT_ORDER_FIELD_NUMBER: _ClassVar[int]
    RECORD_LIMIT_DATA_VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    code: str
    description: str
    query_template: str
    filters: _struct_pb2.ListValue
    sort_field_name: str
    sort_order: str
    record_limit_data_visibility: int
    group_field_name: str
    active: _wrappers_pb2.BoolValue
    external_id: str
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        description: _Optional[str] = ...,
        query_template: _Optional[str] = ...,
        filters: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        sort_field_name: _Optional[str] = ...,
        sort_order: _Optional[str] = ...,
        record_limit_data_visibility: _Optional[int] = ...,
        group_field_name: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        external_id: _Optional[str] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class AnalyticDataCreateRequest(_message.Message):
    __slots__ = [
        "name",
        "code",
        "description",
        "query_template",
        "filters_ids",
        "sort_field_name",
        "sort_order",
        "record_limit_data_visibility",
        "group_field_name",
        "active",
        "external_id",
        "context",
    ]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    QUERY_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_IDS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    SORT_ORDER_FIELD_NUMBER: _ClassVar[int]
    RECORD_LIMIT_DATA_VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    code: str
    description: str
    query_template: str
    filters_ids: _struct_pb2.ListValue
    sort_field_name: str
    sort_order: str
    record_limit_data_visibility: int
    group_field_name: str
    active: _wrappers_pb2.BoolValue
    external_id: str
    context: _base_pb2.Context
    def __init__(
        self,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        description: _Optional[str] = ...,
        query_template: _Optional[str] = ...,
        filters_ids: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        sort_field_name: _Optional[str] = ...,
        sort_order: _Optional[str] = ...,
        record_limit_data_visibility: _Optional[int] = ...,
        group_field_name: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        external_id: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AnalyticDataCreateResponse(_message.Message):
    __slots__ = ["analytic_data", "response_standard"]
    ANALYTIC_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    analytic_data: AnalyticData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        analytic_data: _Optional[_Union[AnalyticData, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class AnalyticDataReadRequest(_message.Message):
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

class AnalyticDataReadResponse(_message.Message):
    __slots__ = ["analytic_datas", "meta_data", "response_standard"]
    ANALYTIC_DATAS_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    analytic_datas: _containers.RepeatedCompositeFieldContainer[AnalyticData]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        analytic_datas: _Optional[_Iterable[_Union[AnalyticData, _Mapping]]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class AnalyticDataUpdateRequest(_message.Message):
    __slots__ = ["analytic_data", "context"]
    ANALYTIC_DATA_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    analytic_data: AnalyticData
    context: _base_pb2.Context
    def __init__(
        self,
        analytic_data: _Optional[_Union[AnalyticData, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AnalyticDataUpdateResponse(_message.Message):
    __slots__ = ["analytic_data", "response_standard"]
    ANALYTIC_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    analytic_data: AnalyticData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        analytic_data: _Optional[_Union[AnalyticData, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class AnalyticDataDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class AnalyticDataDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
