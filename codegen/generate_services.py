import ast
import copy
import operator
import re
import textwrap
import typing
from collections import defaultdict
from re import A

from attr import Attribute
from black import KEYWORDS

from codegen.generate_abstract import AbstractModuleGenerator
from codegen.service_processor import (
    ServiceDomain,
    ServiceMethod,
    ServiceParameter,
    TraitInfo,
)
from codegen.utils import format_docstring, snakeit


class ServiceModuleGenerator(AbstractModuleGenerator):
    """Generate the service files"""

    def __init__(self, types, with_async=False):
        self._async = with_async
        self._types = {t.name: t for t in types}
        self._services: typing.Dict[str, ServiceDomain] = {}
        self._trait_nodes: typing.List[typing.List[ast.AST]] = []
        self._service_nodes: typing.Dict[str, typing.List[ast.AST]] = defaultdict(list)
        self._schema_nodes: typing.Dict[str, typing.Dict[str, ast.AST]] = defaultdict(
            dict
        )
        super().__init__()

    def get_module_nodes(self):
        result = {}
        modules = self._service_nodes.keys()

        for module in modules:
            self.add_import_statement(module, "typing")

            self.add_import_statement(module, ".", "abstract")
            self.add_import_statement(module, ".", "traits")
            self.add_import_statement(
                module, "commercetools.helpers", "RemoveEmptyValuesMixin"
            )
            self.add_import_statement(module, "commercetools.typing", "OptionalListStr")

            all_nodes = (
                self._import_nodes[module]
                + list(self._schema_nodes[module].values())
                + self._service_nodes[module]
            )
            value = ast.Module(body=all_nodes)
            result[module] = {"name": self._generate_module_name(module), "ast": value}

        result["traits"] = {"name": "traits", "ast": self._generate_trait_file()}

        result["__init__"] = {
            "name": "__init__",
            "ast": _generate_init_file(self._services, result),
        }
        return result

    def _generate_module_name(self, name: str):
        """Generate the module name (filename) for the service.

        These are mostly special cases to keep backwards compatibility with
        previously hand written files.

        """
        fixed_mapping = {
            "me": "me",
            "login": "login",
            "category": "categories",
            "inventory_entry": "inventory",
            "tax_category": "tax_categories",
            "project": "project",
        }
        if name in fixed_mapping:
            return fixed_mapping[name]

        if not name.endswith("s"):
            name += "s"
        return name

    def add_service(self, service: ServiceDomain):
        module_name = snakeit(service.context_name)
        node = self.create_class(service, module_name)
        if node:
            self._services[service.context_name] = service
            self._service_nodes[module_name].append(node)

    def add_trait(self, trait: TraitInfo):
        node = _create_trait_schema(trait)
        if node:
            self._trait_nodes.append(node)

    def add_schema(self, context_name: str, schema_node: ast.ClassDef):
        module_name = snakeit(context_name)
        self._schema_nodes[module_name][schema_node.name] = schema_node

    def create_class(self, service: ServiceDomain, module_name: str):
        """Create the service class and it's methods."""
        assert service

        # Define the base class
        class_node = ast.ClassDef(
            name=service.context_name + "Service",
            bases=[ast.Name(id="abstract.AbstractService")],
            keywords=[],
            decorator_list=[],
            body=[],
        )

        # Add the docstring to the class
        if service.description:
            class_node.body.append(
                ast.Expr(
                    ast.Constant(
                        value=format_docstring(service.description, indent=1), kind=None
                    )
                )
            )

        # Bit of magic to keep the ordering roughly the same as the manually
        # created service modules to minimize the diff
        ordering = ["get", "query", "create", "update", "delete", "action"]
        sorted_methods = defaultdict(list)
        for method in service.methods:
            if method.type not in ordering:
                assert "Missing item"
            sorted_methods[method.type].append(method)

        for method_type in sorted_methods:
            sorted_methods[method_type].sort(key=operator.attrgetter("name"))

        for item in ordering:
            for method in sorted_methods[item]:
                print(" - ", method.name)
                assert method is not None, (
                    "Service %s has None method" % service.context_name
                )

                node = self.create_method(class_node, method, module_name)

        return class_node

    def create_method(
        self, class_node: ast.ClassDef, method: ServiceMethod, module_name: str
    ):
        """Add the method to the service class"""
        node = ast.FunctionDef(
            name=method.name,
            args=ast.arguments(
                args=[ast.arg(arg="self", annotation=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[],
            decorator_list=[],
            returns=None,
        )

        for param in method.path_params:
            node.args.args.append(_param_ast(param))

        for param in method.query_params:
            if param.required:
                node.args.args.append(_param_ast(param))
            else:
                node.args.kwonlyargs.append(_param_ast(param))
                node.args.kw_defaults.append(ast.NameConstant(value=None, kind=None))

        return_obj = self._types.get(method.returns)
        if return_obj:
            self.add_import_statement(
                module_name,
                f"commercetools.types.{return_obj.package_name}",
                return_obj.name,
            )
            node.returns = ast.Name(id=return_obj.name)
            if self._async:
                node.returns = ast.Subscript(
                    value=ast.Attribute(value=ast.Name(id="typing"), attr="Awaitable"),
                    slice=ast.Index(value=node.returns)
                )

        # Add docstring
        if method.description:
            node.body.append(
                ast.Expr(
                    value=ast.Constant(
                        value=format_docstring(method.description, indent=2), kind=None
                    )
                )
            )

        self.make_serialize_query_params(method, node, module_name)

        # Generate the method body
        if method.type == "get":
            node = self.make_get_method(method, node, return_obj, module_name)
        elif method.type == "create":
            node = self.make_create_method(method, node, return_obj, module_name)

            # TODO: Add deprecation warning
            if method.context_name == "CustomObject" and method.name == "create":
                extra_method = copy.deepcopy(node)
                extra_method.name = "create_or_update"
                class_node.body.append(extra_method)

        elif method.type == "query":
            node = self.make_query_method(method, node, return_obj, module_name)
        elif method.type == "update":
            node = self.make_update_method(method, node, return_obj, module_name)
        elif method.type == "delete":
            node = self.make_delete_method(method, node, return_obj, module_name)
        elif method.type == "action":

            # TODO: Add deprecation warning
            if method.context_name == "Product" and method.name == "images":
                node.name = "upload_image"
                extra_method = copy.deepcopy(node)
                extra_method.name = "file_upload"
                class_node.body.append(extra_method)

            node = self.make_action_method(method, node, return_obj, module_name)
        else:
            raise NotImplementedError(method.type)

        if node:
            if not node.body:
                node.body.append(ast.Pass())

            class_node.body.append(node)
        else:
            print(
                f"Skipping method {method.context_name}.{method.name} since we couldn't generate it"
            )

    def make_get_method(self, method, node, return_obj, module_name):
        """Create the `.get_*()` method"""
        schema_name = return_obj.name + "Schema"
        self.add_import_statement(
            module_name,
            f"commercetools._schemas.{return_obj.package_name}",
            schema_name,
        )
        node.body.append(
            ast.Return(
                self._call_client(
                    method="_get",
                    endpoint=_create_endpoint_fstring(method.path),
                    params=ast.Name("params"),
                    response_schema_cls=ast.Name(id=schema_name),
                )
            )
        )

        return node

    def make_create_method(self, method, node, return_obj, module_name):
        """Create the `.create(self, draft, ...)` method"""
        input_obj = self._types.get(method.input_type)
        input_schema_name = None

        # Import response schema
        response_schema_name = return_obj.name + "Schema"
        self.add_import_statement(
            module_name,
            f"commercetools._schemas.{return_obj.package_name}",
            response_schema_name,
        )

        if input_obj:
            input_schema_name = input_obj.name + "Schema"

            self.add_import_statement(
                module_name,
                f"commercetools.types.{input_obj.package_name}",
                input_obj.name,
            )
            self.add_import_statement(
                module_name,
                f"commercetools._schemas.{input_obj.package_name}",
                input_schema_name,
            )
            node.args.args.insert(
                len(method.path_params) + 1,
                ast.arg(arg="draft", annotation=ast.Name(id=input_obj.name)),
            )

        node.body.append(
            ast.Return(
                self._call_client(
                    method="_post",
                    endpoint=_create_endpoint_fstring(method.path),
                    params=ast.Name("params"),
                    data_object=ast.Name("draft") if input_obj else None,
                    request_schema_cls=ast.Name(id=input_schema_name)
                    if input_schema_name
                    else None,
                    response_schema_cls=ast.Name(id=response_schema_name)
                    if response_schema_name
                    else None,
                )
            )
        )
        return node

    def make_query_method(self, method, node, return_obj, module_name):
        """Create the `.query(self, input, ...)` method"""
        # Import response schema
        response_schema_name = return_obj.name + "Schema"
        self.add_import_statement(
            module_name,
            f"commercetools._schemas.{return_obj.package_name}",
            response_schema_name,
        )

        node.body.append(
            ast.Return(
                self._call_client(
                    method="_get",
                    endpoint=_create_endpoint_fstring(method.path),
                    params=ast.Name("params"),
                    response_schema_cls=ast.Name(id=response_schema_name)
                    if response_schema_name
                    else None,
                )
            )
        )
        return node

    def make_update_method(self, method, node, return_obj, module_name):
        """Create the `.update_by_*(self, id, actions, ...)` method"""
        response_schema_name = return_obj.name + "Schema"
        self.add_import_statement(
            module_name,
            f"commercetools._schemas.{return_obj.package_name}",
            response_schema_name,
        )

        input_obj = self._types.get(method.input_type)
        if not input_obj:
            return
        action_obj = self._types.get(method.input_type + "Action")
        input_schema_name = input_obj.name + "Schema"

        self.add_import_statement(
            module_name, f"commercetools.types.{input_obj.package_name}", input_obj.name
        )
        self.add_import_statement(
            module_name,
            f"commercetools.types.{action_obj.package_name}",
            action_obj.name,
        )
        self.add_import_statement(
            module_name,
            f"commercetools._schemas.{input_obj.package_name}",
            input_schema_name,
        )

        node.args.args.append(
            ast.arg(
                arg="actions",
                annotation=ast.Subscript(
                    value=ast.Name(id="typing.List"),
                    slice=ast.Index(value=ast.Name(id=action_obj.name)),
                ),
            )
        )
        node.args.kwonlyargs.append(
            ast.arg(arg="force_update", annotation=ast.Name(id="bool"))
        )
        node.args.kw_defaults.append(ast.Constant(value=False, kind=None))

        # update_action = types.ProductUpdate(version=version, actions=actions)
        node.body.append(
            ast.Assign(
                targets=[ast.Name(id="update_action")],
                value=ast.Call(
                    func=ast.Name(id=input_obj.name),
                    args=[],
                    keywords=[
                        ast.keyword(arg="version", value=ast.Name(id="version")),
                        ast.keyword(arg="actions", value=ast.Name(id="actions")),
                    ],
                ),
            )
        )

        node.body.append(
            ast.Return(
                self._call_client(
                    method=f"_post",
                    endpoint=_create_endpoint_fstring(method.path),
                    params=ast.Name("params"),
                    data_object=ast.Name("update_action"),
                    request_schema_cls=ast.Name(id=input_schema_name),
                    response_schema_cls=ast.Name(id=response_schema_name),
                    force_update=ast.Name(id="force_update"),
                )
            )
        )
        return node

    def make_delete_method(self, method, node, return_obj, module_name):
        """Create the `.delete_by_*(self, id, version, ...)` method"""
        node.args.kwonlyargs.append(
            ast.arg(arg="force_delete", annotation=ast.Name(id="bool"))
        )
        node.args.kw_defaults.append(ast.Constant(value=False, kind=None))

        response_schema_name = None
        if return_obj:
            response_schema_name = return_obj.name + "Schema"
            self.add_import_statement(
                module_name,
                f"commercetools._schemas.{return_obj.package_name}",
                response_schema_name,
            )

        node.body.append(
            ast.Return(
                self._call_client(
                    method="_delete",
                    endpoint=_create_endpoint_fstring(method.path),
                    params=ast.Name("params"),
                    response_schema_cls=ast.Name(id=response_schema_name),
                    force_delete=ast.Name(id="force_delete"),
                )
            )
        )
        return node

    def make_action_method(self, method, node, return_obj, module_name):
        """Create an action method, e.g. `.replicate*(self, draft, ...)`"""

        response_schema_name = None
        if return_obj:
            response_schema_name = return_obj.name + "Schema"
            self.add_import_statement(
                module_name,
                f"commercetools._schemas.{return_obj.package_name}",
                response_schema_name,
            )

        input_obj = self._types.get(method.input_type)
        input_name = None
        input_schema_name = None

        if input_obj:
            input_name = "draft" if "Draft" in input_obj.name else "action"

            input_schema_name = input_obj.name + "Schema"

            self.add_import_statement(
                module_name,
                f"commercetools.types.{input_obj.package_name}",
                input_obj.name,
            )
            self.add_import_statement(
                module_name,
                f"commercetools._schemas.{input_obj.package_name}",
                input_schema_name,
            )

            node.args.args.insert(
                len(method.path_params) + 1,
                ast.arg(arg=input_name, annotation=ast.Name(id=input_obj.name)),
            )

        node.body.append(
            ast.Return(
                self._call_client(
                    method=f"_{method.method}",
                    endpoint=_create_endpoint_fstring(method.path),
                    params=ast.Name("params"),
                    data_object=ast.Name(input_name) if input_name else None,
                    request_schema_cls=ast.Name(id=input_schema_name)
                    if input_schema_name
                    else None,
                    response_schema_cls=ast.Name(id=response_schema_name)
                    if response_schema_name
                    else None,
                    file=ast.Name("fh") if method.is_fileupload else None,
                )
            )
        )
        return node

    def _call_client(
        self,
        method,
        endpoint=None,
        params=None,
        data_object=None,
        request_schema_cls=None,
        response_schema_cls=None,
        **kwargs,
    ):
        """Create the actual call to `self.client._get()` or `self.client._post()`"""
        keywords = []
        if endpoint:
            keywords.append(ast.keyword(arg="endpoint", value=endpoint))
        if params:
            keywords.append(ast.keyword(arg="params", value=params))
        if data_object:
            keywords.append(ast.keyword(arg="data_object", value=data_object))

        if request_schema_cls:
            keywords.append(
                ast.keyword(arg="request_schema_cls", value=request_schema_cls)
            )

        if response_schema_cls:
            if method == "_get":
                keywords.append(
                    ast.keyword(arg="schema_cls", value=response_schema_cls)
                )
            else:
                keywords.append(
                    ast.keyword(arg="response_schema_cls", value=response_schema_cls)
                )

        for key, value in kwargs.items():
            if value is not None:
                keywords.append(ast.keyword(arg=key, value=value))

        node = ast.Call(
            func=ast.Attribute(
                value=ast.Attribute(value=ast.Name(id="self"), attr="_client"),
                attr=method,
            ),
            args=[],
            keywords=keywords,
        )
        return node

    def make_serialize_query_params(
        self, method: ServiceMethod, node, module_name: str
    ):
        """Code to serialize optional parameters to the `params` dict passed to
        the client post/get call.

        This method might also optionally generate a marshmallow schema where it
        uses the various traits as base classes.

        """
        query_params = {
            param.name: param for param in method.query_params if param.type != "file"
        }

        # TODO: This should be fixed in the raml specifications since version is
        # part of the body and not part of the query parmaters for update calls
        if method.type == "update" and "version" in query_params:
            del query_params["version"]

        # If this method doesn't accept parameters we just exit early with a
        # `params = {}` line.
        if not query_params:
            line = ast.Assign(
                targets=[ast.Name(id="params")], value=ast.Dict(keys=[], values=[])
            )
            node.body.append(line)
            return

        bases = []
        for trait in method.traits:
            if trait.params:
                bases.append(ast.Name(id="traits.%sSchema" % trait.class_name))

        # Generate a custom schema if required
        if method.extra_params or len(bases) != 1:

            if method.type != "action":
                schema_name = f"_{method.context_name}{method.type.title()}Schema"
            else:
                schema_name = f"_{method.context_name}{method.name.title()}Schema"

            if not bases:
                self.add_import_statement(module_name, "marshmallow", "fields")
                self.add_import_statement(module_name, "marshmallow")

                bases = [
                    ast.Name(id="marshmallow.Schema"),
                    ast.Name(id="RemoveEmptyValuesMixin"),
                ]

            schema_node = ast.ClassDef(
                name=schema_name, bases=bases, keywords=[], decorator_list=[], body=[]
            )

            # Marshmallow field definitions
            schema_methods = []
            for param in method.extra_params:

                # We skip files since we post the value in the request body
                if param.type == "file":
                    continue

                field_node, methods, imports = _create_schema_field(param)
                if field_node:
                    schema_node.body.append(field_node)
                    schema_methods.extend(methods)
                    for import_ in imports:
                        self.add_import_statement(module_name, *import_)

            schema_node.body.extend(schema_methods)
            if not schema_node.body:
                schema_node.body.append(ast.Pass())

            self.add_schema(method.context_name, schema_node)
        else:
            schema_name = bases[0].id

        # params = self._serialize_params({}, schema)
        input_params = {}
        for key, param in query_params.items():
            if key.startswith("/"):
                key = snakeit(param.extra_data["(placeholderParam)"]["paramName"])
            input_params[key] = snakeit(key)

        line = ast.Assign(
            targets=[ast.Name(id="params")],
            value=ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="_serialize_params"),
                args=[
                    ast.Dict(
                        keys=[ast.Str(s=val, kind="") for val in input_params.keys()],
                        values=[ast.Name(id=val) for val in input_params.values()],
                    ),
                    ast.Name(id=schema_name),
                ],
                keywords=[],
            ),
        )
        node.body.append(line)

    def _generate_trait_file(self):
        """Generate the traits.py file which contains marshmallow schema's for
        the various traits.

        For example ExpandableSchema, QuerySchema etc. Only used to serialize
        the query parameters for now.

        It uses the `self._trait_nodes` to write the body.

        """
        nodes = [
            ast.Import(names=[ast.alias(name="marshmallow", asname=None)], level=0),
            ast.ImportFrom(
                module="marshmallow",
                names=[ast.alias(name="fields", asname=None)],
                level=0,
            ),
            ast.ImportFrom(
                module="commercetools.helpers",
                names=[ast.alias(name="RemoveEmptyValuesMixin", asname=None)],
                level=0,
            ),
            ast.ImportFrom(
                module="commercetools.helpers",
                names=[ast.alias(name="OptionalList", asname=None)],
                level=0,
            ),
        ]
        nodes.extend(self._trait_nodes)
        return ast.Module(body=nodes)


def _generate_init_file(services, modules):
    """Generate the __init__.py file which contains the ServicsMixin for
    the client.

    This is mostly to automate the addition of new services.

    """
    nodes = []

    nodes.append(ast.Import(names=[ast.alias(name="typing", asname=None)], level=0))
    nodes.append(
        ast.ImportFrom(
            module="cached_property",
            names=[ast.alias(name="cached_property", asname=None)],
            level=0,
        )
    )

    # Collect all submodules
    submodules = {}
    for service in services.values():
        module_name = snakeit(service.context_name)
        service_name = service.context_name + "Service"
        info = modules[module_name]

        key = ".%s" % info["name"]
        submodules[key] = {
            "module_name": info["name"],
            "class_name": service.context_name + "Service",
            "var_name": snakeit(service.context_name),
        }

    # Add manual generated files (TODO)
    submodules[".project"] = {
        "module_name": "project",
        "class_name": "ProjectService",
        "var_name": "project",
    }

    # Generate TYPE_CHECKING import statements (these will be sorted by isort).
    if_node = ast.If(
        test=ast.Attribute(value=ast.Name(id="typing"), attr="TYPE_CHECKING"),
        body=[],
        orelse=[],
    )
    nodes.append(if_node)
    for name, service in submodules.items():
        node = ast.ImportFrom(
            module=name,
            names=[ast.alias(name=service["class_name"], asname=None)],
            level=0,
        )
        if_node.body.append(node)

    module_varnames = sorted(submodules.values(), key=operator.itemgetter("var_name"))

    # Return the class + properties
    name = "ServicesMixin" if not self._async else "AsyncServicesMixin"
    class_node = ast.ClassDef(
        name=name, bases=[], keywords=[], decorator_list=[], body=[]
    )
    for name, service in submodules.items():
        node = ast.FunctionDef(
            name=service["module_name"],
            args=ast.arguments(
                args=[ast.arg(arg="self", annotation=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[],
            decorator_list=[ast.Name(id="cached_property")],
            returns=ast.Str(s=service["class_name"], kind=None),
        )
        node.body.append(
            ast.ImportFrom(
                module=name,
                names=[ast.alias(name=service["class_name"], asname=None)],
                level=0,
            )
        )
        node.body.append(
            ast.Return(
                ast.Call(
                    func=ast.Name(id=service["class_name"]),
                    args=[ast.Name(id="self")],
                    keywords=[],
                )
            )
        )
        class_node.body.append(node)

    nodes.append(class_node)

    return ast.Module(body=nodes)


def _create_trait_schema(trait: TraitInfo) -> ast.ClassDef:
    """Create a Marshmallow Schema class for a Trait.

    This for example creates the QuerySchema or the PriceSelectingSchema.

    """
    if not trait.params:
        return

    schema_name = trait.class_name + "Schema"
    schema_node = ast.ClassDef(
        name=schema_name,
        bases=[
            ast.Name(id="marshmallow.Schema"),
            ast.Name(id="RemoveEmptyValuesMixin"),
        ],
        keywords=[],
        decorator_list=[],
        body=[],
    )

    # Marshmallow field definitions
    schema_methods = []
    for param in trait.params:
        node, methods, imports = _create_schema_field(param)
        if node:
            schema_methods.extend(methods)
            schema_node.body.append(node)

    schema_node.body.extend(schema_methods)

    return schema_node


def _create_schema_field(param: ServiceParameter):
    """Generate a field assignment for a marshmallow schema"""
    keywords = []
    imports = []
    methods = []
    code_name = snakeit(param.name)
    if code_name != param.name:
        keywords.append(
            ast.keyword(arg="data_key", value=ast.Str(s=param.name, kind=None))
        )
    if not param.required:
        keywords.append(
            ast.keyword(arg="required", value=ast.Constant(value=False, kind=None))
        )

    if param.name.startswith("/"):
        placeholder = param.extra_data["(placeholderParam)"]
        code_name = snakeit(placeholder["paramName"])
        imports.append(("marshmallow", "fields"))
        imports.append(("marshmallow",))
        serialize_func = ast.Call(
            func=ast.Attribute(value=ast.Name(id="fields"), attr="Dict"),
            args=[],
            keywords=[],
        )

        # TODO: can break if there is a suffix
        key_name = placeholder["template"].replace(
            "<%s>" % placeholder["placeholder"], ""
        )
        code = ast.parse(
            textwrap.dedent(
                """
            @marshmallow.post_dump
            def _%(target_name)s_post_dump(self, data, **kwrags):
                values = data.pop('%(target_name)s')
                if not values:
                    return data
                for key, val in values.items():
                    data[f"%(key_name)s{key}"] = val
                return data

            @marshmallow.pre_load
            def _%(target_name)s_post_load(self, data, **kwrags):
                items = {}
                for key in list(data.keys()):
                    if key.startswith("%(key_name)s"):
                        items[key[%(key_len)d:]] = data[key]
                        del data[key]
                data["%(target_name)s"] = items
                return data
        """
                % {
                    "target_name": code_name,
                    "key_name": key_name,
                    "key_len": len(key_name),
                }
            )
        )
        methods.extend(code.body)

    elif param.type == "string":
        imports.append(("commercetools.helpers", "OptionalList"))
        imports.append(("marshmallow", "fields"))
        serialize_func = ast.Call(
            func=ast.Name(id="OptionalList"),
            args=[
                ast.Call(
                    func=ast.Attribute(value=ast.Name(id="fields"), attr="String"),
                    args=[],
                    keywords=[],
                )
            ],
            keywords=keywords,
        )
    elif param.type == "number":
        imports.append(("marshmallow", "fields"))
        serialize_func = ast.Call(
            func=ast.Attribute(value=ast.Name(id="fields"), attr="Int"),
            args=[],
            keywords=keywords,
        )

    elif param.type == "boolean":
        keywords.append(
            ast.keyword(arg="missing", value=ast.Constant(value=False, kind=None))
        )
        imports.append(("marshmallow", "fields"))
        serialize_func = ast.Call(
            func=ast.Attribute(value=ast.Name(id="fields"), attr="Bool"),
            args=[],
            keywords=keywords,
        )
    elif param.type == "file":
        return None, []
    else:
        raise NotImplementedError(param)

    node = ast.Assign(targets=[ast.Name(id=code_name)], value=serialize_func, simple=1)
    return node, methods, imports


def _create_endpoint_fstring(value: str) -> typing.Union[ast.Str, ast.JoinedStr]:
    """Create the value for the `endpoint=..` parameter in the client.

    If the parameter doesn't contain a var a regular string is returned,
    otherwise an f-string is created and returned.

    Note that this method assumes that the parameters in the endpoint are kept
    'intact'. E.g. the raml specifices `/{container}/{key}` so we assume that
    those variables are available in the scope when we create the f-string.

    """
    parts = []
    last = 0
    value = value.lstrip("/")
    for m in re.finditer("{[^}]+}", value):
        parts.append(ast.Constant(value=value[last : m.start()]))

        identifier = snakeit(value[m.start() + 1 : m.end() - 1])
        parts.append(
            ast.FormattedValue(
                value=ast.Name(identifier), conversion=-1, format_spec=None
            )
        )
        last = m.end()
    if last != len(value):
        parts.append(ast.Constant(value=value[last : len(value)]))

    # If no values are in the f-string we can just generate a regular string
    if len(parts) == 1:
        return ast.Str(s=parts[0].value, kind=None)

    return ast.JoinedStr(values=parts)


def _param_ast(param: ServiceParameter) -> ast.arg:
    """Create the ast node for the parameter of a function.

    This can be typed.

    """
    if param.name.startswith("/"):
        annotation = ast.Dict(keys=None, values=None)

        annotation = ast.Subscript(
            value=ast.Attribute(value=ast.Name(id="typing"), attr="Dict"),
            slice=ast.Index(
                value=ast.Tuple(elts=[ast.Name(id="str"), ast.Name(id="str")])
            ),
        )

        return ast.arg(
            arg=snakeit(param.extra_data["(placeholderParam)"]["paramName"]),
            annotation=annotation,
        )

    annotation = None
    if param.type == "string":
        if param.multiple:
            annotation = ast.Name(id="OptionalListStr")
        else:
            annotation = ast.Name(id="str")
    elif param.type == "number":
        annotation = ast.Name(id="int")
    elif param.type == "boolean":
        annotation = ast.Name(id="bool")
    elif param.type == "file":
        annotation = ast.Name(id="typing.BinaryIO")
    return ast.arg(arg=snakeit(param.name), annotation=annotation)
