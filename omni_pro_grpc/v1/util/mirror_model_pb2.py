# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/util/mirror_model.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from omni_pro_grpc.common import base_pb2 as common_dot_base__pb2
from omni_pro_grpc.v1.utilities import model_pb2 as v1_dot_utilities_dot_model__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1av1/util/mirror_model.proto\x12%pro.omni.oms.api.v1.util.mirror_model\x1a\x11\x63ommon/base.proto\x1a\x18v1/utilities/model.proto\x1a\x1cgoogle/protobuf/struct.proto"\x9b\x01\n CreateOrUpdateMirrorModelRequest\x12\x12\n\nmodel_path\x18\x01 \x01(\t\x12+\n\nmodel_data\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x36\n\x07\x63ontext\x18\x03 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9c\x01\n"CreateOrUpdateCreateMirrorResponse\x12+\n\nmodel_data\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\x88\x03\n\x16ReadMirrorModelRequest\x12\x12\n\nmodel_path\x18\x01 \x01(\t\x12\x37\n\x08group_by\x18\x02 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x05 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x06 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x07 \x01(\t\x12\x36\n\x07\x63ontext\x18\x08 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x97\x01\n\x17ReadMirrorModelResponse\x12\x31\n\rmirror_models\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.ListValue\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"r\n\x18\x44\x65leteMirrorModelRequest\x12\x12\n\nmodel_path\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x36\n\x07\x63ontext\x18\x03 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"f\n\x19\x44\x65leteMirrorModelResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\x9c\x05\n\x12MirrorModelService\x12\xa9\x01\n\x11\x43reateMirrorModel\x12G.pro.omni.oms.api.v1.util.mirror_model.CreateOrUpdateMirrorModelRequest\x1aI.pro.omni.oms.api.v1.util.mirror_model.CreateOrUpdateCreateMirrorResponse"\x00\x12\x92\x01\n\x0fReadMirrorModel\x12=.pro.omni.oms.api.v1.util.mirror_model.ReadMirrorModelRequest\x1a>.pro.omni.oms.api.v1.util.mirror_model.ReadMirrorModelResponse"\x00\x12\xa9\x01\n\x11UpdateMirrorModel\x12G.pro.omni.oms.api.v1.util.mirror_model.CreateOrUpdateMirrorModelRequest\x1aI.pro.omni.oms.api.v1.util.mirror_model.CreateOrUpdateCreateMirrorResponse"\x00\x12\x98\x01\n\x11\x44\x65leteMirrorModel\x12?.pro.omni.oms.api.v1.util.mirror_model.DeleteMirrorModelRequest\x1a@.pro.omni.oms.api.v1.util.mirror_model.DeleteMirrorModelResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.util.mirror_model_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _globals["_CREATEORUPDATEMIRRORMODELREQUEST"]._serialized_start = 145
    _globals["_CREATEORUPDATEMIRRORMODELREQUEST"]._serialized_end = 300
    _globals["_CREATEORUPDATECREATEMIRRORRESPONSE"]._serialized_start = 303
    _globals["_CREATEORUPDATECREATEMIRRORRESPONSE"]._serialized_end = 459
    _globals["_READMIRRORMODELREQUEST"]._serialized_start = 462
    _globals["_READMIRRORMODELREQUEST"]._serialized_end = 854
    _globals["_READMIRRORMODELRESPONSE"]._serialized_start = 857
    _globals["_READMIRRORMODELRESPONSE"]._serialized_end = 1008
    _globals["_DELETEMIRRORMODELREQUEST"]._serialized_start = 1010
    _globals["_DELETEMIRRORMODELREQUEST"]._serialized_end = 1124
    _globals["_DELETEMIRRORMODELRESPONSE"]._serialized_start = 1126
    _globals["_DELETEMIRRORMODELRESPONSE"]._serialized_end = 1228
    _globals["_MIRRORMODELSERVICE"]._serialized_start = 1231
    _globals["_MIRRORMODELSERVICE"]._serialized_end = 1899
# @@protoc_insertion_point(module_scope)
