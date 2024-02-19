# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from omni_pro_grpc.v1.rules import schedule_work_line_pb2 as v1_dot_rules_dot_schedule__work__line__pb2


class ScheduleWorkLineServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ScheduleWorkLineCreate = channel.unary_unary(
                '/pro.omni.oms.api.v1.rules.schedule_work_line.ScheduleWorkLineService/ScheduleWorkLineCreate',
                request_serializer=v1_dot_rules_dot_schedule__work__line__pb2.ScheduleWorkLineCreateRequest.SerializeToString,
                response_deserializer=v1_dot_rules_dot_schedule__work__line__pb2.ScheduleWorkLineCreateResponse.FromString,
                )
        self.ScheduleWorkLineRead = channel.unary_unary(
                '/pro.omni.oms.api.v1.rules.schedule_work_line.ScheduleWorkLineService/ScheduleWorkLineRead',
                request_serializer=v1_dot_rules_dot_schedule__work__line__pb2.ScheduleWorkLineReadRequest.SerializeToString,
                response_deserializer=v1_dot_rules_dot_schedule__work__line__pb2.ScheduleWorkLineReadResponse.FromString,
                )
        self.ScheduleWorkLineUpdate = channel.unary_unary(
                '/pro.omni.oms.api.v1.rules.schedule_work_line.ScheduleWorkLineService/ScheduleWorkLineUpdate',
                request_serializer=v1_dot_rules_dot_schedule__work__line__pb2.ScheduleWorkLineUpdateRequest.SerializeToString,
                response_deserializer=v1_dot_rules_dot_schedule__work__line__pb2.ScheduleWorkLineUpdateResponse.FromString,
                )
        self.ScheduleWorkLineDelete = channel.unary_unary(
                '/pro.omni.oms.api.v1.rules.schedule_work_line.ScheduleWorkLineService/ScheduleWorkLineDelete',
                request_serializer=v1_dot_rules_dot_schedule__work__line__pb2.ScheduleWorkLineDeleteRequest.SerializeToString,
                response_deserializer=v1_dot_rules_dot_schedule__work__line__pb2.ScheduleWorkLineDeleteResponse.FromString,
                )


class ScheduleWorkLineServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ScheduleWorkLineCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ScheduleWorkLineRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ScheduleWorkLineUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ScheduleWorkLineDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ScheduleWorkLineServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ScheduleWorkLineCreate': grpc.unary_unary_rpc_method_handler(
                    servicer.ScheduleWorkLineCreate,
                    request_deserializer=v1_dot_rules_dot_schedule__work__line__pb2.ScheduleWorkLineCreateRequest.FromString,
                    response_serializer=v1_dot_rules_dot_schedule__work__line__pb2.ScheduleWorkLineCreateResponse.SerializeToString,
            ),
            'ScheduleWorkLineRead': grpc.unary_unary_rpc_method_handler(
                    servicer.ScheduleWorkLineRead,
                    request_deserializer=v1_dot_rules_dot_schedule__work__line__pb2.ScheduleWorkLineReadRequest.FromString,
                    response_serializer=v1_dot_rules_dot_schedule__work__line__pb2.ScheduleWorkLineReadResponse.SerializeToString,
            ),
            'ScheduleWorkLineUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.ScheduleWorkLineUpdate,
                    request_deserializer=v1_dot_rules_dot_schedule__work__line__pb2.ScheduleWorkLineUpdateRequest.FromString,
                    response_serializer=v1_dot_rules_dot_schedule__work__line__pb2.ScheduleWorkLineUpdateResponse.SerializeToString,
            ),
            'ScheduleWorkLineDelete': grpc.unary_unary_rpc_method_handler(
                    servicer.ScheduleWorkLineDelete,
                    request_deserializer=v1_dot_rules_dot_schedule__work__line__pb2.ScheduleWorkLineDeleteRequest.FromString,
                    response_serializer=v1_dot_rules_dot_schedule__work__line__pb2.ScheduleWorkLineDeleteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pro.omni.oms.api.v1.rules.schedule_work_line.ScheduleWorkLineService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ScheduleWorkLineService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ScheduleWorkLineCreate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.rules.schedule_work_line.ScheduleWorkLineService/ScheduleWorkLineCreate',
            v1_dot_rules_dot_schedule__work__line__pb2.ScheduleWorkLineCreateRequest.SerializeToString,
            v1_dot_rules_dot_schedule__work__line__pb2.ScheduleWorkLineCreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ScheduleWorkLineRead(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.rules.schedule_work_line.ScheduleWorkLineService/ScheduleWorkLineRead',
            v1_dot_rules_dot_schedule__work__line__pb2.ScheduleWorkLineReadRequest.SerializeToString,
            v1_dot_rules_dot_schedule__work__line__pb2.ScheduleWorkLineReadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ScheduleWorkLineUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.rules.schedule_work_line.ScheduleWorkLineService/ScheduleWorkLineUpdate',
            v1_dot_rules_dot_schedule__work__line__pb2.ScheduleWorkLineUpdateRequest.SerializeToString,
            v1_dot_rules_dot_schedule__work__line__pb2.ScheduleWorkLineUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ScheduleWorkLineDelete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.rules.schedule_work_line.ScheduleWorkLineService/ScheduleWorkLineDelete',
            v1_dot_rules_dot_schedule__work__line__pb2.ScheduleWorkLineDeleteRequest.SerializeToString,
            v1_dot_rules_dot_schedule__work__line__pb2.ScheduleWorkLineDeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
