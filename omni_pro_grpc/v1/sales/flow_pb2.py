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


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from omni_pro_grpc.common import base_pb2 as common_dot_base__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x13v1/sales/flow.proto\x12\x1epro.omni.oms.api.v1.sales.flow\x1a\x11\x63ommon/base.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xf1\x01\n\x04\x46low\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12*\n\x06\x61\x63tive\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x06 \x01(\t\x12*\n\tdraw_flow\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\x12?\n\x0cobject_audit\x18\x08 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xbd\x01\n\x11\x46lowCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x13\n\x0b\x65xternal_id\x18\x04 \x01(\t\x12*\n\tdraw_flow\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x36\n\x07\x63ontext\x18\x06 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x93\x01\n\x12\x46lowCreateResponse\x12\x32\n\x04\x66low\x18\x01 \x01(\x0b\x32$.pro.omni.oms.api.v1.sales.flow.Flow\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xed\x02\n\x0f\x46lowReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xcd\x01\n\x10\x46lowReadResponse\x12\x33\n\x05\x66lows\x18\x01 \x03(\x0b\x32$.pro.omni.oms.api.v1.sales.flow.Flow\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12I\n\x11response_standard\x18\x03 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\x7f\n\x11\x46lowUpdateRequest\x12\x32\n\x04\x66low\x18\x01 \x01(\x0b\x32$.pro.omni.oms.api.v1.sales.flow.Flow\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x93\x01\n\x12\x46lowUpdateResponse\x12\x32\n\x04\x66low\x18\x01 \x01(\x0b\x32$.pro.omni.oms.api.v1.sales.flow.Flow\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"W\n\x11\x46lowDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"_\n\x12\x46lowDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"P\n\x16\x46lowChangeStateRequest\x12\x36\n\x07\x63ontext\x18\x01 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x8e\x01\n\x17\x46lowChangeStateResponse\x12(\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.ListValue\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xd6\x05\n\x0b\x46lowService\x12\x8e\x01\n\nFlowCreate\x12\x31.pro.omni.oms.api.v1.sales.flow.FlowCreateRequest\x1a\x32.pro.omni.oms.api.v1.sales.flow.FlowCreateResponse"\x19\x9a\xb5\x18\x15\x08\x02\x12\x11\x61pi/v1/sales/flow\x12\x88\x01\n\x08\x46lowRead\x12/.pro.omni.oms.api.v1.sales.flow.FlowReadRequest\x1a\x30.pro.omni.oms.api.v1.sales.flow.FlowReadResponse"\x19\x9a\xb5\x18\x15\x08\x01\x12\x11\x61pi/v1/sales/flow\x12\x8e\x01\n\nFlowUpdate\x12\x31.pro.omni.oms.api.v1.sales.flow.FlowUpdateRequest\x1a\x32.pro.omni.oms.api.v1.sales.flow.FlowUpdateResponse"\x19\x9a\xb5\x18\x15\x08\x03\x12\x11\x61pi/v1/sales/flow\x12\x8e\x01\n\nFlowDelete\x12\x31.pro.omni.oms.api.v1.sales.flow.FlowDeleteRequest\x1a\x32.pro.omni.oms.api.v1.sales.flow.FlowDeleteResponse"\x19\x9a\xb5\x18\x15\x08\x04\x12\x11\x61pi/v1/sales/flow\x12\x88\x01\n\x0f\x46lowChangeState\x12\x36.pro.omni.oms.api.v1.sales.flow.FlowChangeStateRequest\x1a\x37.pro.omni.oms.api.v1.sales.flow.FlowChangeStateResponse"\x04\x90\xb5\x18\x01\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.sales.flow_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _FLOWSERVICE.methods_by_name["FlowCreate"]._options = None
    _FLOWSERVICE.methods_by_name["FlowCreate"]._serialized_options = (
        b"\232\265\030\025\010\002\022\021api/v1/sales/flow"
    )
    _FLOWSERVICE.methods_by_name["FlowRead"]._options = None
    _FLOWSERVICE.methods_by_name["FlowRead"]._serialized_options = b"\232\265\030\025\010\001\022\021api/v1/sales/flow"
    _FLOWSERVICE.methods_by_name["FlowUpdate"]._options = None
    _FLOWSERVICE.methods_by_name["FlowUpdate"]._serialized_options = (
        b"\232\265\030\025\010\003\022\021api/v1/sales/flow"
    )
    _FLOWSERVICE.methods_by_name["FlowDelete"]._options = None
    _FLOWSERVICE.methods_by_name["FlowDelete"]._serialized_options = (
        b"\232\265\030\025\010\004\022\021api/v1/sales/flow"
    )
    _FLOWSERVICE.methods_by_name["FlowChangeState"]._options = None
    _FLOWSERVICE.methods_by_name["FlowChangeState"]._serialized_options = b"\220\265\030\001"
    _globals["_FLOW"]._serialized_start = 137
    _globals["_FLOW"]._serialized_end = 378
    _globals["_FLOWCREATEREQUEST"]._serialized_start = 381
    _globals["_FLOWCREATEREQUEST"]._serialized_end = 570
    _globals["_FLOWCREATERESPONSE"]._serialized_start = 573
    _globals["_FLOWCREATERESPONSE"]._serialized_end = 720
    _globals["_FLOWREADREQUEST"]._serialized_start = 723
    _globals["_FLOWREADREQUEST"]._serialized_end = 1088
    _globals["_FLOWREADRESPONSE"]._serialized_start = 1091
    _globals["_FLOWREADRESPONSE"]._serialized_end = 1296
    _globals["_FLOWUPDATEREQUEST"]._serialized_start = 1298
    _globals["_FLOWUPDATEREQUEST"]._serialized_end = 1425
    _globals["_FLOWUPDATERESPONSE"]._serialized_start = 1428
    _globals["_FLOWUPDATERESPONSE"]._serialized_end = 1575
    _globals["_FLOWDELETEREQUEST"]._serialized_start = 1577
    _globals["_FLOWDELETEREQUEST"]._serialized_end = 1664
    _globals["_FLOWDELETERESPONSE"]._serialized_start = 1666
    _globals["_FLOWDELETERESPONSE"]._serialized_end = 1761
    _globals["_FLOWCHANGESTATEREQUEST"]._serialized_start = 1763
    _globals["_FLOWCHANGESTATEREQUEST"]._serialized_end = 1843
    _globals["_FLOWCHANGESTATERESPONSE"]._serialized_start = 1846
    _globals["_FLOWCHANGESTATERESPONSE"]._serialized_end = 1988
    _globals["_FLOWSERVICE"]._serialized_start = 1991
    _globals["_FLOWSERVICE"]._serialized_end = 2717
# @@protoc_insertion_point(module_scope)
