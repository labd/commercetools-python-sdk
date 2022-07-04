# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import ImportResource

if typing.TYPE_CHECKING:
    from .common import (
        Asset,
        Image,
        KeyReference,
        LocalizedString,
        ProductKeyReference,
        ProductVariantKeyReference,
        TypedMoney,
    )

__all__ = [
    "Attribute",
    "Attributes",
    "BooleanAttribute",
    "BooleanSetAttribute",
    "DateAttribute",
    "DateSetAttribute",
    "DateTimeAttribute",
    "DateTimeSetAttribute",
    "EnumAttribute",
    "EnumSetAttribute",
    "LocalizableEnumAttribute",
    "LocalizableEnumSetAttribute",
    "LocalizableTextAttribute",
    "LocalizableTextSetAttribute",
    "MoneyAttribute",
    "MoneySetAttribute",
    "NumberAttribute",
    "NumberSetAttribute",
    "ProductVariantImport",
    "ProductVariantPatch",
    "ReferenceAttribute",
    "ReferenceSetAttribute",
    "TextAttribute",
    "TextSetAttribute",
    "TimeAttribute",
    "TimeSetAttribute",
]


class Attribute(_BaseType):
    """This type represents the value of an attribute of a product variant.
    The name and type property must match the name and type property of an attribute definition of the product type.

    """

    #: The name of this attribute must match a name of the product types attribute definitions.
    #: The name is required if this type is used in a product variant and must not be set when
    #: used in a product variant patch.
    name: typing.Optional[str]
    type: str

    def __init__(self, *, name: typing.Optional[str] = None, type: str):
        self.name = name
        self.type = type

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Attribute":
        if data["type"] == "boolean":
            from ._schemas.productvariants import BooleanAttributeSchema

            return BooleanAttributeSchema().load(data)
        if data["type"] == "boolean-set":
            from ._schemas.productvariants import BooleanSetAttributeSchema

            return BooleanSetAttributeSchema().load(data)
        if data["type"] == "date":
            from ._schemas.productvariants import DateAttributeSchema

            return DateAttributeSchema().load(data)
        if data["type"] == "date-set":
            from ._schemas.productvariants import DateSetAttributeSchema

            return DateSetAttributeSchema().load(data)
        if data["type"] == "datetime":
            from ._schemas.productvariants import DateTimeAttributeSchema

            return DateTimeAttributeSchema().load(data)
        if data["type"] == "datetime-set":
            from ._schemas.productvariants import DateTimeSetAttributeSchema

            return DateTimeSetAttributeSchema().load(data)
        if data["type"] == "enum":
            from ._schemas.productvariants import EnumAttributeSchema

            return EnumAttributeSchema().load(data)
        if data["type"] == "enum-set":
            from ._schemas.productvariants import EnumSetAttributeSchema

            return EnumSetAttributeSchema().load(data)
        if data["type"] == "lenum":
            from ._schemas.productvariants import LocalizableEnumAttributeSchema

            return LocalizableEnumAttributeSchema().load(data)
        if data["type"] == "lenum-set":
            from ._schemas.productvariants import LocalizableEnumSetAttributeSchema

            return LocalizableEnumSetAttributeSchema().load(data)
        if data["type"] == "ltext":
            from ._schemas.productvariants import LocalizableTextAttributeSchema

            return LocalizableTextAttributeSchema().load(data)
        if data["type"] == "ltext-set":
            from ._schemas.productvariants import LocalizableTextSetAttributeSchema

            return LocalizableTextSetAttributeSchema().load(data)
        if data["type"] == "money":
            from ._schemas.productvariants import MoneyAttributeSchema

            return MoneyAttributeSchema().load(data)
        if data["type"] == "money-set":
            from ._schemas.productvariants import MoneySetAttributeSchema

            return MoneySetAttributeSchema().load(data)
        if data["type"] == "number":
            from ._schemas.productvariants import NumberAttributeSchema

            return NumberAttributeSchema().load(data)
        if data["type"] == "number-set":
            from ._schemas.productvariants import NumberSetAttributeSchema

            return NumberSetAttributeSchema().load(data)
        if data["type"] == "reference":
            from ._schemas.productvariants import ReferenceAttributeSchema

            return ReferenceAttributeSchema().load(data)
        if data["type"] == "reference-set":
            from ._schemas.productvariants import ReferenceSetAttributeSchema

            return ReferenceSetAttributeSchema().load(data)
        if data["type"] == "text":
            from ._schemas.productvariants import TextAttributeSchema

            return TextAttributeSchema().load(data)
        if data["type"] == "text-set":
            from ._schemas.productvariants import TextSetAttributeSchema

            return TextSetAttributeSchema().load(data)
        if data["type"] == "time":
            from ._schemas.productvariants import TimeAttributeSchema

            return TimeAttributeSchema().load(data)
        if data["type"] == "time-set":
            from ._schemas.productvariants import TimeSetAttributeSchema

            return TimeSetAttributeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productvariants import AttributeSchema

        return AttributeSchema().dump(self)


