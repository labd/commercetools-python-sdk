import ast

from .abstract_gen import AbstractModuleGenerator
from .utils import merge_imports, reorder_class_definitions


class SchemaModuleGenerator(AbstractModuleGenerator):
    """This generator is responsible for generating the schemas.py file"""

    _field_types = {
        "string": "marshmallow.fields.String",
        "object": "marshmallow.fields.Dict",
        "number": "marshmallow.fields.Integer",
        "integer": "marshmallow.fields.Integer",
        "boolean": "marshmallow.fields.Bool",
        "array": "marshmallow.fields.List",
        "datetime": "marshmallow.fields.DateTime",
        "date-only": "marshmallow.fields.Date",
        "any": "marshmallow.fields.Dict",
    }

    def __init__(self):
        self._import_nodes = []
        self._field_nodes = []
        self._type_nodes = []
        super().__init__()

    def get_module_node(self):
        type_nodes = reorder_class_definitions(self._type_nodes)
        import_nodes = merge_imports(self._import_nodes)

        all_nodes = import_nodes + self._field_nodes + type_nodes
        value = ast.Module(body=all_nodes)
        return value

    def add_type_definition(self, resource):
        """Create a class definition"""
        if resource.name in self._field_types:
            return
        if "asMap" in resource.annotations:
            return self.add_dict_field_definition(resource)
        return self.add_resource_definition(resource)

    def add_dict_field_definition(self, resource):
        self.add_import_statement("marshmallow")
        self.add_import_statement("commercetools", "types")

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
                    kwarg=None,
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

        self._field_nodes.append(class_node)

    def add_resource_definition(self, resource):
        self.add_import_statement("marshmallow")
        self.add_import_statement("marshmallow_enum")
        self.add_import_statement("commercetools", "helpers", "types")

        # Create the base class
        if not resource.base or resource.base.name == "object":
            base_class = ast.Attribute(value=ast.Name(id="marshmallow"), attr="Schema")
        else:
            if resource.base.name in self._field_types:
                return
            base_class = ast.Name(id=resource.base.name + "Schema")

        # Define the base class
        class_node = ast.ClassDef(
            name=resource.name + "Schema",
            bases=[base_class],
            keywords=[],
            decorator_list=[],
            body=[],
        )

        # Add the field definitions
        for prop in resource.properties:
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
        class_node.body.append(
            ast.FunctionDef(
                name="make",
                args=ast.arguments(
                    args=[
                        ast.arg(arg="self", annotation=None),
                        ast.arg(arg="data", annotation=None),
                    ],
                    vararg=None,
                    kwonlyargs=[],
                    kw_defaults=[],
                    kwarg=None,
                    defaults=[],
                ),
                body=[
                    ast.Return(
                        value=ast.Call(
                            func=ast.Name(id=f"types.{resource.name}"),
                            args=[],
                            keywords=[ast.keyword(arg=None, value=ast.Name(id="data"))],
                        )
                    )
                ],
                decorator_list=[ast.Name(id="marshmallow.post_load")],
                returns=None,
            )
        )

        d_field = resource.get_discriminator_field()
        if d_field:
            class_node.body[-1].body.insert(
                0,
                ast.Delete(
                    targets=[
                        ast.Subscript(
                            value=ast.Name(id="data"),
                            slice=ast.Index(value=ast.Str(s=d_field.attribute_name)),
                        )
                    ]
                ),
            )

        self._type_nodes.append(class_node)

    def _create_nested_field(self, type_obj):
        return ast.Call(
            func=ast.Name(id="marshmallow.fields.Nested"),
            args=[],
            keywords=[
                ast.keyword(
                    arg="nested",
                    value=ast.Str(s=f"commercetools.schemas.{type_obj.name}Schema"),
                ),
                ast.keyword(arg="unknown", value=ast.Name(id="marshmallow.EXCLUDE")),
            ],
        )

    def _create_discriminator_field(self, type_obj):
        items = {}
        for child in type_obj.get_all_children():
            items[
                child.discriminator_value
            ] = f"commercetools.schemas.{child.name}Schema"

        return ast.Call(
            func=ast.Name(id="helpers.Discriminator"),
            args=[],
            keywords=[
                ast.keyword(arg="discriminator_field", value=ast.Str(s="action")),
                ast.keyword(
                    arg="discriminator_schemas",
                    value=ast.Dict(
                        keys=[ast.Str(s=v) for v in items.keys()],
                        values=[ast.Str(s=v) for v in items.values()],
                    ),
                ),
            ],
        )

    def _create_schema_property(self, prop):
        if not prop.name.isidentifier():
            print("Skipping:", prop)
            return None

        args = []
        kwargs = []

        if prop.type is None:
            field_type_name = self._field_types["object"]

        elif prop.type.enum:
            field_type_name = "marshmallow_enum.EnumField"
            args.append(ast.Attribute(value=ast.Name(id="types"), attr=prop.type.name))
            kwargs.append(ast.keyword(arg="by_value", value=ast.NameConstant(True)))

        elif prop.type.discriminator:
            func = self._create_discriminator_field(prop.type)
            field_type_name = func.func.id
            kwargs = func.keywords

        elif prop.type.name in self._field_types:
            field_type_name = self._field_types[prop.type.name]
            if prop.type.name == "array":
                assert prop.items, f"The array property {prop.name} has no items"
                assert prop.items_type
                if prop.items_type.discriminator:
                    args.append(self._create_discriminator_field(prop.items_type))
                else:
                    args.append(self._create_nested_field(prop.items_type))

        # Dict Field
        elif "asMap" in prop.type.annotations:
            field_type_name = prop.type.name + "Field"

        elif prop.type.base and prop.type.base.name == "string":
            field_type_name = "marshmallow.fields.String"

        else:
            func = self._create_nested_field(prop.type)
            field_type_name = func.func.id
            kwargs = func.keywords

        if prop.optional:
            kwargs.append(
                ast.keyword(arg="missing", value=ast.NameConstant(value=None))
            )

        if prop.many:
            kwargs.append(ast.keyword(arg="many", value=ast.NameConstant(value=True)))

        field_type = ast.Name(id=field_type_name)
        if prop.attribute_name != prop.name:
            kwargs.append(ast.keyword(arg="data_key", value=ast.Str(s=prop.name)))

        node = ast.Assign(
            targets=[ast.Name(id=prop.attribute_name, ctx=ast.Store())],
            value=ast.Call(func=field_type, args=args, keywords=kwargs),
            simple=1,
        )
        return node
