# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni_pro_grpc.v1.utilities import analytic_filter_pb2 as v1_dot_utilities_dot_analytic__filter__pb2


class AnalyticFilterServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AnalyticFilterCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.analytic_filter.AnalyticFilterService/AnalyticFilterCreate",
            request_serializer=v1_dot_utilities_dot_analytic__filter__pb2.AnalyticFilterCreateRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_analytic__filter__pb2.AnalyticFilterCreateResponse.FromString,
        )
        self.AnalyticFilterRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.analytic_filter.AnalyticFilterService/AnalyticFilterRead",
            request_serializer=v1_dot_utilities_dot_analytic__filter__pb2.AnalyticFilterReadRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_analytic__filter__pb2.AnalyticFilterReadResponse.FromString,
        )
        self.AnalyticFilterUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.analytic_filter.AnalyticFilterService/AnalyticFilterUpdate",
            request_serializer=v1_dot_utilities_dot_analytic__filter__pb2.AnalyticFilterUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_analytic__filter__pb2.AnalyticFilterUpdateResponse.FromString,
        )
        self.AnalyticFilterDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.analytic_filter.AnalyticFilterService/AnalyticFilterDelete",
            request_serializer=v1_dot_utilities_dot_analytic__filter__pb2.AnalyticFilterDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_analytic__filter__pb2.AnalyticFilterDeleteResponse.FromString,
        )


class AnalyticFilterServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AnalyticFilterCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AnalyticFilterRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AnalyticFilterUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AnalyticFilterDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_AnalyticFilterServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "AnalyticFilterCreate": grpc.unary_unary_rpc_method_handler(
            servicer.AnalyticFilterCreate,
            request_deserializer=v1_dot_utilities_dot_analytic__filter__pb2.AnalyticFilterCreateRequest.FromString,
            response_serializer=v1_dot_utilities_dot_analytic__filter__pb2.AnalyticFilterCreateResponse.SerializeToString,
        ),
        "AnalyticFilterRead": grpc.unary_unary_rpc_method_handler(
            servicer.AnalyticFilterRead,
            request_deserializer=v1_dot_utilities_dot_analytic__filter__pb2.AnalyticFilterReadRequest.FromString,
            response_serializer=v1_dot_utilities_dot_analytic__filter__pb2.AnalyticFilterReadResponse.SerializeToString,
        ),
        "AnalyticFilterUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.AnalyticFilterUpdate,
            request_deserializer=v1_dot_utilities_dot_analytic__filter__pb2.AnalyticFilterUpdateRequest.FromString,
            response_serializer=v1_dot_utilities_dot_analytic__filter__pb2.AnalyticFilterUpdateResponse.SerializeToString,
        ),
        "AnalyticFilterDelete": grpc.unary_unary_rpc_method_handler(
            servicer.AnalyticFilterDelete,
            request_deserializer=v1_dot_utilities_dot_analytic__filter__pb2.AnalyticFilterDeleteRequest.FromString,
            response_serializer=v1_dot_utilities_dot_analytic__filter__pb2.AnalyticFilterDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.utilities.analytic_filter.AnalyticFilterService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class AnalyticFilterService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AnalyticFilterCreate(
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
            "/pro.omni.oms.api.v1.utilities.analytic_filter.AnalyticFilterService/AnalyticFilterCreate",
            v1_dot_utilities_dot_analytic__filter__pb2.AnalyticFilterCreateRequest.SerializeToString,
            v1_dot_utilities_dot_analytic__filter__pb2.AnalyticFilterCreateResponse.FromString,
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
    def AnalyticFilterRead(
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
            "/pro.omni.oms.api.v1.utilities.analytic_filter.AnalyticFilterService/AnalyticFilterRead",
            v1_dot_utilities_dot_analytic__filter__pb2.AnalyticFilterReadRequest.SerializeToString,
            v1_dot_utilities_dot_analytic__filter__pb2.AnalyticFilterReadResponse.FromString,
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
    def AnalyticFilterUpdate(
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
            "/pro.omni.oms.api.v1.utilities.analytic_filter.AnalyticFilterService/AnalyticFilterUpdate",
            v1_dot_utilities_dot_analytic__filter__pb2.AnalyticFilterUpdateRequest.SerializeToString,
            v1_dot_utilities_dot_analytic__filter__pb2.AnalyticFilterUpdateResponse.FromString,
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
    def AnalyticFilterDelete(
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
            "/pro.omni.oms.api.v1.utilities.analytic_filter.AnalyticFilterService/AnalyticFilterDelete",
            v1_dot_utilities_dot_analytic__filter__pb2.AnalyticFilterDeleteRequest.SerializeToString,
            v1_dot_utilities_dot_analytic__filter__pb2.AnalyticFilterDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