class BooleanAttribute(Attribute):
    """This type represents an attribute whose value is either "true" or "false"."""

    value: bool

    def __init__(self, *, name: typing.Optional[str] = None, value: bool):
        self.value = value

        super().__init__(name=name, type="boolean")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "BooleanAttribute":
        from ._schemas.productvariants import BooleanAttributeSchema

        return BooleanAttributeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productvariants import BooleanAttributeSchema

        return BooleanAttributeSchema().dump(self)


class BooleanSetAttribute(Attribute):
    """This type represents an attribute whose value is set of boolean values."""

    value: typing.List["bool"]

    def __init__(
        self, *, name: typing.Optional[str] = None, value: typing.List["bool"]
    ):
        self.value = value

        super().__init__(name=name, type="boolean-set")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "BooleanSetAttribute":
        from ._schemas.productvariants import BooleanSetAttributeSchema

        return BooleanSetAttributeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productvariants import BooleanSetAttributeSchema

        return BooleanSetAttributeSchema().dump(self)


class DateAttribute(Attribute):
    """This type represents an attribute whose value is a date."""

    value: datetime.date

    def __init__(self, *, name: typing.Optional[str] = None, value: datetime.date):
        self.value = value

        super().__init__(name=name, type="date")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "DateAttribute":
        from ._schemas.productvariants import DateAttributeSchema

        return DateAttributeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productvariants import DateAttributeSchema

        return DateAttributeSchema().dump(self)


class DateSetAttribute(Attribute):
    """This type represents an attribute whose value is a set of dates."""

    value: typing.List["datetime.date"]

    def __init__(
        self, *, name: typing.Optional[str] = None, value: typing.List["datetime.date"]
    ):
        self.value = value

        super().__init__(name=name, type="date-set")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "DateSetAttribute":
        from ._schemas.productvariants import DateSetAttributeSchema

        return DateSetAttributeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productvariants import DateSetAttributeSchema

        return DateSetAttributeSchema().dump(self)


class DateTimeAttribute(Attribute):
    """This type represents an attribute whose value is a date with time."""

    value: datetime.datetime

    def __init__(self, *, name: typing.Optional[str] = None, value: datetime.datetime):
        self.value = value

        super().__init__(name=name, type="datetime")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "DateTimeAttribute":
        from ._schemas.productvariants import DateTimeAttributeSchema

        return DateTimeAttributeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productvariants import DateTimeAttributeSchema

        return DateTimeAttributeSchema().dump(self)


class DateTimeSetAttribute(Attribute):
    """This type represents an attribute whose value is a set of dates with time."""

    value: typing.List["datetime.datetime"]

    def __init__(
        self,
        *,
        name: typing.Optional[str] = None,
        value: typing.List["datetime.datetime"]
    ):
        self.value = value

        super().__init__(name=name, type="datetime-set")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "DateTimeSetAttribute":
        from ._schemas.productvariants import DateTimeSetAttributeSchema

        return DateTimeSetAttributeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productvariants import DateTimeSetAttributeSchema

        return DateTimeSetAttributeSchema().dump(self)


class EnumAttribute(Attribute):
    """This type represents an attribute whose value is an enum.
    The attribute value refers to the key of the enum value.

    """

    value: str

    def __init__(self, *, name: typing.Optional[str] = None, value: str):
        self.value = value

        super().__init__(name=name, type="enum")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "EnumAttribute":
        from ._schemas.productvariants import EnumAttributeSchema

        return EnumAttributeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productvariants import EnumAttributeSchema

        return EnumAttributeSchema().dump(self)


