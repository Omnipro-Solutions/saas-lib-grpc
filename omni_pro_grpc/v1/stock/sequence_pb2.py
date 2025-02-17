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
    b'\n\x17v1/stock/sequence.proto\x12"pro.omni.oms.api.v1.stock.sequence\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xb3\x02\n\x08Sequence\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x16\n\x0eimplementation\x18\x04 \x01(\t\x12\x0e\n\x06prefix\x18\x05 \x01(\t\x12\x0e\n\x06suffix\x18\x06 \x01(\t\x12\x0f\n\x07padding\x18\x07 \x01(\x02\x12\x18\n\x10number_increment\x18\x08 \x01(\x05\x12\x1a\n\x12number_next_actual\x18\t \x01(\x05\x12*\n\x06\x61\x63tive\x18\n \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x0b \x01(\t\x12?\n\x0cobject_audit\x18\x0c \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xff\x01\n\x15SequenceCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x16\n\x0eimplementation\x18\x03 \x01(\t\x12\x0e\n\x06prefix\x18\x04 \x01(\t\x12\x0e\n\x06suffix\x18\x05 \x01(\t\x12\x0f\n\x07padding\x18\x06 \x01(\x02\x12\x18\n\x10number_increment\x18\x07 \x01(\x05\x12\x1a\n\x12number_next_actual\x18\x08 \x01(\x05\x12\x13\n\x0b\x65xternal_id\x18\t \x01(\t\x12\x36\n\x07\x63ontext\x18\n \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xa3\x01\n\x16SequenceCreateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12>\n\x08sequence\x18\x02 \x01(\x0b\x32,.pro.omni.oms.api.v1.stock.sequence.Sequence"\xf1\x02\n\x13SequenceReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xdd\x01\n\x14SequenceReadResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12?\n\tsequences\x18\x03 \x03(\x0b\x32,.pro.omni.oms.api.v1.stock.sequence.Sequence"\x8f\x01\n\x15SequenceUpdateRequest\x12>\n\x08sequence\x18\x01 \x01(\x0b\x32,.pro.omni.oms.api.v1.stock.sequence.Sequence\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xa3\x01\n\x16SequenceUpdateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12>\n\x08sequence\x18\x02 \x01(\x0b\x32,.pro.omni.oms.api.v1.stock.sequence.Sequence"[\n\x15SequenceDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"c\n\x16SequenceDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"U\n\x0fNextByIdRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"Y\n\x11NextByCodeRequest\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x1c\n\x0cNextResponse\x12\x0c\n\x04next\x18\x01 \x01(\t2\xa5\x07\n\x0fSequenceService\x12\xa6\x01\n\x0eSequenceCreate\x12\x39.pro.omni.oms.api.v1.stock.sequence.SequenceCreateRequest\x1a:.pro.omni.oms.api.v1.stock.sequence.SequenceCreateResponse"\x1d\x9a\xb5\x18\x19\x08\x02\x12\x15\x61pi/v1/stock/sequence\x12\xa0\x01\n\x0cSequenceRead\x12\x37.pro.omni.oms.api.v1.stock.sequence.SequenceReadRequest\x1a\x38.pro.omni.oms.api.v1.stock.sequence.SequenceReadResponse"\x1d\x9a\xb5\x18\x19\x08\x01\x12\x15\x61pi/v1/stock/sequence\x12\xa6\x01\n\x0eSequenceUpdate\x12\x39.pro.omni.oms.api.v1.stock.sequence.SequenceUpdateRequest\x1a:.pro.omni.oms.api.v1.stock.sequence.SequenceUpdateResponse"\x1d\x9a\xb5\x18\x19\x08\x03\x12\x15\x61pi/v1/stock/sequence\x12\xa6\x01\n\x0eSequenceDelete\x12\x39.pro.omni.oms.api.v1.stock.sequence.SequenceDeleteRequest\x1a:.pro.omni.oms.api.v1.stock.sequence.SequenceDeleteResponse"\x1d\x9a\xb5\x18\x19\x08\x04\x12\x15\x61pi/v1/stock/sequence\x12w\n\x08NextById\x12\x33.pro.omni.oms.api.v1.stock.sequence.NextByIdRequest\x1a\x30.pro.omni.oms.api.v1.stock.sequence.NextResponse"\x04\x90\xb5\x18\x01\x12{\n\nNextByCode\x12\x35.pro.omni.oms.api.v1.stock.sequence.NextByCodeRequest\x1a\x30.pro.omni.oms.api.v1.stock.sequence.NextResponse"\x04\x90\xb5\x18\x01\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.stock.sequence_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _SEQUENCESERVICE.methods_by_name["SequenceCreate"]._options = None
    _SEQUENCESERVICE.methods_by_name["SequenceCreate"]._serialized_options = (
        b"\232\265\030\031\010\002\022\025api/v1/stock/sequence"
    )
    _SEQUENCESERVICE.methods_by_name["SequenceRead"]._options = None
    _SEQUENCESERVICE.methods_by_name["SequenceRead"]._serialized_options = (
        b"\232\265\030\031\010\001\022\025api/v1/stock/sequence"
    )
    _SEQUENCESERVICE.methods_by_name["SequenceUpdate"]._options = None
    _SEQUENCESERVICE.methods_by_name["SequenceUpdate"]._serialized_options = (
        b"\232\265\030\031\010\003\022\025api/v1/stock/sequence"
    )
    _SEQUENCESERVICE.methods_by_name["SequenceDelete"]._options = None
    _SEQUENCESERVICE.methods_by_name["SequenceDelete"]._serialized_options = (
        b"\232\265\030\031\010\004\022\025api/v1/stock/sequence"
    )
    _SEQUENCESERVICE.methods_by_name["NextById"]._options = None
    _SEQUENCESERVICE.methods_by_name["NextById"]._serialized_options = b"\220\265\030\001"
    _SEQUENCESERVICE.methods_by_name["NextByCode"]._options = None
    _SEQUENCESERVICE.methods_by_name["NextByCode"]._serialized_options = b"\220\265\030\001"
    _globals["_SEQUENCE"]._serialized_start = 115
    _globals["_SEQUENCE"]._serialized_end = 422
    _globals["_SEQUENCECREATEREQUEST"]._serialized_start = 425
    _globals["_SEQUENCECREATEREQUEST"]._serialized_end = 680
    _globals["_SEQUENCECREATERESPONSE"]._serialized_start = 683
    _globals["_SEQUENCECREATERESPONSE"]._serialized_end = 846
    _globals["_SEQUENCEREADREQUEST"]._serialized_start = 849
    _globals["_SEQUENCEREADREQUEST"]._serialized_end = 1218
    _globals["_SEQUENCEREADRESPONSE"]._serialized_start = 1221
    _globals["_SEQUENCEREADRESPONSE"]._serialized_end = 1442
    _globals["_SEQUENCEUPDATEREQUEST"]._serialized_start = 1445
    _globals["_SEQUENCEUPDATEREQUEST"]._serialized_end = 1588
    _globals["_SEQUENCEUPDATERESPONSE"]._serialized_start = 1591
    _globals["_SEQUENCEUPDATERESPONSE"]._serialized_end = 1754
    _globals["_SEQUENCEDELETEREQUEST"]._serialized_start = 1756
    _globals["_SEQUENCEDELETEREQUEST"]._serialized_end = 1847
    _globals["_SEQUENCEDELETERESPONSE"]._serialized_start = 1849
    _globals["_SEQUENCEDELETERESPONSE"]._serialized_end = 1948
    _globals["_NEXTBYIDREQUEST"]._serialized_start = 1950
    _globals["_NEXTBYIDREQUEST"]._serialized_end = 2035
    _globals["_NEXTBYCODEREQUEST"]._serialized_start = 2037
    _globals["_NEXTBYCODEREQUEST"]._serialized_end = 2126
    _globals["_NEXTRESPONSE"]._serialized_start = 2128
    _globals["_NEXTRESPONSE"]._serialized_end = 2156
    _globals["_SEQUENCESERVICE"]._serialized_start = 2159
    _globals["_SEQUENCESERVICE"]._serialized_end = 3092
# @@protoc_insertion_point(module_scope)
