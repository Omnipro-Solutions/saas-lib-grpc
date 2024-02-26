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
from omni_pro_grpc.v1.sales import order_pb2 as _order_pb2
from omni_pro_grpc.v1.sales import sale_pb2 as _sale_pb2
from omni_pro_grpc.v1.sales import user_pb2 as _user_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class IssueType(_message.Message):
    __slots__ = ["id", "name", "code", "emails", "active", "object_audit"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    EMAILS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    code: str
    emails: str
    active: _wrappers_pb2.BoolValue
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[int] = ...,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        emails: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class Issue(_message.Message):
    __slots__ = [
        "id",
        "name",
        "state",
        "description",
        "user",
        "type",
        "sale",
        "order",
        "move_sql_id",
        "move_line_sql_id",
        "picking_sql_id",
        "external_id",
        "issue_historys",
        "active",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SALE_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    MOVE_SQL_ID_FIELD_NUMBER: _ClassVar[int]
    MOVE_LINE_SQL_ID_FIELD_NUMBER: _ClassVar[int]
    PICKING_SQL_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    ISSUE_HISTORYS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    state: str
    description: str
    user: _user_pb2.User
    type: IssueType
    sale: _sale_pb2.Sale
    order: _order_pb2.Order
    move_sql_id: int
    move_line_sql_id: int
    picking_sql_id: int
    external_id: str
    issue_historys: _containers.RepeatedCompositeFieldContainer[IssueHistory]
    active: _wrappers_pb2.BoolValue
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[int] = ...,
        name: _Optional[str] = ...,
        state: _Optional[str] = ...,
        description: _Optional[str] = ...,
        user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...,
        type: _Optional[_Union[IssueType, _Mapping]] = ...,
        sale: _Optional[_Union[_sale_pb2.Sale, _Mapping]] = ...,
        order: _Optional[_Union[_order_pb2.Order, _Mapping]] = ...,
        move_sql_id: _Optional[int] = ...,
        move_line_sql_id: _Optional[int] = ...,
        picking_sql_id: _Optional[int] = ...,
        external_id: _Optional[str] = ...,
        issue_historys: _Optional[_Iterable[_Union[IssueHistory, _Mapping]]] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class IssueHistory(_message.Message):
    __slots__ = ["id", "name", "description", "type", "user", "state", "issue", "active", "object_audit"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ISSUE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    description: str
    type: IssueType
    user: _user_pb2.User
    state: str
    issue: Issue
    active: _wrappers_pb2.BoolValue
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[int] = ...,
        name: _Optional[str] = ...,
        description: _Optional[str] = ...,
        type: _Optional[_Union[IssueType, _Mapping]] = ...,
        user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...,
        state: _Optional[str] = ...,
        issue: _Optional[_Union[Issue, _Mapping]] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class IssueCreateRequest(_message.Message):
    __slots__ = [
        "name",
        "state",
        "description",
        "user_id",
        "type_id",
        "sale_id",
        "order_id",
        "move_sql_id",
        "move_line_sql_id",
        "picking_sql_id",
        "external_id",
        "context",
    ]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    SALE_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    MOVE_SQL_ID_FIELD_NUMBER: _ClassVar[int]
    MOVE_LINE_SQL_ID_FIELD_NUMBER: _ClassVar[int]
    PICKING_SQL_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: str
    description: str
    user_id: str
    type_id: int
    sale_id: int
    order_id: int
    move_sql_id: int
    move_line_sql_id: int
    picking_sql_id: int
    external_id: str
    context: _base_pb2.Context
    def __init__(
        self,
        name: _Optional[str] = ...,
        state: _Optional[str] = ...,
        description: _Optional[str] = ...,
        user_id: _Optional[str] = ...,
        type_id: _Optional[int] = ...,
        sale_id: _Optional[int] = ...,
        order_id: _Optional[int] = ...,
        move_sql_id: _Optional[int] = ...,
        move_line_sql_id: _Optional[int] = ...,
        picking_sql_id: _Optional[int] = ...,
        external_id: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class IssueCreateResponse(_message.Message):
    __slots__ = ["issue", "response_standard"]
    ISSUE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    issue: Issue
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        issue: _Optional[_Union[Issue, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class IssueReadRequest(_message.Message):
    __slots__ = ["id", "group_by", "sort_by", "fields", "filter", "paginated", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: int
    group_by: _containers.RepeatedCompositeFieldContainer[_base_pb2.GroupBy]
    sort_by: _base_pb2.SortBy
    fields: _base_pb2.Fields
    filter: _base_pb2.Filter
    paginated: _base_pb2.Paginated
    context: _base_pb2.Context
    def __init__(
        self,
        id: _Optional[int] = ...,
        group_by: _Optional[_Iterable[_Union[_base_pb2.GroupBy, _Mapping]]] = ...,
        sort_by: _Optional[_Union[_base_pb2.SortBy, _Mapping]] = ...,
        fields: _Optional[_Union[_base_pb2.Fields, _Mapping]] = ...,
        filter: _Optional[_Union[_base_pb2.Filter, _Mapping]] = ...,
        paginated: _Optional[_Union[_base_pb2.Paginated, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class IssueReadResponse(_message.Message):
    __slots__ = ["issues", "meta_data", "response_standard"]
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    issues: _containers.RepeatedCompositeFieldContainer[Issue]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        issues: _Optional[_Iterable[_Union[Issue, _Mapping]]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class IssueUpdateRequest(_message.Message):
    __slots__ = ["issue", "context"]
    ISSUE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    issue: Issue
    context: _base_pb2.Context
    def __init__(
        self,
        issue: _Optional[_Union[Issue, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class IssueUpdateResponse(_message.Message):
    __slots__ = ["issue", "response_standard"]
    ISSUE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    issue: Issue
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        issue: _Optional[_Union[Issue, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class IssueDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: int
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class IssueDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class IssueTypeCreateRequest(_message.Message):
    __slots__ = ["name", "code", "emails", "active", "context"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    EMAILS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    code: str
    emails: str
    active: _wrappers_pb2.BoolValue
    context: _base_pb2.Context
    def __init__(
        self,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        emails: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class IssueTypeCreateResponse(_message.Message):
    __slots__ = ["issue_type", "response_standard"]
    ISSUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    issue_type: IssueType
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        issue_type: _Optional[_Union[IssueType, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class IssueTypeReadRequest(_message.Message):
    __slots__ = ["id", "group_by", "sort_by", "fields", "filter", "paginated", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: int
    group_by: _containers.RepeatedCompositeFieldContainer[_base_pb2.GroupBy]
    sort_by: _base_pb2.SortBy
    fields: _base_pb2.Fields
    filter: _base_pb2.Filter
    paginated: _base_pb2.Paginated
    context: _base_pb2.Context
    def __init__(
        self,
        id: _Optional[int] = ...,
        group_by: _Optional[_Iterable[_Union[_base_pb2.GroupBy, _Mapping]]] = ...,
        sort_by: _Optional[_Union[_base_pb2.SortBy, _Mapping]] = ...,
        fields: _Optional[_Union[_base_pb2.Fields, _Mapping]] = ...,
        filter: _Optional[_Union[_base_pb2.Filter, _Mapping]] = ...,
        paginated: _Optional[_Union[_base_pb2.Paginated, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class IssueTypeReadResponse(_message.Message):
    __slots__ = ["issue_types", "meta_data", "response_standard"]
    ISSUE_TYPES_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    issue_types: _containers.RepeatedCompositeFieldContainer[IssueType]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        issue_types: _Optional[_Iterable[_Union[IssueType, _Mapping]]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class IssueTypeUpdateRequest(_message.Message):
    __slots__ = ["issue_type", "context"]
    ISSUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    issue_type: IssueType
    context: _base_pb2.Context
    def __init__(
        self,
        issue_type: _Optional[_Union[IssueType, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class IssueTypeUpdateResponse(_message.Message):
    __slots__ = ["issue_type", "response_standard"]
    ISSUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    issue_type: IssueType
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        issue_type: _Optional[_Union[IssueType, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class IssueTypeDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: int
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class IssueTypeDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
