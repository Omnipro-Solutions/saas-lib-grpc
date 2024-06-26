# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/stock/state.proto
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
    b'\n\x14v1/stock/state.proto\x12\x1fpro.omni.oms.api.v1.stock.state\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xd6\x01\n\x05State\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x14\n\x0cstate_sql_id\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04\x63ode\x18\x04 \x01(\t\x12\r\n\x05\x63olor\x18\x05 \x01(\t\x12*\n\x06\x61\x63tive\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x07 \x01(\t\x12?\n\x0cobject_audit\x18\x08 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\x83\x01\n\x12StateUpdateRequest\x12\x35\n\x05state\x18\x01 \x01(\x0b\x32&.pro.omni.oms.api.v1.stock.state.State\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x97\x01\n\x13StateUpdateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x35\n\x05state\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.v1.stock.state.State"X\n\x12StateDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"`\n\x13StateDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\x86\x02\n\x0cStateService\x12z\n\x0bStateUpdate\x12\x33.pro.omni.oms.api.v1.stock.state.StateUpdateRequest\x1a\x34.pro.omni.oms.api.v1.stock.state.StateUpdateResponse"\x00\x12z\n\x0bStateDelete\x12\x33.pro.omni.oms.api.v1.stock.state.StateDeleteRequest\x1a\x34.pro.omni.oms.api.v1.stock.state.StateDeleteResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.stock.state_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _globals["_STATE"]._serialized_start = 109
    _globals["_STATE"]._serialized_end = 323
    _globals["_STATEUPDATEREQUEST"]._serialized_start = 326
    _globals["_STATEUPDATEREQUEST"]._serialized_end = 457
    _globals["_STATEUPDATERESPONSE"]._serialized_start = 460
    _globals["_STATEUPDATERESPONSE"]._serialized_end = 611
    _globals["_STATEDELETEREQUEST"]._serialized_start = 613
    _globals["_STATEDELETEREQUEST"]._serialized_end = 701
    _globals["_STATEDELETERESPONSE"]._serialized_start = 703
    _globals["_STATEDELETERESPONSE"]._serialized_end = 799
    _globals["_STATESERVICE"]._serialized_start = 802
    _globals["_STATESERVICE"]._serialized_end = 1064
# @@protoc_insertion_point(module_scope)
