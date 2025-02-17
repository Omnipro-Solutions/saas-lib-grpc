# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/catalogs/attribute.proto
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
    b'\n\x1bv1/catalogs/attribute.proto\x12&pro.omni.oms.api.v1.catalogs.attribute\x1a\x1cgoogle/protobuf/struct.proto\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xae\x02\n\tAttribute\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x16\n\x0e\x61ttribute_type\x18\x04 \x01(\t\x12-\n\tis_common\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12*\n\x06\x61\x63tive\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x07 \x01(\t\x12\x30\n\x0f\x65xtra_attribute\x18\x08 \x01(\x0b\x32\x17.google.protobuf.Struct\x12?\n\x0cobject_audit\x18\t \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xfa\x01\n\x16\x41ttributeCreateRequest\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x16\n\x0e\x61ttribute_type\x18\x03 \x01(\t\x12-\n\tis_common\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x30\n\x0f\x65xtra_attribute\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x13\n\x0b\x65xternal_id\x18\x06 \x01(\t\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xaa\x01\n\x17\x41ttributeCreateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x44\n\tattribute\x18\x02 \x01(\x0b\x32\x31.pro.omni.oms.api.v1.catalogs.attribute.Attribute"\xf2\x02\n\x14\x41ttributeReadRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x37\n\x08group_by\x18\x02 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x05 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x06 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9c\x02\n\x15\x41ttributeReadResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12\x45\n\nattributes\x18\x03 \x03(\x0b\x32\x31.pro.omni.oms.api.v1.catalogs.attribute.Attribute\x12\x36\n\x07\x63ontext\x18\x04 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x96\x01\n\x16\x41ttributeUpdateRequest\x12\x44\n\tattribute\x18\x01 \x01(\x0b\x32\x31.pro.omni.oms.api.v1.catalogs.attribute.Attribute\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xaa\x01\n\x17\x41ttributeUpdateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x44\n\tattribute\x18\x02 \x01(\x0b\x32\x31.pro.omni.oms.api.v1.catalogs.attribute.Attribute"\\\n\x16\x41ttributeDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"d\n\x17\x41ttributeDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xe8\x05\n\x10\x41ttributeService\x12\xb4\x01\n\x0f\x41ttributeCreate\x12>.pro.omni.oms.api.v1.catalogs.attribute.AttributeCreateRequest\x1a?.pro.omni.oms.api.v1.catalogs.attribute.AttributeCreateResponse" \x9a\xb5\x18\x1c\x08\x02\x12\x18\x61pi/v1/catalog/attribute\x12\xae\x01\n\rAttributeRead\x12<.pro.omni.oms.api.v1.catalogs.attribute.AttributeReadRequest\x1a=.pro.omni.oms.api.v1.catalogs.attribute.AttributeReadResponse" \x9a\xb5\x18\x1c\x08\x01\x12\x18\x61pi/v1/catalog/attribute\x12\xb4\x01\n\x0f\x41ttributeUpdate\x12>.pro.omni.oms.api.v1.catalogs.attribute.AttributeUpdateRequest\x1a?.pro.omni.oms.api.v1.catalogs.attribute.AttributeUpdateResponse" \x9a\xb5\x18\x1c\x08\x03\x12\x18\x61pi/v1/catalog/attribute\x12\xb4\x01\n\x0f\x41ttributeDelete\x12>.pro.omni.oms.api.v1.catalogs.attribute.AttributeDeleteRequest\x1a?.pro.omni.oms.api.v1.catalogs.attribute.AttributeDeleteResponse" \x9a\xb5\x18\x1c\x08\x04\x12\x18\x61pi/v1/catalog/attributeb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.catalogs.attribute_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _ATTRIBUTESERVICE.methods_by_name["AttributeCreate"]._options = None
    _ATTRIBUTESERVICE.methods_by_name["AttributeCreate"]._serialized_options = (
        b"\232\265\030\034\010\002\022\030api/v1/catalog/attribute"
    )
    _ATTRIBUTESERVICE.methods_by_name["AttributeRead"]._options = None
    _ATTRIBUTESERVICE.methods_by_name["AttributeRead"]._serialized_options = (
        b"\232\265\030\034\010\001\022\030api/v1/catalog/attribute"
    )
    _ATTRIBUTESERVICE.methods_by_name["AttributeUpdate"]._options = None
    _ATTRIBUTESERVICE.methods_by_name["AttributeUpdate"]._serialized_options = (
        b"\232\265\030\034\010\003\022\030api/v1/catalog/attribute"
    )
    _ATTRIBUTESERVICE.methods_by_name["AttributeDelete"]._options = None
    _ATTRIBUTESERVICE.methods_by_name["AttributeDelete"]._serialized_options = (
        b"\232\265\030\034\010\004\022\030api/v1/catalog/attribute"
    )
    _globals["_ATTRIBUTE"]._serialized_start = 153
    _globals["_ATTRIBUTE"]._serialized_end = 455
    _globals["_ATTRIBUTECREATEREQUEST"]._serialized_start = 458
    _globals["_ATTRIBUTECREATEREQUEST"]._serialized_end = 708
    _globals["_ATTRIBUTECREATERESPONSE"]._serialized_start = 711
    _globals["_ATTRIBUTECREATERESPONSE"]._serialized_end = 881
    _globals["_ATTRIBUTEREADREQUEST"]._serialized_start = 884
    _globals["_ATTRIBUTEREADREQUEST"]._serialized_end = 1254
    _globals["_ATTRIBUTEREADRESPONSE"]._serialized_start = 1257
    _globals["_ATTRIBUTEREADRESPONSE"]._serialized_end = 1541
    _globals["_ATTRIBUTEUPDATEREQUEST"]._serialized_start = 1544
    _globals["_ATTRIBUTEUPDATEREQUEST"]._serialized_end = 1694
    _globals["_ATTRIBUTEUPDATERESPONSE"]._serialized_start = 1697
    _globals["_ATTRIBUTEUPDATERESPONSE"]._serialized_end = 1867
    _globals["_ATTRIBUTEDELETEREQUEST"]._serialized_start = 1869
    _globals["_ATTRIBUTEDELETEREQUEST"]._serialized_end = 1961
    _globals["_ATTRIBUTEDELETERESPONSE"]._serialized_start = 1963
    _globals["_ATTRIBUTEDELETERESPONSE"]._serialized_end = 2063
    _globals["_ATTRIBUTESERVICE"]._serialized_start = 2066
    _globals["_ATTRIBUTESERVICE"]._serialized_end = 2810
# @@protoc_insertion_point(module_scope)
