# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni_pro_grpc.v1.stock import attachment_pb2 as v1_dot_stock_dot_attachment__pb2


class AttachmentServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AttachmentCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.attachment.AttachmentService/AttachmentCreate",
            request_serializer=v1_dot_stock_dot_attachment__pb2.AttachmentCreateRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_attachment__pb2.AttachmentCreateResponse.FromString,
        )
        self.AttachmentRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.attachment.AttachmentService/AttachmentRead",
            request_serializer=v1_dot_stock_dot_attachment__pb2.AttachmentReadRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_attachment__pb2.AttachmentReadResponse.FromString,
        )
        self.AttachmentUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.attachment.AttachmentService/AttachmentUpdate",
            request_serializer=v1_dot_stock_dot_attachment__pb2.AttachmentUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_attachment__pb2.AttachmentUpdateResponse.FromString,
        )
        self.AttachmentDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.attachment.AttachmentService/AttachmentDelete",
            request_serializer=v1_dot_stock_dot_attachment__pb2.AttachmentDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_attachment__pb2.AttachmentDeleteResponse.FromString,
        )


class AttachmentServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AttachmentCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AttachmentRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AttachmentUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AttachmentDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_AttachmentServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "AttachmentCreate": grpc.unary_unary_rpc_method_handler(
            servicer.AttachmentCreate,
            request_deserializer=v1_dot_stock_dot_attachment__pb2.AttachmentCreateRequest.FromString,
            response_serializer=v1_dot_stock_dot_attachment__pb2.AttachmentCreateResponse.SerializeToString,
        ),
        "AttachmentRead": grpc.unary_unary_rpc_method_handler(
            servicer.AttachmentRead,
            request_deserializer=v1_dot_stock_dot_attachment__pb2.AttachmentReadRequest.FromString,
            response_serializer=v1_dot_stock_dot_attachment__pb2.AttachmentReadResponse.SerializeToString,
        ),
        "AttachmentUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.AttachmentUpdate,
            request_deserializer=v1_dot_stock_dot_attachment__pb2.AttachmentUpdateRequest.FromString,
            response_serializer=v1_dot_stock_dot_attachment__pb2.AttachmentUpdateResponse.SerializeToString,
        ),
        "AttachmentDelete": grpc.unary_unary_rpc_method_handler(
            servicer.AttachmentDelete,
            request_deserializer=v1_dot_stock_dot_attachment__pb2.AttachmentDeleteRequest.FromString,
            response_serializer=v1_dot_stock_dot_attachment__pb2.AttachmentDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.stock.attachment.AttachmentService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class AttachmentService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AttachmentCreate(
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
            "/pro.omni.oms.api.v1.stock.attachment.AttachmentService/AttachmentCreate",
            v1_dot_stock_dot_attachment__pb2.AttachmentCreateRequest.SerializeToString,
            v1_dot_stock_dot_attachment__pb2.AttachmentCreateResponse.FromString,
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
    def AttachmentRead(
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
            "/pro.omni.oms.api.v1.stock.attachment.AttachmentService/AttachmentRead",
            v1_dot_stock_dot_attachment__pb2.AttachmentReadRequest.SerializeToString,
            v1_dot_stock_dot_attachment__pb2.AttachmentReadResponse.FromString,
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
    def AttachmentUpdate(
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
            "/pro.omni.oms.api.v1.stock.attachment.AttachmentService/AttachmentUpdate",
            v1_dot_stock_dot_attachment__pb2.AttachmentUpdateRequest.SerializeToString,
            v1_dot_stock_dot_attachment__pb2.AttachmentUpdateResponse.FromString,
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
    def AttachmentDelete(
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
            "/pro.omni.oms.api.v1.stock.attachment.AttachmentService/AttachmentDelete",
            v1_dot_stock_dot_attachment__pb2.AttachmentDeleteRequest.SerializeToString,
            v1_dot_stock_dot_attachment__pb2.AttachmentDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
