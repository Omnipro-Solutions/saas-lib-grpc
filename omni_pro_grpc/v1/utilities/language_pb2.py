# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/utilities/language.proto
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
    b'\n\x1bv1/utilities/language.proto\x12&pro.omni.oms.api.v1.utilities.language\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xeb\x02\n\x08Language\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x10\n\x08\x63ode_iso\x18\x04 \x01(\t\x12\x11\n\tdirection\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x61te_format\x18\x06 \x01(\t\x12\x13\n\x0btime_format\x18\x07 \x01(\t\x12\x15\n\rdecimal_point\x18\x08 \x01(\t\x12\x1b\n\x13thousands_separator\x18\t \x01(\t\x12\x10\n\x08grouping\x18\n \x01(\t\x12\x12\n\nweek_start\x18\x0b \x01(\t\x12\x0c\n\x04icon\x18\x0c \x01(\x0c\x12*\n\x06\x61\x63tive\x18\r \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x0e \x01(\t\x12?\n\x0cobject_audit\x18\x0f \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xe0\x02\n\x12LanguageAddRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x10\n\x08\x63ode_iso\x18\x03 \x01(\t\x12\x11\n\tdirection\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x61te_format\x18\x05 \x01(\t\x12\x13\n\x0btime_format\x18\x06 \x01(\t\x12\x15\n\rdecimal_point\x18\x07 \x01(\t\x12\x1b\n\x13thousands_separator\x18\x08 \x01(\t\x12\x10\n\x08grouping\x18\t \x01(\t\x12\x12\n\nweek_start\x18\n \x01(\t\x12\x0c\n\x04icon\x18\x0b \x01(\x0c\x12*\n\x06\x61\x63tive\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\r \x01(\t\x12\x36\n\x07\x63ontext\x18\x0e \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xa4\x01\n\x13LanguageAddResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x42\n\x08language\x18\x02 \x01(\x0b\x32\x30.pro.omni.oms.api.v1.utilities.language.Language"\xf1\x02\n\x13LanguageReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\t\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xe1\x01\n\x14LanguageReadResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12\x43\n\tlanguages\x18\x03 \x03(\x0b\x32\x30.pro.omni.oms.api.v1.utilities.language.Language"\x93\x01\n\x15LanguageUpdateRequest\x12\x42\n\x08language\x18\x01 \x01(\x0b\x32\x30.pro.omni.oms.api.v1.utilities.language.Language\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xa7\x01\n\x16LanguageUpdateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x42\n\x08language\x18\x02 \x01(\x0b\x32\x30.pro.omni.oms.api.v1.utilities.language.Language"[\n\x15LanguageDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"c\n\x16LanguageDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xd2\x04\n\x0fLanguageService\x12\x88\x01\n\x0bLanguageAdd\x12:.pro.omni.oms.api.v1.utilities.language.LanguageAddRequest\x1a;.pro.omni.oms.api.v1.utilities.language.LanguageAddResponse"\x00\x12\x8b\x01\n\x0cLanguageRead\x12;.pro.omni.oms.api.v1.utilities.language.LanguageReadRequest\x1a<.pro.omni.oms.api.v1.utilities.language.LanguageReadResponse"\x00\x12\x91\x01\n\x0eLanguageUpdate\x12=.pro.omni.oms.api.v1.utilities.language.LanguageUpdateRequest\x1a>.pro.omni.oms.api.v1.utilities.language.LanguageUpdateResponse"\x00\x12\x91\x01\n\x0eLanguageDelete\x12=.pro.omni.oms.api.v1.utilities.language.LanguageDeleteRequest\x1a>.pro.omni.oms.api.v1.utilities.language.LanguageDeleteResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.utilities.language_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _globals["_LANGUAGE"]._serialized_start = 123
    _globals["_LANGUAGE"]._serialized_end = 486
    _globals["_LANGUAGEADDREQUEST"]._serialized_start = 489
    _globals["_LANGUAGEADDREQUEST"]._serialized_end = 841
    _globals["_LANGUAGEADDRESPONSE"]._serialized_start = 844
    _globals["_LANGUAGEADDRESPONSE"]._serialized_end = 1008
    _globals["_LANGUAGEREADREQUEST"]._serialized_start = 1011
    _globals["_LANGUAGEREADREQUEST"]._serialized_end = 1380
    _globals["_LANGUAGEREADRESPONSE"]._serialized_start = 1383
    _globals["_LANGUAGEREADRESPONSE"]._serialized_end = 1608
    _globals["_LANGUAGEUPDATEREQUEST"]._serialized_start = 1611
    _globals["_LANGUAGEUPDATEREQUEST"]._serialized_end = 1758
    _globals["_LANGUAGEUPDATERESPONSE"]._serialized_start = 1761
    _globals["_LANGUAGEUPDATERESPONSE"]._serialized_end = 1928
    _globals["_LANGUAGEDELETEREQUEST"]._serialized_start = 1930
    _globals["_LANGUAGEDELETEREQUEST"]._serialized_end = 2021
    _globals["_LANGUAGEDELETERESPONSE"]._serialized_start = 2023
    _globals["_LANGUAGEDELETERESPONSE"]._serialized_end = 2122
    _globals["_LANGUAGESERVICE"]._serialized_start = 2125
    _globals["_LANGUAGESERVICE"]._serialized_end = 2719
# @@protoc_insertion_point(module_scope)
