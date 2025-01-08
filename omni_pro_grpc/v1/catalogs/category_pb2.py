# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/catalogs/category.proto
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
    b'\n\x1av1/catalogs/category.proto\x12$pro.omni.oms.api.v1.catalog.category\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xb4\x01\n\x08\x43\x61tegory\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12*\n\x06\x61\x63tive\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x05 \x01(\t\x12?\n\x0cobject_audit\x18\x06 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\x80\x01\n\x15\x43\x61tegoryCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x13\n\x0b\x65xternal_id\x18\x03 \x01(\t\x12\x36\n\x07\x63ontext\x18\x04 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xa5\x01\n\x16\x43\x61tegoryCreateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12@\n\x08\x63\x61tegory\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.v1.catalog.category.Category"\xf1\x02\n\x13\x43\x61tegoryReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\t\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xe0\x01\n\x14\x43\x61tegoryReadResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12\x42\n\ncategories\x18\x03 \x03(\x0b\x32..pro.omni.oms.api.v1.catalog.category.Category"\x91\x01\n\x15\x43\x61tegoryUpdateRequest\x12@\n\x08\x63\x61tegory\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.v1.catalog.category.Category\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xa5\x01\n\x16\x43\x61tegoryUpdateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12@\n\x08\x63\x61tegory\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.v1.catalog.category.Category"[\n\x15\x43\x61tegoryDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"c\n\x16\x43\x61tegoryDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xc7\x05\n\x0f\x43\x61tegoryService\x12\xac\x01\n\x0e\x43\x61tegoryCreate\x12;.pro.omni.oms.api.v1.catalog.category.CategoryCreateRequest\x1a<.pro.omni.oms.api.v1.catalog.category.CategoryCreateResponse"\x1f\x9a\xb5\x18\x1b\x08\x02\x12\x17\x61pi/v1/catalog/category\x12\xa6\x01\n\x0c\x43\x61tegoryRead\x12\x39.pro.omni.oms.api.v1.catalog.category.CategoryReadRequest\x1a:.pro.omni.oms.api.v1.catalog.category.CategoryReadResponse"\x1f\x9a\xb5\x18\x1b\x08\x01\x12\x17\x61pi/v1/catalog/category\x12\xac\x01\n\x0e\x43\x61tegoryUpdate\x12;.pro.omni.oms.api.v1.catalog.category.CategoryUpdateRequest\x1a<.pro.omni.oms.api.v1.catalog.category.CategoryUpdateResponse"\x1f\x9a\xb5\x18\x1b\x08\x03\x12\x17\x61pi/v1/catalog/category\x12\xac\x01\n\x0e\x43\x61tegoryDelete\x12;.pro.omni.oms.api.v1.catalog.category.CategoryDeleteRequest\x1a<.pro.omni.oms.api.v1.catalog.category.CategoryDeleteResponse"\x1f\x9a\xb5\x18\x1b\x08\x04\x12\x17\x61pi/v1/catalog/categoryb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.catalogs.category_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _CATEGORYSERVICE.methods_by_name["CategoryCreate"]._options = None
    _CATEGORYSERVICE.methods_by_name["CategoryCreate"]._serialized_options = (
        b"\232\265\030\033\010\002\022\027api/v1/catalog/category"
    )
    _CATEGORYSERVICE.methods_by_name["CategoryRead"]._options = None
    _CATEGORYSERVICE.methods_by_name["CategoryRead"]._serialized_options = (
        b"\232\265\030\033\010\001\022\027api/v1/catalog/category"
    )
    _CATEGORYSERVICE.methods_by_name["CategoryUpdate"]._options = None
    _CATEGORYSERVICE.methods_by_name["CategoryUpdate"]._serialized_options = (
        b"\232\265\030\033\010\003\022\027api/v1/catalog/category"
    )
    _CATEGORYSERVICE.methods_by_name["CategoryDelete"]._options = None
    _CATEGORYSERVICE.methods_by_name["CategoryDelete"]._serialized_options = (
        b"\232\265\030\033\010\004\022\027api/v1/catalog/category"
    )
    _globals["_CATEGORY"]._serialized_start = 120
    _globals["_CATEGORY"]._serialized_end = 300
    _globals["_CATEGORYCREATEREQUEST"]._serialized_start = 303
    _globals["_CATEGORYCREATEREQUEST"]._serialized_end = 431
    _globals["_CATEGORYCREATERESPONSE"]._serialized_start = 434
    _globals["_CATEGORYCREATERESPONSE"]._serialized_end = 599
    _globals["_CATEGORYREADREQUEST"]._serialized_start = 602
    _globals["_CATEGORYREADREQUEST"]._serialized_end = 971
    _globals["_CATEGORYREADRESPONSE"]._serialized_start = 974
    _globals["_CATEGORYREADRESPONSE"]._serialized_end = 1198
    _globals["_CATEGORYUPDATEREQUEST"]._serialized_start = 1201
    _globals["_CATEGORYUPDATEREQUEST"]._serialized_end = 1346
    _globals["_CATEGORYUPDATERESPONSE"]._serialized_start = 1349
    _globals["_CATEGORYUPDATERESPONSE"]._serialized_end = 1514
    _globals["_CATEGORYDELETEREQUEST"]._serialized_start = 1516
    _globals["_CATEGORYDELETEREQUEST"]._serialized_end = 1607
    _globals["_CATEGORYDELETERESPONSE"]._serialized_start = 1609
    _globals["_CATEGORYDELETERESPONSE"]._serialized_end = 1708
    _globals["_CATEGORYSERVICE"]._serialized_start = 1711
    _globals["_CATEGORYSERVICE"]._serialized_end = 2422
# @@protoc_insertion_point(module_scope)
