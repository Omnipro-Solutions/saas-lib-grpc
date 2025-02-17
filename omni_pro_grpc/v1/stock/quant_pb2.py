# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/stock/quant.proto
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
from omni_pro_grpc.v1.stock import location_pb2 as v1_dot_stock_dot_location__pb2
from omni_pro_grpc.v1.stock import product_pb2 as v1_dot_stock_dot_product__pb2
from omni_pro_grpc.v1.stock import uom_pb2 as v1_dot_stock_dot_uom__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x14v1/stock/quant.proto\x12\x1fpro.omni.oms.api.v1.stock.quant\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x17v1/stock/location.proto\x1a\x16v1/stock/product.proto\x1a\x12v1/stock/uom.proto"\xb7\x03\n\x05Quant\x12\n\n\x02id\x18\x01 \x01(\x05\x12;\n\x07product\x18\x02 \x01(\x0b\x32*.pro.omni.oms.api.v1.stock.product.Product\x12>\n\x08location\x18\x03 \x01(\x0b\x32,.pro.omni.oms.api.v1.stock.location.Location\x12\x0c\n\x04lote\x18\x04 \x01(\t\x12\x1a\n\x12\x61vailable_quantity\x18\x05 \x01(\x02\x12\x19\n\x11reserved_quantity\x18\x06 \x01(\x02\x12-\n\x08quantity\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12/\n\x03uom\x18\x08 \x01(\x0b\x32".pro.omni.oms.api.v1.stock.uom.Uom\x12*\n\x06\x61\x63tive\x18\t \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\n \x01(\t\x12?\n\x0cobject_audit\x18\x0b \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\x8e\x02\n\x12QuantCreateRequest\x12\x12\n\nproduct_id\x18\x01 \x01(\t\x12\x13\n\x0blocation_id\x18\x02 \x01(\x05\x12\x0c\n\x04lote\x18\x03 \x01(\t\x12\x1a\n\x12\x61vailable_quantity\x18\x04 \x01(\x02\x12\x19\n\x11reserved_quantity\x18\x05 \x01(\x02\x12-\n\x08quantity\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x0e\n\x06uom_id\x18\x07 \x01(\t\x12\x13\n\x0b\x65xternal_id\x18\x08 \x01(\t\x12\x36\n\x07\x63ontext\x18\t \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x97\x01\n\x13QuantCreateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x35\n\x05quant\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.v1.stock.quant.Quant"\xee\x02\n\x10QuantReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xd1\x01\n\x11QuantReadResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12\x36\n\x06quants\x18\x03 \x03(\x0b\x32&.pro.omni.oms.api.v1.stock.quant.Quant"\x83\x01\n\x12QuantUpdateRequest\x12\x35\n\x05quant\x18\x01 \x01(\x0b\x32&.pro.omni.oms.api.v1.stock.quant.Quant\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x97\x01\n\x13QuantUpdateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x35\n\x05quant\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.v1.stock.quant.Quant"X\n\x12QuantDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"`\n\x13QuantDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\x94\x01\n\x10ProductAvailable\x12-\n\tavailable\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x1a\n\x12\x61vailable_quantity\x18\x02 \x01(\x02\x12\x35\n\x05quant\x18\x03 \x01(\x0b\x32&.pro.omni.oms.api.v1.stock.quant.Quant"\xaa\x01\n\x17ProductAvailableRequest\x12\x13\n\x0blocation_id\x18\x01 \x01(\x05\x12\x12\n\nproduct_id\x18\x02 \x01(\t\x12\x13\n\x0bproduct_sku\x18\x03 \x01(\t\x12\x19\n\x11required_quantity\x18\x04 \x01(\x02\x12\x36\n\x07\x63ontext\x18\x05 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xb3\x01\n\x18ProductAvailableResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12L\n\x11product_available\x18\x02 \x01(\x0b\x32\x31.pro.omni.oms.api.v1.stock.quant.ProductAvailable"\x80\x01\n\x1dSearchQuantIntegrationRequest\x12\'\n\x06quants\x18\x01 \x03(\x0b\x32\x17.google.protobuf.Struct\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xeb\x01\n\x1eSearchQuantIntegrationResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\'\n\x06quants\x18\x02 \x03(\x0b\x32\x17.google.protobuf.Struct\x12*\n\tlocations\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12)\n\x08products\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct"\xb3\x01\n\x17QuantIntegrationRequest\x12\'\n\x06\x63reate\x18\x01 \x03(\x0b\x32\x17.google.protobuf.Struct\x12\'\n\x06update\x18\x02 \x03(\x0b\x32\x17.google.protobuf.Struct\x12\x0e\n\x06\x64\x65lete\x18\x03 \x03(\x05\x12\x36\n\x07\x63ontext\x18\x04 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"s\n\x18QuantIntegrationResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x0c\n\x04hash\x18\x02 \x01(\t2\xfb\x08\n\x0cQuantService\x12\x94\x01\n\x0bQuantCreate\x12\x33.pro.omni.oms.api.v1.stock.quant.QuantCreateRequest\x1a\x34.pro.omni.oms.api.v1.stock.quant.QuantCreateResponse"\x1a\x9a\xb5\x18\x16\x08\x02\x12\x12\x61pi/v1/stock/quant\x12\x8e\x01\n\tQuantRead\x12\x31.pro.omni.oms.api.v1.stock.quant.QuantReadRequest\x1a\x32.pro.omni.oms.api.v1.stock.quant.QuantReadResponse"\x1a\x9a\xb5\x18\x16\x08\x01\x12\x12\x61pi/v1/stock/quant\x12\x94\x01\n\x0bQuantUpdate\x12\x33.pro.omni.oms.api.v1.stock.quant.QuantUpdateRequest\x1a\x34.pro.omni.oms.api.v1.stock.quant.QuantUpdateResponse"\x1a\x9a\xb5\x18\x16\x08\x03\x12\x12\x61pi/v1/stock/quant\x12\x94\x01\n\x0bQuantDelete\x12\x33.pro.omni.oms.api.v1.stock.quant.QuantDeleteRequest\x1a\x34.pro.omni.oms.api.v1.stock.quant.QuantDeleteResponse"\x1a\x9a\xb5\x18\x16\x08\x04\x12\x12\x61pi/v1/stock/quant\x12\x8d\x01\n\x10ProductAvailable\x12\x38.pro.omni.oms.api.v1.stock.quant.ProductAvailableRequest\x1a\x39.pro.omni.oms.api.v1.stock.quant.ProductAvailableResponse"\x04\x90\xb5\x18\x01\x12\xcd\x01\n\x1bSearchQuantStockIntegration\x12>.pro.omni.oms.api.v1.stock.quant.SearchQuantIntegrationRequest\x1a?.pro.omni.oms.api.v1.stock.quant.SearchQuantIntegrationResponse"-\x9a\xb5\x18)\x08\x02\x12%api/v1/stock/search/quant/integration\x12\xb4\x01\n\x15QuantStockIntegration\x12\x38.pro.omni.oms.api.v1.stock.quant.QuantIntegrationRequest\x1a\x39.pro.omni.oms.api.v1.stock.quant.QuantIntegrationResponse"&\x9a\xb5\x18"\x08\x02\x12\x1e\x61pi/v1/stock/quant/integrationb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.stock.quant_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _QUANTSERVICE.methods_by_name["QuantCreate"]._options = None
    _QUANTSERVICE.methods_by_name["QuantCreate"]._serialized_options = (
        b"\232\265\030\026\010\002\022\022api/v1/stock/quant"
    )
    _QUANTSERVICE.methods_by_name["QuantRead"]._options = None
    _QUANTSERVICE.methods_by_name["QuantRead"]._serialized_options = (
        b"\232\265\030\026\010\001\022\022api/v1/stock/quant"
    )
    _QUANTSERVICE.methods_by_name["QuantUpdate"]._options = None
    _QUANTSERVICE.methods_by_name["QuantUpdate"]._serialized_options = (
        b"\232\265\030\026\010\003\022\022api/v1/stock/quant"
    )
    _QUANTSERVICE.methods_by_name["QuantDelete"]._options = None
    _QUANTSERVICE.methods_by_name["QuantDelete"]._serialized_options = (
        b"\232\265\030\026\010\004\022\022api/v1/stock/quant"
    )
    _QUANTSERVICE.methods_by_name["ProductAvailable"]._options = None
    _QUANTSERVICE.methods_by_name["ProductAvailable"]._serialized_options = b"\220\265\030\001"
    _QUANTSERVICE.methods_by_name["SearchQuantStockIntegration"]._options = None
    _QUANTSERVICE.methods_by_name["SearchQuantStockIntegration"]._serialized_options = (
        b"\232\265\030)\010\002\022%api/v1/stock/search/quant/integration"
    )
    _QUANTSERVICE.methods_by_name["QuantStockIntegration"]._options = None
    _QUANTSERVICE.methods_by_name["QuantStockIntegration"]._serialized_options = (
        b'\232\265\030"\010\002\022\036api/v1/stock/quant/integration'
    )
    _globals["_QUANT"]._serialized_start = 208
    _globals["_QUANT"]._serialized_end = 647
    _globals["_QUANTCREATEREQUEST"]._serialized_start = 650
    _globals["_QUANTCREATEREQUEST"]._serialized_end = 920
    _globals["_QUANTCREATERESPONSE"]._serialized_start = 923
    _globals["_QUANTCREATERESPONSE"]._serialized_end = 1074
    _globals["_QUANTREADREQUEST"]._serialized_start = 1077
    _globals["_QUANTREADREQUEST"]._serialized_end = 1443
    _globals["_QUANTREADRESPONSE"]._serialized_start = 1446
    _globals["_QUANTREADRESPONSE"]._serialized_end = 1655
    _globals["_QUANTUPDATEREQUEST"]._serialized_start = 1658
    _globals["_QUANTUPDATEREQUEST"]._serialized_end = 1789
    _globals["_QUANTUPDATERESPONSE"]._serialized_start = 1792
    _globals["_QUANTUPDATERESPONSE"]._serialized_end = 1943
    _globals["_QUANTDELETEREQUEST"]._serialized_start = 1945
    _globals["_QUANTDELETEREQUEST"]._serialized_end = 2033
    _globals["_QUANTDELETERESPONSE"]._serialized_start = 2035
    _globals["_QUANTDELETERESPONSE"]._serialized_end = 2131
    _globals["_PRODUCTAVAILABLE"]._serialized_start = 2134
    _globals["_PRODUCTAVAILABLE"]._serialized_end = 2282
    _globals["_PRODUCTAVAILABLEREQUEST"]._serialized_start = 2285
    _globals["_PRODUCTAVAILABLEREQUEST"]._serialized_end = 2455
    _globals["_PRODUCTAVAILABLERESPONSE"]._serialized_start = 2458
    _globals["_PRODUCTAVAILABLERESPONSE"]._serialized_end = 2637
    _globals["_SEARCHQUANTINTEGRATIONREQUEST"]._serialized_start = 2640
    _globals["_SEARCHQUANTINTEGRATIONREQUEST"]._serialized_end = 2768
    _globals["_SEARCHQUANTINTEGRATIONRESPONSE"]._serialized_start = 2771
    _globals["_SEARCHQUANTINTEGRATIONRESPONSE"]._serialized_end = 3006
    _globals["_QUANTINTEGRATIONREQUEST"]._serialized_start = 3009
    _globals["_QUANTINTEGRATIONREQUEST"]._serialized_end = 3188
    _globals["_QUANTINTEGRATIONRESPONSE"]._serialized_start = 3190
    _globals["_QUANTINTEGRATIONRESPONSE"]._serialized_end = 3305
    _globals["_QUANTSERVICE"]._serialized_start = 3308
    _globals["_QUANTSERVICE"]._serialized_end = 4455
# @@protoc_insertion_point(module_scope)
