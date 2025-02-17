# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/rules/calendar.proto
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
    b'\n\x17v1/rules/calendar.proto\x12"pro.omni.oms.api.v1.rules.calendar\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xa6\x01\n\x08\x43\x61lendar\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12*\n\x06\x61\x63tive\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x04 \x01(\t\x12?\n\x0cobject_audit\x18\x05 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"r\n\x15\x43\x61lendarCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x65xternal_id\x18\x02 \x01(\t\x12\x36\n\x07\x63ontext\x18\x03 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xa3\x01\n\x16\x43\x61lendarCreateResponse\x12>\n\x08\x63\x61lendar\x18\x01 \x01(\x0b\x32,.pro.omni.oms.api.v1.rules.calendar.Calendar\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xf1\x02\n\x13\x43\x61lendarReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\t\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xdd\x01\n\x14\x43\x61lendarReadResponse\x12?\n\tcalendars\x18\x01 \x03(\x0b\x32,.pro.omni.oms.api.v1.rules.calendar.Calendar\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12I\n\x11response_standard\x18\x03 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\x8f\x01\n\x15\x43\x61lendarUpdateRequest\x12>\n\x08\x63\x61lendar\x18\x01 \x01(\x0b\x32,.pro.omni.oms.api.v1.rules.calendar.Calendar\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xa3\x01\n\x16\x43\x61lendarUpdateResponse\x12>\n\x08\x63\x61lendar\x18\x01 \x01(\x0b\x32,.pro.omni.oms.api.v1.rules.calendar.Calendar\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"[\n\x15\x43\x61lendarDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"c\n\x16\x43\x61lendarDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xaf\x05\n\x0f\x43\x61lendarService\x12\xa6\x01\n\x0e\x43\x61lendarCreate\x12\x39.pro.omni.oms.api.v1.rules.calendar.CalendarCreateRequest\x1a:.pro.omni.oms.api.v1.rules.calendar.CalendarCreateResponse"\x1d\x9a\xb5\x18\x19\x08\x02\x12\x15\x61pi/v1/rules/calendar\x12\xa0\x01\n\x0c\x43\x61lendarRead\x12\x37.pro.omni.oms.api.v1.rules.calendar.CalendarReadRequest\x1a\x38.pro.omni.oms.api.v1.rules.calendar.CalendarReadResponse"\x1d\x9a\xb5\x18\x19\x08\x01\x12\x15\x61pi/v1/rules/calendar\x12\xa6\x01\n\x0e\x43\x61lendarUpdate\x12\x39.pro.omni.oms.api.v1.rules.calendar.CalendarUpdateRequest\x1a:.pro.omni.oms.api.v1.rules.calendar.CalendarUpdateResponse"\x1d\x9a\xb5\x18\x19\x08\x03\x12\x15\x61pi/v1/rules/calendar\x12\xa6\x01\n\x0e\x43\x61lendarDelete\x12\x39.pro.omni.oms.api.v1.rules.calendar.CalendarDeleteRequest\x1a:.pro.omni.oms.api.v1.rules.calendar.CalendarDeleteResponse"\x1d\x9a\xb5\x18\x19\x08\x04\x12\x15\x61pi/v1/rules/calendarb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.rules.calendar_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _CALENDARSERVICE.methods_by_name["CalendarCreate"]._options = None
    _CALENDARSERVICE.methods_by_name["CalendarCreate"]._serialized_options = (
        b"\232\265\030\031\010\002\022\025api/v1/rules/calendar"
    )
    _CALENDARSERVICE.methods_by_name["CalendarRead"]._options = None
    _CALENDARSERVICE.methods_by_name["CalendarRead"]._serialized_options = (
        b"\232\265\030\031\010\001\022\025api/v1/rules/calendar"
    )
    _CALENDARSERVICE.methods_by_name["CalendarUpdate"]._options = None
    _CALENDARSERVICE.methods_by_name["CalendarUpdate"]._serialized_options = (
        b"\232\265\030\031\010\003\022\025api/v1/rules/calendar"
    )
    _CALENDARSERVICE.methods_by_name["CalendarDelete"]._options = None
    _CALENDARSERVICE.methods_by_name["CalendarDelete"]._serialized_options = (
        b"\232\265\030\031\010\004\022\025api/v1/rules/calendar"
    )
    _globals["_CALENDAR"]._serialized_start = 115
    _globals["_CALENDAR"]._serialized_end = 281
    _globals["_CALENDARCREATEREQUEST"]._serialized_start = 283
    _globals["_CALENDARCREATEREQUEST"]._serialized_end = 397
    _globals["_CALENDARCREATERESPONSE"]._serialized_start = 400
    _globals["_CALENDARCREATERESPONSE"]._serialized_end = 563
    _globals["_CALENDARREADREQUEST"]._serialized_start = 566
    _globals["_CALENDARREADREQUEST"]._serialized_end = 935
    _globals["_CALENDARREADRESPONSE"]._serialized_start = 938
    _globals["_CALENDARREADRESPONSE"]._serialized_end = 1159
    _globals["_CALENDARUPDATEREQUEST"]._serialized_start = 1162
    _globals["_CALENDARUPDATEREQUEST"]._serialized_end = 1305
    _globals["_CALENDARUPDATERESPONSE"]._serialized_start = 1308
    _globals["_CALENDARUPDATERESPONSE"]._serialized_end = 1471
    _globals["_CALENDARDELETEREQUEST"]._serialized_start = 1473
    _globals["_CALENDARDELETEREQUEST"]._serialized_end = 1564
    _globals["_CALENDARDELETERESPONSE"]._serialized_start = 1566
    _globals["_CALENDARDELETERESPONSE"]._serialized_end = 1665
    _globals["_CALENDARSERVICE"]._serialized_start = 1668
    _globals["_CALENDARSERVICE"]._serialized_end = 2355
# @@protoc_insertion_point(module_scope)
