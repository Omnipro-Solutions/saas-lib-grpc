# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni_pro_grpc.v1.sales import order_pb2 as v1_dot_sales_dot_order__pb2


class OrderServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.OrderCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.order.OrderService/OrderCreate",
            request_serializer=v1_dot_sales_dot_order__pb2.OrderCreateRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_order__pb2.OrderCreateResponse.FromString,
        )
        self.OrderRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.order.OrderService/OrderRead",
            request_serializer=v1_dot_sales_dot_order__pb2.OrderReadRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_order__pb2.OrderReadResponse.FromString,
        )
        self.OrderUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.order.OrderService/OrderUpdate",
            request_serializer=v1_dot_sales_dot_order__pb2.OrderUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_order__pb2.OrderUpdateResponse.FromString,
        )
        self.OrderDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.order.OrderService/OrderDelete",
            request_serializer=v1_dot_sales_dot_order__pb2.OrderDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_order__pb2.OrderDeleteResponse.FromString,
        )
        self.OrderConfirm = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.order.OrderService/OrderConfirm",
            request_serializer=v1_dot_sales_dot_order__pb2.OrderConfirmRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_order__pb2.OrderConfirmResponse.FromString,
        )
        self.SaleStockOperation = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.order.OrderService/SaleStockOperation",
            request_serializer=v1_dot_sales_dot_order__pb2.SaleStockOperationRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_order__pb2.SaleStockOperationResponse.FromString,
        )
        self.OrderChangeState = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.order.OrderService/OrderChangeState",
            request_serializer=v1_dot_sales_dot_order__pb2.OrderChangeStateRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_order__pb2.OrderChangeStateResponse.FromString,
        )
        self.OrderLineDeliveryQuantity = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.order.OrderService/OrderLineDeliveryQuantity",
            request_serializer=v1_dot_sales_dot_order__pb2.OrderLineDeliveryQuantityRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_order__pb2.OrderLineDeliveryQuantityResponse.FromString,
        )
        self.ConfirmOrders = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.order.OrderService/ConfirmOrders",
            request_serializer=v1_dot_sales_dot_order__pb2.ConfirmOrdersRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_order__pb2.ConfirmOrdersResponse.FromString,
        )


class OrderServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def OrderCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def OrderRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def OrderUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def OrderDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def OrderConfirm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SaleStockOperation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def OrderChangeState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def OrderLineDeliveryQuantity(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ConfirmOrders(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_OrderServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "OrderCreate": grpc.unary_unary_rpc_method_handler(
            servicer.OrderCreate,
            request_deserializer=v1_dot_sales_dot_order__pb2.OrderCreateRequest.FromString,
            response_serializer=v1_dot_sales_dot_order__pb2.OrderCreateResponse.SerializeToString,
        ),
        "OrderRead": grpc.unary_unary_rpc_method_handler(
            servicer.OrderRead,
            request_deserializer=v1_dot_sales_dot_order__pb2.OrderReadRequest.FromString,
            response_serializer=v1_dot_sales_dot_order__pb2.OrderReadResponse.SerializeToString,
        ),
        "OrderUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.OrderUpdate,
            request_deserializer=v1_dot_sales_dot_order__pb2.OrderUpdateRequest.FromString,
            response_serializer=v1_dot_sales_dot_order__pb2.OrderUpdateResponse.SerializeToString,
        ),
        "OrderDelete": grpc.unary_unary_rpc_method_handler(
            servicer.OrderDelete,
            request_deserializer=v1_dot_sales_dot_order__pb2.OrderDeleteRequest.FromString,
            response_serializer=v1_dot_sales_dot_order__pb2.OrderDeleteResponse.SerializeToString,
        ),
        "OrderConfirm": grpc.unary_unary_rpc_method_handler(
            servicer.OrderConfirm,
            request_deserializer=v1_dot_sales_dot_order__pb2.OrderConfirmRequest.FromString,
            response_serializer=v1_dot_sales_dot_order__pb2.OrderConfirmResponse.SerializeToString,
        ),
        "SaleStockOperation": grpc.unary_unary_rpc_method_handler(
            servicer.SaleStockOperation,
            request_deserializer=v1_dot_sales_dot_order__pb2.SaleStockOperationRequest.FromString,
            response_serializer=v1_dot_sales_dot_order__pb2.SaleStockOperationResponse.SerializeToString,
        ),
        "OrderChangeState": grpc.unary_unary_rpc_method_handler(
            servicer.OrderChangeState,
            request_deserializer=v1_dot_sales_dot_order__pb2.OrderChangeStateRequest.FromString,
            response_serializer=v1_dot_sales_dot_order__pb2.OrderChangeStateResponse.SerializeToString,
        ),
        "OrderLineDeliveryQuantity": grpc.unary_unary_rpc_method_handler(
            servicer.OrderLineDeliveryQuantity,
            request_deserializer=v1_dot_sales_dot_order__pb2.OrderLineDeliveryQuantityRequest.FromString,
            response_serializer=v1_dot_sales_dot_order__pb2.OrderLineDeliveryQuantityResponse.SerializeToString,
        ),
        "ConfirmOrders": grpc.unary_unary_rpc_method_handler(
            servicer.ConfirmOrders,
            request_deserializer=v1_dot_sales_dot_order__pb2.ConfirmOrdersRequest.FromString,
            response_serializer=v1_dot_sales_dot_order__pb2.ConfirmOrdersResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.sales.order.OrderService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class OrderService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def OrderCreate(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/pro.omni.oms.api.v1.sales.order.OrderService/OrderCreate",
            v1_dot_sales_dot_order__pb2.OrderCreateRequest.SerializeToString,
            v1_dot_sales_dot_order__pb2.OrderCreateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def OrderRead(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/pro.omni.oms.api.v1.sales.order.OrderService/OrderRead",
            v1_dot_sales_dot_order__pb2.OrderReadRequest.SerializeToString,
            v1_dot_sales_dot_order__pb2.OrderReadResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def OrderUpdate(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/pro.omni.oms.api.v1.sales.order.OrderService/OrderUpdate",
            v1_dot_sales_dot_order__pb2.OrderUpdateRequest.SerializeToString,
            v1_dot_sales_dot_order__pb2.OrderUpdateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def OrderDelete(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/pro.omni.oms.api.v1.sales.order.OrderService/OrderDelete",
            v1_dot_sales_dot_order__pb2.OrderDeleteRequest.SerializeToString,
            v1_dot_sales_dot_order__pb2.OrderDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def OrderConfirm(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/pro.omni.oms.api.v1.sales.order.OrderService/OrderConfirm",
            v1_dot_sales_dot_order__pb2.OrderConfirmRequest.SerializeToString,
            v1_dot_sales_dot_order__pb2.OrderConfirmResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def SaleStockOperation(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/pro.omni.oms.api.v1.sales.order.OrderService/SaleStockOperation",
            v1_dot_sales_dot_order__pb2.SaleStockOperationRequest.SerializeToString,
            v1_dot_sales_dot_order__pb2.SaleStockOperationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def OrderChangeState(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/pro.omni.oms.api.v1.sales.order.OrderService/OrderChangeState",
            v1_dot_sales_dot_order__pb2.OrderChangeStateRequest.SerializeToString,
            v1_dot_sales_dot_order__pb2.OrderChangeStateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def OrderLineDeliveryQuantity(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/pro.omni.oms.api.v1.sales.order.OrderService/OrderLineDeliveryQuantity",
            v1_dot_sales_dot_order__pb2.OrderLineDeliveryQuantityRequest.SerializeToString,
            v1_dot_sales_dot_order__pb2.OrderLineDeliveryQuantityResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ConfirmOrders(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/pro.omni.oms.api.v1.sales.order.OrderService/ConfirmOrders",
            v1_dot_sales_dot_order__pb2.ConfirmOrdersRequest.SerializeToString,
            v1_dot_sales_dot_order__pb2.ConfirmOrdersResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
