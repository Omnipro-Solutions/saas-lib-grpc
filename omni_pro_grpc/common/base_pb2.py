# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/base.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x11\x63ommon/base.proto\x12\x1cpro.omni.oms.api.common.base\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/protobuf/struct.proto")\n\x06Object\x12\x11\n\tcode_name\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t"\x1d\n\x07GroupBy\x12\x12\n\nname_field\x18\x01 \x01(\t"x\n\x06SortBy\x12\x12\n\nname_field\x18\x01 \x01(\t\x12;\n\x04type\x18\x02 \x01(\x0e\x32-.pro.omni.oms.api.common.base.SortBy.SortType"\x1d\n\x08SortType\x12\x07\n\x03\x41SC\x10\x00\x12\x08\n\x04\x44\x45SC\x10\x01"\x1c\n\x06\x46ields\x12\x12\n\nname_field\x18\x01 \x03(\t"\x18\n\x06\x46ilter\x12\x0e\n\x06\x66ilter\x18\x01 \x01(\t"*\n\tPaginated\x12\x0e\n\x06offset\x18\x01 \x01(\x05\x12\r\n\x05limit\x18\x02 \x01(\x05"\x8c\x01\n\x08LinkPage\x12=\n\x04type\x18\x01 \x01(\x0e\x32/.pro.omni.oms.api.common.base.LinkPage.LinkType\x12\x0c\n\x04link\x18\x02 \x01(\t"3\n\x08LinkType\x12\x08\n\x04NEXT\x10\x00\x12\x08\n\x04PREV\x10\x01\x12\x08\n\x04LAST\x10\x02\x12\t\n\x05\x46IRST\x10\x03"\x82\x01\n\x08MetaData\x12\r\n\x05total\x18\x01 \x01(\x05\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12\r\n\x05limit\x18\x03 \x01(\x05\x12\r\n\x05\x63ount\x18\x04 \x01(\x05\x12\x39\n\tlink_page\x18\x05 \x03(\x0b\x32&.pro.omni.oms.api.common.base.LinkPage"_\n\x10ResponseStandard\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x13\n\x0bstatus_code\x18\x03 \x01(\x05\x12\x14\n\x0cmessage_code\x18\x04 \x01(\t"\xd9\x01\n\x0bObjectAudit\x12\x12\n\ncreated_by\x18\x01 \x01(\t\x12\x12\n\nupdated_by\x18\x02 \x01(\t\x12\x12\n\ndeleted_by\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ndeleted_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp"P\n\x07\x43ontext\x12\x0e\n\x06tenant\x18\x01 \x01(\t\x12\x0c\n\x04user\x18\x02 \x01(\t\x12\'\n\x06locale\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct"*\n\x0eObjectResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\tb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "common.base_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _globals["_OBJECT"]._serialized_start = 114
    _globals["_OBJECT"]._serialized_end = 155
    _globals["_GROUPBY"]._serialized_start = 157
    _globals["_GROUPBY"]._serialized_end = 186
    _globals["_SORTBY"]._serialized_start = 188
    _globals["_SORTBY"]._serialized_end = 308
    _globals["_SORTBY_SORTTYPE"]._serialized_start = 279
    _globals["_SORTBY_SORTTYPE"]._serialized_end = 308
    _globals["_FIELDS"]._serialized_start = 310
    _globals["_FIELDS"]._serialized_end = 338
    _globals["_FILTER"]._serialized_start = 340
    _globals["_FILTER"]._serialized_end = 364
    _globals["_PAGINATED"]._serialized_start = 366
    _globals["_PAGINATED"]._serialized_end = 408
    _globals["_LINKPAGE"]._serialized_start = 411
    _globals["_LINKPAGE"]._serialized_end = 551
    _globals["_LINKPAGE_LINKTYPE"]._serialized_start = 500
    _globals["_LINKPAGE_LINKTYPE"]._serialized_end = 551
    _globals["_METADATA"]._serialized_start = 554
    _globals["_METADATA"]._serialized_end = 684
    _globals["_RESPONSESTANDARD"]._serialized_start = 686
    _globals["_RESPONSESTANDARD"]._serialized_end = 781
    _globals["_OBJECTAUDIT"]._serialized_start = 784
    _globals["_OBJECTAUDIT"]._serialized_end = 1001
    _globals["_CONTEXT"]._serialized_start = 1003
    _globals["_CONTEXT"]._serialized_end = 1083
    _globals["_OBJECTRESPONSE"]._serialized_start = 1085
    _globals["_OBJECTRESPONSE"]._serialized_end = 1127
# @@protoc_insertion_point(module_scope)
