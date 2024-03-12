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
from omni_pro_grpc.v1.utilities import event_pb2 as _event_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Webhook(_message.Message):
    __slots__ = [
        "id",
        "events",
        "url",
        "method",
        "format",
        "type_webhook",
        "protocol",
        "python_code",
        "dag_id",
        "active",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    TYPE_WEBHOOK_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    PYTHON_CODE_FIELD_NUMBER: _ClassVar[int]
    DAG_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    events: _containers.RepeatedCompositeFieldContainer[_event_pb2.Event]
    url: str
    method: str
    format: str
    type_webhook: str
    protocol: str
    python_code: str
    dag_id: str
    active: _wrappers_pb2.BoolValue
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        events: _Optional[_Iterable[_Union[_event_pb2.Event, _Mapping]]] = ...,
        url: _Optional[str] = ...,
        method: _Optional[str] = ...,
        format: _Optional[str] = ...,
        type_webhook: _Optional[str] = ...,
        protocol: _Optional[str] = ...,
        python_code: _Optional[str] = ...,
        dag_id: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class WebhookCreateRequest(_message.Message):
    __slots__ = ["event_ids", "url", "method", "format", "type_webhook", "protocol", "python_code", "dag_id", "context"]
    EVENT_IDS_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    TYPE_WEBHOOK_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    PYTHON_CODE_FIELD_NUMBER: _ClassVar[int]
    DAG_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    event_ids: _containers.RepeatedScalarFieldContainer[str]
    url: str
    method: str
    format: str
    type_webhook: str
    protocol: str
    python_code: str
    dag_id: str
    context: _base_pb2.Context
    def __init__(
        self,
        event_ids: _Optional[_Iterable[str]] = ...,
        url: _Optional[str] = ...,
        method: _Optional[str] = ...,
        format: _Optional[str] = ...,
        type_webhook: _Optional[str] = ...,
        protocol: _Optional[str] = ...,
        python_code: _Optional[str] = ...,
        dag_id: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class WebhookCreateResponse(_message.Message):
    __slots__ = ["response_standard", "webhook"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    webhook: Webhook
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        webhook: _Optional[_Union[Webhook, _Mapping]] = ...,
    ) -> None: ...

class WebhookReadRequest(_message.Message):
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

class WebhookReadResponse(_message.Message):
    __slots__ = ["response_standard", "meta_data", "webhooks"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    WEBHOOKS_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    webhooks: _containers.RepeatedCompositeFieldContainer[Webhook]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        webhooks: _Optional[_Iterable[_Union[Webhook, _Mapping]]] = ...,
    ) -> None: ...

class WebhookUpdateRequest(_message.Message):
    __slots__ = ["webhook", "context"]
    WEBHOOK_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    webhook: Webhook
    context: _base_pb2.Context
    def __init__(
        self,
        webhook: _Optional[_Union[Webhook, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class WebhookUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "webhook"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    webhook: Webhook
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        webhook: _Optional[_Union[Webhook, _Mapping]] = ...,
    ) -> None: ...

class WebhookDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class WebhookDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
