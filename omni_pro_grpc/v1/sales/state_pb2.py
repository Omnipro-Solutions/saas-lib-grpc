# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/sales/state.proto
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
    b'\n\x14v1/sales/state.proto\x12\x1fpro.omni.oms.api.v1.sales.state\x1a\x11\x63ommon/base.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1egoogle/protobuf/wrappers.proto"\x8a\x02\n\x05State\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12%\n\x04\x66low\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0c\n\x04type\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\r\n\x05\x63olor\x18\x07 \x01(\t\x12*\n\x06\x61\x63tive\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\t \x01(\t\x12?\n\x0cobject_audit\x18\n \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xc0\x01\n\x12StateCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0f\n\x07\x66low_id\x18\x03 \x01(\x05\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\r\n\x05\x63olor\x18\x06 \x01(\t\x12\x13\n\x0b\x65xternal_id\x18\x07 \x01(\t\x12\x36\n\x07\x63ontext\x18\x08 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x97\x01\n\x13StateCreateResponse\x12\x35\n\x05state\x18\x01 \x01(\x0b\x32&.pro.omni.oms.api.v1.sales.state.State\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xee\x02\n\x10StateReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xd1\x01\n\x11StateReadResponse\x12\x36\n\x06states\x18\x01 \x03(\x0b\x32&.pro.omni.oms.api.v1.sales.state.State\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12I\n\x11response_standard\x18\x03 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\x83\x01\n\x12StateUpdateRequest\x12\x35\n\x05state\x18\x01 \x01(\x0b\x32&.pro.omni.oms.api.v1.sales.state.State\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x97\x01\n\x13StateUpdateResponse\x12\x35\n\x05state\x18\x01 \x01(\x0b\x32&.pro.omni.oms.api.v1.sales.state.State\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"X\n\x12StateDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"`\n\x13StateDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xf8\x03\n\x0cStateService\x12z\n\x0bStateCreate\x12\x33.pro.omni.oms.api.v1.sales.state.StateCreateRequest\x1a\x34.pro.omni.oms.api.v1.sales.state.StateCreateResponse"\x00\x12t\n\tStateRead\x12\x31.pro.omni.oms.api.v1.sales.state.StateReadRequest\x1a\x32.pro.omni.oms.api.v1.sales.state.StateReadResponse"\x00\x12z\n\x0bStateUpdate\x12\x33.pro.omni.oms.api.v1.sales.state.StateUpdateRequest\x1a\x34.pro.omni.oms.api.v1.sales.state.StateUpdateResponse"\x00\x12z\n\x0bStateDelete\x12\x33.pro.omni.oms.api.v1.sales.state.StateDeleteRequest\x1a\x34.pro.omni.oms.api.v1.sales.state.StateDeleteResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.sales.state_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _globals["_STATE"]._serialized_start = 139
    _globals["_STATE"]._serialized_end = 405
    _globals["_STATECREATEREQUEST"]._serialized_start = 408
    _globals["_STATECREATEREQUEST"]._serialized_end = 600
    _globals["_STATECREATERESPONSE"]._serialized_start = 603
    _globals["_STATECREATERESPONSE"]._serialized_end = 754
    _globals["_STATEREADREQUEST"]._serialized_start = 757
    _globals["_STATEREADREQUEST"]._serialized_end = 1123
    _globals["_STATEREADRESPONSE"]._serialized_start = 1126
    _globals["_STATEREADRESPONSE"]._serialized_end = 1335
    _globals["_STATEUPDATEREQUEST"]._serialized_start = 1338
    _globals["_STATEUPDATEREQUEST"]._serialized_end = 1469
    _globals["_STATEUPDATERESPONSE"]._serialized_start = 1472
    _globals["_STATEUPDATERESPONSE"]._serialized_end = 1623
    _globals["_STATEDELETEREQUEST"]._serialized_start = 1625
    _globals["_STATEDELETEREQUEST"]._serialized_end = 1713
    _globals["_STATEDELETERESPONSE"]._serialized_start = 1715
    _globals["_STATEDELETERESPONSE"]._serialized_end = 1811
    _globals["_STATESERVICE"]._serialized_start = 1814
    _globals["_STATESERVICE"]._serialized_end = 2318
# @@protoc_insertion_point(module_scope)
