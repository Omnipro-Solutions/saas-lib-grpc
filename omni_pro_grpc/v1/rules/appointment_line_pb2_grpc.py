# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from omni_pro_grpc.v1.rules import appointment_line_pb2 as v1_dot_rules_dot_appointment__line__pb2


class AppointmentLineServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AppointmentLineCreate = channel.unary_unary(
                '/pro.omni.oms.api.v1.rules.appointment_line.AppointmentLineService/AppointmentLineCreate',
                request_serializer=v1_dot_rules_dot_appointment__line__pb2.AppointmentLineCreateRequest.SerializeToString,
                response_deserializer=v1_dot_rules_dot_appointment__line__pb2.AppointmentLineCreateResponse.FromString,
                )
        self.AppointmentLineRead = channel.unary_unary(
                '/pro.omni.oms.api.v1.rules.appointment_line.AppointmentLineService/AppointmentLineRead',
                request_serializer=v1_dot_rules_dot_appointment__line__pb2.AppointmentLineReadRequest.SerializeToString,
                response_deserializer=v1_dot_rules_dot_appointment__line__pb2.AppointmentLineReadResponse.FromString,
                )
        self.AppointmentLineUpdate = channel.unary_unary(
                '/pro.omni.oms.api.v1.rules.appointment_line.AppointmentLineService/AppointmentLineUpdate',
                request_serializer=v1_dot_rules_dot_appointment__line__pb2.AppointmentLineUpdateRequest.SerializeToString,
                response_deserializer=v1_dot_rules_dot_appointment__line__pb2.AppointmentLineUpdateResponse.FromString,
                )
        self.AppointmentLineDelete = channel.unary_unary(
                '/pro.omni.oms.api.v1.rules.appointment_line.AppointmentLineService/AppointmentLineDelete',
                request_serializer=v1_dot_rules_dot_appointment__line__pb2.AppointmentLineDeleteRequest.SerializeToString,
                response_deserializer=v1_dot_rules_dot_appointment__line__pb2.AppointmentLineDeleteResponse.FromString,
                )


class AppointmentLineServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AppointmentLineCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AppointmentLineRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AppointmentLineUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AppointmentLineDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AppointmentLineServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AppointmentLineCreate': grpc.unary_unary_rpc_method_handler(
                    servicer.AppointmentLineCreate,
                    request_deserializer=v1_dot_rules_dot_appointment__line__pb2.AppointmentLineCreateRequest.FromString,
                    response_serializer=v1_dot_rules_dot_appointment__line__pb2.AppointmentLineCreateResponse.SerializeToString,
            ),
            'AppointmentLineRead': grpc.unary_unary_rpc_method_handler(
                    servicer.AppointmentLineRead,
                    request_deserializer=v1_dot_rules_dot_appointment__line__pb2.AppointmentLineReadRequest.FromString,
                    response_serializer=v1_dot_rules_dot_appointment__line__pb2.AppointmentLineReadResponse.SerializeToString,
            ),
            'AppointmentLineUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.AppointmentLineUpdate,
                    request_deserializer=v1_dot_rules_dot_appointment__line__pb2.AppointmentLineUpdateRequest.FromString,
                    response_serializer=v1_dot_rules_dot_appointment__line__pb2.AppointmentLineUpdateResponse.SerializeToString,
            ),
            'AppointmentLineDelete': grpc.unary_unary_rpc_method_handler(
                    servicer.AppointmentLineDelete,
                    request_deserializer=v1_dot_rules_dot_appointment__line__pb2.AppointmentLineDeleteRequest.FromString,
                    response_serializer=v1_dot_rules_dot_appointment__line__pb2.AppointmentLineDeleteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pro.omni.oms.api.v1.rules.appointment_line.AppointmentLineService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AppointmentLineService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AppointmentLineCreate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.rules.appointment_line.AppointmentLineService/AppointmentLineCreate',
            v1_dot_rules_dot_appointment__line__pb2.AppointmentLineCreateRequest.SerializeToString,
            v1_dot_rules_dot_appointment__line__pb2.AppointmentLineCreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AppointmentLineRead(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.rules.appointment_line.AppointmentLineService/AppointmentLineRead',
            v1_dot_rules_dot_appointment__line__pb2.AppointmentLineReadRequest.SerializeToString,
            v1_dot_rules_dot_appointment__line__pb2.AppointmentLineReadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AppointmentLineUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.rules.appointment_line.AppointmentLineService/AppointmentLineUpdate',
            v1_dot_rules_dot_appointment__line__pb2.AppointmentLineUpdateRequest.SerializeToString,
            v1_dot_rules_dot_appointment__line__pb2.AppointmentLineUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AppointmentLineDelete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.rules.appointment_line.AppointmentLineService/AppointmentLineDelete',
            v1_dot_rules_dot_appointment__line__pb2.AppointmentLineDeleteRequest.SerializeToString,
            v1_dot_rules_dot_appointment__line__pb2.AppointmentLineDeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
