import ast
import operator
import typing
from collections import defaultdict

from codegen import raml_types
from codegen.generate_abstract import AbstractModuleGenerator
from codegen.utils import reorder_class_definitions

FIELD_TYPES = {
    "string": "marshmallow.fields.String",
    "object": "marshmallow.fields.Dict",
    "float": "marshmallow.fields.Float",
    "number": "marshmallow.fields.Integer",
    "integer": "marshmallow.fields.Integer",
    "boolean": "marshmallow.fields.Bool",
    "array": "marshmallow.fields.List",
    "datetime": "marshmallow.fields.DateTime",
    "date-only": "marshmallow.fields.Date",
    "any": "marshmallow.fields.Raw",
}


class SchemaModuleGenerator(AbstractModuleGenerator):
    """This generator is responsible for generating the schemas.py file"""

    def __init__(self):
        self._field_nodes: typing.Dict[str, typing.List[ast.AST]] = defaultdict(list)
        self._type_nodes: typing.Dict[str, typing.List[ast.AST]] = defaultdict(list)
        self._type_nodes_map: typing.Dict[str, str] = {}
        super().__init__()

    def get_module_nodes(self):
        modules = list(set(self._field_nodes.keys()) | set(self._type_nodes.keys()))
        result = {}

        for module in modules:
            self.add_import_statement(module, "commercetools", "types")
            self.add_import_statement(module, "marshmallow")

            type_nodes = reorder_class_definitions(self._type_nodes[module])
            global_nodes = [
                ast.Assign(
                    targets=[ast.Name(id="__all__")],
                    value=ast.List(
                        elts=[
                            ast.Str(s=node.name, kind=None)
                            for node in sorted(
                                type_nodes, key=operator.attrgetter("name")
                            )
                        ]
                    ),
                )
            ]
            all_nodes = (
                self._import_nodes[module]
                + global_nodes
                + self._field_nodes[module]
                + type_nodes
            )
            value = ast.Module(body=all_nodes)
            result[module] = value

        result["__init__"] = self.generate_init_module(result.keys())
        return result

    def generate_init_module(self, modules):
        return ast.Module(body=[])

    def add_type_definition(self, resource):
        """Create a class definition"""
        if resource.name in FIELD_TYPES:
            return

        if "asMap" in resource.annotations:
            return self.add_dict_field_definition(resource, resource.package_name)

        return self.add_schema_definition(resource, resource.package_name)

    def add_schema_definition(self, resource, module_name):
        node = SchemaClassGenerator(resource, self).build()
        if node:
            self._type_nodes_map[node.name] = module_name
            self._type_nodes[module_name].append(node)

    def add_dict_field_definition(self, resource, module_name):
        base_class = ast.Name(id="marshmallow.fields.Dict")

        # Define the base class
        class_node = ast.ClassDef(
            name=resource.name + "Field",
            bases=[base_class],
            keywords=[],
            decorator_list=[],
            body=[],
        )

        class_node.body.append(
            ast.FunctionDef(
                name="_deserialize",
                args=ast.arguments(
                    args=[
                        ast.arg(arg="self", annotation=None),
                        ast.arg(arg="value", annotation=None),
                        ast.arg(arg="attr", annotation=None),
                        ast.arg(arg="data", annotation=None),
                    ],
                    vararg=None,
                    kwonlyargs=[],
                    kw_defaults=[],
                    kwarg=ast.arg(arg="kwargs", annotation=None),
                    defaults=[],
                ),
                body=[
                    ast.Assign(
                        targets=[ast.Name(id="result")],
                        value=ast.Call(
                            func=ast.Attribute(
                                value=ast.Call(
                                    func=ast.Name(id="super"), args=[], keywords=[]
                                ),
                                attr="_deserialize",
                            ),
                            args=[
                                ast.Name(id="value"),
                                ast.Name(id="attr"),
                                ast.Name(id="data"),
                            ],
                            kwarg=ast.arg(arg="kwargs", annotation=None),
                            keywords=[],
                        ),
                    ),
                    ast.Return(
                        value=ast.Call(
                            func=ast.Name(id="types." + resource.name),
                            args=[],
                            keywords=[
                                ast.keyword(arg=None, value=ast.Name(id="result"))
                            ],
                        )
                    ),
                ],
                decorator_list=[],
                returns=None,
            )
        )

        self._field_nodes[module_name].append(class_node)

    def import_resource(self, source, module, cls):
        self.add_import_statement(source, f"commercetools._schemas.{module}", cls)


