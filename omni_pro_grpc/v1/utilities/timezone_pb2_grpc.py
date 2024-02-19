# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from omni_pro_grpc.v1.utilities import timezone_pb2 as v1_dot_utilities_dot_timezone__pb2


class TimezoneServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TimezoneAdd = channel.unary_unary(
                '/pro.omni.oms.api.v1.utilities.timezone.TimezoneService/TimezoneAdd',
                request_serializer=v1_dot_utilities_dot_timezone__pb2.TimezoneAddRequest.SerializeToString,
                response_deserializer=v1_dot_utilities_dot_timezone__pb2.TimezoneAddResponse.FromString,
                )
        self.TimezoneRead = channel.unary_unary(
                '/pro.omni.oms.api.v1.utilities.timezone.TimezoneService/TimezoneRead',
                request_serializer=v1_dot_utilities_dot_timezone__pb2.TimezoneReadRequest.SerializeToString,
                response_deserializer=v1_dot_utilities_dot_timezone__pb2.TimezoneReadResponse.FromString,
                )
        self.TimezoneUpdate = channel.unary_unary(
                '/pro.omni.oms.api.v1.utilities.timezone.TimezoneService/TimezoneUpdate',
                request_serializer=v1_dot_utilities_dot_timezone__pb2.TimezoneUpdateRequest.SerializeToString,
                response_deserializer=v1_dot_utilities_dot_timezone__pb2.TimezoneUpdateResponse.FromString,
                )
        self.TimezoneDelete = channel.unary_unary(
                '/pro.omni.oms.api.v1.utilities.timezone.TimezoneService/TimezoneDelete',
                request_serializer=v1_dot_utilities_dot_timezone__pb2.TimezoneDeleteRequest.SerializeToString,
                response_deserializer=v1_dot_utilities_dot_timezone__pb2.TimezoneDeleteResponse.FromString,
                )


class TimezoneServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def TimezoneAdd(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TimezoneRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TimezoneUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TimezoneDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TimezoneServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'TimezoneAdd': grpc.unary_unary_rpc_method_handler(
                    servicer.TimezoneAdd,
                    request_deserializer=v1_dot_utilities_dot_timezone__pb2.TimezoneAddRequest.FromString,
                    response_serializer=v1_dot_utilities_dot_timezone__pb2.TimezoneAddResponse.SerializeToString,
            ),
            'TimezoneRead': grpc.unary_unary_rpc_method_handler(
                    servicer.TimezoneRead,
                    request_deserializer=v1_dot_utilities_dot_timezone__pb2.TimezoneReadRequest.FromString,
                    response_serializer=v1_dot_utilities_dot_timezone__pb2.TimezoneReadResponse.SerializeToString,
            ),
            'TimezoneUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.TimezoneUpdate,
                    request_deserializer=v1_dot_utilities_dot_timezone__pb2.TimezoneUpdateRequest.FromString,
                    response_serializer=v1_dot_utilities_dot_timezone__pb2.TimezoneUpdateResponse.SerializeToString,
            ),
            'TimezoneDelete': grpc.unary_unary_rpc_method_handler(
                    servicer.TimezoneDelete,
                    request_deserializer=v1_dot_utilities_dot_timezone__pb2.TimezoneDeleteRequest.FromString,
                    response_serializer=v1_dot_utilities_dot_timezone__pb2.TimezoneDeleteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pro.omni.oms.api.v1.utilities.timezone.TimezoneService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TimezoneService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def TimezoneAdd(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.utilities.timezone.TimezoneService/TimezoneAdd',
            v1_dot_utilities_dot_timezone__pb2.TimezoneAddRequest.SerializeToString,
            v1_dot_utilities_dot_timezone__pb2.TimezoneAddResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TimezoneRead(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.utilities.timezone.TimezoneService/TimezoneRead',
            v1_dot_utilities_dot_timezone__pb2.TimezoneReadRequest.SerializeToString,
            v1_dot_utilities_dot_timezone__pb2.TimezoneReadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TimezoneUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.utilities.timezone.TimezoneService/TimezoneUpdate',
            v1_dot_utilities_dot_timezone__pb2.TimezoneUpdateRequest.SerializeToString,
            v1_dot_utilities_dot_timezone__pb2.TimezoneUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TimezoneDelete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.utilities.timezone.TimezoneService/TimezoneDelete',
            v1_dot_utilities_dot_timezone__pb2.TimezoneDeleteRequest.SerializeToString,
            v1_dot_utilities_dot_timezone__pb2.TimezoneDeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
