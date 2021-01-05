# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from .common import LocalizedStringField


# Fields
class FieldContainerField(marshmallow.fields.Dict):
    def _deserialize(self, value, attr, data, **kwargs):
        result = super()._deserialize(value, attr, data)
        return models.FieldContainer(**result)


# Marshmallow Schemas
class CustomSchema(marshmallow.Schema):
    type = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.TypeKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    fields = FieldContainerField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Custom(**data)


class CustomFieldSchema(marshmallow.Schema):
    type = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CustomField(**data)


class BooleanFieldSchema(CustomFieldSchema):
    value = marshmallow.fields.Boolean(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.BooleanField(**data)


class StringFieldSchema(CustomFieldSchema):
    value = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.StringField(**data)


class LocalizedStringFieldSchema(CustomFieldSchema):
    value = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.LocalizedStringField(**data)


class EnumFieldSchema(CustomFieldSchema):
    value = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.EnumField(**data)


class LocalizedEnumFieldSchema(CustomFieldSchema):
    value = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.LocalizedEnumField(**data)


class NumberFieldSchema(CustomFieldSchema):
    value = marshmallow.fields.Float(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.NumberField(**data)


class MoneyFieldSchema(CustomFieldSchema):
    value = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "highPrecision": helpers.absmod(
                __name__, ".common.HighPrecisionMoneySchema"
            ),
            "centPrecision": helpers.absmod(__name__, ".common.MoneySchema"),
        },
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.MoneyField(**data)


class DateFieldSchema(CustomFieldSchema):
    value = marshmallow.fields.Date(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.DateField(**data)


class TimeFieldSchema(CustomFieldSchema):
    value = marshmallow.fields.Time(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.TimeField(**data)


class DateTimeFieldSchema(CustomFieldSchema):
    value = marshmallow.fields.DateTime(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.DateTimeField(**data)


class ReferenceFieldSchema(CustomFieldSchema):
    value = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("typeId", "type_id"),
        discriminator_schemas={
            "cart-discount": helpers.absmod(
                __name__, ".common.CartDiscountKeyReferenceSchema"
            ),
            "category": helpers.absmod(__name__, ".common.CategoryKeyReferenceSchema"),
            "channel": helpers.absmod(__name__, ".common.ChannelKeyReferenceSchema"),
            "customer": helpers.absmod(__name__, ".common.CustomerKeyReferenceSchema"),
            "customer-group": helpers.absmod(
                __name__, ".common.CustomerGroupKeyReferenceSchema"
            ),
            "price": helpers.absmod(__name__, ".common.PriceKeyReferenceSchema"),
            "product": helpers.absmod(__name__, ".common.ProductKeyReferenceSchema"),
            "product-discount": helpers.absmod(
                __name__, ".common.ProductDiscountKeyReferenceSchema"
            ),
            "product-type": helpers.absmod(
                __name__, ".common.ProductTypeKeyReferenceSchema"
            ),
            "product-variant": helpers.absmod(
                __name__, ".common.ProductVariantKeyReferenceSchema"
            ),
            "shipping-method": helpers.absmod(
                __name__, ".common.ShippingMethodKeyReferenceSchema"
            ),
            "state": helpers.absmod(__name__, ".common.StateKeyReferenceSchema"),
            "store": helpers.absmod(__name__, ".common.StoreKeyReferenceSchema"),
            "tax-category": helpers.absmod(
                __name__, ".common.TaxCategoryKeyReferenceSchema"
            ),
            "type": helpers.absmod(__name__, ".common.TypeKeyReferenceSchema"),
        },
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ReferenceField(**data)


class BooleanSetFieldSchema(CustomFieldSchema):
    value = marshmallow.fields.List(
        marshmallow.fields.Boolean(allow_none=True), allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.BooleanSetField(**data)


class StringSetFieldSchema(CustomFieldSchema):
    value = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.StringSetField(**data)


class LocalizedStringSetFieldSchema(CustomFieldSchema):
    value = helpers.LazyNestedField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.LocalizedStringSetField(**data)


class EnumSetFieldSchema(CustomFieldSchema):
    value = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.EnumSetField(**data)


class LocalizedEnumSetFieldSchema(CustomFieldSchema):
    value = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.LocalizedEnumSetField(**data)


class NumberSetFieldSchema(CustomFieldSchema):
    value = marshmallow.fields.List(
        marshmallow.fields.Float(allow_none=True), allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.NumberSetField(**data)


class MoneySetFieldSchema(CustomFieldSchema):
    value = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.MoneySetField(**data)


class DateSetFieldSchema(CustomFieldSchema):
    value = marshmallow.fields.List(
        marshmallow.fields.Date(allow_none=True), allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.DateSetField(**data)


class TimeSetFieldSchema(CustomFieldSchema):
    value = marshmallow.fields.List(
        marshmallow.fields.Time(allow_none=True), allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.TimeSetField(**data)


class DateTimeSetFieldSchema(CustomFieldSchema):
    value = marshmallow.fields.List(
        marshmallow.fields.DateTime(allow_none=True), allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.DateTimeSetField(**data)


class ReferenceSetFieldSchema(CustomFieldSchema):
    value = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("typeId", "type_id"),
            discriminator_schemas={
                "cart-discount": helpers.absmod(
                    __name__, ".common.CartDiscountKeyReferenceSchema"
                ),
                "category": helpers.absmod(
                    __name__, ".common.CategoryKeyReferenceSchema"
                ),
                "channel": helpers.absmod(
                    __name__, ".common.ChannelKeyReferenceSchema"
                ),
                "customer": helpers.absmod(
                    __name__, ".common.CustomerKeyReferenceSchema"
                ),
                "customer-group": helpers.absmod(
                    __name__, ".common.CustomerGroupKeyReferenceSchema"
                ),
                "price": helpers.absmod(__name__, ".common.PriceKeyReferenceSchema"),
                "product": helpers.absmod(
                    __name__, ".common.ProductKeyReferenceSchema"
                ),
                "product-discount": helpers.absmod(
                    __name__, ".common.ProductDiscountKeyReferenceSchema"
                ),
                "product-type": helpers.absmod(
                    __name__, ".common.ProductTypeKeyReferenceSchema"
                ),
                "product-variant": helpers.absmod(
                    __name__, ".common.ProductVariantKeyReferenceSchema"
                ),
                "shipping-method": helpers.absmod(
                    __name__, ".common.ShippingMethodKeyReferenceSchema"
                ),
                "state": helpers.absmod(__name__, ".common.StateKeyReferenceSchema"),
                "store": helpers.absmod(__name__, ".common.StoreKeyReferenceSchema"),
                "tax-category": helpers.absmod(
                    __name__, ".common.TaxCategoryKeyReferenceSchema"
                ),
                "type": helpers.absmod(__name__, ".common.TypeKeyReferenceSchema"),
            },
        ),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ReferenceSetField(**data)
