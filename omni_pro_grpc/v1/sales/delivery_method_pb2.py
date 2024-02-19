# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/sales/delivery_method.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from omni_pro_grpc.common import base_pb2 as common_dot_base__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ev1/sales/delivery_method.proto\x12)pro.omni.oms.api.v1.sales.delivery.method\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xda\x01\n\x0e\x44\x65liveryMethod\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x1e\n\x16\x64\x65livery_method_doc_id\x18\x04 \x01(\t\x12*\n\x06\x61\x63tive\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x06 \x01(\t\x12?\n\x0cobject_audit\x18\x07 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit\"\xa6\x01\n\x1b\x44\x65liveryMethodCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x1e\n\x16\x64\x65livery_method_doc_id\x18\x03 \x01(\t\x12\x13\n\x0b\x65xternal_id\x18\x04 \x01(\t\x12\x36\n\x07\x63ontext\x18\x05 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context\"\xbd\x01\n\x1c\x44\x65liveryMethodCreateResponse\x12R\n\x0f\x64\x65livery_method\x18\x01 \x01(\x0b\x32\x39.pro.omni.oms.api.v1.sales.delivery.method.DeliveryMethod\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\"\xf7\x02\n\x19\x44\x65liveryMethodReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context\"\xf7\x01\n\x1a\x44\x65liveryMethodReadResponse\x12S\n\x10\x64\x65livery_methods\x18\x01 \x03(\x0b\x32\x39.pro.omni.oms.api.v1.sales.delivery.method.DeliveryMethod\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12I\n\x11response_standard\x18\x03 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\"\xa9\x01\n\x1b\x44\x65liveryMethodUpdateRequest\x12R\n\x0f\x64\x65livery_method\x18\x01 \x01(\x0b\x32\x39.pro.omni.oms.api.v1.sales.delivery.method.DeliveryMethod\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context\"\xbd\x01\n\x1c\x44\x65liveryMethodUpdateResponse\x12R\n\x0f\x64\x65livery_method\x18\x01 \x01(\x0b\x32\x39.pro.omni.oms.api.v1.sales.delivery.method.DeliveryMethod\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\"a\n\x1b\x44\x65liveryMethodDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context\"i\n\x1c\x44\x65liveryMethodDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xc1\x05\n\x15\x44\x65liveryMethodService\x12\xa9\x01\n\x14\x44\x65liveryMethodCreate\x12\x46.pro.omni.oms.api.v1.sales.delivery.method.DeliveryMethodCreateRequest\x1aG.pro.omni.oms.api.v1.sales.delivery.method.DeliveryMethodCreateResponse\"\x00\x12\xa3\x01\n\x12\x44\x65liveryMethodRead\x12\x44.pro.omni.oms.api.v1.sales.delivery.method.DeliveryMethodReadRequest\x1a\x45.pro.omni.oms.api.v1.sales.delivery.method.DeliveryMethodReadResponse\"\x00\x12\xa9\x01\n\x14\x44\x65liveryMethodUpdate\x12\x46.pro.omni.oms.api.v1.sales.delivery.method.DeliveryMethodUpdateRequest\x1aG.pro.omni.oms.api.v1.sales.delivery.method.DeliveryMethodUpdateResponse\"\x00\x12\xa9\x01\n\x14\x44\x65liveryMethodDelete\x12\x46.pro.omni.oms.api.v1.sales.delivery.method.DeliveryMethodDeleteRequest\x1aG.pro.omni.oms.api.v1.sales.delivery.method.DeliveryMethodDeleteResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'v1.sales.delivery_method_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_DELIVERYMETHOD']._serialized_start=129
  _globals['_DELIVERYMETHOD']._serialized_end=347
  _globals['_DELIVERYMETHODCREATEREQUEST']._serialized_start=350
  _globals['_DELIVERYMETHODCREATEREQUEST']._serialized_end=516
  _globals['_DELIVERYMETHODCREATERESPONSE']._serialized_start=519
  _globals['_DELIVERYMETHODCREATERESPONSE']._serialized_end=708
  _globals['_DELIVERYMETHODREADREQUEST']._serialized_start=711
  _globals['_DELIVERYMETHODREADREQUEST']._serialized_end=1086
  _globals['_DELIVERYMETHODREADRESPONSE']._serialized_start=1089
  _globals['_DELIVERYMETHODREADRESPONSE']._serialized_end=1336
  _globals['_DELIVERYMETHODUPDATEREQUEST']._serialized_start=1339
  _globals['_DELIVERYMETHODUPDATEREQUEST']._serialized_end=1508
  _globals['_DELIVERYMETHODUPDATERESPONSE']._serialized_start=1511
  _globals['_DELIVERYMETHODUPDATERESPONSE']._serialized_end=1700
  _globals['_DELIVERYMETHODDELETEREQUEST']._serialized_start=1702
  _globals['_DELIVERYMETHODDELETEREQUEST']._serialized_end=1799
  _globals['_DELIVERYMETHODDELETERESPONSE']._serialized_start=1801
  _globals['_DELIVERYMETHODDELETERESPONSE']._serialized_end=1906
  _globals['_DELIVERYMETHODSERVICE']._serialized_start=1909
  _globals['_DELIVERYMETHODSERVICE']._serialized_end=2614
# @@protoc_insertion_point(module_scope)
