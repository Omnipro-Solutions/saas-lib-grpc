# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/utilities/currency.proto
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
    b'\n\x1bv1/utilities/currency.proto\x12&pro.omni.oms.api.v1.utilities.currency\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xcb\x02\n\x08\x43urrency\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x1b\n\x13\x63urrency_unit_label\x18\x04 \x01(\t\x12\x1e\n\x16\x63urrency_subunit_label\x18\x05 \x01(\t\x12\x0c\n\x04rate\x18\x06 \x01(\x05\x12\x10\n\x08rounding\x18\x07 \x01(\x01\x12\x16\n\x0e\x64\x65\x63imal_places\x18\x08 \x01(\x05\x12\x0e\n\x06symbol\x18\t \x01(\t\x12\x10\n\x08position\x18\n \x01(\t\x12*\n\x06\x61\x63tive\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x0c \x01(\t\x12?\n\x0cobject_audit\x18\r \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xc0\x02\n\x12\x43urrencyAddRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x1b\n\x13\x63urrency_unit_label\x18\x03 \x01(\t\x12\x1e\n\x16\x63urrency_subunit_label\x18\x04 \x01(\t\x12\x0c\n\x04rate\x18\x05 \x01(\x05\x12\x10\n\x08rounding\x18\x06 \x01(\x01\x12\x16\n\x0e\x64\x65\x63imal_places\x18\x07 \x01(\x05\x12\x0e\n\x06symbol\x18\x08 \x01(\t\x12\x10\n\x08position\x18\t \x01(\t\x12*\n\x06\x61\x63tive\x18\n \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x0b \x01(\t\x12\x36\n\x07\x63ontext\x18\x0c \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xa4\x01\n\x13\x43urrencyAddResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x42\n\x08\x63urrency\x18\x02 \x01(\x0b\x32\x30.pro.omni.oms.api.v1.utilities.currency.Currency"\xf1\x02\n\x13\x43urrencyReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\t\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xe2\x01\n\x14\x43urrencyReadResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12\x44\n\ncurrencies\x18\x03 \x03(\x0b\x32\x30.pro.omni.oms.api.v1.utilities.currency.Currency"\x93\x01\n\x15\x43urrencyUpdateRequest\x12\x42\n\x08\x63urrency\x18\x01 \x01(\x0b\x32\x30.pro.omni.oms.api.v1.utilities.currency.Currency\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xa7\x01\n\x16\x43urrencyUpdateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x42\n\x08\x63urrency\x18\x02 \x01(\x0b\x32\x30.pro.omni.oms.api.v1.utilities.currency.Currency"[\n\x15\x43urrencyDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"c\n\x16\x43urrencyDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xd6\x05\n\x0f\x43urrencyService\x12\xa9\x01\n\x0b\x43urrencyAdd\x12:.pro.omni.oms.api.v1.utilities.currency.CurrencyAddRequest\x1a;.pro.omni.oms.api.v1.utilities.currency.CurrencyAddResponse"!\x9a\xb5\x18\x1d\x08\x02\x12\x19\x61pi/v1/utilities/currency\x12\xac\x01\n\x0c\x43urrencyRead\x12;.pro.omni.oms.api.v1.utilities.currency.CurrencyReadRequest\x1a<.pro.omni.oms.api.v1.utilities.currency.CurrencyReadResponse"!\x9a\xb5\x18\x1d\x08\x01\x12\x19\x61pi/v1/utilities/currency\x12\xb2\x01\n\x0e\x43urrencyUpdate\x12=.pro.omni.oms.api.v1.utilities.currency.CurrencyUpdateRequest\x1a>.pro.omni.oms.api.v1.utilities.currency.CurrencyUpdateResponse"!\x9a\xb5\x18\x1d\x08\x03\x12\x19\x61pi/v1/utilities/currency\x12\xb2\x01\n\x0e\x43urrencyDelete\x12=.pro.omni.oms.api.v1.utilities.currency.CurrencyDeleteRequest\x1a>.pro.omni.oms.api.v1.utilities.currency.CurrencyDeleteResponse"!\x9a\xb5\x18\x1d\x08\x04\x12\x19\x61pi/v1/utilities/currencyb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.utilities.currency_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _CURRENCYSERVICE.methods_by_name["CurrencyAdd"]._options = None
    _CURRENCYSERVICE.methods_by_name["CurrencyAdd"]._serialized_options = (
        b"\232\265\030\035\010\002\022\031api/v1/utilities/currency"
    )
    _CURRENCYSERVICE.methods_by_name["CurrencyRead"]._options = None
    _CURRENCYSERVICE.methods_by_name["CurrencyRead"]._serialized_options = (
        b"\232\265\030\035\010\001\022\031api/v1/utilities/currency"
    )
    _CURRENCYSERVICE.methods_by_name["CurrencyUpdate"]._options = None
    _CURRENCYSERVICE.methods_by_name["CurrencyUpdate"]._serialized_options = (
        b"\232\265\030\035\010\003\022\031api/v1/utilities/currency"
    )
    _CURRENCYSERVICE.methods_by_name["CurrencyDelete"]._options = None
    _CURRENCYSERVICE.methods_by_name["CurrencyDelete"]._serialized_options = (
        b"\232\265\030\035\010\004\022\031api/v1/utilities/currency"
    )
    _globals["_CURRENCY"]._serialized_start = 123
    _globals["_CURRENCY"]._serialized_end = 454
    _globals["_CURRENCYADDREQUEST"]._serialized_start = 457
    _globals["_CURRENCYADDREQUEST"]._serialized_end = 777
    _globals["_CURRENCYADDRESPONSE"]._serialized_start = 780
    _globals["_CURRENCYADDRESPONSE"]._serialized_end = 944
    _globals["_CURRENCYREADREQUEST"]._serialized_start = 947
    _globals["_CURRENCYREADREQUEST"]._serialized_end = 1316
    _globals["_CURRENCYREADRESPONSE"]._serialized_start = 1319
    _globals["_CURRENCYREADRESPONSE"]._serialized_end = 1545
    _globals["_CURRENCYUPDATEREQUEST"]._serialized_start = 1548
    _globals["_CURRENCYUPDATEREQUEST"]._serialized_end = 1695
    _globals["_CURRENCYUPDATERESPONSE"]._serialized_start = 1698
    _globals["_CURRENCYUPDATERESPONSE"]._serialized_end = 1865
    _globals["_CURRENCYDELETEREQUEST"]._serialized_start = 1867
    _globals["_CURRENCYDELETEREQUEST"]._serialized_end = 1958
    _globals["_CURRENCYDELETERESPONSE"]._serialized_start = 1960
    _globals["_CURRENCYDELETERESPONSE"]._serialized_end = 2059
    _globals["_CURRENCYSERVICE"]._serialized_start = 2062
    _globals["_CURRENCYSERVICE"]._serialized_end = 2788
# @@protoc_insertion_point(module_scope)
