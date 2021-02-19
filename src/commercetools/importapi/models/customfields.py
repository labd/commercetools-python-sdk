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

if typing.TYPE_CHECKING:
    from .common import (
        KeyReference,
        LocalizedString,
        Money,
        TypedMoney,
        TypeKeyReference,
    )

__all__ = [
    "BooleanField",
    "BooleanSetField",
    "Custom",
    "CustomField",
    "DateField",
    "DateSetField",
    "DateTimeField",
    "DateTimeSetField",
    "EnumField",
    "EnumSetField",
    "FieldContainer",
    "LocalizedEnumField",
    "LocalizedEnumSetField",
    "LocalizedStringField",
    "LocalizedStringSetField",
    "MoneyField",
    "MoneySetField",
    "NumberField",
    "NumberSetField",
    "ReferenceField",
    "ReferenceSetField",
    "StringField",
    "StringSetField",
    "TimeField",
    "TimeSetField",
]


class Custom(_BaseType):
    """The representation to be sent to the server when creating a resource with custom fields."""

    #: The type that provides the field definitions for this object.
    type: "TypeKeyReference"
    #: The custom fields of this object.
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        type: "TypeKeyReference",
        fields: typing.Optional["FieldContainer"] = None
    ):
        self.type = type
        self.fields = fields
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Custom":
        from ._schemas.customfields import CustomSchema

        return CustomSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customfields import CustomSchema

        return CustomSchema().dump(self)


class FieldContainer(typing.Dict[str, "CustomField"]):
    pass


class CustomField(_BaseType):
    """Provides the value for a custom field of a specific type."""

    #: The type of this field.
    type: str

    def __init__(self, *, type: str):
        self.type = type
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomField":
        if data["type"] == "Boolean":
            from ._schemas.customfields import BooleanFieldSchema

            return BooleanFieldSchema().load(data)
        if data["type"] == "String":
            from ._schemas.customfields import StringFieldSchema

            return StringFieldSchema().load(data)
        if data["type"] == "LocalizedString":
            from ._schemas.customfields import LocalizedStringFieldSchema

            return LocalizedStringFieldSchema().load(data)
        if data["type"] == "Enum":
            from ._schemas.customfields import EnumFieldSchema

            return EnumFieldSchema().load(data)
        if data["type"] == "LocalizedEnum":
            from ._schemas.customfields import LocalizedEnumFieldSchema

            return LocalizedEnumFieldSchema().load(data)
        if data["type"] == "Number":
            from ._schemas.customfields import NumberFieldSchema

            return NumberFieldSchema().load(data)
        if data["type"] == "Money":
            from ._schemas.customfields import MoneyFieldSchema

            return MoneyFieldSchema().load(data)
        if data["type"] == "Date":
            from ._schemas.customfields import DateFieldSchema

            return DateFieldSchema().load(data)
        if data["type"] == "Time":
            from ._schemas.customfields import TimeFieldSchema

            return TimeFieldSchema().load(data)
        if data["type"] == "DateTime":
            from ._schemas.customfields import DateTimeFieldSchema

            return DateTimeFieldSchema().load(data)
        if data["type"] == "Reference":
            from ._schemas.customfields import ReferenceFieldSchema

            return ReferenceFieldSchema().load(data)
        if data["type"] == "BooleanSet":
            from ._schemas.customfields import BooleanSetFieldSchema

            return BooleanSetFieldSchema().load(data)
        if data["type"] == "StringSet":
            from ._schemas.customfields import StringSetFieldSchema

            return StringSetFieldSchema().load(data)
        if data["type"] == "LocalizedStringSet":
            from ._schemas.customfields import LocalizedStringSetFieldSchema

            return LocalizedStringSetFieldSchema().load(data)
        if data["type"] == "EnumSet":
            from ._schemas.customfields import EnumSetFieldSchema

            return EnumSetFieldSchema().load(data)
        if data["type"] == "LocalizedEnumSet":
            from ._schemas.customfields import LocalizedEnumSetFieldSchema

            return LocalizedEnumSetFieldSchema().load(data)
        if data["type"] == "NumberSet":
            from ._schemas.customfields import NumberSetFieldSchema

            return NumberSetFieldSchema().load(data)
        if data["type"] == "MoneySet":
            from ._schemas.customfields import MoneySetFieldSchema

            return MoneySetFieldSchema().load(data)
        if data["type"] == "DateSet":
            from ._schemas.customfields import DateSetFieldSchema

            return DateSetFieldSchema().load(data)
        if data["type"] == "TimeSet":
            from ._schemas.customfields import TimeSetFieldSchema

            return TimeSetFieldSchema().load(data)
        if data["type"] == "DateTimeSet":
            from ._schemas.customfields import DateTimeSetFieldSchema

            return DateTimeSetFieldSchema().load(data)
        if data["type"] == "ReferenceSet":
            from ._schemas.customfields import ReferenceSetFieldSchema

            return ReferenceSetFieldSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customfields import CustomFieldSchema

        return CustomFieldSchema().dump(self)


