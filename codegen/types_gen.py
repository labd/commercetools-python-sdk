import ast
import typing

from .abstract_gen import AbstractModuleGenerator
from .rammel import datatypes
from .utils import enum_attr, merge_imports, reorder_class_definitions

BUILTIN_TYPES = {
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


class TypesModuleGenerator(AbstractModuleGenerator):
    def __init__(self):
        self._import_nodes: typing.List[ast.AST] = []
        self._type_nodes: typing.List[ast.AST] = []
        super().__init__()

    def get_module_node(self):
        self.add_import_statement("attr")
        self.add_import_statement("enum")
        self.add_import_statement("typing")
        self.add_import_statement("datetime")

        type_nodes = reorder_class_definitions(self._type_nodes)
        import_nodes = merge_imports(self._import_nodes)

        all_nodes = import_nodes + type_nodes
        value = ast.Module(body=all_nodes)
        return value

    def add_type_definition(self, resource):
        node = self.create_object(resource)
        if node:
            self._type_nodes.append(node)

    def create_object(self, resource):
        """Create a class definition"""

        if resource.type == "string" and not resource.enum:
            assert not resource.properties
            return

        if resource.name in BUILTIN_TYPES:
            return

        if resource.enum:
            return self.create_enum(resource)

        if "asMap" in resource.annotations:
            return self.create_dict(resource)

        # We can assume for now that when there is a regex property that there
        # is at most one property. This might change in the future however, so
        # we should do something smart with this (combination of
        # dict/dataclass)?
        properties = resource.get_all_properties()
        if len(properties) == 1 and properties[0].name.startswith("/"):
            return self.create_dict(resource)

        return self.create_dataclass(resource)

    def create_dict(self, resource):
        """Create a subclass from dict

            class FieldContainer(typing.Dict[K, V]):
                pass

        """
        value_type = resource.properties[0].type
        if value_type.name in BUILTIN_TYPES:
            value_node = BUILTIN_TYPES[value_type.name]
        else:
            value_node = ast.Str(s=value_type.name)
        bases = [
            ast.Subscript(
                value=ast.Name(id="typing.Dict"),
                slice=ast.Index(value=ast.Tuple(elts=[ast.Name(id="str"), value_node])),
            )
        ]
        class_node = ast.ClassDef(
            name=resource.name, bases=bases, keywords=[], decorator_list=[], body=[]
        )

        node = ast.FunctionDef(
            name="__repr__",
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
            returns=ast.Name(id="str"),
        )

        # Cheating a bit here, but using ast nodes for this results in a lot of
        # code.
        repr_statement = ast.Return(
            value=ast.Name(
                id="'"
                + resource.name
                + "(%s)' % (', '.join(f'{k}={v!r}' for k, v in self.items()))"
            )
        )

        node.body.append(repr_statement)
        class_node.body.append(node)
        return class_node

    def create_enum(self, resource):
        """Create an Enum class.

            class ChannelRoleEnum(enum.Enum):
                INVENTORY_SUPPLY = 'InventorySupply'
                PRODUCT_DISTRIBUTION = 'ProductDistribution'
                ORDER_EXPORT = 'OrderExport'
                ORDER_IMPORT = 'OrderImport'
                PRIMARY = 'Primary'

        """
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
        return class_node

    def create_dataclass(self, resource):
        return ResourceClassGenerator(resource).build()


class ResourceClassGenerator:
    """Create an attr.s class definition

        @attr.s(auto_attribs=True, init=False, repr=False)
        class Attribute:
            name: str
            value: typing.Any

            def __init__(self, name: str = None, value: typing.Any = None):
                super().__init__(name, value)

    """

    resource: datatypes.DataType

    def __init__(self, resource: datatypes.DataType):
        self.resource = resource
        self.properties = self.resource.get_all_properties()
        self.attribute_names = [
            prop.attribute_name for prop in self.properties if prop.attribute_name
        ]

        # Do we have a discriminator field? In that case we add it as a 'hidden'
        # attr field again with a default value set to the discriminator value
        self.discriminator_attr = None
        if self.resource.discriminator_value:
            self.discriminator_attr = self.resource.get_discriminator_field()

    def build(self):
        # Define the base class. If the resource is a scalar type (str, int)
        # then we
        bases = []
        assert not self.resource.is_scalar_type
        if self.resource.base and self.resource.base.name not in ("any", "object"):
            bases.append(ast.Name(id=self.resource.base.name))

        # Create the class node
        class_node = ast.ClassDef(
            name=self.resource.name,
            bases=bases,
            keywords=[],
            decorator_list=[
                ast.Call(
                    func=ast.Attribute(value=ast.Name(id="attr"), attr="s"),
                    args=[],
                    keywords=[
                        ast.keyword(
                            arg="auto_attribs", value=ast.NameConstant(value=True)
                        ),
                        ast.keyword(arg="init", value=ast.NameConstant(value=False)),
                        ast.keyword(arg="repr", value=ast.NameConstant(value=False)),
                    ],
                )
            ],
            body=[],
        )

        # Add the properties for the attr class
        for prop in self.resource.properties:
            node = self._create_property(prop)
            if node:
                class_node.body.append(node)

        init_func = self._create_init_method(class_node)
        if not init_func.body:
            init_func.body.append(ast.Pass())
        class_node.body.append(init_func)

        repr_func = self._create_repr_method()
        class_node.body.append(repr_func)
        return class_node

    def _create_property(self, prop: datatypes.Property):
        attribute_name = prop.attribute_name
        if not attribute_name:
            print(
                f"[ERROR]: '{self.resource.name}.{prop.name}' - No valid attribute_name"
            )
            assert len(self.properties) == 1, self.properties
            return None

        annotation_type = self._get_annotation_for_property(prop)
        node = ast.AnnAssign(
            target=ast.Name(id=attribute_name),
            annotation=annotation_type,
            value=None,
            simple=1,
        )
        return node

    def _get_annotation_for_property(self, prop: datatypes.Property):
        """Create an node which represents an annotation for a property"""
        if prop.type is None:
            annotation_type = BUILTIN_TYPES["any"]
        elif prop.type.name in BUILTIN_TYPES:
            annotation_type = BUILTIN_TYPES[prop.type.name]
        elif prop.type.base and prop.type.base.name == "string" and not prop.type.enum:
            annotation_type = ast.Str(s="str")
        else:
            annotation_type = ast.Str(s=prop.type.name)

        # use typing.List[]. We make an hardcoded exception for
        # resources ending on PagedQueryResponse and mark that as Sequence. The
        # reason is to keep mypy happy when we pass subclasses of Resource to
        # PagedQueryResponse object
        if prop.many:
            attr = "List"
            if self.resource.name.endswith("PagedQueryResponse"):
                attr = "Sequence"
            annotation_type = ast.Subscript(
                value=ast.Attribute(value=ast.Name(id="typing"), attr=attr),
                slice=ast.Index(value=annotation_type),
            )

        # Wrap it in a typing.Optional[T]
        annotation_type = ast.Subscript(
            value=ast.Attribute(value=ast.Name(id="typing"), attr="Optional"),
            slice=ast.Index(value=annotation_type),
        )

        return annotation_type

    def _create_init_method(self, class_node) -> ast.FunctionDef:
        """Create the __init__ method

            def __init__(self, id: typing.Optional[int]=None) -> None:
                self.id = None

        """
        # Create the arguments for the __init__ method
        init_args = []
        for prop in self.properties:
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
        init_func = ast.FunctionDef(
            name="__init__",
            args=ast.arguments(
                args=[ast.arg(arg="self", annotation=None)],
                vararg=None,
                kwonlyargs=init_args,
                kw_defaults=[
                    ast.NameConstant(value=None) for _ in range(0, len(init_args))
                ],
                kwarg=None,
                defaults=[],
            ),
            body=[],
            decorator_list=[],
            returns=ast.NameConstant(value=None),
        )

        # Create assignments (self.x = x)
        for prop in self.resource.properties:
            attribute_name = prop.attribute_name
            if not attribute_name:
                continue
            init_func.body.append(
                ast.Assign(
                    targets=[
                        ast.Attribute(value=ast.Name(id="self"), attr=attribute_name)
                    ],
                    value=ast.Name(id=attribute_name),
                )
            )

        # Create the keyword arguments for the super() call. It should only
        # contain the arguments which are part of the superclass. Special
        # handling is done for discriminator values which are enums.
        init_values = []
        super_attributes = []
        if self.resource.base and self.resource.base.properties:
            super_attributes = [
                p.attribute_name for p in self.resource.base.get_all_properties()
            ]
        for name in self.attribute_names:
            if (
                self.discriminator_attr
                and name == self.discriminator_attr.attribute_name
            ):
                if self.discriminator_attr.type.enum:
                    init_values.append(
                        ast.keyword(
                            arg=name,
                            value=ast.Attribute(
                                value=ast.Name(
                                    id=f"{self.discriminator_attr.type.name}"
                                ),
                                attr=enum_attr(self.resource.discriminator_value),
                            ),
                        )
                    )
                else:
                    init_values.append(
                        ast.keyword(
                            arg=name, value=ast.Str(s=self.resource.discriminator_value)
                        )
                    )
            elif name in super_attributes:
                init_values.append(ast.keyword(arg=name, value=ast.Name(id=name)))

        # Add the super().__init__(args) call. This call is only required when
        # we have a superclass. Only the args
        if class_node.bases:
            init_func.body.append(
                ast.Expr(
                    value=ast.Call(
                        func=ast.Attribute(
                            value=ast.Call(
                                func=ast.Name(id="super"), args=[], keywords=[]
                            ),
                            attr="__init__",
                        ),
                        args=[],
                        keywords=init_values,
                    )
                )
            )
        return init_func

    def _create_repr_method(self):
        """Create the __repr__ method.

            def __repr__(self) -> str:
                return ('Attribute(name=%r, value=%r)' % (self.name, self.value))

        """
        node = ast.FunctionDef(
            name="__repr__",
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
            returns=ast.Name(id="str"),
        )
        node.body.append(
            ast.Return(
                value=ast.BinOp(
                    left=ast.Str(
                        s="%s(%s)"
                        % (
                            self.resource.name,
                            ", ".join(f"{attr}=%r" for attr in self.attribute_names),
                        )
                    ),
                    op=ast.Mod(),
                    right=ast.Tuple(
                        elts=[
                            ast.Name(id=f"self.{attr}") for attr in self.attribute_names
                        ]
                    ),
                )
            )
        )
        return node
