# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/utilities/timezone.proto
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
    b'\n\x1bv1/utilities/timezone.proto\x12&pro.omni.oms.api.v1.utilities.timezone\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xd8\x01\n\x08Timezone\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x0e\n\x06offset\x18\x04 \x01(\x05\x12\x12\n\noffset_dst\x18\x05 \x01(\x05\x12*\n\x06\x61\x63tive\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x07 \x01(\t\x12?\n\x0cobject_audit\x18\x08 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xcd\x01\n\x12TimezoneAddRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0e\n\x06offset\x18\x03 \x01(\x05\x12\x12\n\noffset_dst\x18\x04 \x01(\x05\x12*\n\x06\x61\x63tive\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x06 \x01(\t\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xa4\x01\n\x13TimezoneAddResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x42\n\x08timezone\x18\x02 \x01(\x0b\x32\x30.pro.omni.oms.api.v1.utilities.timezone.Timezone"\xf1\x02\n\x13TimezoneReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\t\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xe1\x01\n\x14TimezoneReadResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12\x43\n\ttimezones\x18\x03 \x03(\x0b\x32\x30.pro.omni.oms.api.v1.utilities.timezone.Timezone"\x93\x01\n\x15TimezoneUpdateRequest\x12\x42\n\x08timezone\x18\x01 \x01(\x0b\x32\x30.pro.omni.oms.api.v1.utilities.timezone.Timezone\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xa7\x01\n\x16TimezoneUpdateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x42\n\x08timezone\x18\x02 \x01(\x0b\x32\x30.pro.omni.oms.api.v1.utilities.timezone.Timezone"[\n\x15TimezoneDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"c\n\x16TimezoneDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xd6\x05\n\x0fTimezoneService\x12\xa9\x01\n\x0bTimezoneAdd\x12:.pro.omni.oms.api.v1.utilities.timezone.TimezoneAddRequest\x1a;.pro.omni.oms.api.v1.utilities.timezone.TimezoneAddResponse"!\x9a\xb5\x18\x1d\x08\x02\x12\x19\x61pi/v1/utilities/timezone\x12\xac\x01\n\x0cTimezoneRead\x12;.pro.omni.oms.api.v1.utilities.timezone.TimezoneReadRequest\x1a<.pro.omni.oms.api.v1.utilities.timezone.TimezoneReadResponse"!\x9a\xb5\x18\x1d\x08\x01\x12\x19\x61pi/v1/utilities/timezone\x12\xb2\x01\n\x0eTimezoneUpdate\x12=.pro.omni.oms.api.v1.utilities.timezone.TimezoneUpdateRequest\x1a>.pro.omni.oms.api.v1.utilities.timezone.TimezoneUpdateResponse"!\x9a\xb5\x18\x1d\x08\x03\x12\x19\x61pi/v1/utilities/timezone\x12\xb2\x01\n\x0eTimezoneDelete\x12=.pro.omni.oms.api.v1.utilities.timezone.TimezoneDeleteRequest\x1a>.pro.omni.oms.api.v1.utilities.timezone.TimezoneDeleteResponse"!\x9a\xb5\x18\x1d\x08\x04\x12\x19\x61pi/v1/utilities/timezoneb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.utilities.timezone_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _TIMEZONESERVICE.methods_by_name["TimezoneAdd"]._options = None
    _TIMEZONESERVICE.methods_by_name["TimezoneAdd"]._serialized_options = (
        b"\232\265\030\035\010\002\022\031api/v1/utilities/timezone"
    )
    _TIMEZONESERVICE.methods_by_name["TimezoneRead"]._options = None
    _TIMEZONESERVICE.methods_by_name["TimezoneRead"]._serialized_options = (
        b"\232\265\030\035\010\001\022\031api/v1/utilities/timezone"
    )
    _TIMEZONESERVICE.methods_by_name["TimezoneUpdate"]._options = None
    _TIMEZONESERVICE.methods_by_name["TimezoneUpdate"]._serialized_options = (
        b"\232\265\030\035\010\003\022\031api/v1/utilities/timezone"
    )
    _TIMEZONESERVICE.methods_by_name["TimezoneDelete"]._options = None
    _TIMEZONESERVICE.methods_by_name["TimezoneDelete"]._serialized_options = (
        b"\232\265\030\035\010\004\022\031api/v1/utilities/timezone"
    )
    _globals["_TIMEZONE"]._serialized_start = 123
    _globals["_TIMEZONE"]._serialized_end = 339
    _globals["_TIMEZONEADDREQUEST"]._serialized_start = 342
    _globals["_TIMEZONEADDREQUEST"]._serialized_end = 547
    _globals["_TIMEZONEADDRESPONSE"]._serialized_start = 550
    _globals["_TIMEZONEADDRESPONSE"]._serialized_end = 714
    _globals["_TIMEZONEREADREQUEST"]._serialized_start = 717
    _globals["_TIMEZONEREADREQUEST"]._serialized_end = 1086
    _globals["_TIMEZONEREADRESPONSE"]._serialized_start = 1089
    _globals["_TIMEZONEREADRESPONSE"]._serialized_end = 1314
    _globals["_TIMEZONEUPDATEREQUEST"]._serialized_start = 1317
    _globals["_TIMEZONEUPDATEREQUEST"]._serialized_end = 1464
    _globals["_TIMEZONEUPDATERESPONSE"]._serialized_start = 1467
    _globals["_TIMEZONEUPDATERESPONSE"]._serialized_end = 1634
    _globals["_TIMEZONEDELETEREQUEST"]._serialized_start = 1636
    _globals["_TIMEZONEDELETEREQUEST"]._serialized_end = 1727
    _globals["_TIMEZONEDELETERESPONSE"]._serialized_start = 1729
    _globals["_TIMEZONEDELETERESPONSE"]._serialized_end = 1828
    _globals["_TIMEZONESERVICE"]._serialized_start = 1831
    _globals["_TIMEZONESERVICE"]._serialized_end = 2557
# @@protoc_insertion_point(module_scope)
