# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from .common import ImportResourceSchema, LocalizedStringField

# Fields


# Marshmallow Schemas
class AttributeSchema(marshmallow.Schema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    type = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.Attribute(**data)


class BooleanAttributeSchema(AttributeSchema):
    value = marshmallow.fields.Boolean(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.BooleanAttribute(**data)


class BooleanSetAttributeSchema(AttributeSchema):
    value = marshmallow.fields.List(
        marshmallow.fields.Boolean(allow_none=True), allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.BooleanSetAttribute(**data)


class DateAttributeSchema(AttributeSchema):
    value = marshmallow.fields.Date(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.DateAttribute(**data)


class DateSetAttributeSchema(AttributeSchema):
    value = marshmallow.fields.List(
        marshmallow.fields.Date(allow_none=True), allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.DateSetAttribute(**data)


class DateTimeAttributeSchema(AttributeSchema):
    value = marshmallow.fields.DateTime(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.DateTimeAttribute(**data)


class DateTimeSetAttributeSchema(AttributeSchema):
    value = marshmallow.fields.List(
        marshmallow.fields.DateTime(allow_none=True), allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.DateTimeSetAttribute(**data)


class EnumAttributeSchema(AttributeSchema):
    value = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.EnumAttribute(**data)


class EnumSetAttributeSchema(AttributeSchema):
    value = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.EnumSetAttribute(**data)


class LocalizableEnumAttributeSchema(AttributeSchema):
    value = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.LocalizableEnumAttribute(**data)


class LocalizableEnumSetAttributeSchema(AttributeSchema):
    value = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.LocalizableEnumSetAttribute(**data)


class LocalizableTextAttributeSchema(AttributeSchema):
    value = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.LocalizableTextAttribute(**data)


class LocalizableTextSetAttributeSchema(AttributeSchema):
    value = helpers.LazyNestedField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.LocalizableTextSetAttribute(**data)


class MoneyAttributeSchema(AttributeSchema):
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
        return models.MoneyAttribute(**data)


class MoneySetAttributeSchema(AttributeSchema):
    value = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("type", "type"),
            discriminator_schemas={
                "highPrecision": helpers.absmod(
                    __name__, ".common.HighPrecisionMoneySchema"
                ),
                "centPrecision": helpers.absmod(__name__, ".common.MoneySchema"),
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
        return models.MoneySetAttribute(**data)


class NumberAttributeSchema(AttributeSchema):
    value = marshmallow.fields.Float(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.NumberAttribute(**data)


class NumberSetAttributeSchema(AttributeSchema):
    value = marshmallow.fields.List(
        marshmallow.fields.Float(allow_none=True), allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.NumberSetAttribute(**data)


class ReferenceAttributeSchema(AttributeSchema):
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
        return models.ReferenceAttribute(**data)


class ReferenceSetAttributeSchema(AttributeSchema):
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
        return models.ReferenceSetAttribute(**data)


class TextAttributeSchema(AttributeSchema):
    value = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.TextAttribute(**data)


class TextSetAttributeSchema(AttributeSchema):
    value = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.TextSetAttribute(**data)


class TimeAttributeSchema(AttributeSchema):
    value = marshmallow.fields.Time(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.TimeAttribute(**data)


class TimeSetAttributeSchema(AttributeSchema):
    value = marshmallow.fields.List(
        marshmallow.fields.Time(allow_none=True), allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.TimeSetAttribute(**data)


class ProductVariantImportSchema(ImportResourceSchema):
    sku = marshmallow.fields.String(allow_none=True, missing=None)
    is_master_variant = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="isMasterVariant"
    )
    attributes = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("type", "type"),
            discriminator_schemas={
                "boolean": helpers.absmod(__name__, ".BooleanAttributeSchema"),
                "boolean-set": helpers.absmod(__name__, ".BooleanSetAttributeSchema"),
                "date": helpers.absmod(__name__, ".DateAttributeSchema"),
                "date-set": helpers.absmod(__name__, ".DateSetAttributeSchema"),
                "datetime": helpers.absmod(__name__, ".DateTimeAttributeSchema"),
                "datetime-set": helpers.absmod(__name__, ".DateTimeSetAttributeSchema"),
                "enum": helpers.absmod(__name__, ".EnumAttributeSchema"),
                "enum-set": helpers.absmod(__name__, ".EnumSetAttributeSchema"),
                "lenum": helpers.absmod(__name__, ".LocalizableEnumAttributeSchema"),
                "lenum-set": helpers.absmod(
                    __name__, ".LocalizableEnumSetAttributeSchema"
                ),
                "ltext": helpers.absmod(__name__, ".LocalizableTextAttributeSchema"),
                "ltext-set": helpers.absmod(
                    __name__, ".LocalizableTextSetAttributeSchema"
                ),
                "money": helpers.absmod(__name__, ".MoneyAttributeSchema"),
                "money-set": helpers.absmod(__name__, ".MoneySetAttributeSchema"),
                "number": helpers.absmod(__name__, ".NumberAttributeSchema"),
                "number-set": helpers.absmod(__name__, ".NumberSetAttributeSchema"),
                "reference": helpers.absmod(__name__, ".ReferenceAttributeSchema"),
                "reference-set": helpers.absmod(
                    __name__, ".ReferenceSetAttributeSchema"
                ),
                "text": helpers.absmod(__name__, ".TextAttributeSchema"),
                "text-set": helpers.absmod(__name__, ".TextSetAttributeSchema"),
                "time": helpers.absmod(__name__, ".TimeAttributeSchema"),
                "time-set": helpers.absmod(__name__, ".TimeSetAttributeSchema"),
            },
        ),
        allow_none=True,
        missing=None,
    )
    images = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.ImageSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    assets = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AssetSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    publish = marshmallow.fields.Boolean(allow_none=True, missing=None)
    product = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.ProductKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductVariantImport(**data)


class ProductVariantPatchSchema(marshmallow.Schema):
    product_variant = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.ProductVariantKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="productVariant",
    )
    attributes = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".AttributesSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductVariantPatch(**data)


class AttributesSchema(marshmallow.Schema):
    _regex = helpers.RegexField(
        unknown=marshmallow.EXCLUDE,
        pattern=re.compile(""),
        type=helpers.LazyNestedField(
            nested=helpers.absmod(__name__, ".AttributeSchema"),
            unknown=marshmallow.EXCLUDE,
            allow_none=True,
            many=True,
        ),
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        data = typing.cast(helpers.RegexField, self.fields["_regex"]).postprocess(data)
        return models.Attributes(**data)

    @marshmallow.pre_load
    def pre_load(self, data, **kwargs):
        data = typing.cast(helpers.RegexField, self.fields["_regex"]).preprocess(data)
        return data

    @marshmallow.pre_dump
    def pre_dump(self, data, **kwargs):
        data = typing.cast(helpers.RegexField, self.fields["_regex"]).preprocess(data)
        return data

    @marshmallow.post_dump
    def post_dump(self, data, **kwargs):
        data = typing.cast(helpers.RegexField, self.fields["_regex"]).postprocess(data)
        return data
