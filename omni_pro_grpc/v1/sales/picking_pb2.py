# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/sales/picking.proto
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
    b'\n\x16v1/sales/picking.proto\x12!pro.omni.oms.api.v1.sales.picking\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x11\x63ommon/base.proto\x1a\x1cgoogle/protobuf/struct.proto"\x89\x02\n\x07Picking\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08order_id\x18\x03 \x01(\x05\x12\x16\n\x0epicking_sql_id\x18\x04 \x01(\x05\x12\x0e\n\x06picker\x18\x05 \x01(\t\x12(\n\x07\x63\x61rrier\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\x12*\n\x06\x61\x63tive\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x08 \x01(\t\x12?\n\x0cobject_audit\x18\t \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xab\x01\n\x14PickingCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08order_id\x18\x02 \x01(\x05\x12\x16\n\x0epicking_sql_id\x18\x03 \x01(\x05\x12\x13\n\x0b\x65xternal_id\x18\x04 \x01(\t\x12\x0e\n\x06picker\x18\x05 \x01(\t\x12\x36\n\x07\x63ontext\x18\x06 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9f\x01\n\x15PickingCreateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12;\n\x07picking\x18\x02 \x01(\x0b\x32*.pro.omni.oms.api.v1.sales.picking.Picking"\xf0\x02\n\x12PickingReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xd9\x01\n\x13PickingReadResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12<\n\x08pickings\x18\x03 \x03(\x0b\x32*.pro.omni.oms.api.v1.sales.picking.Picking"\x8b\x01\n\x14PickingUpdateRequest\x12;\n\x07picking\x18\x01 \x01(\x0b\x32*.pro.omni.oms.api.v1.sales.picking.Picking\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9f\x01\n\x15PickingUpdateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12;\n\x07picking\x18\x02 \x01(\x0b\x32*.pro.omni.oms.api.v1.sales.picking.Picking"Z\n\x14PickingDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"b\n\x15PickingDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xa5\x04\n\x0ePickingService\x12\x84\x01\n\rPickingCreate\x12\x37.pro.omni.oms.api.v1.sales.picking.PickingCreateRequest\x1a\x38.pro.omni.oms.api.v1.sales.picking.PickingCreateResponse"\x00\x12~\n\x0bPickingRead\x12\x35.pro.omni.oms.api.v1.sales.picking.PickingReadRequest\x1a\x36.pro.omni.oms.api.v1.sales.picking.PickingReadResponse"\x00\x12\x84\x01\n\rPickingUpdate\x12\x37.pro.omni.oms.api.v1.sales.picking.PickingUpdateRequest\x1a\x38.pro.omni.oms.api.v1.sales.picking.PickingUpdateResponse"\x00\x12\x84\x01\n\rPickingDelete\x12\x37.pro.omni.oms.api.v1.sales.picking.PickingDeleteRequest\x1a\x38.pro.omni.oms.api.v1.sales.picking.PickingDeleteResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.sales.picking_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _globals["_PICKING"]._serialized_start = 143
    _globals["_PICKING"]._serialized_end = 408
    _globals["_PICKINGCREATEREQUEST"]._serialized_start = 411
    _globals["_PICKINGCREATEREQUEST"]._serialized_end = 582
    _globals["_PICKINGCREATERESPONSE"]._serialized_start = 585
    _globals["_PICKINGCREATERESPONSE"]._serialized_end = 744
    _globals["_PICKINGREADREQUEST"]._serialized_start = 747
    _globals["_PICKINGREADREQUEST"]._serialized_end = 1115
    _globals["_PICKINGREADRESPONSE"]._serialized_start = 1118
    _globals["_PICKINGREADRESPONSE"]._serialized_end = 1335
    _globals["_PICKINGUPDATEREQUEST"]._serialized_start = 1338
    _globals["_PICKINGUPDATEREQUEST"]._serialized_end = 1477
    _globals["_PICKINGUPDATERESPONSE"]._serialized_start = 1480
    _globals["_PICKINGUPDATERESPONSE"]._serialized_end = 1639
    _globals["_PICKINGDELETEREQUEST"]._serialized_start = 1641
    _globals["_PICKINGDELETEREQUEST"]._serialized_end = 1731
    _globals["_PICKINGDELETERESPONSE"]._serialized_start = 1733
    _globals["_PICKINGDELETERESPONSE"]._serialized_end = 1831
    _globals["_PICKINGSERVICE"]._serialized_start = 1834
    _globals["_PICKINGSERVICE"]._serialized_end = 2383
# @@protoc_insertion_point(module_scope)
