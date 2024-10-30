# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni_pro_grpc.v1.tasks import solar_pb2 as v1_dot_tasks_dot_solar__pb2


class SolarServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SolarCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.tasks.solar.SolarService/SolarCreate",
            request_serializer=v1_dot_tasks_dot_solar__pb2.SolarCreateRequest.SerializeToString,
            response_deserializer=v1_dot_tasks_dot_solar__pb2.SolarCreateResponse.FromString,
        )
        self.SolarRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.tasks.solar.SolarService/SolarRead",
            request_serializer=v1_dot_tasks_dot_solar__pb2.SolarReadRequest.SerializeToString,
            response_deserializer=v1_dot_tasks_dot_solar__pb2.SolarReadResponse.FromString,
        )
        self.SolarUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.tasks.solar.SolarService/SolarUpdate",
            request_serializer=v1_dot_tasks_dot_solar__pb2.SolarUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_tasks_dot_solar__pb2.SolarUpdateResponse.FromString,
        )
        self.SolarDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.tasks.solar.SolarService/SolarDelete",
            request_serializer=v1_dot_tasks_dot_solar__pb2.SolarDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_tasks_dot_solar__pb2.SolarDeleteResponse.FromString,
        )


class SolarServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SolarCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SolarRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SolarUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SolarDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_SolarServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "SolarCreate": grpc.unary_unary_rpc_method_handler(
            servicer.SolarCreate,
            request_deserializer=v1_dot_tasks_dot_solar__pb2.SolarCreateRequest.FromString,
            response_serializer=v1_dot_tasks_dot_solar__pb2.SolarCreateResponse.SerializeToString,
        ),
        "SolarRead": grpc.unary_unary_rpc_method_handler(
            servicer.SolarRead,
            request_deserializer=v1_dot_tasks_dot_solar__pb2.SolarReadRequest.FromString,
            response_serializer=v1_dot_tasks_dot_solar__pb2.SolarReadResponse.SerializeToString,
        ),
        "SolarUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.SolarUpdate,
            request_deserializer=v1_dot_tasks_dot_solar__pb2.SolarUpdateRequest.FromString,
            response_serializer=v1_dot_tasks_dot_solar__pb2.SolarUpdateResponse.SerializeToString,
        ),
        "SolarDelete": grpc.unary_unary_rpc_method_handler(
            servicer.SolarDelete,
            request_deserializer=v1_dot_tasks_dot_solar__pb2.SolarDeleteRequest.FromString,
            response_serializer=v1_dot_tasks_dot_solar__pb2.SolarDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.tasks.solar.SolarService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class SolarService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SolarCreate(
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
            "/pro.omni.oms.api.v1.tasks.solar.SolarService/SolarCreate",
            v1_dot_tasks_dot_solar__pb2.SolarCreateRequest.SerializeToString,
            v1_dot_tasks_dot_solar__pb2.SolarCreateResponse.FromString,
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
    def SolarRead(
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
            "/pro.omni.oms.api.v1.tasks.solar.SolarService/SolarRead",
            v1_dot_tasks_dot_solar__pb2.SolarReadRequest.SerializeToString,
            v1_dot_tasks_dot_solar__pb2.SolarReadResponse.FromString,
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
    def SolarUpdate(
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
            "/pro.omni.oms.api.v1.tasks.solar.SolarService/SolarUpdate",
            v1_dot_tasks_dot_solar__pb2.SolarUpdateRequest.SerializeToString,
            v1_dot_tasks_dot_solar__pb2.SolarUpdateResponse.FromString,
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
    def SolarDelete(
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
            "/pro.omni.oms.api.v1.tasks.solar.SolarService/SolarDelete",
            v1_dot_tasks_dot_solar__pb2.SolarDeleteRequest.SerializeToString,
            v1_dot_tasks_dot_solar__pb2.SolarDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )