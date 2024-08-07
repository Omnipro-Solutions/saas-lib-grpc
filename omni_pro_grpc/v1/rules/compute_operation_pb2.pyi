from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from omni_pro_grpc.common import base_pb2 as _base_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ComputeMethodData(_message.Message):
    __slots__ = ["cart_details", "items", "shipping_details"]
    CART_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_DETAILS_FIELD_NUMBER: _ClassVar[int]
    cart_details: _struct_pb2.Struct
    items: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    shipping_details: _struct_pb2.Struct
    def __init__(
        self,
        cart_details: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        items: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ...,
        shipping_details: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
    ) -> None: ...

class ComputeMethodRequest(_message.Message):
    __slots__ = ["data", "version", "context"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[ComputeMethodData]
    version: int
    context: _base_pb2.Context
    def __init__(
        self,
        data: _Optional[_Iterable[_Union[ComputeMethodData, _Mapping]]] = ...,
        version: _Optional[int] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class ComputeMethodResponse(_message.Message):
    __slots__ = ["result", "response_standard"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    result: _struct_pb2.ListValue
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        result: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class ComputeMethodStockAvailableRequest(_message.Message):
    __slots__ = ["methods", "items", "context"]
    METHODS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    methods: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    items: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    context: _base_pb2.Context
    def __init__(
        self,
        methods: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ...,
        items: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class ComputeMethodStockAvailableResponse(_message.Message):
    __slots__ = ["result", "response_standard"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    result: _struct_pb2.ListValue
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        result: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class ComputeDeliveryCarrierData(_message.Message):
    __slots__ = [
        "address",
        "products",
        "warehouse_sql_id",
        "delivery_method_doc_id",
        "picking_sql_id",
        "internal_transfer",
    ]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_SQL_ID_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_METHOD_DOC_ID_FIELD_NUMBER: _ClassVar[int]
    PICKING_SQL_ID_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    address: _struct_pb2.Struct
    products: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    warehouse_sql_id: int
    delivery_method_doc_id: str
    picking_sql_id: int
    internal_transfer: _wrappers_pb2.BoolValue
    def __init__(
        self,
        address: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        products: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ...,
        warehouse_sql_id: _Optional[int] = ...,
        delivery_method_doc_id: _Optional[str] = ...,
        picking_sql_id: _Optional[int] = ...,
        internal_transfer: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
    ) -> None: ...

class ComputeDeliveryCarrierRequest(_message.Message):
    __slots__ = ["data", "context"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[ComputeDeliveryCarrierData]
    context: _base_pb2.Context
    def __init__(
        self,
        data: _Optional[_Iterable[_Union[ComputeDeliveryCarrierData, _Mapping]]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class ComputeDeliveryCarrierDataResponse(_message.Message):
    __slots__ = ["carrier_sql_id", "warehouse_sql_id", "picking_sql_id", "exceptions"]
    CARRIER_SQL_ID_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_SQL_ID_FIELD_NUMBER: _ClassVar[int]
    PICKING_SQL_ID_FIELD_NUMBER: _ClassVar[int]
    EXCEPTIONS_FIELD_NUMBER: _ClassVar[int]
    carrier_sql_id: int
    warehouse_sql_id: int
    picking_sql_id: int
    exceptions: str
    def __init__(
        self,
        carrier_sql_id: _Optional[int] = ...,
        warehouse_sql_id: _Optional[int] = ...,
        picking_sql_id: _Optional[int] = ...,
        exceptions: _Optional[str] = ...,
    ) -> None: ...

class ComputeDeliveryCarrierResponse(_message.Message):
    __slots__ = ["response", "response_standard"]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response: _containers.RepeatedCompositeFieldContainer[ComputeDeliveryCarrierDataResponse]
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response: _Optional[_Iterable[_Union[ComputeDeliveryCarrierDataResponse, _Mapping]]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...
