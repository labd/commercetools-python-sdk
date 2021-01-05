# Generated file, please do not change!!!

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


class Attribute(_BaseType):
    """This type represents the value of an attribute of a product variant.
    The name and type property must match the name and type property of an attribute definition of the product type.

    """

    #: The name of this attribute must match a name of the product types attribute definitions.
    #: The name is required if this type is used in a product variant and must not be set when
    #: used in a product variant patch.
    name: typing.Optional["str"]
    type: "str"

    def __init__(self, *, name: typing.Optional["str"] = None, type: "str"):
        self.name = name
        self.type = type
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Attribute":
        from ._schemas.productvariants import AttributeSchema

        return AttributeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productvariants import AttributeSchema

        return AttributeSchema().dump(self)


class BooleanAttribute(Attribute):
    """This type represents an attribute which value is either "true" or "false"."""

    value: "bool"

    def __init__(self, *, name: typing.Optional["str"] = None, value: "bool"):
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
    """This type represents an attribute which value is set of boolean values."""

    value: typing.List["bool"]

    def __init__(
        self, *, name: typing.Optional["str"] = None, value: typing.List["bool"]
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
    """This type represents an attribute which value is a date."""

    value: "datetime.date"

    def __init__(self, *, name: typing.Optional["str"] = None, value: "datetime.date"):
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
    """This type represents an attribute which value is a set of dates."""

    value: typing.List["datetime.date"]

    def __init__(
        self,
        *,
        name: typing.Optional["str"] = None,
        value: typing.List["datetime.date"]
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
    """This type represents an attribute which value is a date with time."""

    value: "datetime.datetime"

    def __init__(
        self, *, name: typing.Optional["str"] = None, value: "datetime.datetime"
    ):
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
    """This type represents an attribute which value is a set of dates with time."""

    value: typing.List["datetime.datetime"]

    def __init__(
        self,
        *,
        name: typing.Optional["str"] = None,
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
    """This type represents an attribute which value is an enum.
    The attribute value refers to the key of the enum value.

    """

    value: "str"

    def __init__(self, *, name: typing.Optional["str"] = None, value: "str"):
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
    """This type represents an attribute which value is an enum.
    The attribute value refers to the key of the enum value.

    """

    value: typing.List["str"]

    def __init__(
        self, *, name: typing.Optional["str"] = None, value: typing.List["str"]
    ):
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
    """This type represents an attribute which value is a localized enum.
    The attribute value refers to the key of the enum value.

    """

    value: "str"

    def __init__(self, *, name: typing.Optional["str"] = None, value: "str"):
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
    """This type represents an attribute which value is a localized enum.
    The attribute value refers to the key of the enum value.

    """

    value: typing.List["str"]

    def __init__(
        self, *, name: typing.Optional["str"] = None, value: typing.List["str"]
    ):
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
    """This type represents an attribute which value is a localized text."""

    value: "LocalizedString"

    def __init__(
        self, *, name: typing.Optional["str"] = None, value: "LocalizedString"
    ):
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
    """This type represents an attribute which value is a localized text."""

    value: typing.List["LocalizedString"]

    def __init__(
        self,
        *,
        name: typing.Optional["str"] = None,
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
    """This type represents an attribute which value is a money object."""

    value: "TypedMoney"

    def __init__(self, *, name: typing.Optional["str"] = None, value: "TypedMoney"):
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
    """This type represents an attribute which value is a set of money objects."""

    value: typing.List["TypedMoney"]

    def __init__(
        self, *, name: typing.Optional["str"] = None, value: typing.List["TypedMoney"]
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
    """This type represents an attribute which value is a number."""

    value: "float"

    def __init__(self, *, name: typing.Optional["str"] = None, value: "float"):
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
    """This type represents an attribute which value is a set of numbers."""

    value: typing.List["float"]

    def __init__(
        self, *, name: typing.Optional["str"] = None, value: typing.List["float"]
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
    """This type represents an attribute which value is a key reference."""

    #: References a resource by its key.
    value: "KeyReference"

    def __init__(self, *, name: typing.Optional["str"] = None, value: "KeyReference"):
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
    """This type represents an attribute which value is a set of references."""

    value: typing.List["KeyReference"]

    def __init__(
        self, *, name: typing.Optional["str"] = None, value: typing.List["KeyReference"]
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
    """This type represents an attribute which value is a string."""

    value: "str"

    def __init__(self, *, name: typing.Optional["str"] = None, value: "str"):
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
    """This type represents an attribute which value is a set of strings."""

    value: typing.List["str"]

    def __init__(
        self, *, name: typing.Optional["str"] = None, value: typing.List["str"]
    ):
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
    """This type represents an attribute which value is a time."""

    value: "datetime.time"

    def __init__(self, *, name: typing.Optional["str"] = None, value: "datetime.time"):
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
    """This type represents an attribute which value is a set of times."""

    value: typing.List["datetime.time"]

    def __init__(
        self,
        *,
        name: typing.Optional["str"] = None,
        value: typing.List["datetime.time"]
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
    """Import representation for a product variant. Use this type for importing new product variants
    into a commercetools project.

    """

    #: Maps to `ProductVariant.sku`.
    sku: typing.Optional["str"]
    #: Maps to `ProductVariant.isMasterVariant`.
    is_master_variant: "bool"
    #: Maps to `ProductVariant.attributes`.
    #:
    #: Each attribute referenced must be defined
    #: in an already existing product type in the commercetools project, or the import
    #: operation state is set to `Unresolved`.
    attributes: typing.Optional[typing.List["Attribute"]]
    #: Maps to `ProductVariant.images`.
    images: typing.Optional[typing.List["Image"]]
    #: Maps to `ProductVariant.assets`.
    assets: typing.Optional[typing.List["Asset"]]
    #: If there were updates, only the updates will be published to `staged` and `current` projection.
    publish: typing.Optional["bool"]
    #: The product in which this product variant is contained. Maps to `ProductVariant.product`.
    #:
    #: The product referenced
    #: must already exist in the commercetools project, or the
    #: import operation state is set to `Unresolved`.
    product: "ProductKeyReference"

    def __init__(
        self,
        *,
        key: "str",
        sku: typing.Optional["str"] = None,
        is_master_variant: "bool",
        attributes: typing.Optional[typing.List["Attribute"]] = None,
        images: typing.Optional[typing.List["Image"]] = None,
        assets: typing.Optional[typing.List["Asset"]] = None,
        publish: typing.Optional["bool"] = None,
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
    """Import representation for an update to a product variant. Use this type for importing updates to existing
    product variants into a commercetools project.

    """

    #: The product variant to which this patch is applied.
    #:
    #: The product variant referenced
    #: must already exist in the commercetools project, or the
    #: import operation state is set to `Unresolved`.
    product_variant: "ProductVariantKeyReference"
    #: Maps to `ProductVariant.attributes`.
    #:
    #: Each attribute referenced must be defined
    #: in an already existing product type in the commercetools project, or the import
    #: operation state is set to `ValidationFailed`.
    attributes: typing.Optional["Attributes"]

    def __init__(
        self,
        *,
        product_variant: "ProductVariantKeyReference",
        attributes: typing.Optional["Attributes"] = None
    ):
        self.product_variant = product_variant
        self.attributes = attributes
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductVariantPatch":
        from ._schemas.productvariants import ProductVariantPatchSchema

        return ProductVariantPatchSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productvariants import ProductVariantPatchSchema

        return ProductVariantPatchSchema().dump(self)


class Attributes(typing.Dict[str, str]):
    pass
