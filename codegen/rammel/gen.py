from typing import Any, Dict

from .datatypes import DataType, Property, UnresolvedType


def create_data_type(name: str, data: Dict[str, Any]):
    obj = DataType(name=name, type=data.get("type"))

    # Copy all annotations
    for key, value in data.items():
        if key.startswith("("):
            obj.annotations[key[1:-1]] = value

    # Copy enum properties
    obj.enum = data.get("enum", [])
    obj.discriminator = data.get("discriminator")
    obj.discriminator_value = data.get("discriminatorValue")

    # Iterate object properties
    properties = data.get("properties") or {}
    for key, value in properties.items():
        if isinstance(value, dict):
            property_type = value["type"]
            items = value.get("items")
            if items:
                items = [v.strip() for v in value.get("items").split("|")]
        else:
            property_type = value
            items = []

        optional = key.endswith("?")
        many = property_type.endswith("[]")
        if many:
            property_type = property_type[:-2]

        property_types = [v.strip() for v in property_type.split("|")]
        property_objects = [UnresolvedType(name=p) for p in property_types]
        prop = Property(
            name=key.rstrip("?"),
            optional=optional,
            types=property_objects,
            many=many,
            items=items,
        )
        obj.properties.append(prop)

    return obj


class TypeProcessor:

    builtin_types = [
        DataType(name="any", type=None),
        DataType(name="string", type="any"),
        DataType(name="array", type="any"),
        DataType(name="number", type="any"),
        DataType(name="boolean", type="any"),
        DataType(name="datetime", type="any"),
        DataType(name="integer", type="number"),
        DataType(name="object", type="any"),
        DataType(name="date-only", type="any"),
    ]

    def __init__(self):
        self.types: Dict[str, DataType] = {}
        for type_ in self.builtin_types:
            self.types[type_.name] = type_

    def load(self, data):
        for key, value in data.items():
            obj = create_data_type(key, value)
            self.types[obj.name] = obj
        self.resolve()

    def resolve_type(self, name: str):
        if name in self.types:
            return self.types[name]
        else:
            print("unresolved-type:", name)
            return self.types["any"]

    def get_type_by_name(self, name):
        if not name:
            return
        if " | " in name:
            return self.types["any"]
        return self.types[name]

    def resolve(self):
        for type_name, type_obj in self.types.items():
            type_obj.base = self.get_type_by_name(type_obj.type)
            if type_obj.base:
                type_obj.base.children.append(type_obj)

            # TODO: A property can have multiple types. For now we only us the
            # first one (see Property.type)
            for property in type_obj.properties:
                property.type = self.resolve_type(property.type.name)
                if property.type.name == "array":
                    if not property.items:
                        print(
                            f"[WARNING] {type_obj.name}.{property.name} is of type array but has no items defined"
                        )
                        property.items = ["any"]
                    property.items_types = [
                        self.resolve_type(item) for item in property.items
                    ]

    def dump(self):
        for type_name, type_obj in self.types.items():
            print("%s(%s)" % (type_name, type_obj.base))
            print(" - Annotations")
            for a_name, a_value in type_obj.annotations.items():
                print("   -", a_name)

            print(" - Properties")
            for prop in type_obj.properties:
                print("   -", prop.name)
