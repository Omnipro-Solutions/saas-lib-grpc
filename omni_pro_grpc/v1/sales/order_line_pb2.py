# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/sales/order_line.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from omni_pro_grpc.common import base_pb2 as common_dot_base__pb2
from omni_pro_grpc.v1.sales import product_pb2 as v1_dot_sales_dot_product__pb2
from omni_pro_grpc.v1.sales import uom_pb2 as v1_dot_sales_dot_uom__pb2
from omni_pro_grpc.v1.sales import order_pb2 as v1_dot_sales_dot_order__pb2
from omni_pro_grpc.v1.sales import tax_pb2 as v1_dot_sales_dot_tax__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19v1/sales/order_line.proto\x12$pro.omni.oms.api.v1.sales.order.line\x1a\x11\x63ommon/base.proto\x1a\x16v1/sales/product.proto\x1a\x12v1/sales/uom.proto\x1a\x14v1/sales/order.proto\x1a\x12v1/sales/tax.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xec\x03\n\tOrderLine\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x35\n\x05order\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.v1.sales.order.Order\x12;\n\x07product\x18\x03 \x01(\x0b\x32*.pro.omni.oms.api.v1.sales.product.Product\x12\x10\n\x08quantity\x18\x04 \x01(\x02\x12/\n\x03uom\x18\x05 \x01(\x0b\x32\".pro.omni.oms.api.v1.sales.uom.Uom\x12\x12\n\nprice_unit\x18\x06 \x01(\x02\x12\x31\n\x05taxes\x18\x07 \x03(\x0b\x32\".pro.omni.oms.api.v1.sales.tax.Tax\x12\x10\n\x08\x64iscount\x18\x08 \x01(\x02\x12\x13\n\x0bprice_total\x18\t \x01(\x02\x12\x11\n\tsub_total\x18\n \x01(\x02\x12\x19\n\x11\x65\x63ommerce_item_id\x18\x0b \x01(\t\x12*\n\x06\x61\x63tive\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\r \x01(\t\x12?\n\x0cobject_audit\x18\x0e \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit\"\xa8\x02\n\x16OrderLineCreateRequest\x12\x10\n\x08order_id\x18\x01 \x01(\x05\x12\x12\n\nproduct_id\x18\x02 \x01(\t\x12\x10\n\x08quantity\x18\x03 \x01(\x02\x12\x0e\n\x06uom_id\x18\x04 \x01(\t\x12\x12\n\nprice_unit\x18\x05 \x01(\x02\x12\x10\n\x08taxes_id\x18\x06 \x03(\x05\x12\x10\n\x08\x64iscount\x18\x07 \x01(\x02\x12\x13\n\x0bprice_total\x18\x08 \x01(\x02\x12\x11\n\tsub_total\x18\t \x01(\x02\x12\x19\n\x11\x65\x63ommerce_item_id\x18\n \x01(\t\x12\x13\n\x0b\x65xternal_id\x18\x0b \x01(\t\x12\x36\n\x07\x63ontext\x18\x0c \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context\"\xa9\x01\n\x17OrderLineCreateResponse\x12\x43\n\norder_line\x18\x01 \x01(\x0b\x32/.pro.omni.oms.api.v1.sales.order.line.OrderLine\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\"\xf2\x02\n\x14OrderLineReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context\"\xe3\x01\n\x15OrderLineReadResponse\x12\x44\n\x0border_lines\x18\x01 \x03(\x0b\x32/.pro.omni.oms.api.v1.sales.order.line.OrderLine\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x03 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\"\x95\x01\n\x16OrderLineUpdateRequest\x12\x43\n\norder_line\x18\x01 \x01(\x0b\x32/.pro.omni.oms.api.v1.sales.order.line.OrderLine\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context\"\xa9\x01\n\x17OrderLineUpdateResponse\x12\x43\n\norder_line\x18\x01 \x01(\x0b\x32/.pro.omni.oms.api.v1.sales.order.line.OrderLine\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\"\\\n\x16OrderLineDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context\"d\n\x17OrderLineDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xd8\x04\n\x10OrderLineService\x12\x90\x01\n\x0fOrderLineCreate\x12<.pro.omni.oms.api.v1.sales.order.line.OrderLineCreateRequest\x1a=.pro.omni.oms.api.v1.sales.order.line.OrderLineCreateResponse\"\x00\x12\x8a\x01\n\rOrderLineRead\x12:.pro.omni.oms.api.v1.sales.order.line.OrderLineReadRequest\x1a;.pro.omni.oms.api.v1.sales.order.line.OrderLineReadResponse\"\x00\x12\x90\x01\n\x0fOrderLineUpdate\x12<.pro.omni.oms.api.v1.sales.order.line.OrderLineUpdateRequest\x1a=.pro.omni.oms.api.v1.sales.order.line.OrderLineUpdateResponse\"\x00\x12\x90\x01\n\x0fOrderLineDelete\x12<.pro.omni.oms.api.v1.sales.order.line.OrderLineDeleteRequest\x1a=.pro.omni.oms.api.v1.sales.order.line.OrderLineDeleteResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'v1.sales.order_line_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_ORDERLINE']._serialized_start=205
  _globals['_ORDERLINE']._serialized_end=697
  _globals['_ORDERLINECREATEREQUEST']._serialized_start=700
  _globals['_ORDERLINECREATEREQUEST']._serialized_end=996
  _globals['_ORDERLINECREATERESPONSE']._serialized_start=999
  _globals['_ORDERLINECREATERESPONSE']._serialized_end=1168
  _globals['_ORDERLINEREADREQUEST']._serialized_start=1171
  _globals['_ORDERLINEREADREQUEST']._serialized_end=1541
  _globals['_ORDERLINEREADRESPONSE']._serialized_start=1544
  _globals['_ORDERLINEREADRESPONSE']._serialized_end=1771
  _globals['_ORDERLINEUPDATEREQUEST']._serialized_start=1774
  _globals['_ORDERLINEUPDATEREQUEST']._serialized_end=1923
  _globals['_ORDERLINEUPDATERESPONSE']._serialized_start=1926
  _globals['_ORDERLINEUPDATERESPONSE']._serialized_end=2095
  _globals['_ORDERLINEDELETEREQUEST']._serialized_start=2097
  _globals['_ORDERLINEDELETEREQUEST']._serialized_end=2189
  _globals['_ORDERLINEDELETERESPONSE']._serialized_start=2191
  _globals['_ORDERLINEDELETERESPONSE']._serialized_end=2291
  _globals['_ORDERLINESERVICE']._serialized_start=2294
  _globals['_ORDERLINESERVICE']._serialized_end=2894
# @@protoc_insertion_point(module_scope)
