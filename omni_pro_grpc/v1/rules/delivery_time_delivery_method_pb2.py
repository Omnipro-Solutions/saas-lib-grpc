# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/rules/delivery_time_delivery_method.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from omni_pro_grpc.common import base_pb2 as common_dot_base__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n,v1/rules/delivery_time_delivery_method.proto\x12\x37pro.omni.oms.api.v1.rules.delivery_time_delivery_method\x1a\x11\x63ommon/base.proto"\xc4\x01\n\x1a\x44\x65liveryTimeDeliveryMethod\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x18\n\x10\x64\x65livery_time_id\x18\x02 \x01(\x05\x12\x1a\n\x12\x64\x65livery_method_id\x18\x03 \x01(\x05\x12\x0e\n\x06\x61\x63tive\x18\x04 \x01(\x08\x12\x13\n\x0b\x65xternal_id\x18\x05 \x01(\t\x12?\n\x0cobject_audit\x18\x06 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xac\x01\n\'DeliveryTimeDeliveryMethodCreateRequest\x12\x18\n\x10\x64\x65livery_time_id\x18\x01 \x01(\x05\x12\x1a\n\x12\x64\x65livery_method_id\x18\x02 \x01(\x05\x12\x13\n\x0b\x65xternal_id\x18\x03 \x01(\t\x12\x36\n\x07\x63ontext\x18\x04 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xf1\x01\n(DeliveryTimeDeliveryMethodCreateResponse\x12z\n\x1d\x64\x65livery_time_delivery_method\x18\x01 \x01(\x0b\x32S.pro.omni.oms.api.v1.rules.delivery_time_delivery_method.DeliveryTimeDeliveryMethod\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\x83\x03\n%DeliveryTimeDeliveryMethodReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xaa\x02\n&DeliveryTimeDeliveryMethodReadResponse\x12z\n\x1d\x64\x65livery_time_delivery_method\x18\x01 \x03(\x0b\x32S.pro.omni.oms.api.v1.rules.delivery_time_delivery_method.DeliveryTimeDeliveryMethod\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12I\n\x11response_standard\x18\x03 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xdd\x01\n\'DeliveryTimeDeliveryMethodUpdateRequest\x12z\n\x1d\x64\x65livery_time_delivery_method\x18\x01 \x01(\x0b\x32S.pro.omni.oms.api.v1.rules.delivery_time_delivery_method.DeliveryTimeDeliveryMethod\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xf1\x01\n(DeliveryTimeDeliveryMethodUpdateResponse\x12z\n\x1d\x64\x65livery_time_delivery_method\x18\x01 \x01(\x0b\x32S.pro.omni.oms.api.v1.rules.delivery_time_delivery_method.DeliveryTimeDeliveryMethod\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"m\n\'DeliveryTimeDeliveryMethodDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"u\n(DeliveryTimeDeliveryMethodDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xcd\x07\n!DeliveryTimeDeliveryMethodService\x12\xe9\x01\n DeliveryTimeDeliveryMethodCreate\x12`.pro.omni.oms.api.v1.rules.delivery_time_delivery_method.DeliveryTimeDeliveryMethodCreateRequest\x1a\x61.pro.omni.oms.api.v1.rules.delivery_time_delivery_method.DeliveryTimeDeliveryMethodCreateResponse"\x00\x12\xe3\x01\n\x1e\x44\x65liveryTimeDeliveryMethodRead\x12^.pro.omni.oms.api.v1.rules.delivery_time_delivery_method.DeliveryTimeDeliveryMethodReadRequest\x1a_.pro.omni.oms.api.v1.rules.delivery_time_delivery_method.DeliveryTimeDeliveryMethodReadResponse"\x00\x12\xe9\x01\n DeliveryTimeDeliveryMethodUpdate\x12`.pro.omni.oms.api.v1.rules.delivery_time_delivery_method.DeliveryTimeDeliveryMethodUpdateRequest\x1a\x61.pro.omni.oms.api.v1.rules.delivery_time_delivery_method.DeliveryTimeDeliveryMethodUpdateResponse"\x00\x12\xe9\x01\n DeliveryTimeDeliveryMethodDelete\x12`.pro.omni.oms.api.v1.rules.delivery_time_delivery_method.DeliveryTimeDeliveryMethodDeleteRequest\x1a\x61.pro.omni.oms.api.v1.rules.delivery_time_delivery_method.DeliveryTimeDeliveryMethodDeleteResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.rules.delivery_time_delivery_method_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _globals["_DELIVERYTIMEDELIVERYMETHOD"]._serialized_start = 125
    _globals["_DELIVERYTIMEDELIVERYMETHOD"]._serialized_end = 321
    _globals["_DELIVERYTIMEDELIVERYMETHODCREATEREQUEST"]._serialized_start = 324
    _globals["_DELIVERYTIMEDELIVERYMETHODCREATEREQUEST"]._serialized_end = 496
    _globals["_DELIVERYTIMEDELIVERYMETHODCREATERESPONSE"]._serialized_start = 499
    _globals["_DELIVERYTIMEDELIVERYMETHODCREATERESPONSE"]._serialized_end = 740
    _globals["_DELIVERYTIMEDELIVERYMETHODREADREQUEST"]._serialized_start = 743
    _globals["_DELIVERYTIMEDELIVERYMETHODREADREQUEST"]._serialized_end = 1130
    _globals["_DELIVERYTIMEDELIVERYMETHODREADRESPONSE"]._serialized_start = 1133
    _globals["_DELIVERYTIMEDELIVERYMETHODREADRESPONSE"]._serialized_end = 1431
    _globals["_DELIVERYTIMEDELIVERYMETHODUPDATEREQUEST"]._serialized_start = 1434
    _globals["_DELIVERYTIMEDELIVERYMETHODUPDATEREQUEST"]._serialized_end = 1655
    _globals["_DELIVERYTIMEDELIVERYMETHODUPDATERESPONSE"]._serialized_start = 1658
    _globals["_DELIVERYTIMEDELIVERYMETHODUPDATERESPONSE"]._serialized_end = 1899
    _globals["_DELIVERYTIMEDELIVERYMETHODDELETEREQUEST"]._serialized_start = 1901
    _globals["_DELIVERYTIMEDELIVERYMETHODDELETEREQUEST"]._serialized_end = 2010
    _globals["_DELIVERYTIMEDELIVERYMETHODDELETERESPONSE"]._serialized_start = 2012
    _globals["_DELIVERYTIMEDELIVERYMETHODDELETERESPONSE"]._serialized_end = 2129
    _globals["_DELIVERYTIMEDELIVERYMETHODSERVICE"]._serialized_start = 2132
    _globals["_DELIVERYTIMEDELIVERYMETHODSERVICE"]._serialized_end = 3105
# @@protoc_insertion_point(module_scope)
