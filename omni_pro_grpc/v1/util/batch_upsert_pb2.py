# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/util/batch_upsert.proto
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
    b'\n\x1av1/util/batch_upsert.proto\x12*pro.omni.oms.api.v1.utilities.batch_upsert\x1a\x11\x63ommon/base.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1egoogle/protobuf/wrappers.proto"\x9c\x01\n\x12\x42\x61tchUpsertRequest\x12\x0e\n\x06tenant\x18\x01 \x01(\t\x12\x12\n\nmodel_path\x18\x02 \x01(\t\x12*\n\x06models\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.ListValue\x12\x36\n\x07\x63ontext\x18\x04 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x92\x01\n\x13\x42\x61tchUpsertResponse\x12\x30\n\x0c\x65rror_models\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.ListValue\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xab\x01\n\x12\x42\x61tchUpsertService\x12\x94\x01\n\x0b\x42\x61tchUpsert\x12>.pro.omni.oms.api.v1.utilities.batch_upsert.BatchUpsertRequest\x1a?.pro.omni.oms.api.v1.utilities.batch_upsert.BatchUpsertResponse"\x04\x90\xb5\x18\x01\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.util.batch_upsert_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _BATCHUPSERTSERVICE.methods_by_name["BatchUpsert"]._options = None
    _BATCHUPSERTSERVICE.methods_by_name["BatchUpsert"]._serialized_options = b"\220\265\030\001"
    _globals["_BATCHUPSERTREQUEST"]._serialized_start = 156
    _globals["_BATCHUPSERTREQUEST"]._serialized_end = 312
    _globals["_BATCHUPSERTRESPONSE"]._serialized_start = 315
    _globals["_BATCHUPSERTRESPONSE"]._serialized_end = 461
    _globals["_BATCHUPSERTSERVICE"]._serialized_start = 464
    _globals["_BATCHUPSERTSERVICE"]._serialized_end = 635
# @@protoc_insertion_point(module_scope)
