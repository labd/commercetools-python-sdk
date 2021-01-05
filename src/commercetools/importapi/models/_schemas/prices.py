# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from .common import ImportResourceSchema

# Fields


# Marshmallow Schemas
class SubRateSchema(helpers.BaseSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    amount = marshmallow.fields.Float(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.SubRate(**data)


class TaxRateSchema(helpers.BaseSchema):
    id = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    name = marshmallow.fields.String(allow_none=True, missing=None)
    amount = marshmallow.fields.Float(allow_none=True, missing=None)
    included_in_price = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="includedInPrice"
    )
    country = marshmallow.fields.String(allow_none=True, missing=None)
    state = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    sub_rates = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".SubRateSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="subRates",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.TaxRate(**data)


class PriceImportSchema(ImportResourceSchema):
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
    country = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    valid_from = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="validFrom",
    )
    valid_until = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="validUntil",
    )
    customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.CustomerGroupKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="customerGroup",
    )
    channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.ChannelKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    discounted = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.DiscountedPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    publish = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    tiers = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.PriceTierSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customfields.CustomSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    product_variant = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.ProductVariantKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="productVariant",
    )
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

        return models.PriceImport(**data)
