# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni_pro_grpc.v1.stock import picking_pb2 as v1_dot_stock_dot_picking__pb2


class PickingServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PickingCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.picking.PickingService/PickingCreate",
            request_serializer=v1_dot_stock_dot_picking__pb2.PickingCreateRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_picking__pb2.PickingCreateResponse.FromString,
        )
        self.PickingRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.picking.PickingService/PickingRead",
            request_serializer=v1_dot_stock_dot_picking__pb2.PickingReadRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_picking__pb2.PickingReadResponse.FromString,
        )
        self.PickingUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.picking.PickingService/PickingUpdate",
            request_serializer=v1_dot_stock_dot_picking__pb2.PickingUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_picking__pb2.PickingUpdateResponse.FromString,
        )
        self.PickingDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.picking.PickingService/PickingDelete",
            request_serializer=v1_dot_stock_dot_picking__pb2.PickingDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_picking__pb2.PickingDeleteResponse.FromString,
        )
        self.ValidatePicking = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.picking.PickingService/ValidatePicking",
            request_serializer=v1_dot_stock_dot_picking__pb2.ValidatePickingRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_picking__pb2.ValidatePickingResponse.FromString,
        )
        self.PickingMoves = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.picking.PickingService/PickingMoves",
            request_serializer=v1_dot_stock_dot_picking__pb2.PickingMovesRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_picking__pb2.PickingMovesResponse.FromString,
        )
        self.OrderConfirm = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.picking.PickingService/OrderConfirm",
            request_serializer=v1_dot_stock_dot_picking__pb2.OrderConfirmRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_picking__pb2.OrderConfirmResponse.FromString,
        )
        self.SalePicking = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.picking.PickingService/SalePicking",
            request_serializer=v1_dot_stock_dot_picking__pb2.SalePickingRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_picking__pb2.SalePickingResponse.FromString,
        )
        self.PickingKanban = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.picking.PickingService/PickingKanban",
            request_serializer=v1_dot_stock_dot_picking__pb2.PickingKanbanReadRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_picking__pb2.PickingKanbanReadResponse.FromString,
        )
        self.CheckAvailability = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.picking.PickingService/CheckAvailability",
            request_serializer=v1_dot_stock_dot_picking__pb2.CheckAvailabilityRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_picking__pb2.CheckAvailabilityResponse.FromString,
        )
        self.GetProductAvailableSubstitution = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.picking.PickingService/GetProductAvailableSubstitution",
            request_serializer=v1_dot_stock_dot_picking__pb2.GetProductAvailableSubstitutionRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_picking__pb2.GetProductAvailableSubstitutionResponse.FromString,
        )


class PickingServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PickingCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def PickingRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def PickingUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def PickingDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ValidatePicking(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def PickingMoves(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def OrderConfirm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SalePicking(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def PickingKanban(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CheckAvailability(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetProductAvailableSubstitution(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_PickingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "PickingCreate": grpc.unary_unary_rpc_method_handler(
            servicer.PickingCreate,
            request_deserializer=v1_dot_stock_dot_picking__pb2.PickingCreateRequest.FromString,
            response_serializer=v1_dot_stock_dot_picking__pb2.PickingCreateResponse.SerializeToString,
        ),
        "PickingRead": grpc.unary_unary_rpc_method_handler(
            servicer.PickingRead,
            request_deserializer=v1_dot_stock_dot_picking__pb2.PickingReadRequest.FromString,
            response_serializer=v1_dot_stock_dot_picking__pb2.PickingReadResponse.SerializeToString,
        ),
        "PickingUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.PickingUpdate,
            request_deserializer=v1_dot_stock_dot_picking__pb2.PickingUpdateRequest.FromString,
            response_serializer=v1_dot_stock_dot_picking__pb2.PickingUpdateResponse.SerializeToString,
        ),
        "PickingDelete": grpc.unary_unary_rpc_method_handler(
            servicer.PickingDelete,
            request_deserializer=v1_dot_stock_dot_picking__pb2.PickingDeleteRequest.FromString,
            response_serializer=v1_dot_stock_dot_picking__pb2.PickingDeleteResponse.SerializeToString,
        ),
        "ValidatePicking": grpc.unary_unary_rpc_method_handler(
            servicer.ValidatePicking,
            request_deserializer=v1_dot_stock_dot_picking__pb2.ValidatePickingRequest.FromString,
            response_serializer=v1_dot_stock_dot_picking__pb2.ValidatePickingResponse.SerializeToString,
        ),
        "PickingMoves": grpc.unary_unary_rpc_method_handler(
            servicer.PickingMoves,
            request_deserializer=v1_dot_stock_dot_picking__pb2.PickingMovesRequest.FromString,
            response_serializer=v1_dot_stock_dot_picking__pb2.PickingMovesResponse.SerializeToString,
        ),
        "OrderConfirm": grpc.unary_unary_rpc_method_handler(
            servicer.OrderConfirm,
            request_deserializer=v1_dot_stock_dot_picking__pb2.OrderConfirmRequest.FromString,
            response_serializer=v1_dot_stock_dot_picking__pb2.OrderConfirmResponse.SerializeToString,
        ),
        "SalePicking": grpc.unary_unary_rpc_method_handler(
            servicer.SalePicking,
            request_deserializer=v1_dot_stock_dot_picking__pb2.SalePickingRequest.FromString,
            response_serializer=v1_dot_stock_dot_picking__pb2.SalePickingResponse.SerializeToString,
        ),
        "PickingKanban": grpc.unary_unary_rpc_method_handler(
            servicer.PickingKanban,
            request_deserializer=v1_dot_stock_dot_picking__pb2.PickingKanbanReadRequest.FromString,
            response_serializer=v1_dot_stock_dot_picking__pb2.PickingKanbanReadResponse.SerializeToString,
        ),
        "CheckAvailability": grpc.unary_unary_rpc_method_handler(
            servicer.CheckAvailability,
            request_deserializer=v1_dot_stock_dot_picking__pb2.CheckAvailabilityRequest.FromString,
            response_serializer=v1_dot_stock_dot_picking__pb2.CheckAvailabilityResponse.SerializeToString,
        ),
        "GetProductAvailableSubstitution": grpc.unary_unary_rpc_method_handler(
            servicer.GetProductAvailableSubstitution,
            request_deserializer=v1_dot_stock_dot_picking__pb2.GetProductAvailableSubstitutionRequest.FromString,
            response_serializer=v1_dot_stock_dot_picking__pb2.GetProductAvailableSubstitutionResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.stock.picking.PickingService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class PickingService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PickingCreate(
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
            "/pro.omni.oms.api.v1.stock.picking.PickingService/PickingCreate",
            v1_dot_stock_dot_picking__pb2.PickingCreateRequest.SerializeToString,
            v1_dot_stock_dot_picking__pb2.PickingCreateResponse.FromString,
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
    def PickingRead(
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
            "/pro.omni.oms.api.v1.stock.picking.PickingService/PickingRead",
            v1_dot_stock_dot_picking__pb2.PickingReadRequest.SerializeToString,
            v1_dot_stock_dot_picking__pb2.PickingReadResponse.FromString,
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
    def PickingUpdate(
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
            "/pro.omni.oms.api.v1.stock.picking.PickingService/PickingUpdate",
            v1_dot_stock_dot_picking__pb2.PickingUpdateRequest.SerializeToString,
            v1_dot_stock_dot_picking__pb2.PickingUpdateResponse.FromString,
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
    def PickingDelete(
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
            "/pro.omni.oms.api.v1.stock.picking.PickingService/PickingDelete",
            v1_dot_stock_dot_picking__pb2.PickingDeleteRequest.SerializeToString,
            v1_dot_stock_dot_picking__pb2.PickingDeleteResponse.FromString,
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
    def ValidatePicking(
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
            "/pro.omni.oms.api.v1.stock.picking.PickingService/ValidatePicking",
            v1_dot_stock_dot_picking__pb2.ValidatePickingRequest.SerializeToString,
            v1_dot_stock_dot_picking__pb2.ValidatePickingResponse.FromString,
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
    def PickingMoves(
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
            "/pro.omni.oms.api.v1.stock.picking.PickingService/PickingMoves",
            v1_dot_stock_dot_picking__pb2.PickingMovesRequest.SerializeToString,
            v1_dot_stock_dot_picking__pb2.PickingMovesResponse.FromString,
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
            "/pro.omni.oms.api.v1.stock.picking.PickingService/OrderConfirm",
            v1_dot_stock_dot_picking__pb2.OrderConfirmRequest.SerializeToString,
            v1_dot_stock_dot_picking__pb2.OrderConfirmResponse.FromString,
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
    def SalePicking(
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
            "/pro.omni.oms.api.v1.stock.picking.PickingService/SalePicking",
            v1_dot_stock_dot_picking__pb2.SalePickingRequest.SerializeToString,
            v1_dot_stock_dot_picking__pb2.SalePickingResponse.FromString,
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
    def PickingKanban(
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
            "/pro.omni.oms.api.v1.stock.picking.PickingService/PickingKanban",
            v1_dot_stock_dot_picking__pb2.PickingKanbanReadRequest.SerializeToString,
            v1_dot_stock_dot_picking__pb2.PickingKanbanReadResponse.FromString,
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
    def CheckAvailability(
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
            "/pro.omni.oms.api.v1.stock.picking.PickingService/CheckAvailability",
            v1_dot_stock_dot_picking__pb2.CheckAvailabilityRequest.SerializeToString,
            v1_dot_stock_dot_picking__pb2.CheckAvailabilityResponse.FromString,
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
    def GetProductAvailableSubstitution(
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
            "/pro.omni.oms.api.v1.stock.picking.PickingService/GetProductAvailableSubstitution",
            v1_dot_stock_dot_picking__pb2.GetProductAvailableSubstitutionRequest.SerializeToString,
            v1_dot_stock_dot_picking__pb2.GetProductAvailableSubstitutionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
