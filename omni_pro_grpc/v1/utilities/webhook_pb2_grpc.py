# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni_pro_grpc.v1.utilities import webhook_pb2 as v1_dot_utilities_dot_webhook__pb2


class WebhookServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.WebhookCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.webhook.WebhookService/WebhookCreate",
            request_serializer=v1_dot_utilities_dot_webhook__pb2.WebhookCreateRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_webhook__pb2.WebhookCreateResponse.FromString,
        )
        self.WebhookRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.webhook.WebhookService/WebhookRead",
            request_serializer=v1_dot_utilities_dot_webhook__pb2.WebhookReadRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_webhook__pb2.WebhookReadResponse.FromString,
        )
        self.WebhookUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.webhook.WebhookService/WebhookUpdate",
            request_serializer=v1_dot_utilities_dot_webhook__pb2.WebhookUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_webhook__pb2.WebhookUpdateResponse.FromString,
        )
        self.WebhookDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.webhook.WebhookService/WebhookDelete",
            request_serializer=v1_dot_utilities_dot_webhook__pb2.WebhookDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_webhook__pb2.WebhookDeleteResponse.FromString,
        )


class WebhookServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def WebhookCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def WebhookRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def WebhookUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def WebhookDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_WebhookServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "WebhookCreate": grpc.unary_unary_rpc_method_handler(
            servicer.WebhookCreate,
            request_deserializer=v1_dot_utilities_dot_webhook__pb2.WebhookCreateRequest.FromString,
            response_serializer=v1_dot_utilities_dot_webhook__pb2.WebhookCreateResponse.SerializeToString,
        ),
        "WebhookRead": grpc.unary_unary_rpc_method_handler(
            servicer.WebhookRead,
            request_deserializer=v1_dot_utilities_dot_webhook__pb2.WebhookReadRequest.FromString,
            response_serializer=v1_dot_utilities_dot_webhook__pb2.WebhookReadResponse.SerializeToString,
        ),
        "WebhookUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.WebhookUpdate,
            request_deserializer=v1_dot_utilities_dot_webhook__pb2.WebhookUpdateRequest.FromString,
            response_serializer=v1_dot_utilities_dot_webhook__pb2.WebhookUpdateResponse.SerializeToString,
        ),
        "WebhookDelete": grpc.unary_unary_rpc_method_handler(
            servicer.WebhookDelete,
            request_deserializer=v1_dot_utilities_dot_webhook__pb2.WebhookDeleteRequest.FromString,
            response_serializer=v1_dot_utilities_dot_webhook__pb2.WebhookDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.utilities.webhook.WebhookService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class WebhookService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def WebhookCreate(
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
            "/pro.omni.oms.api.v1.utilities.webhook.WebhookService/WebhookCreate",
            v1_dot_utilities_dot_webhook__pb2.WebhookCreateRequest.SerializeToString,
            v1_dot_utilities_dot_webhook__pb2.WebhookCreateResponse.FromString,
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
    def WebhookRead(
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
            "/pro.omni.oms.api.v1.utilities.webhook.WebhookService/WebhookRead",
            v1_dot_utilities_dot_webhook__pb2.WebhookReadRequest.SerializeToString,
            v1_dot_utilities_dot_webhook__pb2.WebhookReadResponse.FromString,
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
    def WebhookUpdate(
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
            "/pro.omni.oms.api.v1.utilities.webhook.WebhookService/WebhookUpdate",
            v1_dot_utilities_dot_webhook__pb2.WebhookUpdateRequest.SerializeToString,
            v1_dot_utilities_dot_webhook__pb2.WebhookUpdateResponse.FromString,
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
    def WebhookDelete(
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
            "/pro.omni.oms.api.v1.utilities.webhook.WebhookService/WebhookDelete",
            v1_dot_utilities_dot_webhook__pb2.WebhookDeleteRequest.SerializeToString,
            v1_dot_utilities_dot_webhook__pb2.WebhookDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
