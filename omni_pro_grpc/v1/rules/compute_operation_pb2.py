# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/rules/compute_operation.proto
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
    b'\n v1/rules/compute_operation.proto\x12+pro.omni.oms.api.v1.rules.compute_operation\x1a\x11\x63ommon/base.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1egoogle/protobuf/wrappers.proto"\x9d\x01\n\x11\x43omputeMethodData\x12-\n\x0c\x63\x61rt_details\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12&\n\x05items\x18\x02 \x03(\x0b\x32\x17.google.protobuf.Struct\x12\x31\n\x10shipping_details\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct"\xad\x01\n\x14\x43omputeMethodRequest\x12L\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32>.pro.omni.oms.api.v1.rules.compute_operation.ComputeMethodData\x12\x0f\n\x07version\x18\x02 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x03 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x8e\x01\n\x15\x43omputeMethodResponse\x12*\n\x06result\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.ListValue\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xae\x01\n"ComputeMethodStockAvailableRequest\x12(\n\x07methods\x18\x01 \x03(\x0b\x32\x17.google.protobuf.Struct\x12&\n\x05items\x18\x02 \x03(\x0b\x32\x17.google.protobuf.Struct\x12\x36\n\x07\x63ontext\x18\x03 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9c\x01\n#ComputeMethodStockAvailableResponse\x12*\n\x06result\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.ListValue\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xfa\x01\n\x1a\x43omputeDeliveryCarrierData\x12(\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12)\n\x08products\x18\x02 \x03(\x0b\x32\x17.google.protobuf.Struct\x12\x18\n\x10warehouse_sql_id\x18\x03 \x01(\x05\x12\x1e\n\x16\x64\x65livery_method_doc_id\x18\x04 \x01(\t\x12\x16\n\x0epicking_sql_id\x18\x05 \x01(\x05\x12\x35\n\x11internal_transfer\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.BoolValue"\xae\x01\n\x1d\x43omputeDeliveryCarrierRequest\x12U\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32G.pro.omni.oms.api.v1.rules.compute_operation.ComputeDeliveryCarrierData\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x82\x01\n"ComputeDeliveryCarrierDataResponse\x12\x16\n\x0e\x63\x61rrier_sql_id\x18\x01 \x01(\x05\x12\x18\n\x10warehouse_sql_id\x18\x02 \x01(\x05\x12\x16\n\x0epicking_sql_id\x18\x03 \x01(\x05\x12\x12\n\nexceptions\x18\x04 \x01(\t"\xce\x01\n\x1e\x43omputeDeliveryCarrierResponse\x12\x61\n\x08response\x18\x01 \x03(\x0b\x32O.pro.omni.oms.api.v1.rules.compute_operation.ComputeDeliveryCarrierDataResponse\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xaf\x04\n\x17\x43omputeOperationService\x12\x98\x01\n\rComputeMethod\x12\x41.pro.omni.oms.api.v1.rules.compute_operation.ComputeMethodRequest\x1a\x42.pro.omni.oms.api.v1.rules.compute_operation.ComputeMethodResponse"\x00\x12\xc2\x01\n\x1b\x43omputeMethodStockAvailable\x12O.pro.omni.oms.api.v1.rules.compute_operation.ComputeMethodStockAvailableRequest\x1aP.pro.omni.oms.api.v1.rules.compute_operation.ComputeMethodStockAvailableResponse"\x00\x12\xb3\x01\n\x16\x43omputeDeliveryCarrier\x12J.pro.omni.oms.api.v1.rules.compute_operation.ComputeDeliveryCarrierRequest\x1aK.pro.omni.oms.api.v1.rules.compute_operation.ComputeDeliveryCarrierResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.rules.compute_operation_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _globals["_COMPUTEMETHODDATA"]._serialized_start = 163
    _globals["_COMPUTEMETHODDATA"]._serialized_end = 320
    _globals["_COMPUTEMETHODREQUEST"]._serialized_start = 323
    _globals["_COMPUTEMETHODREQUEST"]._serialized_end = 496
    _globals["_COMPUTEMETHODRESPONSE"]._serialized_start = 499
    _globals["_COMPUTEMETHODRESPONSE"]._serialized_end = 641
    _globals["_COMPUTEMETHODSTOCKAVAILABLEREQUEST"]._serialized_start = 644
    _globals["_COMPUTEMETHODSTOCKAVAILABLEREQUEST"]._serialized_end = 818
    _globals["_COMPUTEMETHODSTOCKAVAILABLERESPONSE"]._serialized_start = 821
    _globals["_COMPUTEMETHODSTOCKAVAILABLERESPONSE"]._serialized_end = 977
    _globals["_COMPUTEDELIVERYCARRIERDATA"]._serialized_start = 980
    _globals["_COMPUTEDELIVERYCARRIERDATA"]._serialized_end = 1230
    _globals["_COMPUTEDELIVERYCARRIERREQUEST"]._serialized_start = 1233
    _globals["_COMPUTEDELIVERYCARRIERREQUEST"]._serialized_end = 1407
    _globals["_COMPUTEDELIVERYCARRIERDATARESPONSE"]._serialized_start = 1410
    _globals["_COMPUTEDELIVERYCARRIERDATARESPONSE"]._serialized_end = 1540
    _globals["_COMPUTEDELIVERYCARRIERRESPONSE"]._serialized_start = 1543
    _globals["_COMPUTEDELIVERYCARRIERRESPONSE"]._serialized_end = 1749
    _globals["_COMPUTEOPERATIONSERVICE"]._serialized_start = 1752
    _globals["_COMPUTEOPERATIONSERVICE"]._serialized_end = 2311
# @@protoc_insertion_point(module_scope)
