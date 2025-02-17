# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/utilities/file_record.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from omni_pro_grpc.common import base_pb2 as common_dot_base__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1ev1/utilities/file_record.proto\x12)pro.omni.oms.api.v1.utilities.file_record\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/protobuf/struct.proto"\x8c\x03\n\nFileRecord\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfile_name\x18\x02 \x01(\t\x12\x14\n\x0c\x63ontent_type\x18\x03 \x01(\t\x12\x11\n\tfile_size\x18\x04 \x01(\x05\x12\x11\n\ts3_bucket\x18\x05 \x01(\t\x12\x13\n\x0bupload_date\x18\x06 \x01(\t\x12\x15\n\rlast_modified\x18\x07 \x01(\t\x12\x10\n\x08\x66ile_url\x18\x08 \x01(\t\x12*\n\tmeta_data\x18\t \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0c\n\x04\x65tag\x18\n \x01(\t\x12\x19\n\x11\x61\x63\x63\x65ss_permission\x18\x0b \x01(\t\x12\x0e\n\x06\x62inary\x18\x0c \x01(\x0c\x12*\n\x06\x61\x63tive\x18\r \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x0e \x01(\t\x12?\n\x0cobject_audit\x18\x0f \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xd5\x02\n\x14\x46ileRecordAddRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x14\n\x0c\x63ontent_type\x18\x02 \x01(\t\x12\x11\n\tfile_size\x18\x03 \x01(\x05\x12\x11\n\ts3_bucket\x18\x04 \x01(\t\x12\x13\n\x0bupload_date\x18\x05 \x01(\t\x12\x15\n\rlast_modified\x18\x06 \x01(\t\x12\x10\n\x08\x66ile_url\x18\x07 \x01(\t\x12*\n\tmeta_data\x18\x08 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0c\n\x04\x65tag\x18\t \x01(\t\x12\x19\n\x11\x61\x63\x63\x65ss_permission\x18\n \x01(\t\x12\x0e\n\x06\x62inary\x18\x0b \x01(\x0c\x12\x13\n\x0b\x65xternal_id\x18\x0c \x01(\t\x12\x36\n\x07\x63ontext\x18\r \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xae\x01\n\x15\x46ileRecordAddResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12J\n\x0b\x66ile_record\x18\x02 \x01(\x0b\x32\x35.pro.omni.oms.api.v1.utilities.file_record.FileRecord"\xf3\x02\n\x15\x46ileRecordReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\t\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xea\x01\n\x16\x46ileRecordReadResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12J\n\x0b\x66ile_record\x18\x03 \x03(\x0b\x32\x35.pro.omni.oms.api.v1.utilities.file_record.FileRecord"\x9d\x01\n\x17\x46ileRecordUpdateRequest\x12J\n\x0b\x66ile_record\x18\x01 \x01(\x0b\x32\x35.pro.omni.oms.api.v1.utilities.file_record.FileRecord\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xb1\x01\n\x18\x46ileRecordUpdateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12J\n\x0b\x66ile_record\x18\x02 \x01(\x0b\x32\x35.pro.omni.oms.api.v1.utilities.file_record.FileRecord"]\n\x17\x46ileRecordDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"e\n\x18\x46ileRecordDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"_\n\x12PresignFileRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"w\n\x13PresignFileResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x15\n\rpresigned_url\x18\x02 \x01(\t2\xd1\x07\n\x11\x46ileRecordService\x12\xb8\x01\n\rFileRecordAdd\x12?.pro.omni.oms.api.v1.utilities.file_record.FileRecordAddRequest\x1a@.pro.omni.oms.api.v1.utilities.file_record.FileRecordAddResponse"$\x9a\xb5\x18 \x08\x02\x12\x1c\x61pi/v1/utilities/file_record\x12\xbb\x01\n\x0e\x46ileRecordRead\x12@.pro.omni.oms.api.v1.utilities.file_record.FileRecordReadRequest\x1a\x41.pro.omni.oms.api.v1.utilities.file_record.FileRecordReadResponse"$\x9a\xb5\x18 \x08\x01\x12\x1c\x61pi/v1/utilities/file_record\x12\xc1\x01\n\x10\x46ileRecordUpdate\x12\x42.pro.omni.oms.api.v1.utilities.file_record.FileRecordUpdateRequest\x1a\x43.pro.omni.oms.api.v1.utilities.file_record.FileRecordUpdateResponse"$\x9a\xb5\x18 \x08\x03\x12\x1c\x61pi/v1/utilities/file_record\x12\xc1\x01\n\x10\x46ileRecordDelete\x12\x42.pro.omni.oms.api.v1.utilities.file_record.FileRecordDeleteRequest\x1a\x43.pro.omni.oms.api.v1.utilities.file_record.FileRecordDeleteResponse"$\x9a\xb5\x18 \x08\x04\x12\x1c\x61pi/v1/utilities/file_record\x12\xba\x01\n\x0bPresignFile\x12=.pro.omni.oms.api.v1.utilities.file_record.PresignFileRequest\x1a>.pro.omni.oms.api.v1.utilities.file_record.PresignFileResponse",\x9a\xb5\x18(\x08\x01\x12$api/v1/utilities/file_record/presignb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.utilities.file_record_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _FILERECORDSERVICE.methods_by_name["FileRecordAdd"]._options = None
    _FILERECORDSERVICE.methods_by_name["FileRecordAdd"]._serialized_options = (
        b"\232\265\030 \010\002\022\034api/v1/utilities/file_record"
    )
    _FILERECORDSERVICE.methods_by_name["FileRecordRead"]._options = None
    _FILERECORDSERVICE.methods_by_name["FileRecordRead"]._serialized_options = (
        b"\232\265\030 \010\001\022\034api/v1/utilities/file_record"
    )
    _FILERECORDSERVICE.methods_by_name["FileRecordUpdate"]._options = None
    _FILERECORDSERVICE.methods_by_name["FileRecordUpdate"]._serialized_options = (
        b"\232\265\030 \010\003\022\034api/v1/utilities/file_record"
    )
    _FILERECORDSERVICE.methods_by_name["FileRecordDelete"]._options = None
    _FILERECORDSERVICE.methods_by_name["FileRecordDelete"]._serialized_options = (
        b"\232\265\030 \010\004\022\034api/v1/utilities/file_record"
    )
    _FILERECORDSERVICE.methods_by_name["PresignFile"]._options = None
    _FILERECORDSERVICE.methods_by_name["PresignFile"]._serialized_options = (
        b"\232\265\030(\010\001\022$api/v1/utilities/file_record/presign"
    )
    _globals["_FILERECORD"]._serialized_start = 159
    _globals["_FILERECORD"]._serialized_end = 555
    _globals["_FILERECORDADDREQUEST"]._serialized_start = 558
    _globals["_FILERECORDADDREQUEST"]._serialized_end = 899
    _globals["_FILERECORDADDRESPONSE"]._serialized_start = 902
    _globals["_FILERECORDADDRESPONSE"]._serialized_end = 1076
    _globals["_FILERECORDREADREQUEST"]._serialized_start = 1079
    _globals["_FILERECORDREADREQUEST"]._serialized_end = 1450
    _globals["_FILERECORDREADRESPONSE"]._serialized_start = 1453
    _globals["_FILERECORDREADRESPONSE"]._serialized_end = 1687
    _globals["_FILERECORDUPDATEREQUEST"]._serialized_start = 1690
    _globals["_FILERECORDUPDATEREQUEST"]._serialized_end = 1847
    _globals["_FILERECORDUPDATERESPONSE"]._serialized_start = 1850
    _globals["_FILERECORDUPDATERESPONSE"]._serialized_end = 2027
    _globals["_FILERECORDDELETEREQUEST"]._serialized_start = 2029
    _globals["_FILERECORDDELETEREQUEST"]._serialized_end = 2122
    _globals["_FILERECORDDELETERESPONSE"]._serialized_start = 2124
    _globals["_FILERECORDDELETERESPONSE"]._serialized_end = 2225
    _globals["_PRESIGNFILEREQUEST"]._serialized_start = 2227
    _globals["_PRESIGNFILEREQUEST"]._serialized_end = 2322
    _globals["_PRESIGNFILERESPONSE"]._serialized_start = 2324
    _globals["_PRESIGNFILERESPONSE"]._serialized_end = 2443
    _globals["_FILERECORDSERVICE"]._serialized_start = 2446
    _globals["_FILERECORDSERVICE"]._serialized_end = 3423
# @@protoc_insertion_point(module_scope)
