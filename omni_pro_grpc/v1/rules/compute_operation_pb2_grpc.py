# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni_pro_grpc.v1.rules import compute_operation_pb2 as v1_dot_rules_dot_compute__operation__pb2


class ComputeOperationServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ComputeMethod = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.compute_operation.ComputeOperationService/ComputeMethod",
            request_serializer=v1_dot_rules_dot_compute__operation__pb2.ComputeMethodRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_compute__operation__pb2.ComputeMethodResponse.FromString,
        )
        self.ComputeMethodStockAvailable = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.compute_operation.ComputeOperationService/ComputeMethodStockAvailable",
            request_serializer=v1_dot_rules_dot_compute__operation__pb2.ComputeMethodStockAvailableRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_compute__operation__pb2.ComputeMethodStockAvailableResponse.FromString,
        )
        self.ComputeDeliveryCarrier = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.compute_operation.ComputeOperationService/ComputeDeliveryCarrier",
            request_serializer=v1_dot_rules_dot_compute__operation__pb2.ComputeDeliveryCarrierRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_compute__operation__pb2.ComputeDeliveryCarrierResponse.FromString,
        )


class ComputeOperationServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ComputeMethod(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ComputeMethodStockAvailable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ComputeDeliveryCarrier(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ComputeOperationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ComputeMethod": grpc.unary_unary_rpc_method_handler(
            servicer.ComputeMethod,
            request_deserializer=v1_dot_rules_dot_compute__operation__pb2.ComputeMethodRequest.FromString,
            response_serializer=v1_dot_rules_dot_compute__operation__pb2.ComputeMethodResponse.SerializeToString,
        ),
        "ComputeMethodStockAvailable": grpc.unary_unary_rpc_method_handler(
            servicer.ComputeMethodStockAvailable,
            request_deserializer=v1_dot_rules_dot_compute__operation__pb2.ComputeMethodStockAvailableRequest.FromString,
            response_serializer=v1_dot_rules_dot_compute__operation__pb2.ComputeMethodStockAvailableResponse.SerializeToString,
        ),
        "ComputeDeliveryCarrier": grpc.unary_unary_rpc_method_handler(
            servicer.ComputeDeliveryCarrier,
            request_deserializer=v1_dot_rules_dot_compute__operation__pb2.ComputeDeliveryCarrierRequest.FromString,
            response_serializer=v1_dot_rules_dot_compute__operation__pb2.ComputeDeliveryCarrierResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.rules.compute_operation.ComputeOperationService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class ComputeOperationService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ComputeMethod(
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
            "/pro.omni.oms.api.v1.rules.compute_operation.ComputeOperationService/ComputeMethod",
            v1_dot_rules_dot_compute__operation__pb2.ComputeMethodRequest.SerializeToString,
            v1_dot_rules_dot_compute__operation__pb2.ComputeMethodResponse.FromString,
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
    def ComputeMethodStockAvailable(
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
            "/pro.omni.oms.api.v1.rules.compute_operation.ComputeOperationService/ComputeMethodStockAvailable",
            v1_dot_rules_dot_compute__operation__pb2.ComputeMethodStockAvailableRequest.SerializeToString,
            v1_dot_rules_dot_compute__operation__pb2.ComputeMethodStockAvailableResponse.FromString,
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
    def ComputeDeliveryCarrier(
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
            "/pro.omni.oms.api.v1.rules.compute_operation.ComputeOperationService/ComputeDeliveryCarrier",
            v1_dot_rules_dot_compute__operation__pb2.ComputeDeliveryCarrierRequest.SerializeToString,
            v1_dot_rules_dot_compute__operation__pb2.ComputeDeliveryCarrierResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
