# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni_pro_grpc.v1.utilities import export_pb2 as v1_dot_utilities_dot_export__pb2


class ExportServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ExportModel = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.export.ExportService/ExportModel",
            request_serializer=v1_dot_utilities_dot_export__pb2.ExportModelRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_export__pb2.ExportModelResponse.FromString,
        )


class ExportServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ExportModel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ExportServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ExportModel": grpc.unary_unary_rpc_method_handler(
            servicer.ExportModel,
            request_deserializer=v1_dot_utilities_dot_export__pb2.ExportModelRequest.FromString,
            response_serializer=v1_dot_utilities_dot_export__pb2.ExportModelResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.utilities.export.ExportService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class ExportService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ExportModel(
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
            "/pro.omni.oms.api.v1.utilities.export.ExportService/ExportModel",
            v1_dot_utilities_dot_export__pb2.ExportModelRequest.SerializeToString,
            v1_dot_utilities_dot_export__pb2.ExportModelResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
