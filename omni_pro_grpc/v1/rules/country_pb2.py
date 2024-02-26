# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/rules/country.proto
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
    b'\n\x16v1/rules/country.proto\x12!pro.omni.oms.api.v1.rules.country\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xcb\x01\n\x07\x43ountry\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x16\n\x0e\x63ountry_doc_id\x18\x04 \x01(\t\x12*\n\x06\x61\x63tive\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x06 \x01(\t\x12?\n\x0cobject_audit\x18\x07 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\x98\x01\n\x14\x43ountryCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x17\n\x0f\x63\x61tegory_doc_id\x18\x03 \x01(\t\x12\x13\n\x0b\x65xternal_id\x18\x04 \x01(\t\x12\x36\n\x07\x63ontext\x18\x05 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9f\x01\n\x15\x43ountryCreateResponse\x12;\n\x07\x63ountry\x18\x01 \x01(\x0b\x32*.pro.omni.oms.api.v1.rules.country.Country\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xf0\x02\n\x12\x43ountryReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\t\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xda\x01\n\x13\x43ountryReadResponse\x12=\n\tcountries\x18\x01 \x03(\x0b\x32*.pro.omni.oms.api.v1.rules.country.Country\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12I\n\x11response_standard\x18\x03 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\x8b\x01\n\x14\x43ountryUpdateRequest\x12;\n\x07\x63ountry\x18\x01 \x01(\x0b\x32*.pro.omni.oms.api.v1.rules.country.Country\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9f\x01\n\x15\x43ountryUpdateResponse\x12;\n\x07\x63ountry\x18\x01 \x01(\x0b\x32*.pro.omni.oms.api.v1.rules.country.Country\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"Z\n\x14\x43ountryDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"b\n\x15\x43ountryDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xa5\x04\n\x0e\x43ountryService\x12\x84\x01\n\rCountryCreate\x12\x37.pro.omni.oms.api.v1.rules.country.CountryCreateRequest\x1a\x38.pro.omni.oms.api.v1.rules.country.CountryCreateResponse"\x00\x12~\n\x0b\x43ountryRead\x12\x35.pro.omni.oms.api.v1.rules.country.CountryReadRequest\x1a\x36.pro.omni.oms.api.v1.rules.country.CountryReadResponse"\x00\x12\x84\x01\n\rCountryUpdate\x12\x37.pro.omni.oms.api.v1.rules.country.CountryUpdateRequest\x1a\x38.pro.omni.oms.api.v1.rules.country.CountryUpdateResponse"\x00\x12\x84\x01\n\rCountryDelete\x12\x37.pro.omni.oms.api.v1.rules.country.CountryDeleteRequest\x1a\x38.pro.omni.oms.api.v1.rules.country.CountryDeleteResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.rules.country_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _globals["_COUNTRY"]._serialized_start = 113
    _globals["_COUNTRY"]._serialized_end = 316
    _globals["_COUNTRYCREATEREQUEST"]._serialized_start = 319
    _globals["_COUNTRYCREATEREQUEST"]._serialized_end = 471
    _globals["_COUNTRYCREATERESPONSE"]._serialized_start = 474
    _globals["_COUNTRYCREATERESPONSE"]._serialized_end = 633
    _globals["_COUNTRYREADREQUEST"]._serialized_start = 636
    _globals["_COUNTRYREADREQUEST"]._serialized_end = 1004
    _globals["_COUNTRYREADRESPONSE"]._serialized_start = 1007
    _globals["_COUNTRYREADRESPONSE"]._serialized_end = 1225
    _globals["_COUNTRYUPDATEREQUEST"]._serialized_start = 1228
    _globals["_COUNTRYUPDATEREQUEST"]._serialized_end = 1367
    _globals["_COUNTRYUPDATERESPONSE"]._serialized_start = 1370
    _globals["_COUNTRYUPDATERESPONSE"]._serialized_end = 1529
    _globals["_COUNTRYDELETEREQUEST"]._serialized_start = 1531
    _globals["_COUNTRYDELETEREQUEST"]._serialized_end = 1621
    _globals["_COUNTRYDELETERESPONSE"]._serialized_start = 1623
    _globals["_COUNTRYDELETERESPONSE"]._serialized_end = 1721
    _globals["_COUNTRYSERVICE"]._serialized_start = 1724
    _globals["_COUNTRYSERVICE"]._serialized_end = 2273
# @@protoc_insertion_point(module_scope)
