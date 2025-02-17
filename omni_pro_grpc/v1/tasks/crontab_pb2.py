# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/tasks/crontab.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from omni_pro_grpc.common import base_pb2 as common_dot_base__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x16v1/tasks/crontab.proto\x12\x1epro.omni.oms.api.tasks.crontab\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto"\x9d\x02\n\x07\x43rontab\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06minute\x18\x02 \x01(\t\x12\x0c\n\x04hour\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x61y_of_week\x18\x04 \x01(\t\x12\x14\n\x0c\x64\x61y_of_month\x18\x05 \x01(\t\x12\x15\n\rmonth_of_year\x18\x06 \x01(\t\x12\x12\n\nexpression\x18\x07 \x01(\t\x12\x10\n\x08timezone\x18\x08 \x01(\t\x12\x13\n\x0b\x65xternal_id\x18\t \x01(\t\x12*\n\x06\x61\x63tive\x18\n \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12?\n\x0cobject_audit\x18\x0b \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xe9\x01\n\x14\x43rontabCreateRequest\x12\x0e\n\x06minute\x18\x01 \x01(\t\x12\x0c\n\x04hour\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x61y_of_week\x18\x03 \x01(\t\x12\x14\n\x0c\x64\x61y_of_month\x18\x04 \x01(\t\x12\x15\n\rmonth_of_year\x18\x05 \x01(\t\x12\x12\n\nexpression\x18\x06 \x01(\t\x12\x10\n\x08timezone\x18\x07 \x01(\t\x12\x13\n\x0b\x65xternal_id\x18\x08 \x01(\t\x12\x36\n\x07\x63ontext\x18\t \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9c\x01\n\x15\x43rontabCreateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x38\n\x07\x63rontab\x18\x02 \x01(\x0b\x32\'.pro.omni.oms.api.tasks.crontab.Crontab"\xf0\x02\n\x12\x43rontabReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xd6\x01\n\x13\x43rontabReadResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12\x39\n\x08\x63rontabs\x18\x03 \x03(\x0b\x32\'.pro.omni.oms.api.tasks.crontab.Crontab"\x88\x01\n\x14\x43rontabUpdateRequest\x12\x38\n\x07\x63rontab\x18\x01 \x01(\x0b\x32\'.pro.omni.oms.api.tasks.crontab.Crontab\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9c\x01\n\x15\x43rontabUpdateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x38\n\x07\x63rontab\x18\x02 \x01(\x0b\x32\'.pro.omni.oms.api.tasks.crontab.Crontab"Z\n\x14\x43rontabDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"b\n\x15\x43rontabDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xfe\x04\n\x0e\x43rontabService\x12\x9a\x01\n\rCrontabCreate\x12\x34.pro.omni.oms.api.tasks.crontab.CrontabCreateRequest\x1a\x35.pro.omni.oms.api.tasks.crontab.CrontabCreateResponse"\x1c\x9a\xb5\x18\x18\x08\x02\x12\x14\x61pi/v1/tasks/crontab\x12\x94\x01\n\x0b\x43rontabRead\x12\x32.pro.omni.oms.api.tasks.crontab.CrontabReadRequest\x1a\x33.pro.omni.oms.api.tasks.crontab.CrontabReadResponse"\x1c\x9a\xb5\x18\x18\x08\x01\x12\x14\x61pi/v1/tasks/crontab\x12\x9a\x01\n\rCrontabUpdate\x12\x34.pro.omni.oms.api.tasks.crontab.CrontabUpdateRequest\x1a\x35.pro.omni.oms.api.tasks.crontab.CrontabUpdateResponse"\x1c\x9a\xb5\x18\x18\x08\x03\x12\x14\x61pi/v1/tasks/crontab\x12\x9a\x01\n\rCrontabDelete\x12\x34.pro.omni.oms.api.tasks.crontab.CrontabDeleteRequest\x1a\x35.pro.omni.oms.api.tasks.crontab.CrontabDeleteResponse"\x1c\x9a\xb5\x18\x18\x08\x04\x12\x14\x61pi/v1/tasks/crontabb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.tasks.crontab_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _CRONTABSERVICE.methods_by_name["CrontabCreate"]._options = None
    _CRONTABSERVICE.methods_by_name["CrontabCreate"]._serialized_options = (
        b"\232\265\030\030\010\002\022\024api/v1/tasks/crontab"
    )
    _CRONTABSERVICE.methods_by_name["CrontabRead"]._options = None
    _CRONTABSERVICE.methods_by_name["CrontabRead"]._serialized_options = (
        b"\232\265\030\030\010\001\022\024api/v1/tasks/crontab"
    )
    _CRONTABSERVICE.methods_by_name["CrontabUpdate"]._options = None
    _CRONTABSERVICE.methods_by_name["CrontabUpdate"]._serialized_options = (
        b"\232\265\030\030\010\003\022\024api/v1/tasks/crontab"
    )
    _CRONTABSERVICE.methods_by_name["CrontabDelete"]._options = None
    _CRONTABSERVICE.methods_by_name["CrontabDelete"]._serialized_options = (
        b"\232\265\030\030\010\004\022\024api/v1/tasks/crontab"
    )
    _globals["_CRONTAB"]._serialized_start = 110
    _globals["_CRONTAB"]._serialized_end = 395
    _globals["_CRONTABCREATEREQUEST"]._serialized_start = 398
    _globals["_CRONTABCREATEREQUEST"]._serialized_end = 631
    _globals["_CRONTABCREATERESPONSE"]._serialized_start = 634
    _globals["_CRONTABCREATERESPONSE"]._serialized_end = 790
    _globals["_CRONTABREADREQUEST"]._serialized_start = 793
    _globals["_CRONTABREADREQUEST"]._serialized_end = 1161
    _globals["_CRONTABREADRESPONSE"]._serialized_start = 1164
    _globals["_CRONTABREADRESPONSE"]._serialized_end = 1378
    _globals["_CRONTABUPDATEREQUEST"]._serialized_start = 1381
    _globals["_CRONTABUPDATEREQUEST"]._serialized_end = 1517
    _globals["_CRONTABUPDATERESPONSE"]._serialized_start = 1520
    _globals["_CRONTABUPDATERESPONSE"]._serialized_end = 1676
    _globals["_CRONTABDELETEREQUEST"]._serialized_start = 1678
    _globals["_CRONTABDELETEREQUEST"]._serialized_end = 1768
    _globals["_CRONTABDELETERESPONSE"]._serialized_start = 1770
    _globals["_CRONTABDELETERESPONSE"]._serialized_end = 1868
    _globals["_CRONTABSERVICE"]._serialized_start = 1871
    _globals["_CRONTABSERVICE"]._serialized_end = 2509
# @@protoc_insertion_point(module_scope)
