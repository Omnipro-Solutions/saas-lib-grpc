# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni_pro_grpc.v1.sales import uom_pb2 as v1_dot_sales_dot_uom__pb2


class UomServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UomCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.uom.UomService/UomCreate",
            request_serializer=v1_dot_sales_dot_uom__pb2.UomCreateRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_uom__pb2.UomCreateResponse.FromString,
        )
        self.UomRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.uom.UomService/UomRead",
            request_serializer=v1_dot_sales_dot_uom__pb2.UomReadRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_uom__pb2.UomReadResponse.FromString,
        )
        self.UomUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.uom.UomService/UomUpdate",
            request_serializer=v1_dot_sales_dot_uom__pb2.UomUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_uom__pb2.UomUpdateResponse.FromString,
        )
        self.UomDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.uom.UomService/UomDelete",
            request_serializer=v1_dot_sales_dot_uom__pb2.UomDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_uom__pb2.UomDeleteResponse.FromString,
        )


class UomServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UomCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UomRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UomUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UomDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_UomServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "UomCreate": grpc.unary_unary_rpc_method_handler(
            servicer.UomCreate,
            request_deserializer=v1_dot_sales_dot_uom__pb2.UomCreateRequest.FromString,
            response_serializer=v1_dot_sales_dot_uom__pb2.UomCreateResponse.SerializeToString,
        ),
        "UomRead": grpc.unary_unary_rpc_method_handler(
            servicer.UomRead,
            request_deserializer=v1_dot_sales_dot_uom__pb2.UomReadRequest.FromString,
            response_serializer=v1_dot_sales_dot_uom__pb2.UomReadResponse.SerializeToString,
        ),
        "UomUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.UomUpdate,
            request_deserializer=v1_dot_sales_dot_uom__pb2.UomUpdateRequest.FromString,
            response_serializer=v1_dot_sales_dot_uom__pb2.UomUpdateResponse.SerializeToString,
        ),
        "UomDelete": grpc.unary_unary_rpc_method_handler(
            servicer.UomDelete,
            request_deserializer=v1_dot_sales_dot_uom__pb2.UomDeleteRequest.FromString,
            response_serializer=v1_dot_sales_dot_uom__pb2.UomDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.sales.uom.UomService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class UomService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UomCreate(
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
            "/pro.omni.oms.api.v1.sales.uom.UomService/UomCreate",
            v1_dot_sales_dot_uom__pb2.UomCreateRequest.SerializeToString,
            v1_dot_sales_dot_uom__pb2.UomCreateResponse.FromString,
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
    def UomRead(
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
            "/pro.omni.oms.api.v1.sales.uom.UomService/UomRead",
            v1_dot_sales_dot_uom__pb2.UomReadRequest.SerializeToString,
            v1_dot_sales_dot_uom__pb2.UomReadResponse.FromString,
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
    def UomUpdate(
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
            "/pro.omni.oms.api.v1.sales.uom.UomService/UomUpdate",
            v1_dot_sales_dot_uom__pb2.UomUpdateRequest.SerializeToString,
            v1_dot_sales_dot_uom__pb2.UomUpdateResponse.FromString,
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
    def UomDelete(
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
            "/pro.omni.oms.api.v1.sales.uom.UomService/UomDelete",
            v1_dot_sales_dot_uom__pb2.UomDeleteRequest.SerializeToString,
            v1_dot_sales_dot_uom__pb2.UomDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
