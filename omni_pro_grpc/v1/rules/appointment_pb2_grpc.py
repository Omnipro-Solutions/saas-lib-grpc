# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni_pro_grpc.v1.rules import appointment_pb2 as v1_dot_rules_dot_appointment__pb2


class AppointmentServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AppointmentCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.appointment.AppointmentService/AppointmentCreate",
            request_serializer=v1_dot_rules_dot_appointment__pb2.AppointmentCreateRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_appointment__pb2.AppointmentCreateResponse.FromString,
        )
        self.AppointmentRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.appointment.AppointmentService/AppointmentRead",
            request_serializer=v1_dot_rules_dot_appointment__pb2.AppointmentReadRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_appointment__pb2.AppointmentReadResponse.FromString,
        )
        self.AppointmentUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.appointment.AppointmentService/AppointmentUpdate",
            request_serializer=v1_dot_rules_dot_appointment__pb2.AppointmentUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_appointment__pb2.AppointmentUpdateResponse.FromString,
        )
        self.AppointmentDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.appointment.AppointmentService/AppointmentDelete",
            request_serializer=v1_dot_rules_dot_appointment__pb2.AppointmentDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_appointment__pb2.AppointmentDeleteResponse.FromString,
        )
        self.SearchAppointment = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.appointment.AppointmentService/SearchAppointment",
            request_serializer=v1_dot_rules_dot_appointment__pb2.SearchAppointmentRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_appointment__pb2.SearchAppointmentResponse.FromString,
        )
        self.ConfirmAppointment = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.appointment.AppointmentService/ConfirmAppointment",
            request_serializer=v1_dot_rules_dot_appointment__pb2.ConfirmAppointmentRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_appointment__pb2.ConfirmAppointmentResponse.FromString,
        )


class AppointmentServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AppointmentCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AppointmentRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AppointmentUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AppointmentDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SearchAppointment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ConfirmAppointment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_AppointmentServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "AppointmentCreate": grpc.unary_unary_rpc_method_handler(
            servicer.AppointmentCreate,
            request_deserializer=v1_dot_rules_dot_appointment__pb2.AppointmentCreateRequest.FromString,
            response_serializer=v1_dot_rules_dot_appointment__pb2.AppointmentCreateResponse.SerializeToString,
        ),
        "AppointmentRead": grpc.unary_unary_rpc_method_handler(
            servicer.AppointmentRead,
            request_deserializer=v1_dot_rules_dot_appointment__pb2.AppointmentReadRequest.FromString,
            response_serializer=v1_dot_rules_dot_appointment__pb2.AppointmentReadResponse.SerializeToString,
        ),
        "AppointmentUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.AppointmentUpdate,
            request_deserializer=v1_dot_rules_dot_appointment__pb2.AppointmentUpdateRequest.FromString,
            response_serializer=v1_dot_rules_dot_appointment__pb2.AppointmentUpdateResponse.SerializeToString,
        ),
        "AppointmentDelete": grpc.unary_unary_rpc_method_handler(
            servicer.AppointmentDelete,
            request_deserializer=v1_dot_rules_dot_appointment__pb2.AppointmentDeleteRequest.FromString,
            response_serializer=v1_dot_rules_dot_appointment__pb2.AppointmentDeleteResponse.SerializeToString,
        ),
        "SearchAppointment": grpc.unary_unary_rpc_method_handler(
            servicer.SearchAppointment,
            request_deserializer=v1_dot_rules_dot_appointment__pb2.SearchAppointmentRequest.FromString,
            response_serializer=v1_dot_rules_dot_appointment__pb2.SearchAppointmentResponse.SerializeToString,
        ),
        "ConfirmAppointment": grpc.unary_unary_rpc_method_handler(
            servicer.ConfirmAppointment,
            request_deserializer=v1_dot_rules_dot_appointment__pb2.ConfirmAppointmentRequest.FromString,
            response_serializer=v1_dot_rules_dot_appointment__pb2.ConfirmAppointmentResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.rules.appointment.AppointmentService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class AppointmentService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AppointmentCreate(
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
            "/pro.omni.oms.api.v1.rules.appointment.AppointmentService/AppointmentCreate",
            v1_dot_rules_dot_appointment__pb2.AppointmentCreateRequest.SerializeToString,
            v1_dot_rules_dot_appointment__pb2.AppointmentCreateResponse.FromString,
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
    def AppointmentRead(
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
            "/pro.omni.oms.api.v1.rules.appointment.AppointmentService/AppointmentRead",
            v1_dot_rules_dot_appointment__pb2.AppointmentReadRequest.SerializeToString,
            v1_dot_rules_dot_appointment__pb2.AppointmentReadResponse.FromString,
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
    def AppointmentUpdate(
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
            "/pro.omni.oms.api.v1.rules.appointment.AppointmentService/AppointmentUpdate",
            v1_dot_rules_dot_appointment__pb2.AppointmentUpdateRequest.SerializeToString,
            v1_dot_rules_dot_appointment__pb2.AppointmentUpdateResponse.FromString,
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
    def AppointmentDelete(
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
            "/pro.omni.oms.api.v1.rules.appointment.AppointmentService/AppointmentDelete",
            v1_dot_rules_dot_appointment__pb2.AppointmentDeleteRequest.SerializeToString,
            v1_dot_rules_dot_appointment__pb2.AppointmentDeleteResponse.FromString,
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
    def SearchAppointment(
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
            "/pro.omni.oms.api.v1.rules.appointment.AppointmentService/SearchAppointment",
            v1_dot_rules_dot_appointment__pb2.SearchAppointmentRequest.SerializeToString,
            v1_dot_rules_dot_appointment__pb2.SearchAppointmentResponse.FromString,
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
    def ConfirmAppointment(
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
            "/pro.omni.oms.api.v1.rules.appointment.AppointmentService/ConfirmAppointment",
            v1_dot_rules_dot_appointment__pb2.ConfirmAppointmentRequest.SerializeToString,
            v1_dot_rules_dot_appointment__pb2.ConfirmAppointmentResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
