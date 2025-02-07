# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/utilities/table_temp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from omni_pro_grpc.common import base_pb2 as common_dot_base__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1dv1/utilities/table_temp.proto\x12(pro.omni.oms.api.v1.utilities.table_temp\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x91\x02\n\tTableTemp\x12\n\n\x02id\x18\x01 \x01(\t\x12\x18\n\x10range_start_date\x18\x02 \x01(\t\x12\x16\n\x0erange_end_date\x18\x03 \x01(\t\x12\x30\n\x0c\x65xpire_table\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nname_table\x18\x05 \x01(\t\x12*\n\x06\x61\x63tive\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x07 \x01(\t\x12?\n\x0cobject_audit\x18\x08 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\x89\x02\n\x16TableTempCreateRequest\x12\x18\n\x10range_start_date\x18\x01 \x01(\t\x12\x16\n\x0erange_end_date\x18\x02 \x01(\t\x12\x30\n\x0c\x65xpire_table\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nname_table\x18\x04 \x01(\t\x12*\n\x06\x61\x63tive\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x06 \x01(\t\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xad\x01\n\x17TableTempCreateResponse\x12G\n\ntable_temp\x18\x01 \x01(\x0b\x32\x33.pro.omni.oms.api.v1.utilities.table_temp.TableTemp\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xf2\x02\n\x14TableTempReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\t\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xe7\x01\n\x15TableTempReadResponse\x12H\n\x0btable_temps\x18\x01 \x03(\x0b\x32\x33.pro.omni.oms.api.v1.utilities.table_temp.TableTemp\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12I\n\x11response_standard\x18\x03 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\x99\x01\n\x16TableTempUpdateRequest\x12G\n\ntable_temp\x18\x01 \x01(\x0b\x32\x33.pro.omni.oms.api.v1.utilities.table_temp.TableTemp\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xad\x01\n\x17TableTempUpdateResponse\x12G\n\ntable_temp\x18\x01 \x01(\x0b\x32\x33.pro.omni.oms.api.v1.utilities.table_temp.TableTemp\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\\\n\x16TableTempDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"d\n\x17TableTempDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\x84\x06\n\x10TableTempService\x12\xbb\x01\n\x0fTableTempCreate\x12@.pro.omni.oms.api.v1.utilities.table_temp.TableTempCreateRequest\x1a\x41.pro.omni.oms.api.v1.utilities.table_temp.TableTempCreateResponse"#\x9a\xb5\x18\x1f\x08\x02\x12\x1b\x61pi/v1/utilities/table/temp\x12\xb5\x01\n\rTableTempRead\x12>.pro.omni.oms.api.v1.utilities.table_temp.TableTempReadRequest\x1a?.pro.omni.oms.api.v1.utilities.table_temp.TableTempReadResponse"#\x9a\xb5\x18\x1f\x08\x01\x12\x1b\x61pi/v1/utilities/table/temp\x12\xbb\x01\n\x0fTableTempUpdate\x12@.pro.omni.oms.api.v1.utilities.table_temp.TableTempUpdateRequest\x1a\x41.pro.omni.oms.api.v1.utilities.table_temp.TableTempUpdateResponse"#\x9a\xb5\x18\x1f\x08\x03\x12\x1b\x61pi/v1/utilities/table/temp\x12\xbb\x01\n\x0fTableTempDelete\x12@.pro.omni.oms.api.v1.utilities.table_temp.TableTempDeleteRequest\x1a\x41.pro.omni.oms.api.v1.utilities.table_temp.TableTempDeleteResponse"#\x9a\xb5\x18\x1f\x08\x04\x12\x1b\x61pi/v1/utilities/table/tempb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.utilities.table_temp_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _TABLETEMPSERVICE.methods_by_name["TableTempCreate"]._options = None
    _TABLETEMPSERVICE.methods_by_name["TableTempCreate"]._serialized_options = (
        b"\232\265\030\037\010\002\022\033api/v1/utilities/table/temp"
    )
    _TABLETEMPSERVICE.methods_by_name["TableTempRead"]._options = None
    _TABLETEMPSERVICE.methods_by_name["TableTempRead"]._serialized_options = (
        b"\232\265\030\037\010\001\022\033api/v1/utilities/table/temp"
    )
    _TABLETEMPSERVICE.methods_by_name["TableTempUpdate"]._options = None
    _TABLETEMPSERVICE.methods_by_name["TableTempUpdate"]._serialized_options = (
        b"\232\265\030\037\010\003\022\033api/v1/utilities/table/temp"
    )
    _TABLETEMPSERVICE.methods_by_name["TableTempDelete"]._options = None
    _TABLETEMPSERVICE.methods_by_name["TableTempDelete"]._serialized_options = (
        b"\232\265\030\037\010\004\022\033api/v1/utilities/table/temp"
    )
    _globals["_TABLETEMP"]._serialized_start = 160
    _globals["_TABLETEMP"]._serialized_end = 433
    _globals["_TABLETEMPCREATEREQUEST"]._serialized_start = 436
    _globals["_TABLETEMPCREATEREQUEST"]._serialized_end = 701
    _globals["_TABLETEMPCREATERESPONSE"]._serialized_start = 704
    _globals["_TABLETEMPCREATERESPONSE"]._serialized_end = 877
    _globals["_TABLETEMPREADREQUEST"]._serialized_start = 880
    _globals["_TABLETEMPREADREQUEST"]._serialized_end = 1250
    _globals["_TABLETEMPREADRESPONSE"]._serialized_start = 1253
    _globals["_TABLETEMPREADRESPONSE"]._serialized_end = 1484
    _globals["_TABLETEMPUPDATEREQUEST"]._serialized_start = 1487
    _globals["_TABLETEMPUPDATEREQUEST"]._serialized_end = 1640
    _globals["_TABLETEMPUPDATERESPONSE"]._serialized_start = 1643
    _globals["_TABLETEMPUPDATERESPONSE"]._serialized_end = 1816
    _globals["_TABLETEMPDELETEREQUEST"]._serialized_start = 1818
    _globals["_TABLETEMPDELETEREQUEST"]._serialized_end = 1910
    _globals["_TABLETEMPDELETERESPONSE"]._serialized_start = 1912
    _globals["_TABLETEMPDELETERESPONSE"]._serialized_end = 2012
    _globals["_TABLETEMPSERVICE"]._serialized_start = 2015
    _globals["_TABLETEMPSERVICE"]._serialized_end = 2787
# @@protoc_insertion_point(module_scope)
