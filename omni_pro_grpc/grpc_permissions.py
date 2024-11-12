import argparse
import importlib
import json
import re
from pathlib import Path


class GRPCPermissionExtractor:
    def __init__(self, base_module: str):
        self.base_module = Path(base_module)
        self.base_path = self.get_module_path(base_module)

    def get_module_path(self, module_name: str) -> Path:
        """
        Get the file path of the specified module.
        Args:
            module_name (str): The name of the module to get the path for.
        Returns:
            Path: The parent directory of the module's file.
        """
        module = importlib.import_module(module_name)
        return Path(module.__file__).parent

    def to_permission_name(self, method_name: str) -> str:
        """
        Convert a method name to a permission name.
        Args:
            method_name (str): The name of the method to convert.
        Returns:
            str: The permission name
        """
        # Convert CamelCase to snake_case and uppercase it
        snake_case = re.sub(r"(?<!^)(?=[A-Z])", "_", method_name).upper()
        return f"CAN_{snake_case}"

    def extract_from_package(self, module_path: Path) -> dict:
        """
        Extracts service method permissions from gRPC Python files in a given module directory.
        Args:
            module_path (Path): The path to the module directory containing gRPC Python files.
        Returns:
            dict: A dictionary where keys are service names and values are lists of transformed method names.
        """

        permissions = {}

        # List all files in the module directory
        for file_path in module_path.iterdir():
            if (file_name := file_path.name).endswith("_pb2_grpc.py"):
                # Remove the _pb2_grpc.py suffix
                service_name = file_name.replace("_pb2_grpc.py", "")

                # Construct the file path
                # file_path = os.path.join(module_path, file_name)

                # Read the file to find Service classes
                with open(file_path, "r") as file:
                    content = file.read()

                matches = re.findall(r"class (\w+Service)\(.*?\):\n(.*?)(?=\nclass|\Z)", content, re.DOTALL)
                for class_name, class_body in matches:
                    # Extract methods
                    method_names = re.findall(r"def (\w+?)\(", class_body)
                    # Transform method names
                    permissions[service_name] = [self.to_permission_name(name) for name in method_names]

        return permissions

    def extract_from_multiple_package(self) -> dict:
        """
        Extracts permissions from all modules within the base package directory.
        This method iterates over all directories in the base package path, and for each directory,
        it calls the `extract_from_package` method to extract permissions. The extracted permissions
        are then stored in a dictionary with the package name as the key.
        Returns:
            dict: A dictionary where keys are package names and values are dictionaries with a "permissions" key.
        """

        structure = {}

        # List all directories in the base package
        for package_name in self.base_path.iterdir():
            package_path = package_name

            if package_path.is_dir():
                # Extract permissions from each package
                service_permissions = self.extract_from_package(package_path)

                if service_permissions:
                    structure[package_name.name] = {"permissions": service_permissions}

        return structure


def main():
    parser = argparse.ArgumentParser(
        description="GRPC Permission Extractor",
        usage="python -m omni_pro_grpc.grpc_permissions package [{single,multi}]",
        epilog="""Example: python -m omni_pro_grpc.grpc_permissions omni_pro_grpc.v1.utilities -m single
        python -m omni_pro_grpc.grpc_permissions omni_pro_grpc.v1 -m multi""",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("package", help="El paquete base para extraer permisos, por ejemplo: omni_pro_grpc.v1")
    parser.add_argument(
        "-m",
        "--mode",
        choices=["single", "multi"],
        help="Indica si se extraen los permisos de un paquete o de varios",
        default="multi",
    )

    args = parser.parse_args()

    perm_extract = GRPCPermissionExtractor(args.package)
    if args.mode == "single":
        print(json.dumps({"permissions": perm_extract.extract_from_package(perm_extract.base_path)}, indent=4))
    else:
        print(json.dumps(perm_extract.extract_from_multiple_package(), indent=4))


if __name__ == "__main__":
    main()
