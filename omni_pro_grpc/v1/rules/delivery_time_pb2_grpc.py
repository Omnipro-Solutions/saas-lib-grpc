# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni_pro_grpc.v1.rules import delivery_time_pb2 as v1_dot_rules_dot_delivery__time__pb2


class DeliveryTimeServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DeliveryTimeCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.delivery_time.DeliveryTimeService/DeliveryTimeCreate",
            request_serializer=v1_dot_rules_dot_delivery__time__pb2.DeliveryTimeCreateRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_delivery__time__pb2.DeliveryTimeCreateResponse.FromString,
        )
        self.DeliveryTimeRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.delivery_time.DeliveryTimeService/DeliveryTimeRead",
            request_serializer=v1_dot_rules_dot_delivery__time__pb2.DeliveryTimeReadRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_delivery__time__pb2.DeliveryTimeReadResponse.FromString,
        )
        self.DeliveryTimeUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.delivery_time.DeliveryTimeService/DeliveryTimeUpdate",
            request_serializer=v1_dot_rules_dot_delivery__time__pb2.DeliveryTimeUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_delivery__time__pb2.DeliveryTimeUpdateResponse.FromString,
        )
        self.DeliveryTimeDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.delivery_time.DeliveryTimeService/DeliveryTimeDelete",
            request_serializer=v1_dot_rules_dot_delivery__time__pb2.DeliveryTimeDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_delivery__time__pb2.DeliveryTimeDeleteResponse.FromString,
        )
        self.AddWarehousesTo = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.delivery_time.DeliveryTimeService/AddWarehousesTo",
            request_serializer=v1_dot_rules_dot_delivery__time__pb2.AddWarehousesToRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_delivery__time__pb2.AddWarehousesToResponse.FromString,
        )
        self.RemoveWarehousesTo = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.delivery_time.DeliveryTimeService/RemoveWarehousesTo",
            request_serializer=v1_dot_rules_dot_delivery__time__pb2.RemoveWarehousesToRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_delivery__time__pb2.RemoveWarehousesToResponse.FromString,
        )
        self.AddWarehousesFrom = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.delivery_time.DeliveryTimeService/AddWarehousesFrom",
            request_serializer=v1_dot_rules_dot_delivery__time__pb2.AddWarehousesFromRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_delivery__time__pb2.AddWarehousesFromResponse.FromString,
        )
        self.RemoveWarehousesFrom = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.delivery_time.DeliveryTimeService/RemoveWarehousesFrom",
            request_serializer=v1_dot_rules_dot_delivery__time__pb2.RemoveWarehousesFromRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_delivery__time__pb2.RemoveWarehousesFromResponse.FromString,
        )
        self.AddDeliveryMethod = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.delivery_time.DeliveryTimeService/AddDeliveryMethod",
            request_serializer=v1_dot_rules_dot_delivery__time__pb2.AddDeliveryMethodRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_delivery__time__pb2.AddDeliveryMethodResponse.FromString,
        )
        self.RemoveDeliveryMethod = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.delivery_time.DeliveryTimeService/RemoveDeliveryMethod",
            request_serializer=v1_dot_rules_dot_delivery__time__pb2.RemoveDeliveryMethodRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_delivery__time__pb2.RemoveDeliveryMethodResponse.FromString,
        )


class DeliveryTimeServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def DeliveryTimeCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeliveryTimeRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeliveryTimeUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeliveryTimeDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AddWarehousesTo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def RemoveWarehousesTo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AddWarehousesFrom(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def RemoveWarehousesFrom(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AddDeliveryMethod(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def RemoveDeliveryMethod(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_DeliveryTimeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "DeliveryTimeCreate": grpc.unary_unary_rpc_method_handler(
            servicer.DeliveryTimeCreate,
            request_deserializer=v1_dot_rules_dot_delivery__time__pb2.DeliveryTimeCreateRequest.FromString,
            response_serializer=v1_dot_rules_dot_delivery__time__pb2.DeliveryTimeCreateResponse.SerializeToString,
        ),
        "DeliveryTimeRead": grpc.unary_unary_rpc_method_handler(
            servicer.DeliveryTimeRead,
            request_deserializer=v1_dot_rules_dot_delivery__time__pb2.DeliveryTimeReadRequest.FromString,
            response_serializer=v1_dot_rules_dot_delivery__time__pb2.DeliveryTimeReadResponse.SerializeToString,
        ),
        "DeliveryTimeUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.DeliveryTimeUpdate,
            request_deserializer=v1_dot_rules_dot_delivery__time__pb2.DeliveryTimeUpdateRequest.FromString,
            response_serializer=v1_dot_rules_dot_delivery__time__pb2.DeliveryTimeUpdateResponse.SerializeToString,
        ),
        "DeliveryTimeDelete": grpc.unary_unary_rpc_method_handler(
            servicer.DeliveryTimeDelete,
            request_deserializer=v1_dot_rules_dot_delivery__time__pb2.DeliveryTimeDeleteRequest.FromString,
            response_serializer=v1_dot_rules_dot_delivery__time__pb2.DeliveryTimeDeleteResponse.SerializeToString,
        ),
        "AddWarehousesTo": grpc.unary_unary_rpc_method_handler(
            servicer.AddWarehousesTo,
            request_deserializer=v1_dot_rules_dot_delivery__time__pb2.AddWarehousesToRequest.FromString,
            response_serializer=v1_dot_rules_dot_delivery__time__pb2.AddWarehousesToResponse.SerializeToString,
        ),
        "RemoveWarehousesTo": grpc.unary_unary_rpc_method_handler(
            servicer.RemoveWarehousesTo,
            request_deserializer=v1_dot_rules_dot_delivery__time__pb2.RemoveWarehousesToRequest.FromString,
            response_serializer=v1_dot_rules_dot_delivery__time__pb2.RemoveWarehousesToResponse.SerializeToString,
        ),
        "AddWarehousesFrom": grpc.unary_unary_rpc_method_handler(
            servicer.AddWarehousesFrom,
            request_deserializer=v1_dot_rules_dot_delivery__time__pb2.AddWarehousesFromRequest.FromString,
            response_serializer=v1_dot_rules_dot_delivery__time__pb2.AddWarehousesFromResponse.SerializeToString,
        ),
        "RemoveWarehousesFrom": grpc.unary_unary_rpc_method_handler(
            servicer.RemoveWarehousesFrom,
            request_deserializer=v1_dot_rules_dot_delivery__time__pb2.RemoveWarehousesFromRequest.FromString,
            response_serializer=v1_dot_rules_dot_delivery__time__pb2.RemoveWarehousesFromResponse.SerializeToString,
        ),
        "AddDeliveryMethod": grpc.unary_unary_rpc_method_handler(
            servicer.AddDeliveryMethod,
            request_deserializer=v1_dot_rules_dot_delivery__time__pb2.AddDeliveryMethodRequest.FromString,
            response_serializer=v1_dot_rules_dot_delivery__time__pb2.AddDeliveryMethodResponse.SerializeToString,
        ),
        "RemoveDeliveryMethod": grpc.unary_unary_rpc_method_handler(
            servicer.RemoveDeliveryMethod,
            request_deserializer=v1_dot_rules_dot_delivery__time__pb2.RemoveDeliveryMethodRequest.FromString,
            response_serializer=v1_dot_rules_dot_delivery__time__pb2.RemoveDeliveryMethodResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.rules.delivery_time.DeliveryTimeService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class DeliveryTimeService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def DeliveryTimeCreate(
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
            "/pro.omni.oms.api.v1.rules.delivery_time.DeliveryTimeService/DeliveryTimeCreate",
            v1_dot_rules_dot_delivery__time__pb2.DeliveryTimeCreateRequest.SerializeToString,
            v1_dot_rules_dot_delivery__time__pb2.DeliveryTimeCreateResponse.FromString,
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
    def DeliveryTimeRead(
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
            "/pro.omni.oms.api.v1.rules.delivery_time.DeliveryTimeService/DeliveryTimeRead",
            v1_dot_rules_dot_delivery__time__pb2.DeliveryTimeReadRequest.SerializeToString,
            v1_dot_rules_dot_delivery__time__pb2.DeliveryTimeReadResponse.FromString,
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
    def DeliveryTimeUpdate(
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
            "/pro.omni.oms.api.v1.rules.delivery_time.DeliveryTimeService/DeliveryTimeUpdate",
            v1_dot_rules_dot_delivery__time__pb2.DeliveryTimeUpdateRequest.SerializeToString,
            v1_dot_rules_dot_delivery__time__pb2.DeliveryTimeUpdateResponse.FromString,
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
    def DeliveryTimeDelete(
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
            "/pro.omni.oms.api.v1.rules.delivery_time.DeliveryTimeService/DeliveryTimeDelete",
            v1_dot_rules_dot_delivery__time__pb2.DeliveryTimeDeleteRequest.SerializeToString,
            v1_dot_rules_dot_delivery__time__pb2.DeliveryTimeDeleteResponse.FromString,
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
    def AddWarehousesTo(
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
            "/pro.omni.oms.api.v1.rules.delivery_time.DeliveryTimeService/AddWarehousesTo",
            v1_dot_rules_dot_delivery__time__pb2.AddWarehousesToRequest.SerializeToString,
            v1_dot_rules_dot_delivery__time__pb2.AddWarehousesToResponse.FromString,
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
    def RemoveWarehousesTo(
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
            "/pro.omni.oms.api.v1.rules.delivery_time.DeliveryTimeService/RemoveWarehousesTo",
            v1_dot_rules_dot_delivery__time__pb2.RemoveWarehousesToRequest.SerializeToString,
            v1_dot_rules_dot_delivery__time__pb2.RemoveWarehousesToResponse.FromString,
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
    def AddWarehousesFrom(
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
            "/pro.omni.oms.api.v1.rules.delivery_time.DeliveryTimeService/AddWarehousesFrom",
            v1_dot_rules_dot_delivery__time__pb2.AddWarehousesFromRequest.SerializeToString,
            v1_dot_rules_dot_delivery__time__pb2.AddWarehousesFromResponse.FromString,
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
    def RemoveWarehousesFrom(
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
            "/pro.omni.oms.api.v1.rules.delivery_time.DeliveryTimeService/RemoveWarehousesFrom",
            v1_dot_rules_dot_delivery__time__pb2.RemoveWarehousesFromRequest.SerializeToString,
            v1_dot_rules_dot_delivery__time__pb2.RemoveWarehousesFromResponse.FromString,
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
    def AddDeliveryMethod(
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
            "/pro.omni.oms.api.v1.rules.delivery_time.DeliveryTimeService/AddDeliveryMethod",
            v1_dot_rules_dot_delivery__time__pb2.AddDeliveryMethodRequest.SerializeToString,
            v1_dot_rules_dot_delivery__time__pb2.AddDeliveryMethodResponse.FromString,
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
    def RemoveDeliveryMethod(
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
            "/pro.omni.oms.api.v1.rules.delivery_time.DeliveryTimeService/RemoveDeliveryMethod",
            v1_dot_rules_dot_delivery__time__pb2.RemoveDeliveryMethodRequest.SerializeToString,
            v1_dot_rules_dot_delivery__time__pb2.RemoveDeliveryMethodResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
