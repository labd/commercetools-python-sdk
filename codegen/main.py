import os
import typing
from pathlib import Path

import astor
import black
import isort.api

from codegen.generate_schema import SchemaModuleGenerator
from codegen.generate_services import ServiceModuleGenerator
from codegen.generate_types import TypesModuleGenerator
from codegen.service_processor import ServiceProcessor
from codegen.type_processor import TypeProcessor
from codegen.yaml import read_raml_file


def parse_raml_file(filename) -> typing.Dict[str, typing.Any]:
    data = read_raml_file(filename)
    types = TypeProcessor()
    types.load(data["types"])
    services = ServiceProcessor()
    services.load(data)
    return {"types": types, "resources": data, "services": services}


def generate_types_module(types):
    generator = TypesModuleGenerator()
    for resource in types:
        generator.add_type_definition(resource)
    return generator.get_module_nodes()


def generate_schemas_modules(types):
    generator = SchemaModuleGenerator(types)
    for resource in types:
        generator.add_type_definition(resource)
    return generator.get_module_nodes()


def generate_services_modules(services: ServiceProcessor, types):
    generator = ServiceModuleGenerator(types)
    for trait in services.traits.values():
        generator.add_trait(trait)

    for service in services:
        generator.add_service(service)
    return generator.get_module_nodes()


def generate():
    raml = parse_raml_file("../commercetools-api-reference/api-specs/api/api.raml")

    types = raml["types"].types.values()
    services = raml["services"]

    path = os.path.join("src", "commercetools")
    try:
        os.makedirs(path)
    except FileExistsError:
        pass

    # Generate services.py
    ast_nodes = generate_services_modules(services, types)
    target_path = os.path.join(path, "services")
    if not os.path.exists(target_path):
        os.mkdir(target_path)

    for name, metadata in ast_nodes.items():
        filename = os.path.join(target_path, metadata["name"] + ".py")
        write_module(filename, metadata["ast"])

    # Generate types.py
    ast_nodes = generate_types_module(types)
    target_path = os.path.join(path, "types")
    if not os.path.exists(target_path):
        os.mkdir(target_path)

    for name, module_ast in ast_nodes.items():
        filename = os.path.join(target_path, f"{name}.py")
        write_module(filename, module_ast)

    # Generate schemas.py
    ast_nodes = generate_schemas_modules(types)
    target_path = os.path.join(path, "_schemas")
    if not os.path.exists(target_path):
        os.mkdir(target_path)

    for name, module_ast in ast_nodes.items():
        filename = os.path.join(target_path, f"{name}.py")
        write_module(filename, module_ast)


def write_module(filename, ast):
    content = astor.to_source(ast)
    with open(filename, "w") as fh:
        fh.write("# DO NOT EDIT! This file is automatically generated\n")
        fh.write(content)
    reformat_code(filename)


def reformat_code(filename: str):
    config = isort.api.Config()
    isort.api.sort_file(filename, config=config)

    src = Path(filename)
    report = black.Report()
    mode = black.FileMode(line_length=88)
    black.reformat_one(
        src=src,
        fast=False,
        write_back=black.WriteBack.YES,
        mode=mode,
        report=report,
    )
