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
class ProductDraftImportSchema(ImportResourceSchema):
    product_type = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.ProductTypeKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="productType",
    )
    name = LocalizedStringField(allow_none=True, missing=None)
    slug = LocalizedStringField(allow_none=True, missing=None)
    description = LocalizedStringField(allow_none=True, missing=None)
    categories = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.CategoryKeyReferenceSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    meta_title = LocalizedStringField(
        allow_none=True, missing=None, data_key="metaTitle"
    )
    meta_description = LocalizedStringField(
        allow_none=True, missing=None, data_key="metaDescription"
    )
    meta_keywords = LocalizedStringField(
        allow_none=True, missing=None, data_key="metaKeywords"
    )
    master_variant = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductVariantDraftImportSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="masterVariant",
    )
    variants = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductVariantDraftImportSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    tax_category = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.TaxCategoryKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="taxCategory",
    )
    search_keywords = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".products.SearchKeywordsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="searchKeywords",
    )
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.StateKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    publish = marshmallow.fields.Boolean(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductDraftImport(**data)


class ProductVariantDraftImportSchema(marshmallow.Schema):
    sku = marshmallow.fields.String(allow_none=True, missing=None)
    key = marshmallow.fields.String(allow_none=True, missing=None)
    prices = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".PriceDraftImportSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    attributes = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("type", "type"),
            discriminator_schemas={
                "boolean": helpers.absmod(
                    __name__, ".productvariants.BooleanAttributeSchema"
                ),
                "boolean-set": helpers.absmod(
                    __name__, ".productvariants.BooleanSetAttributeSchema"
                ),
                "date": helpers.absmod(
                    __name__, ".productvariants.DateAttributeSchema"
                ),
                "date-set": helpers.absmod(
                    __name__, ".productvariants.DateSetAttributeSchema"
                ),
                "datetime": helpers.absmod(
                    __name__, ".productvariants.DateTimeAttributeSchema"
                ),
                "datetime-set": helpers.absmod(
                    __name__, ".productvariants.DateTimeSetAttributeSchema"
                ),
                "enum": helpers.absmod(
                    __name__, ".productvariants.EnumAttributeSchema"
                ),
                "enum-set": helpers.absmod(
                    __name__, ".productvariants.EnumSetAttributeSchema"
                ),
                "lenum": helpers.absmod(
                    __name__, ".productvariants.LocalizableEnumAttributeSchema"
                ),
                "lenum-set": helpers.absmod(
                    __name__, ".productvariants.LocalizableEnumSetAttributeSchema"
                ),
                "ltext": helpers.absmod(
                    __name__, ".productvariants.LocalizableTextAttributeSchema"
                ),
                "ltext-set": helpers.absmod(
                    __name__, ".productvariants.LocalizableTextSetAttributeSchema"
                ),
                "money": helpers.absmod(
                    __name__, ".productvariants.MoneyAttributeSchema"
                ),
                "money-set": helpers.absmod(
                    __name__, ".productvariants.MoneySetAttributeSchema"
                ),
                "number": helpers.absmod(
                    __name__, ".productvariants.NumberAttributeSchema"
                ),
                "number-set": helpers.absmod(
                    __name__, ".productvariants.NumberSetAttributeSchema"
                ),
                "reference": helpers.absmod(
                    __name__, ".productvariants.ReferenceAttributeSchema"
                ),
                "reference-set": helpers.absmod(
                    __name__, ".productvariants.ReferenceSetAttributeSchema"
                ),
                "text": helpers.absmod(
                    __name__, ".productvariants.TextAttributeSchema"
                ),
                "text-set": helpers.absmod(
                    __name__, ".productvariants.TextSetAttributeSchema"
                ),
                "time": helpers.absmod(
                    __name__, ".productvariants.TimeAttributeSchema"
                ),
                "time-set": helpers.absmod(
                    __name__, ".productvariants.TimeSetAttributeSchema"
                ),
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

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductVariantDraftImport(**data)


class PriceDraftImportSchema(marshmallow.Schema):
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
    country = marshmallow.fields.String(allow_none=True, missing=None)
    customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.CustomerGroupKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="customerGroup",
    )
    channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.ChannelKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    valid_from = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validFrom"
    )
    valid_until = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validUntil"
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customfields.CustomSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    discounted = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.DiscountedPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    tiers = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.PriceTierSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.PriceDraftImport(**data)
