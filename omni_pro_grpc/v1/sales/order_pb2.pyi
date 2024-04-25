from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from omni_pro_grpc.common import base_pb2 as _base_pb2
from omni_pro_grpc.v1.sales import address_pb2 as _address_pb2
from omni_pro_grpc.v1.sales import carrier_pb2 as _carrier_pb2
from omni_pro_grpc.v1.sales import delivery_method_pb2 as _delivery_method_pb2
from omni_pro_grpc.v1.sales import flow_pb2 as _flow_pb2
from omni_pro_grpc.v1.sales import picking_pb2 as _picking_pb2
from omni_pro_grpc.v1.sales import sale_pb2 as _sale_pb2
from omni_pro_grpc.v1.sales import state_pb2 as _state_pb2
from omni_pro_grpc.v1.sales import warehouse_pb2 as _warehouse_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Order(_message.Message):
    __slots__ = [
        "id",
        "name",
        "sale",
        "ship_address",
        "delivery_method",
        "carriers",
        "tax_total",
        "discount_total",
        "subtotal",
        "total",
        "active",
        "external_id",
        "warehouse",
        "cid",
        "shipping_amount_subtotal",
        "shipping_amount_discount",
        "shipping_amount_tax",
        "shipping_amount_total",
        "shipping_amount_discount_description",
        "type_delivery",
        "confirmed",
        "state",
        "flow",
        "sale_stock_operation",
        "pickings",
        "object_audit",
        "order_lines",
        "date_delivery",
        "order_history",
        "substitution_applied",
        "delivery_hours",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SALE_FIELD_NUMBER: _ClassVar[int]
    SHIP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_METHOD_FIELD_NUMBER: _ClassVar[int]
    CARRIERS_FIELD_NUMBER: _ClassVar[int]
    TAX_TOTAL_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_TOTAL_FIELD_NUMBER: _ClassVar[int]
    SUBTOTAL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    CID_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_AMOUNT_SUBTOTAL_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_AMOUNT_DISCOUNT_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_AMOUNT_TAX_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_AMOUNT_TOTAL_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_AMOUNT_DISCOUNT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_DELIVERY_FIELD_NUMBER: _ClassVar[int]
    CONFIRMED_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    FLOW_FIELD_NUMBER: _ClassVar[int]
    SALE_STOCK_OPERATION_FIELD_NUMBER: _ClassVar[int]
    PICKINGS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    ORDER_LINES_FIELD_NUMBER: _ClassVar[int]
    DATE_DELIVERY_FIELD_NUMBER: _ClassVar[int]
    ORDER_HISTORY_FIELD_NUMBER: _ClassVar[int]
    SUBSTITUTION_APPLIED_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_HOURS_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    sale: _sale_pb2.Sale
    ship_address: _address_pb2.Address
    delivery_method: _delivery_method_pb2.DeliveryMethod
    carriers: _containers.RepeatedCompositeFieldContainer[_carrier_pb2.Carrier]
    tax_total: float
    discount_total: float
    subtotal: float
    total: float
    active: _wrappers_pb2.BoolValue
    external_id: str
    warehouse: _warehouse_pb2.Warehouse
    cid: str
    shipping_amount_subtotal: float
    shipping_amount_discount: float
    shipping_amount_tax: float
    shipping_amount_total: float
    shipping_amount_discount_description: str
    type_delivery: str
    confirmed: bool
    state: _state_pb2.State
    flow: _flow_pb2.Flow
    sale_stock_operation: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    pickings: _containers.RepeatedCompositeFieldContainer[_picking_pb2.Picking]
    object_audit: _base_pb2.ObjectAudit
    order_lines: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    date_delivery: _timestamp_pb2.Timestamp
    order_history: _containers.RepeatedCompositeFieldContainer[OrderHistory]
    substitution_applied: int
    delivery_hours: str
    def __init__(
        self,
        id: _Optional[int] = ...,
        name: _Optional[str] = ...,
        sale: _Optional[_Union[_sale_pb2.Sale, _Mapping]] = ...,
        ship_address: _Optional[_Union[_address_pb2.Address, _Mapping]] = ...,
        delivery_method: _Optional[_Union[_delivery_method_pb2.DeliveryMethod, _Mapping]] = ...,
        carriers: _Optional[_Iterable[_Union[_carrier_pb2.Carrier, _Mapping]]] = ...,
        tax_total: _Optional[float] = ...,
        discount_total: _Optional[float] = ...,
        subtotal: _Optional[float] = ...,
        total: _Optional[float] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        external_id: _Optional[str] = ...,
        warehouse: _Optional[_Union[_warehouse_pb2.Warehouse, _Mapping]] = ...,
        cid: _Optional[str] = ...,
        shipping_amount_subtotal: _Optional[float] = ...,
        shipping_amount_discount: _Optional[float] = ...,
        shipping_amount_tax: _Optional[float] = ...,
        shipping_amount_total: _Optional[float] = ...,
        shipping_amount_discount_description: _Optional[str] = ...,
        type_delivery: _Optional[str] = ...,
        confirmed: bool = ...,
        state: _Optional[_Union[_state_pb2.State, _Mapping]] = ...,
        flow: _Optional[_Union[_flow_pb2.Flow, _Mapping]] = ...,
        sale_stock_operation: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ...,
        pickings: _Optional[_Iterable[_Union[_picking_pb2.Picking, _Mapping]]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
        order_lines: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ...,
        date_delivery: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        order_history: _Optional[_Iterable[_Union[OrderHistory, _Mapping]]] = ...,
        substitution_applied: _Optional[int] = ...,
        delivery_hours: _Optional[str] = ...,
    ) -> None: ...

class OrderHistory(_message.Message):
    __slots__ = [
        "id",
        "flow_id",
        "flow_name",
        "order",
        "previous_state_id",
        "previous_state_name",
        "previous_state_type",
        "previous_state_description",
        "current_state_id",
        "current_state_name",
        "current_state_type",
        "current_state_description",
        "transition_id",
        "transition_type",
        "logic",
        "delivery_hours",
        "send_ecommerce",
        "substitution_applied",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    FLOW_ID_FIELD_NUMBER: _ClassVar[int]
    FLOW_NAME_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_STATE_ID_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_STATE_NAME_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_STATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_STATE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CURRENT_STATE_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_STATE_NAME_FIELD_NUMBER: _ClassVar[int]
    CURRENT_STATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_STATE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TRANSITION_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSITION_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOGIC_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_HOURS_FIELD_NUMBER: _ClassVar[int]
    SEND_ECOMMERCE_FIELD_NUMBER: _ClassVar[int]
    SUBSTITUTION_APPLIED_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: int
    flow_id: int
    flow_name: str
    order: Order
    previous_state_id: int
    previous_state_name: str
    previous_state_type: str
    previous_state_description: str
    current_state_id: int
    current_state_name: str
    current_state_type: str
    current_state_description: str
    transition_id: int
    transition_type: str
    logic: str
    delivery_hours: str
    send_ecommerce: _wrappers_pb2.BoolValue
    substitution_applied: int
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[int] = ...,
        flow_id: _Optional[int] = ...,
        flow_name: _Optional[str] = ...,
        order: _Optional[_Union[Order, _Mapping]] = ...,
        previous_state_id: _Optional[int] = ...,
        previous_state_name: _Optional[str] = ...,
        previous_state_type: _Optional[str] = ...,
        previous_state_description: _Optional[str] = ...,
        current_state_id: _Optional[int] = ...,
        current_state_name: _Optional[str] = ...,
        current_state_type: _Optional[str] = ...,
        current_state_description: _Optional[str] = ...,
        transition_id: _Optional[int] = ...,
        transition_type: _Optional[str] = ...,
        logic: _Optional[str] = ...,
        delivery_hours: _Optional[str] = ...,
        send_ecommerce: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        substitution_applied: _Optional[int] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class OrderCreateRequest(_message.Message):
    __slots__ = [
        "name",
        "sale_id",
        "ship_address_code",
        "delivery_method_id",
        "carrier_ids",
        "tax_total",
        "discount_total",
        "subtotal",
        "total",
        "external_id",
        "warehouse_id",
        "cid",
        "shipping_amount_subtotal",
        "shipping_amount_discount",
        "shipping_amount_tax",
        "shipping_amount_total",
        "shipping_amount_discount_description",
        "type_delivery",
        "state_id",
        "flow_id",
        "confirmed",
        "sale_stock_operation",
        "context",
        "date_delivery",
    ]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SALE_ID_FIELD_NUMBER: _ClassVar[int]
    SHIP_ADDRESS_CODE_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    CARRIER_IDS_FIELD_NUMBER: _ClassVar[int]
    TAX_TOTAL_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_TOTAL_FIELD_NUMBER: _ClassVar[int]
    SUBTOTAL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_ID_FIELD_NUMBER: _ClassVar[int]
    CID_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_AMOUNT_SUBTOTAL_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_AMOUNT_DISCOUNT_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_AMOUNT_TAX_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_AMOUNT_TOTAL_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_AMOUNT_DISCOUNT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_DELIVERY_FIELD_NUMBER: _ClassVar[int]
    STATE_ID_FIELD_NUMBER: _ClassVar[int]
    FLOW_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIRMED_FIELD_NUMBER: _ClassVar[int]
    SALE_STOCK_OPERATION_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DATE_DELIVERY_FIELD_NUMBER: _ClassVar[int]
    name: str
    sale_id: int
    ship_address_code: str
    delivery_method_id: int
    carrier_ids: _containers.RepeatedScalarFieldContainer[int]
    tax_total: float
    discount_total: float
    subtotal: float
    total: float
    external_id: str
    warehouse_id: int
    cid: str
    shipping_amount_subtotal: float
    shipping_amount_discount: float
    shipping_amount_tax: float
    shipping_amount_total: float
    shipping_amount_discount_description: str
    type_delivery: str
    state_id: int
    flow_id: int
    confirmed: bool
    sale_stock_operation: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    context: _base_pb2.Context
    date_delivery: _timestamp_pb2.Timestamp
    def __init__(
        self,
        name: _Optional[str] = ...,
        sale_id: _Optional[int] = ...,
        ship_address_code: _Optional[str] = ...,
        delivery_method_id: _Optional[int] = ...,
        carrier_ids: _Optional[_Iterable[int]] = ...,
        tax_total: _Optional[float] = ...,
        discount_total: _Optional[float] = ...,
        subtotal: _Optional[float] = ...,
        total: _Optional[float] = ...,
        external_id: _Optional[str] = ...,
        warehouse_id: _Optional[int] = ...,
        cid: _Optional[str] = ...,
        shipping_amount_subtotal: _Optional[float] = ...,
        shipping_amount_discount: _Optional[float] = ...,
        shipping_amount_tax: _Optional[float] = ...,
        shipping_amount_total: _Optional[float] = ...,
        shipping_amount_discount_description: _Optional[str] = ...,
        type_delivery: _Optional[str] = ...,
        state_id: _Optional[int] = ...,
        flow_id: _Optional[int] = ...,
        confirmed: bool = ...,
        sale_stock_operation: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
        date_delivery: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
    ) -> None: ...

class OrderCreateResponse(_message.Message):
    __slots__ = ["order", "response_standard"]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    order: Order
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        order: _Optional[_Union[Order, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class OrderReadRequest(_message.Message):
    __slots__ = ["group_by", "sort_by", "fields", "filter", "paginated", "id", "context"]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    group_by: _containers.RepeatedCompositeFieldContainer[_base_pb2.GroupBy]
    sort_by: _base_pb2.SortBy
    fields: _base_pb2.Fields
    filter: _base_pb2.Filter
    paginated: _base_pb2.Paginated
    id: int
    context: _base_pb2.Context
    def __init__(
        self,
        group_by: _Optional[_Iterable[_Union[_base_pb2.GroupBy, _Mapping]]] = ...,
        sort_by: _Optional[_Union[_base_pb2.SortBy, _Mapping]] = ...,
        fields: _Optional[_Union[_base_pb2.Fields, _Mapping]] = ...,
        filter: _Optional[_Union[_base_pb2.Filter, _Mapping]] = ...,
        paginated: _Optional[_Union[_base_pb2.Paginated, _Mapping]] = ...,
        id: _Optional[int] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class OrderReadResponse(_message.Message):
    __slots__ = ["orders", "response_standard", "meta_data"]
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    orders: _containers.RepeatedCompositeFieldContainer[Order]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    def __init__(
        self,
        orders: _Optional[_Iterable[_Union[Order, _Mapping]]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
    ) -> None: ...

class OrderUpdateRequest(_message.Message):
    __slots__ = ["order", "context"]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    order: Order
    context: _base_pb2.Context
    def __init__(
        self,
        order: _Optional[_Union[Order, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class OrderUpdateResponse(_message.Message):
    __slots__ = ["order", "response_standard"]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    order: Order
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        order: _Optional[_Union[Order, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class OrderDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: int
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class OrderDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class OrderConfirmRequest(_message.Message):
    __slots__ = ["payload", "context"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    payload: _struct_pb2.Struct
    context: _base_pb2.Context
    def __init__(
        self,
        payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class OrderConfirmResponse(_message.Message):
    __slots__ = ["confirm", "response_standard"]
    CONFIRM_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    confirm: _struct_pb2.Struct
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        confirm: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class SaleStockOperationRequest(_message.Message):
    __slots__ = ["payload", "context"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    payload: _struct_pb2.Struct
    context: _base_pb2.Context
    def __init__(
        self,
        payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class SaleStockOperationResponse(_message.Message):
    __slots__ = ["data", "response_standard"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        data: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class OrderChangeStateRequest(_message.Message):
    __slots__ = ["order_id", "context"]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    order_id: int
    context: _base_pb2.Context
    def __init__(
        self, order_id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class OrderChangeStateResponse(_message.Message):
    __slots__ = ["response_standard", "order"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    order: Order
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        order: _Optional[_Union[Order, _Mapping]] = ...,
    ) -> None: ...
