# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni_pro_grpc.v1.tasks import periodic_task_pb2 as v1_dot_tasks_dot_periodic__task__pb2


class PeriodicTaskServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PeriodicTaskCreate = channel.unary_unary(
            "/pro.omni.oms.api.tasks.periodic_task.PeriodicTaskService/PeriodicTaskCreate",
            request_serializer=v1_dot_tasks_dot_periodic__task__pb2.PeriodicTaskCreateRequest.SerializeToString,
            response_deserializer=v1_dot_tasks_dot_periodic__task__pb2.PeriodicTaskCreateResponse.FromString,
        )
        self.PeriodicTaskRead = channel.unary_unary(
            "/pro.omni.oms.api.tasks.periodic_task.PeriodicTaskService/PeriodicTaskRead",
            request_serializer=v1_dot_tasks_dot_periodic__task__pb2.PeriodicTaskReadRequest.SerializeToString,
            response_deserializer=v1_dot_tasks_dot_periodic__task__pb2.PeriodicTaskReadResponse.FromString,
        )
        self.PeriodicTaskUpdate = channel.unary_unary(
            "/pro.omni.oms.api.tasks.periodic_task.PeriodicTaskService/PeriodicTaskUpdate",
            request_serializer=v1_dot_tasks_dot_periodic__task__pb2.PeriodicTaskUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_tasks_dot_periodic__task__pb2.PeriodicTaskUpdateResponse.FromString,
        )
        self.PeriodicTaskDelete = channel.unary_unary(
            "/pro.omni.oms.api.tasks.periodic_task.PeriodicTaskService/PeriodicTaskDelete",
            request_serializer=v1_dot_tasks_dot_periodic__task__pb2.PeriodicTaskDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_tasks_dot_periodic__task__pb2.PeriodicTaskDeleteResponse.FromString,
        )


class PeriodicTaskServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PeriodicTaskCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def PeriodicTaskRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def PeriodicTaskUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def PeriodicTaskDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_PeriodicTaskServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "PeriodicTaskCreate": grpc.unary_unary_rpc_method_handler(
            servicer.PeriodicTaskCreate,
            request_deserializer=v1_dot_tasks_dot_periodic__task__pb2.PeriodicTaskCreateRequest.FromString,
            response_serializer=v1_dot_tasks_dot_periodic__task__pb2.PeriodicTaskCreateResponse.SerializeToString,
        ),
        "PeriodicTaskRead": grpc.unary_unary_rpc_method_handler(
            servicer.PeriodicTaskRead,
            request_deserializer=v1_dot_tasks_dot_periodic__task__pb2.PeriodicTaskReadRequest.FromString,
            response_serializer=v1_dot_tasks_dot_periodic__task__pb2.PeriodicTaskReadResponse.SerializeToString,
        ),
        "PeriodicTaskUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.PeriodicTaskUpdate,
            request_deserializer=v1_dot_tasks_dot_periodic__task__pb2.PeriodicTaskUpdateRequest.FromString,
            response_serializer=v1_dot_tasks_dot_periodic__task__pb2.PeriodicTaskUpdateResponse.SerializeToString,
        ),
        "PeriodicTaskDelete": grpc.unary_unary_rpc_method_handler(
            servicer.PeriodicTaskDelete,
            request_deserializer=v1_dot_tasks_dot_periodic__task__pb2.PeriodicTaskDeleteRequest.FromString,
            response_serializer=v1_dot_tasks_dot_periodic__task__pb2.PeriodicTaskDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.tasks.periodic_task.PeriodicTaskService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class PeriodicTaskService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PeriodicTaskCreate(
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
            "/pro.omni.oms.api.tasks.periodic_task.PeriodicTaskService/PeriodicTaskCreate",
            v1_dot_tasks_dot_periodic__task__pb2.PeriodicTaskCreateRequest.SerializeToString,
            v1_dot_tasks_dot_periodic__task__pb2.PeriodicTaskCreateResponse.FromString,
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
    def PeriodicTaskRead(
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
            "/pro.omni.oms.api.tasks.periodic_task.PeriodicTaskService/PeriodicTaskRead",
            v1_dot_tasks_dot_periodic__task__pb2.PeriodicTaskReadRequest.SerializeToString,
            v1_dot_tasks_dot_periodic__task__pb2.PeriodicTaskReadResponse.FromString,
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
    def PeriodicTaskUpdate(
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
            "/pro.omni.oms.api.tasks.periodic_task.PeriodicTaskService/PeriodicTaskUpdate",
            v1_dot_tasks_dot_periodic__task__pb2.PeriodicTaskUpdateRequest.SerializeToString,
            v1_dot_tasks_dot_periodic__task__pb2.PeriodicTaskUpdateResponse.FromString,
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
    def PeriodicTaskDelete(
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
            "/pro.omni.oms.api.tasks.periodic_task.PeriodicTaskService/PeriodicTaskDelete",
            v1_dot_tasks_dot_periodic__task__pb2.PeriodicTaskDeleteRequest.SerializeToString,
            v1_dot_tasks_dot_periodic__task__pb2.PeriodicTaskDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )