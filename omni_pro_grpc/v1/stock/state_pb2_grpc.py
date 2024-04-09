# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni_pro_grpc.v1.stock import state_pb2 as v1_dot_stock_dot_state__pb2


class StateServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StateUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.state.StateService/StateUpdate",
            request_serializer=v1_dot_stock_dot_state__pb2.StateUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_state__pb2.StateUpdateResponse.FromString,
        )
        self.StateDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.state.StateService/StateDelete",
            request_serializer=v1_dot_stock_dot_state__pb2.StateDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_state__pb2.StateDeleteResponse.FromString,
        )


class StateServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StateUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def StateDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_StateServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "StateUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.StateUpdate,
            request_deserializer=v1_dot_stock_dot_state__pb2.StateUpdateRequest.FromString,
            response_serializer=v1_dot_stock_dot_state__pb2.StateUpdateResponse.SerializeToString,
        ),
        "StateDelete": grpc.unary_unary_rpc_method_handler(
            servicer.StateDelete,
            request_deserializer=v1_dot_stock_dot_state__pb2.StateDeleteRequest.FromString,
            response_serializer=v1_dot_stock_dot_state__pb2.StateDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.stock.state.StateService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class StateService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StateUpdate(
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
            "/pro.omni.oms.api.v1.stock.state.StateService/StateUpdate",
            v1_dot_stock_dot_state__pb2.StateUpdateRequest.SerializeToString,
            v1_dot_stock_dot_state__pb2.StateUpdateResponse.FromString,
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
    def StateDelete(
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
            "/pro.omni.oms.api.v1.stock.state.StateService/StateDelete",
            v1_dot_stock_dot_state__pb2.StateDeleteRequest.SerializeToString,
            v1_dot_stock_dot_state__pb2.StateDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
