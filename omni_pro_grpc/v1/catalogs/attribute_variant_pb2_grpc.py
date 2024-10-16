# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni_pro_grpc.v1.catalogs import attribute_variant_pb2 as v1_dot_catalogs_dot_attribute__variant__pb2


class AttributeVariantServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AttributeVariantCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.catalogs.attribute_variant.AttributeVariantService/AttributeVariantCreate",
            request_serializer=v1_dot_catalogs_dot_attribute__variant__pb2.AttributeVariantCreateRequest.SerializeToString,
            response_deserializer=v1_dot_catalogs_dot_attribute__variant__pb2.AttributeVariantCreateResponse.FromString,
        )
        self.AttributeVariantRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.catalogs.attribute_variant.AttributeVariantService/AttributeVariantRead",
            request_serializer=v1_dot_catalogs_dot_attribute__variant__pb2.AttributeVariantReadRequest.SerializeToString,
            response_deserializer=v1_dot_catalogs_dot_attribute__variant__pb2.AttributeVariantReadResponse.FromString,
        )
        self.AttributeVariantUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.catalogs.attribute_variant.AttributeVariantService/AttributeVariantUpdate",
            request_serializer=v1_dot_catalogs_dot_attribute__variant__pb2.AttributeVariantUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_catalogs_dot_attribute__variant__pb2.AttributeVariantUpdateResponse.FromString,
        )
        self.AttributeVariantDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.catalogs.attribute_variant.AttributeVariantService/AttributeVariantDelete",
            request_serializer=v1_dot_catalogs_dot_attribute__variant__pb2.AttributeVariantDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_catalogs_dot_attribute__variant__pb2.AttributeVariantDeleteResponse.FromString,
        )


class AttributeVariantServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AttributeVariantCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AttributeVariantRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AttributeVariantUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AttributeVariantDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_AttributeVariantServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "AttributeVariantCreate": grpc.unary_unary_rpc_method_handler(
            servicer.AttributeVariantCreate,
            request_deserializer=v1_dot_catalogs_dot_attribute__variant__pb2.AttributeVariantCreateRequest.FromString,
            response_serializer=v1_dot_catalogs_dot_attribute__variant__pb2.AttributeVariantCreateResponse.SerializeToString,
        ),
        "AttributeVariantRead": grpc.unary_unary_rpc_method_handler(
            servicer.AttributeVariantRead,
            request_deserializer=v1_dot_catalogs_dot_attribute__variant__pb2.AttributeVariantReadRequest.FromString,
            response_serializer=v1_dot_catalogs_dot_attribute__variant__pb2.AttributeVariantReadResponse.SerializeToString,
        ),
        "AttributeVariantUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.AttributeVariantUpdate,
            request_deserializer=v1_dot_catalogs_dot_attribute__variant__pb2.AttributeVariantUpdateRequest.FromString,
            response_serializer=v1_dot_catalogs_dot_attribute__variant__pb2.AttributeVariantUpdateResponse.SerializeToString,
        ),
        "AttributeVariantDelete": grpc.unary_unary_rpc_method_handler(
            servicer.AttributeVariantDelete,
            request_deserializer=v1_dot_catalogs_dot_attribute__variant__pb2.AttributeVariantDeleteRequest.FromString,
            response_serializer=v1_dot_catalogs_dot_attribute__variant__pb2.AttributeVariantDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.catalogs.attribute_variant.AttributeVariantService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class AttributeVariantService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AttributeVariantCreate(
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
            "/pro.omni.oms.api.v1.catalogs.attribute_variant.AttributeVariantService/AttributeVariantCreate",
            v1_dot_catalogs_dot_attribute__variant__pb2.AttributeVariantCreateRequest.SerializeToString,
            v1_dot_catalogs_dot_attribute__variant__pb2.AttributeVariantCreateResponse.FromString,
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
    def AttributeVariantRead(
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
            "/pro.omni.oms.api.v1.catalogs.attribute_variant.AttributeVariantService/AttributeVariantRead",
            v1_dot_catalogs_dot_attribute__variant__pb2.AttributeVariantReadRequest.SerializeToString,
            v1_dot_catalogs_dot_attribute__variant__pb2.AttributeVariantReadResponse.FromString,
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
    def AttributeVariantUpdate(
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
            "/pro.omni.oms.api.v1.catalogs.attribute_variant.AttributeVariantService/AttributeVariantUpdate",
            v1_dot_catalogs_dot_attribute__variant__pb2.AttributeVariantUpdateRequest.SerializeToString,
            v1_dot_catalogs_dot_attribute__variant__pb2.AttributeVariantUpdateResponse.FromString,
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
    def AttributeVariantDelete(
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
            "/pro.omni.oms.api.v1.catalogs.attribute_variant.AttributeVariantService/AttributeVariantDelete",
            v1_dot_catalogs_dot_attribute__variant__pb2.AttributeVariantDeleteRequest.SerializeToString,
            v1_dot_catalogs_dot_attribute__variant__pb2.AttributeVariantDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
