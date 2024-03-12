# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni_pro_grpc.v1.sales import flow_pb2 as v1_dot_sales_dot_flow__pb2


class FlowServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.FlowCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.flow.FlowService/FlowCreate",
            request_serializer=v1_dot_sales_dot_flow__pb2.FlowCreateRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_flow__pb2.FlowCreateResponse.FromString,
        )
        self.FlowRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.flow.FlowService/FlowRead",
            request_serializer=v1_dot_sales_dot_flow__pb2.FlowReadRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_flow__pb2.FlowReadResponse.FromString,
        )
        self.FlowUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.flow.FlowService/FlowUpdate",
            request_serializer=v1_dot_sales_dot_flow__pb2.FlowUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_flow__pb2.FlowUpdateResponse.FromString,
        )
        self.FlowDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.flow.FlowService/FlowDelete",
            request_serializer=v1_dot_sales_dot_flow__pb2.FlowDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_flow__pb2.FlowDeleteResponse.FromString,
        )
        self.FlowChangeState = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.flow.FlowService/FlowChangeState",
            request_serializer=v1_dot_sales_dot_flow__pb2.FlowChangeStateRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_flow__pb2.FlowChangeStateResponse.FromString,
        )


class FlowServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def FlowCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def FlowRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def FlowUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def FlowDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def FlowChangeState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_FlowServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "FlowCreate": grpc.unary_unary_rpc_method_handler(
            servicer.FlowCreate,
            request_deserializer=v1_dot_sales_dot_flow__pb2.FlowCreateRequest.FromString,
            response_serializer=v1_dot_sales_dot_flow__pb2.FlowCreateResponse.SerializeToString,
        ),
        "FlowRead": grpc.unary_unary_rpc_method_handler(
            servicer.FlowRead,
            request_deserializer=v1_dot_sales_dot_flow__pb2.FlowReadRequest.FromString,
            response_serializer=v1_dot_sales_dot_flow__pb2.FlowReadResponse.SerializeToString,
        ),
        "FlowUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.FlowUpdate,
            request_deserializer=v1_dot_sales_dot_flow__pb2.FlowUpdateRequest.FromString,
            response_serializer=v1_dot_sales_dot_flow__pb2.FlowUpdateResponse.SerializeToString,
        ),
        "FlowDelete": grpc.unary_unary_rpc_method_handler(
            servicer.FlowDelete,
            request_deserializer=v1_dot_sales_dot_flow__pb2.FlowDeleteRequest.FromString,
            response_serializer=v1_dot_sales_dot_flow__pb2.FlowDeleteResponse.SerializeToString,
        ),
        "FlowChangeState": grpc.unary_unary_rpc_method_handler(
            servicer.FlowChangeState,
            request_deserializer=v1_dot_sales_dot_flow__pb2.FlowChangeStateRequest.FromString,
            response_serializer=v1_dot_sales_dot_flow__pb2.FlowChangeStateResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.sales.flow.FlowService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class FlowService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def FlowCreate(
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
            "/pro.omni.oms.api.v1.sales.flow.FlowService/FlowCreate",
            v1_dot_sales_dot_flow__pb2.FlowCreateRequest.SerializeToString,
            v1_dot_sales_dot_flow__pb2.FlowCreateResponse.FromString,
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
    def FlowRead(
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
            "/pro.omni.oms.api.v1.sales.flow.FlowService/FlowRead",
            v1_dot_sales_dot_flow__pb2.FlowReadRequest.SerializeToString,
            v1_dot_sales_dot_flow__pb2.FlowReadResponse.FromString,
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
    def FlowUpdate(
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
            "/pro.omni.oms.api.v1.sales.flow.FlowService/FlowUpdate",
            v1_dot_sales_dot_flow__pb2.FlowUpdateRequest.SerializeToString,
            v1_dot_sales_dot_flow__pb2.FlowUpdateResponse.FromString,
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
    def FlowDelete(
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
            "/pro.omni.oms.api.v1.sales.flow.FlowService/FlowDelete",
            v1_dot_sales_dot_flow__pb2.FlowDeleteRequest.SerializeToString,
            v1_dot_sales_dot_flow__pb2.FlowDeleteResponse.FromString,
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
    def FlowChangeState(
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
            "/pro.omni.oms.api.v1.sales.flow.FlowService/FlowChangeState",
            v1_dot_sales_dot_flow__pb2.FlowChangeStateRequest.SerializeToString,
            v1_dot_sales_dot_flow__pb2.FlowChangeStateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
