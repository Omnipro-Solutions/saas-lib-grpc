# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/utilities/webhook.proto
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
from omni_pro_grpc.v1.utilities import event_pb2 as v1_dot_utilities_dot_event__pb2
from omni_pro_grpc.v1.utilities import method_grpc_pb2 as v1_dot_utilities_dot_method__grpc__pb2
from omni_pro_grpc.v1.utilities import template_notification_pb2 as v1_dot_utilities_dot_template__notification__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1av1/utilities/webhook.proto\x12%pro.omni.oms.api.v1.utilities.webhook\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x18v1/utilities/event.proto\x1a\x1ev1/utilities/method_grpc.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a(v1/utilities/template_notification.proto"\xbe\x05\n\x07Webhook\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12:\n\x06\x65vents\x18\x03 \x03(\x0b\x32*.pro.omni.oms.api.v1.utilities.event.Event\x12\x0b\n\x03url\x18\x04 \x01(\t\x12\x0e\n\x06method\x18\x05 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x06 \x01(\t\x12\x14\n\x0ctype_webhook\x18\x07 \x01(\t\x12\x10\n\x08protocol\x18\x08 \x01(\t\x12\x13\n\x0bpython_code\x18\t \x01(\t\x12\x16\n\x0etrigger_fields\x18\n \x03(\t\x12\x0e\n\x06\x64\x61g_id\x18\x0b \x01(\t\x12J\n\x0bmethod_grpc\x18\x0c \x01(\x0b\x32\x35.pro.omni.oms.api.v1.utilities.method_grpc.MethodGrpc\x12%\n\x04\x61uth\x18\r \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tauth_type\x18\x0e \x01(\t\x12(\n\x07headers\x18\x0f \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x13\n\x0bnotify_type\x18\x10 \x01(\t\x12/\n\x0epriority_level\x18\x11 \x01(\x0b\x32\x17.google.protobuf.Struct\x12h\n\x15template_notification\x18\x12 \x01(\x0b\x32I.pro.omni.oms.api.v1.utilities.template_notification.TemplateNotification\x12*\n\x06\x61\x63tive\x18\x13 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12?\n\x0cobject_audit\x18\x14 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xb9\x04\n\x14WebhookCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tevent_ids\x18\x02 \x03(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x0e\n\x06method\x18\x04 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x05 \x01(\t\x12\x14\n\x0ctype_webhook\x18\x06 \x01(\t\x12\x10\n\x08protocol\x18\x07 \x01(\t\x12\x13\n\x0bpython_code\x18\x08 \x01(\t\x12\x16\n\x0etrigger_fields\x18\t \x03(\t\x12\x0e\n\x06\x64\x61g_id\x18\n \x01(\t\x12\x16\n\x0emethod_grpc_id\x18\x0b \x01(\t\x12%\n\x04\x61uth\x18\x0c \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tauth_type\x18\r \x01(\t\x12(\n\x07headers\x18\x0e \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x13\n\x0bnotify_type\x18\x0f \x01(\t\x12 \n\x18template_notification_id\x18\x10 \x01(\t\x12\x16\n\x0epriority_level\x18\x11 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x12 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context\x12*\n\x06\x61\x63tive\x18\x13 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12?\n\x0cobject_audit\x18\x14 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xa3\x01\n\x15WebhookCreateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12?\n\x07webhook\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.v1.utilities.webhook.Webhook"\xf0\x02\n\x12WebhookReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\t\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xdd\x01\n\x13WebhookReadResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12@\n\x08webhooks\x18\x03 \x03(\x0b\x32..pro.omni.oms.api.v1.utilities.webhook.Webhook"\x8f\x01\n\x14WebhookUpdateRequest\x12?\n\x07webhook\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.v1.utilities.webhook.Webhook\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xa3\x01\n\x15WebhookUpdateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12?\n\x07webhook\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.v1.utilities.webhook.Webhook"Z\n\x14WebhookDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"b\n\x15WebhookDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xc6\x05\n\x0eWebhookService\x12\xac\x01\n\rWebhookCreate\x12;.pro.omni.oms.api.v1.utilities.webhook.WebhookCreateRequest\x1a<.pro.omni.oms.api.v1.utilities.webhook.WebhookCreateResponse" \x9a\xb5\x18\x1c\x08\x02\x12\x18\x61pi/v1/utilities/webhook\x12\xa6\x01\n\x0bWebhookRead\x12\x39.pro.omni.oms.api.v1.utilities.webhook.WebhookReadRequest\x1a:.pro.omni.oms.api.v1.utilities.webhook.WebhookReadResponse" \x9a\xb5\x18\x1c\x08\x01\x12\x18\x61pi/v1/utilities/webhook\x12\xac\x01\n\rWebhookUpdate\x12;.pro.omni.oms.api.v1.utilities.webhook.WebhookUpdateRequest\x1a<.pro.omni.oms.api.v1.utilities.webhook.WebhookUpdateResponse" \x9a\xb5\x18\x1c\x08\x03\x12\x18\x61pi/v1/utilities/webhook\x12\xac\x01\n\rWebhookDelete\x12;.pro.omni.oms.api.v1.utilities.webhook.WebhookDeleteRequest\x1a<.pro.omni.oms.api.v1.utilities.webhook.WebhookDeleteResponse" \x9a\xb5\x18\x1c\x08\x04\x12\x18\x61pi/v1/utilities/webhookb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.utilities.webhook_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _WEBHOOKSERVICE.methods_by_name["WebhookCreate"]._options = None
    _WEBHOOKSERVICE.methods_by_name["WebhookCreate"]._serialized_options = (
        b"\232\265\030\034\010\002\022\030api/v1/utilities/webhook"
    )
    _WEBHOOKSERVICE.methods_by_name["WebhookRead"]._options = None
    _WEBHOOKSERVICE.methods_by_name["WebhookRead"]._serialized_options = (
        b"\232\265\030\034\010\001\022\030api/v1/utilities/webhook"
    )
    _WEBHOOKSERVICE.methods_by_name["WebhookUpdate"]._options = None
    _WEBHOOKSERVICE.methods_by_name["WebhookUpdate"]._serialized_options = (
        b"\232\265\030\034\010\003\022\030api/v1/utilities/webhook"
    )
    _WEBHOOKSERVICE.methods_by_name["WebhookDelete"]._options = None
    _WEBHOOKSERVICE.methods_by_name["WebhookDelete"]._serialized_options = (
        b"\232\265\030\034\010\004\022\030api/v1/utilities/webhook"
    )
    _globals["_WEBHOOK"]._serialized_start = 251
    _globals["_WEBHOOK"]._serialized_end = 953
    _globals["_WEBHOOKCREATEREQUEST"]._serialized_start = 956
    _globals["_WEBHOOKCREATEREQUEST"]._serialized_end = 1525
    _globals["_WEBHOOKCREATERESPONSE"]._serialized_start = 1528
    _globals["_WEBHOOKCREATERESPONSE"]._serialized_end = 1691
    _globals["_WEBHOOKREADREQUEST"]._serialized_start = 1694
    _globals["_WEBHOOKREADREQUEST"]._serialized_end = 2062
    _globals["_WEBHOOKREADRESPONSE"]._serialized_start = 2065
    _globals["_WEBHOOKREADRESPONSE"]._serialized_end = 2286
    _globals["_WEBHOOKUPDATEREQUEST"]._serialized_start = 2289
    _globals["_WEBHOOKUPDATEREQUEST"]._serialized_end = 2432
    _globals["_WEBHOOKUPDATERESPONSE"]._serialized_start = 2435
    _globals["_WEBHOOKUPDATERESPONSE"]._serialized_end = 2598
    _globals["_WEBHOOKDELETEREQUEST"]._serialized_start = 2600
    _globals["_WEBHOOKDELETEREQUEST"]._serialized_end = 2690
    _globals["_WEBHOOKDELETERESPONSE"]._serialized_start = 2692
    _globals["_WEBHOOKDELETERESPONSE"]._serialized_end = 2790
    _globals["_WEBHOOKSERVICE"]._serialized_start = 2793
    _globals["_WEBHOOKSERVICE"]._serialized_end = 3503
# @@protoc_insertion_point(module_scope)
