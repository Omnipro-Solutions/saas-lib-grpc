# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni_pro_grpc.v1.utilities import method_grpc_pb2 as v1_dot_utilities_dot_method__grpc__pb2


class MethodGrpcServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MethodGrpcCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.method_grpc.MethodGrpcService/MethodGrpcCreate",
            request_serializer=v1_dot_utilities_dot_method__grpc__pb2.MethodGrpcCreateRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_method__grpc__pb2.MethodGrpcCreateResponse.FromString,
        )
        self.MethodGrpcRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.method_grpc.MethodGrpcService/MethodGrpcRead",
            request_serializer=v1_dot_utilities_dot_method__grpc__pb2.MethodGrpcReadRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_method__grpc__pb2.MethodGrpcReadResponse.FromString,
        )
        self.MethodGrpcUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.method_grpc.MethodGrpcService/MethodGrpcUpdate",
            request_serializer=v1_dot_utilities_dot_method__grpc__pb2.MethodGrpcUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_method__grpc__pb2.MethodGrpcUpdateResponse.FromString,
        )
        self.MethodGrpcDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.method_grpc.MethodGrpcService/MethodGrpcDelete",
            request_serializer=v1_dot_utilities_dot_method__grpc__pb2.MethodGrpcDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_method__grpc__pb2.MethodGrpcDeleteResponse.FromString,
        )


class MethodGrpcServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def MethodGrpcCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def MethodGrpcRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def MethodGrpcUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def MethodGrpcDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_MethodGrpcServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "MethodGrpcCreate": grpc.unary_unary_rpc_method_handler(
            servicer.MethodGrpcCreate,
            request_deserializer=v1_dot_utilities_dot_method__grpc__pb2.MethodGrpcCreateRequest.FromString,
            response_serializer=v1_dot_utilities_dot_method__grpc__pb2.MethodGrpcCreateResponse.SerializeToString,
        ),
        "MethodGrpcRead": grpc.unary_unary_rpc_method_handler(
            servicer.MethodGrpcRead,
            request_deserializer=v1_dot_utilities_dot_method__grpc__pb2.MethodGrpcReadRequest.FromString,
            response_serializer=v1_dot_utilities_dot_method__grpc__pb2.MethodGrpcReadResponse.SerializeToString,
        ),
        "MethodGrpcUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.MethodGrpcUpdate,
            request_deserializer=v1_dot_utilities_dot_method__grpc__pb2.MethodGrpcUpdateRequest.FromString,
            response_serializer=v1_dot_utilities_dot_method__grpc__pb2.MethodGrpcUpdateResponse.SerializeToString,
        ),
        "MethodGrpcDelete": grpc.unary_unary_rpc_method_handler(
            servicer.MethodGrpcDelete,
            request_deserializer=v1_dot_utilities_dot_method__grpc__pb2.MethodGrpcDeleteRequest.FromString,
            response_serializer=v1_dot_utilities_dot_method__grpc__pb2.MethodGrpcDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.utilities.method_grpc.MethodGrpcService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class MethodGrpcService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def MethodGrpcCreate(
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
            "/pro.omni.oms.api.v1.utilities.method_grpc.MethodGrpcService/MethodGrpcCreate",
            v1_dot_utilities_dot_method__grpc__pb2.MethodGrpcCreateRequest.SerializeToString,
            v1_dot_utilities_dot_method__grpc__pb2.MethodGrpcCreateResponse.FromString,
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
    def MethodGrpcRead(
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
            "/pro.omni.oms.api.v1.utilities.method_grpc.MethodGrpcService/MethodGrpcRead",
            v1_dot_utilities_dot_method__grpc__pb2.MethodGrpcReadRequest.SerializeToString,
            v1_dot_utilities_dot_method__grpc__pb2.MethodGrpcReadResponse.FromString,
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
    def MethodGrpcUpdate(
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
            "/pro.omni.oms.api.v1.utilities.method_grpc.MethodGrpcService/MethodGrpcUpdate",
            v1_dot_utilities_dot_method__grpc__pb2.MethodGrpcUpdateRequest.SerializeToString,
            v1_dot_utilities_dot_method__grpc__pb2.MethodGrpcUpdateResponse.FromString,
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
    def MethodGrpcDelete(
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
            "/pro.omni.oms.api.v1.utilities.method_grpc.MethodGrpcService/MethodGrpcDelete",
            v1_dot_utilities_dot_method__grpc__pb2.MethodGrpcDeleteRequest.SerializeToString,
            v1_dot_utilities_dot_method__grpc__pb2.MethodGrpcDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
