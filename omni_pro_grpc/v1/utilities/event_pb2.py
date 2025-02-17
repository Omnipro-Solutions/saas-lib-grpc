# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/utilities/event.proto
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
    b'\n\x18v1/utilities/event.proto\x12#pro.omni.oms.api.v1.utilities.event\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x18v1/utilities/model.proto"\x97\x02\n\x05\x45vent\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x39\n\x05model\x18\x04 \x01(\x0b\x32*.pro.omni.oms.api.v1.utilities.model.Model\x12\x11\n\toperation\x18\x05 \x01(\t\x12*\n\x06\x61\x63tive\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x07 \x01(\t\x12\x16\n\x0epriority_level\x18\x08 \x01(\t\x12?\n\x0cobject_audit\x18\t \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xba\x01\n\x12\x45ventCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x10\n\x08model_id\x18\x03 \x01(\t\x12\x11\n\toperation\x18\x04 \x01(\t\x12\x13\n\x0b\x65xternal_id\x18\x05 \x01(\t\x12\x16\n\x0epriority_level\x18\x06 \x01(\t\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9b\x01\n\x13\x45ventCreateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\x05\x65vent\x18\x02 \x01(\x0b\x32*.pro.omni.oms.api.v1.utilities.event.Event"\xee\x02\n\x10\x45ventReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\t\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xd5\x01\n\x11\x45ventReadResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12:\n\x06\x65vents\x18\x03 \x03(\x0b\x32*.pro.omni.oms.api.v1.utilities.event.Event"\x87\x01\n\x12\x45ventUpdateRequest\x12\x39\n\x05\x65vent\x18\x01 \x01(\x0b\x32*.pro.omni.oms.api.v1.utilities.event.Event\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9b\x01\n\x13\x45ventUpdateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\x05\x65vent\x18\x02 \x01(\x0b\x32*.pro.omni.oms.api.v1.utilities.event.Event"X\n\x12\x45ventDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"`\n\x13\x45ventDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\x94\x05\n\x0c\x45ventService\x12\xa0\x01\n\x0b\x45ventCreate\x12\x37.pro.omni.oms.api.v1.utilities.event.EventCreateRequest\x1a\x38.pro.omni.oms.api.v1.utilities.event.EventCreateResponse"\x1e\x9a\xb5\x18\x1a\x08\x02\x12\x16\x61pi/v1/utilities/event\x12\x9a\x01\n\tEventRead\x12\x35.pro.omni.oms.api.v1.utilities.event.EventReadRequest\x1a\x36.pro.omni.oms.api.v1.utilities.event.EventReadResponse"\x1e\x9a\xb5\x18\x1a\x08\x01\x12\x16\x61pi/v1/utilities/event\x12\xa0\x01\n\x0b\x45ventUpdate\x12\x37.pro.omni.oms.api.v1.utilities.event.EventUpdateRequest\x1a\x38.pro.omni.oms.api.v1.utilities.event.EventUpdateResponse"\x1e\x9a\xb5\x18\x1a\x08\x03\x12\x16\x61pi/v1/utilities/event\x12\xa0\x01\n\x0b\x45ventDelete\x12\x37.pro.omni.oms.api.v1.utilities.event.EventDeleteRequest\x1a\x38.pro.omni.oms.api.v1.utilities.event.EventDeleteResponse"\x1e\x9a\xb5\x18\x1a\x08\x04\x12\x16\x61pi/v1/utilities/eventb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.utilities.event_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _EVENTSERVICE.methods_by_name["EventCreate"]._options = None
    _EVENTSERVICE.methods_by_name["EventCreate"]._serialized_options = (
        b"\232\265\030\032\010\002\022\026api/v1/utilities/event"
    )
    _EVENTSERVICE.methods_by_name["EventRead"]._options = None
    _EVENTSERVICE.methods_by_name["EventRead"]._serialized_options = (
        b"\232\265\030\032\010\001\022\026api/v1/utilities/event"
    )
    _EVENTSERVICE.methods_by_name["EventUpdate"]._options = None
    _EVENTSERVICE.methods_by_name["EventUpdate"]._serialized_options = (
        b"\232\265\030\032\010\003\022\026api/v1/utilities/event"
    )
    _EVENTSERVICE.methods_by_name["EventDelete"]._options = None
    _EVENTSERVICE.methods_by_name["EventDelete"]._serialized_options = (
        b"\232\265\030\032\010\004\022\026api/v1/utilities/event"
    )
    _globals["_EVENT"]._serialized_start = 143
    _globals["_EVENT"]._serialized_end = 422
    _globals["_EVENTCREATEREQUEST"]._serialized_start = 425
    _globals["_EVENTCREATEREQUEST"]._serialized_end = 611
    _globals["_EVENTCREATERESPONSE"]._serialized_start = 614
    _globals["_EVENTCREATERESPONSE"]._serialized_end = 769
    _globals["_EVENTREADREQUEST"]._serialized_start = 772
    _globals["_EVENTREADREQUEST"]._serialized_end = 1138
    _globals["_EVENTREADRESPONSE"]._serialized_start = 1141
    _globals["_EVENTREADRESPONSE"]._serialized_end = 1354
    _globals["_EVENTUPDATEREQUEST"]._serialized_start = 1357
    _globals["_EVENTUPDATEREQUEST"]._serialized_end = 1492
    _globals["_EVENTUPDATERESPONSE"]._serialized_start = 1495
    _globals["_EVENTUPDATERESPONSE"]._serialized_end = 1650
    _globals["_EVENTDELETEREQUEST"]._serialized_start = 1652
    _globals["_EVENTDELETEREQUEST"]._serialized_end = 1740
    _globals["_EVENTDELETERESPONSE"]._serialized_start = 1742
    _globals["_EVENTDELETERESPONSE"]._serialized_end = 1838
    _globals["_EVENTSERVICE"]._serialized_start = 1841
    _globals["_EVENTSERVICE"]._serialized_end = 2501
# @@protoc_insertion_point(module_scope)
