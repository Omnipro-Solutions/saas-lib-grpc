# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/catalogs/attribute_variant.proto
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
    b'\n#v1/catalogs/attribute_variant.proto\x12.pro.omni.oms.api.v1.catalogs.attribute_variant\x1a\x1cgoogle/protobuf/struct.proto\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xde\x01\n\x10\x41ttributeVariant\x12\n\n\x02id\x18\x01 \x01(\t\x12*\n\tattribute\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x10\n\x08sequence\x18\x03 \x01(\x05\x12\x13\n\x0b\x65xternal_id\x18\x04 \x01(\t\x12*\n\x06\x61\x63tive\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12?\n\x0cobject_audit\x18\x06 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\x96\x01\n\x1d\x41ttributeVariantCreateRequest\x12\x16\n\x0e\x61ttribute_code\x18\x01 \x01(\t\x12\x10\n\x08sequence\x18\x02 \x01(\x05\x12\x13\n\x0b\x65xternal_id\x18\x03 \x01(\t\x12\x36\n\x07\x63ontext\x18\x04 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xc8\x01\n\x1e\x41ttributeVariantCreateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12[\n\x11\x61ttribute_variant\x18\x02 \x01(\x0b\x32@.pro.omni.oms.api.v1.catalogs.attribute_variant.AttributeVariant"\xf9\x02\n\x1b\x41ttributeVariantReadRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x37\n\x08group_by\x18\x02 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x05 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x06 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x82\x02\n\x1c\x41ttributeVariantReadResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12\\\n\x12\x61ttribute_variants\x18\x03 \x03(\x0b\x32@.pro.omni.oms.api.v1.catalogs.attribute_variant.AttributeVariant"\xb4\x01\n\x1d\x41ttributeVariantUpdateRequest\x12[\n\x11\x61ttribute_variant\x18\x01 \x01(\x0b\x32@.pro.omni.oms.api.v1.catalogs.attribute_variant.AttributeVariant\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xc8\x01\n\x1e\x41ttributeVariantUpdateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12[\n\x11\x61ttribute_variant\x18\x02 \x01(\x0b\x32@.pro.omni.oms.api.v1.catalogs.attribute_variant.AttributeVariant"c\n\x1d\x41ttributeVariantDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"k\n\x1e\x41ttributeVariantDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xa3\x07\n\x17\x41ttributeVariantService\x12\xe1\x01\n\x16\x41ttributeVariantCreate\x12M.pro.omni.oms.api.v1.catalogs.attribute_variant.AttributeVariantCreateRequest\x1aN.pro.omni.oms.api.v1.catalogs.attribute_variant.AttributeVariantCreateResponse"(\x9a\xb5\x18$\x08\x02\x12 api/v1/catalog/attribute/variant\x12\xdb\x01\n\x14\x41ttributeVariantRead\x12K.pro.omni.oms.api.v1.catalogs.attribute_variant.AttributeVariantReadRequest\x1aL.pro.omni.oms.api.v1.catalogs.attribute_variant.AttributeVariantReadResponse"(\x9a\xb5\x18$\x08\x01\x12 api/v1/catalog/attribute/variant\x12\xe1\x01\n\x16\x41ttributeVariantUpdate\x12M.pro.omni.oms.api.v1.catalogs.attribute_variant.AttributeVariantUpdateRequest\x1aN.pro.omni.oms.api.v1.catalogs.attribute_variant.AttributeVariantUpdateResponse"(\x9a\xb5\x18$\x08\x03\x12 api/v1/catalog/attribute/variant\x12\xe1\x01\n\x16\x41ttributeVariantDelete\x12M.pro.omni.oms.api.v1.catalogs.attribute_variant.AttributeVariantDeleteRequest\x1aN.pro.omni.oms.api.v1.catalogs.attribute_variant.AttributeVariantDeleteResponse"(\x9a\xb5\x18$\x08\x04\x12 api/v1/catalog/attribute/variantb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.catalogs.attribute_variant_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _ATTRIBUTEVARIANTSERVICE.methods_by_name["AttributeVariantCreate"]._options = None
    _ATTRIBUTEVARIANTSERVICE.methods_by_name["AttributeVariantCreate"]._serialized_options = (
        b"\232\265\030$\010\002\022 api/v1/catalog/attribute/variant"
    )
    _ATTRIBUTEVARIANTSERVICE.methods_by_name["AttributeVariantRead"]._options = None
    _ATTRIBUTEVARIANTSERVICE.methods_by_name["AttributeVariantRead"]._serialized_options = (
        b"\232\265\030$\010\001\022 api/v1/catalog/attribute/variant"
    )
    _ATTRIBUTEVARIANTSERVICE.methods_by_name["AttributeVariantUpdate"]._options = None
    _ATTRIBUTEVARIANTSERVICE.methods_by_name["AttributeVariantUpdate"]._serialized_options = (
        b"\232\265\030$\010\003\022 api/v1/catalog/attribute/variant"
    )
    _ATTRIBUTEVARIANTSERVICE.methods_by_name["AttributeVariantDelete"]._options = None
    _ATTRIBUTEVARIANTSERVICE.methods_by_name["AttributeVariantDelete"]._serialized_options = (
        b"\232\265\030$\010\004\022 api/v1/catalog/attribute/variant"
    )
    _globals["_ATTRIBUTEVARIANT"]._serialized_start = 169
    _globals["_ATTRIBUTEVARIANT"]._serialized_end = 391
    _globals["_ATTRIBUTEVARIANTCREATEREQUEST"]._serialized_start = 394
    _globals["_ATTRIBUTEVARIANTCREATEREQUEST"]._serialized_end = 544
    _globals["_ATTRIBUTEVARIANTCREATERESPONSE"]._serialized_start = 547
    _globals["_ATTRIBUTEVARIANTCREATERESPONSE"]._serialized_end = 747
    _globals["_ATTRIBUTEVARIANTREADREQUEST"]._serialized_start = 750
    _globals["_ATTRIBUTEVARIANTREADREQUEST"]._serialized_end = 1127
    _globals["_ATTRIBUTEVARIANTREADRESPONSE"]._serialized_start = 1130
    _globals["_ATTRIBUTEVARIANTREADRESPONSE"]._serialized_end = 1388
    _globals["_ATTRIBUTEVARIANTUPDATEREQUEST"]._serialized_start = 1391
    _globals["_ATTRIBUTEVARIANTUPDATEREQUEST"]._serialized_end = 1571
    _globals["_ATTRIBUTEVARIANTUPDATERESPONSE"]._serialized_start = 1574
    _globals["_ATTRIBUTEVARIANTUPDATERESPONSE"]._serialized_end = 1774
    _globals["_ATTRIBUTEVARIANTDELETEREQUEST"]._serialized_start = 1776
    _globals["_ATTRIBUTEVARIANTDELETEREQUEST"]._serialized_end = 1875
    _globals["_ATTRIBUTEVARIANTDELETERESPONSE"]._serialized_start = 1877
    _globals["_ATTRIBUTEVARIANTDELETERESPONSE"]._serialized_end = 1984
    _globals["_ATTRIBUTEVARIANTSERVICE"]._serialized_start = 1987
    _globals["_ATTRIBUTEVARIANTSERVICE"]._serialized_end = 2918
# @@protoc_insertion_point(module_scope)
