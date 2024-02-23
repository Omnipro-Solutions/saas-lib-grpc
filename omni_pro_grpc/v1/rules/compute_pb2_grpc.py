# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni_pro_grpc.v1.rules import compute_pb2 as v1_dot_rules_dot_compute__pb2


class ComputeServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ComputeCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.compute.ComputeService/ComputeCreate",
            request_serializer=v1_dot_rules_dot_compute__pb2.ComputeCreateRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_compute__pb2.ComputeCreateResponse.FromString,
        )
        self.ComputeRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.compute.ComputeService/ComputeRead",
            request_serializer=v1_dot_rules_dot_compute__pb2.ComputeReadRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_compute__pb2.ComputeReadResponse.FromString,
        )
        self.ComputeUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.compute.ComputeService/ComputeUpdate",
            request_serializer=v1_dot_rules_dot_compute__pb2.ComputeUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_compute__pb2.ComputeUpdateResponse.FromString,
        )
        self.ComputeDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.compute.ComputeService/ComputeDelete",
            request_serializer=v1_dot_rules_dot_compute__pb2.ComputeDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_compute__pb2.ComputeDeleteResponse.FromString,
        )


class ComputeServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ComputeCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ComputeRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ComputeUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ComputeDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ComputeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ComputeCreate": grpc.unary_unary_rpc_method_handler(
            servicer.ComputeCreate,
            request_deserializer=v1_dot_rules_dot_compute__pb2.ComputeCreateRequest.FromString,
            response_serializer=v1_dot_rules_dot_compute__pb2.ComputeCreateResponse.SerializeToString,
        ),
        "ComputeRead": grpc.unary_unary_rpc_method_handler(
            servicer.ComputeRead,
            request_deserializer=v1_dot_rules_dot_compute__pb2.ComputeReadRequest.FromString,
            response_serializer=v1_dot_rules_dot_compute__pb2.ComputeReadResponse.SerializeToString,
        ),
        "ComputeUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.ComputeUpdate,
            request_deserializer=v1_dot_rules_dot_compute__pb2.ComputeUpdateRequest.FromString,
            response_serializer=v1_dot_rules_dot_compute__pb2.ComputeUpdateResponse.SerializeToString,
        ),
        "ComputeDelete": grpc.unary_unary_rpc_method_handler(
            servicer.ComputeDelete,
            request_deserializer=v1_dot_rules_dot_compute__pb2.ComputeDeleteRequest.FromString,
            response_serializer=v1_dot_rules_dot_compute__pb2.ComputeDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.rules.compute.ComputeService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class ComputeService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ComputeCreate(
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
            "/pro.omni.oms.api.v1.rules.compute.ComputeService/ComputeCreate",
            v1_dot_rules_dot_compute__pb2.ComputeCreateRequest.SerializeToString,
            v1_dot_rules_dot_compute__pb2.ComputeCreateResponse.FromString,
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
    def ComputeRead(
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
            "/pro.omni.oms.api.v1.rules.compute.ComputeService/ComputeRead",
            v1_dot_rules_dot_compute__pb2.ComputeReadRequest.SerializeToString,
            v1_dot_rules_dot_compute__pb2.ComputeReadResponse.FromString,
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
    def ComputeUpdate(
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
            "/pro.omni.oms.api.v1.rules.compute.ComputeService/ComputeUpdate",
            v1_dot_rules_dot_compute__pb2.ComputeUpdateRequest.SerializeToString,
            v1_dot_rules_dot_compute__pb2.ComputeUpdateResponse.FromString,
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
    def ComputeDelete(
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
            "/pro.omni.oms.api.v1.rules.compute.ComputeService/ComputeDelete",
            v1_dot_rules_dot_compute__pb2.ComputeDeleteRequest.SerializeToString,
            v1_dot_rules_dot_compute__pb2.ComputeDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
