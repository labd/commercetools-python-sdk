import keyword
import ast

from .abstract_gen import AbstractModuleGenerator
from .rammel import datatypes
from .utils import merge_imports, reorder_class_definitions, snakeit


class TypesModuleGenerator(AbstractModuleGenerator):
    _builtin_types = {
        "string": ast.Name(id="str"),
        "number": ast.Name(id="int"),
        "integer": ast.Name(id="int"),
        "boolean": ast.Name(id="bool"),
        "object": ast.Name(id="object"),
        "array": ast.Name(id="list"),
        "datetime": ast.Attribute(value=ast.Name(id="datetime"), attr="datetime"),
        "date-only": ast.Attribute(value=ast.Name(id="datetime"), attr="date"),
        "any": ast.Attribute(value=ast.Name(id="typing"), attr="Any"),
    }

    def __init__(self):
        self._import_nodes = []
        self._type_nodes = []
        super().__init__()

    def get_module_node(self):
        type_nodes = reorder_class_definitions(self._type_nodes)
        import_nodes = merge_imports(self._import_nodes)

        all_nodes = import_nodes + type_nodes
        value = ast.Module(body=all_nodes)
        return value

    def add_type_definition(self, resource):
        """Create a class definition"""

        if resource.name in self._builtin_types:
            return

        if resource.enum:
            return self.add_enum_definition(resource)

        if "asMap" in resource.annotations:
            return self.add_dict_definition(resource)
        return self.add_object_definition(resource)

    def add_dict_definition(self, resource):
        bases = [ast.Name(id="dict")]
        class_node = ast.ClassDef(
            name=resource.name, bases=bases, keywords=[], decorator_list=[], body=[]
        )
        if not class_node.body:
            class_node.body.append(ast.Pass())
        self._type_nodes.append(class_node)

    def add_enum_definition(self, resource):
        self.add_import_statement("enum")

        def enum_attr(val):
            val = val.replace("-", "_")
            val = snakeit(val).upper()
            if keyword.iskeyword(val):
                val += "_"
            return val

        bases = [ast.Name(id="enum.Enum")]
        class_node = ast.ClassDef(
            name=resource.name,
            bases=bases,
            keywords=[],
            decorator_list=[],
            body=[
                ast.Assign(targets=[ast.Name(id=enum_attr(val))], value=ast.Str(s=val))
                for val in resource.enum
            ],
        )
        if not class_node.body:
            class_node.body.append(ast.Pass())
        self._type_nodes.append(class_node)

    def add_object_definition(self, resource):
        """Create an attr.s class definition

            @attr.s(auto_attribs=True)
            class Attribute:
                name: str = None
                value: typing.Any = None

                def __init__(self, name: str = None, value: typing.Any = None):
                    super().__init__(name, value)

        """
        self.add_import_statement("attr")
        self.add_import_statement("typing")
        self.add_import_statement("datetime")

        # Define the base class
        bases = []
        if resource.is_scalar_type:
            bases.append(self._builtin_types[resource.base.name])
        elif resource.base and resource.base.name not in ("any", "object"):
            bases.append(ast.Name(id=resource.base.name))

        class_node = ast.ClassDef(
            name=resource.name,
            bases=bases,
            keywords=[],
            decorator_list=[
                ast.Call(
                    func=ast.Attribute(value=ast.Name(id="attr"), attr="s"),
                    args=[],
                    keywords=[
                        ast.keyword(
                            arg="auto_attribs", value=ast.NameConstant(value=True)
                        )
                    ],
                )
            ],
            body=[],
        )

        all_properties = resource.get_all_properties()

        # Do we have a discriminator field? In that case we add it as a 'hidden'
        # attr field again with a default value set to the discriminator value
        if resource.discriminator_value:
            discriminator_attr = resource.get_discriminator_field()

            all_properties.remove(discriminator_attr)

            assert discriminator_attr
            node = self._create_type_definition_property(
                resource, discriminator_attr, is_discriminator=True
            )
            if node:
                class_node.body.append(node)

        # Add the properties for the attr class
        for prop in resource.properties:
            node = self._create_type_definition_property(resource, prop)
            if node:
                class_node.body.append(node)

        init_args = [ast.arg(arg="self", annotation=None)]
        for prop in all_properties:
            attribute_name = prop.attribute_name

            if not attribute_name:
                continue

            init_args.append(
                ast.arg(
                    arg=attribute_name,
                    annotation=self._get_annotation_for_property(prop),
                )
            )

        # Generate an __init__ function. This isn't really needed for
        # attrs but it results in some nicer code completion for editors
        attribute_names = [prop.attribute_name for prop in all_properties]
        init_func = ast.FunctionDef(
            name="__init__",
            args=ast.arguments(
                args=init_args,
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    ast.NameConstant(value=None) for _ in range(0, len(attribute_names))
                ],
            ),
            body=[
                ast.Expr(
                    value=ast.Call(
                        func=ast.Attribute(
                            value=ast.Call(
                                func=ast.Name(id="super"), args=[], keywords=[]
                            ),
                            attr="__init__",
                        ),
                        args=[ast.Name(id=name) for name in attribute_names],
                        keywords=[],
                    )
                )
            ],
            decorator_list=[],
            returns=ast.NameConstant(value=None),
        )

        class_node.body.append(init_func)

        if not class_node.body:
            class_node.body.append(ast.Pass())

        self._type_nodes.append(class_node)

    def _create_type_definition_property(
        self,
        resource: datatypes.DataType,
        prop: datatypes.Property,
        is_discriminator: bool = False,
    ):
        attribute_name = prop.attribute_name
        if not attribute_name:
            print("Skipping:", prop)
            return None

        if not is_discriminator:
            value = ast.NameConstant(value=None)
        else:
            value = ast.Call(
                func=ast.Attribute(value=ast.Name(id="attr"), attr="ib"),
                args=[],
                keywords=[
                    ast.keyword(arg="repr", value=ast.NameConstant(value=False)),
                    ast.keyword(arg="init", value=ast.NameConstant(value=False)),
                    ast.keyword(
                        arg="default", value=ast.Str(s=resource.discriminator_value)
                    ),
                ],
            )

        annotation_type = self._get_annotation_for_property(prop)
        node = ast.AnnAssign(
            target=ast.Name(id=attribute_name),
            annotation=annotation_type,
            value=value,
            simple=1,
        )
        return node

    def _get_annotation_for_property(self, prop: datatypes.Property):
        """Create an node which represents an annotation for a property"""
        if prop.type is None:
            annotation_type = self._builtin_types["any"]
        elif prop.type.name in self._builtin_types:
            annotation_type = self._builtin_types[prop.type.name]
        else:
            annotation_type = ast.Str(s=prop.type.name)

        if prop.many:
            annotation_type = ast.Subscript(
                value=ast.Attribute(value=ast.Name(id="typing"), attr="List"),
                slice=ast.Index(value=annotation_type),
            )

        # Wrap it in a typing.Optional[T]
        annotation_type = ast.Subscript(
            value=ast.Attribute(value=ast.Name(id="typing"), attr="Optional"),
            slice=ast.Index(value=annotation_type),
        )

        return annotation_type
