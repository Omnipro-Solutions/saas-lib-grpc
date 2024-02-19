# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from omni_pro_grpc.v1.rules import delivery_price_delivery_method_pb2 as v1_dot_rules_dot_delivery__price__delivery__method__pb2


class DeliveryPriceDeliveryMethodServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DeliveryPriceDeliveryMethodCreate = channel.unary_unary(
                '/pro.omni.oms.api.v1.rules.delivery_price_delivery_method.DeliveryPriceDeliveryMethodService/DeliveryPriceDeliveryMethodCreate',
                request_serializer=v1_dot_rules_dot_delivery__price__delivery__method__pb2.DeliveryPriceDeliveryMethodCreateRequest.SerializeToString,
                response_deserializer=v1_dot_rules_dot_delivery__price__delivery__method__pb2.DeliveryPriceDeliveryMethodCreateResponse.FromString,
                )
        self.DeliveryPriceDeliveryMethodRead = channel.unary_unary(
                '/pro.omni.oms.api.v1.rules.delivery_price_delivery_method.DeliveryPriceDeliveryMethodService/DeliveryPriceDeliveryMethodRead',
                request_serializer=v1_dot_rules_dot_delivery__price__delivery__method__pb2.DeliveryPriceDeliveryMethodReadRequest.SerializeToString,
                response_deserializer=v1_dot_rules_dot_delivery__price__delivery__method__pb2.DeliveryPriceDeliveryMethodReadResponse.FromString,
                )
        self.DeliveryPriceDeliveryMethodUpdate = channel.unary_unary(
                '/pro.omni.oms.api.v1.rules.delivery_price_delivery_method.DeliveryPriceDeliveryMethodService/DeliveryPriceDeliveryMethodUpdate',
                request_serializer=v1_dot_rules_dot_delivery__price__delivery__method__pb2.DeliveryPriceDeliveryMethodUpdateRequest.SerializeToString,
                response_deserializer=v1_dot_rules_dot_delivery__price__delivery__method__pb2.DeliveryPriceDeliveryMethodUpdateResponse.FromString,
                )
        self.DeliveryPriceDeliveryMethodDelete = channel.unary_unary(
                '/pro.omni.oms.api.v1.rules.delivery_price_delivery_method.DeliveryPriceDeliveryMethodService/DeliveryPriceDeliveryMethodDelete',
                request_serializer=v1_dot_rules_dot_delivery__price__delivery__method__pb2.DeliveryPriceDeliveryMethodDeleteRequest.SerializeToString,
                response_deserializer=v1_dot_rules_dot_delivery__price__delivery__method__pb2.DeliveryPriceDeliveryMethodDeleteResponse.FromString,
                )


class DeliveryPriceDeliveryMethodServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def DeliveryPriceDeliveryMethodCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeliveryPriceDeliveryMethodRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeliveryPriceDeliveryMethodUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeliveryPriceDeliveryMethodDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DeliveryPriceDeliveryMethodServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DeliveryPriceDeliveryMethodCreate': grpc.unary_unary_rpc_method_handler(
                    servicer.DeliveryPriceDeliveryMethodCreate,
                    request_deserializer=v1_dot_rules_dot_delivery__price__delivery__method__pb2.DeliveryPriceDeliveryMethodCreateRequest.FromString,
                    response_serializer=v1_dot_rules_dot_delivery__price__delivery__method__pb2.DeliveryPriceDeliveryMethodCreateResponse.SerializeToString,
            ),
            'DeliveryPriceDeliveryMethodRead': grpc.unary_unary_rpc_method_handler(
                    servicer.DeliveryPriceDeliveryMethodRead,
                    request_deserializer=v1_dot_rules_dot_delivery__price__delivery__method__pb2.DeliveryPriceDeliveryMethodReadRequest.FromString,
                    response_serializer=v1_dot_rules_dot_delivery__price__delivery__method__pb2.DeliveryPriceDeliveryMethodReadResponse.SerializeToString,
            ),
            'DeliveryPriceDeliveryMethodUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.DeliveryPriceDeliveryMethodUpdate,
                    request_deserializer=v1_dot_rules_dot_delivery__price__delivery__method__pb2.DeliveryPriceDeliveryMethodUpdateRequest.FromString,
                    response_serializer=v1_dot_rules_dot_delivery__price__delivery__method__pb2.DeliveryPriceDeliveryMethodUpdateResponse.SerializeToString,
            ),
            'DeliveryPriceDeliveryMethodDelete': grpc.unary_unary_rpc_method_handler(
                    servicer.DeliveryPriceDeliveryMethodDelete,
                    request_deserializer=v1_dot_rules_dot_delivery__price__delivery__method__pb2.DeliveryPriceDeliveryMethodDeleteRequest.FromString,
                    response_serializer=v1_dot_rules_dot_delivery__price__delivery__method__pb2.DeliveryPriceDeliveryMethodDeleteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pro.omni.oms.api.v1.rules.delivery_price_delivery_method.DeliveryPriceDeliveryMethodService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DeliveryPriceDeliveryMethodService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def DeliveryPriceDeliveryMethodCreate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.rules.delivery_price_delivery_method.DeliveryPriceDeliveryMethodService/DeliveryPriceDeliveryMethodCreate',
            v1_dot_rules_dot_delivery__price__delivery__method__pb2.DeliveryPriceDeliveryMethodCreateRequest.SerializeToString,
            v1_dot_rules_dot_delivery__price__delivery__method__pb2.DeliveryPriceDeliveryMethodCreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeliveryPriceDeliveryMethodRead(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.rules.delivery_price_delivery_method.DeliveryPriceDeliveryMethodService/DeliveryPriceDeliveryMethodRead',
            v1_dot_rules_dot_delivery__price__delivery__method__pb2.DeliveryPriceDeliveryMethodReadRequest.SerializeToString,
            v1_dot_rules_dot_delivery__price__delivery__method__pb2.DeliveryPriceDeliveryMethodReadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeliveryPriceDeliveryMethodUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.rules.delivery_price_delivery_method.DeliveryPriceDeliveryMethodService/DeliveryPriceDeliveryMethodUpdate',
            v1_dot_rules_dot_delivery__price__delivery__method__pb2.DeliveryPriceDeliveryMethodUpdateRequest.SerializeToString,
            v1_dot_rules_dot_delivery__price__delivery__method__pb2.DeliveryPriceDeliveryMethodUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeliveryPriceDeliveryMethodDelete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pro.omni.oms.api.v1.rules.delivery_price_delivery_method.DeliveryPriceDeliveryMethodService/DeliveryPriceDeliveryMethodDelete',
            v1_dot_rules_dot_delivery__price__delivery__method__pb2.DeliveryPriceDeliveryMethodDeleteRequest.SerializeToString,
            v1_dot_rules_dot_delivery__price__delivery__method__pb2.DeliveryPriceDeliveryMethodDeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
