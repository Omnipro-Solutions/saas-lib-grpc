# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni_pro_grpc.v1.utilities import ms_pb2 as v1_dot_utilities_dot_ms__pb2


class MicroserviceServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MicroserviceCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.microservice.MicroserviceService/MicroserviceCreate",
            request_serializer=v1_dot_utilities_dot_ms__pb2.MicroserviceCreateRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_ms__pb2.MicroserviceCreateResponse.FromString,
        )
        self.MicroserviceRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.microservice.MicroserviceService/MicroserviceRead",
            request_serializer=v1_dot_utilities_dot_ms__pb2.MicroserviceReadRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_ms__pb2.MicroserviceReadResponse.FromString,
        )
        self.MicroserviceUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.microservice.MicroserviceService/MicroserviceUpdate",
            request_serializer=v1_dot_utilities_dot_ms__pb2.MicroserviceUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_ms__pb2.MicroserviceUpdateResponse.FromString,
        )
        self.MicroserviceDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.microservice.MicroserviceService/MicroserviceDelete",
            request_serializer=v1_dot_utilities_dot_ms__pb2.MicroserviceDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_ms__pb2.MicroserviceDeleteResponse.FromString,
        )


class MicroserviceServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def MicroserviceCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def MicroserviceRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def MicroserviceUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def MicroserviceDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_MicroserviceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "MicroserviceCreate": grpc.unary_unary_rpc_method_handler(
            servicer.MicroserviceCreate,
            request_deserializer=v1_dot_utilities_dot_ms__pb2.MicroserviceCreateRequest.FromString,
            response_serializer=v1_dot_utilities_dot_ms__pb2.MicroserviceCreateResponse.SerializeToString,
        ),
        "MicroserviceRead": grpc.unary_unary_rpc_method_handler(
            servicer.MicroserviceRead,
            request_deserializer=v1_dot_utilities_dot_ms__pb2.MicroserviceReadRequest.FromString,
            response_serializer=v1_dot_utilities_dot_ms__pb2.MicroserviceReadResponse.SerializeToString,
        ),
        "MicroserviceUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.MicroserviceUpdate,
            request_deserializer=v1_dot_utilities_dot_ms__pb2.MicroserviceUpdateRequest.FromString,
            response_serializer=v1_dot_utilities_dot_ms__pb2.MicroserviceUpdateResponse.SerializeToString,
        ),
        "MicroserviceDelete": grpc.unary_unary_rpc_method_handler(
            servicer.MicroserviceDelete,
            request_deserializer=v1_dot_utilities_dot_ms__pb2.MicroserviceDeleteRequest.FromString,
            response_serializer=v1_dot_utilities_dot_ms__pb2.MicroserviceDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.utilities.microservice.MicroserviceService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class MicroserviceService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def MicroserviceCreate(
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
            "/pro.omni.oms.api.v1.utilities.microservice.MicroserviceService/MicroserviceCreate",
            v1_dot_utilities_dot_ms__pb2.MicroserviceCreateRequest.SerializeToString,
            v1_dot_utilities_dot_ms__pb2.MicroserviceCreateResponse.FromString,
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
    def MicroserviceRead(
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
            "/pro.omni.oms.api.v1.utilities.microservice.MicroserviceService/MicroserviceRead",
            v1_dot_utilities_dot_ms__pb2.MicroserviceReadRequest.SerializeToString,
            v1_dot_utilities_dot_ms__pb2.MicroserviceReadResponse.FromString,
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
    def MicroserviceUpdate(
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
            "/pro.omni.oms.api.v1.utilities.microservice.MicroserviceService/MicroserviceUpdate",
            v1_dot_utilities_dot_ms__pb2.MicroserviceUpdateRequest.SerializeToString,
            v1_dot_utilities_dot_ms__pb2.MicroserviceUpdateResponse.FromString,
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
    def MicroserviceDelete(
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
            "/pro.omni.oms.api.v1.utilities.microservice.MicroserviceService/MicroserviceDelete",
            v1_dot_utilities_dot_ms__pb2.MicroserviceDeleteRequest.SerializeToString,
            v1_dot_utilities_dot_ms__pb2.MicroserviceDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
