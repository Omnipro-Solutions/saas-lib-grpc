# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni_pro_grpc.v1.utilities import event_pb2 as v1_dot_utilities_dot_event__pb2


class EventServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.EventCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.event.EventService/EventCreate",
            request_serializer=v1_dot_utilities_dot_event__pb2.EventCreateRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_event__pb2.EventCreateResponse.FromString,
        )
        self.EventRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.event.EventService/EventRead",
            request_serializer=v1_dot_utilities_dot_event__pb2.EventReadRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_event__pb2.EventReadResponse.FromString,
        )
        self.EventUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.event.EventService/EventUpdate",
            request_serializer=v1_dot_utilities_dot_event__pb2.EventUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_event__pb2.EventUpdateResponse.FromString,
        )
        self.EventDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.event.EventService/EventDelete",
            request_serializer=v1_dot_utilities_dot_event__pb2.EventDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_event__pb2.EventDeleteResponse.FromString,
        )


class EventServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def EventCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def EventRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def EventUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def EventDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_EventServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "EventCreate": grpc.unary_unary_rpc_method_handler(
            servicer.EventCreate,
            request_deserializer=v1_dot_utilities_dot_event__pb2.EventCreateRequest.FromString,
            response_serializer=v1_dot_utilities_dot_event__pb2.EventCreateResponse.SerializeToString,
        ),
        "EventRead": grpc.unary_unary_rpc_method_handler(
            servicer.EventRead,
            request_deserializer=v1_dot_utilities_dot_event__pb2.EventReadRequest.FromString,
            response_serializer=v1_dot_utilities_dot_event__pb2.EventReadResponse.SerializeToString,
        ),
        "EventUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.EventUpdate,
            request_deserializer=v1_dot_utilities_dot_event__pb2.EventUpdateRequest.FromString,
            response_serializer=v1_dot_utilities_dot_event__pb2.EventUpdateResponse.SerializeToString,
        ),
        "EventDelete": grpc.unary_unary_rpc_method_handler(
            servicer.EventDelete,
            request_deserializer=v1_dot_utilities_dot_event__pb2.EventDeleteRequest.FromString,
            response_serializer=v1_dot_utilities_dot_event__pb2.EventDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.utilities.event.EventService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class EventService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def EventCreate(
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
            "/pro.omni.oms.api.v1.utilities.event.EventService/EventCreate",
            v1_dot_utilities_dot_event__pb2.EventCreateRequest.SerializeToString,
            v1_dot_utilities_dot_event__pb2.EventCreateResponse.FromString,
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
    def EventRead(
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
            "/pro.omni.oms.api.v1.utilities.event.EventService/EventRead",
            v1_dot_utilities_dot_event__pb2.EventReadRequest.SerializeToString,
            v1_dot_utilities_dot_event__pb2.EventReadResponse.FromString,
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
    def EventUpdate(
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
            "/pro.omni.oms.api.v1.utilities.event.EventService/EventUpdate",
            v1_dot_utilities_dot_event__pb2.EventUpdateRequest.SerializeToString,
            v1_dot_utilities_dot_event__pb2.EventUpdateResponse.FromString,
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
    def EventDelete(
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
            "/pro.omni.oms.api.v1.utilities.event.EventService/EventDelete",
            v1_dot_utilities_dot_event__pb2.EventDeleteRequest.SerializeToString,
            v1_dot_utilities_dot_event__pb2.EventDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
