# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni_pro_grpc.v1.clients import type_document_pb2 as v1_dot_clients_dot_type__document__pb2


class TypeDocumentServiceStub(object):
    """TypeDocument es una replica, solo declarar el message TypeDocument"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TypeDocumentCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.clients.type_document.TypeDocumentService/TypeDocumentCreate",
            request_serializer=v1_dot_clients_dot_type__document__pb2.TypeDocumentCreateRequest.SerializeToString,
            response_deserializer=v1_dot_clients_dot_type__document__pb2.TypeDocumentCreateResponse.FromString,
        )
        self.TypeDocumentRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.clients.type_document.TypeDocumentService/TypeDocumentRead",
            request_serializer=v1_dot_clients_dot_type__document__pb2.TypeDocumentReadRequest.SerializeToString,
            response_deserializer=v1_dot_clients_dot_type__document__pb2.TypeDocumentReadResponse.FromString,
        )
        self.TypeDocumentUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.clients.type_document.TypeDocumentService/TypeDocumentUpdate",
            request_serializer=v1_dot_clients_dot_type__document__pb2.TypeDocumentUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_clients_dot_type__document__pb2.TypeDocumentUpdateResponse.FromString,
        )
        self.TypeDocumentDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.clients.type_document.TypeDocumentService/TypeDocumentDelete",
            request_serializer=v1_dot_clients_dot_type__document__pb2.TypeDocumentDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_clients_dot_type__document__pb2.TypeDocumentDeleteResponse.FromString,
        )


class TypeDocumentServiceServicer(object):
    """TypeDocument es una replica, solo declarar el message TypeDocument"""

    def TypeDocumentCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def TypeDocumentRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def TypeDocumentUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def TypeDocumentDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_TypeDocumentServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "TypeDocumentCreate": grpc.unary_unary_rpc_method_handler(
            servicer.TypeDocumentCreate,
            request_deserializer=v1_dot_clients_dot_type__document__pb2.TypeDocumentCreateRequest.FromString,
            response_serializer=v1_dot_clients_dot_type__document__pb2.TypeDocumentCreateResponse.SerializeToString,
        ),
        "TypeDocumentRead": grpc.unary_unary_rpc_method_handler(
            servicer.TypeDocumentRead,
            request_deserializer=v1_dot_clients_dot_type__document__pb2.TypeDocumentReadRequest.FromString,
            response_serializer=v1_dot_clients_dot_type__document__pb2.TypeDocumentReadResponse.SerializeToString,
        ),
        "TypeDocumentUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.TypeDocumentUpdate,
            request_deserializer=v1_dot_clients_dot_type__document__pb2.TypeDocumentUpdateRequest.FromString,
            response_serializer=v1_dot_clients_dot_type__document__pb2.TypeDocumentUpdateResponse.SerializeToString,
        ),
        "TypeDocumentDelete": grpc.unary_unary_rpc_method_handler(
            servicer.TypeDocumentDelete,
            request_deserializer=v1_dot_clients_dot_type__document__pb2.TypeDocumentDeleteRequest.FromString,
            response_serializer=v1_dot_clients_dot_type__document__pb2.TypeDocumentDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.clients.type_document.TypeDocumentService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class TypeDocumentService(object):
    """TypeDocument es una replica, solo declarar el message TypeDocument"""

    @staticmethod
    def TypeDocumentCreate(
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
            "/pro.omni.oms.api.v1.clients.type_document.TypeDocumentService/TypeDocumentCreate",
            v1_dot_clients_dot_type__document__pb2.TypeDocumentCreateRequest.SerializeToString,
            v1_dot_clients_dot_type__document__pb2.TypeDocumentCreateResponse.FromString,
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
    def TypeDocumentRead(
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
            "/pro.omni.oms.api.v1.clients.type_document.TypeDocumentService/TypeDocumentRead",
            v1_dot_clients_dot_type__document__pb2.TypeDocumentReadRequest.SerializeToString,
            v1_dot_clients_dot_type__document__pb2.TypeDocumentReadResponse.FromString,
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
    def TypeDocumentUpdate(
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
            "/pro.omni.oms.api.v1.clients.type_document.TypeDocumentService/TypeDocumentUpdate",
            v1_dot_clients_dot_type__document__pb2.TypeDocumentUpdateRequest.SerializeToString,
            v1_dot_clients_dot_type__document__pb2.TypeDocumentUpdateResponse.FromString,
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
    def TypeDocumentDelete(
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
            "/pro.omni.oms.api.v1.clients.type_document.TypeDocumentService/TypeDocumentDelete",
            v1_dot_clients_dot_type__document__pb2.TypeDocumentDeleteRequest.SerializeToString,
            v1_dot_clients_dot_type__document__pb2.TypeDocumentDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
