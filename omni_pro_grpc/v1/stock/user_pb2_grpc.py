# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni_pro_grpc.v1.stock import user_pb2 as v1_dot_stock_dot_user__pb2


class UserServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UserCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.user.UserService/UserCreate",
            request_serializer=v1_dot_stock_dot_user__pb2.UserCreateRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_user__pb2.UserCreateResponse.FromString,
        )
        self.UserRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.user.UserService/UserRead",
            request_serializer=v1_dot_stock_dot_user__pb2.UserReadRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_user__pb2.UserReadResponse.FromString,
        )
        self.UserUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.user.UserService/UserUpdate",
            request_serializer=v1_dot_stock_dot_user__pb2.UserUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_user__pb2.UserUpdateResponse.FromString,
        )
        self.UserDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.user.UserService/UserDelete",
            request_serializer=v1_dot_stock_dot_user__pb2.UserDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_user__pb2.UserDeleteResponse.FromString,
        )


class UserServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UserCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UserRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UserUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UserDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_UserServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "UserCreate": grpc.unary_unary_rpc_method_handler(
            servicer.UserCreate,
            request_deserializer=v1_dot_stock_dot_user__pb2.UserCreateRequest.FromString,
            response_serializer=v1_dot_stock_dot_user__pb2.UserCreateResponse.SerializeToString,
        ),
        "UserRead": grpc.unary_unary_rpc_method_handler(
            servicer.UserRead,
            request_deserializer=v1_dot_stock_dot_user__pb2.UserReadRequest.FromString,
            response_serializer=v1_dot_stock_dot_user__pb2.UserReadResponse.SerializeToString,
        ),
        "UserUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.UserUpdate,
            request_deserializer=v1_dot_stock_dot_user__pb2.UserUpdateRequest.FromString,
            response_serializer=v1_dot_stock_dot_user__pb2.UserUpdateResponse.SerializeToString,
        ),
        "UserDelete": grpc.unary_unary_rpc_method_handler(
            servicer.UserDelete,
            request_deserializer=v1_dot_stock_dot_user__pb2.UserDeleteRequest.FromString,
            response_serializer=v1_dot_stock_dot_user__pb2.UserDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.stock.user.UserService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class UserService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UserCreate(
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
            "/pro.omni.oms.api.v1.stock.user.UserService/UserCreate",
            v1_dot_stock_dot_user__pb2.UserCreateRequest.SerializeToString,
            v1_dot_stock_dot_user__pb2.UserCreateResponse.FromString,
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
    def UserRead(
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
            "/pro.omni.oms.api.v1.stock.user.UserService/UserRead",
            v1_dot_stock_dot_user__pb2.UserReadRequest.SerializeToString,
            v1_dot_stock_dot_user__pb2.UserReadResponse.FromString,
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
    def UserUpdate(
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
            "/pro.omni.oms.api.v1.stock.user.UserService/UserUpdate",
            v1_dot_stock_dot_user__pb2.UserUpdateRequest.SerializeToString,
            v1_dot_stock_dot_user__pb2.UserUpdateResponse.FromString,
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
    def UserDelete(
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
            "/pro.omni.oms.api.v1.stock.user.UserService/UserDelete",
            v1_dot_stock_dot_user__pb2.UserDeleteRequest.SerializeToString,
            v1_dot_stock_dot_user__pb2.UserDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
