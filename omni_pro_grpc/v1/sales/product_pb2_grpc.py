# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni_pro_grpc.v1.sales import product_pb2 as v1_dot_sales_dot_product__pb2


class ProductServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ProductCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.product.ProductService/ProductCreate",
            request_serializer=v1_dot_sales_dot_product__pb2.ProductCreateRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_product__pb2.ProductCreateResponse.FromString,
        )
        self.ProductRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.product.ProductService/ProductRead",
            request_serializer=v1_dot_sales_dot_product__pb2.ProductReadRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_product__pb2.ProductReadResponse.FromString,
        )
        self.ProductUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.product.ProductService/ProductUpdate",
            request_serializer=v1_dot_sales_dot_product__pb2.ProductUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_product__pb2.ProductUpdateResponse.FromString,
        )
        self.ProductDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.product.ProductService/ProductDelete",
            request_serializer=v1_dot_sales_dot_product__pb2.ProductDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_product__pb2.ProductDeleteResponse.FromString,
        )


class ProductServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ProductCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ProductRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ProductUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ProductDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ProductServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ProductCreate": grpc.unary_unary_rpc_method_handler(
            servicer.ProductCreate,
            request_deserializer=v1_dot_sales_dot_product__pb2.ProductCreateRequest.FromString,
            response_serializer=v1_dot_sales_dot_product__pb2.ProductCreateResponse.SerializeToString,
        ),
        "ProductRead": grpc.unary_unary_rpc_method_handler(
            servicer.ProductRead,
            request_deserializer=v1_dot_sales_dot_product__pb2.ProductReadRequest.FromString,
            response_serializer=v1_dot_sales_dot_product__pb2.ProductReadResponse.SerializeToString,
        ),
        "ProductUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.ProductUpdate,
            request_deserializer=v1_dot_sales_dot_product__pb2.ProductUpdateRequest.FromString,
            response_serializer=v1_dot_sales_dot_product__pb2.ProductUpdateResponse.SerializeToString,
        ),
        "ProductDelete": grpc.unary_unary_rpc_method_handler(
            servicer.ProductDelete,
            request_deserializer=v1_dot_sales_dot_product__pb2.ProductDeleteRequest.FromString,
            response_serializer=v1_dot_sales_dot_product__pb2.ProductDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.sales.product.ProductService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class ProductService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ProductCreate(
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
            "/pro.omni.oms.api.v1.sales.product.ProductService/ProductCreate",
            v1_dot_sales_dot_product__pb2.ProductCreateRequest.SerializeToString,
            v1_dot_sales_dot_product__pb2.ProductCreateResponse.FromString,
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
    def ProductRead(
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
            "/pro.omni.oms.api.v1.sales.product.ProductService/ProductRead",
            v1_dot_sales_dot_product__pb2.ProductReadRequest.SerializeToString,
            v1_dot_sales_dot_product__pb2.ProductReadResponse.FromString,
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
    def ProductUpdate(
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
            "/pro.omni.oms.api.v1.sales.product.ProductService/ProductUpdate",
            v1_dot_sales_dot_product__pb2.ProductUpdateRequest.SerializeToString,
            v1_dot_sales_dot_product__pb2.ProductUpdateResponse.FromString,
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
    def ProductDelete(
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
            "/pro.omni.oms.api.v1.sales.product.ProductService/ProductDelete",
            v1_dot_sales_dot_product__pb2.ProductDeleteRequest.SerializeToString,
            v1_dot_sales_dot_product__pb2.ProductDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
