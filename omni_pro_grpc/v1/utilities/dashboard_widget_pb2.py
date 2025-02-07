# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/utilities/dashboard_widget.proto
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
from omni_pro_grpc.v1.utilities import analytic_data_pb2 as v1_dot_utilities_dot_analytic__data__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n#v1/utilities/dashboard_widget.proto\x12.pro.omni.oms.api.v1.utilities.dashboard_widget\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a v1/utilities/analytic_data.proto"\x88\x03\n\x0f\x44\x61shboardWidget\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12P\n\ranalytic_data\x18\x04 \x01(\x0b\x32\x39.pro.omni.oms.api.v1.utilities.analytic_data.AnalyticData\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x0c\n\x04type\x18\x06 \x01(\t\x12)\n\x08settings\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\x12+\n\nproperties\x18\x08 \x01(\x0b\x32\x17.google.protobuf.Struct\x12*\n\x06\x61\x63tive\x18\t \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\n \x01(\t\x12?\n\x0cobject_audit\x18\x0b \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xc8\x02\n\x1c\x44\x61shboardWidgetCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x18\n\x10\x61nalytic_data_id\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x0c\n\x04type\x18\x05 \x01(\t\x12)\n\x08settings\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\x12+\n\nproperties\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\x12*\n\x06\x61\x63tive\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\t \x01(\t\x12\x36\n\x07\x63ontext\x18\n \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xc5\x01\n\x1d\x44\x61shboardWidgetCreateResponse\x12Y\n\x10\x64\x61shboard_widget\x18\x01 \x01(\x0b\x32?.pro.omni.oms.api.v1.utilities.dashboard_widget.DashboardWidget\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xf8\x02\n\x1a\x44\x61shboardWidgetReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\t\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xff\x01\n\x1b\x44\x61shboardWidgetReadResponse\x12Z\n\x11\x64\x61shboard_widgets\x18\x01 \x03(\x0b\x32?.pro.omni.oms.api.v1.utilities.dashboard_widget.DashboardWidget\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12I\n\x11response_standard\x18\x03 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xb1\x01\n\x1c\x44\x61shboardWidgetUpdateRequest\x12Y\n\x10\x64\x61shboard_widget\x18\x01 \x01(\x0b\x32?.pro.omni.oms.api.v1.utilities.dashboard_widget.DashboardWidget\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xc5\x01\n\x1d\x44\x61shboardWidgetUpdateResponse\x12Y\n\x10\x64\x61shboard_widget\x18\x01 \x01(\x0b\x32?.pro.omni.oms.api.v1.utilities.dashboard_widget.DashboardWidget\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"b\n\x1c\x44\x61shboardWidgetDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"j\n\x1d\x44\x61shboardWidgetDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\x9a\x07\n\x16\x44\x61shboardWidgetService\x12\xdf\x01\n\x15\x44\x61shboardWidgetCreate\x12L.pro.omni.oms.api.v1.utilities.dashboard_widget.DashboardWidgetCreateRequest\x1aM.pro.omni.oms.api.v1.utilities.dashboard_widget.DashboardWidgetCreateResponse")\x9a\xb5\x18%\x08\x02\x12!api/v1/utilities/dashboard/widget\x12\xd9\x01\n\x13\x44\x61shboardWidgetRead\x12J.pro.omni.oms.api.v1.utilities.dashboard_widget.DashboardWidgetReadRequest\x1aK.pro.omni.oms.api.v1.utilities.dashboard_widget.DashboardWidgetReadResponse")\x9a\xb5\x18%\x08\x01\x12!api/v1/utilities/dashboard/widget\x12\xdf\x01\n\x15\x44\x61shboardWidgetUpdate\x12L.pro.omni.oms.api.v1.utilities.dashboard_widget.DashboardWidgetUpdateRequest\x1aM.pro.omni.oms.api.v1.utilities.dashboard_widget.DashboardWidgetUpdateResponse")\x9a\xb5\x18%\x08\x03\x12!api/v1/utilities/dashboard/widget\x12\xdf\x01\n\x15\x44\x61shboardWidgetDelete\x12L.pro.omni.oms.api.v1.utilities.dashboard_widget.DashboardWidgetDeleteRequest\x1aM.pro.omni.oms.api.v1.utilities.dashboard_widget.DashboardWidgetDeleteResponse")\x9a\xb5\x18%\x08\x04\x12!api/v1/utilities/dashboard/widgetb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.utilities.dashboard_widget_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _DASHBOARDWIDGETSERVICE.methods_by_name["DashboardWidgetCreate"]._options = None
    _DASHBOARDWIDGETSERVICE.methods_by_name["DashboardWidgetCreate"]._serialized_options = (
        b"\232\265\030%\010\002\022!api/v1/utilities/dashboard/widget"
    )
    _DASHBOARDWIDGETSERVICE.methods_by_name["DashboardWidgetRead"]._options = None
    _DASHBOARDWIDGETSERVICE.methods_by_name["DashboardWidgetRead"]._serialized_options = (
        b"\232\265\030%\010\001\022!api/v1/utilities/dashboard/widget"
    )
    _DASHBOARDWIDGETSERVICE.methods_by_name["DashboardWidgetUpdate"]._options = None
    _DASHBOARDWIDGETSERVICE.methods_by_name["DashboardWidgetUpdate"]._serialized_options = (
        b"\232\265\030%\010\003\022!api/v1/utilities/dashboard/widget"
    )
    _DASHBOARDWIDGETSERVICE.methods_by_name["DashboardWidgetDelete"]._options = None
    _DASHBOARDWIDGETSERVICE.methods_by_name["DashboardWidgetDelete"]._serialized_options = (
        b"\232\265\030%\010\004\022!api/v1/utilities/dashboard/widget"
    )
    _globals["_DASHBOARDWIDGET"]._serialized_start = 203
    _globals["_DASHBOARDWIDGET"]._serialized_end = 595
    _globals["_DASHBOARDWIDGETCREATEREQUEST"]._serialized_start = 598
    _globals["_DASHBOARDWIDGETCREATEREQUEST"]._serialized_end = 926
    _globals["_DASHBOARDWIDGETCREATERESPONSE"]._serialized_start = 929
    _globals["_DASHBOARDWIDGETCREATERESPONSE"]._serialized_end = 1126
    _globals["_DASHBOARDWIDGETREADREQUEST"]._serialized_start = 1129
    _globals["_DASHBOARDWIDGETREADREQUEST"]._serialized_end = 1505
    _globals["_DASHBOARDWIDGETREADRESPONSE"]._serialized_start = 1508
    _globals["_DASHBOARDWIDGETREADRESPONSE"]._serialized_end = 1763
    _globals["_DASHBOARDWIDGETUPDATEREQUEST"]._serialized_start = 1766
    _globals["_DASHBOARDWIDGETUPDATEREQUEST"]._serialized_end = 1943
    _globals["_DASHBOARDWIDGETUPDATERESPONSE"]._serialized_start = 1946
    _globals["_DASHBOARDWIDGETUPDATERESPONSE"]._serialized_end = 2143
    _globals["_DASHBOARDWIDGETDELETEREQUEST"]._serialized_start = 2145
    _globals["_DASHBOARDWIDGETDELETEREQUEST"]._serialized_end = 2243
    _globals["_DASHBOARDWIDGETDELETERESPONSE"]._serialized_start = 2245
    _globals["_DASHBOARDWIDGETDELETERESPONSE"]._serialized_end = 2351
    _globals["_DASHBOARDWIDGETSERVICE"]._serialized_start = 2354
    _globals["_DASHBOARDWIDGETSERVICE"]._serialized_end = 3276
# @@protoc_insertion_point(module_scope)
