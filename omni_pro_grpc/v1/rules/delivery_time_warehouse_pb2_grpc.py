# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni_pro_grpc.v1.rules import delivery_time_warehouse_pb2 as v1_dot_rules_dot_delivery__time__warehouse__pb2


class DeliveryTimeWarehouseServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DeliveryTimeWarehouseCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.delivery_time_warehouse.DeliveryTimeWarehouseService/DeliveryTimeWarehouseCreate",
            request_serializer=v1_dot_rules_dot_delivery__time__warehouse__pb2.DeliveryTimeWarehouseCreateRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_delivery__time__warehouse__pb2.DeliveryTimeWarehouseCreateResponse.FromString,
        )
        self.DeliveryTimeWarehouseRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.delivery_time_warehouse.DeliveryTimeWarehouseService/DeliveryTimeWarehouseRead",
            request_serializer=v1_dot_rules_dot_delivery__time__warehouse__pb2.DeliveryTimeWarehouseReadRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_delivery__time__warehouse__pb2.DeliveryTimeWarehouseReadResponse.FromString,
        )
        self.DeliveryTimeWarehouseUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.delivery_time_warehouse.DeliveryTimeWarehouseService/DeliveryTimeWarehouseUpdate",
            request_serializer=v1_dot_rules_dot_delivery__time__warehouse__pb2.DeliveryTimeWarehouseUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_delivery__time__warehouse__pb2.DeliveryTimeWarehouseUpdateResponse.FromString,
        )
        self.DeliveryTimeWarehouseDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.delivery_time_warehouse.DeliveryTimeWarehouseService/DeliveryTimeWarehouseDelete",
            request_serializer=v1_dot_rules_dot_delivery__time__warehouse__pb2.DeliveryTimeWarehouseDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_delivery__time__warehouse__pb2.DeliveryTimeWarehouseDeleteResponse.FromString,
        )


class DeliveryTimeWarehouseServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def DeliveryTimeWarehouseCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeliveryTimeWarehouseRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeliveryTimeWarehouseUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeliveryTimeWarehouseDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_DeliveryTimeWarehouseServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "DeliveryTimeWarehouseCreate": grpc.unary_unary_rpc_method_handler(
            servicer.DeliveryTimeWarehouseCreate,
            request_deserializer=v1_dot_rules_dot_delivery__time__warehouse__pb2.DeliveryTimeWarehouseCreateRequest.FromString,
            response_serializer=v1_dot_rules_dot_delivery__time__warehouse__pb2.DeliveryTimeWarehouseCreateResponse.SerializeToString,
        ),
        "DeliveryTimeWarehouseRead": grpc.unary_unary_rpc_method_handler(
            servicer.DeliveryTimeWarehouseRead,
            request_deserializer=v1_dot_rules_dot_delivery__time__warehouse__pb2.DeliveryTimeWarehouseReadRequest.FromString,
            response_serializer=v1_dot_rules_dot_delivery__time__warehouse__pb2.DeliveryTimeWarehouseReadResponse.SerializeToString,
        ),
        "DeliveryTimeWarehouseUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.DeliveryTimeWarehouseUpdate,
            request_deserializer=v1_dot_rules_dot_delivery__time__warehouse__pb2.DeliveryTimeWarehouseUpdateRequest.FromString,
            response_serializer=v1_dot_rules_dot_delivery__time__warehouse__pb2.DeliveryTimeWarehouseUpdateResponse.SerializeToString,
        ),
        "DeliveryTimeWarehouseDelete": grpc.unary_unary_rpc_method_handler(
            servicer.DeliveryTimeWarehouseDelete,
            request_deserializer=v1_dot_rules_dot_delivery__time__warehouse__pb2.DeliveryTimeWarehouseDeleteRequest.FromString,
            response_serializer=v1_dot_rules_dot_delivery__time__warehouse__pb2.DeliveryTimeWarehouseDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.rules.delivery_time_warehouse.DeliveryTimeWarehouseService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class DeliveryTimeWarehouseService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def DeliveryTimeWarehouseCreate(
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
            "/pro.omni.oms.api.v1.rules.delivery_time_warehouse.DeliveryTimeWarehouseService/DeliveryTimeWarehouseCreate",
            v1_dot_rules_dot_delivery__time__warehouse__pb2.DeliveryTimeWarehouseCreateRequest.SerializeToString,
            v1_dot_rules_dot_delivery__time__warehouse__pb2.DeliveryTimeWarehouseCreateResponse.FromString,
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
    def DeliveryTimeWarehouseRead(
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
            "/pro.omni.oms.api.v1.rules.delivery_time_warehouse.DeliveryTimeWarehouseService/DeliveryTimeWarehouseRead",
            v1_dot_rules_dot_delivery__time__warehouse__pb2.DeliveryTimeWarehouseReadRequest.SerializeToString,
            v1_dot_rules_dot_delivery__time__warehouse__pb2.DeliveryTimeWarehouseReadResponse.FromString,
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
    def DeliveryTimeWarehouseUpdate(
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
            "/pro.omni.oms.api.v1.rules.delivery_time_warehouse.DeliveryTimeWarehouseService/DeliveryTimeWarehouseUpdate",
            v1_dot_rules_dot_delivery__time__warehouse__pb2.DeliveryTimeWarehouseUpdateRequest.SerializeToString,
            v1_dot_rules_dot_delivery__time__warehouse__pb2.DeliveryTimeWarehouseUpdateResponse.FromString,
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
    def DeliveryTimeWarehouseDelete(
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
            "/pro.omni.oms.api.v1.rules.delivery_time_warehouse.DeliveryTimeWarehouseService/DeliveryTimeWarehouseDelete",
            v1_dot_rules_dot_delivery__time__warehouse__pb2.DeliveryTimeWarehouseDeleteRequest.SerializeToString,
            v1_dot_rules_dot_delivery__time__warehouse__pb2.DeliveryTimeWarehouseDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
