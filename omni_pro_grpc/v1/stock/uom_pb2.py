# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/stock/uom.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from omni_pro_grpc.common import base_pb2 as common_dot_base__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12v1/stock/uom.proto\x12\x1dpro.omni.oms.api.v1.stock.uom\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xc3\x01\n\x03Uom\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nuom_doc_id\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12*\n\x06\x61\x63tive\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x06 \x01(\t\x12?\n\x0cobject_audit\x18\x07 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit\"\x8f\x01\n\x10UomCreateRequest\x12\x12\n\nuom_doc_id\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x65xternal_id\x18\x04 \x01(\t\x12\x36\n\x07\x63ontext\x18\x05 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context\"\x86\x01\n\x11UomCreateResponse\x12@\n\x08response\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12/\n\x03uom\x18\x02 \x01(\x0b\x32\".pro.omni.oms.api.v1.stock.uom.Uom\"\xec\x02\n\x0eUomReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context\"\xc9\x01\n\x0fUomReadResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12\x30\n\x04uoms\x18\x03 \x03(\x0b\x32\".pro.omni.oms.api.v1.stock.uom.Uom\"{\n\x10UomUpdateRequest\x12/\n\x03uom\x18\x01 \x01(\x0b\x32\".pro.omni.oms.api.v1.stock.uom.Uom\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context\"\x86\x01\n\x11UomUpdateResponse\x12@\n\x08response\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12/\n\x03uom\x18\x02 \x01(\x0b\x32\".pro.omni.oms.api.v1.stock.uom.Uom\"V\n\x10UomDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context\"U\n\x11UomDeleteResponse\x12@\n\x08response\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xce\x03\n\nUomService\x12p\n\tUomCreate\x12/.pro.omni.oms.api.v1.stock.uom.UomCreateRequest\x1a\x30.pro.omni.oms.api.v1.stock.uom.UomCreateResponse\"\x00\x12j\n\x07UomRead\x12-.pro.omni.oms.api.v1.stock.uom.UomReadRequest\x1a..pro.omni.oms.api.v1.stock.uom.UomReadResponse\"\x00\x12p\n\tUomUpdate\x12/.pro.omni.oms.api.v1.stock.uom.UomUpdateRequest\x1a\x30.pro.omni.oms.api.v1.stock.uom.UomUpdateResponse\"\x00\x12p\n\tUomDelete\x12/.pro.omni.oms.api.v1.stock.uom.UomDeleteRequest\x1a\x30.pro.omni.oms.api.v1.stock.uom.UomDeleteResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'v1.stock.uom_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_UOM']._serialized_start=105
  _globals['_UOM']._serialized_end=300
  _globals['_UOMCREATEREQUEST']._serialized_start=303
  _globals['_UOMCREATEREQUEST']._serialized_end=446
  _globals['_UOMCREATERESPONSE']._serialized_start=449
  _globals['_UOMCREATERESPONSE']._serialized_end=583
  _globals['_UOMREADREQUEST']._serialized_start=586
  _globals['_UOMREADREQUEST']._serialized_end=950
  _globals['_UOMREADRESPONSE']._serialized_start=953
  _globals['_UOMREADRESPONSE']._serialized_end=1154
  _globals['_UOMUPDATEREQUEST']._serialized_start=1156
  _globals['_UOMUPDATEREQUEST']._serialized_end=1279
  _globals['_UOMUPDATERESPONSE']._serialized_start=1282
  _globals['_UOMUPDATERESPONSE']._serialized_end=1416
  _globals['_UOMDELETEREQUEST']._serialized_start=1418
  _globals['_UOMDELETEREQUEST']._serialized_end=1504
  _globals['_UOMDELETERESPONSE']._serialized_start=1506
  _globals['_UOMDELETERESPONSE']._serialized_end=1591
  _globals['_UOMSERVICE']._serialized_start=1594
  _globals['_UOMSERVICE']._serialized_end=2056
# @@protoc_insertion_point(module_scope)
