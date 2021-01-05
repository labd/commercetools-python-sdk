# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import ImportResource, ReferenceType

if typing.TYPE_CHECKING:
    from .common import LocalizedString, ProductTypeKeyReference, ReferenceType


class AttributeDefinition(_BaseType):
    type: "AttributeType"
    name: "str"
    label: "LocalizedString"
    is_required: "bool"
    attribute_constraint: typing.Optional["AttributeConstraintEnum"]
    input_tip: typing.Optional["LocalizedString"]
    input_hint: typing.Optional["TextInputHint"]
    is_searchable: typing.Optional["bool"]

    def __init__(
        self,
        *,
        type: "AttributeType",
        name: "str",
        label: "LocalizedString",
        is_required: "bool",
        attribute_constraint: typing.Optional["AttributeConstraintEnum"] = None,
        input_tip: typing.Optional["LocalizedString"] = None,
        input_hint: typing.Optional["TextInputHint"] = None,
        is_searchable: typing.Optional["bool"] = None
    ):
        self.type = type
        self.name = name
        self.label = label
        self.is_required = is_required
        self.attribute_constraint = attribute_constraint
        self.input_tip = input_tip
        self.input_hint = input_hint
        self.is_searchable = is_searchable
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AttributeDefinition":
        from ._schemas.producttypes import AttributeDefinitionSchema

        return AttributeDefinitionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.producttypes import AttributeDefinitionSchema

        return AttributeDefinitionSchema().dump(self)


class AttributeType(_BaseType):
    name: "str"

    def __init__(self, *, name: "str"):
        self.name = name
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AttributeType":
        from ._schemas.producttypes import AttributeTypeSchema

        return AttributeTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.producttypes import AttributeTypeSchema

        return AttributeTypeSchema().dump(self)


class AttributeBooleanType(AttributeType):
    def __init__(self):

        super().__init__(name="boolean")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AttributeBooleanType":
        from ._schemas.producttypes import AttributeBooleanTypeSchema

        return AttributeBooleanTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.producttypes import AttributeBooleanTypeSchema

        return AttributeBooleanTypeSchema().dump(self)


class AttributeDateTimeType(AttributeType):
    def __init__(self):

        super().__init__(name="datetime")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AttributeDateTimeType":
        from ._schemas.producttypes import AttributeDateTimeTypeSchema

        return AttributeDateTimeTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.producttypes import AttributeDateTimeTypeSchema

        return AttributeDateTimeTypeSchema().dump(self)


class AttributeDateType(AttributeType):
    def __init__(self):

        super().__init__(name="date")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AttributeDateType":
        from ._schemas.producttypes import AttributeDateTypeSchema

        return AttributeDateTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.producttypes import AttributeDateTypeSchema

        return AttributeDateTypeSchema().dump(self)


class AttributeEnumType(AttributeType):
    values: typing.List["AttributePlainEnumValue"]

    def __init__(self, *, values: typing.List["AttributePlainEnumValue"]):
        self.values = values
        super().__init__(name="enum")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AttributeEnumType":
        from ._schemas.producttypes import AttributeEnumTypeSchema

        return AttributeEnumTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.producttypes import AttributeEnumTypeSchema

        return AttributeEnumTypeSchema().dump(self)


class AttributePlainEnumValue(_BaseType):
    key: "str"
    label: "str"

    def __init__(self, *, key: "str", label: "str"):
        self.key = key
        self.label = label
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AttributePlainEnumValue":
        from ._schemas.producttypes import AttributePlainEnumValueSchema

        return AttributePlainEnumValueSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.producttypes import AttributePlainEnumValueSchema

        return AttributePlainEnumValueSchema().dump(self)


class AttributeLocalizableTextType(AttributeType):
    def __init__(self):

        super().__init__(name="ltext")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AttributeLocalizableTextType":
        from ._schemas.producttypes import AttributeLocalizableTextTypeSchema

        return AttributeLocalizableTextTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.producttypes import AttributeLocalizableTextTypeSchema

        return AttributeLocalizableTextTypeSchema().dump(self)


class AttributeLocalizedEnumType(AttributeType):
    values: typing.List["AttributeLocalizedEnumValue"]

    def __init__(self, *, values: typing.List["AttributeLocalizedEnumValue"]):
        self.values = values
        super().__init__(name="lenum")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AttributeLocalizedEnumType":
        from ._schemas.producttypes import AttributeLocalizedEnumTypeSchema

        return AttributeLocalizedEnumTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.producttypes import AttributeLocalizedEnumTypeSchema

        return AttributeLocalizedEnumTypeSchema().dump(self)


