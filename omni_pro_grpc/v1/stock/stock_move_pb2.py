# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/stock/stock_move.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from omni_pro_grpc.common import base_pb2 as common_dot_base__pb2
from omni_pro_grpc.v1.stock import picking_pb2 as v1_dot_stock_dot_picking__pb2
from omni_pro_grpc.v1.stock import product_pb2 as v1_dot_stock_dot_product__pb2
from omni_pro_grpc.v1.stock import uom_pb2 as v1_dot_stock_dot_uom__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x19v1/stock/stock_move.proto\x12$pro.omni.oms.api.v1.stock.stock_move\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x16v1/stock/picking.proto\x1a\x16v1/stock/product.proto\x1a\x12v1/stock/uom.proto"\xdf\x03\n\tStockMove\x12\n\n\x02id\x18\x01 \x01(\x05\x12;\n\x07picking\x18\x02 \x01(\x0b\x32*.pro.omni.oms.api.v1.stock.picking.Picking\x12\r\n\x05state\x18\x03 \x01(\t\x12;\n\x07product\x18\x04 \x01(\x0b\x32*.pro.omni.oms.api.v1.stock.product.Product\x12\x32\n\rquantity_done\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x37\n\x0bproduct_uom\x18\x06 \x01(\x0b\x32".pro.omni.oms.api.v1.stock.uom.Uom\x12\x1b\n\x13\x64\x65scription_picking\x18\x07 \x01(\t\x12\x31\n\x0cqty_reserved\x18\x08 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12*\n\x06\x61\x63tive\x18\t \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\n \x01(\t\x12?\n\x0cobject_audit\x18\x0b \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xb8\x02\n\x16StockMoveCreateRequest\x12\x12\n\npicking_id\x18\x01 \x01(\x05\x12\r\n\x05state\x18\x02 \x01(\t\x12\x12\n\nproduct_id\x18\x03 \x01(\t\x12\x32\n\rquantity_done\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x16\n\x0eproduct_uom_id\x18\x05 \x01(\t\x12\x1b\n\x13\x64\x65scription_picking\x18\x06 \x01(\t\x12\x31\n\x0cqty_reserved\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x13\n\x0b\x65xternal_id\x18\x08 \x01(\t\x12\x36\n\x07\x63ontext\x18\t \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xa9\x01\n\x17StockMoveCreateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x43\n\nstock_move\x18\x02 \x01(\x0b\x32/.pro.omni.oms.api.v1.stock.stock_move.StockMove"\xf2\x02\n\x14StockMoveReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xe3\x01\n\x15StockMoveReadResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12\x44\n\x0bstock_moves\x18\x03 \x03(\x0b\x32/.pro.omni.oms.api.v1.stock.stock_move.StockMove"\x95\x01\n\x16StockMoveUpdateRequest\x12\x43\n\nstock_move\x18\x01 \x01(\x0b\x32/.pro.omni.oms.api.v1.stock.stock_move.StockMove\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xa9\x01\n\x17StockMoveUpdateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x43\n\nstock_move\x18\x02 \x01(\x0b\x32/.pro.omni.oms.api.v1.stock.stock_move.StockMove"\\\n\x16StockMoveDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"d\n\x17StockMoveDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xbc\x05\n\x10StockMoveService\x12\xa9\x01\n\x0fStockMoveCreate\x12<.pro.omni.oms.api.v1.stock.stock_move.StockMoveCreateRequest\x1a=.pro.omni.oms.api.v1.stock.stock_move.StockMoveCreateResponse"\x19\x9a\xb5\x18\x15\x08\x02\x12\x11\x61pi/v1/stock/move\x12\xa3\x01\n\rStockMoveRead\x12:.pro.omni.oms.api.v1.stock.stock_move.StockMoveReadRequest\x1a;.pro.omni.oms.api.v1.stock.stock_move.StockMoveReadResponse"\x19\x9a\xb5\x18\x15\x08\x01\x12\x11\x61pi/v1/stock/move\x12\xa9\x01\n\x0fStockMoveUpdate\x12<.pro.omni.oms.api.v1.stock.stock_move.StockMoveUpdateRequest\x1a=.pro.omni.oms.api.v1.stock.stock_move.StockMoveUpdateResponse"\x19\x9a\xb5\x18\x15\x08\x03\x12\x11\x61pi/v1/stock/move\x12\xa9\x01\n\x0fStockMoveDelete\x12<.pro.omni.oms.api.v1.stock.stock_move.StockMoveDeleteRequest\x1a=.pro.omni.oms.api.v1.stock.stock_move.StockMoveDeleteResponse"\x19\x9a\xb5\x18\x15\x08\x04\x12\x11\x61pi/v1/stock/moveb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.stock.stock_move_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _STOCKMOVESERVICE.methods_by_name["StockMoveCreate"]._options = None
    _STOCKMOVESERVICE.methods_by_name["StockMoveCreate"]._serialized_options = (
        b"\232\265\030\025\010\002\022\021api/v1/stock/move"
    )
    _STOCKMOVESERVICE.methods_by_name["StockMoveRead"]._options = None
    _STOCKMOVESERVICE.methods_by_name["StockMoveRead"]._serialized_options = (
        b"\232\265\030\025\010\001\022\021api/v1/stock/move"
    )
    _STOCKMOVESERVICE.methods_by_name["StockMoveUpdate"]._options = None
    _STOCKMOVESERVICE.methods_by_name["StockMoveUpdate"]._serialized_options = (
        b"\232\265\030\025\010\003\022\021api/v1/stock/move"
    )
    _STOCKMOVESERVICE.methods_by_name["StockMoveDelete"]._options = None
    _STOCKMOVESERVICE.methods_by_name["StockMoveDelete"]._serialized_options = (
        b"\232\265\030\025\010\004\022\021api/v1/stock/move"
    )
    _globals["_STOCKMOVE"]._serialized_start = 187
    _globals["_STOCKMOVE"]._serialized_end = 666
    _globals["_STOCKMOVECREATEREQUEST"]._serialized_start = 669
    _globals["_STOCKMOVECREATEREQUEST"]._serialized_end = 981
    _globals["_STOCKMOVECREATERESPONSE"]._serialized_start = 984
    _globals["_STOCKMOVECREATERESPONSE"]._serialized_end = 1153
    _globals["_STOCKMOVEREADREQUEST"]._serialized_start = 1156
    _globals["_STOCKMOVEREADREQUEST"]._serialized_end = 1526
    _globals["_STOCKMOVEREADRESPONSE"]._serialized_start = 1529
    _globals["_STOCKMOVEREADRESPONSE"]._serialized_end = 1756
    _globals["_STOCKMOVEUPDATEREQUEST"]._serialized_start = 1759
    _globals["_STOCKMOVEUPDATEREQUEST"]._serialized_end = 1908
    _globals["_STOCKMOVEUPDATERESPONSE"]._serialized_start = 1911
    _globals["_STOCKMOVEUPDATERESPONSE"]._serialized_end = 2080
    _globals["_STOCKMOVEDELETEREQUEST"]._serialized_start = 2082
    _globals["_STOCKMOVEDELETEREQUEST"]._serialized_end = 2174
    _globals["_STOCKMOVEDELETERESPONSE"]._serialized_start = 2176
    _globals["_STOCKMOVEDELETERESPONSE"]._serialized_end = 2276
    _globals["_STOCKMOVESERVICE"]._serialized_start = 2279
    _globals["_STOCKMOVESERVICE"]._serialized_end = 2979
# @@protoc_insertion_point(module_scope)