class EnumSetAttribute(Attribute):
    """This type represents an attribute whose value is an enum.
    The attribute value refers to the key of the enum value.

    """

    value: typing.List["str"]

    def __init__(self, *, name: typing.Optional[str] = None, value: typing.List["str"]):
        self.value = value

        super().__init__(name=name, type="enum-set")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "EnumSetAttribute":
        from ._schemas.productvariants import EnumSetAttributeSchema

        return EnumSetAttributeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productvariants import EnumSetAttributeSchema

        return EnumSetAttributeSchema().dump(self)


class LocalizableEnumAttribute(Attribute):
    """This type represents an attribute whose value is a localized enum.
    The attribute value refers to the key of the enum value.

    """

    value: str

    def __init__(self, *, name: typing.Optional[str] = None, value: str):
        self.value = value

        super().__init__(name=name, type="lenum")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "LocalizableEnumAttribute":
        from ._schemas.productvariants import LocalizableEnumAttributeSchema

        return LocalizableEnumAttributeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productvariants import LocalizableEnumAttributeSchema

        return LocalizableEnumAttributeSchema().dump(self)


class LocalizableEnumSetAttribute(Attribute):
    """This type represents an attribute whose value is a localized enum.
    The attribute value refers to the key of the enum value.

    """

    value: typing.List["str"]

    def __init__(self, *, name: typing.Optional[str] = None, value: typing.List["str"]):
        self.value = value

        super().__init__(name=name, type="lenum-set")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "LocalizableEnumSetAttribute":
        from ._schemas.productvariants import LocalizableEnumSetAttributeSchema

        return LocalizableEnumSetAttributeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productvariants import LocalizableEnumSetAttributeSchema

        return LocalizableEnumSetAttributeSchema().dump(self)


class LocalizableTextAttribute(Attribute):
    """This type represents an attribute whose value is a localized text."""

    #: A localized string is a JSON object where the keys are of [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag), and the values the corresponding strings used for that language.
    #: ```json
    #: {
    #:   "de": "Hundefutter",
    #:   "en": "dog food"
    #: }
    #: ```
    value: "LocalizedString"

    def __init__(self, *, name: typing.Optional[str] = None, value: "LocalizedString"):
        self.value = value

        super().__init__(name=name, type="ltext")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "LocalizableTextAttribute":
        from ._schemas.productvariants import LocalizableTextAttributeSchema

        return LocalizableTextAttributeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productvariants import LocalizableTextAttributeSchema

        return LocalizableTextAttributeSchema().dump(self)


class LocalizableTextSetAttribute(Attribute):
    """This type represents an attribute whose value is a localized text."""

    value: typing.List["LocalizedString"]

    def __init__(
        self,
        *,
        name: typing.Optional[str] = None,
        value: typing.List["LocalizedString"]
    ):
        self.value = value

        super().__init__(name=name, type="ltext-set")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "LocalizableTextSetAttribute":
        from ._schemas.productvariants import LocalizableTextSetAttributeSchema

        return LocalizableTextSetAttributeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productvariants import LocalizableTextSetAttributeSchema

        return LocalizableTextSetAttributeSchema().dump(self)


class MoneyAttribute(Attribute):
    """This type represents an attribute whose value is a money object."""

    value: "TypedMoney"

    def __init__(self, *, name: typing.Optional[str] = None, value: "TypedMoney"):
        self.value = value

        super().__init__(name=name, type="money")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MoneyAttribute":
        from ._schemas.productvariants import MoneyAttributeSchema

        return MoneyAttributeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productvariants import MoneyAttributeSchema

        return MoneyAttributeSchema().dump(self)


class MoneySetAttribute(Attribute):
    """This type represents an attribute whose value is a set of money objects."""

    value: typing.List["TypedMoney"]

    def __init__(
        self, *, name: typing.Optional[str] = None, value: typing.List["TypedMoney"]
    ):
        self.value = value

        super().__init__(name=name, type="money-set")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MoneySetAttribute":
        from ._schemas.productvariants import MoneySetAttributeSchema

        return MoneySetAttributeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productvariants import MoneySetAttributeSchema

        return MoneySetAttributeSchema().dump(self)


