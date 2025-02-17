# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni_pro_grpc.v1.utilities import template_notification_pb2 as v1_dot_utilities_dot_template__notification__pb2


class TemplateNotificationServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TemplateNotificationCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.template_notification.TemplateNotificationService/TemplateNotificationCreate",
            request_serializer=v1_dot_utilities_dot_template__notification__pb2.TemplateNotificationCreateRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_template__notification__pb2.TemplateNotificationCreateResponse.FromString,
        )
        self.TemplateNotificationRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.template_notification.TemplateNotificationService/TemplateNotificationRead",
            request_serializer=v1_dot_utilities_dot_template__notification__pb2.TemplateNotificationReadRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_template__notification__pb2.TemplateNotificationReadResponse.FromString,
        )
        self.TemplateNotificationUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.template_notification.TemplateNotificationService/TemplateNotificationUpdate",
            request_serializer=v1_dot_utilities_dot_template__notification__pb2.TemplateNotificationUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_template__notification__pb2.TemplateNotificationUpdateResponse.FromString,
        )
        self.TemplateNotificationDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.template_notification.TemplateNotificationService/TemplateNotificationDelete",
            request_serializer=v1_dot_utilities_dot_template__notification__pb2.TemplateNotificationDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_template__notification__pb2.TemplateNotificationDeleteResponse.FromString,
        )
        self.TemplateNotificationRender = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.template_notification.TemplateNotificationService/TemplateNotificationRender",
            request_serializer=v1_dot_utilities_dot_template__notification__pb2.TemplateNotificationRenderRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_template__notification__pb2.TemplateNotificationRenderResponse.FromString,
        )


class TemplateNotificationServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def TemplateNotificationCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def TemplateNotificationRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def TemplateNotificationUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def TemplateNotificationDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def TemplateNotificationRender(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_TemplateNotificationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "TemplateNotificationCreate": grpc.unary_unary_rpc_method_handler(
            servicer.TemplateNotificationCreate,
            request_deserializer=v1_dot_utilities_dot_template__notification__pb2.TemplateNotificationCreateRequest.FromString,
            response_serializer=v1_dot_utilities_dot_template__notification__pb2.TemplateNotificationCreateResponse.SerializeToString,
        ),
        "TemplateNotificationRead": grpc.unary_unary_rpc_method_handler(
            servicer.TemplateNotificationRead,
            request_deserializer=v1_dot_utilities_dot_template__notification__pb2.TemplateNotificationReadRequest.FromString,
            response_serializer=v1_dot_utilities_dot_template__notification__pb2.TemplateNotificationReadResponse.SerializeToString,
        ),
        "TemplateNotificationUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.TemplateNotificationUpdate,
            request_deserializer=v1_dot_utilities_dot_template__notification__pb2.TemplateNotificationUpdateRequest.FromString,
            response_serializer=v1_dot_utilities_dot_template__notification__pb2.TemplateNotificationUpdateResponse.SerializeToString,
        ),
        "TemplateNotificationDelete": grpc.unary_unary_rpc_method_handler(
            servicer.TemplateNotificationDelete,
            request_deserializer=v1_dot_utilities_dot_template__notification__pb2.TemplateNotificationDeleteRequest.FromString,
            response_serializer=v1_dot_utilities_dot_template__notification__pb2.TemplateNotificationDeleteResponse.SerializeToString,
        ),
        "TemplateNotificationRender": grpc.unary_unary_rpc_method_handler(
            servicer.TemplateNotificationRender,
            request_deserializer=v1_dot_utilities_dot_template__notification__pb2.TemplateNotificationRenderRequest.FromString,
            response_serializer=v1_dot_utilities_dot_template__notification__pb2.TemplateNotificationRenderResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.utilities.template_notification.TemplateNotificationService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class TemplateNotificationService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def TemplateNotificationCreate(
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
            "/pro.omni.oms.api.v1.utilities.template_notification.TemplateNotificationService/TemplateNotificationCreate",
            v1_dot_utilities_dot_template__notification__pb2.TemplateNotificationCreateRequest.SerializeToString,
            v1_dot_utilities_dot_template__notification__pb2.TemplateNotificationCreateResponse.FromString,
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
    def TemplateNotificationRead(
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
            "/pro.omni.oms.api.v1.utilities.template_notification.TemplateNotificationService/TemplateNotificationRead",
            v1_dot_utilities_dot_template__notification__pb2.TemplateNotificationReadRequest.SerializeToString,
            v1_dot_utilities_dot_template__notification__pb2.TemplateNotificationReadResponse.FromString,
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
    def TemplateNotificationUpdate(
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
            "/pro.omni.oms.api.v1.utilities.template_notification.TemplateNotificationService/TemplateNotificationUpdate",
            v1_dot_utilities_dot_template__notification__pb2.TemplateNotificationUpdateRequest.SerializeToString,
            v1_dot_utilities_dot_template__notification__pb2.TemplateNotificationUpdateResponse.FromString,
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
    def TemplateNotificationDelete(
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
            "/pro.omni.oms.api.v1.utilities.template_notification.TemplateNotificationService/TemplateNotificationDelete",
            v1_dot_utilities_dot_template__notification__pb2.TemplateNotificationDeleteRequest.SerializeToString,
            v1_dot_utilities_dot_template__notification__pb2.TemplateNotificationDeleteResponse.FromString,
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
    def TemplateNotificationRender(
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
            "/pro.omni.oms.api.v1.utilities.template_notification.TemplateNotificationService/TemplateNotificationRender",
            v1_dot_utilities_dot_template__notification__pb2.TemplateNotificationRenderRequest.SerializeToString,
            v1_dot_utilities_dot_template__notification__pb2.TemplateNotificationRenderResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
