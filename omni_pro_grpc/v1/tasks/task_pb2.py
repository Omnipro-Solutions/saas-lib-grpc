# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/tasks/task.proto
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
    b'\n\x13v1/tasks/task.proto\x1a\x11\x63ommon/base.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xa4\x01\n\x04Task\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12\x11\n\ttask_name\x18\x02 \x01(\t\x12,\n\x0btask_params\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12+\n\x07ignored\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x0e\n\x06status\x18\x05 \x01(\t\x12\r\n\x05state\x18\x06 \x01(\t"T\n\x11TaskInvokeRequest\x12\x11\n\ttask_name\x18\x01 \x01(\t\x12,\n\x0btask_params\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct"t\n\x12TaskInvokeResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x13\n\x04task\x18\x02 \x01(\x0b\x32\x05.Task2F\n\x0bTaskService\x12\x37\n\nTaskInvoke\x12\x12.TaskInvokeRequest\x1a\x13.TaskInvokeResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.tasks.task_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _globals["_TASK"]._serialized_start = 105
    _globals["_TASK"]._serialized_end = 269
    _globals["_TASKINVOKEREQUEST"]._serialized_start = 271
    _globals["_TASKINVOKEREQUEST"]._serialized_end = 355
    _globals["_TASKINVOKERESPONSE"]._serialized_start = 357
    _globals["_TASKINVOKERESPONSE"]._serialized_end = 473
    _globals["_TASKSERVICE"]._serialized_start = 475
    _globals["_TASKSERVICE"]._serialized_end = 545
# @@protoc_insertion_point(module_scope)