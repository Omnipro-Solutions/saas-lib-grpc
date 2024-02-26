# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/stock/sequence.proto
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
    b'\n\x17v1/stock/sequence.proto\x12"pro.omni.oms.api.v1.stock.sequence\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xcd\x01\n\x08Sequence\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x17\n\x0fsequence_doc_id\x18\x04 \x01(\t\x12*\n\x06\x61\x63tive\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x06 \x01(\t\x12?\n\x0cobject_audit\x18\x07 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\x99\x01\n\x15SequenceCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x17\n\x0fsequence_doc_id\x18\x03 \x01(\t\x12\x13\n\x0b\x65xternal_id\x18\x04 \x01(\t\x12\x36\n\x07\x63ontext\x18\x05 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xa3\x01\n\x16SequenceCreateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12>\n\x08sequence\x18\x02 \x01(\x0b\x32,.pro.omni.oms.api.v1.stock.sequence.Sequence"\xf1\x02\n\x13SequenceReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xdd\x01\n\x14SequenceReadResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12?\n\tsequences\x18\x03 \x03(\x0b\x32,.pro.omni.oms.api.v1.stock.sequence.Sequence"\x8f\x01\n\x15SequenceUpdateRequest\x12>\n\x08sequence\x18\x01 \x01(\x0b\x32,.pro.omni.oms.api.v1.stock.sequence.Sequence\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xa3\x01\n\x16SequenceUpdateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12>\n\x08sequence\x18\x02 \x01(\x0b\x32,.pro.omni.oms.api.v1.stock.sequence.Sequence"[\n\x15SequenceDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"c\n\x16SequenceDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xbb\x04\n\x0fSequenceService\x12\x89\x01\n\x0eSequenceCreate\x12\x39.pro.omni.oms.api.v1.stock.sequence.SequenceCreateRequest\x1a:.pro.omni.oms.api.v1.stock.sequence.SequenceCreateResponse"\x00\x12\x83\x01\n\x0cSequenceRead\x12\x37.pro.omni.oms.api.v1.stock.sequence.SequenceReadRequest\x1a\x38.pro.omni.oms.api.v1.stock.sequence.SequenceReadResponse"\x00\x12\x89\x01\n\x0eSequenceUpdate\x12\x39.pro.omni.oms.api.v1.stock.sequence.SequenceUpdateRequest\x1a:.pro.omni.oms.api.v1.stock.sequence.SequenceUpdateResponse"\x00\x12\x89\x01\n\x0eSequenceDelete\x12\x39.pro.omni.oms.api.v1.stock.sequence.SequenceDeleteRequest\x1a:.pro.omni.oms.api.v1.stock.sequence.SequenceDeleteResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.stock.sequence_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _globals["_SEQUENCE"]._serialized_start = 115
    _globals["_SEQUENCE"]._serialized_end = 320
    _globals["_SEQUENCECREATEREQUEST"]._serialized_start = 323
    _globals["_SEQUENCECREATEREQUEST"]._serialized_end = 476
    _globals["_SEQUENCECREATERESPONSE"]._serialized_start = 479
    _globals["_SEQUENCECREATERESPONSE"]._serialized_end = 642
    _globals["_SEQUENCEREADREQUEST"]._serialized_start = 645
    _globals["_SEQUENCEREADREQUEST"]._serialized_end = 1014
    _globals["_SEQUENCEREADRESPONSE"]._serialized_start = 1017
    _globals["_SEQUENCEREADRESPONSE"]._serialized_end = 1238
    _globals["_SEQUENCEUPDATEREQUEST"]._serialized_start = 1241
    _globals["_SEQUENCEUPDATEREQUEST"]._serialized_end = 1384
    _globals["_SEQUENCEUPDATERESPONSE"]._serialized_start = 1387
    _globals["_SEQUENCEUPDATERESPONSE"]._serialized_end = 1550
    _globals["_SEQUENCEDELETEREQUEST"]._serialized_start = 1552
    _globals["_SEQUENCEDELETEREQUEST"]._serialized_end = 1643
    _globals["_SEQUENCEDELETERESPONSE"]._serialized_start = 1645
    _globals["_SEQUENCEDELETERESPONSE"]._serialized_end = 1744
    _globals["_SEQUENCESERVICE"]._serialized_start = 1747
    _globals["_SEQUENCESERVICE"]._serialized_end = 2318
# @@protoc_insertion_point(module_scope)