class BooleanField(CustomField):
    """A field with a boolean value."""

    value: bool

    def __init__(self, *, value: bool):
        self.value = value
        super().__init__(type="Boolean")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "BooleanField":
        from ._schemas.customfields import BooleanFieldSchema

        return BooleanFieldSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customfields import BooleanFieldSchema

        return BooleanFieldSchema().dump(self)


class StringField(CustomField):
    """A field with a string value."""

    value: str

    def __init__(self, *, value: str):
        self.value = value
        super().__init__(type="String")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StringField":
        from ._schemas.customfields import StringFieldSchema

        return StringFieldSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customfields import StringFieldSchema

        return StringFieldSchema().dump(self)


class LocalizedStringField(CustomField):
    """A field with a localized string value."""

    #: A localized string is a JSON object where the keys are of [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag), and the values the corresponding strings used for that language.
    #: ```json
    #: {
    #:   "de": "Hundefutter",
    #:   "en": "dog food"
    #: }
    #: ```
    value: "LocalizedString"

    def __init__(self, *, value: "LocalizedString"):
        self.value = value
        super().__init__(type="LocalizedString")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "LocalizedStringField":
        from ._schemas.customfields import LocalizedStringFieldSchema

        return LocalizedStringFieldSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customfields import LocalizedStringFieldSchema

        return LocalizedStringFieldSchema().dump(self)


class EnumField(CustomField):
    """A field with a enum value."""

    value: str

    def __init__(self, *, value: str):
        self.value = value
        super().__init__(type="Enum")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "EnumField":
        from ._schemas.customfields import EnumFieldSchema

        return EnumFieldSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customfields import EnumFieldSchema

        return EnumFieldSchema().dump(self)


class LocalizedEnumField(CustomField):
    """A field with a localized enum value."""

    value: str

    def __init__(self, *, value: str):
        self.value = value
        super().__init__(type="LocalizedEnum")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "LocalizedEnumField":
        from ._schemas.customfields import LocalizedEnumFieldSchema

        return LocalizedEnumFieldSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customfields import LocalizedEnumFieldSchema

        return LocalizedEnumFieldSchema().dump(self)


class NumberField(CustomField):
    """A field with a number value."""

    value: float

    def __init__(self, *, value: float):
        self.value = value
        super().__init__(type="Number")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "NumberField":
        from ._schemas.customfields import NumberFieldSchema

        return NumberFieldSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customfields import NumberFieldSchema

        return NumberFieldSchema().dump(self)


class MoneyField(CustomField):
    """A field with a money value."""

    value: "TypedMoney"

    def __init__(self, *, value: "TypedMoney"):
        self.value = value
        super().__init__(type="Money")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MoneyField":
        from ._schemas.customfields import MoneyFieldSchema

        return MoneyFieldSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customfields import MoneyFieldSchema

        return MoneyFieldSchema().dump(self)


class DateField(CustomField):
    """A field with a date value."""

    value: datetime.date

    def __init__(self, *, value: datetime.date):
        self.value = value
        super().__init__(type="Date")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "DateField":
        from ._schemas.customfields import DateFieldSchema

        return DateFieldSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customfields import DateFieldSchema

        return DateFieldSchema().dump(self)


class TimeField(CustomField):
    """A field with a time value."""

    value: datetime.time

    def __init__(self, *, value: datetime.time):
        self.value = value
        super().__init__(type="Time")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TimeField":
        from ._schemas.customfields import TimeFieldSchema

        return TimeFieldSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customfields import TimeFieldSchema

        return TimeFieldSchema().dump(self)


class DateTimeField(CustomField):
    """A field with a date time value."""

    value: datetime.datetime

    def __init__(self, *, value: datetime.datetime):
        self.value = value
        super().__init__(type="DateTime")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "DateTimeField":
        from ._schemas.customfields import DateTimeFieldSchema

        return DateTimeFieldSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customfields import DateTimeFieldSchema

        return DateTimeFieldSchema().dump(self)


class ReferenceField(CustomField):
    """A field with a reference value."""

    #: References a resource by its key.
    value: "KeyReference"

    def __init__(self, *, value: "KeyReference"):
        self.value = value
        super().__init__(type="Reference")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ReferenceField":
        from ._schemas.customfields import ReferenceFieldSchema

        return ReferenceFieldSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customfields import ReferenceFieldSchema

        return ReferenceFieldSchema().dump(self)


