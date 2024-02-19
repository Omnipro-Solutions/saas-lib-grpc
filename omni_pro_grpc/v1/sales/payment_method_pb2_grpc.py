# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from omni_pro_grpc.v1.sales import payment_method_pb2 as v1_dot_sales_dot_payment__method__pb2


class PaymentMethodServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PaymentMethodCreate = channel.unary_unary(
                '/pro.omni.oms.api.v1.sales.payment.method.PaymentMethodService/PaymentMethodCreate',
                request_serializer=v1_dot_sales_dot_payment__method__pb2.PaymentMethodCreateRequest.SerializeToString,
                response_deserializer=v1_dot_sales_dot_payment__method__pb2.PaymentMethodCreateResponse.FromString,
                )
        self.PaymentMethodRead = channel.unary_unary(
                '/pro.omni.oms.api.v1.sales.payment.method.PaymentMethodService/PaymentMethodRead',
                request_serializer=v1_dot_sales_dot_payment__method__pb2.PaymentMethodReadRequest.SerializeToString,
                response_deserializer=v1_dot_sales_dot_payment__method__pb2.PaymentMethodReadResponse.FromString,
                )
        self.PaymentMethodUpdate = channel.unary_unary(
                '/pro.omni.oms.api.v1.sales.payment.method.PaymentMethodService/PaymentMethodUpdate',
                request_serializer=v1_dot_sales_dot_payment__method__pb2.PaymentMethodUpdateRequest.SerializeToString,
                response_deserializer=v1_dot_sales_dot_payment__method__pb2.PaymentMethodUpdateResponse.FromString,
                )
        self.PaymentMethodDelete = channel.unary_unary(
                '/pro.omni.oms.api.v1.sales.payment.method.PaymentMethodService/PaymentMethodDelete',
                request_serializer=v1_dot_sales_dot_payment__method__pb2.PaymentMethodDeleteRequest.SerializeToString,
                response_deserializer=v1_dot_sales_dot_payment__method__pb2.PaymentMethodDeleteResponse.FromString,
                )


class PaymentMethodServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PaymentMethodCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PaymentMethodRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PaymentMethodUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PaymentMethodDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PaymentMethodServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PaymentMethodCreate': grpc.unary_unary_rpc_method_handler(
                    servicer.PaymentMethodCreate,
                    request_deserializer=v1_dot_sales_dot_payment__method__pb2.PaymentMethodCreateRequest.FromString,
                    response_serializer=v1_dot_sales_dot_payment__method__pb2.PaymentMethodCreateResponse.SerializeToString,
            ),
            'PaymentMethodRead': grpc.unary_unary_rpc_method_handler(
                    servicer.PaymentMethodRead,
                    request_deserializer=v1_dot_sales_dot_payment__method__pb2.PaymentMethodReadRequest.FromString,
                    response_serializer=v1_dot_sales_dot_payment__method__pb2.PaymentMethodReadResponse.SerializeToString,
            ),
            'PaymentMethodUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.PaymentMethodUpdate,
                    request_deserializer=v1_dot_sales_dot_payment__method__pb2.PaymentMethodUpdateRequest.FromString,
                    response_serializer=v1_dot_sales_dot_payment__method__pb2.PaymentMethodUpdateResponse.SerializeToString,
            ),
            'PaymentMethodDelete': grpc.unary_unary_rpc_method_handler(
                    servicer.PaymentMethodDelete,
                    request_deserializer=v1_dot_sales_dot_payment__method__pb2.PaymentMethodDeleteRequest.FromString,
                    response_serializer=v1_dot_sales_dot_payment__method__pb2.PaymentMethodDeleteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pro.omni.oms.api.v1.sales.payment.method.PaymentMethodService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PaymentMethodService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PaymentMethodCreate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.sales.payment.method.PaymentMethodService/PaymentMethodCreate',
            v1_dot_sales_dot_payment__method__pb2.PaymentMethodCreateRequest.SerializeToString,
            v1_dot_sales_dot_payment__method__pb2.PaymentMethodCreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PaymentMethodRead(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.sales.payment.method.PaymentMethodService/PaymentMethodRead',
            v1_dot_sales_dot_payment__method__pb2.PaymentMethodReadRequest.SerializeToString,
            v1_dot_sales_dot_payment__method__pb2.PaymentMethodReadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PaymentMethodUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.sales.payment.method.PaymentMethodService/PaymentMethodUpdate',
            v1_dot_sales_dot_payment__method__pb2.PaymentMethodUpdateRequest.SerializeToString,
            v1_dot_sales_dot_payment__method__pb2.PaymentMethodUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PaymentMethodDelete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.sales.payment.method.PaymentMethodService/PaymentMethodDelete',
            v1_dot_sales_dot_payment__method__pb2.PaymentMethodDeleteRequest.SerializeToString,
            v1_dot_sales_dot_payment__method__pb2.PaymentMethodDeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
