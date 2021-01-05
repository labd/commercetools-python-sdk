# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..common import MoneyType, ReferenceTypeId


# Fields
class LocalizedStringField(marshmallow.fields.Dict):
    def _deserialize(self, value, attr, data, **kwargs):
        result = super()._deserialize(value, attr, data)
        return models.LocalizedString(**result)


# Marshmallow Schemas
class PagedQueryResponseSchema(marshmallow.Schema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".BaseResourceSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    meta = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.PagedQueryResponse(**data)


class UpdateSchema(marshmallow.Schema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".UpdateActionSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Update(**data)


class UpdateActionSchema(marshmallow.Schema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.UpdateAction(**data)


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


class AssetSchema(marshmallow.Schema):
    id = marshmallow.fields.String(allow_none=True, missing=None)
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
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Asset(**data)


class AssetDimensionsSchema(marshmallow.Schema):
    w = marshmallow.fields.Integer(allow_none=True, missing=None)
    h = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.AssetDimensions(**data)


class AssetDraftSchema(marshmallow.Schema):
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
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.AssetDraft(**data)


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


class BaseResourceSchema(marshmallow.Schema):
    id = marshmallow.fields.String(allow_none=True, missing=None)
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    created_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="createdAt"
    )
    last_modified_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="lastModifiedAt"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.BaseResource(**data)


class ClientLoggingSchema(marshmallow.Schema):
    client_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="clientId"
    )
    external_user_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="externalUserId"
    )
    customer = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer.CustomerReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    anonymous_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="anonymousId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ClientLogging(**data)


class CreatedBySchema(ClientLoggingSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CreatedBy(**data)


class DiscountedPriceSchema(marshmallow.Schema):
    value = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    discount = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".product_discount.ProductDiscountReferenceSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.DiscountedPrice(**data)


class GeoJsonSchema(marshmallow.Schema):
    type = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.GeoJson(**data)


class GeoJsonPointSchema(GeoJsonSchema):
    coordinates = marshmallow.fields.List(
        marshmallow.fields.Float(allow_none=True), allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.GeoJsonPoint(**data)


class ImageSchema(marshmallow.Schema):
    url = marshmallow.fields.String(allow_none=True, missing=None)
    dimensions = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ImageDimensionsSchema"),
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


class ImageDimensionsSchema(marshmallow.Schema):
    w = marshmallow.fields.Integer(allow_none=True, missing=None)
    h = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ImageDimensions(**data)


class KeyReferenceSchema(marshmallow.Schema):
    type_id = marshmallow_enum.EnumField(
        ReferenceTypeId, by_value=True, allow_none=True, missing=None, data_key="typeId"
    )
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.KeyReference(**data)


class LastModifiedBySchema(ClientLoggingSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.LastModifiedBy(**data)


class MoneySchema(marshmallow.Schema):
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

        return models.Money(**data)


class PriceSchema(marshmallow.Schema):
    id = marshmallow.fields.String(allow_none=True, missing=None)
    value = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "centPrecision": helpers.absmod(__name__, ".CentPrecisionMoneySchema"),
            "highPrecision": helpers.absmod(__name__, ".HighPrecisionMoneySchema"),
        },
        missing=None,
    )
    country = marshmallow.fields.String(allow_none=True, missing=None)
    customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer_group.CustomerGroupReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="customerGroup",
    )
    channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelReferenceSchema"),
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
    discounted = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".DiscountedPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    tiers = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".PriceTierSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Price(**data)


class PriceDraftSchema(marshmallow.Schema):
    value = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    country = marshmallow.fields.String(allow_none=True, missing=None)
    customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".customer_group.CustomerGroupResourceIdentifierSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="customerGroup",
    )
    channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelResourceIdentifierSchema"),
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
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    tiers = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".PriceTierDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    discounted = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".DiscountedPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.PriceDraft(**data)


class PriceTierSchema(marshmallow.Schema):
    minimum_quantity = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="minimumQuantity"
    )
    value = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "centPrecision": helpers.absmod(__name__, ".CentPrecisionMoneySchema"),
            "highPrecision": helpers.absmod(__name__, ".HighPrecisionMoneySchema"),
        },
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.PriceTier(**data)


class PriceTierDraftSchema(marshmallow.Schema):
    minimum_quantity = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="minimumQuantity"
    )
    value = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.PriceTierDraft(**data)


class QueryPriceSchema(marshmallow.Schema):
    id = marshmallow.fields.String(allow_none=True, missing=None)
    value = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    country = marshmallow.fields.String(allow_none=True, missing=None)
    customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer_group.CustomerGroupReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="customerGroup",
    )
    channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelReferenceSchema"),
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
    discounted = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".DiscountedPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    tiers = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".PriceTierDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.QueryPrice(**data)


class ReferenceSchema(marshmallow.Schema):
    type_id = marshmallow_enum.EnumField(
        ReferenceTypeId, by_value=True, allow_none=True, missing=None, data_key="typeId"
    )
    id = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.Reference(**data)


class ResourceIdentifierSchema(marshmallow.Schema):
    type_id = marshmallow_enum.EnumField(
        ReferenceTypeId, by_value=True, allow_none=True, missing=None, data_key="typeId"
    )
    id = marshmallow.fields.String(allow_none=True, missing=None)
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.ResourceIdentifier(**data)


class ScopedPriceSchema(marshmallow.Schema):
    id = marshmallow.fields.String(allow_none=True, missing=None)
    value = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "centPrecision": helpers.absmod(__name__, ".CentPrecisionMoneySchema"),
            "highPrecision": helpers.absmod(__name__, ".HighPrecisionMoneySchema"),
        },
        missing=None,
    )
    current_value = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "centPrecision": helpers.absmod(__name__, ".CentPrecisionMoneySchema"),
            "highPrecision": helpers.absmod(__name__, ".HighPrecisionMoneySchema"),
        },
        missing=None,
        data_key="currentValue",
    )
    country = marshmallow.fields.String(allow_none=True, missing=None)
    customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer_group.CustomerGroupReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="customerGroup",
    )
    channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelReferenceSchema"),
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
    discounted = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".DiscountedPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ScopedPrice(**data)


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


class CentPrecisionMoneySchema(TypedMoneySchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CentPrecisionMoney(**data)


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


class TypedMoneyDraftSchema(MoneySchema):
    type = marshmallow_enum.EnumField(
        MoneyType, by_value=True, allow_none=True, missing=None
    )
    fraction_digits = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="fractionDigits"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.TypedMoneyDraft(**data)


class CentPrecisionMoneyDraftSchema(TypedMoneyDraftSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CentPrecisionMoneyDraft(**data)


class HighPrecisionMoneyDraftSchema(TypedMoneyDraftSchema):
    precise_amount = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="preciseAmount"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.HighPrecisionMoneyDraft(**data)
