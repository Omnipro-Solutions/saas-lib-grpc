# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/utilities/action.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from omni_pro_grpc.common import base_pb2 as common_dot_base__pb2
from omni_pro_grpc.v1.utilities import method_grpc_pb2 as v1_dot_utilities_dot_method__grpc__pb2
from omni_pro_grpc.v1.utilities import model_pb2 as v1_dot_utilities_dot_model__pb2
from omni_pro_grpc.v1.utilities import ms_pb2 as v1_dot_utilities_dot_ms__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x19v1/utilities/action.proto\x12$pro.omni.oms.api.v1.utilities.action\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x18v1/utilities/model.proto\x1a\x15v1/utilities/ms.proto\x1a\x1ev1/utilities/method_grpc.proto\x1a\x1cgoogle/protobuf/struct.proto"\xcc\x03\n\x06\x41\x63tion\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x39\n\x05model\x18\x04 \x01(\x0b\x32*.pro.omni.oms.api.v1.utilities.model.Model\x12N\n\x0cmicroservice\x18\x05 \x01(\x0b\x32\x38.pro.omni.oms.api.v1.utilities.microservice.Microservice\x12\x0b\n\x03url\x18\x06 \x01(\t\x12\x0c\n\x04view\x18\x07 \x01(\t\x12\r\n\x05token\x18\x08 \x01(\t\x12*\n\x06\x61\x63tive\x18\t \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\n \x01(\t\x12\x17\n\x0f\x61pply_if_filter\x18\x0b \x01(\t\x12J\n\x0bgrpc_method\x18\x0c \x01(\x0b\x32\x35.pro.omni.oms.api.v1.utilities.method_grpc.MethodGrpc\x12?\n\x0cobject_audit\x18\r \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xb0\x02\n\x13\x41\x63tionCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x10\n\x08model_id\x18\x03 \x01(\t\x12\x17\n\x0fmicroservice_id\x18\x04 \x01(\t\x12\x0b\n\x03url\x18\x05 \x01(\t\x12\x0c\n\x04view\x18\x06 \x01(\t\x12\r\n\x05token\x18\x07 \x01(\t\x12\x17\n\x0f\x61pply_if_filter\x18\x08 \x01(\t\x12\x16\n\x0egrpc_method_id\x18\t \x01(\t\x12*\n\x06\x61\x63tive\x18\n \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x0b \x01(\t\x12\x36\n\x07\x63ontext\x18\x0c \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9f\x01\n\x14\x41\x63tionCreateResponse\x12<\n\x06\x61\x63tion\x18\x01 \x01(\x0b\x32,.pro.omni.oms.api.v1.utilities.action.Action\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xef\x02\n\x11\x41\x63tionReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\t\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xd9\x01\n\x12\x41\x63tionReadResponse\x12=\n\x07\x61\x63tions\x18\x01 \x03(\x0b\x32,.pro.omni.oms.api.v1.utilities.action.Action\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12I\n\x11response_standard\x18\x03 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\x8b\x01\n\x13\x41\x63tionUpdateRequest\x12<\n\x06\x61\x63tion\x18\x01 \x01(\x0b\x32,.pro.omni.oms.api.v1.utilities.action.Action\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9f\x01\n\x14\x41\x63tionUpdateResponse\x12<\n\x06\x61\x63tion\x18\x01 \x01(\x0b\x32,.pro.omni.oms.api.v1.utilities.action.Action\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"Y\n\x13\x41\x63tionDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"a\n\x14\x41\x63tionDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\x8a\x01\n\x11\x43\x61llActionRequest\x12\x11\n\taction_id\x18\x01 \x01(\t\x12*\n\tinstances\x18\x02 \x03(\x0b\x32\x17.google.protobuf.Struct\x12\x36\n\x07\x63ontext\x18\x03 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x8a\x01\n\x12\x43\x61llActionResponse\x12)\n\x08response\x18\x01 \x03(\x0b\x32\x17.google.protobuf.Struct\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xb5\x05\n\rActionService\x12\x87\x01\n\x0c\x41\x63tionCreate\x12\x39.pro.omni.oms.api.v1.utilities.action.ActionCreateRequest\x1a:.pro.omni.oms.api.v1.utilities.action.ActionCreateResponse"\x00\x12\x81\x01\n\nActionRead\x12\x37.pro.omni.oms.api.v1.utilities.action.ActionReadRequest\x1a\x38.pro.omni.oms.api.v1.utilities.action.ActionReadResponse"\x00\x12\x87\x01\n\x0c\x41\x63tionUpdate\x12\x39.pro.omni.oms.api.v1.utilities.action.ActionUpdateRequest\x1a:.pro.omni.oms.api.v1.utilities.action.ActionUpdateResponse"\x00\x12\x87\x01\n\x0c\x41\x63tionDelete\x12\x39.pro.omni.oms.api.v1.utilities.action.ActionDeleteRequest\x1a:.pro.omni.oms.api.v1.utilities.action.ActionDeleteResponse"\x00\x12\x81\x01\n\nCallAction\x12\x37.pro.omni.oms.api.v1.utilities.action.CallActionRequest\x1a\x38.pro.omni.oms.api.v1.utilities.action.CallActionResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.utilities.action_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _globals["_ACTION"]._serialized_start = 230
    _globals["_ACTION"]._serialized_end = 690
    _globals["_ACTIONCREATEREQUEST"]._serialized_start = 693
    _globals["_ACTIONCREATEREQUEST"]._serialized_end = 997
    _globals["_ACTIONCREATERESPONSE"]._serialized_start = 1000
    _globals["_ACTIONCREATERESPONSE"]._serialized_end = 1159
    _globals["_ACTIONREADREQUEST"]._serialized_start = 1162
    _globals["_ACTIONREADREQUEST"]._serialized_end = 1529
    _globals["_ACTIONREADRESPONSE"]._serialized_start = 1532
    _globals["_ACTIONREADRESPONSE"]._serialized_end = 1749
    _globals["_ACTIONUPDATEREQUEST"]._serialized_start = 1752
    _globals["_ACTIONUPDATEREQUEST"]._serialized_end = 1891
    _globals["_ACTIONUPDATERESPONSE"]._serialized_start = 1894
    _globals["_ACTIONUPDATERESPONSE"]._serialized_end = 2053
    _globals["_ACTIONDELETEREQUEST"]._serialized_start = 2055
    _globals["_ACTIONDELETEREQUEST"]._serialized_end = 2144
    _globals["_ACTIONDELETERESPONSE"]._serialized_start = 2146
    _globals["_ACTIONDELETERESPONSE"]._serialized_end = 2243
    _globals["_CALLACTIONREQUEST"]._serialized_start = 2246
    _globals["_CALLACTIONREQUEST"]._serialized_end = 2384
    _globals["_CALLACTIONRESPONSE"]._serialized_start = 2387
    _globals["_CALLACTIONRESPONSE"]._serialized_end = 2525
    _globals["_ACTIONSERVICE"]._serialized_start = 2528
    _globals["_ACTIONSERVICE"]._serialized_end = 3221
# @@protoc_insertion_point(module_scope)
