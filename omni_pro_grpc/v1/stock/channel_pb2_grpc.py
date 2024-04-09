# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni_pro_grpc.v1.stock import channel_pb2 as v1_dot_stock_dot_channel__pb2


class ChannelServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ChannelUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.channel.ChannelService/ChannelUpdate",
            request_serializer=v1_dot_stock_dot_channel__pb2.ChannelUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_channel__pb2.ChannelUpdateResponse.FromString,
        )
        self.ChannelDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.channel.ChannelService/ChannelDelete",
            request_serializer=v1_dot_stock_dot_channel__pb2.ChannelDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_channel__pb2.ChannelDeleteResponse.FromString,
        )


class ChannelServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ChannelUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ChannelDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ChannelServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ChannelUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.ChannelUpdate,
            request_deserializer=v1_dot_stock_dot_channel__pb2.ChannelUpdateRequest.FromString,
            response_serializer=v1_dot_stock_dot_channel__pb2.ChannelUpdateResponse.SerializeToString,
        ),
        "ChannelDelete": grpc.unary_unary_rpc_method_handler(
            servicer.ChannelDelete,
            request_deserializer=v1_dot_stock_dot_channel__pb2.ChannelDeleteRequest.FromString,
            response_serializer=v1_dot_stock_dot_channel__pb2.ChannelDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.stock.channel.ChannelService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class ChannelService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ChannelUpdate(
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
            "/pro.omni.oms.api.v1.stock.channel.ChannelService/ChannelUpdate",
            v1_dot_stock_dot_channel__pb2.ChannelUpdateRequest.SerializeToString,
            v1_dot_stock_dot_channel__pb2.ChannelUpdateResponse.FromString,
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
    def ChannelDelete(
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
            "/pro.omni.oms.api.v1.stock.channel.ChannelService/ChannelDelete",
            v1_dot_stock_dot_channel__pb2.ChannelDeleteRequest.SerializeToString,
            v1_dot_stock_dot_channel__pb2.ChannelDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
