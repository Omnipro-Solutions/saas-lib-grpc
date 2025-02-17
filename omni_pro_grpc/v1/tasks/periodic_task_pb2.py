# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/tasks/periodic_task.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from omni_pro_grpc.common import base_pb2 as common_dot_base__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1cv1/tasks/periodic_task.proto\x12$pro.omni.oms.api.tasks.periodic_task\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x8e\x05\n\x0cPeriodicTask\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04task\x18\x02 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x03 \x01(\t\x12\x0e\n\x06kwargs\x18\x04 \x01(\t\x12\r\n\x05queue\x18\x05 \x01(\t\x12\x10\n\x08\x65xchange\x18\x06 \x01(\t\x12\x13\n\x0brouting_key\x18\x07 \x01(\t\x12\x0f\n\x07headers\x18\x08 \x01(\t\x12\x10\n\x08priority\x18\t \x01(\x05\x12+\n\x07\x65xpires\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x0e\x65xpire_seconds\x18\x0b \x01(\x05\x12+\n\x07one_off\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12.\n\nstart_time\x18\r \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0blast_run_at\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x17\n\x0ftotal_run_count\x18\x0f \x01(\x05\x12\x30\n\x0c\x64\x61te_changed\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0b\x64\x65scription\x18\x11 \x01(\t\x12\x15\n\rdiscriminator\x18\x12 \x01(\t\x12\x13\n\x0bschedule_id\x18\x13 \x01(\x05\x12\n\n\x02id\x18\x14 \x01(\x05\x12\x13\n\x0b\x65xternal_id\x18\x15 \x01(\t\x12*\n\x06\x61\x63tive\x18\x16 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12?\n\x0cobject_audit\x18\x17 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xb6\x04\n\x19PeriodicTaskCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04task\x18\x02 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x03 \x01(\t\x12\x0e\n\x06kwargs\x18\x04 \x01(\t\x12\r\n\x05queue\x18\x05 \x01(\t\x12\x10\n\x08\x65xchange\x18\x06 \x01(\t\x12\x13\n\x0brouting_key\x18\x07 \x01(\t\x12\x0f\n\x07headers\x18\x08 \x01(\t\x12\x10\n\x08priority\x18\t \x01(\x05\x12+\n\x07\x65xpires\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x0e\x65xpire_seconds\x18\x0b \x01(\x05\x12+\n\x07one_off\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12.\n\nstart_time\x18\r \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12*\n\x06\x61\x63tive\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x15\n\rdiscriminator\x18\x0f \x01(\t\x12\x13\n\x0bschedule_id\x18\x10 \x01(\x05\x12\x13\n\x0b\x65xternal_id\x18\x11 \x01(\t\x12?\n\x0cobject_audit\x18\x12 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit\x12\x36\n\x07\x63ontext\x18\x13 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xb2\x01\n\x1aPeriodicTaskCreateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12I\n\rperiodic_task\x18\x02 \x01(\x0b\x32\x32.pro.omni.oms.api.tasks.periodic_task.PeriodicTask"\xf5\x02\n\x17PeriodicTaskReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xec\x01\n\x18PeriodicTaskReadResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12J\n\x0eperiodic_tasks\x18\x03 \x03(\x0b\x32\x32.pro.omni.oms.api.tasks.periodic_task.PeriodicTask"\x9e\x01\n\x19PeriodicTaskUpdateRequest\x12I\n\rperiodic_task\x18\x01 \x01(\x0b\x32\x32.pro.omni.oms.api.tasks.periodic_task.PeriodicTask\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xb2\x01\n\x1aPeriodicTaskUpdateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12I\n\rperiodic_task\x18\x02 \x01(\x0b\x32\x32.pro.omni.oms.api.tasks.periodic_task.PeriodicTask"_\n\x19PeriodicTaskDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"g\n\x1aPeriodicTaskDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\x87\x06\n\x13PeriodicTaskService\x12\xbb\x01\n\x12PeriodicTaskCreate\x12?.pro.omni.oms.api.tasks.periodic_task.PeriodicTaskCreateRequest\x1a@.pro.omni.oms.api.tasks.periodic_task.PeriodicTaskCreateResponse""\x9a\xb5\x18\x1e\x08\x02\x12\x1a\x61pi/v1/tasks/periodic_task\x12\xb5\x01\n\x10PeriodicTaskRead\x12=.pro.omni.oms.api.tasks.periodic_task.PeriodicTaskReadRequest\x1a>.pro.omni.oms.api.tasks.periodic_task.PeriodicTaskReadResponse""\x9a\xb5\x18\x1e\x08\x01\x12\x1a\x61pi/v1/tasks/periodic_task\x12\xbb\x01\n\x12PeriodicTaskUpdate\x12?.pro.omni.oms.api.tasks.periodic_task.PeriodicTaskUpdateRequest\x1a@.pro.omni.oms.api.tasks.periodic_task.PeriodicTaskUpdateResponse""\x9a\xb5\x18\x1e\x08\x03\x12\x1a\x61pi/v1/tasks/periodic_task\x12\xbb\x01\n\x12PeriodicTaskDelete\x12?.pro.omni.oms.api.tasks.periodic_task.PeriodicTaskDeleteRequest\x1a@.pro.omni.oms.api.tasks.periodic_task.PeriodicTaskDeleteResponse""\x9a\xb5\x18\x1e\x08\x04\x12\x1a\x61pi/v1/tasks/periodic_taskb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.tasks.periodic_task_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _PERIODICTASKSERVICE.methods_by_name["PeriodicTaskCreate"]._options = None
    _PERIODICTASKSERVICE.methods_by_name["PeriodicTaskCreate"]._serialized_options = (
        b"\232\265\030\036\010\002\022\032api/v1/tasks/periodic_task"
    )
    _PERIODICTASKSERVICE.methods_by_name["PeriodicTaskRead"]._options = None
    _PERIODICTASKSERVICE.methods_by_name["PeriodicTaskRead"]._serialized_options = (
        b"\232\265\030\036\010\001\022\032api/v1/tasks/periodic_task"
    )
    _PERIODICTASKSERVICE.methods_by_name["PeriodicTaskUpdate"]._options = None
    _PERIODICTASKSERVICE.methods_by_name["PeriodicTaskUpdate"]._serialized_options = (
        b"\232\265\030\036\010\003\022\032api/v1/tasks/periodic_task"
    )
    _PERIODICTASKSERVICE.methods_by_name["PeriodicTaskDelete"]._options = None
    _PERIODICTASKSERVICE.methods_by_name["PeriodicTaskDelete"]._serialized_options = (
        b"\232\265\030\036\010\004\022\032api/v1/tasks/periodic_task"
    )
    _globals["_PERIODICTASK"]._serialized_start = 155
    _globals["_PERIODICTASK"]._serialized_end = 809
    _globals["_PERIODICTASKCREATEREQUEST"]._serialized_start = 812
    _globals["_PERIODICTASKCREATEREQUEST"]._serialized_end = 1378
    _globals["_PERIODICTASKCREATERESPONSE"]._serialized_start = 1381
    _globals["_PERIODICTASKCREATERESPONSE"]._serialized_end = 1559
    _globals["_PERIODICTASKREADREQUEST"]._serialized_start = 1562
    _globals["_PERIODICTASKREADREQUEST"]._serialized_end = 1935
    _globals["_PERIODICTASKREADRESPONSE"]._serialized_start = 1938
    _globals["_PERIODICTASKREADRESPONSE"]._serialized_end = 2174
    _globals["_PERIODICTASKUPDATEREQUEST"]._serialized_start = 2177
    _globals["_PERIODICTASKUPDATEREQUEST"]._serialized_end = 2335
    _globals["_PERIODICTASKUPDATERESPONSE"]._serialized_start = 2338
    _globals["_PERIODICTASKUPDATERESPONSE"]._serialized_end = 2516
    _globals["_PERIODICTASKDELETEREQUEST"]._serialized_start = 2518
    _globals["_PERIODICTASKDELETEREQUEST"]._serialized_end = 2613
    _globals["_PERIODICTASKDELETERESPONSE"]._serialized_start = 2615
    _globals["_PERIODICTASKDELETERESPONSE"]._serialized_end = 2718
    _globals["_PERIODICTASKSERVICE"]._serialized_start = 2721
    _globals["_PERIODICTASKSERVICE"]._serialized_end = 3496
# @@protoc_insertion_point(module_scope)
