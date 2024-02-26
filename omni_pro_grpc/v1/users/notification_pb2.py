# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/users/notification.proto
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
from omni_pro_grpc.v1.users import user_pb2 as v1_dot_users_dot_user__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1bv1/users/notification.proto\x12&pro.omni.oms.api.v1.users.notification\x1a\x13v1/users/user.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xbd\x02\n\x0cNotification\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x32\n\x04user\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.v1.users.user.User\x12\x0c\n\x04type\x18\x04 \x01(\t\x12(\n\x04show\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12*\n\x06\x61\x63tive\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12%\n\x04\x64\x61ta\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x13\n\x0b\x65xternal_id\x18\x08 \x01(\t\x12?\n\x0cobject_audit\x18\t \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\x92\x02\n\x19NotificationCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12(\n\x04show\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12*\n\x06\x61\x63tive\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12%\n\x04\x64\x61ta\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x13\n\x0b\x65xternal_id\x18\x07 \x01(\t\x12\x36\n\x07\x63ontext\x18\x08 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xb3\x01\n\x1aNotificationCreateResponse\x12J\n\x0cnotification\x18\x01 \x01(\x0b\x32\x34.pro.omni.oms.api.v1.users.notification.Notification\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xf5\x02\n\x17NotificationReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\t\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xed\x01\n\x18NotificationReadResponse\x12K\n\rnotifications\x18\x01 \x03(\x0b\x32\x34.pro.omni.oms.api.v1.users.notification.Notification\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12I\n\x11response_standard\x18\x03 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\x9f\x01\n\x19NotificationUpdateRequest\x12J\n\x0cnotification\x18\x01 \x01(\x0b\x32\x34.pro.omni.oms.api.v1.users.notification.Notification\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xb3\x01\n\x1aNotificationUpdateResponse\x12J\n\x0cnotification\x18\x01 \x01(\x0b\x32\x34.pro.omni.oms.api.v1.users.notification.Notification\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"_\n\x19NotificationDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"g\n\x1aNotificationDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"a\n\rHiddenRequest\x12\x18\n\x10notification_ids\x18\x01 \x03(\t\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"[\n\x0eHiddenResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\x8a\x06\n\x13NotificationService\x12\x9d\x01\n\x12NotificationCreate\x12\x41.pro.omni.oms.api.v1.users.notification.NotificationCreateRequest\x1a\x42.pro.omni.oms.api.v1.users.notification.NotificationCreateResponse"\x00\x12\x97\x01\n\x10NotificationRead\x12?.pro.omni.oms.api.v1.users.notification.NotificationReadRequest\x1a@.pro.omni.oms.api.v1.users.notification.NotificationReadResponse"\x00\x12\x9d\x01\n\x12NotificationUpdate\x12\x41.pro.omni.oms.api.v1.users.notification.NotificationUpdateRequest\x1a\x42.pro.omni.oms.api.v1.users.notification.NotificationUpdateResponse"\x00\x12\x9d\x01\n\x12NotificationDelete\x12\x41.pro.omni.oms.api.v1.users.notification.NotificationDeleteRequest\x1a\x42.pro.omni.oms.api.v1.users.notification.NotificationDeleteResponse"\x00\x12y\n\x06Hidden\x12\x35.pro.omni.oms.api.v1.users.notification.HiddenRequest\x1a\x36.pro.omni.oms.api.v1.users.notification.HiddenResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.users.notification_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _globals["_NOTIFICATION"]._serialized_start = 174
    _globals["_NOTIFICATION"]._serialized_end = 491
    _globals["_NOTIFICATIONCREATEREQUEST"]._serialized_start = 494
    _globals["_NOTIFICATIONCREATEREQUEST"]._serialized_end = 768
    _globals["_NOTIFICATIONCREATERESPONSE"]._serialized_start = 771
    _globals["_NOTIFICATIONCREATERESPONSE"]._serialized_end = 950
    _globals["_NOTIFICATIONREADREQUEST"]._serialized_start = 953
    _globals["_NOTIFICATIONREADREQUEST"]._serialized_end = 1326
    _globals["_NOTIFICATIONREADRESPONSE"]._serialized_start = 1329
    _globals["_NOTIFICATIONREADRESPONSE"]._serialized_end = 1566
    _globals["_NOTIFICATIONUPDATEREQUEST"]._serialized_start = 1569
    _globals["_NOTIFICATIONUPDATEREQUEST"]._serialized_end = 1728
    _globals["_NOTIFICATIONUPDATERESPONSE"]._serialized_start = 1731
    _globals["_NOTIFICATIONUPDATERESPONSE"]._serialized_end = 1910
    _globals["_NOTIFICATIONDELETEREQUEST"]._serialized_start = 1912
    _globals["_NOTIFICATIONDELETEREQUEST"]._serialized_end = 2007
    _globals["_NOTIFICATIONDELETERESPONSE"]._serialized_start = 2009
    _globals["_NOTIFICATIONDELETERESPONSE"]._serialized_end = 2112
    _globals["_HIDDENREQUEST"]._serialized_start = 2114
    _globals["_HIDDENREQUEST"]._serialized_end = 2211
    _globals["_HIDDENRESPONSE"]._serialized_start = 2213
    _globals["_HIDDENRESPONSE"]._serialized_end = 2304
    _globals["_NOTIFICATIONSERVICE"]._serialized_start = 2307
    _globals["_NOTIFICATIONSERVICE"]._serialized_end = 3085
# @@protoc_insertion_point(module_scope)
