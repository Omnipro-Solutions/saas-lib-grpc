# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/airflow/register_model.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from omni_pro_grpc.common import base_pb2 as common_dot_base__pb2
from omni_pro_grpc.v1.utilities import model_pb2 as v1_dot_utilities_dot_model__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1fv1/airflow/register_model.proto\x1a\x11\x63ommon/base.proto\x1a\x18v1/utilities/model.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xf7\x01\n\x17ModelRegisterJobRequest\x12\x12\n\nservice_id\x18\x01 \x01(\t\x12*\n\x06update\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12M\n\x0cmodel_create\x18\x03 \x01(\x0b\x32\x37.pro.omni.oms.api.v1.utilities.model.ModelCreateRequest\x12M\n\x0cmodel_update\x18\x04 \x01(\x0b\x32\x37.pro.omni.oms.api.v1.utilities.model.ModelUpdateRequest"e\n\x18ModelRegisterJobResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2b\n\x15ModelsRegisterService\x12I\n\x10ModelRegisterJob\x12\x18.ModelRegisterJobRequest\x1a\x19.ModelRegisterJobResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.airflow.register_model_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _globals["_MODELREGISTERJOBREQUEST"]._serialized_start = 113
    _globals["_MODELREGISTERJOBREQUEST"]._serialized_end = 360
    _globals["_MODELREGISTERJOBRESPONSE"]._serialized_start = 362
    _globals["_MODELREGISTERJOBRESPONSE"]._serialized_end = 463
    _globals["_MODELSREGISTERSERVICE"]._serialized_start = 465
    _globals["_MODELSREGISTERSERVICE"]._serialized_end = 563
# @@protoc_insertion_point(module_scope)
