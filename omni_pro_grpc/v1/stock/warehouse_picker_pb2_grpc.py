# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni_pro_grpc.v1.stock import warehouse_picker_pb2 as v1_dot_stock_dot_warehouse__picker__pb2


class WarehousePickerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.WarehousePickerRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.warehouse_picker.WarehousePickerService/WarehousePickerRead",
            request_serializer=v1_dot_stock_dot_warehouse__picker__pb2.WarehousePickerReadRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_warehouse__picker__pb2.WarehousePickerReadResponse.FromString,
        )


class WarehousePickerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def WarehousePickerRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_WarehousePickerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "WarehousePickerRead": grpc.unary_unary_rpc_method_handler(
            servicer.WarehousePickerRead,
            request_deserializer=v1_dot_stock_dot_warehouse__picker__pb2.WarehousePickerReadRequest.FromString,
            response_serializer=v1_dot_stock_dot_warehouse__picker__pb2.WarehousePickerReadResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.stock.warehouse_picker.WarehousePickerService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class WarehousePickerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def WarehousePickerRead(
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
            "/pro.omni.oms.api.v1.stock.warehouse_picker.WarehousePickerService/WarehousePickerRead",
            v1_dot_stock_dot_warehouse__picker__pb2.WarehousePickerReadRequest.SerializeToString,
            v1_dot_stock_dot_warehouse__picker__pb2.WarehousePickerReadResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
