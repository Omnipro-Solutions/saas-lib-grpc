# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/rules/python_code.proto
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
    b'\n\x1av1/rules/python_code.proto\x12%pro.omni.oms.api.v1.rules.python_code\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto"\x91\x01\n\nPythonCode\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0bpython_code\x18\x03 \x01(\t\x12\x13\n\x0b\x65xternal_id\x18\x04 \x01(\t\x12?\n\x0cobject_audit\x18\x05 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\x83\x01\n\x11PythonCodeRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bpython_code\x18\x02 \x01(\t\x12\x13\n\x0b\x65xternal_id\x18\x03 \x01(\t\x12\x36\n\x07\x63ontext\x18\x04 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xa7\x01\n\x12PythonCodeResponse\x12\x46\n\x0bpython_code\x18\x01 \x01(\x0b\x32\x31.pro.omni.oms.api.v1.rules.python_code.PythonCode\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xf3\x02\n\x15PythonCodeReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\t\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xe7\x01\n\x16PythonCodeReadResponse\x12G\n\x0cpython_codes\x18\x01 \x03(\x0b\x32\x31.pro.omni.oms.api.v1.rules.python_code.PythonCode\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12I\n\x11response_standard\x18\x03 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\x99\x01\n\x17PythonCodeUpdateRequest\x12\x46\n\x0bpython_code\x18\x01 \x01(\x0b\x32\x31.pro.omni.oms.api.v1.rules.python_code.PythonCode\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xad\x01\n\x18PythonCodeUpdateResponse\x12\x46\n\x0bpython_code\x18\x01 \x01(\x0b\x32\x31.pro.omni.oms.api.v1.rules.python_code.PythonCode\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"]\n\x17PythonCodeDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"e\n\x18PythonCodeDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xe1\x05\n\x11PythonCodeService\x12\xa9\x01\n\x10PythonCodeCreate\x12\x38.pro.omni.oms.api.v1.rules.python_code.PythonCodeRequest\x1a\x39.pro.omni.oms.api.v1.rules.python_code.PythonCodeResponse" \x9a\xb5\x18\x1c\x08\x02\x12\x18\x61pi/v1/rules/python-code\x12\xaf\x01\n\x0ePythonCodeRead\x12<.pro.omni.oms.api.v1.rules.python_code.PythonCodeReadRequest\x1a=.pro.omni.oms.api.v1.rules.python_code.PythonCodeReadResponse" \x9a\xb5\x18\x1c\x08\x01\x12\x18\x61pi/v1/rules/python-code\x12\xb5\x01\n\x10PythonCodeUpdate\x12>.pro.omni.oms.api.v1.rules.python_code.PythonCodeUpdateRequest\x1a?.pro.omni.oms.api.v1.rules.python_code.PythonCodeUpdateResponse" \x9a\xb5\x18\x1c\x08\x03\x12\x18\x61pi/v1/rules/python-code\x12\xb5\x01\n\x10PythonCodeDelete\x12>.pro.omni.oms.api.v1.rules.python_code.PythonCodeDeleteRequest\x1a?.pro.omni.oms.api.v1.rules.python_code.PythonCodeDeleteResponse" \x9a\xb5\x18\x1c\x08\x04\x12\x18\x61pi/v1/rules/python-codeb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.rules.python_code_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _PYTHONCODESERVICE.methods_by_name["PythonCodeCreate"]._options = None
    _PYTHONCODESERVICE.methods_by_name["PythonCodeCreate"]._serialized_options = (
        b"\232\265\030\034\010\002\022\030api/v1/rules/python-code"
    )
    _PYTHONCODESERVICE.methods_by_name["PythonCodeRead"]._options = None
    _PYTHONCODESERVICE.methods_by_name["PythonCodeRead"]._serialized_options = (
        b"\232\265\030\034\010\001\022\030api/v1/rules/python-code"
    )
    _PYTHONCODESERVICE.methods_by_name["PythonCodeUpdate"]._options = None
    _PYTHONCODESERVICE.methods_by_name["PythonCodeUpdate"]._serialized_options = (
        b"\232\265\030\034\010\003\022\030api/v1/rules/python-code"
    )
    _PYTHONCODESERVICE.methods_by_name["PythonCodeDelete"]._options = None
    _PYTHONCODESERVICE.methods_by_name["PythonCodeDelete"]._serialized_options = (
        b"\232\265\030\034\010\004\022\030api/v1/rules/python-code"
    )
    _globals["_PYTHONCODE"]._serialized_start = 121
    _globals["_PYTHONCODE"]._serialized_end = 266
    _globals["_PYTHONCODEREQUEST"]._serialized_start = 269
    _globals["_PYTHONCODEREQUEST"]._serialized_end = 400
    _globals["_PYTHONCODERESPONSE"]._serialized_start = 403
    _globals["_PYTHONCODERESPONSE"]._serialized_end = 570
    _globals["_PYTHONCODEREADREQUEST"]._serialized_start = 573
    _globals["_PYTHONCODEREADREQUEST"]._serialized_end = 944
    _globals["_PYTHONCODEREADRESPONSE"]._serialized_start = 947
    _globals["_PYTHONCODEREADRESPONSE"]._serialized_end = 1178
    _globals["_PYTHONCODEUPDATEREQUEST"]._serialized_start = 1181
    _globals["_PYTHONCODEUPDATEREQUEST"]._serialized_end = 1334
    _globals["_PYTHONCODEUPDATERESPONSE"]._serialized_start = 1337
    _globals["_PYTHONCODEUPDATERESPONSE"]._serialized_end = 1510
    _globals["_PYTHONCODEDELETEREQUEST"]._serialized_start = 1512
    _globals["_PYTHONCODEDELETEREQUEST"]._serialized_end = 1605
    _globals["_PYTHONCODEDELETERESPONSE"]._serialized_start = 1607
    _globals["_PYTHONCODEDELETERESPONSE"]._serialized_end = 1708
    _globals["_PYTHONCODESERVICE"]._serialized_start = 1711
    _globals["_PYTHONCODESERVICE"]._serialized_end = 2448
# @@protoc_insertion_point(module_scope)
