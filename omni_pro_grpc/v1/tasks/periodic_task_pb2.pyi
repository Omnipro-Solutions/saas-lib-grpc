from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from omni_pro_grpc.common import base_pb2 as _base_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class PeriodicTask(_message.Message):
    __slots__ = [
        "name",
        "task",
        "args",
        "kwargs",
        "queue",
        "exchange",
        "routing_key",
        "headers",
        "priority",
        "expires",
        "expire_seconds",
        "one_off",
        "start_time",
        "last_run_at",
        "total_run_count",
        "date_changed",
        "description",
        "discriminator",
        "schedule_id",
        "id",
        "external_id",
        "active",
        "object_audit",
    ]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    KWARGS_FIELD_NUMBER: _ClassVar[int]
    QUEUE_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ROUTING_KEY_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ONE_OFF_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_RUN_AT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RUN_COUNT_FIELD_NUMBER: _ClassVar[int]
    DATE_CHANGED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISCRIMINATOR_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    name: str
    task: str
    args: str
    kwargs: str
    queue: str
    exchange: str
    routing_key: str
    headers: str
    priority: int
    expires: _timestamp_pb2.Timestamp
    expire_seconds: int
    one_off: _wrappers_pb2.BoolValue
    start_time: _timestamp_pb2.Timestamp
    last_run_at: _timestamp_pb2.Timestamp
    total_run_count: int
    date_changed: _timestamp_pb2.Timestamp
    description: str
    discriminator: str
    schedule_id: int
    id: int
    external_id: str
    active: _wrappers_pb2.BoolValue
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        name: _Optional[str] = ...,
        task: _Optional[str] = ...,
        args: _Optional[str] = ...,
        kwargs: _Optional[str] = ...,
        queue: _Optional[str] = ...,
        exchange: _Optional[str] = ...,
        routing_key: _Optional[str] = ...,
        headers: _Optional[str] = ...,
        priority: _Optional[int] = ...,
        expires: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        expire_seconds: _Optional[int] = ...,
        one_off: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        last_run_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        total_run_count: _Optional[int] = ...,
        date_changed: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        description: _Optional[str] = ...,
        discriminator: _Optional[str] = ...,
        schedule_id: _Optional[int] = ...,
        id: _Optional[int] = ...,
        external_id: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class PeriodicTaskCreateRequest(_message.Message):
    __slots__ = [
        "name",
        "task",
        "args",
        "kwargs",
        "queue",
        "exchange",
        "routing_key",
        "headers",
        "priority",
        "expires",
        "expire_seconds",
        "one_off",
        "start_time",
        "active",
        "discriminator",
        "schedule_id",
        "external_id",
        "object_audit",
        "context",
    ]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    KWARGS_FIELD_NUMBER: _ClassVar[int]
    QUEUE_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ROUTING_KEY_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ONE_OFF_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    DISCRIMINATOR_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    task: str
    args: str
    kwargs: str
    queue: str
    exchange: str
    routing_key: str
    headers: str
    priority: int
    expires: _timestamp_pb2.Timestamp
    expire_seconds: int
    one_off: _wrappers_pb2.BoolValue
    start_time: _timestamp_pb2.Timestamp
    active: _wrappers_pb2.BoolValue
    discriminator: str
    schedule_id: int
    external_id: str
    object_audit: _base_pb2.ObjectAudit
    context: _base_pb2.Context
    def __init__(
        self,
        name: _Optional[str] = ...,
        task: _Optional[str] = ...,
        args: _Optional[str] = ...,
        kwargs: _Optional[str] = ...,
        queue: _Optional[str] = ...,
        exchange: _Optional[str] = ...,
        routing_key: _Optional[str] = ...,
        headers: _Optional[str] = ...,
        priority: _Optional[int] = ...,
        expires: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        expire_seconds: _Optional[int] = ...,
        one_off: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        discriminator: _Optional[str] = ...,
        schedule_id: _Optional[int] = ...,
        external_id: _Optional[str] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class PeriodicTaskCreateResponse(_message.Message):
    __slots__ = ["response_standard", "periodic_task"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    PERIODIC_TASK_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    periodic_task: PeriodicTask
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        periodic_task: _Optional[_Union[PeriodicTask, _Mapping]] = ...,
    ) -> None: ...

class PeriodicTaskReadRequest(_message.Message):
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

class PeriodicTaskReadResponse(_message.Message):
    __slots__ = ["response_standard", "meta_data", "periodic_tasks"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    PERIODIC_TASKS_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    periodic_tasks: _containers.RepeatedCompositeFieldContainer[PeriodicTask]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        periodic_tasks: _Optional[_Iterable[_Union[PeriodicTask, _Mapping]]] = ...,
    ) -> None: ...

class PeriodicTaskUpdateRequest(_message.Message):
    __slots__ = ["periodic_task", "context"]
    PERIODIC_TASK_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    periodic_task: PeriodicTask
    context: _base_pb2.Context
    def __init__(
        self,
        periodic_task: _Optional[_Union[PeriodicTask, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class PeriodicTaskUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "periodic_task"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    PERIODIC_TASK_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    periodic_task: PeriodicTask
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        periodic_task: _Optional[_Union[PeriodicTask, _Mapping]] = ...,
    ) -> None: ...

class PeriodicTaskDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: int
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class PeriodicTaskDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