class BooleanSetField(CustomField):
    """A field with a boolean set value."""

    value: typing.List["bool"]

    def __init__(self, *, value: typing.List["bool"]):
        self.value = value
        super().__init__(type="BooleanSet")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "BooleanSetField":
        from ._schemas.customfields import BooleanSetFieldSchema

        return BooleanSetFieldSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customfields import BooleanSetFieldSchema

        return BooleanSetFieldSchema().dump(self)


class StringSetField(CustomField):
    """A field with a string set value."""

    value: typing.List["str"]

    def __init__(self, *, value: typing.List["str"]):
        self.value = value
        super().__init__(type="StringSet")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StringSetField":
        from ._schemas.customfields import StringSetFieldSchema

        return StringSetFieldSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customfields import StringSetFieldSchema

        return StringSetFieldSchema().dump(self)


class LocalizedStringSetField(CustomField):
    """A field with a localized string set value."""

    value: typing.List["LocalizedString"]

    def __init__(self, *, value: typing.List["LocalizedString"]):
        self.value = value
        super().__init__(type="LocalizedStringSet")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "LocalizedStringSetField":
        from ._schemas.customfields import LocalizedStringSetFieldSchema

        return LocalizedStringSetFieldSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customfields import LocalizedStringSetFieldSchema

        return LocalizedStringSetFieldSchema().dump(self)


class EnumSetField(CustomField):
    """A field with a enum set value."""

    value: typing.List["str"]

    def __init__(self, *, value: typing.List["str"]):
        self.value = value
        super().__init__(type="EnumSet")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "EnumSetField":
        from ._schemas.customfields import EnumSetFieldSchema

        return EnumSetFieldSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customfields import EnumSetFieldSchema

        return EnumSetFieldSchema().dump(self)


class LocalizedEnumSetField(CustomField):
    """A field with a localized enum set value."""

    value: typing.List["str"]

    def __init__(self, *, value: typing.List["str"]):
        self.value = value
        super().__init__(type="LocalizedEnumSet")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "LocalizedEnumSetField":
        from ._schemas.customfields import LocalizedEnumSetFieldSchema

        return LocalizedEnumSetFieldSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customfields import LocalizedEnumSetFieldSchema

        return LocalizedEnumSetFieldSchema().dump(self)


class NumberSetField(CustomField):
    """A field with a number value."""

    value: typing.List["float"]

    def __init__(self, *, value: typing.List["float"]):
        self.value = value
        super().__init__(type="NumberSet")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "NumberSetField":
        from ._schemas.customfields import NumberSetFieldSchema

        return NumberSetFieldSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customfields import NumberSetFieldSchema

        return NumberSetFieldSchema().dump(self)


class MoneySetField(CustomField):
    """A field with a money set value."""

    value: typing.List["Money"]

    def __init__(self, *, value: typing.List["Money"]):
        self.value = value
        super().__init__(type="MoneySet")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MoneySetField":
        from ._schemas.customfields import MoneySetFieldSchema

        return MoneySetFieldSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customfields import MoneySetFieldSchema

        return MoneySetFieldSchema().dump(self)


class DateSetField(CustomField):
    """A field with a date set value."""

    value: typing.List["datetime.date"]

    def __init__(self, *, value: typing.List["datetime.date"]):
        self.value = value
        super().__init__(type="DateSet")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "DateSetField":
        from ._schemas.customfields import DateSetFieldSchema

        return DateSetFieldSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customfields import DateSetFieldSchema

        return DateSetFieldSchema().dump(self)


class TimeSetField(CustomField):
    """A field with a time set value."""

    value: typing.List["datetime.time"]

    def __init__(self, *, value: typing.List["datetime.time"]):
        self.value = value
        super().__init__(type="TimeSet")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TimeSetField":
        from ._schemas.customfields import TimeSetFieldSchema

        return TimeSetFieldSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customfields import TimeSetFieldSchema

        return TimeSetFieldSchema().dump(self)


class DateTimeSetField(CustomField):
    """A field with a date time set value."""

    value: typing.List["datetime.datetime"]

    def __init__(self, *, value: typing.List["datetime.datetime"]):
        self.value = value
        super().__init__(type="DateTimeSet")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "DateTimeSetField":
        from ._schemas.customfields import DateTimeSetFieldSchema

        return DateTimeSetFieldSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customfields import DateTimeSetFieldSchema

        return DateTimeSetFieldSchema().dump(self)


class ReferenceSetField(CustomField):
    """A field with a reference set value."""

    value: typing.List["KeyReference"]

    def __init__(self, *, value: typing.List["KeyReference"]):
        self.value = value
        super().__init__(type="ReferenceSet")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ReferenceSetField":
        from ._schemas.customfields import ReferenceSetFieldSchema

        return ReferenceSetFieldSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customfields import ReferenceSetFieldSchema

        return ReferenceSetFieldSchema().dump(self)
