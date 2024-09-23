# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/clients/client.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from omni_pro_grpc.common import base_pb2 as common_dot_base__pb2
from omni_pro_grpc.v1.clients import address_pb2 as v1_dot_clients_dot_address__pb2
from omni_pro_grpc.v1.clients import type_document_pb2 as v1_dot_clients_dot_type__document__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x17v1/clients/client.proto\x12"pro.omni.oms.api.v1.clients.client\x1a\x11\x63ommon/base.proto\x1a\x18v1/clients/address.proto\x1a\x1ev1/clients/type_document.proto\x1a\x1cgoogle/protobuf/struct.proto"\x91\x04\n\x06\x43lient\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\nfirst_name\x18\x03 \x01(\t\x12\x11\n\tlast_name\x18\x04 \x01(\t\x12N\n\rdocument_type\x18\x05 \x01(\x0b\x32\x37.pro.omni.oms.api.v1.clients.type_document.TypeDocument\x12\x10\n\x08\x64ocument\x18\x06 \x01(\t\x12\x0e\n\x06mobile\x18\x07 \x01(\t\x12\r\n\x05phone\x18\x08 \x01(\t\x12\x14\n\x0cprefix_phone\x18\t \x01(\t\x12\x15\n\rprefix_mobile\x18\n \x01(\t\x12\r\n\x05\x65mail\x18\x0b \x01(\t\x12\x35\n\x07\x63ountry\x18\x0c \x01(\x0b\x32$.pro.omni.oms.api.common.base.Object\x12?\n\taddresses\x18\r \x03(\x0b\x32,.pro.omni.oms.api.v1.clients.address.Address\x12\x0e\n\x06\x61\x63tive\x18\x0e \x01(\x08\x12\x13\n\x0b\x65xternal_id\x18\x0f \x01(\t\x12+\n\nproperties\x18\x10 \x01(\x0b\x32\x17.google.protobuf.Struct\x12?\n\x0cobject_audit\x18\x11 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\x99\x03\n\x13\x43lientCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x18\n\x10\x64ocument_type_id\x18\x04 \x01(\t\x12\x10\n\x08\x64ocument\x18\x05 \x01(\t\x12\x0e\n\x06mobile\x18\x06 \x01(\t\x12\r\n\x05phone\x18\x07 \x01(\t\x12\x14\n\x0cprefix_phone\x18\x08 \x01(\t\x12\x15\n\rprefix_mobile\x18\t \x01(\t\x12\r\n\x05\x65mail\x18\n \x01(\t\x12\x15\n\raddresses_ids\x18\x0b \x03(\t\x12\x35\n\x07\x63ountry\x18\x0c \x01(\x0b\x32$.pro.omni.oms.api.common.base.Object\x12\x13\n\x0b\x65xternal_id\x18\r \x01(\t\x12+\n\nproperties\x18\x0e \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x36\n\x07\x63ontext\x18\x0f \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9d\x01\n\x14\x43lientCreateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12:\n\x06\x63lient\x18\x02 \x01(\x0b\x32*.pro.omni.oms.api.v1.clients.client.Client"\xef\x02\n\x11\x43lientReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\t\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xd7\x01\n\x12\x43lientReadResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12;\n\x07\x63lients\x18\x03 \x03(\x0b\x32*.pro.omni.oms.api.v1.clients.client.Client"\x89\x01\n\x13\x43lientUpdateRequest\x12:\n\x06\x63lient\x18\x01 \x01(\x0b\x32*.pro.omni.oms.api.v1.clients.client.Client\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9d\x01\n\x14\x43lientUpdateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12:\n\x06\x63lient\x18\x02 \x01(\x0b\x32*.pro.omni.oms.api.v1.clients.client.Client"Y\n\x13\x43lientDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"a\n\x14\x43lientDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xdd\x01\n\x17\x43lientSyncByHashRequest\x12%\n\x04info\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x31\n\x10shipping_address\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x30\n\x0f\x62illing_address\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x36\n\x07\x63ontext\x18\x04 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x93\x01\n\x18\x43lientSyncByHashResponse\x12,\n\x0b\x64\x61ta_client\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xb3\x05\n\x0e\x43lientsService\x12\x83\x01\n\x0c\x43lientCreate\x12\x37.pro.omni.oms.api.v1.clients.client.ClientCreateRequest\x1a\x38.pro.omni.oms.api.v1.clients.client.ClientCreateResponse"\x00\x12}\n\nClientRead\x12\x35.pro.omni.oms.api.v1.clients.client.ClientReadRequest\x1a\x36.pro.omni.oms.api.v1.clients.client.ClientReadResponse"\x00\x12\x83\x01\n\x0c\x43lientUpdate\x12\x37.pro.omni.oms.api.v1.clients.client.ClientUpdateRequest\x1a\x38.pro.omni.oms.api.v1.clients.client.ClientUpdateResponse"\x00\x12\x83\x01\n\x0c\x43lientDelete\x12\x37.pro.omni.oms.api.v1.clients.client.ClientDeleteRequest\x1a\x38.pro.omni.oms.api.v1.clients.client.ClientDeleteResponse"\x00\x12\x8f\x01\n\x10\x43lientSyncByHash\x12;.pro.omni.oms.api.v1.clients.client.ClientSyncByHashRequest\x1a<.pro.omni.oms.api.v1.clients.client.ClientSyncByHashResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.clients.client_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _globals["_CLIENT"]._serialized_start = 171
    _globals["_CLIENT"]._serialized_end = 700
    _globals["_CLIENTCREATEREQUEST"]._serialized_start = 703
    _globals["_CLIENTCREATEREQUEST"]._serialized_end = 1112
    _globals["_CLIENTCREATERESPONSE"]._serialized_start = 1115
    _globals["_CLIENTCREATERESPONSE"]._serialized_end = 1272
    _globals["_CLIENTREADREQUEST"]._serialized_start = 1275
    _globals["_CLIENTREADREQUEST"]._serialized_end = 1642
    _globals["_CLIENTREADRESPONSE"]._serialized_start = 1645
    _globals["_CLIENTREADRESPONSE"]._serialized_end = 1860
    _globals["_CLIENTUPDATEREQUEST"]._serialized_start = 1863
    _globals["_CLIENTUPDATEREQUEST"]._serialized_end = 2000
    _globals["_CLIENTUPDATERESPONSE"]._serialized_start = 2003
    _globals["_CLIENTUPDATERESPONSE"]._serialized_end = 2160
    _globals["_CLIENTDELETEREQUEST"]._serialized_start = 2162
    _globals["_CLIENTDELETEREQUEST"]._serialized_end = 2251
    _globals["_CLIENTDELETERESPONSE"]._serialized_start = 2253
    _globals["_CLIENTDELETERESPONSE"]._serialized_end = 2350
    _globals["_CLIENTSYNCBYHASHREQUEST"]._serialized_start = 2353
    _globals["_CLIENTSYNCBYHASHREQUEST"]._serialized_end = 2574
    _globals["_CLIENTSYNCBYHASHRESPONSE"]._serialized_start = 2577
    _globals["_CLIENTSYNCBYHASHRESPONSE"]._serialized_end = 2724
    _globals["_CLIENTSSERVICE"]._serialized_start = 2727
    _globals["_CLIENTSSERVICE"]._serialized_end = 3418
# @@protoc_insertion_point(module_scope)
