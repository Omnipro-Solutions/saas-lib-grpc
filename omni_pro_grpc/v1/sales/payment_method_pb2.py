# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/sales/payment_method.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from omni_pro_grpc.common import base_pb2 as common_dot_base__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dv1/sales/payment_method.proto\x12(pro.omni.oms.api.v1.sales.payment.method\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xb9\x01\n\rPaymentMethod\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12*\n\x06\x61\x63tive\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x05 \x01(\t\x12?\n\x0cobject_audit\x18\x06 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit\"\x85\x01\n\x1aPaymentMethodCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x13\n\x0b\x65xternal_id\x18\x03 \x01(\t\x12\x36\n\x07\x63ontext\x18\x04 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context\"\xb9\x01\n\x1bPaymentMethodCreateResponse\x12O\n\x0epayment_method\x18\x01 \x01(\x0b\x32\x37.pro.omni.oms.api.v1.sales.payment.method.PaymentMethod\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\"\xf6\x02\n\x18PaymentMethodReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context\"\xf3\x01\n\x19PaymentMethodReadResponse\x12P\n\x0fpayment_methods\x18\x01 \x03(\x0b\x32\x37.pro.omni.oms.api.v1.sales.payment.method.PaymentMethod\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x03 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\"\xa5\x01\n\x1aPaymentMethodUpdateRequest\x12O\n\x0epayment_method\x18\x01 \x01(\x0b\x32\x37.pro.omni.oms.api.v1.sales.payment.method.PaymentMethod\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context\"\xb9\x01\n\x1bPaymentMethodUpdateResponse\x12O\n\x0epayment_method\x18\x01 \x01(\x0b\x32\x37.pro.omni.oms.api.v1.sales.payment.method.PaymentMethod\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\"`\n\x1aPaymentMethodDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context\"h\n\x1bPaymentMethodDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xac\x05\n\x14PaymentMethodService\x12\xa4\x01\n\x13PaymentMethodCreate\x12\x44.pro.omni.oms.api.v1.sales.payment.method.PaymentMethodCreateRequest\x1a\x45.pro.omni.oms.api.v1.sales.payment.method.PaymentMethodCreateResponse\"\x00\x12\x9e\x01\n\x11PaymentMethodRead\x12\x42.pro.omni.oms.api.v1.sales.payment.method.PaymentMethodReadRequest\x1a\x43.pro.omni.oms.api.v1.sales.payment.method.PaymentMethodReadResponse\"\x00\x12\xa4\x01\n\x13PaymentMethodUpdate\x12\x44.pro.omni.oms.api.v1.sales.payment.method.PaymentMethodUpdateRequest\x1a\x45.pro.omni.oms.api.v1.sales.payment.method.PaymentMethodUpdateResponse\"\x00\x12\xa4\x01\n\x13PaymentMethodDelete\x12\x44.pro.omni.oms.api.v1.sales.payment.method.PaymentMethodDeleteRequest\x1a\x45.pro.omni.oms.api.v1.sales.payment.method.PaymentMethodDeleteResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'v1.sales.payment_method_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_PAYMENTMETHOD']._serialized_start=127
  _globals['_PAYMENTMETHOD']._serialized_end=312
  _globals['_PAYMENTMETHODCREATEREQUEST']._serialized_start=315
  _globals['_PAYMENTMETHODCREATEREQUEST']._serialized_end=448
  _globals['_PAYMENTMETHODCREATERESPONSE']._serialized_start=451
  _globals['_PAYMENTMETHODCREATERESPONSE']._serialized_end=636
  _globals['_PAYMENTMETHODREADREQUEST']._serialized_start=639
  _globals['_PAYMENTMETHODREADREQUEST']._serialized_end=1013
  _globals['_PAYMENTMETHODREADRESPONSE']._serialized_start=1016
  _globals['_PAYMENTMETHODREADRESPONSE']._serialized_end=1259
  _globals['_PAYMENTMETHODUPDATEREQUEST']._serialized_start=1262
  _globals['_PAYMENTMETHODUPDATEREQUEST']._serialized_end=1427
  _globals['_PAYMENTMETHODUPDATERESPONSE']._serialized_start=1430
  _globals['_PAYMENTMETHODUPDATERESPONSE']._serialized_end=1615
  _globals['_PAYMENTMETHODDELETEREQUEST']._serialized_start=1617
  _globals['_PAYMENTMETHODDELETEREQUEST']._serialized_end=1713
  _globals['_PAYMENTMETHODDELETERESPONSE']._serialized_start=1715
  _globals['_PAYMENTMETHODDELETERESPONSE']._serialized_end=1819
  _globals['_PAYMENTMETHODSERVICE']._serialized_start=1822
  _globals['_PAYMENTMETHODSERVICE']._serialized_end=2506
# @@protoc_insertion_point(module_scope)
