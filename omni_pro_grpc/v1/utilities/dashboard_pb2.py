# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/utilities/dashboard.proto
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

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1cv1/utilities/dashboard.proto\x12\'pro.omni.oms.api.v1.utilities.dashboard\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/protobuf/struct.proto"\xfa\x01\n\tDashboard\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12.\n\rlayout_config\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12*\n\x06\x61\x63tive\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x07 \x01(\t\x12?\n\x0cobject_audit\x18\x08 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xf2\x01\n\x16\x44\x61shboardCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12.\n\rlayout_config\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12*\n\x06\x61\x63tive\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x06 \x01(\t\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xab\x01\n\x17\x44\x61shboardCreateResponse\x12\x45\n\tdashboard\x18\x01 \x01(\x0b\x32\x32.pro.omni.oms.api.v1.utilities.dashboard.Dashboard\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xf2\x02\n\x14\x44\x61shboardReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\t\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xe5\x01\n\x15\x44\x61shboardReadResponse\x12\x46\n\ndashboards\x18\x01 \x03(\x0b\x32\x32.pro.omni.oms.api.v1.utilities.dashboard.Dashboard\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12I\n\x11response_standard\x18\x03 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\x97\x01\n\x16\x44\x61shboardUpdateRequest\x12\x45\n\tdashboard\x18\x01 \x01(\x0b\x32\x32.pro.omni.oms.api.v1.utilities.dashboard.Dashboard\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xab\x01\n\x17\x44\x61shboardUpdateResponse\x12\x45\n\tdashboard\x18\x01 \x01(\x0b\x32\x32.pro.omni.oms.api.v1.utilities.dashboard.Dashboard\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\\\n\x16\x44\x61shboardDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"d\n\x17\x44\x61shboardDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xf0\x04\n\x10\x44\x61shboardService\x12\x96\x01\n\x0f\x44\x61shboardCreate\x12?.pro.omni.oms.api.v1.utilities.dashboard.DashboardCreateRequest\x1a@.pro.omni.oms.api.v1.utilities.dashboard.DashboardCreateResponse"\x00\x12\x90\x01\n\rDashboardRead\x12=.pro.omni.oms.api.v1.utilities.dashboard.DashboardReadRequest\x1a>.pro.omni.oms.api.v1.utilities.dashboard.DashboardReadResponse"\x00\x12\x96\x01\n\x0f\x44\x61shboardUpdate\x12?.pro.omni.oms.api.v1.utilities.dashboard.DashboardUpdateRequest\x1a@.pro.omni.oms.api.v1.utilities.dashboard.DashboardUpdateResponse"\x00\x12\x96\x01\n\x0f\x44\x61shboardDelete\x12?.pro.omni.oms.api.v1.utilities.dashboard.DashboardDeleteRequest\x1a@.pro.omni.oms.api.v1.utilities.dashboard.DashboardDeleteResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.utilities.dashboard_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _globals["_DASHBOARD"]._serialized_start = 155
    _globals["_DASHBOARD"]._serialized_end = 405
    _globals["_DASHBOARDCREATEREQUEST"]._serialized_start = 408
    _globals["_DASHBOARDCREATEREQUEST"]._serialized_end = 650
    _globals["_DASHBOARDCREATERESPONSE"]._serialized_start = 653
    _globals["_DASHBOARDCREATERESPONSE"]._serialized_end = 824
    _globals["_DASHBOARDREADREQUEST"]._serialized_start = 827
    _globals["_DASHBOARDREADREQUEST"]._serialized_end = 1197
    _globals["_DASHBOARDREADRESPONSE"]._serialized_start = 1200
    _globals["_DASHBOARDREADRESPONSE"]._serialized_end = 1429
    _globals["_DASHBOARDUPDATEREQUEST"]._serialized_start = 1432
    _globals["_DASHBOARDUPDATEREQUEST"]._serialized_end = 1583
    _globals["_DASHBOARDUPDATERESPONSE"]._serialized_start = 1586
    _globals["_DASHBOARDUPDATERESPONSE"]._serialized_end = 1757
    _globals["_DASHBOARDDELETEREQUEST"]._serialized_start = 1759
    _globals["_DASHBOARDDELETEREQUEST"]._serialized_end = 1851
    _globals["_DASHBOARDDELETERESPONSE"]._serialized_start = 1853
    _globals["_DASHBOARDDELETERESPONSE"]._serialized_end = 1953
    _globals["_DASHBOARDSERVICE"]._serialized_start = 1956
    _globals["_DASHBOARDSERVICE"]._serialized_end = 2580
# @@protoc_insertion_point(module_scope)
