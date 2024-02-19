# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from omni_pro_grpc.v1.utilities import sequence_pb2 as v1_dot_utilities_dot_sequence__pb2


class SequenceServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SequenceCreate = channel.unary_unary(
                '/pro.omni.oms.api.v1.utilities.sequence.SequenceService/SequenceCreate',
                request_serializer=v1_dot_utilities_dot_sequence__pb2.SequenceCreateRequest.SerializeToString,
                response_deserializer=v1_dot_utilities_dot_sequence__pb2.SequenceCreateResponse.FromString,
                )
        self.SequenceRead = channel.unary_unary(
                '/pro.omni.oms.api.v1.utilities.sequence.SequenceService/SequenceRead',
                request_serializer=v1_dot_utilities_dot_sequence__pb2.SequenceReadRequest.SerializeToString,
                response_deserializer=v1_dot_utilities_dot_sequence__pb2.SequenceReadResponse.FromString,
                )
        self.SequenceUpdate = channel.unary_unary(
                '/pro.omni.oms.api.v1.utilities.sequence.SequenceService/SequenceUpdate',
                request_serializer=v1_dot_utilities_dot_sequence__pb2.SequenceUpdateRequest.SerializeToString,
                response_deserializer=v1_dot_utilities_dot_sequence__pb2.SequenceUpdateResponse.FromString,
                )
        self.SequenceDelete = channel.unary_unary(
                '/pro.omni.oms.api.v1.utilities.sequence.SequenceService/SequenceDelete',
                request_serializer=v1_dot_utilities_dot_sequence__pb2.SequenceDeleteRequest.SerializeToString,
                response_deserializer=v1_dot_utilities_dot_sequence__pb2.SequenceDeleteResponse.FromString,
                )
        self.NextById = channel.unary_unary(
                '/pro.omni.oms.api.v1.utilities.sequence.SequenceService/NextById',
                request_serializer=v1_dot_utilities_dot_sequence__pb2.NextByIdRequest.SerializeToString,
                response_deserializer=v1_dot_utilities_dot_sequence__pb2.NextResponse.FromString,
                )
        self.NextByCode = channel.unary_unary(
                '/pro.omni.oms.api.v1.utilities.sequence.SequenceService/NextByCode',
                request_serializer=v1_dot_utilities_dot_sequence__pb2.NextByCodeRequest.SerializeToString,
                response_deserializer=v1_dot_utilities_dot_sequence__pb2.NextResponse.FromString,
                )


class SequenceServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SequenceCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SequenceRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SequenceUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SequenceDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NextById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NextByCode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SequenceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SequenceCreate': grpc.unary_unary_rpc_method_handler(
                    servicer.SequenceCreate,
                    request_deserializer=v1_dot_utilities_dot_sequence__pb2.SequenceCreateRequest.FromString,
                    response_serializer=v1_dot_utilities_dot_sequence__pb2.SequenceCreateResponse.SerializeToString,
            ),
            'SequenceRead': grpc.unary_unary_rpc_method_handler(
                    servicer.SequenceRead,
                    request_deserializer=v1_dot_utilities_dot_sequence__pb2.SequenceReadRequest.FromString,
                    response_serializer=v1_dot_utilities_dot_sequence__pb2.SequenceReadResponse.SerializeToString,
            ),
            'SequenceUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.SequenceUpdate,
                    request_deserializer=v1_dot_utilities_dot_sequence__pb2.SequenceUpdateRequest.FromString,
                    response_serializer=v1_dot_utilities_dot_sequence__pb2.SequenceUpdateResponse.SerializeToString,
            ),
            'SequenceDelete': grpc.unary_unary_rpc_method_handler(
                    servicer.SequenceDelete,
                    request_deserializer=v1_dot_utilities_dot_sequence__pb2.SequenceDeleteRequest.FromString,
                    response_serializer=v1_dot_utilities_dot_sequence__pb2.SequenceDeleteResponse.SerializeToString,
            ),
            'NextById': grpc.unary_unary_rpc_method_handler(
                    servicer.NextById,
                    request_deserializer=v1_dot_utilities_dot_sequence__pb2.NextByIdRequest.FromString,
                    response_serializer=v1_dot_utilities_dot_sequence__pb2.NextResponse.SerializeToString,
            ),
            'NextByCode': grpc.unary_unary_rpc_method_handler(
                    servicer.NextByCode,
                    request_deserializer=v1_dot_utilities_dot_sequence__pb2.NextByCodeRequest.FromString,
                    response_serializer=v1_dot_utilities_dot_sequence__pb2.NextResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pro.omni.oms.api.v1.utilities.sequence.SequenceService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SequenceService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SequenceCreate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.utilities.sequence.SequenceService/SequenceCreate',
            v1_dot_utilities_dot_sequence__pb2.SequenceCreateRequest.SerializeToString,
            v1_dot_utilities_dot_sequence__pb2.SequenceCreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SequenceRead(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.utilities.sequence.SequenceService/SequenceRead',
            v1_dot_utilities_dot_sequence__pb2.SequenceReadRequest.SerializeToString,
            v1_dot_utilities_dot_sequence__pb2.SequenceReadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SequenceUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.utilities.sequence.SequenceService/SequenceUpdate',
            v1_dot_utilities_dot_sequence__pb2.SequenceUpdateRequest.SerializeToString,
            v1_dot_utilities_dot_sequence__pb2.SequenceUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SequenceDelete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.utilities.sequence.SequenceService/SequenceDelete',
            v1_dot_utilities_dot_sequence__pb2.SequenceDeleteRequest.SerializeToString,
            v1_dot_utilities_dot_sequence__pb2.SequenceDeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NextById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.utilities.sequence.SequenceService/NextById',
            v1_dot_utilities_dot_sequence__pb2.NextByIdRequest.SerializeToString,
            v1_dot_utilities_dot_sequence__pb2.NextResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NextByCode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.utilities.sequence.SequenceService/NextByCode',
            v1_dot_utilities_dot_sequence__pb2.NextByCodeRequest.SerializeToString,
            v1_dot_utilities_dot_sequence__pb2.NextResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
