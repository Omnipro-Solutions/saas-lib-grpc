# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/sales/flow.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from omni_pro_grpc.common import base_pb2 as common_dot_base__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from omni_pro_grpc.v1.sales import state_pb2 as v1_dot_sales_dot_state__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13v1/sales/flow.proto\x12\x1epro.omni.oms.api.v1.sales.flow\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x14v1/sales/state.proto\"\x84\x02\n\x04\x46low\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12=\n\rinitial_state\x18\x04 \x01(\x0b\x32&.pro.omni.oms.api.v1.sales.state.State\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12*\n\x06\x61\x63tive\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x07 \x01(\t\x12?\n\x0cobject_audit\x18\x08 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit\"\xab\x01\n\x11\x46lowCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x18\n\x10initial_state_id\x18\x03 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x13\n\x0b\x65xternal_id\x18\x05 \x01(\t\x12\x36\n\x07\x63ontext\x18\x06 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context\"\x93\x01\n\x12\x46lowCreateResponse\x12\x32\n\x04\x66low\x18\x01 \x01(\x0b\x32$.pro.omni.oms.api.v1.sales.flow.Flow\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\"\xed\x02\n\x0f\x46lowReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context\"\xcd\x01\n\x10\x46lowReadResponse\x12\x33\n\x05\x66lows\x18\x01 \x03(\x0b\x32$.pro.omni.oms.api.v1.sales.flow.Flow\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12I\n\x11response_standard\x18\x03 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\"\x7f\n\x11\x46lowUpdateRequest\x12\x32\n\x04\x66low\x18\x01 \x01(\x0b\x32$.pro.omni.oms.api.v1.sales.flow.Flow\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context\"\x93\x01\n\x12\x46lowUpdateResponse\x12\x32\n\x04\x66low\x18\x01 \x01(\x0b\x32$.pro.omni.oms.api.v1.sales.flow.Flow\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\"W\n\x11\x46lowDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context\"_\n\x12\x46lowDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xe3\x03\n\x0b\x46lowService\x12u\n\nFlowCreate\x12\x31.pro.omni.oms.api.v1.sales.flow.FlowCreateRequest\x1a\x32.pro.omni.oms.api.v1.sales.flow.FlowCreateResponse\"\x00\x12o\n\x08\x46lowRead\x12/.pro.omni.oms.api.v1.sales.flow.FlowReadRequest\x1a\x30.pro.omni.oms.api.v1.sales.flow.FlowReadResponse\"\x00\x12u\n\nFlowUpdate\x12\x31.pro.omni.oms.api.v1.sales.flow.FlowUpdateRequest\x1a\x32.pro.omni.oms.api.v1.sales.flow.FlowUpdateResponse\"\x00\x12u\n\nFlowDelete\x12\x31.pro.omni.oms.api.v1.sales.flow.FlowDeleteRequest\x1a\x32.pro.omni.oms.api.v1.sales.flow.FlowDeleteResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'v1.sales.flow_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_FLOW']._serialized_start=129
  _globals['_FLOW']._serialized_end=389
  _globals['_FLOWCREATEREQUEST']._serialized_start=392
  _globals['_FLOWCREATEREQUEST']._serialized_end=563
  _globals['_FLOWCREATERESPONSE']._serialized_start=566
  _globals['_FLOWCREATERESPONSE']._serialized_end=713
  _globals['_FLOWREADREQUEST']._serialized_start=716
  _globals['_FLOWREADREQUEST']._serialized_end=1081
  _globals['_FLOWREADRESPONSE']._serialized_start=1084
  _globals['_FLOWREADRESPONSE']._serialized_end=1289
  _globals['_FLOWUPDATEREQUEST']._serialized_start=1291
  _globals['_FLOWUPDATEREQUEST']._serialized_end=1418
  _globals['_FLOWUPDATERESPONSE']._serialized_start=1421
  _globals['_FLOWUPDATERESPONSE']._serialized_end=1568
  _globals['_FLOWDELETEREQUEST']._serialized_start=1570
  _globals['_FLOWDELETEREQUEST']._serialized_end=1657
  _globals['_FLOWDELETERESPONSE']._serialized_start=1659
  _globals['_FLOWDELETERESPONSE']._serialized_end=1754
  _globals['_FLOWSERVICE']._serialized_start=1757
  _globals['_FLOWSERVICE']._serialized_end=2240
# @@protoc_insertion_point(module_scope)