class NumberAttribute(Attribute):
    """This type represents an attribute whose value is a number."""

    value: float

    def __init__(self, *, name: typing.Optional[str] = None, value: float):
        self.value = value

        super().__init__(name=name, type="number")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "NumberAttribute":
        from ._schemas.productvariants import NumberAttributeSchema

        return NumberAttributeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productvariants import NumberAttributeSchema

        return NumberAttributeSchema().dump(self)


class NumberSetAttribute(Attribute):
    """This type represents an attribute whose value is a set of numbers."""

    value: typing.List["float"]

    def __init__(
        self, *, name: typing.Optional[str] = None, value: typing.List["float"]
    ):
        self.value = value

        super().__init__(name=name, type="number-set")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "NumberSetAttribute":
        from ._schemas.productvariants import NumberSetAttributeSchema

        return NumberSetAttributeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productvariants import NumberSetAttributeSchema

        return NumberSetAttributeSchema().dump(self)


class ReferenceAttribute(Attribute):
    """This type represents an attribute whose value is a key reference."""

    #: References a resource by key.
    value: "KeyReference"

    def __init__(self, *, name: typing.Optional[str] = None, value: "KeyReference"):
        self.value = value

        super().__init__(name=name, type="reference")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ReferenceAttribute":
        from ._schemas.productvariants import ReferenceAttributeSchema

        return ReferenceAttributeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productvariants import ReferenceAttributeSchema

        return ReferenceAttributeSchema().dump(self)


class ReferenceSetAttribute(Attribute):
    """This type represents an attribute whose value is a set of references."""

    value: typing.List["KeyReference"]

    def __init__(
        self, *, name: typing.Optional[str] = None, value: typing.List["KeyReference"]
    ):
        self.value = value

        super().__init__(name=name, type="reference-set")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ReferenceSetAttribute":
        from ._schemas.productvariants import ReferenceSetAttributeSchema

        return ReferenceSetAttributeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productvariants import ReferenceSetAttributeSchema

        return ReferenceSetAttributeSchema().dump(self)


class TextAttribute(Attribute):
    """This type represents an attribute whose value is a string."""

    value: str

    def __init__(self, *, name: typing.Optional[str] = None, value: str):
        self.value = value

        super().__init__(name=name, type="text")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TextAttribute":
        from ._schemas.productvariants import TextAttributeSchema

        return TextAttributeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productvariants import TextAttributeSchema

        return TextAttributeSchema().dump(self)


class TextSetAttribute(Attribute):
    """This type represents an attribute whose value is a set of strings."""

    value: typing.List["str"]

    def __init__(self, *, name: typing.Optional[str] = None, value: typing.List["str"]):
        self.value = value

        super().__init__(name=name, type="text-set")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TextSetAttribute":
        from ._schemas.productvariants import TextSetAttributeSchema

        return TextSetAttributeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productvariants import TextSetAttributeSchema

        return TextSetAttributeSchema().dump(self)


class TimeAttribute(Attribute):
    """This type represents an attribute whose value is a time."""

    value: datetime.time

    def __init__(self, *, name: typing.Optional[str] = None, value: datetime.time):
        self.value = value

        super().__init__(name=name, type="time")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TimeAttribute":
        from ._schemas.productvariants import TimeAttributeSchema

        return TimeAttributeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productvariants import TimeAttributeSchema

        return TimeAttributeSchema().dump(self)


class TimeSetAttribute(Attribute):
    """This type represents an attribute whose value is a set of times."""

    value: typing.List["datetime.time"]

    def __init__(
        self, *, name: typing.Optional[str] = None, value: typing.List["datetime.time"]
    ):
        self.value = value

        super().__init__(name=name, type="time-set")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TimeSetAttribute":
        from ._schemas.productvariants import TimeSetAttributeSchema

        return TimeSetAttributeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productvariants import TimeSetAttributeSchema

        return TimeSetAttributeSchema().dump(self)


