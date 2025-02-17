# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/rules/stock_security.proto
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
    b'\n\x1dv1/rules/stock_security.proto\x12(pro.omni.oms.api.v1.rules.stock_security\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto"V\n\x14ProductStockSecurity\x12\x16\n\x0eproduct_doc_id\x18\x01 \x01(\t\x12\x0b\n\x03sku\x18\x02 \x01(\t\x12\x19\n\x11quantity_security\x18\x03 \x01(\x02"\x99\x02\n\rStockSecurity\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12P\n\x08products\x18\x05 \x03(\x0b\x32>.pro.omni.oms.api.v1.rules.stock_security.ProductStockSecurity\x12*\n\x06\x61\x63tive\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x07 \x01(\t\x12?\n\x0cobject_audit\x18\x08 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xe5\x01\n\x1aStockSecurityCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12P\n\x08products\x18\x04 \x03(\x0b\x32>.pro.omni.oms.api.v1.rules.stock_security.ProductStockSecurity\x12\x13\n\x0b\x65xternal_id\x18\x05 \x01(\t\x12\x36\n\x07\x63ontext\x18\x06 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xb9\x01\n\x1bStockSecurityCreateResponse\x12O\n\x0estock_security\x18\x01 \x01(\x0b\x32\x37.pro.omni.oms.api.v1.rules.stock_security.StockSecurity\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xf6\x02\n\x18StockSecurityReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\t\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xf2\x01\n\x19StockSecurityReadResponse\x12O\n\x0estock_security\x18\x01 \x03(\x0b\x32\x37.pro.omni.oms.api.v1.rules.stock_security.StockSecurity\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12I\n\x11response_standard\x18\x03 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xa5\x01\n\x1aStockSecurityUpdateRequest\x12O\n\x0estock_security\x18\x01 \x01(\x0b\x32\x37.pro.omni.oms.api.v1.rules.stock_security.StockSecurity\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xb9\x01\n\x1bStockSecurityUpdateResponse\x12O\n\x0estock_security\x18\x01 \x01(\x0b\x32\x37.pro.omni.oms.api.v1.rules.stock_security.StockSecurity\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"`\n\x1aStockSecurityDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"h\n\x1bStockSecurityDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xb8\x06\n\x14StockSecurityService\x12\xc7\x01\n\x13StockSecurityCreate\x12\x44.pro.omni.oms.api.v1.rules.stock_security.StockSecurityCreateRequest\x1a\x45.pro.omni.oms.api.v1.rules.stock_security.StockSecurityCreateResponse"#\x9a\xb5\x18\x1f\x08\x02\x12\x1b\x61pi/v1/rules/stock-security\x12\xc1\x01\n\x11StockSecurityRead\x12\x42.pro.omni.oms.api.v1.rules.stock_security.StockSecurityReadRequest\x1a\x43.pro.omni.oms.api.v1.rules.stock_security.StockSecurityReadResponse"#\x9a\xb5\x18\x1f\x08\x01\x12\x1b\x61pi/v1/rules/stock-security\x12\xc7\x01\n\x13StockSecurityUpdate\x12\x44.pro.omni.oms.api.v1.rules.stock_security.StockSecurityUpdateRequest\x1a\x45.pro.omni.oms.api.v1.rules.stock_security.StockSecurityUpdateResponse"#\x9a\xb5\x18\x1f\x08\x03\x12\x1b\x61pi/v1/rules/stock-security\x12\xc7\x01\n\x13StockSecurityDelete\x12\x44.pro.omni.oms.api.v1.rules.stock_security.StockSecurityDeleteRequest\x1a\x45.pro.omni.oms.api.v1.rules.stock_security.StockSecurityDeleteResponse"#\x9a\xb5\x18\x1f\x08\x04\x12\x1b\x61pi/v1/rules/stock-securityb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.rules.stock_security_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _STOCKSECURITYSERVICE.methods_by_name["StockSecurityCreate"]._options = None
    _STOCKSECURITYSERVICE.methods_by_name["StockSecurityCreate"]._serialized_options = (
        b"\232\265\030\037\010\002\022\033api/v1/rules/stock-security"
    )
    _STOCKSECURITYSERVICE.methods_by_name["StockSecurityRead"]._options = None
    _STOCKSECURITYSERVICE.methods_by_name["StockSecurityRead"]._serialized_options = (
        b"\232\265\030\037\010\001\022\033api/v1/rules/stock-security"
    )
    _STOCKSECURITYSERVICE.methods_by_name["StockSecurityUpdate"]._options = None
    _STOCKSECURITYSERVICE.methods_by_name["StockSecurityUpdate"]._serialized_options = (
        b"\232\265\030\037\010\003\022\033api/v1/rules/stock-security"
    )
    _STOCKSECURITYSERVICE.methods_by_name["StockSecurityDelete"]._options = None
    _STOCKSECURITYSERVICE.methods_by_name["StockSecurityDelete"]._serialized_options = (
        b"\232\265\030\037\010\004\022\033api/v1/rules/stock-security"
    )
    _globals["_PRODUCTSTOCKSECURITY"]._serialized_start = 126
    _globals["_PRODUCTSTOCKSECURITY"]._serialized_end = 212
    _globals["_STOCKSECURITY"]._serialized_start = 215
    _globals["_STOCKSECURITY"]._serialized_end = 496
    _globals["_STOCKSECURITYCREATEREQUEST"]._serialized_start = 499
    _globals["_STOCKSECURITYCREATEREQUEST"]._serialized_end = 728
    _globals["_STOCKSECURITYCREATERESPONSE"]._serialized_start = 731
    _globals["_STOCKSECURITYCREATERESPONSE"]._serialized_end = 916
    _globals["_STOCKSECURITYREADREQUEST"]._serialized_start = 919
    _globals["_STOCKSECURITYREADREQUEST"]._serialized_end = 1293
    _globals["_STOCKSECURITYREADRESPONSE"]._serialized_start = 1296
    _globals["_STOCKSECURITYREADRESPONSE"]._serialized_end = 1538
    _globals["_STOCKSECURITYUPDATEREQUEST"]._serialized_start = 1541
    _globals["_STOCKSECURITYUPDATEREQUEST"]._serialized_end = 1706
    _globals["_STOCKSECURITYUPDATERESPONSE"]._serialized_start = 1709
    _globals["_STOCKSECURITYUPDATERESPONSE"]._serialized_end = 1894
    _globals["_STOCKSECURITYDELETEREQUEST"]._serialized_start = 1896
    _globals["_STOCKSECURITYDELETEREQUEST"]._serialized_end = 1992
    _globals["_STOCKSECURITYDELETERESPONSE"]._serialized_start = 1994
    _globals["_STOCKSECURITYDELETERESPONSE"]._serialized_end = 2098
    _globals["_STOCKSECURITYSERVICE"]._serialized_start = 2101
    _globals["_STOCKSECURITYSERVICE"]._serialized_end = 2925
# @@protoc_insertion_point(module_scope)
