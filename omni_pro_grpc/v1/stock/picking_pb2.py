# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/stock/picking.proto
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
from omni_pro_grpc.v1.stock import address_pb2 as v1_dot_stock_dot_address__pb2
from omni_pro_grpc.v1.stock import attachment_pb2 as v1_dot_stock_dot_attachment__pb2
from omni_pro_grpc.v1.stock import carrier_pb2 as v1_dot_stock_dot_carrier__pb2
from omni_pro_grpc.v1.stock import client_pb2 as v1_dot_stock_dot_client__pb2
from omni_pro_grpc.v1.stock import delivery_method_pb2 as v1_dot_stock_dot_delivery__method__pb2
from omni_pro_grpc.v1.stock import location_pb2 as v1_dot_stock_dot_location__pb2
from omni_pro_grpc.v1.stock import order_pb2 as v1_dot_stock_dot_order__pb2
from omni_pro_grpc.v1.stock import payment_method_pb2 as v1_dot_stock_dot_payment__method__pb2
from omni_pro_grpc.v1.stock import (
    picking_integration_operation_pb2 as v1_dot_stock_dot_picking__integration__operation__pb2,
)
from omni_pro_grpc.v1.stock import picking_type_pb2 as v1_dot_stock_dot_picking__type__pb2
from omni_pro_grpc.v1.stock import procurement_group_pb2 as v1_dot_stock_dot_procurement__group__pb2
from omni_pro_grpc.v1.stock import sale_pb2 as v1_dot_stock_dot_sale__pb2
from omni_pro_grpc.v1.stock import user_pb2 as v1_dot_stock_dot_user__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x16v1/stock/picking.proto\x12!pro.omni.oms.api.v1.stock.picking\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x17v1/stock/location.proto\x1a\x1bv1/stock/picking_type.proto\x1a\x16v1/stock/carrier.proto\x1a v1/stock/procurement_group.proto\x1a\x19v1/stock/attachment.proto\x1a\x15v1/stock/client.proto\x1a\x1ev1/stock/delivery_method.proto\x1a\x14v1/stock/order.proto\x1a\x1dv1/stock/payment_method.proto\x1a\x13v1/stock/sale.proto\x1a\x13v1/stock/user.proto\x1a\x16v1/stock/address.proto\x1a,v1/stock/picking_integration_operation.proto"\xf1\x0f\n\x07Picking\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12I\n\x0cpicking_type\x18\x03 \x01(\x0b\x32\x33.pro.omni.oms.api.v1.stock.picking_type.PickingType\x12>\n\x08location\x18\x04 \x01(\x0b\x32,.pro.omni.oms.api.v1.stock.location.Location\x12\x43\n\rlocation_dest\x18\x05 \x01(\x0b\x32,.pro.omni.oms.api.v1.stock.location.Location\x12J\n\x10\x61ttachment_guide\x18\x06 \x01(\x0b\x32\x30.pro.omni.oms.api.v1.stock.attachment.Attachment\x12L\n\x12\x61ttachment_invoice\x18\x07 \x01(\x0b\x32\x30.pro.omni.oms.api.v1.stock.attachment.Attachment\x12\x0e\n\x06origin\x18\x08 \x01(\t\x12:\n\x16\x64\x61te_start_preparation\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\tdate_done\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\x0escheduled_date\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1e\n\x16time_total_preparation\x18\x0c \x01(\x02\x12\x15\n\rtime_assigned\x18\r \x01(\x02\x12;\n\x07\x63\x61rrier\x18\x0e \x01(\x0b\x32*.pro.omni.oms.api.v1.stock.carrier.Carrier\x12\x1c\n\x14\x63\x61rrier_tracking_ref\x18\x0f \x01(\t\x12L\n\x05group\x18\x10 \x01(\x0b\x32=.pro.omni.oms.api.v1.stock.procurement_group.ProcurementGroup\x12\x0e\n\x06weight\x18\x11 \x01(\x02\x12\x17\n\x0fshipping_weight\x18\x12 \x01(\x02\x12\r\n\x05state\x18\x13 \x01(\t\x12@\n\ndependency\x18\x14 \x01(\x0b\x32,.pro.omni.oms.api.common.base.ObjectResponse\x12\x0c\n\x04note\x18\x15 \x01(\t\x12\x1c\n\x14\x63\x61rrier_tracking_url\x18\x16 \x01(\t\x12\x32\n\x11shipping_receives\x18\x17 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x32\n\x0e\x64\x61te_validated\x18\x18 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0fsale_date_order\x18\x19 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x38\n\x06\x63lient\x18\x1a \x01(\x0b\x32(.pro.omni.oms.api.v1.stock.client.Client\x12R\n\x0f\x64\x65livery_method\x18\x1b \x01(\x0b\x32\x39.pro.omni.oms.api.v1.stock.delivery_method.DeliveryMethod\x12\x35\n\x05order\x18\x1c \x01(\x0b\x32&.pro.omni.oms.api.v1.stock.order.Order\x12O\n\x0epayment_method\x18\x1d \x01(\x0b\x32\x37.pro.omni.oms.api.v1.stock.payment_method.PaymentMethod\x12\x32\n\x04sale\x18\x1e \x01(\x0b\x32$.pro.omni.oms.api.v1.stock.sale.Sale\x12\x32\n\x04user\x18\x1f \x01(\x0b\x32$.pro.omni.oms.api.v1.stock.user.User\x12\x44\n\x10shipping_address\x18  \x01(\x0b\x32*.pro.omni.oms.api.v1.stock.address.Address\x12*\n\x06\x61\x63tive\x18! \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12*\n\twarehouse\x18" \x01(\x0b\x32\x17.google.protobuf.Struct\x12,\n\x0bstock_moves\x18# \x03(\x0b\x32\x17.google.protobuf.Struct\x12\x31\n\x10stock_move_lines\x18$ \x03(\x0b\x32\x17.google.protobuf.Struct\x12?\n\x1b\x63heck_integration_operation\x18% \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12|\n\x1epicking_integration_operations\x18& \x03(\x0b\x32T.pro.omni.oms.api.v1.stock.picking_integration_operation.PickingIntegrationOperation\x12\x13\n\x0b\x65xternal_id\x18\' \x01(\t\x12?\n\x0cobject_audit\x18( \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xea\x07\n\x14PickingCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x17\n\x0fpicking_type_id\x18\x02 \x01(\x05\x12\x13\n\x0blocation_id\x18\x03 \x01(\x05\x12\x18\n\x10location_dest_id\x18\x04 \x01(\x05\x12\x1b\n\x13\x61ttachment_guide_id\x18\x05 \x01(\x05\x12\x1d\n\x15\x61ttachment_invoice_id\x18\x06 \x01(\x05\x12\x0e\n\x06origin\x18\x07 \x01(\t\x12:\n\x16\x64\x61te_start_preparation\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\tdate_done\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\x0escheduled_date\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1e\n\x16time_total_preparation\x18\x0b \x01(\x02\x12\x15\n\rtime_assigned\x18\x0c \x01(\x02\x12\x12\n\ncarrier_id\x18\r \x01(\x05\x12\x1c\n\x14\x63\x61rrier_tracking_ref\x18\x0e \x01(\t\x12\x10\n\x08group_id\x18\x0f \x01(\x05\x12\x0e\n\x06weight\x18\x10 \x01(\x02\x12\x17\n\x0fshipping_weight\x18\x11 \x01(\x02\x12\r\n\x05state\x18\x12 \x01(\t\x12\x15\n\rdependency_id\x18\x13 \x01(\x05\x12\x0c\n\x04note\x18\x14 \x01(\t\x12\x1c\n\x14\x63\x61rrier_tracking_url\x18\x15 \x01(\t\x12\x32\n\x0e\x64\x61te_validated\x18\x16 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0fsale_date_order\x18\x17 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\tclient_id\x18\x18 \x01(\t\x12\x1a\n\x12\x64\x65livery_method_id\x18\x19 \x01(\t\x12\x10\n\x08order_id\x18\x1a \x01(\x05\x12\x19\n\x11payment_method_id\x18\x1b \x01(\t\x12\x0f\n\x07sale_id\x18\x1c \x01(\x05\x12\x0f\n\x07user_id\x18\x1d \x01(\t\x12\x1d\n\x15shipping_address_code\x18\x1e \x01(\t\x12\x14\n\x0cwarehouse_id\x18\x1f \x01(\x05\x12\x32\n\x11shipping_receives\x18  \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x13\n\x0b\x65xternal_id\x18! \x01(\t\x12\x36\n\x07\x63ontext\x18" \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9f\x01\n\x15PickingCreateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12;\n\x07picking\x18\x02 \x01(\x0b\x32*.pro.omni.oms.api.v1.stock.picking.Picking"\xf0\x02\n\x12PickingReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xd9\x01\n\x13PickingReadResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12<\n\x08pickings\x18\x03 \x03(\x0b\x32*.pro.omni.oms.api.v1.stock.picking.Picking"\x8b\x01\n\x14PickingUpdateRequest\x12;\n\x07picking\x18\x01 \x01(\x0b\x32*.pro.omni.oms.api.v1.stock.picking.Picking\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9f\x01\n\x15PickingUpdateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12;\n\x07picking\x18\x02 \x01(\x0b\x32*.pro.omni.oms.api.v1.stock.picking.Picking"Z\n\x14PickingDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"b\n\x15PickingDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xc9\x01\n\x16ValidatePickingRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x33\n\x0fpicking_partial\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x36\n\x12immediate_transfer\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x36\n\x07\x63ontext\x18\x04 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x8b\x01\n\x17ValidatePickingResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12%\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct"Y\n\x13PickingMovesRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x88\x01\n\x14PickingMovesResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12%\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct"z\n\x13OrderConfirmRequest\x12+\n\norder_data\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9f\x01\n\x14OrderConfirmResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12<\n\x08pickings\x18\x02 \x03(\x0b\x32*.pro.omni.oms.api.v1.stock.picking.Picking"s\n\x12SalePickingRequest\x12%\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9e\x01\n\x13SalePickingResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12<\n\x08pickings\x18\x02 \x03(\x0b\x32*.pro.omni.oms.api.v1.stock.picking.Picking"\xf6\x02\n\x18PickingKanbanReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xc8\x01\n\x19PickingKanbanReadResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12%\n\x04\x64\x61ta\x18\x03 \x03(\x0b\x32\x17.google.protobuf.Struct"x\n\x17PickingProcessorRequest\x12%\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xa3\x01\n\x18PickingProcessorResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12<\n\x08pickings\x18\x02 \x03(\x0b\x32*.pro.omni.oms.api.v1.stock.picking.Picking"^\n\x18\x43heckAvailabilityRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x8d\x01\n\x19\x43heckAvailabilityResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12%\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct"\x97\x01\n&GetProductAvailableSubstitutionRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12)\n\x08products\x18\x02 \x03(\x0b\x32\x17.google.protobuf.Struct\x12\x36\n\x07\x63ontext\x18\x03 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x95\x02\n\'GetProductAvailableSubstitutionResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12)\n\x08products\x18\x02 \x03(\x0b\x32\x17.google.protobuf.Struct\x12\x14\n\x0cnot_products\x18\x03 \x03(\t\x12%\n\x1dproduct_without_available_qty\x18\x04 \x03(\t\x12\x37\n\x16products_partial_stock\x18\x05 \x03(\x0b\x32\x17.google.protobuf.Struct"\x86\x01\n\x15ReplaceProductRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12)\n\x08products\x18\x02 \x03(\x0b\x32\x17.google.protobuf.Struct\x12\x36\n\x07\x63ontext\x18\x03 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"c\n\x16ReplaceProductResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"[\n\x14\x43\x61ncelPickingRequest\x12\x0b\n\x03ids\x18\x01 \x03(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x93\x01\n\x15\x43\x61ncelPickingResponse\x12/\n\x0e\x63\x61ncel_picking\x18\x01 \x03(\x0b\x32\x17.google.protobuf.Struct\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"v\n\x18\x44\x65letePickingSaleRequest\x12\x0f\n\x07sale_id\x18\x01 \x01(\x05\x12\x11\n\tsale_name\x18\x02 \x01(\t\x12\x36\n\x07\x63ontext\x18\x03 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x8f\x01\n\x19\x44\x65letePickingSaleResponse\x12\'\n\x06result\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xa5\x01\n(UpdatePickingIntegrationOperationRequest\x12\x12\n\npicking_id\x18\x01 \x01(\x05\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\x12\x0f\n\x07message\x18\x04 \x01(\t\x12\x36\n\x07\x63ontext\x18\x05 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xf3\x01\n)UpdatePickingIntegrationOperationResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12{\n\x1dpicking_integration_operation\x18\x02 \x01(\x0b\x32T.pro.omni.oms.api.v1.stock.picking_integration_operation.PickingIntegrationOperation2\xdf\x14\n\x0ePickingService\x12\xa0\x01\n\rPickingCreate\x12\x37.pro.omni.oms.api.v1.stock.picking.PickingCreateRequest\x1a\x38.pro.omni.oms.api.v1.stock.picking.PickingCreateResponse"\x1c\x9a\xb5\x18\x18\x08\x02\x12\x14\x61pi/v1/stock/picking\x12\x9a\x01\n\x0bPickingRead\x12\x35.pro.omni.oms.api.v1.stock.picking.PickingReadRequest\x1a\x36.pro.omni.oms.api.v1.stock.picking.PickingReadResponse"\x1c\x9a\xb5\x18\x18\x08\x01\x12\x14\x61pi/v1/stock/picking\x12\xa0\x01\n\rPickingUpdate\x12\x37.pro.omni.oms.api.v1.stock.picking.PickingUpdateRequest\x1a\x38.pro.omni.oms.api.v1.stock.picking.PickingUpdateResponse"\x1c\x9a\xb5\x18\x18\x08\x03\x12\x14\x61pi/v1/stock/picking\x12\xa0\x01\n\rPickingDelete\x12\x37.pro.omni.oms.api.v1.stock.picking.PickingDeleteRequest\x1a\x38.pro.omni.oms.api.v1.stock.picking.PickingDeleteResponse"\x1c\x9a\xb5\x18\x18\x08\x04\x12\x14\x61pi/v1/stock/picking\x12\xb7\x01\n\x0fValidatePicking\x12\x39.pro.omni.oms.api.v1.stock.picking.ValidatePickingRequest\x1a:.pro.omni.oms.api.v1.stock.picking.ValidatePickingResponse"-\x9a\xb5\x18)\x08\x02\x12%api/v1/stock/picking/validate-picking\x12\x85\x01\n\x0cOrderConfirm\x12\x36.pro.omni.oms.api.v1.stock.picking.OrderConfirmRequest\x1a\x37.pro.omni.oms.api.v1.stock.picking.OrderConfirmResponse"\x04\x90\xb5\x18\x01\x12\x82\x01\n\x0bSalePicking\x12\x35.pro.omni.oms.api.v1.stock.picking.SalePickingRequest\x1a\x36.pro.omni.oms.api.v1.stock.picking.SalePickingResponse"\x04\x90\xb5\x18\x01\x12\xaf\x01\n\rPickingKanban\x12;.pro.omni.oms.api.v1.stock.picking.PickingKanbanReadRequest\x1a<.pro.omni.oms.api.v1.stock.picking.PickingKanbanReadResponse"#\x9a\xb5\x18\x1f\x08\x01\x12\x1b\x61pi/v1/stock/picking/kanban\x12\xc7\x01\n\x11\x43heckAvailability\x12;.pro.omni.oms.api.v1.stock.picking.CheckAvailabilityRequest\x1a<.pro.omni.oms.api.v1.stock.picking.CheckAvailabilityResponse"7\x9a\xb5\x18\x33\x08\x02\x12/api/v1/stock/picking/check/availability/picking\x12\xf5\x01\n\x1fGetProductAvailableSubstitution\x12I.pro.omni.oms.api.v1.stock.picking.GetProductAvailableSubstitutionRequest\x1aJ.pro.omni.oms.api.v1.stock.picking.GetProductAvailableSubstitutionResponse";\x9a\xb5\x18\x37\x08\x02\x12\x33\x61pi/v1/stock/picking/product/available/substitution\x12\xb9\x01\n\x0eReplaceProduct\x12\x38.pro.omni.oms.api.v1.stock.picking.ReplaceProductRequest\x1a\x39.pro.omni.oms.api.v1.stock.picking.ReplaceProductResponse"2\x9a\xb5\x18.\x08\x02\x12*api/v1/stock/picking/product/apply/replace\x12\xaf\x01\n\rCancelPicking\x12\x37.pro.omni.oms.api.v1.stock.picking.CancelPickingRequest\x1a\x38.pro.omni.oms.api.v1.stock.picking.CancelPickingResponse"+\x9a\xb5\x18\'\x08\x02\x12#api/v1/stock/picking/cancel-picking\x12\x91\x01\n\x10PickingProcessor\x12:.pro.omni.oms.api.v1.stock.picking.PickingProcessorRequest\x1a;.pro.omni.oms.api.v1.stock.picking.PickingProcessorResponse"\x04\x90\xb5\x18\x01\x12\x94\x01\n\x11\x44\x65letePickingSale\x12;.pro.omni.oms.api.v1.stock.picking.DeletePickingSaleRequest\x1a<.pro.omni.oms.api.v1.stock.picking.DeletePickingSaleResponse"\x04\x90\xb5\x18\x01\x12\xf2\x01\n!UpdatePickingIntegrationOperation\x12K.pro.omni.oms.api.v1.stock.picking.UpdatePickingIntegrationOperationRequest\x1aL.pro.omni.oms.api.v1.stock.picking.UpdatePickingIntegrationOperationResponse"2\x9a\xb5\x18.\x08\x03\x12*api/v1/stock/picking/integration-operationb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.stock.picking_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _PICKINGSERVICE.methods_by_name["PickingCreate"]._options = None
    _PICKINGSERVICE.methods_by_name["PickingCreate"]._serialized_options = (
        b"\232\265\030\030\010\002\022\024api/v1/stock/picking"
    )
    _PICKINGSERVICE.methods_by_name["PickingRead"]._options = None
    _PICKINGSERVICE.methods_by_name["PickingRead"]._serialized_options = (
        b"\232\265\030\030\010\001\022\024api/v1/stock/picking"
    )
    _PICKINGSERVICE.methods_by_name["PickingUpdate"]._options = None
    _PICKINGSERVICE.methods_by_name["PickingUpdate"]._serialized_options = (
        b"\232\265\030\030\010\003\022\024api/v1/stock/picking"
    )
    _PICKINGSERVICE.methods_by_name["PickingDelete"]._options = None
    _PICKINGSERVICE.methods_by_name["PickingDelete"]._serialized_options = (
        b"\232\265\030\030\010\004\022\024api/v1/stock/picking"
    )
    _PICKINGSERVICE.methods_by_name["ValidatePicking"]._options = None
    _PICKINGSERVICE.methods_by_name["ValidatePicking"]._serialized_options = (
        b"\232\265\030)\010\002\022%api/v1/stock/picking/validate-picking"
    )
    _PICKINGSERVICE.methods_by_name["OrderConfirm"]._options = None
    _PICKINGSERVICE.methods_by_name["OrderConfirm"]._serialized_options = b"\220\265\030\001"
    _PICKINGSERVICE.methods_by_name["SalePicking"]._options = None
    _PICKINGSERVICE.methods_by_name["SalePicking"]._serialized_options = b"\220\265\030\001"
    _PICKINGSERVICE.methods_by_name["PickingKanban"]._options = None
    _PICKINGSERVICE.methods_by_name["PickingKanban"]._serialized_options = (
        b"\232\265\030\037\010\001\022\033api/v1/stock/picking/kanban"
    )
    _PICKINGSERVICE.methods_by_name["CheckAvailability"]._options = None
    _PICKINGSERVICE.methods_by_name["CheckAvailability"]._serialized_options = (
        b"\232\265\0303\010\002\022/api/v1/stock/picking/check/availability/picking"
    )
    _PICKINGSERVICE.methods_by_name["GetProductAvailableSubstitution"]._options = None
    _PICKINGSERVICE.methods_by_name["GetProductAvailableSubstitution"]._serialized_options = (
        b"\232\265\0307\010\002\0223api/v1/stock/picking/product/available/substitution"
    )
    _PICKINGSERVICE.methods_by_name["ReplaceProduct"]._options = None
    _PICKINGSERVICE.methods_by_name["ReplaceProduct"]._serialized_options = (
        b"\232\265\030.\010\002\022*api/v1/stock/picking/product/apply/replace"
    )
    _PICKINGSERVICE.methods_by_name["CancelPicking"]._options = None
    _PICKINGSERVICE.methods_by_name["CancelPicking"]._serialized_options = (
        b"\232\265\030'\010\002\022#api/v1/stock/picking/cancel-picking"
    )
    _PICKINGSERVICE.methods_by_name["PickingProcessor"]._options = None
    _PICKINGSERVICE.methods_by_name["PickingProcessor"]._serialized_options = b"\220\265\030\001"
    _PICKINGSERVICE.methods_by_name["DeletePickingSale"]._options = None
    _PICKINGSERVICE.methods_by_name["DeletePickingSale"]._serialized_options = b"\220\265\030\001"
    _PICKINGSERVICE.methods_by_name["UpdatePickingIntegrationOperation"]._options = None
    _PICKINGSERVICE.methods_by_name["UpdatePickingIntegrationOperation"]._serialized_options = (
        b"\232\265\030.\010\003\022*api/v1/stock/picking/integration-operation"
    )
    _globals["_PICKING"]._serialized_start = 535
    _globals["_PICKING"]._serialized_end = 2568
    _globals["_PICKINGCREATEREQUEST"]._serialized_start = 2571
    _globals["_PICKINGCREATEREQUEST"]._serialized_end = 3573
    _globals["_PICKINGCREATERESPONSE"]._serialized_start = 3576
    _globals["_PICKINGCREATERESPONSE"]._serialized_end = 3735
    _globals["_PICKINGREADREQUEST"]._serialized_start = 3738
    _globals["_PICKINGREADREQUEST"]._serialized_end = 4106
    _globals["_PICKINGREADRESPONSE"]._serialized_start = 4109
    _globals["_PICKINGREADRESPONSE"]._serialized_end = 4326
    _globals["_PICKINGUPDATEREQUEST"]._serialized_start = 4329
    _globals["_PICKINGUPDATEREQUEST"]._serialized_end = 4468
    _globals["_PICKINGUPDATERESPONSE"]._serialized_start = 4471
    _globals["_PICKINGUPDATERESPONSE"]._serialized_end = 4630
    _globals["_PICKINGDELETEREQUEST"]._serialized_start = 4632
    _globals["_PICKINGDELETEREQUEST"]._serialized_end = 4722
    _globals["_PICKINGDELETERESPONSE"]._serialized_start = 4724
    _globals["_PICKINGDELETERESPONSE"]._serialized_end = 4822
    _globals["_VALIDATEPICKINGREQUEST"]._serialized_start = 4825
    _globals["_VALIDATEPICKINGREQUEST"]._serialized_end = 5026
    _globals["_VALIDATEPICKINGRESPONSE"]._serialized_start = 5029
    _globals["_VALIDATEPICKINGRESPONSE"]._serialized_end = 5168
    _globals["_PICKINGMOVESREQUEST"]._serialized_start = 5170
    _globals["_PICKINGMOVESREQUEST"]._serialized_end = 5259
    _globals["_PICKINGMOVESRESPONSE"]._serialized_start = 5262
    _globals["_PICKINGMOVESRESPONSE"]._serialized_end = 5398
    _globals["_ORDERCONFIRMREQUEST"]._serialized_start = 5400
    _globals["_ORDERCONFIRMREQUEST"]._serialized_end = 5522
    _globals["_ORDERCONFIRMRESPONSE"]._serialized_start = 5525
    _globals["_ORDERCONFIRMRESPONSE"]._serialized_end = 5684
    _globals["_SALEPICKINGREQUEST"]._serialized_start = 5686
    _globals["_SALEPICKINGREQUEST"]._serialized_end = 5801
    _globals["_SALEPICKINGRESPONSE"]._serialized_start = 5804
    _globals["_SALEPICKINGRESPONSE"]._serialized_end = 5962
    _globals["_PICKINGKANBANREADREQUEST"]._serialized_start = 5965
    _globals["_PICKINGKANBANREADREQUEST"]._serialized_end = 6339
    _globals["_PICKINGKANBANREADRESPONSE"]._serialized_start = 6342
    _globals["_PICKINGKANBANREADRESPONSE"]._serialized_end = 6542
    _globals["_PICKINGPROCESSORREQUEST"]._serialized_start = 6544
    _globals["_PICKINGPROCESSORREQUEST"]._serialized_end = 6664
    _globals["_PICKINGPROCESSORRESPONSE"]._serialized_start = 6667
    _globals["_PICKINGPROCESSORRESPONSE"]._serialized_end = 6830
    _globals["_CHECKAVAILABILITYREQUEST"]._serialized_start = 6832
    _globals["_CHECKAVAILABILITYREQUEST"]._serialized_end = 6926
    _globals["_CHECKAVAILABILITYRESPONSE"]._serialized_start = 6929
    _globals["_CHECKAVAILABILITYRESPONSE"]._serialized_end = 7070
    _globals["_GETPRODUCTAVAILABLESUBSTITUTIONREQUEST"]._serialized_start = 7073
    _globals["_GETPRODUCTAVAILABLESUBSTITUTIONREQUEST"]._serialized_end = 7224
    _globals["_GETPRODUCTAVAILABLESUBSTITUTIONRESPONSE"]._serialized_start = 7227
    _globals["_GETPRODUCTAVAILABLESUBSTITUTIONRESPONSE"]._serialized_end = 7504
    _globals["_REPLACEPRODUCTREQUEST"]._serialized_start = 7507
    _globals["_REPLACEPRODUCTREQUEST"]._serialized_end = 7641
    _globals["_REPLACEPRODUCTRESPONSE"]._serialized_start = 7643
    _globals["_REPLACEPRODUCTRESPONSE"]._serialized_end = 7742
    _globals["_CANCELPICKINGREQUEST"]._serialized_start = 7744
    _globals["_CANCELPICKINGREQUEST"]._serialized_end = 7835
    _globals["_CANCELPICKINGRESPONSE"]._serialized_start = 7838
    _globals["_CANCELPICKINGRESPONSE"]._serialized_end = 7985
    _globals["_DELETEPICKINGSALEREQUEST"]._serialized_start = 7987
    _globals["_DELETEPICKINGSALEREQUEST"]._serialized_end = 8105
    _globals["_DELETEPICKINGSALERESPONSE"]._serialized_start = 8108
    _globals["_DELETEPICKINGSALERESPONSE"]._serialized_end = 8251
    _globals["_UPDATEPICKINGINTEGRATIONOPERATIONREQUEST"]._serialized_start = 8254
    _globals["_UPDATEPICKINGINTEGRATIONOPERATIONREQUEST"]._serialized_end = 8419
    _globals["_UPDATEPICKINGINTEGRATIONOPERATIONRESPONSE"]._serialized_start = 8422
    _globals["_UPDATEPICKINGINTEGRATIONOPERATIONRESPONSE"]._serialized_end = 8665
    _globals["_PICKINGSERVICE"]._serialized_start = 8668
    _globals["_PICKINGSERVICE"]._serialized_end = 11323
# @@protoc_insertion_point(module_scope)
