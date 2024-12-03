from google.protobuf.descriptor_pool import DescriptorPool
from grpc_reflection.v1alpha import reflection
from grpc_reflection.v1alpha.proto_reflection_descriptor_database import ProtoReflectionDescriptorDatabase
from omni_pro_base.config import Config
from omni_pro_grpc.grpc_connector import OmniChannel
from omni_pro_grpc.grpc_function import MethodRPCFunction, MicroServiceRPCFunction
from omni_pro_grpc.util import MessageToDict
from omni_pro_redis.redis import RedisManager


class OmniServerDescriptor:
    @classmethod
    def describe_server(cls, microservice, context: dict, *args, **kwargs) -> list:
        """
        Describe the server by retrieving information about the gRPC services and methods.

        Args:
            microservice: Microservice.
            context (dict): The context containing additional information.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            list: A list of dictionaries containing information about the gRPC services and methods.

        """
        with OmniChannel(
            microservice.code,
            options=[
                ("grpc.max_receive_message_length", 100 * 1024 * 1024),
                ("grpc.max_send_message_length", 100 * 1024 * 1024),
            ],
            *args,
            **kwargs,
            tennat=context["tenant"],
        ) as channel:
            reflection_db = ProtoReflectionDescriptorDatabase(channel)
            services = reflection_db.get_services()
            service_info_list = []
            not_ms_method_grpc = next(
                filter(lambda x: x.get("code") == "not_ms_method_grpc", MessageToDict(microservice.settings)), {}
            ).get("value", [])
            for service in services:
                if service == reflection.SERVICE_NAME:
                    continue
                desc_pool = DescriptorPool(reflection_db)
                service_desc = desc_pool.FindServiceByName(service)
                mod_name = service_desc.file.name.replace(".proto", "").replace("/", ".")
                for method in service_desc.methods:
                    input_type = method.input_type
                    info = {
                        "module_grpc": f"{mod_name}_pb2_grpc",
                        "stub_classname": f"{service_desc.name}Stub",
                        "module_pb2": f"{mod_name}_pb2",
                        "rpc_method": method.name,
                        "request_class": input_type.name,
                        # "response_class": method.output_type.name,
                    }
                    code = f"{info['module_pb2']}.{service_desc.name}.{info['rpc_method']}"
                    ms_data = {"microservice_id": ""}
                    if code not in not_ms_method_grpc:
                        ms_data = {"microservice_id": microservice.id}
                    resp = MethodRPCFunction(context=context).create_or_update(
                        params={
                            "data": {
                                "name": info["rpc_method"],
                                "code": code,
                                "module_grpc": info["module_grpc"],
                                "class_name": info["stub_classname"],
                                "module_pb2": info["module_pb2"],
                                "method": info["rpc_method"],
                                "request": info["request_class"],
                            }
                            | ms_data,
                            "filter": {"filter": {"filter": f"[('code', '=', '{code}')]"}},
                        }
                    )
                    service_info_list.append({"info": info, "proto": resp[0].method_grpc if resp[1] else None})

            return service_info_list

    @classmethod
    def register(cls, filters: dict, context: dict, *args, **kwargs):
        """
        Registers the server.

        Args:
            service_id (str): The ID of the service.
            context (dict): The context containing additional information.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        """
        resp = MicroServiceRPCFunction(context=context).read_ms(params=filters)
        all_services = []
        for microservice in resp[0].microservices:
            all_services.extend(
                cls.describe_server(
                    microservice=microservice,
                    context=context,
                    *args,
                    **kwargs,
                )
            )
        return all_services

    @classmethod
    def run(cls, pattern="*", exlcudes_keys=["SETTINGS"], filters={}) -> list:
        """
        Executes the main logic of the program.

        Args:
            pattern (str, optional): A pattern to filter the tenant codes. Defaults to "*".
            exlcudes_keys (list, optional): A list of keys to exclude from the tenant codes. Defaults to ["SETTINGS"].
            filters (dict, optional): A dictionary of filters to apply. Defaults to {}.

        Returns:
            list: A list of all services.

        """
        redis_manager = RedisManager(
            host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB, redis_ssl=Config.REDIS_SSL
        )
        tenans = redis_manager.get_tenant_codes(pattern=pattern, exlcudes_keys=exlcudes_keys)
        for tenant in tenans:
            context = {
                "tenant": tenant,
                "user": "internal",
            }
            resp = MicroServiceRPCFunction(context=context).read_ms(params={"filter": filters})
            all_services = []
            for micorservice in resp[0].microservices:
                all_services.extend(
                    cls.describe_server(
                        microservice=micorservice,
                        context=context,
                    )
                )
            return all_services
