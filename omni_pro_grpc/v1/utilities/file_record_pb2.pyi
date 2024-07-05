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

class FileRecord(_message.Message):
    __slots__ = [
        "id",
        "file_name",
        "content_type",
        "file_size",
        "s3_bucket",
        "upload_date",
        "last_modified",
        "file_url",
        "meta_data",
        "etag",
        "access_permission",
        "binary",
        "active",
        "external_id",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    S3_BUCKET_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_DATE_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    FILE_URL_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    ACCESS_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    BINARY_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    file_name: str
    content_type: str
    file_size: int
    s3_bucket: str
    upload_date: str
    last_modified: str
    file_url: str
    meta_data: _struct_pb2.Struct
    etag: str
    access_permission: str
    binary: bytes
    active: _wrappers_pb2.BoolValue
    external_id: str
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        file_name: _Optional[str] = ...,
        content_type: _Optional[str] = ...,
        file_size: _Optional[int] = ...,
        s3_bucket: _Optional[str] = ...,
        upload_date: _Optional[str] = ...,
        last_modified: _Optional[str] = ...,
        file_url: _Optional[str] = ...,
        meta_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        etag: _Optional[str] = ...,
        access_permission: _Optional[str] = ...,
        binary: _Optional[bytes] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        external_id: _Optional[str] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class FileRecordAddRequest(_message.Message):
    __slots__ = [
        "file_name",
        "content_type",
        "file_size",
        "s3_bucket",
        "upload_date",
        "last_modified",
        "file_url",
        "meta_data",
        "etag",
        "access_permission",
        "binary",
        "external_id",
        "context",
    ]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    S3_BUCKET_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_DATE_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    FILE_URL_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    ACCESS_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    BINARY_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    content_type: str
    file_size: int
    s3_bucket: str
    upload_date: str
    last_modified: str
    file_url: str
    meta_data: _struct_pb2.Struct
    etag: str
    access_permission: str
    binary: bytes
    external_id: str
    context: _base_pb2.Context
    def __init__(
        self,
        file_name: _Optional[str] = ...,
        content_type: _Optional[str] = ...,
        file_size: _Optional[int] = ...,
        s3_bucket: _Optional[str] = ...,
        upload_date: _Optional[str] = ...,
        last_modified: _Optional[str] = ...,
        file_url: _Optional[str] = ...,
        meta_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        etag: _Optional[str] = ...,
        access_permission: _Optional[str] = ...,
        binary: _Optional[bytes] = ...,
        external_id: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class FileRecordAddResponse(_message.Message):
    __slots__ = ["response_standard", "file_record"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    FILE_RECORD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    file_record: FileRecord
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        file_record: _Optional[_Union[FileRecord, _Mapping]] = ...,
    ) -> None: ...

class FileRecordReadRequest(_message.Message):
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

class FileRecordReadResponse(_message.Message):
    __slots__ = ["response_standard", "meta_data", "file_record"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    FILE_RECORD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    file_record: _containers.RepeatedCompositeFieldContainer[FileRecord]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        file_record: _Optional[_Iterable[_Union[FileRecord, _Mapping]]] = ...,
    ) -> None: ...

class FileRecordUpdateRequest(_message.Message):
    __slots__ = ["file_record", "context"]
    FILE_RECORD_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    file_record: FileRecord
    context: _base_pb2.Context
    def __init__(
        self,
        file_record: _Optional[_Union[FileRecord, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class FileRecordUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "file_record"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    FILE_RECORD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    file_record: FileRecord
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        file_record: _Optional[_Union[FileRecord, _Mapping]] = ...,
    ) -> None: ...

class FileRecordDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class FileRecordDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class PresignFileRequest(_message.Message):
    __slots__ = ["file_name", "context"]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    context: _base_pb2.Context
    def __init__(
        self, file_name: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class PresignFileResponse(_message.Message):
    __slots__ = ["response_standard", "presigned_url"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    PRESIGNED_URL_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    presigned_url: str
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        presigned_url: _Optional[str] = ...,
    ) -> None: ...
