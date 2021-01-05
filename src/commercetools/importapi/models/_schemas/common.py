# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..common import MoneyType, ReferenceType


# Fields
class LocalizedStringField(marshmallow.fields.Dict):
    def _deserialize(self, value, attr, data, **kwargs):
        result = super()._deserialize(value, attr, data)
        return models.LocalizedString(**result)


# Marshmallow Schemas
class AssetSchema(marshmallow.Schema):
    key = marshmallow.fields.String(allow_none=True, missing=None)
    sources = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".AssetSourceSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    name = LocalizedStringField(allow_none=True, missing=None)
    description = LocalizedStringField(allow_none=True, missing=None)
    tags = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), allow_none=True, missing=None
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customfields.CustomSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Asset(**data)


class AssetDimensionsSchema(marshmallow.Schema):
    w = marshmallow.fields.Float(allow_none=True, missing=None)
    h = marshmallow.fields.Float(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.AssetDimensions(**data)


class AssetSourceSchema(marshmallow.Schema):
    uri = marshmallow.fields.String(allow_none=True, missing=None)
    key = marshmallow.fields.String(allow_none=True, missing=None)
    dimensions = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".AssetDimensionsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    content_type = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="contentType"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.AssetSource(**data)


class ImageSchema(marshmallow.Schema):
    url = marshmallow.fields.String(allow_none=True, missing=None)
    dimensions = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".AssetDimensionsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    label = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Image(**data)


class EnumValueSchema(marshmallow.Schema):
    key = marshmallow.fields.String(allow_none=True, missing=None)
    label = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.EnumValue(**data)


class LocalizedEnumValueSchema(marshmallow.Schema):
    key = marshmallow.fields.String(allow_none=True, missing=None)
    label = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.LocalizedEnumValue(**data)


class ImportResourceSchema(marshmallow.Schema):
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ImportResource(**data)


class KeyReferenceSchema(marshmallow.Schema):
    key = marshmallow.fields.String(allow_none=True, missing=None)
    type_id = marshmallow_enum.EnumField(
        ReferenceType, by_value=True, allow_none=True, missing=None, data_key="typeId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.KeyReference(**data)


class CartDiscountKeyReferenceSchema(KeyReferenceSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.CartDiscountKeyReference(**data)


class CategoryKeyReferenceSchema(KeyReferenceSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.CategoryKeyReference(**data)


class ChannelKeyReferenceSchema(KeyReferenceSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.ChannelKeyReference(**data)


class CustomerKeyReferenceSchema(KeyReferenceSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.CustomerKeyReference(**data)


class CustomerGroupKeyReferenceSchema(KeyReferenceSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.CustomerGroupKeyReference(**data)


class PriceKeyReferenceSchema(KeyReferenceSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.PriceKeyReference(**data)


class ProductKeyReferenceSchema(KeyReferenceSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.ProductKeyReference(**data)


class ProductDiscountKeyReferenceSchema(KeyReferenceSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.ProductDiscountKeyReference(**data)


class ProductTypeKeyReferenceSchema(KeyReferenceSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.ProductTypeKeyReference(**data)


class ProductVariantKeyReferenceSchema(KeyReferenceSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.ProductVariantKeyReference(**data)


class ShippingMethodKeyReferenceSchema(KeyReferenceSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.ShippingMethodKeyReference(**data)


class StateKeyReferenceSchema(KeyReferenceSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.StateKeyReference(**data)


class StoreKeyReferenceSchema(KeyReferenceSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.StoreKeyReference(**data)


class TaxCategoryKeyReferenceSchema(KeyReferenceSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.TaxCategoryKeyReference(**data)


class TypeKeyReferenceSchema(KeyReferenceSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.TypeKeyReference(**data)


class TypedMoneySchema(marshmallow.Schema):
    type = marshmallow_enum.EnumField(
        MoneyType, by_value=True, allow_none=True, missing=None
    )
    fraction_digits = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="fractionDigits"
    )
    cent_amount = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="centAmount"
    )
    currency_code = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="currencyCode"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.TypedMoney(**data)


class HighPrecisionMoneySchema(TypedMoneySchema):
    precise_amount = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="preciseAmount"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.HighPrecisionMoney(**data)


class MoneySchema(TypedMoneySchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.Money(**data)


class DiscountedPriceSchema(marshmallow.Schema):
    value = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "highPrecision": helpers.absmod(__name__, ".HighPrecisionMoneySchema"),
            "centPrecision": helpers.absmod(__name__, ".MoneySchema"),
        },
        missing=None,
    )
    discount = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductDiscountKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.DiscountedPrice(**data)


class PriceTierSchema(marshmallow.Schema):
    minimum_quantity = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="minimumQuantity"
    )
    value = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "highPrecision": helpers.absmod(__name__, ".HighPrecisionMoneySchema"),
            "centPrecision": helpers.absmod(__name__, ".MoneySchema"),
        },
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.PriceTier(**data)


class AddressSchema(marshmallow.Schema):
    id = marshmallow.fields.String(allow_none=True, missing=None)
    key = marshmallow.fields.String(allow_none=True, missing=None)
    title = marshmallow.fields.String(allow_none=True, missing=None)
    salutation = marshmallow.fields.String(allow_none=True, missing=None)
    first_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="firstName"
    )
    last_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lastName"
    )
    street_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="streetName"
    )
    street_number = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="streetNumber"
    )
    additional_street_info = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="additionalStreetInfo"
    )
    postal_code = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="postalCode"
    )
    city = marshmallow.fields.String(allow_none=True, missing=None)
    region = marshmallow.fields.String(allow_none=True, missing=None)
    state = marshmallow.fields.String(allow_none=True, missing=None)
    country = marshmallow.fields.String(allow_none=True, missing=None)
    company = marshmallow.fields.String(allow_none=True, missing=None)
    department = marshmallow.fields.String(allow_none=True, missing=None)
    building = marshmallow.fields.String(allow_none=True, missing=None)
    apartment = marshmallow.fields.String(allow_none=True, missing=None)
    p_o_box = marshmallow.fields.String(allow_none=True, missing=None, data_key="pOBox")
    phone = marshmallow.fields.String(allow_none=True, missing=None)
    mobile = marshmallow.fields.String(allow_none=True, missing=None)
    email = marshmallow.fields.String(allow_none=True, missing=None)
    fax = marshmallow.fields.String(allow_none=True, missing=None)
    additional_address_info = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="additionalAddressInfo"
    )
    external_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="externalId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Address(**data)
