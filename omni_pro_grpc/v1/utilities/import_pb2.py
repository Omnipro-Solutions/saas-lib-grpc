# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/utilities/import.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from omni_pro_grpc.common import base_pb2 as common_dot_base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19v1/utilities/import.proto\x12$pro.omni.oms.api.v1.utilities.import\x1a\x11\x63ommon/base.proto\"s\n\x12ImportModelRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x12\n\nmodel_name\x18\x02 \x01(\t\x12\x36\n\x07\x63ontext\x18\x03 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context\"`\n\x13ImportModelResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\x96\x01\n\rImportService\x12\x84\x01\n\x0bImportModel\x12\x38.pro.omni.oms.api.v1.utilities.import.ImportModelRequest\x1a\x39.pro.omni.oms.api.v1.utilities.import.ImportModelResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'v1.utilities.import_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_IMPORTMODELREQUEST']._serialized_start=86
  _globals['_IMPORTMODELREQUEST']._serialized_end=201
  _globals['_IMPORTMODELRESPONSE']._serialized_start=203
  _globals['_IMPORTMODELRESPONSE']._serialized_end=299
  _globals['_IMPORTSERVICE']._serialized_start=302
  _globals['_IMPORTSERVICE']._serialized_end=452
# @@protoc_insertion_point(module_scope)
