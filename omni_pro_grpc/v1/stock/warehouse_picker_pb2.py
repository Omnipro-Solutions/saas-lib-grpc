# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/stock/warehouse_picker.proto
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
    b'\n\x1fv1/stock/warehouse_picker.proto\x12*pro.omni.oms.api.v1.stock.warehouse_picker\x1a\x11\x63ommon/base.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1egoogle/protobuf/wrappers.proto"\x95\x02\n\x0fWarehousePicker\x12\n\n\x02id\x18\x01 \x01(\x05\x12*\n\twarehouse\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0c\n\x04pick\x18\x03 \x01(\x05\x12\x0c\n\x04pack\x18\x04 \x01(\x05\x12\x0b\n\x03out\x18\x05 \x01(\x05\x12\x10\n\x08returned\x18\x06 \x01(\x05\x12\x10\n\x08internal\x18\x07 \x01(\x05\x12\x10\n\x08incoming\x18\x08 \x01(\x05\x12*\n\x06\x61\x63tive\x18\t \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12?\n\x0cobject_audit\x18\n \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xf8\x02\n\x1aWarehousePickerReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xfb\x01\n\x1bWarehousePickerReadResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12V\n\x11warehouse_pickers\x18\x03 \x03(\x0b\x32;.pro.omni.oms.api.v1.stock.warehouse_picker.WarehousePicker2\xe8\x01\n\x16WarehousePickerService\x12\xcd\x01\n\x13WarehousePickerRead\x12\x46.pro.omni.oms.api.v1.stock.warehouse_picker.WarehousePickerReadRequest\x1aG.pro.omni.oms.api.v1.stock.warehouse_picker.WarehousePickerReadResponse"%\x9a\xb5\x18!\x08\x01\x12\x1d\x61pi/v1/stock/warehouse/pickerb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.stock.warehouse_picker_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _WAREHOUSEPICKERSERVICE.methods_by_name["WarehousePickerRead"]._options = None
    _WAREHOUSEPICKERSERVICE.methods_by_name["WarehousePickerRead"]._serialized_options = (
        b"\232\265\030!\010\001\022\035api/v1/stock/warehouse/picker"
    )
    _globals["_WAREHOUSEPICKER"]._serialized_start = 161
    _globals["_WAREHOUSEPICKER"]._serialized_end = 438
    _globals["_WAREHOUSEPICKERREADREQUEST"]._serialized_start = 441
    _globals["_WAREHOUSEPICKERREADREQUEST"]._serialized_end = 817
    _globals["_WAREHOUSEPICKERREADRESPONSE"]._serialized_start = 820
    _globals["_WAREHOUSEPICKERREADRESPONSE"]._serialized_end = 1071
    _globals["_WAREHOUSEPICKERSERVICE"]._serialized_start = 1074
    _globals["_WAREHOUSEPICKERSERVICE"]._serialized_end = 1306
# @@protoc_insertion_point(module_scope)
