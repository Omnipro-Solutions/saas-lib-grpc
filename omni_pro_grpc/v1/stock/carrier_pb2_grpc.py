# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from omni_pro_grpc.v1.stock import carrier_pb2 as v1_dot_stock_dot_carrier__pb2


class CarrierServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CarrierCreate = channel.unary_unary(
                '/pro.omni.oms.api.v1.stock.carrier.CarrierService/CarrierCreate',
                request_serializer=v1_dot_stock_dot_carrier__pb2.CarrierCreateRequest.SerializeToString,
                response_deserializer=v1_dot_stock_dot_carrier__pb2.CarrierCreateResponse.FromString,
                )
        self.CarrierRead = channel.unary_unary(
                '/pro.omni.oms.api.v1.stock.carrier.CarrierService/CarrierRead',
                request_serializer=v1_dot_stock_dot_carrier__pb2.CarrierReadRequest.SerializeToString,
                response_deserializer=v1_dot_stock_dot_carrier__pb2.CarrierReadResponse.FromString,
                )
        self.CarrierUpdate = channel.unary_unary(
                '/pro.omni.oms.api.v1.stock.carrier.CarrierService/CarrierUpdate',
                request_serializer=v1_dot_stock_dot_carrier__pb2.CarrierUpdateRequest.SerializeToString,
                response_deserializer=v1_dot_stock_dot_carrier__pb2.CarrierUpdateResponse.FromString,
                )
        self.CarrierDelete = channel.unary_unary(
                '/pro.omni.oms.api.v1.stock.carrier.CarrierService/CarrierDelete',
                request_serializer=v1_dot_stock_dot_carrier__pb2.CarrierDeleteRequest.SerializeToString,
                response_deserializer=v1_dot_stock_dot_carrier__pb2.CarrierDeleteResponse.FromString,
                )


class CarrierServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CarrierCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CarrierRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CarrierUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CarrierDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CarrierServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CarrierCreate': grpc.unary_unary_rpc_method_handler(
                    servicer.CarrierCreate,
                    request_deserializer=v1_dot_stock_dot_carrier__pb2.CarrierCreateRequest.FromString,
                    response_serializer=v1_dot_stock_dot_carrier__pb2.CarrierCreateResponse.SerializeToString,
            ),
            'CarrierRead': grpc.unary_unary_rpc_method_handler(
                    servicer.CarrierRead,
                    request_deserializer=v1_dot_stock_dot_carrier__pb2.CarrierReadRequest.FromString,
                    response_serializer=v1_dot_stock_dot_carrier__pb2.CarrierReadResponse.SerializeToString,
            ),
            'CarrierUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.CarrierUpdate,
                    request_deserializer=v1_dot_stock_dot_carrier__pb2.CarrierUpdateRequest.FromString,
                    response_serializer=v1_dot_stock_dot_carrier__pb2.CarrierUpdateResponse.SerializeToString,
            ),
            'CarrierDelete': grpc.unary_unary_rpc_method_handler(
                    servicer.CarrierDelete,
                    request_deserializer=v1_dot_stock_dot_carrier__pb2.CarrierDeleteRequest.FromString,
                    response_serializer=v1_dot_stock_dot_carrier__pb2.CarrierDeleteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pro.omni.oms.api.v1.stock.carrier.CarrierService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CarrierService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CarrierCreate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.stock.carrier.CarrierService/CarrierCreate',
            v1_dot_stock_dot_carrier__pb2.CarrierCreateRequest.SerializeToString,
            v1_dot_stock_dot_carrier__pb2.CarrierCreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CarrierRead(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.stock.carrier.CarrierService/CarrierRead',
            v1_dot_stock_dot_carrier__pb2.CarrierReadRequest.SerializeToString,
            v1_dot_stock_dot_carrier__pb2.CarrierReadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CarrierUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.stock.carrier.CarrierService/CarrierUpdate',
            v1_dot_stock_dot_carrier__pb2.CarrierUpdateRequest.SerializeToString,
            v1_dot_stock_dot_carrier__pb2.CarrierUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CarrierDelete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.stock.carrier.CarrierService/CarrierDelete',
            v1_dot_stock_dot_carrier__pb2.CarrierDeleteRequest.SerializeToString,
            v1_dot_stock_dot_carrier__pb2.CarrierDeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
