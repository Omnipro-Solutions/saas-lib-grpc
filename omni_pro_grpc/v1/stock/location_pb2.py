# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/stock/location.proto
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
    b'\n\x17v1/stock/location.proto\x12"pro.omni.oms.api.v1.stock.location\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xdb\x02\n\x08Location\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12<\n\x06parent\x18\x03 \x01(\x0b\x32,.pro.omni.oms.api.common.base.ObjectResponse\x12\x0c\n\x04\x63ode\x18\x04 \x01(\t\x12\x15\n\rtype_location\x18\x05 \x01(\t\x12\x0f\n\x07\x62\x61rcode\x18\x06 \x01(\t\x12?\n\twarehouse\x18\x07 \x01(\x0b\x32,.pro.omni.oms.api.common.base.ObjectResponse\x12*\n\x06\x61\x63tive\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x13\n\x0b\x65xternal_id\x18\t \x01(\t\x12?\n\x0cobject_audit\x18\n \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xd1\x01\n\x15LocationCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tparent_id\x18\x02 \x01(\x05\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x15\n\rtype_location\x18\x04 \x01(\t\x12\x0f\n\x07\x62\x61rcode\x18\x05 \x01(\t\x12\x14\n\x0cwarehouse_id\x18\x06 \x01(\x05\x12\x13\n\x0b\x65xternal_id\x18\x07 \x01(\t\x12\x36\n\x07\x63ontext\x18\x08 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xa3\x01\n\x16LocationCreateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12>\n\x08location\x18\x02 \x01(\x0b\x32,.pro.omni.oms.api.v1.stock.location.Location"\xf1\x02\n\x13LocationReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xdd\x01\n\x14LocationReadResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12?\n\tlocations\x18\x03 \x03(\x0b\x32,.pro.omni.oms.api.v1.stock.location.Location"\x8f\x01\n\x15LocationUpdateRequest\x12>\n\x08location\x18\x01 \x01(\x0b\x32,.pro.omni.oms.api.v1.stock.location.Location\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xa3\x01\n\x16LocationUpdateResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12>\n\x08location\x18\x02 \x01(\x0b\x32,.pro.omni.oms.api.v1.stock.location.Location"[\n\x15LocationDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"c\n\x16LocationDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xaf\x05\n\x0fLocationService\x12\xa6\x01\n\x0eLocationCreate\x12\x39.pro.omni.oms.api.v1.stock.location.LocationCreateRequest\x1a:.pro.omni.oms.api.v1.stock.location.LocationCreateResponse"\x1d\x9a\xb5\x18\x19\x08\x02\x12\x15\x61pi/v1/stock/location\x12\xa0\x01\n\x0cLocationRead\x12\x37.pro.omni.oms.api.v1.stock.location.LocationReadRequest\x1a\x38.pro.omni.oms.api.v1.stock.location.LocationReadResponse"\x1d\x9a\xb5\x18\x19\x08\x01\x12\x15\x61pi/v1/stock/location\x12\xa6\x01\n\x0eLocationUpdate\x12\x39.pro.omni.oms.api.v1.stock.location.LocationUpdateRequest\x1a:.pro.omni.oms.api.v1.stock.location.LocationUpdateResponse"\x1d\x9a\xb5\x18\x19\x08\x03\x12\x15\x61pi/v1/stock/location\x12\xa6\x01\n\x0eLocationDelete\x12\x39.pro.omni.oms.api.v1.stock.location.LocationDeleteRequest\x1a:.pro.omni.oms.api.v1.stock.location.LocationDeleteResponse"\x1d\x9a\xb5\x18\x19\x08\x04\x12\x15\x61pi/v1/stock/locationb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.stock.location_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _LOCATIONSERVICE.methods_by_name["LocationCreate"]._options = None
    _LOCATIONSERVICE.methods_by_name["LocationCreate"]._serialized_options = (
        b"\232\265\030\031\010\002\022\025api/v1/stock/location"
    )
    _LOCATIONSERVICE.methods_by_name["LocationRead"]._options = None
    _LOCATIONSERVICE.methods_by_name["LocationRead"]._serialized_options = (
        b"\232\265\030\031\010\001\022\025api/v1/stock/location"
    )
    _LOCATIONSERVICE.methods_by_name["LocationUpdate"]._options = None
    _LOCATIONSERVICE.methods_by_name["LocationUpdate"]._serialized_options = (
        b"\232\265\030\031\010\003\022\025api/v1/stock/location"
    )
    _LOCATIONSERVICE.methods_by_name["LocationDelete"]._options = None
    _LOCATIONSERVICE.methods_by_name["LocationDelete"]._serialized_options = (
        b"\232\265\030\031\010\004\022\025api/v1/stock/location"
    )
    _globals["_LOCATION"]._serialized_start = 115
    _globals["_LOCATION"]._serialized_end = 462
    _globals["_LOCATIONCREATEREQUEST"]._serialized_start = 465
    _globals["_LOCATIONCREATEREQUEST"]._serialized_end = 674
    _globals["_LOCATIONCREATERESPONSE"]._serialized_start = 677
    _globals["_LOCATIONCREATERESPONSE"]._serialized_end = 840
    _globals["_LOCATIONREADREQUEST"]._serialized_start = 843
    _globals["_LOCATIONREADREQUEST"]._serialized_end = 1212
    _globals["_LOCATIONREADRESPONSE"]._serialized_start = 1215
    _globals["_LOCATIONREADRESPONSE"]._serialized_end = 1436
    _globals["_LOCATIONUPDATEREQUEST"]._serialized_start = 1439
    _globals["_LOCATIONUPDATEREQUEST"]._serialized_end = 1582
    _globals["_LOCATIONUPDATERESPONSE"]._serialized_start = 1585
    _globals["_LOCATIONUPDATERESPONSE"]._serialized_end = 1748
    _globals["_LOCATIONDELETEREQUEST"]._serialized_start = 1750
    _globals["_LOCATIONDELETEREQUEST"]._serialized_end = 1841
    _globals["_LOCATIONDELETERESPONSE"]._serialized_start = 1843
    _globals["_LOCATIONDELETERESPONSE"]._serialized_end = 1942
    _globals["_LOCATIONSERVICE"]._serialized_start = 1945
    _globals["_LOCATIONSERVICE"]._serialized_end = 2632
# @@protoc_insertion_point(module_scope)
