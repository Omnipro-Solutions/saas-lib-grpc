# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni_pro_grpc.v1.tasks import interval_pb2 as v1_dot_tasks_dot_interval__pb2


class IntervalServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.IntervalCreate = channel.unary_unary(
            "/pro.omni.oms.api.tasks.interval.IntervalService/IntervalCreate",
            request_serializer=v1_dot_tasks_dot_interval__pb2.IntervalCreateRequest.SerializeToString,
            response_deserializer=v1_dot_tasks_dot_interval__pb2.IntervalCreateResponse.FromString,
        )
        self.IntervalRead = channel.unary_unary(
            "/pro.omni.oms.api.tasks.interval.IntervalService/IntervalRead",
            request_serializer=v1_dot_tasks_dot_interval__pb2.IntervalReadRequest.SerializeToString,
            response_deserializer=v1_dot_tasks_dot_interval__pb2.IntervalReadResponse.FromString,
        )
        self.IntervalUpdate = channel.unary_unary(
            "/pro.omni.oms.api.tasks.interval.IntervalService/IntervalUpdate",
            request_serializer=v1_dot_tasks_dot_interval__pb2.IntervalUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_tasks_dot_interval__pb2.IntervalUpdateResponse.FromString,
        )
        self.IntervalDelete = channel.unary_unary(
            "/pro.omni.oms.api.tasks.interval.IntervalService/IntervalDelete",
            request_serializer=v1_dot_tasks_dot_interval__pb2.IntervalDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_tasks_dot_interval__pb2.IntervalDeleteResponse.FromString,
        )


class IntervalServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def IntervalCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def IntervalRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def IntervalUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def IntervalDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_IntervalServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "IntervalCreate": grpc.unary_unary_rpc_method_handler(
            servicer.IntervalCreate,
            request_deserializer=v1_dot_tasks_dot_interval__pb2.IntervalCreateRequest.FromString,
            response_serializer=v1_dot_tasks_dot_interval__pb2.IntervalCreateResponse.SerializeToString,
        ),
        "IntervalRead": grpc.unary_unary_rpc_method_handler(
            servicer.IntervalRead,
            request_deserializer=v1_dot_tasks_dot_interval__pb2.IntervalReadRequest.FromString,
            response_serializer=v1_dot_tasks_dot_interval__pb2.IntervalReadResponse.SerializeToString,
        ),
        "IntervalUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.IntervalUpdate,
            request_deserializer=v1_dot_tasks_dot_interval__pb2.IntervalUpdateRequest.FromString,
            response_serializer=v1_dot_tasks_dot_interval__pb2.IntervalUpdateResponse.SerializeToString,
        ),
        "IntervalDelete": grpc.unary_unary_rpc_method_handler(
            servicer.IntervalDelete,
            request_deserializer=v1_dot_tasks_dot_interval__pb2.IntervalDeleteRequest.FromString,
            response_serializer=v1_dot_tasks_dot_interval__pb2.IntervalDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.tasks.interval.IntervalService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class IntervalService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def IntervalCreate(
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
            "/pro.omni.oms.api.tasks.interval.IntervalService/IntervalCreate",
            v1_dot_tasks_dot_interval__pb2.IntervalCreateRequest.SerializeToString,
            v1_dot_tasks_dot_interval__pb2.IntervalCreateResponse.FromString,
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
    def IntervalRead(
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
            "/pro.omni.oms.api.tasks.interval.IntervalService/IntervalRead",
            v1_dot_tasks_dot_interval__pb2.IntervalReadRequest.SerializeToString,
            v1_dot_tasks_dot_interval__pb2.IntervalReadResponse.FromString,
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
    def IntervalUpdate(
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
            "/pro.omni.oms.api.tasks.interval.IntervalService/IntervalUpdate",
            v1_dot_tasks_dot_interval__pb2.IntervalUpdateRequest.SerializeToString,
            v1_dot_tasks_dot_interval__pb2.IntervalUpdateResponse.FromString,
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
    def IntervalDelete(
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
            "/pro.omni.oms.api.tasks.interval.IntervalService/IntervalDelete",
            v1_dot_tasks_dot_interval__pb2.IntervalDeleteRequest.SerializeToString,
            v1_dot_tasks_dot_interval__pb2.IntervalDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )