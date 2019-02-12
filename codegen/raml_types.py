from typing import Dict, List, Optional

import attr

from codegen.utils import snakeit


@attr.s(auto_attribs=True)
class DataType:
    name: str
    type: Optional[str]
    properties: List['Property'] = attr.Factory(lambda: [])
    annotations: Dict[str, object] = attr.Factory(lambda: {})
    enum: List[str] = attr.Factory(lambda: [])
    base: "DataType" = attr.ib(repr=False, default=None)
    discriminator: Optional[str] = None
    discriminator_value: Optional[str] = None
    children: List["DataType"] = attr.ib(repr=False, default=attr.Factory(lambda: []))

    @property
    def is_scalar_type(self):
        return self.type in [
            "string",
            "number",
            "float",
            "integer",
            "boolean",
            "date",
            "file",
            "any",
        ]

    def get_bases(self):
        bases = []
        cur = self
        while cur:
            bases.append(cur)
            cur = cur.base
        return bases

    def get_all_properties(self) -> List['Property']:
        """Return all the properties for this datatype including parent types.

        Note that we need to remove duplicate properties in case a sub resoruce
        overrides a property of the parent.

        """
        properties = {}  # assume ordered dict
        bases = reversed(self.get_bases())  # bottom to top
        for base in bases:
            for prop in base.properties:
                properties[prop.name] = prop
        return list(properties.values())

    def get_discriminator_field(self):
        field = None
        bases = self.get_bases()
        for base in bases:
            if base.discriminator:
                field = base.discriminator
                break
        if field:
            all_properties = self.get_all_properties()
            all_properties = {prop.name: prop for prop in all_properties}
            return all_properties[field]

    def get_all_children(self):
        children = list(self.children)
        for child in self.children:
            children.extend(child.get_all_children())
        return children


@attr.s(auto_attribs=True, slots=True)
class Property:
    name: str
    types: List[DataType]
    optional: bool = False
    many: bool = False
    items: List[str] = attr.Factory(lambda: [])
    items_types: Optional[List["DataType"]] = None

    @property
    def type(self):
        if self.types:
            return self.types[0]

    @type.setter
    def type(self, value):
        if self.types:
            self.types[0] = value
        else:
            self.types = [value]

    @property
    def attribute_name(self) -> Optional[str]:
        name = snakeit(self.name)
        if not name or not name.isidentifier():
            return None
        return name


@attr.s(auto_attribs=True)
class Package:
    name: str
    types: List[DataType] = attr.Factory(lambda: [])
    references: List[object] = attr.Factory(lambda: [])


@attr.s(auto_attribs=True)
class UnresolvedType:
    name: str