class AttributeLocalizedEnumValue(_BaseType):
    key: "str"
    label: "LocalizedString"

    def __init__(self, *, key: "str", label: "LocalizedString"):
        self.key = key
        self.label = label
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AttributeLocalizedEnumValue":
        from ._schemas.producttypes import AttributeLocalizedEnumValueSchema

        return AttributeLocalizedEnumValueSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.producttypes import AttributeLocalizedEnumValueSchema

        return AttributeLocalizedEnumValueSchema().dump(self)


class AttributeMoneyType(AttributeType):
    def __init__(self):

        super().__init__(name="money")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AttributeMoneyType":
        from ._schemas.producttypes import AttributeMoneyTypeSchema

        return AttributeMoneyTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.producttypes import AttributeMoneyTypeSchema

        return AttributeMoneyTypeSchema().dump(self)


class AttributeNestedType(AttributeType):
    #: References a product type by its key.
    type_reference: "ProductTypeKeyReference"

    def __init__(self, *, type_reference: "ProductTypeKeyReference"):
        self.type_reference = type_reference
        super().__init__(name="nested")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AttributeNestedType":
        from ._schemas.producttypes import AttributeNestedTypeSchema

        return AttributeNestedTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.producttypes import AttributeNestedTypeSchema

        return AttributeNestedTypeSchema().dump(self)


class AttributeNumberType(AttributeType):
    def __init__(self):

        super().__init__(name="number")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AttributeNumberType":
        from ._schemas.producttypes import AttributeNumberTypeSchema

        return AttributeNumberTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.producttypes import AttributeNumberTypeSchema

        return AttributeNumberTypeSchema().dump(self)


class AttributeReferenceType(AttributeType):
    #: The type of the referenced resource.
    reference_type_id: "ReferenceType"

    def __init__(self, *, reference_type_id: "ReferenceType"):
        self.reference_type_id = reference_type_id
        super().__init__(name="reference")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AttributeReferenceType":
        from ._schemas.producttypes import AttributeReferenceTypeSchema

        return AttributeReferenceTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.producttypes import AttributeReferenceTypeSchema

        return AttributeReferenceTypeSchema().dump(self)


class AttributeSetType(AttributeType):
    element_type: "AttributeType"

    def __init__(self, *, element_type: "AttributeType"):
        self.element_type = element_type
        super().__init__(name="set")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AttributeSetType":
        from ._schemas.producttypes import AttributeSetTypeSchema

        return AttributeSetTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.producttypes import AttributeSetTypeSchema

        return AttributeSetTypeSchema().dump(self)


class AttributeTextType(AttributeType):
    def __init__(self):

        super().__init__(name="text")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AttributeTextType":
        from ._schemas.producttypes import AttributeTextTypeSchema

        return AttributeTextTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.producttypes import AttributeTextTypeSchema

        return AttributeTextTypeSchema().dump(self)


class AttributeTimeType(AttributeType):
    def __init__(self):

        super().__init__(name="time")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AttributeTimeType":
        from ._schemas.producttypes import AttributeTimeTypeSchema

        return AttributeTimeTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.producttypes import AttributeTimeTypeSchema

        return AttributeTimeTypeSchema().dump(self)


class AttributeConstraintEnum(enum.Enum):
    NONE = "None"
    UNIQUE = "Unique"
    COMBINATION_UNIQUE = "CombinationUnique"
    SAME_FOR_ALL = "SameForAll"


class TextInputHint(enum.Enum):
    SINGLE_LINE = "SingleLine"
    MULTI_LINE = "MultiLine"


class ProductTypeImport(ImportResource):
    """Import representation for a product type."""

    #: Maps to `ProductType.name`.
    name: "str"
    #: Maps to `ProductType.description`.
    description: "str"
    #: The product type's attributes.
    attributes: typing.Optional[typing.List["AttributeDefinition"]]

    def __init__(
        self,
        *,
        key: "str",
        name: "str",
        description: "str",
        attributes: typing.Optional[typing.List["AttributeDefinition"]] = None
    ):
        self.name = name
        self.description = description
        self.attributes = attributes
        super().__init__(key=key)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductTypeImport":
        from ._schemas.producttypes import ProductTypeImportSchema

        return ProductTypeImportSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.producttypes import ProductTypeImportSchema

        return ProductTypeImportSchema().dump(self)
