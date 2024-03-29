# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni_pro_grpc.v1.rules import schedule_work_pb2 as v1_dot_rules_dot_schedule__work__pb2


class ScheduleWorkServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ScheduleWorkCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.schedule_work.ScheduleWorkService/ScheduleWorkCreate",
            request_serializer=v1_dot_rules_dot_schedule__work__pb2.ScheduleWorkCreateRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_schedule__work__pb2.ScheduleWorkCreateResponse.FromString,
        )
        self.ScheduleWorkRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.schedule_work.ScheduleWorkService/ScheduleWorkRead",
            request_serializer=v1_dot_rules_dot_schedule__work__pb2.ScheduleWorkReadRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_schedule__work__pb2.ScheduleWorkReadResponse.FromString,
        )
        self.ScheduleWorkUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.schedule_work.ScheduleWorkService/ScheduleWorkUpdate",
            request_serializer=v1_dot_rules_dot_schedule__work__pb2.ScheduleWorkUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_schedule__work__pb2.ScheduleWorkUpdateResponse.FromString,
        )
        self.ScheduleWorkDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.schedule_work.ScheduleWorkService/ScheduleWorkDelete",
            request_serializer=v1_dot_rules_dot_schedule__work__pb2.ScheduleWorkDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_schedule__work__pb2.ScheduleWorkDeleteResponse.FromString,
        )
        self.AddScheduleWorkLine = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.schedule_work.ScheduleWorkService/AddScheduleWorkLine",
            request_serializer=v1_dot_rules_dot_schedule__work__pb2.AddScheduleWorkLineRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_schedule__work__pb2.AddScheduleWorkLineResponse.FromString,
        )
        self.RemoveScheduleWorkLine = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.schedule_work.ScheduleWorkService/RemoveScheduleWorkLine",
            request_serializer=v1_dot_rules_dot_schedule__work__pb2.RemoveScheduleWorkLineRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_schedule__work__pb2.RemoveScheduleWorkLineResponse.FromString,
        )


class ScheduleWorkServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ScheduleWorkCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ScheduleWorkRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ScheduleWorkUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ScheduleWorkDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AddScheduleWorkLine(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def RemoveScheduleWorkLine(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ScheduleWorkServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ScheduleWorkCreate": grpc.unary_unary_rpc_method_handler(
            servicer.ScheduleWorkCreate,
            request_deserializer=v1_dot_rules_dot_schedule__work__pb2.ScheduleWorkCreateRequest.FromString,
            response_serializer=v1_dot_rules_dot_schedule__work__pb2.ScheduleWorkCreateResponse.SerializeToString,
        ),
        "ScheduleWorkRead": grpc.unary_unary_rpc_method_handler(
            servicer.ScheduleWorkRead,
            request_deserializer=v1_dot_rules_dot_schedule__work__pb2.ScheduleWorkReadRequest.FromString,
            response_serializer=v1_dot_rules_dot_schedule__work__pb2.ScheduleWorkReadResponse.SerializeToString,
        ),
        "ScheduleWorkUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.ScheduleWorkUpdate,
            request_deserializer=v1_dot_rules_dot_schedule__work__pb2.ScheduleWorkUpdateRequest.FromString,
            response_serializer=v1_dot_rules_dot_schedule__work__pb2.ScheduleWorkUpdateResponse.SerializeToString,
        ),
        "ScheduleWorkDelete": grpc.unary_unary_rpc_method_handler(
            servicer.ScheduleWorkDelete,
            request_deserializer=v1_dot_rules_dot_schedule__work__pb2.ScheduleWorkDeleteRequest.FromString,
            response_serializer=v1_dot_rules_dot_schedule__work__pb2.ScheduleWorkDeleteResponse.SerializeToString,
        ),
        "AddScheduleWorkLine": grpc.unary_unary_rpc_method_handler(
            servicer.AddScheduleWorkLine,
            request_deserializer=v1_dot_rules_dot_schedule__work__pb2.AddScheduleWorkLineRequest.FromString,
            response_serializer=v1_dot_rules_dot_schedule__work__pb2.AddScheduleWorkLineResponse.SerializeToString,
        ),
        "RemoveScheduleWorkLine": grpc.unary_unary_rpc_method_handler(
            servicer.RemoveScheduleWorkLine,
            request_deserializer=v1_dot_rules_dot_schedule__work__pb2.RemoveScheduleWorkLineRequest.FromString,
            response_serializer=v1_dot_rules_dot_schedule__work__pb2.RemoveScheduleWorkLineResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.rules.schedule_work.ScheduleWorkService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class ScheduleWorkService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ScheduleWorkCreate(
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
            "/pro.omni.oms.api.v1.rules.schedule_work.ScheduleWorkService/ScheduleWorkCreate",
            v1_dot_rules_dot_schedule__work__pb2.ScheduleWorkCreateRequest.SerializeToString,
            v1_dot_rules_dot_schedule__work__pb2.ScheduleWorkCreateResponse.FromString,
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
    def ScheduleWorkRead(
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
            "/pro.omni.oms.api.v1.rules.schedule_work.ScheduleWorkService/ScheduleWorkRead",
            v1_dot_rules_dot_schedule__work__pb2.ScheduleWorkReadRequest.SerializeToString,
            v1_dot_rules_dot_schedule__work__pb2.ScheduleWorkReadResponse.FromString,
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
    def ScheduleWorkUpdate(
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
            "/pro.omni.oms.api.v1.rules.schedule_work.ScheduleWorkService/ScheduleWorkUpdate",
            v1_dot_rules_dot_schedule__work__pb2.ScheduleWorkUpdateRequest.SerializeToString,
            v1_dot_rules_dot_schedule__work__pb2.ScheduleWorkUpdateResponse.FromString,
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
    def ScheduleWorkDelete(
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
            "/pro.omni.oms.api.v1.rules.schedule_work.ScheduleWorkService/ScheduleWorkDelete",
            v1_dot_rules_dot_schedule__work__pb2.ScheduleWorkDeleteRequest.SerializeToString,
            v1_dot_rules_dot_schedule__work__pb2.ScheduleWorkDeleteResponse.FromString,
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
    def AddScheduleWorkLine(
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
            "/pro.omni.oms.api.v1.rules.schedule_work.ScheduleWorkService/AddScheduleWorkLine",
            v1_dot_rules_dot_schedule__work__pb2.AddScheduleWorkLineRequest.SerializeToString,
            v1_dot_rules_dot_schedule__work__pb2.AddScheduleWorkLineResponse.FromString,
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
    def RemoveScheduleWorkLine(
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
            "/pro.omni.oms.api.v1.rules.schedule_work.ScheduleWorkService/RemoveScheduleWorkLine",
            v1_dot_rules_dot_schedule__work__pb2.RemoveScheduleWorkLineRequest.SerializeToString,
            v1_dot_rules_dot_schedule__work__pb2.RemoveScheduleWorkLineResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
