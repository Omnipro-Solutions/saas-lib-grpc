# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/stock/product.proto
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
    b'\n\x16v1/stock/product.proto\x12!pro.omni.oms.api.v1.stock.product\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/protobuf/struct.proto"\x83\x02\n\x07Product\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x16\n\x0eproduct_doc_id\x18\x02 \x01(\t\x12\x17\n\x0ftemplate_doc_id\x18\x03 \x01(\t\x12\x0b\n\x03sku\x18\x04 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x0c\n\x04\x63ode\x18\x07 \x01(\t\x12*\n\x06\x61\x63tive\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\t \x01(\t\x12?\n\x0cobject_audit\x18\n \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xb0\x01\n\x14ProductCreateRequest\x12\x16\n\x0eproduct_doc_id\x18\x01 \x01(\t\x12\x17\n\x0ftemplate_doc_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04\x63ode\x18\x04 \x01(\t\x12\x13\n\x0b\x65xternal_id\x18\x05 \x01(\t\x12\x36\n\x07\x63ontext\x18\x06 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9f\x01\n\x15ProductCreateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12;\n\x07product\x18\x02 \x01(\x0b\x32*.pro.omni.oms.api.v1.stock.product.Product"\xf0\x02\n\x12ProductReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xd9\x01\n\x13ProductReadResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12<\n\x08products\x18\x03 \x03(\x0b\x32*.pro.omni.oms.api.v1.stock.product.Product"\x8b\x01\n\x14ProductUpdateRequest\x12;\n\x07product\x18\x01 \x01(\x0b\x32*.pro.omni.oms.api.v1.stock.product.Product\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9f\x01\n\x15ProductUpdateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12;\n\x07product\x18\x02 \x01(\x0b\x32*.pro.omni.oms.api.v1.stock.product.Product"Z\n\x14ProductDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"b\n\x15ProductDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"~\n\x19ProductIntegrationRequest\x12)\n\x08products\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"g\n\x1aProductIntegrationResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xbb\x05\n\x0eProductService\x12\x84\x01\n\rProductCreate\x12\x37.pro.omni.oms.api.v1.stock.product.ProductCreateRequest\x1a\x38.pro.omni.oms.api.v1.stock.product.ProductCreateResponse"\x00\x12~\n\x0bProductRead\x12\x35.pro.omni.oms.api.v1.stock.product.ProductReadRequest\x1a\x36.pro.omni.oms.api.v1.stock.product.ProductReadResponse"\x00\x12\x84\x01\n\rProductUpdate\x12\x37.pro.omni.oms.api.v1.stock.product.ProductUpdateRequest\x1a\x38.pro.omni.oms.api.v1.stock.product.ProductUpdateResponse"\x00\x12\x84\x01\n\rProductDelete\x12\x37.pro.omni.oms.api.v1.stock.product.ProductDeleteRequest\x1a\x38.pro.omni.oms.api.v1.stock.product.ProductDeleteResponse"\x00\x12\x93\x01\n\x12ProductIntegration\x12<.pro.omni.oms.api.v1.stock.product.ProductIntegrationRequest\x1a=.pro.omni.oms.api.v1.stock.product.ProductIntegrationResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.stock.product_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _globals["_PRODUCT"]._serialized_start = 143
    _globals["_PRODUCT"]._serialized_end = 402
    _globals["_PRODUCTCREATEREQUEST"]._serialized_start = 405
    _globals["_PRODUCTCREATEREQUEST"]._serialized_end = 581
    _globals["_PRODUCTCREATERESPONSE"]._serialized_start = 584
    _globals["_PRODUCTCREATERESPONSE"]._serialized_end = 743
    _globals["_PRODUCTREADREQUEST"]._serialized_start = 746
    _globals["_PRODUCTREADREQUEST"]._serialized_end = 1114
    _globals["_PRODUCTREADRESPONSE"]._serialized_start = 1117
    _globals["_PRODUCTREADRESPONSE"]._serialized_end = 1334
    _globals["_PRODUCTUPDATEREQUEST"]._serialized_start = 1337
    _globals["_PRODUCTUPDATEREQUEST"]._serialized_end = 1476
    _globals["_PRODUCTUPDATERESPONSE"]._serialized_start = 1479
    _globals["_PRODUCTUPDATERESPONSE"]._serialized_end = 1638
    _globals["_PRODUCTDELETEREQUEST"]._serialized_start = 1640
    _globals["_PRODUCTDELETEREQUEST"]._serialized_end = 1730
    _globals["_PRODUCTDELETERESPONSE"]._serialized_start = 1732
    _globals["_PRODUCTDELETERESPONSE"]._serialized_end = 1830
    _globals["_PRODUCTINTEGRATIONREQUEST"]._serialized_start = 1832
    _globals["_PRODUCTINTEGRATIONREQUEST"]._serialized_end = 1958
    _globals["_PRODUCTINTEGRATIONRESPONSE"]._serialized_start = 1960
    _globals["_PRODUCTINTEGRATIONRESPONSE"]._serialized_end = 2063
    _globals["_PRODUCTSERVICE"]._serialized_start = 2066
    _globals["_PRODUCTSERVICE"]._serialized_end = 2765
# @@protoc_insertion_point(module_scope)