class SchemaClassGenerator:
    """Create a marshmallow schema"""

    def __init__(
        self, resource: raml_types.DataType, generator: SchemaModuleGenerator
    ) -> None:
        self.resource = resource
        self.properties = resource.get_all_properties()
        self.contains_regex_field = any(
            p.name.startswith("/") for p in resource.properties
        )
        self.generator = generator

    def build(self) -> typing.Optional[ast.ClassDef]:
        base_class: typing.Union[ast.Attribute, ast.Name]

        # Create the base class
        if not self.resource.base or self.resource.base.name == "object":
            base_class = ast.Attribute(value=ast.Name(id="marshmallow"), attr="Schema")
        else:
            if self.resource.base.name in FIELD_TYPES:
                return None
            base_class = ast.Name(id=self.resource.base.name + "Schema")

            if self.resource.package_name != self.resource.base.package_name:
                self.generator.import_resource(
                    self.resource.package_name,
                    self.resource.base.package_name,
                    self.resource.base.name + "Schema",
                )

        # Define the base class
        class_node = ast.ClassDef(
            name=self.resource.name + "Schema",
            bases=[base_class],
            keywords=[],
            decorator_list=[],
            body=[],
        )

        doc_string = (
            f"Marshmallow schema for :class:`commercetools.types.{self.resource.name}`."
        )
        class_node.body.append(ast.Expr(value=ast.Str(s=doc_string, kind=None)))

        # Add the field definitions
        for prop in self.resource.properties:
            node = self._create_schema_property(prop)
            if node:
                class_node.body.append(node)

        # Add the Meta class
        class_node.body.append(
            ast.ClassDef(
                name="Meta",
                bases=[],
                keywords=[],
                body=[
                    ast.Assign(
                        targets=[ast.Name(id="unknown")],
                        value=ast.Name(id="marshmallow.EXCLUDE"),
                    )
                ],
                decorator_list=[],
            )
        )

        # Create the post_load() method
        post_load_node = self._create_marshmallow_hook("post_load")
        if self.contains_regex_field:
            post_load_node.body.append(self._create_regex_call("_regex", "postprocess"))
        post_load_node.body.append(
            ast.Return(
                value=ast.Call(
                    func=ast.Name(id=f"types.{self.resource.name}"),
                    args=[],
                    keywords=[ast.keyword(arg=None, value=ast.Name(id="data"))],
                )
            )
        )
        class_node.body.append(post_load_node)

        # Create the pre_load() method
        if self.contains_regex_field:
            node = self._create_marshmallow_hook("pre_load")
            node.body.append(self._create_regex_call("_regex", "preprocess"))
            node.body.append(ast.Return(value=ast.Name(id="data")))
            class_node.body.append(node)

            node = self._create_marshmallow_hook("pre_dump")
            node.body.append(self._create_regex_call("_regex", "preprocess"))
            node.body.append(ast.Return(value=ast.Name(id="data")))
            class_node.body.append(node)

            node = self._create_marshmallow_hook("post_dump")
            node.body.append(self._create_regex_call("_regex", "postprocess"))
            node.body.append(ast.Return(value=ast.Name(id="data")))
            class_node.body.append(node)

        d_field = self.resource.get_discriminator_field()
        if d_field:
            post_load_node.body.insert(
                0,
                ast.Delete(
                    targets=[
                        ast.Subscript(
                            value=ast.Name(id="data"),
                            slice=ast.Index(
                                value=ast.Str(s=d_field.attribute_name, kind=None)
                            ),
                        )
                    ]
                ),
            )
        return class_node

    def _create_schema_property(self, prop):
        node = self._get_property_field(prop)

        if prop.many:
            if node.func.id == "helpers.LazyNestedField":
                node.keywords.append(
                    ast.keyword(
                        arg="many", value=ast.NameConstant(value=True, kind=None)
                    )
                )
            else:
                node = ast.Call(
                    func=ast.Name(id="marshmallow.fields.List"),
                    args=[node],
                    keywords=[],
                )

        if prop.optional:
            node.keywords.append(
                ast.keyword(
                    arg="missing", value=ast.NameConstant(value=None, kind=None)
                )
            )

        if prop.attribute_name != prop.name and not prop.name.startswith("/"):
            node.keywords.append(
                ast.keyword(arg="data_key", value=ast.Str(s=prop.name, kind=None))
            )

        if prop.name.startswith("/"):
            assert len(self.properties) == 1
            self.generator.add_import_statement(self.resource.package_name, "re")
            self.generator.add_import_statement(
                self.resource.package_name, "commercetools", "helpers"
            )
            node = ast.Call(
                func=ast.Name(id="helpers.RegexField"),
                args=[],
                keywords=[
                    ast.keyword(
                        arg="unknown", value=ast.Name(id="marshmallow.EXCLUDE")
                    ),
                    ast.keyword(
                        arg="pattern",
                        value=ast.Call(
                            func=ast.Name(id="re.compile"),
                            args=[ast.Str(s=prop.name[1:-1], kind=None)],
                            keywords=[],
                        ),
                    ),
                    ast.keyword(arg="type", value=node),
                ],
            )

        node = ast.Assign(
            targets=[ast.Name(id=prop.attribute_name or "_regex")], value=node, simple=1
        )
        return node

    def _get_property_field(self, prop):
        if prop.type is None:
            return ast.Call(
                func=ast.Name(id=FIELD_TYPES["object"]),
                args=[],
                keywords=[
                    ast.keyword(
                        arg="allow_none", value=ast.NameConstant(True, kind=None)
                    )
                ],
            )
        elif prop.type.enum:
            self.generator.add_import_statement(
                self.resource.package_name, "marshmallow_enum"
            )
            return ast.Call(
                func=ast.Name(id="marshmallow_enum.EnumField"),
                args=[ast.Attribute(value=ast.Name(id="types"), attr=prop.type.name)],
                keywords=[
                    ast.keyword(arg="by_value", value=ast.NameConstant(True, kind=None))
                ],
            )

        elif prop.type.discriminator:
            return self._create_discriminator_field(prop.type)

        elif prop.type.name.startswith("/"):
            return ast.Call(
                func=ast.Name(id=prop.type.name + "Field"), args=[], keywords=[]
            )

        elif prop.type.name in FIELD_TYPES:
            node = ast.Call(
                func=ast.Name(id=FIELD_TYPES[prop.type.name]),
                args=[],
                keywords=[
                    ast.keyword(
                        arg="allow_none", value=ast.NameConstant(True, kind=None)
                    )
                ],
            )
            if prop.type.name == "array":
                assert prop.items, f"The array property {prop.name} has no items"
                assert prop.items_types

                # TODO: We for now assume that the items are all subclasses of
                # the first item. We shouldn't do that :-)
                if prop.items_types[0].discriminator:
                    node.args.append(
                        self._create_discriminator_field(prop.items_types[0])
                    )
                else:
                    node.args.append(self._create_nested_field(prop.items_types[0]))
            return node

        # Dict Field
        elif "asMap" in prop.type.annotations:
            if self.resource.package_name != prop.type.package_name:
                self.generator.import_resource(
                    self.resource.package_name,
                    prop.type.package_name,
                    prop.type.name + "Field",
                )
            return ast.Call(
                func=ast.Name(id=prop.type.name + "Field"),
                args=[],
                keywords=[
                    ast.keyword(
                        arg="allow_none", value=ast.NameConstant(True, kind=None)
                    )
                ],
            )

        elif prop.type.base and prop.type.base.name == "string":
            return ast.Call(
                func=ast.Name(id="marshmallow.fields.String"), args=[], keywords=[]
            )

        else:
            return self._create_nested_field(prop.type)

    def _create_discriminator_field(self, type_obj):
        items = {}
        for child in type_obj.get_all_children():
            items[
                child.discriminator_value
            ] = f"commercetools._schemas.{child.package_name}.{child.name}Schema"

        field = type_obj.get_discriminator_field()
        self.generator.add_import_statement(
            self.resource.package_name, "commercetools", "helpers"
        )

        return ast.Call(
            func=ast.Name(id="helpers.Discriminator"),
            args=[],
            keywords=[
                ast.keyword(
                    arg="discriminator_field",
                    value=ast.Tuple(
                        elts=[
                            ast.Str(s=field.name, kind=None),
                            ast.Str(s=field.attribute_name, kind=None),
                        ]
                    ),
                ),
                ast.keyword(
                    arg="discriminator_schemas",
                    value=ast.Dict(
                        keys=[ast.Str(s=v, kind=None) for v in items.keys()],
                        values=[ast.Str(s=v, kind=None) for v in items.values()],
                    ),
                ),
                ast.keyword(arg="unknown", value=ast.Name(id="marshmallow.EXCLUDE")),
                ast.keyword(arg="allow_none", value=ast.NameConstant(True, kind=None)),
            ],
        )

    def _create_nested_field(self, type_obj):
        """Create a `marshmallow.fields.Nested()` field.

        Generated code::

            marshmallow.fields.Nested(
                nested="commercetools._schemas.{package}.{object}Schema",
                unknown=marshmallow.EXCLUDE,
                allow_none=True
            )

        """
        self.generator.add_import_statement(
            self.resource.package_name, "commercetools", "helpers"
        )
        return ast.Call(
            func=ast.Name(id="helpers.LazyNestedField"),
            args=[],
            keywords=[
                ast.keyword(
                    arg="nested",
                    value=ast.Str(
                        s=f"commercetools._schemas.{type_obj.package_name}.{type_obj.name}Schema",
                        kind=None,
                    ),
                ),
                ast.keyword(arg="unknown", value=ast.Name(id="marshmallow.EXCLUDE")),
                ast.keyword(arg="allow_none", value=ast.NameConstant(True, kind=None)),
            ],
        )

    def _create_regex_call(self, field_name, method_name):
        """Generate `data = self.fields[{ field_name }].{ method_name }(data)`"""
        return ast.Assign(
            targets=[ast.Name(id="data")],
            value=ast.Call(
                func=ast.Attribute(
                    value=ast.Subscript(
                        value=ast.Attribute(value=ast.Name(id="self"), attr="fields"),
                        slice=ast.Index(value=ast.Str(s=field_name, kind=None)),
                    ),
                    attr=method_name,
                ),
                args=[ast.Name(id="data")],
                keywords=[],
            ),
        )

    def _create_marshmallow_hook(self, name):
        """Create a method on the Marshmallow schema which acts as a hook.

        Generated code:

            @marshmallow.post_load
            def { name }(self, data):
                <empty>

        """

        return ast.FunctionDef(
            name=name,
            args=ast.arguments(
                args=[
                    ast.arg(arg="self", annotation=None),
                    ast.arg(arg="data", annotation=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=ast.arg(arg="kwargs", annotation=None),
                defaults=[],
            ),
            body=[],
            decorator_list=[ast.Name(id=f"marshmallow.{name}")],
            returns=None,
        )
