# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/sales/order.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from omni_pro_grpc.common import base_pb2 as common_dot_base__pb2
from omni_pro_grpc.v1.sales import address_pb2 as v1_dot_sales_dot_address__pb2
from omni_pro_grpc.v1.sales import carrier_pb2 as v1_dot_sales_dot_carrier__pb2
from omni_pro_grpc.v1.sales import delivery_method_pb2 as v1_dot_sales_dot_delivery__method__pb2
from omni_pro_grpc.v1.sales import flow_pb2 as v1_dot_sales_dot_flow__pb2
from omni_pro_grpc.v1.sales import picking_pb2 as v1_dot_sales_dot_picking__pb2
from omni_pro_grpc.v1.sales import sale_pb2 as v1_dot_sales_dot_sale__pb2
from omni_pro_grpc.v1.sales import state_pb2 as v1_dot_sales_dot_state__pb2
from omni_pro_grpc.v1.sales import warehouse_pb2 as v1_dot_sales_dot_warehouse__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x14v1/sales/order.proto\x12\x1fpro.omni.oms.api.v1.sales.order\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x16v1/sales/address.proto\x1a\x13v1/sales/sale.proto\x1a\x16v1/sales/picking.proto\x1a\x1ev1/sales/delivery_method.proto\x1a\x18v1/sales/warehouse.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x16v1/sales/carrier.proto\x1a\x14v1/sales/state.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x13v1/sales/flow.proto"\xb2\n\n\x05Order\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x32\n\x04sale\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.v1.sales.sale.Sale\x12@\n\x0cship_address\x18\x04 \x01(\x0b\x32*.pro.omni.oms.api.v1.sales.address.Address\x12R\n\x0f\x64\x65livery_method\x18\x05 \x01(\x0b\x32\x39.pro.omni.oms.api.v1.sales.delivery.method.DeliveryMethod\x12<\n\x08\x63\x61rriers\x18\x06 \x03(\x0b\x32*.pro.omni.oms.api.v1.sales.carrier.Carrier\x12\x11\n\ttax_total\x18\x07 \x01(\x02\x12\x16\n\x0e\x64iscount_total\x18\x08 \x01(\x02\x12\x10\n\x08subtotal\x18\t \x01(\x02\x12\r\n\x05total\x18\n \x01(\x02\x12*\n\x06\x61\x63tive\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x0c \x01(\t\x12\x41\n\twarehouse\x18\r \x01(\x0b\x32..pro.omni.oms.api.v1.sales.warehouse.Warehouse\x12\x0b\n\x03\x63id\x18\x0e \x01(\t\x12 \n\x18shipping_amount_subtotal\x18\x0f \x01(\x02\x12 \n\x18shipping_amount_discount\x18\x10 \x01(\x02\x12\x1b\n\x13shipping_amount_tax\x18\x11 \x01(\x02\x12\x1d\n\x15shipping_amount_total\x18\x12 \x01(\x02\x12,\n$shipping_amount_discount_description\x18\x13 \x01(\t\x12\x15\n\rtype_delivery\x18\x14 \x01(\t\x12\x11\n\tconfirmed\x18\x15 \x01(\x08\x12\x35\n\x05state\x18\x16 \x01(\x0b\x32&.pro.omni.oms.api.v1.sales.state.State\x12\x32\n\x04\x66low\x18\x17 \x01(\x0b\x32$.pro.omni.oms.api.v1.sales.flow.Flow\x12\x35\n\x14sale_stock_operation\x18\x18 \x03(\x0b\x32\x17.google.protobuf.Struct\x12<\n\x08pickings\x18\x19 \x03(\x0b\x32*.pro.omni.oms.api.v1.sales.picking.Picking\x12?\n\x0cobject_audit\x18\x1a \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit\x12,\n\x0border_lines\x18\x1b \x03(\x0b\x32\x17.google.protobuf.Struct\x12\x31\n\rdate_delivery\x18\x1c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x44\n\rorder_history\x18\x1d \x03(\x0b\x32-.pro.omni.oms.api.v1.sales.order.OrderHistory\x12\x1c\n\x14substitution_applied\x18\x1e \x01(\x05\x12\x16\n\x0e\x64\x65livery_hours\x18\x1f \x01(\t\x12\x16\n\x0e\x64\x65livery_total\x18  \x01(\x02\x12(\n\x07summary\x18! \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x12\n\nexceptions\x18" \x03(\t"\xb5\x04\n\x0cOrderHistory\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07\x66low_id\x18\x02 \x01(\x05\x12\x11\n\tflow_name\x18\x03 \x01(\t\x12\x35\n\x05order\x18\x04 \x01(\x0b\x32&.pro.omni.oms.api.v1.sales.order.Order\x12\x19\n\x11previous_state_id\x18\x05 \x01(\x05\x12\x1b\n\x13previous_state_name\x18\x06 \x01(\t\x12\x1b\n\x13previous_state_type\x18\x07 \x01(\t\x12"\n\x1aprevious_state_description\x18\x08 \x01(\t\x12\x18\n\x10\x63urrent_state_id\x18\t \x01(\x05\x12\x1a\n\x12\x63urrent_state_name\x18\n \x01(\t\x12\x1a\n\x12\x63urrent_state_type\x18\x0b \x01(\t\x12!\n\x19\x63urrent_state_description\x18\x0c \x01(\t\x12\x15\n\rtransition_id\x18\r \x01(\x05\x12\x17\n\x0ftransition_type\x18\x0e \x01(\t\x12\r\n\x05logic\x18\x0f \x01(\t\x12\x32\n\x0esend_ecommerce\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x1c\n\x14substitution_applied\x18\x11 \x01(\x05\x12?\n\x0cobject_audit\x18\x12 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xb8\x05\n\x12OrderCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07sale_id\x18\x02 \x01(\x05\x12\x19\n\x11ship_address_code\x18\x03 \x01(\t\x12\x1a\n\x12\x64\x65livery_method_id\x18\x04 \x01(\x05\x12\x13\n\x0b\x63\x61rrier_ids\x18\x05 \x03(\x05\x12\x11\n\ttax_total\x18\x06 \x01(\x02\x12\x16\n\x0e\x64iscount_total\x18\x07 \x01(\x02\x12\x10\n\x08subtotal\x18\x08 \x01(\x02\x12\r\n\x05total\x18\t \x01(\x02\x12\x13\n\x0b\x65xternal_id\x18\n \x01(\t\x12\x14\n\x0cwarehouse_id\x18\x0b \x01(\x05\x12\x0b\n\x03\x63id\x18\x0c \x01(\t\x12 \n\x18shipping_amount_subtotal\x18\r \x01(\x02\x12 \n\x18shipping_amount_discount\x18\x0e \x01(\x02\x12\x1b\n\x13shipping_amount_tax\x18\x0f \x01(\x02\x12\x1d\n\x15shipping_amount_total\x18\x10 \x01(\x02\x12,\n$shipping_amount_discount_description\x18\x11 \x01(\t\x12\x15\n\rtype_delivery\x18\x12 \x01(\t\x12\x10\n\x08state_id\x18\x13 \x01(\x05\x12\x0f\n\x07\x66low_id\x18\x14 \x01(\x05\x12\x11\n\tconfirmed\x18\x15 \x01(\x08\x12\x16\n\x0e\x64\x65livery_hours\x18\x16 \x01(\t\x12\x35\n\x14sale_stock_operation\x18\x17 \x03(\x0b\x32\x17.google.protobuf.Struct\x12\x36\n\x07\x63ontext\x18\x18 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context\x12\x31\n\rdate_delivery\x18\x19 \x01(\x0b\x32\x1a.google.protobuf.Timestamp"\x97\x01\n\x13OrderCreateResponse\x12\x35\n\x05order\x18\x01 \x01(\x0b\x32&.pro.omni.oms.api.v1.sales.order.Order\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xee\x02\n\x10OrderReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xd1\x01\n\x11OrderReadResponse\x12\x36\n\x06orders\x18\x01 \x03(\x0b\x32&.pro.omni.oms.api.v1.sales.order.Order\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x03 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData"\x83\x01\n\x12OrderUpdateRequest\x12\x35\n\x05order\x18\x01 \x01(\x0b\x32&.pro.omni.oms.api.v1.sales.order.Order\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x97\x01\n\x13OrderUpdateResponse\x12\x35\n\x05order\x18\x01 \x01(\x0b\x32&.pro.omni.oms.api.v1.sales.order.Order\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"X\n\x12OrderDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"`\n\x13OrderDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"w\n\x13OrderConfirmRequest\x12(\n\x07payload\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x8b\x01\n\x14OrderConfirmResponse\x12(\n\x07\x63onfirm\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"}\n\x19SaleStockOperationRequest\x12(\n\x07payload\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x8e\x01\n\x1aSaleStockOperationResponse\x12%\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x17.google.protobuf.Struct\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"c\n\x17OrderChangeStateRequest\x12\x10\n\x08order_id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9c\x01\n\x18OrderChangeStateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x35\n\x05order\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.v1.sales.order.Order"\xa5\x01\n OrderLineDeliveryQuantityRequest\x12\x10\n\x08order_id\x18\x01 \x01(\x05\x12\x0f\n\x07sale_id\x18\x02 \x01(\x05\x12&\n\x05items\x18\x03 \x03(\x0b\x32\x17.google.protobuf.Struct\x12\x36\n\x07\x63ontext\x18\x04 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"n\n!OrderLineDeliveryQuantityResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"a\n\x14\x43onfirmOrdersRequest\x12\x11\n\torder_ids\x18\x01 \x03(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"g\n\x13\x43onfirmOrdersResult\x12\x10\n\x08order_id\x18\x01 \x01(\x05\x12-\n\tconfirmed\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x0f\n\x07message\x18\x03 \x01(\t"\xa8\x01\n\x15\x43onfirmOrdersResponse\x12\x44\n\x06result\x18\x01 \x03(\x0b\x32\x34.pro.omni.oms.api.v1.sales.order.ConfirmOrdersResult\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xbf\t\n\x0cOrderService\x12z\n\x0bOrderCreate\x12\x33.pro.omni.oms.api.v1.sales.order.OrderCreateRequest\x1a\x34.pro.omni.oms.api.v1.sales.order.OrderCreateResponse"\x00\x12t\n\tOrderRead\x12\x31.pro.omni.oms.api.v1.sales.order.OrderReadRequest\x1a\x32.pro.omni.oms.api.v1.sales.order.OrderReadResponse"\x00\x12z\n\x0bOrderUpdate\x12\x33.pro.omni.oms.api.v1.sales.order.OrderUpdateRequest\x1a\x34.pro.omni.oms.api.v1.sales.order.OrderUpdateResponse"\x00\x12z\n\x0bOrderDelete\x12\x33.pro.omni.oms.api.v1.sales.order.OrderDeleteRequest\x1a\x34.pro.omni.oms.api.v1.sales.order.OrderDeleteResponse"\x00\x12}\n\x0cOrderConfirm\x12\x34.pro.omni.oms.api.v1.sales.order.OrderConfirmRequest\x1a\x35.pro.omni.oms.api.v1.sales.order.OrderConfirmResponse"\x00\x12\x8f\x01\n\x12SaleStockOperation\x12:.pro.omni.oms.api.v1.sales.order.SaleStockOperationRequest\x1a;.pro.omni.oms.api.v1.sales.order.SaleStockOperationResponse"\x00\x12\x89\x01\n\x10OrderChangeState\x12\x38.pro.omni.oms.api.v1.sales.order.OrderChangeStateRequest\x1a\x39.pro.omni.oms.api.v1.sales.order.OrderChangeStateResponse"\x00\x12\xa4\x01\n\x19OrderLineDeliveryQuantity\x12\x41.pro.omni.oms.api.v1.sales.order.OrderLineDeliveryQuantityRequest\x1a\x42.pro.omni.oms.api.v1.sales.order.OrderLineDeliveryQuantityResponse"\x00\x12\x80\x01\n\rConfirmOrders\x12\x35.pro.omni.oms.api.v1.sales.order.ConfirmOrdersRequest\x1a\x36.pro.omni.oms.api.v1.sales.order.ConfirmOrdersResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.sales.order_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _globals["_ORDER"]._serialized_start = 366
    _globals["_ORDER"]._serialized_end = 1696
    _globals["_ORDERHISTORY"]._serialized_start = 1699
    _globals["_ORDERHISTORY"]._serialized_end = 2264
    _globals["_ORDERCREATEREQUEST"]._serialized_start = 2267
    _globals["_ORDERCREATEREQUEST"]._serialized_end = 2963
    _globals["_ORDERCREATERESPONSE"]._serialized_start = 2966
    _globals["_ORDERCREATERESPONSE"]._serialized_end = 3117
    _globals["_ORDERREADREQUEST"]._serialized_start = 3120
    _globals["_ORDERREADREQUEST"]._serialized_end = 3486
    _globals["_ORDERREADRESPONSE"]._serialized_start = 3489
    _globals["_ORDERREADRESPONSE"]._serialized_end = 3698
    _globals["_ORDERUPDATEREQUEST"]._serialized_start = 3701
    _globals["_ORDERUPDATEREQUEST"]._serialized_end = 3832
    _globals["_ORDERUPDATERESPONSE"]._serialized_start = 3835
    _globals["_ORDERUPDATERESPONSE"]._serialized_end = 3986
    _globals["_ORDERDELETEREQUEST"]._serialized_start = 3988
    _globals["_ORDERDELETEREQUEST"]._serialized_end = 4076
    _globals["_ORDERDELETERESPONSE"]._serialized_start = 4078
    _globals["_ORDERDELETERESPONSE"]._serialized_end = 4174
    _globals["_ORDERCONFIRMREQUEST"]._serialized_start = 4176
    _globals["_ORDERCONFIRMREQUEST"]._serialized_end = 4295
    _globals["_ORDERCONFIRMRESPONSE"]._serialized_start = 4298
    _globals["_ORDERCONFIRMRESPONSE"]._serialized_end = 4437
    _globals["_SALESTOCKOPERATIONREQUEST"]._serialized_start = 4439
    _globals["_SALESTOCKOPERATIONREQUEST"]._serialized_end = 4564
    _globals["_SALESTOCKOPERATIONRESPONSE"]._serialized_start = 4567
    _globals["_SALESTOCKOPERATIONRESPONSE"]._serialized_end = 4709
    _globals["_ORDERCHANGESTATEREQUEST"]._serialized_start = 4711
    _globals["_ORDERCHANGESTATEREQUEST"]._serialized_end = 4810
    _globals["_ORDERCHANGESTATERESPONSE"]._serialized_start = 4813
    _globals["_ORDERCHANGESTATERESPONSE"]._serialized_end = 4969
    _globals["_ORDERLINEDELIVERYQUANTITYREQUEST"]._serialized_start = 4972
    _globals["_ORDERLINEDELIVERYQUANTITYREQUEST"]._serialized_end = 5137
    _globals["_ORDERLINEDELIVERYQUANTITYRESPONSE"]._serialized_start = 5139
    _globals["_ORDERLINEDELIVERYQUANTITYRESPONSE"]._serialized_end = 5249
    _globals["_CONFIRMORDERSREQUEST"]._serialized_start = 5251
    _globals["_CONFIRMORDERSREQUEST"]._serialized_end = 5348
    _globals["_CONFIRMORDERSRESULT"]._serialized_start = 5350
    _globals["_CONFIRMORDERSRESULT"]._serialized_end = 5453
    _globals["_CONFIRMORDERSRESPONSE"]._serialized_start = 5456
    _globals["_CONFIRMORDERSRESPONSE"]._serialized_end = 5624
    _globals["_ORDERSERVICE"]._serialized_start = 5627
    _globals["_ORDERSERVICE"]._serialized_end = 6842
# @@protoc_insertion_point(module_scope)
