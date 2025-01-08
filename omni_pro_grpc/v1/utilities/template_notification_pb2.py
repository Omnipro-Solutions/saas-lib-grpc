# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/utilities/template_notification.proto
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
from omni_pro_grpc.v1.utilities import model_pb2 as v1_dot_utilities_dot_model__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n(v1/utilities/template_notification.proto\x12\x33pro.omni.oms.api.v1.utilities.template_notification\x1a\x11\x63ommon/base.proto\x1a\x18v1/utilities/model.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xc7\x03\n\x14TemplateNotification\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x0b\n\x03raw\x18\x05 \x01(\t\x12\x0e\n\x06render\x18\x06 \x01(\t\x12\x39\n\x05model\x18\x07 \x01(\x0b\x32*.pro.omni.oms.api.v1.utilities.model.Model\x12*\n\x06\x61\x63tive\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\t \x01(\t\x12\x0f\n\x07subject\x18\n \x01(\t\x12\x13\n\x0b\x66rom_sender\x18\x0b \x01(\t\x12\x10\n\x08\x65mail_to\x18\x0c \x03(\t\x12\x16\n\x0emodel_email_to\x18\r \x01(\t\x12\x10\n\x08\x65mail_cc\x18\x0e \x03(\t\x12\x11\n\tnumber_to\x18\x0f \x03(\t\x12\x17\n\x0fmodel_number_to\x18\x10 \x01(\t\x12\x11\n\tnumber_cc\x18\x11 \x03(\t\x12?\n\x0cobject_audit\x18\x12 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\x96\x03\n!TemplateNotificationCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0b\n\x03raw\x18\x04 \x01(\t\x12\x0e\n\x06render\x18\x05 \x01(\t\x12\x10\n\x08model_id\x18\x06 \x01(\t\x12*\n\x06\x61\x63tive\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\x08 \x01(\t\x12\x0f\n\x07subject\x18\t \x01(\t\x12\x13\n\x0b\x66rom_sender\x18\n \x01(\t\x12\x10\n\x08\x65mail_to\x18\x0b \x03(\t\x12\x16\n\x0emodel_email_to\x18\x0c \x01(\t\x12\x10\n\x08\x65mail_cc\x18\r \x03(\t\x12\x11\n\tnumber_to\x18\x0e \x03(\t\x12\x17\n\x0fmodel_number_to\x18\x0f \x01(\t\x12\x11\n\tnumber_cc\x18\x10 \x03(\t\x12\x36\n\x07\x63ontext\x18\x11 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xd9\x01\n"TemplateNotificationCreateResponse\x12h\n\x15template_notification\x18\x01 \x01(\x0b\x32I.pro.omni.oms.api.v1.utilities.template_notification.TemplateNotification\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xfd\x02\n\x1fTemplateNotificationReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\t\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x93\x02\n TemplateNotificationReadResponse\x12i\n\x16template_notifications\x18\x01 \x03(\x0b\x32I.pro.omni.oms.api.v1.utilities.template_notification.TemplateNotification\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12I\n\x11response_standard\x18\x03 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xc5\x01\n!TemplateNotificationUpdateRequest\x12h\n\x15template_notification\x18\x01 \x01(\x0b\x32I.pro.omni.oms.api.v1.utilities.template_notification.TemplateNotification\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xd9\x01\n"TemplateNotificationUpdateResponse\x12h\n\x15template_notification\x18\x01 \x01(\x0b\x32I.pro.omni.oms.api.v1.utilities.template_notification.TemplateNotification\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"g\n!TemplateNotificationDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"o\n"TemplateNotificationDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"z\n!TemplateNotificationRenderRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tmodel_ids\x18\x02 \x03(\t\x12\x36\n\x07\x63ontext\x18\x03 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x98\x01\n"TemplateNotificationRenderResponse\x12\'\n\x06render\x18\x01 \x03(\x0b\x32\x17.google.protobuf.Struct\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xed\t\n\x1bTemplateNotificationService\x12\xfd\x01\n\x1aTemplateNotificationCreate\x12V.pro.omni.oms.api.v1.utilities.template_notification.TemplateNotificationCreateRequest\x1aW.pro.omni.oms.api.v1.utilities.template_notification.TemplateNotificationCreateResponse".\x9a\xb5\x18*\x08\x02\x12&api/v1/utilities/template_notification\x12\xf7\x01\n\x18TemplateNotificationRead\x12T.pro.omni.oms.api.v1.utilities.template_notification.TemplateNotificationReadRequest\x1aU.pro.omni.oms.api.v1.utilities.template_notification.TemplateNotificationReadResponse".\x9a\xb5\x18*\x08\x01\x12&api/v1/utilities/template_notification\x12\xfd\x01\n\x1aTemplateNotificationUpdate\x12V.pro.omni.oms.api.v1.utilities.template_notification.TemplateNotificationUpdateRequest\x1aW.pro.omni.oms.api.v1.utilities.template_notification.TemplateNotificationUpdateResponse".\x9a\xb5\x18*\x08\x03\x12&api/v1/utilities/template_notification\x12\xfd\x01\n\x1aTemplateNotificationDelete\x12V.pro.omni.oms.api.v1.utilities.template_notification.TemplateNotificationDeleteRequest\x1aW.pro.omni.oms.api.v1.utilities.template_notification.TemplateNotificationDeleteResponse".\x9a\xb5\x18*\x08\x04\x12&api/v1/utilities/template_notification\x12\xd3\x01\n\x1aTemplateNotificationRender\x12V.pro.omni.oms.api.v1.utilities.template_notification.TemplateNotificationRenderRequest\x1aW.pro.omni.oms.api.v1.utilities.template_notification.TemplateNotificationRenderResponse"\x04\x90\xb5\x18\x01\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.utilities.template_notification_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _TEMPLATENOTIFICATIONSERVICE.methods_by_name["TemplateNotificationCreate"]._options = None
    _TEMPLATENOTIFICATIONSERVICE.methods_by_name["TemplateNotificationCreate"]._serialized_options = (
        b"\232\265\030*\010\002\022&api/v1/utilities/template_notification"
    )
    _TEMPLATENOTIFICATIONSERVICE.methods_by_name["TemplateNotificationRead"]._options = None
    _TEMPLATENOTIFICATIONSERVICE.methods_by_name["TemplateNotificationRead"]._serialized_options = (
        b"\232\265\030*\010\001\022&api/v1/utilities/template_notification"
    )
    _TEMPLATENOTIFICATIONSERVICE.methods_by_name["TemplateNotificationUpdate"]._options = None
    _TEMPLATENOTIFICATIONSERVICE.methods_by_name["TemplateNotificationUpdate"]._serialized_options = (
        b"\232\265\030*\010\003\022&api/v1/utilities/template_notification"
    )
    _TEMPLATENOTIFICATIONSERVICE.methods_by_name["TemplateNotificationDelete"]._options = None
    _TEMPLATENOTIFICATIONSERVICE.methods_by_name["TemplateNotificationDelete"]._serialized_options = (
        b"\232\265\030*\010\004\022&api/v1/utilities/template_notification"
    )
    _TEMPLATENOTIFICATIONSERVICE.methods_by_name["TemplateNotificationRender"]._options = None
    _TEMPLATENOTIFICATIONSERVICE.methods_by_name["TemplateNotificationRender"]._serialized_options = b"\220\265\030\001"
    _globals["_TEMPLATENOTIFICATION"]._serialized_start = 205
    _globals["_TEMPLATENOTIFICATION"]._serialized_end = 660
    _globals["_TEMPLATENOTIFICATIONCREATEREQUEST"]._serialized_start = 663
    _globals["_TEMPLATENOTIFICATIONCREATEREQUEST"]._serialized_end = 1069
    _globals["_TEMPLATENOTIFICATIONCREATERESPONSE"]._serialized_start = 1072
    _globals["_TEMPLATENOTIFICATIONCREATERESPONSE"]._serialized_end = 1289
    _globals["_TEMPLATENOTIFICATIONREADREQUEST"]._serialized_start = 1292
    _globals["_TEMPLATENOTIFICATIONREADREQUEST"]._serialized_end = 1673
    _globals["_TEMPLATENOTIFICATIONREADRESPONSE"]._serialized_start = 1676
    _globals["_TEMPLATENOTIFICATIONREADRESPONSE"]._serialized_end = 1951
    _globals["_TEMPLATENOTIFICATIONUPDATEREQUEST"]._serialized_start = 1954
    _globals["_TEMPLATENOTIFICATIONUPDATEREQUEST"]._serialized_end = 2151
    _globals["_TEMPLATENOTIFICATIONUPDATERESPONSE"]._serialized_start = 2154
    _globals["_TEMPLATENOTIFICATIONUPDATERESPONSE"]._serialized_end = 2371
    _globals["_TEMPLATENOTIFICATIONDELETEREQUEST"]._serialized_start = 2373
    _globals["_TEMPLATENOTIFICATIONDELETEREQUEST"]._serialized_end = 2476
    _globals["_TEMPLATENOTIFICATIONDELETERESPONSE"]._serialized_start = 2478
    _globals["_TEMPLATENOTIFICATIONDELETERESPONSE"]._serialized_end = 2589
    _globals["_TEMPLATENOTIFICATIONRENDERREQUEST"]._serialized_start = 2591
    _globals["_TEMPLATENOTIFICATIONRENDERREQUEST"]._serialized_end = 2713
    _globals["_TEMPLATENOTIFICATIONRENDERRESPONSE"]._serialized_start = 2716
    _globals["_TEMPLATENOTIFICATIONRENDERRESPONSE"]._serialized_end = 2868
    _globals["_TEMPLATENOTIFICATIONSERVICE"]._serialized_start = 2871
    _globals["_TEMPLATENOTIFICATIONSERVICE"]._serialized_end = 4132
# @@protoc_insertion_point(module_scope)
