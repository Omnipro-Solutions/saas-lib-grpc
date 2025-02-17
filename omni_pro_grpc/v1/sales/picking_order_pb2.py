# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/sales/picking_order.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from omni_pro_grpc.common import base_pb2 as common_dot_base__pb2
from omni_pro_grpc.v1.sales import order_pb2 as v1_dot_sales_dot_order__pb2
from omni_pro_grpc.v1.sales import picking_pb2 as v1_dot_sales_dot_picking__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1cv1/sales/picking_order.proto\x12\'pro.omni.oms.api.v1.sales.picking.order\x1a\x11\x63ommon/base.proto\x1a\x16v1/sales/picking.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x14v1/sales/order.proto"\x90\x02\n\x0cPickingOrder\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x35\n\x05order\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.v1.sales.order.Order\x12;\n\x07picking\x18\x03 \x01(\x0b\x32*.pro.omni.oms.api.v1.sales.picking.Picking\x12*\n\x06\x61\x63tive\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x05 \x01(\t\x12?\n\x0cobject_audit\x18\x06 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\x8e\x01\n\x19PickingOrderCreateRequest\x12\x10\n\x08order_id\x18\x01 \x01(\x05\x12\x12\n\npicking_id\x18\x02 \x01(\x05\x12\x13\n\x0b\x65xternal_id\x18\x03 \x01(\t\x12\x36\n\x07\x63ontext\x18\x04 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xb5\x01\n\x1aPickingOrderCreateResponse\x12L\n\rpicking_order\x18\x01 \x01(\x0b\x32\x35.pro.omni.oms.api.v1.sales.picking.order.PickingOrder\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xf5\x02\n\x17PickingOrderReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xef\x01\n\x18PickingOrderReadResponse\x12M\n\x0epicking_orders\x18\x01 \x03(\x0b\x32\x35.pro.omni.oms.api.v1.sales.picking.order.PickingOrder\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x03 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData"\xa1\x01\n\x19PickingOrderUpdateRequest\x12L\n\rpicking_order\x18\x01 \x01(\x0b\x32\x35.pro.omni.oms.api.v1.sales.picking.order.PickingOrder\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xb5\x01\n\x1aPickingOrderUpdateResponse\x12L\n\rpicking_order\x18\x01 \x01(\x0b\x32\x35.pro.omni.oms.api.v1.sales.picking.order.PickingOrder\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"_\n\x19PickingOrderDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xb5\x01\n\x1aPickingOrderDeleteResponse\x12L\n\rpicking_order\x18\x01 \x01(\x0b\x32\x35.pro.omni.oms.api.v1.sales.picking.order.PickingOrder\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\x9f\x06\n\x13PickingOrderService\x12\xc1\x01\n\x12PickingOrderCreate\x12\x42.pro.omni.oms.api.v1.sales.picking.order.PickingOrderCreateRequest\x1a\x43.pro.omni.oms.api.v1.sales.picking.order.PickingOrderCreateResponse""\x9a\xb5\x18\x1e\x08\x02\x12\x1a\x61pi/v1/sales/picking-order\x12\xbb\x01\n\x10PickingOrderRead\x12@.pro.omni.oms.api.v1.sales.picking.order.PickingOrderReadRequest\x1a\x41.pro.omni.oms.api.v1.sales.picking.order.PickingOrderReadResponse""\x9a\xb5\x18\x1e\x08\x01\x12\x1a\x61pi/v1/sales/picking-order\x12\xc1\x01\n\x12PickingOrderUpdate\x12\x42.pro.omni.oms.api.v1.sales.picking.order.PickingOrderUpdateRequest\x1a\x43.pro.omni.oms.api.v1.sales.picking.order.PickingOrderUpdateResponse""\x9a\xb5\x18\x1e\x08\x03\x12\x1a\x61pi/v1/sales/picking-order\x12\xc1\x01\n\x12PickingOrderDelete\x12\x42.pro.omni.oms.api.v1.sales.picking.order.PickingOrderDeleteRequest\x1a\x43.pro.omni.oms.api.v1.sales.picking.order.PickingOrderDeleteResponse""\x9a\xb5\x18\x1e\x08\x04\x12\x1a\x61pi/v1/sales/picking-orderb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.sales.picking_order_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _PICKINGORDERSERVICE.methods_by_name["PickingOrderCreate"]._options = None
    _PICKINGORDERSERVICE.methods_by_name["PickingOrderCreate"]._serialized_options = (
        b"\232\265\030\036\010\002\022\032api/v1/sales/picking-order"
    )
    _PICKINGORDERSERVICE.methods_by_name["PickingOrderRead"]._options = None
    _PICKINGORDERSERVICE.methods_by_name["PickingOrderRead"]._serialized_options = (
        b"\232\265\030\036\010\001\022\032api/v1/sales/picking-order"
    )
    _PICKINGORDERSERVICE.methods_by_name["PickingOrderUpdate"]._options = None
    _PICKINGORDERSERVICE.methods_by_name["PickingOrderUpdate"]._serialized_options = (
        b"\232\265\030\036\010\003\022\032api/v1/sales/picking-order"
    )
    _PICKINGORDERSERVICE.methods_by_name["PickingOrderDelete"]._options = None
    _PICKINGORDERSERVICE.methods_by_name["PickingOrderDelete"]._serialized_options = (
        b"\232\265\030\036\010\004\022\032api/v1/sales/picking-order"
    )
    _globals["_PICKINGORDER"]._serialized_start = 171
    _globals["_PICKINGORDER"]._serialized_end = 443
    _globals["_PICKINGORDERCREATEREQUEST"]._serialized_start = 446
    _globals["_PICKINGORDERCREATEREQUEST"]._serialized_end = 588
    _globals["_PICKINGORDERCREATERESPONSE"]._serialized_start = 591
    _globals["_PICKINGORDERCREATERESPONSE"]._serialized_end = 772
    _globals["_PICKINGORDERREADREQUEST"]._serialized_start = 775
    _globals["_PICKINGORDERREADREQUEST"]._serialized_end = 1148
    _globals["_PICKINGORDERREADRESPONSE"]._serialized_start = 1151
    _globals["_PICKINGORDERREADRESPONSE"]._serialized_end = 1390
    _globals["_PICKINGORDERUPDATEREQUEST"]._serialized_start = 1393
    _globals["_PICKINGORDERUPDATEREQUEST"]._serialized_end = 1554
    _globals["_PICKINGORDERUPDATERESPONSE"]._serialized_start = 1557
    _globals["_PICKINGORDERUPDATERESPONSE"]._serialized_end = 1738
    _globals["_PICKINGORDERDELETEREQUEST"]._serialized_start = 1740
    _globals["_PICKINGORDERDELETEREQUEST"]._serialized_end = 1835
    _globals["_PICKINGORDERDELETERESPONSE"]._serialized_start = 1838
    _globals["_PICKINGORDERDELETERESPONSE"]._serialized_end = 2019
    _globals["_PICKINGORDERSERVICE"]._serialized_start = 2022
    _globals["_PICKINGORDERSERVICE"]._serialized_end = 2821
# @@protoc_insertion_point(module_scope)
