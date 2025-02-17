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
from omni_pro_grpc.v1.utilities import table_temp_pb2 as _table_temp_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Dashboard(_message.Message):
    __slots__ = [
        "id",
        "name",
        "code",
        "description",
        "layout_config",
        "main",
        "dashboard_widgets",
        "range_start_date",
        "range_end_date",
        "table_temp",
        "active",
        "external_id",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LAYOUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MAIN_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_WIDGETS_FIELD_NUMBER: _ClassVar[int]
    RANGE_START_DATE_FIELD_NUMBER: _ClassVar[int]
    RANGE_END_DATE_FIELD_NUMBER: _ClassVar[int]
    TABLE_TEMP_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    code: str
    description: str
    layout_config: _struct_pb2.Struct
    main: _wrappers_pb2.BoolValue
    dashboard_widgets: _struct_pb2.ListValue
    range_start_date: str
    range_end_date: str
    table_temp: _table_temp_pb2.TableTemp
    active: _wrappers_pb2.BoolValue
    external_id: str
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        description: _Optional[str] = ...,
        layout_config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        main: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        dashboard_widgets: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        range_start_date: _Optional[str] = ...,
        range_end_date: _Optional[str] = ...,
        table_temp: _Optional[_Union[_table_temp_pb2.TableTemp, _Mapping]] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        external_id: _Optional[str] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class DashboardCreateRequest(_message.Message):
    __slots__ = [
        "name",
        "code",
        "description",
        "layout_config",
        "main",
        "dashboard_widgets_ids",
        "range_start_date",
        "range_end_date",
        "table_temp_id",
        "active",
        "external_id",
        "context",
    ]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LAYOUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MAIN_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_WIDGETS_IDS_FIELD_NUMBER: _ClassVar[int]
    RANGE_START_DATE_FIELD_NUMBER: _ClassVar[int]
    RANGE_END_DATE_FIELD_NUMBER: _ClassVar[int]
    TABLE_TEMP_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    code: str
    description: str
    layout_config: _struct_pb2.Struct
    main: _wrappers_pb2.BoolValue
    dashboard_widgets_ids: _struct_pb2.ListValue
    range_start_date: str
    range_end_date: str
    table_temp_id: str
    active: _wrappers_pb2.BoolValue
    external_id: str
    context: _base_pb2.Context
    def __init__(
        self,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        description: _Optional[str] = ...,
        layout_config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        main: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        dashboard_widgets_ids: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        range_start_date: _Optional[str] = ...,
        range_end_date: _Optional[str] = ...,
        table_temp_id: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        external_id: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class DashboardCreateResponse(_message.Message):
    __slots__ = ["dashboard", "response_standard"]
    DASHBOARD_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    dashboard: Dashboard
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        dashboard: _Optional[_Union[Dashboard, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DashboardReadRequest(_message.Message):
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

class DashboardReadResponse(_message.Message):
    __slots__ = ["dashboards", "meta_data", "response_standard"]
    DASHBOARDS_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    dashboards: _containers.RepeatedCompositeFieldContainer[Dashboard]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        dashboards: _Optional[_Iterable[_Union[Dashboard, _Mapping]]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DashboardUpdateRequest(_message.Message):
    __slots__ = ["dashboard", "context"]
    DASHBOARD_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    dashboard: Dashboard
    context: _base_pb2.Context
    def __init__(
        self,
        dashboard: _Optional[_Union[Dashboard, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class DashboardUpdateResponse(_message.Message):
    __slots__ = ["dashboard", "response_standard"]
    DASHBOARD_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    dashboard: Dashboard
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        dashboard: _Optional[_Union[Dashboard, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DashboardDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class DashboardDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