class ProductVariantImport(ImportResource):
    """The data representation for a ProductVariant to be imported that is persisted as a [ProductVariant](/../api/projects/products#productvariant) in the Project."""

    #: Maps to `ProductVariant.sku`.
    sku: typing.Optional[str]
    #: Maps to `ProductVariant.isMasterVariant`.
    is_master_variant: bool
    #: Maps to `ProductVariant.attributes`.
    #: The referenced attribute must be defined in an already existing ProductType in the project, or the `state` of the [ImportOperation](/import-operation#importoperation) will be `unresolved`.
    attributes: typing.Optional[typing.List["Attribute"]]
    #: Maps to `ProductVariant.images`.
    images: typing.Optional[typing.List["Image"]]
    #: Maps to `ProductVariant.assets`.
    assets: typing.Optional[typing.List["Asset"]]
    #: If `publish` is set to either `true` or `false`, both staged and current projections are set to the same value provided by the import data.
    #: If `publish` is not set, the staged projection is set to the provided import data, but the current projection stays unchanged.
    #: However, if the import data contains no update, that is, if it matches the staged projection of the existing Product, the import induces no change in the existing Product whether `publish` is set or not.
    publish: typing.Optional[bool]
    #: The [Product](/../api/projects/products#productvariant) to which this Product Variant belongs. Maps to `ProductVariant.product`.
    #: The Reference to the [Product](/../api/projects/products#product) with which the ProductVariant is associated.
    #: If referenced Product does not exist, the `state` of the [ImportOperation](/import-operation#importoperation) will be set to `unresolved` until the necessary Product is created.
    product: "ProductKeyReference"

    def __init__(
        self,
        *,
        key: str,
        sku: typing.Optional[str] = None,
        is_master_variant: bool,
        attributes: typing.Optional[typing.List["Attribute"]] = None,
        images: typing.Optional[typing.List["Image"]] = None,
        assets: typing.Optional[typing.List["Asset"]] = None,
        publish: typing.Optional[bool] = None,
        product: "ProductKeyReference"
    ):
        self.sku = sku
        self.is_master_variant = is_master_variant
        self.attributes = attributes
        self.images = images
        self.assets = assets
        self.publish = publish
        self.product = product

        super().__init__(key=key)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductVariantImport":
        from ._schemas.productvariants import ProductVariantImportSchema

        return ProductVariantImportSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productvariants import ProductVariantImportSchema

        return ProductVariantImportSchema().dump(self)


class ProductVariantPatch(_BaseType):
    """Representation for an update of a [ProductVariant](/../api/projects/products#productvariant). Use this type to import updates for existing
    [ProductVariants](/../api/projects/products#productvariant) in a Project.

    """

    #: The [ProductVariant](/../api/projects/products#productvariant) to which this patch is applied.
    #: The Reference to the [ProductVariant](/../api/projects/products#productvariant) with which the ProductVariantPatch is associated.
    #: If referenced ProductVariant does not exist, the `state` of the [ImportOperation](/import-operation#importoperation) will be set to `unresolved` until the necessary ProductVariant is created.
    product_variant: "ProductVariantKeyReference"
    #: Maps to `ProductVariant.attributes`.
    #: The referenced attribute must be defined in an already existing [ProductType](/../api/projects/productTypes#producttype) in the Project, or the `state` of the [ImportOperation](/import-operation#importoperation) will be `unresolved`.
    attributes: typing.Optional["Attributes"]
    #: If `false`, the attribute changes are applied to both [current and staged projected representations](/../api/projects/productProjections#current--staged) of the [Product](/../api/projects/products#product).
    staged: typing.Optional[bool]

    def __init__(
        self,
        *,
        product_variant: "ProductVariantKeyReference",
        attributes: typing.Optional["Attributes"] = None,
        staged: typing.Optional[bool] = None
    ):
        self.product_variant = product_variant
        self.attributes = attributes
        self.staged = staged

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductVariantPatch":
        from ._schemas.productvariants import ProductVariantPatchSchema

        return ProductVariantPatchSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productvariants import ProductVariantPatchSchema

        return ProductVariantPatchSchema().dump(self)


class Attributes(typing.Dict[str, typing.Union["Attribute", None]]):
    pass
