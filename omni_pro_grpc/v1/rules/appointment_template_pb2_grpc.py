# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from omni_pro_grpc.v1.rules import appointment_template_pb2 as v1_dot_rules_dot_appointment__template__pb2


class AppointmentTemplateServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AppointmentTemplateCreate = channel.unary_unary(
                '/pro.omni.oms.api.v1.rules.appointment_template.AppointmentTemplateService/AppointmentTemplateCreate',
                request_serializer=v1_dot_rules_dot_appointment__template__pb2.AppointmentTemplateCreateRequest.SerializeToString,
                response_deserializer=v1_dot_rules_dot_appointment__template__pb2.AppointmentTemplateCreateResponse.FromString,
                )
        self.AppointmentTemplateRead = channel.unary_unary(
                '/pro.omni.oms.api.v1.rules.appointment_template.AppointmentTemplateService/AppointmentTemplateRead',
                request_serializer=v1_dot_rules_dot_appointment__template__pb2.AppointmentTemplateReadRequest.SerializeToString,
                response_deserializer=v1_dot_rules_dot_appointment__template__pb2.AppointmentTemplateReadResponse.FromString,
                )
        self.AppointmentTemplateUpdate = channel.unary_unary(
                '/pro.omni.oms.api.v1.rules.appointment_template.AppointmentTemplateService/AppointmentTemplateUpdate',
                request_serializer=v1_dot_rules_dot_appointment__template__pb2.AppointmentTemplateUpdateRequest.SerializeToString,
                response_deserializer=v1_dot_rules_dot_appointment__template__pb2.AppointmentTemplateUpdateResponse.FromString,
                )
        self.AppointmentTemplateDelete = channel.unary_unary(
                '/pro.omni.oms.api.v1.rules.appointment_template.AppointmentTemplateService/AppointmentTemplateDelete',
                request_serializer=v1_dot_rules_dot_appointment__template__pb2.AppointmentTemplateDeleteRequest.SerializeToString,
                response_deserializer=v1_dot_rules_dot_appointment__template__pb2.AppointmentTemplateDeleteResponse.FromString,
                )


class AppointmentTemplateServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AppointmentTemplateCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AppointmentTemplateRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AppointmentTemplateUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AppointmentTemplateDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AppointmentTemplateServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AppointmentTemplateCreate': grpc.unary_unary_rpc_method_handler(
                    servicer.AppointmentTemplateCreate,
                    request_deserializer=v1_dot_rules_dot_appointment__template__pb2.AppointmentTemplateCreateRequest.FromString,
                    response_serializer=v1_dot_rules_dot_appointment__template__pb2.AppointmentTemplateCreateResponse.SerializeToString,
            ),
            'AppointmentTemplateRead': grpc.unary_unary_rpc_method_handler(
                    servicer.AppointmentTemplateRead,
                    request_deserializer=v1_dot_rules_dot_appointment__template__pb2.AppointmentTemplateReadRequest.FromString,
                    response_serializer=v1_dot_rules_dot_appointment__template__pb2.AppointmentTemplateReadResponse.SerializeToString,
            ),
            'AppointmentTemplateUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.AppointmentTemplateUpdate,
                    request_deserializer=v1_dot_rules_dot_appointment__template__pb2.AppointmentTemplateUpdateRequest.FromString,
                    response_serializer=v1_dot_rules_dot_appointment__template__pb2.AppointmentTemplateUpdateResponse.SerializeToString,
            ),
            'AppointmentTemplateDelete': grpc.unary_unary_rpc_method_handler(
                    servicer.AppointmentTemplateDelete,
                    request_deserializer=v1_dot_rules_dot_appointment__template__pb2.AppointmentTemplateDeleteRequest.FromString,
                    response_serializer=v1_dot_rules_dot_appointment__template__pb2.AppointmentTemplateDeleteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pro.omni.oms.api.v1.rules.appointment_template.AppointmentTemplateService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AppointmentTemplateService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AppointmentTemplateCreate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.rules.appointment_template.AppointmentTemplateService/AppointmentTemplateCreate',
            v1_dot_rules_dot_appointment__template__pb2.AppointmentTemplateCreateRequest.SerializeToString,
            v1_dot_rules_dot_appointment__template__pb2.AppointmentTemplateCreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AppointmentTemplateRead(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.rules.appointment_template.AppointmentTemplateService/AppointmentTemplateRead',
            v1_dot_rules_dot_appointment__template__pb2.AppointmentTemplateReadRequest.SerializeToString,
            v1_dot_rules_dot_appointment__template__pb2.AppointmentTemplateReadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AppointmentTemplateUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.rules.appointment_template.AppointmentTemplateService/AppointmentTemplateUpdate',
            v1_dot_rules_dot_appointment__template__pb2.AppointmentTemplateUpdateRequest.SerializeToString,
            v1_dot_rules_dot_appointment__template__pb2.AppointmentTemplateUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AppointmentTemplateDelete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.rules.appointment_template.AppointmentTemplateService/AppointmentTemplateDelete',
            v1_dot_rules_dot_appointment__template__pb2.AppointmentTemplateDeleteRequest.SerializeToString,
            v1_dot_rules_dot_appointment__template__pb2.AppointmentTemplateDeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
