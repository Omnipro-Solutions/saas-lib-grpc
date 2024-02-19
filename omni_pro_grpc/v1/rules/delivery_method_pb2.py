# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/rules/delivery_method.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from omni_pro_grpc.common import base_pb2 as common_dot_base__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from omni_pro_grpc.v1.rules import warehouse_pb2 as v1_dot_rules_dot_warehouse__pb2
from omni_pro_grpc.v1.rules import location_pb2 as v1_dot_rules_dot_location__pb2
from omni_pro_grpc.v1.rules import delivery_warehouse_pb2 as v1_dot_rules_dot_delivery__warehouse__pb2
from omni_pro_grpc.v1.rules import delivery_category_pb2 as v1_dot_rules_dot_delivery__category__pb2
from omni_pro_grpc.v1.rules import delivery_locality_pb2 as v1_dot_rules_dot_delivery__locality__pb2
from omni_pro_grpc.v1.rules import delivery_schedule_pb2 as v1_dot_rules_dot_delivery__schedule__pb2
from omni_pro_grpc.v1.rules import stock_security_pb2 as v1_dot_rules_dot_stock__security__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ev1/rules/delivery_method.proto\x12)pro.omni.oms.api.v1.rules.delivery_method\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x18v1/rules/warehouse.proto\x1a\x17v1/rules/location.proto\x1a!v1/rules/delivery_warehouse.proto\x1a v1/rules/delivery_category.proto\x1a v1/rules/delivery_locality.proto\x1a v1/rules/delivery_schedule.proto\x1a\x1dv1/rules/stock_security.proto\"\xf8\x07\n\x0e\x44\x65liveryMethod\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12K\n\x13\x64\x65livery_warehouses\x18\x03 \x03(\x0b\x32..pro.omni.oms.api.v1.rules.warehouse.Warehouse\x12\x1d\n\x15type_picking_transfer\x18\x04 \x01(\t\x12\x1f\n\x17validate_warehouse_code\x18\x05 \x01(\t\x12\x36\n\x11quantity_security\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x0c\n\x04\x63ode\x18\x07 \x01(\t\x12\x15\n\rtype_delivery\x18\x08 \x01(\t\x12G\n\x11\x64\x65livery_location\x18\t \x01(\x0b\x32,.pro.omni.oms.api.v1.rules.location.Location\x12Z\n\x11transfer_template\x18\n \x01(\x0b\x32?.pro.omni.oms.api.v1.rules.delivery_warehouse.DeliveryWarehouse\x12X\n\x11\x63\x61tegory_template\x18\x0b \x01(\x0b\x32=.pro.omni.oms.api.v1.rules.delivery_category.DeliveryCategory\x12Y\n\x12locality_available\x18\x0c \x01(\x0b\x32=.pro.omni.oms.api.v1.rules.delivery_locality.DeliveryLocality\x12X\n\x11schedule_template\x18\r \x01(\x0b\x32=.pro.omni.oms.api.v1.rules.delivery_schedule.DeliverySchedule\x12O\n\x0estock_security\x18\x0e \x01(\x0b\x32\x37.pro.omni.oms.api.v1.rules.stock_security.StockSecurity\x12H\n$transfer_between_delivery_warehouses\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12*\n\x06\x61\x63tive\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x11 \x01(\t\x12\x11\n\ttime_zone\x18\x12 \x01(\t\x12?\n\x0cobject_audit\x18\x13 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit\"\xa7\x04\n\x1b\x44\x65liveryMethodCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1d\n\x15type_picking_transfer\x18\x02 \x01(\t\x12\x1f\n\x17validate_warehouse_code\x18\x03 \x01(\t\x12\x19\n\x11quantity_security\x18\x04 \x01(\x02\x12\x0c\n\x04\x63ode\x18\x05 \x01(\t\x12\x15\n\rtype_delivery\x18\x06 \x01(\t\x12\x1c\n\x14\x64\x65livery_location_id\x18\x07 \x01(\x05\x12\x1c\n\x14transfer_template_id\x18\x08 \x01(\t\x12\x1c\n\x14\x63\x61tegory_template_id\x18\t \x01(\t\x12\x1d\n\x15locality_available_id\x18\n \x01(\t\x12\x1c\n\x14schedule_template_id\x18\x0b \x01(\t\x12\x19\n\x11stock_security_id\x18\x0c \x01(\t\x12\x1e\n\x16\x64\x65livery_warehouse_ids\x18\r \x03(\x05\x12H\n$transfer_between_delivery_warehouses\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x0f \x01(\t\x12\x11\n\ttime_zone\x18\x10 \x01(\t\x12\x36\n\x07\x63ontext\x18\x11 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context\"\xbd\x01\n\x1c\x44\x65liveryMethodCreateResponse\x12R\n\x0f\x64\x65livery_method\x18\x01 \x01(\x0b\x32\x39.pro.omni.oms.api.v1.rules.delivery_method.DeliveryMethod\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\"\xf7\x02\n\x19\x44\x65liveryMethodReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\t\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context\"\xf7\x01\n\x1a\x44\x65liveryMethodReadResponse\x12S\n\x10\x64\x65livery_methods\x18\x01 \x03(\x0b\x32\x39.pro.omni.oms.api.v1.rules.delivery_method.DeliveryMethod\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12I\n\x11response_standard\x18\x03 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\"\xa9\x01\n\x1b\x44\x65liveryMethodUpdateRequest\x12R\n\x0f\x64\x65livery_method\x18\x01 \x01(\x0b\x32\x39.pro.omni.oms.api.v1.rules.delivery_method.DeliveryMethod\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context\"\xbd\x01\n\x1c\x44\x65liveryMethodUpdateResponse\x12R\n\x0f\x64\x65livery_method\x18\x01 \x01(\x0b\x32\x39.pro.omni.oms.api.v1.rules.delivery_method.DeliveryMethod\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\"a\n\x1b\x44\x65liveryMethodDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context\"i\n\x1c\x44\x65liveryMethodDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\"\x91\x01\n\x1b\x41\x64\x64\x44\x65liveryWarehouseRequest\x12\x1a\n\x12\x64\x65livery_method_id\x18\x01 \x01(\t\x12\x1e\n\x16\x64\x65livery_warehouse_ids\x18\x02 \x03(\x05\x12\x36\n\x07\x63ontext\x18\x03 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context\"\xbd\x01\n\x1c\x41\x64\x64\x44\x65liveryWarehouseResponse\x12R\n\x0f\x64\x65livery_method\x18\x01 \x01(\x0b\x32\x39.pro.omni.oms.api.v1.rules.delivery_method.DeliveryMethod\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\"\x94\x01\n\x1eRemoveDeliveryWarehouseRequest\x12\x1a\n\x12\x64\x65livery_method_id\x18\x01 \x01(\t\x12\x1e\n\x16\x64\x65livery_warehouse_ids\x18\x02 \x03(\x05\x12\x36\n\x07\x63ontext\x18\x03 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context\"\xc0\x01\n\x1fRemoveDeliveryWarehouseResponse\x12R\n\x0f\x64\x65livery_method\x18\x01 \x01(\x0b\x32\x39.pro.omni.oms.api.v1.rules.delivery_method.DeliveryMethod\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xa2\x08\n\x15\x44\x65liveryMethodService\x12\xa9\x01\n\x14\x44\x65liveryMethodCreate\x12\x46.pro.omni.oms.api.v1.rules.delivery_method.DeliveryMethodCreateRequest\x1aG.pro.omni.oms.api.v1.rules.delivery_method.DeliveryMethodCreateResponse\"\x00\x12\xa3\x01\n\x12\x44\x65liveryMethodRead\x12\x44.pro.omni.oms.api.v1.rules.delivery_method.DeliveryMethodReadRequest\x1a\x45.pro.omni.oms.api.v1.rules.delivery_method.DeliveryMethodReadResponse\"\x00\x12\xa9\x01\n\x14\x44\x65liveryMethodUpdate\x12\x46.pro.omni.oms.api.v1.rules.delivery_method.DeliveryMethodUpdateRequest\x1aG.pro.omni.oms.api.v1.rules.delivery_method.DeliveryMethodUpdateResponse\"\x00\x12\xa9\x01\n\x14\x44\x65liveryMethodDelete\x12\x46.pro.omni.oms.api.v1.rules.delivery_method.DeliveryMethodDeleteRequest\x1aG.pro.omni.oms.api.v1.rules.delivery_method.DeliveryMethodDeleteResponse\"\x00\x12\xa9\x01\n\x14\x41\x64\x64\x44\x65liveryWarehouse\x12\x46.pro.omni.oms.api.v1.rules.delivery_method.AddDeliveryWarehouseRequest\x1aG.pro.omni.oms.api.v1.rules.delivery_method.AddDeliveryWarehouseResponse\"\x00\x12\xb2\x01\n\x17RemoveDeliveryWarehouse\x12I.pro.omni.oms.api.v1.rules.delivery_method.RemoveDeliveryWarehouseRequest\x1aJ.pro.omni.oms.api.v1.rules.delivery_method.RemoveDeliveryWarehouseResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'v1.rules.delivery_method_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_DELIVERYMETHOD']._serialized_start=348
  _globals['_DELIVERYMETHOD']._serialized_end=1364
  _globals['_DELIVERYMETHODCREATEREQUEST']._serialized_start=1367
  _globals['_DELIVERYMETHODCREATEREQUEST']._serialized_end=1918
  _globals['_DELIVERYMETHODCREATERESPONSE']._serialized_start=1921
  _globals['_DELIVERYMETHODCREATERESPONSE']._serialized_end=2110
  _globals['_DELIVERYMETHODREADREQUEST']._serialized_start=2113
  _globals['_DELIVERYMETHODREADREQUEST']._serialized_end=2488
  _globals['_DELIVERYMETHODREADRESPONSE']._serialized_start=2491
  _globals['_DELIVERYMETHODREADRESPONSE']._serialized_end=2738
  _globals['_DELIVERYMETHODUPDATEREQUEST']._serialized_start=2741
  _globals['_DELIVERYMETHODUPDATEREQUEST']._serialized_end=2910
  _globals['_DELIVERYMETHODUPDATERESPONSE']._serialized_start=2913
  _globals['_DELIVERYMETHODUPDATERESPONSE']._serialized_end=3102
  _globals['_DELIVERYMETHODDELETEREQUEST']._serialized_start=3104
  _globals['_DELIVERYMETHODDELETEREQUEST']._serialized_end=3201
  _globals['_DELIVERYMETHODDELETERESPONSE']._serialized_start=3203
  _globals['_DELIVERYMETHODDELETERESPONSE']._serialized_end=3308
  _globals['_ADDDELIVERYWAREHOUSEREQUEST']._serialized_start=3311
  _globals['_ADDDELIVERYWAREHOUSEREQUEST']._serialized_end=3456
  _globals['_ADDDELIVERYWAREHOUSERESPONSE']._serialized_start=3459
  _globals['_ADDDELIVERYWAREHOUSERESPONSE']._serialized_end=3648
  _globals['_REMOVEDELIVERYWAREHOUSEREQUEST']._serialized_start=3651
  _globals['_REMOVEDELIVERYWAREHOUSEREQUEST']._serialized_end=3799
  _globals['_REMOVEDELIVERYWAREHOUSERESPONSE']._serialized_start=3802
  _globals['_REMOVEDELIVERYWAREHOUSERESPONSE']._serialized_end=3994
  _globals['_DELIVERYMETHODSERVICE']._serialized_start=3997
  _globals['_DELIVERYMETHODSERVICE']._serialized_end=5055
# @@protoc_insertion_point(module_scope)
