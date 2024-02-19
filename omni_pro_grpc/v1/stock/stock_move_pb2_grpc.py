# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from omni_pro_grpc.v1.stock import stock_move_pb2 as v1_dot_stock_dot_stock__move__pb2


class StockMoveServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StockMoveCreate = channel.unary_unary(
                '/pro.omni.oms.api.v1.stock.stock_move.StockMoveService/StockMoveCreate',
                request_serializer=v1_dot_stock_dot_stock__move__pb2.StockMoveCreateRequest.SerializeToString,
                response_deserializer=v1_dot_stock_dot_stock__move__pb2.StockMoveCreateResponse.FromString,
                )
        self.StockMoveRead = channel.unary_unary(
                '/pro.omni.oms.api.v1.stock.stock_move.StockMoveService/StockMoveRead',
                request_serializer=v1_dot_stock_dot_stock__move__pb2.StockMoveReadRequest.SerializeToString,
                response_deserializer=v1_dot_stock_dot_stock__move__pb2.StockMoveReadResponse.FromString,
                )
        self.StockMoveUpdate = channel.unary_unary(
                '/pro.omni.oms.api.v1.stock.stock_move.StockMoveService/StockMoveUpdate',
                request_serializer=v1_dot_stock_dot_stock__move__pb2.StockMoveUpdateRequest.SerializeToString,
                response_deserializer=v1_dot_stock_dot_stock__move__pb2.StockMoveUpdateResponse.FromString,
                )
        self.StockMoveDelete = channel.unary_unary(
                '/pro.omni.oms.api.v1.stock.stock_move.StockMoveService/StockMoveDelete',
                request_serializer=v1_dot_stock_dot_stock__move__pb2.StockMoveDeleteRequest.SerializeToString,
                response_deserializer=v1_dot_stock_dot_stock__move__pb2.StockMoveDeleteResponse.FromString,
                )


class StockMoveServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StockMoveCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StockMoveRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StockMoveUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StockMoveDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StockMoveServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StockMoveCreate': grpc.unary_unary_rpc_method_handler(
                    servicer.StockMoveCreate,
                    request_deserializer=v1_dot_stock_dot_stock__move__pb2.StockMoveCreateRequest.FromString,
                    response_serializer=v1_dot_stock_dot_stock__move__pb2.StockMoveCreateResponse.SerializeToString,
            ),
            'StockMoveRead': grpc.unary_unary_rpc_method_handler(
                    servicer.StockMoveRead,
                    request_deserializer=v1_dot_stock_dot_stock__move__pb2.StockMoveReadRequest.FromString,
                    response_serializer=v1_dot_stock_dot_stock__move__pb2.StockMoveReadResponse.SerializeToString,
            ),
            'StockMoveUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.StockMoveUpdate,
                    request_deserializer=v1_dot_stock_dot_stock__move__pb2.StockMoveUpdateRequest.FromString,
                    response_serializer=v1_dot_stock_dot_stock__move__pb2.StockMoveUpdateResponse.SerializeToString,
            ),
            'StockMoveDelete': grpc.unary_unary_rpc_method_handler(
                    servicer.StockMoveDelete,
                    request_deserializer=v1_dot_stock_dot_stock__move__pb2.StockMoveDeleteRequest.FromString,
                    response_serializer=v1_dot_stock_dot_stock__move__pb2.StockMoveDeleteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pro.omni.oms.api.v1.stock.stock_move.StockMoveService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StockMoveService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StockMoveCreate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.stock.stock_move.StockMoveService/StockMoveCreate',
            v1_dot_stock_dot_stock__move__pb2.StockMoveCreateRequest.SerializeToString,
            v1_dot_stock_dot_stock__move__pb2.StockMoveCreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StockMoveRead(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.stock.stock_move.StockMoveService/StockMoveRead',
            v1_dot_stock_dot_stock__move__pb2.StockMoveReadRequest.SerializeToString,
            v1_dot_stock_dot_stock__move__pb2.StockMoveReadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StockMoveUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.stock.stock_move.StockMoveService/StockMoveUpdate',
            v1_dot_stock_dot_stock__move__pb2.StockMoveUpdateRequest.SerializeToString,
            v1_dot_stock_dot_stock__move__pb2.StockMoveUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StockMoveDelete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.stock.stock_move.StockMoveService/StockMoveDelete',
            v1_dot_stock_dot_stock__move__pb2.StockMoveDeleteRequest.SerializeToString,
            v1_dot_stock_dot_stock__move__pb2.StockMoveDeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
