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
from omni_pro_grpc.v1.utilities import model_pb2 as _model_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class TemplateNotification(_message.Message):
    __slots__ = [
        "id",
        "name",
        "code",
        "type",
        "raw",
        "render",
        "model",
        "active",
        "external_id",
        "subject",
        "from_sender",
        "email_to",
        "model_email_to",
        "email_cc",
        "number_to",
        "model_number_to",
        "number_cc",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RAW_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    FROM_SENDER_FIELD_NUMBER: _ClassVar[int]
    EMAIL_TO_FIELD_NUMBER: _ClassVar[int]
    MODEL_EMAIL_TO_FIELD_NUMBER: _ClassVar[int]
    EMAIL_CC_FIELD_NUMBER: _ClassVar[int]
    NUMBER_TO_FIELD_NUMBER: _ClassVar[int]
    MODEL_NUMBER_TO_FIELD_NUMBER: _ClassVar[int]
    NUMBER_CC_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    code: str
    type: str
    raw: str
    render: str
    model: _model_pb2.Model
    active: _wrappers_pb2.BoolValue
    external_id: str
    subject: str
    from_sender: str
    email_to: _containers.RepeatedScalarFieldContainer[str]
    model_email_to: str
    email_cc: _containers.RepeatedScalarFieldContainer[str]
    number_to: _containers.RepeatedScalarFieldContainer[str]
    model_number_to: str
    number_cc: _containers.RepeatedScalarFieldContainer[str]
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        type: _Optional[str] = ...,
        raw: _Optional[str] = ...,
        render: _Optional[str] = ...,
        model: _Optional[_Union[_model_pb2.Model, _Mapping]] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        external_id: _Optional[str] = ...,
        subject: _Optional[str] = ...,
        from_sender: _Optional[str] = ...,
        email_to: _Optional[_Iterable[str]] = ...,
        model_email_to: _Optional[str] = ...,
        email_cc: _Optional[_Iterable[str]] = ...,
        number_to: _Optional[_Iterable[str]] = ...,
        model_number_to: _Optional[str] = ...,
        number_cc: _Optional[_Iterable[str]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class TemplateNotificationCreateRequest(_message.Message):
    __slots__ = [
        "name",
        "code",
        "type",
        "raw",
        "render",
        "model_id",
        "active",
        "external_id",
        "subject",
        "from_sender",
        "email_to",
        "model_email_to",
        "email_cc",
        "number_to",
        "model_number_to",
        "number_cc",
        "context",
    ]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RAW_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    FROM_SENDER_FIELD_NUMBER: _ClassVar[int]
    EMAIL_TO_FIELD_NUMBER: _ClassVar[int]
    MODEL_EMAIL_TO_FIELD_NUMBER: _ClassVar[int]
    EMAIL_CC_FIELD_NUMBER: _ClassVar[int]
    NUMBER_TO_FIELD_NUMBER: _ClassVar[int]
    MODEL_NUMBER_TO_FIELD_NUMBER: _ClassVar[int]
    NUMBER_CC_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    code: str
    type: str
    raw: str
    render: str
    model_id: str
    active: _wrappers_pb2.BoolValue
    external_id: str
    subject: str
    from_sender: str
    email_to: _containers.RepeatedScalarFieldContainer[str]
    model_email_to: str
    email_cc: _containers.RepeatedScalarFieldContainer[str]
    number_to: _containers.RepeatedScalarFieldContainer[str]
    model_number_to: str
    number_cc: _containers.RepeatedScalarFieldContainer[str]
    context: _base_pb2.Context
    def __init__(
        self,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        type: _Optional[str] = ...,
        raw: _Optional[str] = ...,
        render: _Optional[str] = ...,
        model_id: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        external_id: _Optional[str] = ...,
        subject: _Optional[str] = ...,
        from_sender: _Optional[str] = ...,
        email_to: _Optional[_Iterable[str]] = ...,
        model_email_to: _Optional[str] = ...,
        email_cc: _Optional[_Iterable[str]] = ...,
        number_to: _Optional[_Iterable[str]] = ...,
        model_number_to: _Optional[str] = ...,
        number_cc: _Optional[_Iterable[str]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class TemplateNotificationCreateResponse(_message.Message):
    __slots__ = ["template_notification", "response_standard"]
    TEMPLATE_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    template_notification: TemplateNotification
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        template_notification: _Optional[_Union[TemplateNotification, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class TemplateNotificationReadRequest(_message.Message):
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

class TemplateNotificationReadResponse(_message.Message):
    __slots__ = ["template_notifications", "meta_data", "response_standard"]
    TEMPLATE_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    template_notifications: _containers.RepeatedCompositeFieldContainer[TemplateNotification]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        template_notifications: _Optional[_Iterable[_Union[TemplateNotification, _Mapping]]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class TemplateNotificationUpdateRequest(_message.Message):
    __slots__ = ["template_notification", "context"]
    TEMPLATE_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    template_notification: TemplateNotification
    context: _base_pb2.Context
    def __init__(
        self,
        template_notification: _Optional[_Union[TemplateNotification, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class TemplateNotificationUpdateResponse(_message.Message):
    __slots__ = ["template_notification", "response_standard"]
    TEMPLATE_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    template_notification: TemplateNotification
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        template_notification: _Optional[_Union[TemplateNotification, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class TemplateNotificationDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class TemplateNotificationDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class TemplateNotificationRenderRequest(_message.Message):
    __slots__ = ["id", "model_ids", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_IDS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    model_ids: _containers.RepeatedScalarFieldContainer[str]
    context: _base_pb2.Context
    def __init__(
        self,
        id: _Optional[str] = ...,
        model_ids: _Optional[_Iterable[str]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class TemplateNotificationRenderResponse(_message.Message):
    __slots__ = ["render", "response_standard"]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    render: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        render: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...
