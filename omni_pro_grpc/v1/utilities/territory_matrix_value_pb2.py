# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/utilities/territory_matrix_value.proto
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
    b'\n)v1/utilities/territory_matrix_value.proto\x12\x34pro.omni.oms.api.v1.utilities.territory_matrix_value\x1a\x11\x63ommon/base.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1egoogle/protobuf/wrappers.proto"\x86\x02\n\x14TerritoryMatrixValue\x12\n\n\x02id\x18\x01 \x01(\t\x12\x36\n\x12territory_matrixes\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.ListValue\x12(\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.ListValue\x12*\n\x06\x61\x63tive\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x05 \x01(\t\x12?\n\x0cobject_audit\x18\x06 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xfe\x01\n!TerritoryMatrixValueCreateRequest\x12\x36\n\x12territory_matrixes\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.ListValue\x12(\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.ListValue\x12*\n\x06\x61\x63tive\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x04 \x01(\t\x12\x36\n\x07\x63ontext\x18\x05 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xdb\x01\n"TerritoryMatrixValueCreateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12j\n\x16territory_matrix_value\x18\x02 \x01(\x0b\x32J.pro.omni.oms.api.v1.utilities.territory_matrix_value.TerritoryMatrixValue"\xfd\x02\n\x1fTerritoryMatrixValueReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\t\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x97\x02\n TerritoryMatrixValueReadResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12m\n\x19territory_matrixes_values\x18\x03 \x03(\x0b\x32J.pro.omni.oms.api.v1.utilities.territory_matrix_value.TerritoryMatrixValue"\xc7\x01\n!TerritoryMatrixValueUpdateRequest\x12j\n\x16territory_matrix_value\x18\x01 \x01(\x0b\x32J.pro.omni.oms.api.v1.utilities.territory_matrix_value.TerritoryMatrixValue\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xdb\x01\n"TerritoryMatrixValueUpdateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12j\n\x16territory_matrix_value\x18\x02 \x01(\x0b\x32J.pro.omni.oms.api.v1.utilities.territory_matrix_value.TerritoryMatrixValue"g\n!TerritoryMatrixValueDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"o\n"TerritoryMatrixValueDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xa3\x08\n\x1bTerritoryMatrixValueService\x12\x80\x02\n\x1aTerritoryMatrixValueCreate\x12W.pro.omni.oms.api.v1.utilities.territory_matrix_value.TerritoryMatrixValueCreateRequest\x1aX.pro.omni.oms.api.v1.utilities.territory_matrix_value.TerritoryMatrixValueCreateResponse"/\x9a\xb5\x18+\x08\x02\x12\'api/v1/utilities/territory-matrix-value\x12\xfa\x01\n\x18TerritoryMatrixValueRead\x12U.pro.omni.oms.api.v1.utilities.territory_matrix_value.TerritoryMatrixValueReadRequest\x1aV.pro.omni.oms.api.v1.utilities.territory_matrix_value.TerritoryMatrixValueReadResponse"/\x9a\xb5\x18+\x08\x01\x12\'api/v1/utilities/territory-matrix-value\x12\x80\x02\n\x1aTerritoryMatrixValueUpdate\x12W.pro.omni.oms.api.v1.utilities.territory_matrix_value.TerritoryMatrixValueUpdateRequest\x1aX.pro.omni.oms.api.v1.utilities.territory_matrix_value.TerritoryMatrixValueUpdateResponse"/\x9a\xb5\x18+\x08\x03\x12\'api/v1/utilities/territory-matrix-value\x12\x80\x02\n\x1aTerritoryMatrixValueDelete\x12W.pro.omni.oms.api.v1.utilities.territory_matrix_value.TerritoryMatrixValueDeleteRequest\x1aX.pro.omni.oms.api.v1.utilities.territory_matrix_value.TerritoryMatrixValueDeleteResponse"/\x9a\xb5\x18+\x08\x04\x12\'api/v1/utilities/territory-matrix-valueb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.utilities.territory_matrix_value_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _TERRITORYMATRIXVALUESERVICE.methods_by_name["TerritoryMatrixValueCreate"]._options = None
    _TERRITORYMATRIXVALUESERVICE.methods_by_name["TerritoryMatrixValueCreate"]._serialized_options = (
        b"\232\265\030+\010\002\022'api/v1/utilities/territory-matrix-value"
    )
    _TERRITORYMATRIXVALUESERVICE.methods_by_name["TerritoryMatrixValueRead"]._options = None
    _TERRITORYMATRIXVALUESERVICE.methods_by_name["TerritoryMatrixValueRead"]._serialized_options = (
        b"\232\265\030+\010\001\022'api/v1/utilities/territory-matrix-value"
    )
    _TERRITORYMATRIXVALUESERVICE.methods_by_name["TerritoryMatrixValueUpdate"]._options = None
    _TERRITORYMATRIXVALUESERVICE.methods_by_name["TerritoryMatrixValueUpdate"]._serialized_options = (
        b"\232\265\030+\010\003\022'api/v1/utilities/territory-matrix-value"
    )
    _TERRITORYMATRIXVALUESERVICE.methods_by_name["TerritoryMatrixValueDelete"]._options = None
    _TERRITORYMATRIXVALUESERVICE.methods_by_name["TerritoryMatrixValueDelete"]._serialized_options = (
        b"\232\265\030+\010\004\022'api/v1/utilities/territory-matrix-value"
    )
    _globals["_TERRITORYMATRIXVALUE"]._serialized_start = 181
    _globals["_TERRITORYMATRIXVALUE"]._serialized_end = 443
    _globals["_TERRITORYMATRIXVALUECREATEREQUEST"]._serialized_start = 446
    _globals["_TERRITORYMATRIXVALUECREATEREQUEST"]._serialized_end = 700
    _globals["_TERRITORYMATRIXVALUECREATERESPONSE"]._serialized_start = 703
    _globals["_TERRITORYMATRIXVALUECREATERESPONSE"]._serialized_end = 922
    _globals["_TERRITORYMATRIXVALUEREADREQUEST"]._serialized_start = 925
    _globals["_TERRITORYMATRIXVALUEREADREQUEST"]._serialized_end = 1306
    _globals["_TERRITORYMATRIXVALUEREADRESPONSE"]._serialized_start = 1309
    _globals["_TERRITORYMATRIXVALUEREADRESPONSE"]._serialized_end = 1588
    _globals["_TERRITORYMATRIXVALUEUPDATEREQUEST"]._serialized_start = 1591
    _globals["_TERRITORYMATRIXVALUEUPDATEREQUEST"]._serialized_end = 1790
    _globals["_TERRITORYMATRIXVALUEUPDATERESPONSE"]._serialized_start = 1793
    _globals["_TERRITORYMATRIXVALUEUPDATERESPONSE"]._serialized_end = 2012
    _globals["_TERRITORYMATRIXVALUEDELETEREQUEST"]._serialized_start = 2014
    _globals["_TERRITORYMATRIXVALUEDELETEREQUEST"]._serialized_end = 2117
    _globals["_TERRITORYMATRIXVALUEDELETERESPONSE"]._serialized_start = 2119
    _globals["_TERRITORYMATRIXVALUEDELETERESPONSE"]._serialized_end = 2230
    _globals["_TERRITORYMATRIXVALUESERVICE"]._serialized_start = 2233
    _globals["_TERRITORYMATRIXVALUESERVICE"]._serialized_end = 3292
# @@protoc_insertion_point(module_scope)
