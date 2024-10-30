# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/tasks/interval.proto
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
    b'\n\x17v1/tasks/interval.proto\x12\x1fpro.omni.oms.api.tasks.interval\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xb7\x01\n\x08Interval\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05\x65very\x18\x02 \x01(\x05\x12\x0e\n\x06period\x18\x03 \x01(\t\x12\x13\n\x0b\x65xternal_id\x18\x04 \x01(\t\x12*\n\x06\x61\x63tive\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12?\n\x0cobject_audit\x18\x06 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\x83\x01\n\x15IntervalCreateRequest\x12\r\n\x05\x65very\x18\x01 \x01(\x05\x12\x0e\n\x06period\x18\x02 \x01(\t\x12\x13\n\x0b\x65xternal_id\x18\x03 \x01(\t\x12\x36\n\x07\x63ontext\x18\x04 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xa0\x01\n\x16IntervalCreateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12;\n\x08interval\x18\x02 \x01(\x0b\x32).pro.omni.oms.api.tasks.interval.Interval"\xf1\x02\n\x13IntervalReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xda\x01\n\x14IntervalReadResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12<\n\tintervals\x18\x03 \x03(\x0b\x32).pro.omni.oms.api.tasks.interval.Interval"\x8c\x01\n\x15IntervalUpdateRequest\x12;\n\x08interval\x18\x01 \x01(\x0b\x32).pro.omni.oms.api.tasks.interval.Interval\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xa0\x01\n\x16IntervalUpdateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12;\n\x08interval\x18\x02 \x01(\x0b\x32).pro.omni.oms.api.tasks.interval.Interval"[\n\x15IntervalDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"c\n\x16IntervalDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xa2\x04\n\x0fIntervalService\x12\x83\x01\n\x0eIntervalCreate\x12\x36.pro.omni.oms.api.tasks.interval.IntervalCreateRequest\x1a\x37.pro.omni.oms.api.tasks.interval.IntervalCreateResponse"\x00\x12}\n\x0cIntervalRead\x12\x34.pro.omni.oms.api.tasks.interval.IntervalReadRequest\x1a\x35.pro.omni.oms.api.tasks.interval.IntervalReadResponse"\x00\x12\x83\x01\n\x0eIntervalUpdate\x12\x36.pro.omni.oms.api.tasks.interval.IntervalUpdateRequest\x1a\x37.pro.omni.oms.api.tasks.interval.IntervalUpdateResponse"\x00\x12\x83\x01\n\x0eIntervalDelete\x12\x36.pro.omni.oms.api.tasks.interval.IntervalDeleteRequest\x1a\x37.pro.omni.oms.api.tasks.interval.IntervalDeleteResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.tasks.interval_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _globals["_INTERVAL"]._serialized_start = 112
    _globals["_INTERVAL"]._serialized_end = 295
    _globals["_INTERVALCREATEREQUEST"]._serialized_start = 298
    _globals["_INTERVALCREATEREQUEST"]._serialized_end = 429
    _globals["_INTERVALCREATERESPONSE"]._serialized_start = 432
    _globals["_INTERVALCREATERESPONSE"]._serialized_end = 592
    _globals["_INTERVALREADREQUEST"]._serialized_start = 595
    _globals["_INTERVALREADREQUEST"]._serialized_end = 964
    _globals["_INTERVALREADRESPONSE"]._serialized_start = 967
    _globals["_INTERVALREADRESPONSE"]._serialized_end = 1185
    _globals["_INTERVALUPDATEREQUEST"]._serialized_start = 1188
    _globals["_INTERVALUPDATEREQUEST"]._serialized_end = 1328
    _globals["_INTERVALUPDATERESPONSE"]._serialized_start = 1331
    _globals["_INTERVALUPDATERESPONSE"]._serialized_end = 1491
    _globals["_INTERVALDELETEREQUEST"]._serialized_start = 1493
    _globals["_INTERVALDELETEREQUEST"]._serialized_end = 1584
    _globals["_INTERVALDELETERESPONSE"]._serialized_start = 1586
    _globals["_INTERVALDELETERESPONSE"]._serialized_end = 1685
    _globals["_INTERVALSERVICE"]._serialized_start = 1688
    _globals["_INTERVALSERVICE"]._serialized_end = 2234
# @@protoc_insertion_point(module_scope)