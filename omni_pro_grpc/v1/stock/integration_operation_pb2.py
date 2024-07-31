# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/stock/integration_operation.proto
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
    b'\n$v1/stock/integration_operation.proto\x12/pro.omni.oms.api.v1.stock.integration_operation\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto"\x92\x02\n\x14IntegrationOperation\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12-\n\tmandatory\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x0c\n\x04type\x18\x06 \x01(\t\x12*\n\x06\x61\x63tive\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x08 \x01(\t\x12?\n\x0cobject_audit\x18\t \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xc2\x01\n!IntegrationOperationCreateRequest\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x11\n\tmandatory\x18\x04 \x01(\x08\x12\x0c\n\x04type\x18\x05 \x01(\t\x12\x13\n\x0b\x65xternal_id\x18\x06 \x01(\t\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xd5\x01\n"IntegrationOperationCreateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x64\n\x15integration_operation\x18\x02 \x01(\x0b\x32\x45.pro.omni.oms.api.v1.stock.integration_operation.IntegrationOperation"\xfd\x02\n\x1fIntegrationOperationReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x8f\x02\n IntegrationOperationReadResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12\x65\n\x16integration_operations\x18\x03 \x03(\x0b\x32\x45.pro.omni.oms.api.v1.stock.integration_operation.IntegrationOperation"\xc1\x01\n!IntegrationOperationUpdateRequest\x12\x64\n\x15integration_operation\x18\x01 \x01(\x0b\x32\x45.pro.omni.oms.api.v1.stock.integration_operation.IntegrationOperation\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xd5\x01\n"IntegrationOperationUpdateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x64\n\x15integration_operation\x18\x02 \x01(\x0b\x32\x45.pro.omni.oms.api.v1.stock.integration_operation.IntegrationOperation"g\n!IntegrationOperationDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"o\n"IntegrationOperationDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xbf\x06\n\x1bIntegrationOperationService\x12\xc7\x01\n\x1aIntegrationOperationCreate\x12R.pro.omni.oms.api.v1.stock.integration_operation.IntegrationOperationCreateRequest\x1aS.pro.omni.oms.api.v1.stock.integration_operation.IntegrationOperationCreateResponse"\x00\x12\xc1\x01\n\x18IntegrationOperationRead\x12P.pro.omni.oms.api.v1.stock.integration_operation.IntegrationOperationReadRequest\x1aQ.pro.omni.oms.api.v1.stock.integration_operation.IntegrationOperationReadResponse"\x00\x12\xc7\x01\n\x1aIntegrationOperationUpdate\x12R.pro.omni.oms.api.v1.stock.integration_operation.IntegrationOperationUpdateRequest\x1aS.pro.omni.oms.api.v1.stock.integration_operation.IntegrationOperationUpdateResponse"\x00\x12\xc7\x01\n\x1aIntegrationOperationDelete\x12R.pro.omni.oms.api.v1.stock.integration_operation.IntegrationOperationDeleteRequest\x1aS.pro.omni.oms.api.v1.stock.integration_operation.IntegrationOperationDeleteResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.stock.integration_operation_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _globals["_INTEGRATIONOPERATION"]._serialized_start = 141
    _globals["_INTEGRATIONOPERATION"]._serialized_end = 415
    _globals["_INTEGRATIONOPERATIONCREATEREQUEST"]._serialized_start = 418
    _globals["_INTEGRATIONOPERATIONCREATEREQUEST"]._serialized_end = 612
    _globals["_INTEGRATIONOPERATIONCREATERESPONSE"]._serialized_start = 615
    _globals["_INTEGRATIONOPERATIONCREATERESPONSE"]._serialized_end = 828
    _globals["_INTEGRATIONOPERATIONREADREQUEST"]._serialized_start = 831
    _globals["_INTEGRATIONOPERATIONREADREQUEST"]._serialized_end = 1212
    _globals["_INTEGRATIONOPERATIONREADRESPONSE"]._serialized_start = 1215
    _globals["_INTEGRATIONOPERATIONREADRESPONSE"]._serialized_end = 1486
    _globals["_INTEGRATIONOPERATIONUPDATEREQUEST"]._serialized_start = 1489
    _globals["_INTEGRATIONOPERATIONUPDATEREQUEST"]._serialized_end = 1682
    _globals["_INTEGRATIONOPERATIONUPDATERESPONSE"]._serialized_start = 1685
    _globals["_INTEGRATIONOPERATIONUPDATERESPONSE"]._serialized_end = 1898
    _globals["_INTEGRATIONOPERATIONDELETEREQUEST"]._serialized_start = 1900
    _globals["_INTEGRATIONOPERATIONDELETEREQUEST"]._serialized_end = 2003
    _globals["_INTEGRATIONOPERATIONDELETERESPONSE"]._serialized_start = 2005
    _globals["_INTEGRATIONOPERATIONDELETERESPONSE"]._serialized_end = 2116
    _globals["_INTEGRATIONOPERATIONSERVICE"]._serialized_start = 2119
    _globals["_INTEGRATIONOPERATIONSERVICE"]._serialized_end = 2950
# @@protoc_insertion_point(module_scope)
