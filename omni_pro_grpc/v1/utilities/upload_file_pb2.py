# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/utilities/upload_file.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from omni_pro_grpc.common import base_pb2 as common_dot_base__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1ev1/utilities/upload_file.proto\x12)pro.omni.oms.api.v1.utilities.upload_file\x1a\x11\x63ommon/base.proto"\x84\x01\n\x05\x46ield\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x17\n\x0fx_amz_algorithm\x18\x02 \x01(\t\x12\x18\n\x10x_amz_credential\x18\x03 \x01(\t\x12\x12\n\nx_amz_date\x18\x04 \x01(\t\x12\x0e\n\x06policy\x18\x05 \x01(\t\x12\x17\n\x0fx_amz_signature\x18\x06 \x01(\t"[\n\nUploadFile\x12\x0b\n\x03url\x18\x01 \x01(\t\x12@\n\x06\x66ields\x18\x02 \x01(\x0b\x32\x30.pro.omni.oms.api.v1.utilities.upload_file.Field"^\n\x11UploadXlsxRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xa6\x01\n\x12UploadXlsxResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x45\n\x06result\x18\x02 \x01(\x0b\x32\x35.pro.omni.oms.api.v1.utilities.upload_file.UploadFile2\xa1\x01\n\x11UploadFileService\x12\x8b\x01\n\nUploadXlsx\x12<.pro.omni.oms.api.v1.utilities.upload_file.UploadXlsxRequest\x1a=.pro.omni.oms.api.v1.utilities.upload_file.UploadXlsxResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.utilities.upload_file_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _globals["_FIELD"]._serialized_start = 97
    _globals["_FIELD"]._serialized_end = 229
    _globals["_UPLOADFILE"]._serialized_start = 231
    _globals["_UPLOADFILE"]._serialized_end = 322
    _globals["_UPLOADXLSXREQUEST"]._serialized_start = 324
    _globals["_UPLOADXLSXREQUEST"]._serialized_end = 418
    _globals["_UPLOADXLSXRESPONSE"]._serialized_start = 421
    _globals["_UPLOADXLSXRESPONSE"]._serialized_end = 587
    _globals["_UPLOADFILESERVICE"]._serialized_start = 590
    _globals["_UPLOADFILESERVICE"]._serialized_end = 751
# @@protoc_insertion_point(module_scope)
