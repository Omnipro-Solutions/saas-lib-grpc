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

DESCRIPTOR: _descriptor.FileDescriptor

class Crontab(_message.Message):
    __slots__ = [
        "id",
        "minute",
        "hour",
        "day_of_week",
        "day_of_month",
        "month_of_year",
        "expression",
        "timezone",
        "external_id",
        "active",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    MINUTE_FIELD_NUMBER: _ClassVar[int]
    HOUR_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_MONTH_FIELD_NUMBER: _ClassVar[int]
    MONTH_OF_YEAR_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: int
    minute: str
    hour: str
    day_of_week: str
    day_of_month: str
    month_of_year: str
    expression: str
    timezone: str
    external_id: str
    active: _wrappers_pb2.BoolValue
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[int] = ...,
        minute: _Optional[str] = ...,
        hour: _Optional[str] = ...,
        day_of_week: _Optional[str] = ...,
        day_of_month: _Optional[str] = ...,
        month_of_year: _Optional[str] = ...,
        expression: _Optional[str] = ...,
        timezone: _Optional[str] = ...,
        external_id: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class CrontabCreateRequest(_message.Message):
    __slots__ = [
        "minute",
        "hour",
        "day_of_week",
        "day_of_month",
        "month_of_year",
        "expression",
        "timezone",
        "external_id",
        "context",
    ]
    MINUTE_FIELD_NUMBER: _ClassVar[int]
    HOUR_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_MONTH_FIELD_NUMBER: _ClassVar[int]
    MONTH_OF_YEAR_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    minute: str
    hour: str
    day_of_week: str
    day_of_month: str
    month_of_year: str
    expression: str
    timezone: str
    external_id: str
    context: _base_pb2.Context
    def __init__(
        self,
        minute: _Optional[str] = ...,
        hour: _Optional[str] = ...,
        day_of_week: _Optional[str] = ...,
        day_of_month: _Optional[str] = ...,
        month_of_year: _Optional[str] = ...,
        expression: _Optional[str] = ...,
        timezone: _Optional[str] = ...,
        external_id: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class CrontabCreateResponse(_message.Message):
    __slots__ = ["response_standard", "crontab"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    CRONTAB_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    crontab: Crontab
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        crontab: _Optional[_Union[Crontab, _Mapping]] = ...,
    ) -> None: ...

class CrontabReadRequest(_message.Message):
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
    id: int
    context: _base_pb2.Context
    def __init__(
        self,
        group_by: _Optional[_Iterable[_Union[_base_pb2.GroupBy, _Mapping]]] = ...,
        sort_by: _Optional[_Union[_base_pb2.SortBy, _Mapping]] = ...,
        fields: _Optional[_Union[_base_pb2.Fields, _Mapping]] = ...,
        filter: _Optional[_Union[_base_pb2.Filter, _Mapping]] = ...,
        paginated: _Optional[_Union[_base_pb2.Paginated, _Mapping]] = ...,
        id: _Optional[int] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class CrontabReadResponse(_message.Message):
    __slots__ = ["response_standard", "meta_data", "crontabs"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    CRONTABS_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    crontabs: _containers.RepeatedCompositeFieldContainer[Crontab]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        crontabs: _Optional[_Iterable[_Union[Crontab, _Mapping]]] = ...,
    ) -> None: ...

class CrontabUpdateRequest(_message.Message):
    __slots__ = ["crontab", "context"]
    CRONTAB_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    crontab: Crontab
    context: _base_pb2.Context
    def __init__(
        self,
        crontab: _Optional[_Union[Crontab, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class CrontabUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "crontab"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    CRONTAB_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    crontab: Crontab
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        crontab: _Optional[_Union[Crontab, _Mapping]] = ...,
    ) -> None: ...

class CrontabDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: int
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class CrontabDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
