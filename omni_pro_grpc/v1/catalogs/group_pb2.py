# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/catalogs/group.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from omni_pro_grpc.common import base_pb2 as common_dot_base__pb2
from omni_pro_grpc.v1.catalogs import attribute_pb2 as v1_dot_catalogs_dot_attribute__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x17v1/catalogs/group.proto\x12"pro.omni.oms.api.v1.catalogs.group\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1bv1/catalogs/attribute.proto"\xf8\x01\n\x05Group\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12*\n\x06\x61\x63tive\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x05 \x01(\t\x12\x45\n\nattributes\x18\x06 \x03(\x0b\x32\x31.pro.omni.oms.api.v1.catalogs.attribute.Attribute\x12?\n\x0cobject_audit\x18\x07 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\x94\x01\n\x12GroupCreateRequest\x12\x15\n\rattribute_ids\x18\x01 \x03(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x65xternal_id\x18\x04 \x01(\t\x12\x36\n\x07\x63ontext\x18\x05 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9a\x01\n\x13GroupCreateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x38\n\x05group\x18\x02 \x01(\x0b\x32).pro.omni.oms.api.v1.catalogs.group.Group"\xee\x02\n\x10GroupReadRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x37\n\x08group_by\x18\x02 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x05 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x06 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xd4\x01\n\x11GroupReadResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12\x39\n\x06groups\x18\x03 \x03(\x0b\x32).pro.omni.oms.api.v1.catalogs.group.Group"\x86\x01\n\x12GroupUpdateRequest\x12\x38\n\x05group\x18\x01 \x01(\x0b\x32).pro.omni.oms.api.v1.catalogs.group.Group\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9a\x01\n\x13GroupUpdateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x38\n\x05group\x18\x02 \x01(\x0b\x32).pro.omni.oms.api.v1.catalogs.group.Group"X\n\x12GroupDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"`\n\x13GroupDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\x93\x04\n\x0cGroupService\x12\x80\x01\n\x0bGroupCreate\x12\x36.pro.omni.oms.api.v1.catalogs.group.GroupCreateRequest\x1a\x37.pro.omni.oms.api.v1.catalogs.group.GroupCreateResponse"\x00\x12z\n\tGroupRead\x12\x34.pro.omni.oms.api.v1.catalogs.group.GroupReadRequest\x1a\x35.pro.omni.oms.api.v1.catalogs.group.GroupReadResponse"\x00\x12\x80\x01\n\x0bGroupUpdate\x12\x36.pro.omni.oms.api.v1.catalogs.group.GroupUpdateRequest\x1a\x37.pro.omni.oms.api.v1.catalogs.group.GroupUpdateResponse"\x00\x12\x80\x01\n\x0bGroupDelete\x12\x36.pro.omni.oms.api.v1.catalogs.group.GroupDeleteRequest\x1a\x37.pro.omni.oms.api.v1.catalogs.group.GroupDeleteResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.catalogs.group_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _globals["_GROUP"]._serialized_start = 144
    _globals["_GROUP"]._serialized_end = 392
    _globals["_GROUPCREATEREQUEST"]._serialized_start = 395
    _globals["_GROUPCREATEREQUEST"]._serialized_end = 543
    _globals["_GROUPCREATERESPONSE"]._serialized_start = 546
    _globals["_GROUPCREATERESPONSE"]._serialized_end = 700
    _globals["_GROUPREADREQUEST"]._serialized_start = 703
    _globals["_GROUPREADREQUEST"]._serialized_end = 1069
    _globals["_GROUPREADRESPONSE"]._serialized_start = 1072
    _globals["_GROUPREADRESPONSE"]._serialized_end = 1284
    _globals["_GROUPUPDATEREQUEST"]._serialized_start = 1287
    _globals["_GROUPUPDATEREQUEST"]._serialized_end = 1421
    _globals["_GROUPUPDATERESPONSE"]._serialized_start = 1424
    _globals["_GROUPUPDATERESPONSE"]._serialized_end = 1578
    _globals["_GROUPDELETEREQUEST"]._serialized_start = 1580
    _globals["_GROUPDELETEREQUEST"]._serialized_end = 1668
    _globals["_GROUPDELETERESPONSE"]._serialized_start = 1670
    _globals["_GROUPDELETERESPONSE"]._serialized_end = 1766
    _globals["_GROUPSERVICE"]._serialized_start = 1769
    _globals["_GROUPSERVICE"]._serialized_end = 2300
# @@protoc_insertion_point(module_scope)
