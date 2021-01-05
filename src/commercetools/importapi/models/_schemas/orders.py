# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..orders import (
    CartOrigin,
    InventoryMode,
    OrderState,
    PaymentState,
    RoundingMode,
    ShipmentState,
    ShippingMethodState,
    ShippingRateTierType,
    TaxCalculationMode,
)
from .common import ImportResourceSchema, LocalizedStringField

# Fields


# Marshmallow Schemas
class ItemStateSchema(marshmallow.Schema):
    quantity = marshmallow.fields.Float(allow_none=True, missing=None)
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.StateKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ItemState(**data)


class ItemShippingTargetSchema(marshmallow.Schema):
    address_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressKey"
    )
    quantity = marshmallow.fields.Float(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ItemShippingTarget(**data)


class ItemShippingDetailsDraftSchema(marshmallow.Schema):
    targets = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ItemShippingTargetSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ItemShippingDetailsDraft(**data)


class LineItemPriceSchema(marshmallow.Schema):
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
    valid_from = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validFrom"
    )
    valid_until = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validUntil"
    )
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

        return models.LineItemPrice(**data)


class LineItemProductVariantImportDraftSchema(marshmallow.Schema):
    product = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.ProductKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    sku = marshmallow.fields.String(allow_none=True, missing=None)
    prices = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".LineItemPriceSchema"),
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

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.LineItemProductVariantImportDraft(**data)


class LineItemImportDraftSchema(marshmallow.Schema):
    product = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.ProductKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    name = LocalizedStringField(allow_none=True, missing=None)
    variant = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".LineItemProductVariantImportDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".LineItemPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    quantity = marshmallow.fields.Float(allow_none=True, missing=None)
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ItemStateSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    supply_channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.ChannelKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="supplyChannel",
    )
    distribution_channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.ChannelKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="distributionChannel",
    )
    tax_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".prices.TaxRateSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="taxRate",
    )
    shipping_details = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ItemShippingDetailsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="shippingDetails",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.LineItemImportDraft(**data)


class ShippingRatePriceTierSchema(marshmallow.Schema):
    type = marshmallow_enum.EnumField(
        ShippingRateTierType, by_value=True, allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ShippingRatePriceTier(**data)


class CartClassificationTierSchema(ShippingRatePriceTierSchema):
    value = marshmallow.fields.String(allow_none=True, missing=None)
    price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    tiers = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("type", "type"),
            discriminator_schemas={
                "CartClassification": helpers.absmod(
                    __name__, ".CartClassificationTierSchema"
                )
            },
        ),
        allow_none=True,
        missing=None,
    )
    is_matching = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="isMatching"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CartClassificationTier(**data)


class ShippingRateDraftSchema(marshmallow.Schema):
    price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    free_above = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="freeAbove",
    )
    tiers = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("type", "type"),
            discriminator_schemas={
                "CartClassification": helpers.absmod(
                    __name__, ".CartClassificationTierSchema"
                )
            },
        ),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ShippingRateDraft(**data)


class ParcelMeasurementsSchema(marshmallow.Schema):
    height_in_millimeter = marshmallow.fields.Float(
        allow_none=True, missing=None, data_key="heightInMillimeter"
    )
    length_in_millimeter = marshmallow.fields.Float(
        allow_none=True, missing=None, data_key="lengthInMillimeter"
    )
    width_in_millimeter = marshmallow.fields.Float(
        allow_none=True, missing=None, data_key="widthInMillimeter"
    )
    weight_in_gram = marshmallow.fields.Float(
        allow_none=True, missing=None, data_key="weightInGram"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ParcelMeasurements(**data)


class TrackingDataSchema(marshmallow.Schema):
    tracking_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="trackingId"
    )
    carrier = marshmallow.fields.String(allow_none=True, missing=None)
    provider = marshmallow.fields.String(allow_none=True, missing=None)
    provider_transaction = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="providerTransaction"
    )
    is_return = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="isReturn"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.TrackingData(**data)


class DeliveryItemSchema(marshmallow.Schema):
    id = marshmallow.fields.String(allow_none=True, missing=None)
    quantity = marshmallow.fields.Float(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.DeliveryItem(**data)


class ParcelSchema(marshmallow.Schema):
    id = marshmallow.fields.String(allow_none=True, missing=None)
    created_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="createdAt"
    )
    measurements = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ParcelMeasurementsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    tracking_data = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".TrackingDataSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="trackingData",
    )
    items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".DeliveryItemSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Parcel(**data)


class DeliverySchema(marshmallow.Schema):
    id = marshmallow.fields.String(allow_none=True, missing=None)
    created_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="createdAt"
    )
    items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".DeliveryItemSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    parcels = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ParcelSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Delivery(**data)


class DiscountedLineItemPortionSchema(marshmallow.Schema):
    discount = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.CartDiscountKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    discounted_amount = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="discountedAmount",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.DiscountedLineItemPortion(**data)


class DiscountedLineItemPriceDraftSchema(marshmallow.Schema):
    value = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    included_discounts = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".DiscountedLineItemPortionSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="includedDiscounts",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.DiscountedLineItemPriceDraft(**data)


class ShippingInfoImportDraftSchema(marshmallow.Schema):
    shipping_method_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="shippingMethodName"
    )
    price = helpers.Discriminator(
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
    shipping_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ShippingRateDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="shippingRate",
    )
    tax_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".prices.TaxRateSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="taxRate",
    )
    tax_category = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.TaxCategoryKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="taxCategory",
    )
    shipping_method = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.ShippingMethodKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="shippingMethod",
    )
    deliveries = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".DeliverySchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    discounted_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".DiscountedLineItemPriceDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="discountedPrice",
    )
    shipping_method_state = marshmallow_enum.EnumField(
        ShippingMethodState,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="shippingMethodState",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ShippingInfoImportDraft(**data)


class ExternalTaxRateDraftSchema(marshmallow.Schema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    amount = marshmallow.fields.Float(allow_none=True, missing=None)
    country = marshmallow.fields.String(allow_none=True, missing=None)
    state = marshmallow.fields.String(allow_none=True, missing=None)
    sub_rates = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".prices.SubRateSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="subRates",
    )
    included_in_price = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="includedInPrice"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ExternalTaxRateDraft(**data)


class CustomLineItemTaxedPriceSchema(marshmallow.Schema):
    total_net = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "highPrecision": helpers.absmod(
                __name__, ".common.HighPrecisionMoneySchema"
            ),
            "centPrecision": helpers.absmod(__name__, ".common.MoneySchema"),
        },
        missing=None,
        data_key="totalNet",
    )
    total_gross = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "highPrecision": helpers.absmod(
                __name__, ".common.HighPrecisionMoneySchema"
            ),
            "centPrecision": helpers.absmod(__name__, ".common.MoneySchema"),
        },
        missing=None,
        data_key="totalGross",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CustomLineItemTaxedPrice(**data)


class CustomLineItemDraftSchema(marshmallow.Schema):
    name = LocalizedStringField(allow_none=True, missing=None)
    money = helpers.Discriminator(
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
    taxed_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".CustomLineItemTaxedPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="taxedPrice",
    )
    total_price = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "highPrecision": helpers.absmod(
                __name__, ".common.HighPrecisionMoneySchema"
            ),
            "centPrecision": helpers.absmod(__name__, ".common.MoneySchema"),
        },
        missing=None,
        data_key="totalPrice",
    )
    slug = marshmallow.fields.String(allow_none=True, missing=None)
    quantity = marshmallow.fields.Float(allow_none=True, missing=None)
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ItemStateSchema"),
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
    tax_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".prices.TaxRateSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="taxRate",
    )
    external_tax_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ExternalTaxRateDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="externalTaxRate",
    )
    discounted_price_per_quantity = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".DiscountedLineItemPriceDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="discountedPricePerQuantity",
    )
    shipping_details = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ItemShippingDetailsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="shippingDetails",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CustomLineItemDraft(**data)


class TaxPortionSchema(marshmallow.Schema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    rate = marshmallow.fields.Float(allow_none=True, missing=None)
    amount = helpers.Discriminator(
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

        return models.TaxPortion(**data)


class TaxedPriceSchema(marshmallow.Schema):
    total_net = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="totalNet",
    )
    total_gross = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="totalGross",
    )
    tax_portions = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".TaxPortionSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="taxPortions",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.TaxedPrice(**data)


class OrderImportSchema(ImportResourceSchema):
    order_number = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="orderNumber"
    )
    customer = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.CustomerKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    customer_email = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customerEmail"
    )
    line_items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".LineItemImportDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="lineItems",
    )
    custom_line_items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".CustomLineItemDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="customLineItems",
    )
    total_price = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "highPrecision": helpers.absmod(
                __name__, ".common.HighPrecisionMoneySchema"
            ),
            "centPrecision": helpers.absmod(__name__, ".common.MoneySchema"),
        },
        missing=None,
        data_key="totalPrice",
    )
    taxed_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".TaxedPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="taxedPrice",
    )
    shipping_address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="shippingAddress",
    )
    billing_address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="billingAddress",
    )
    customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.CustomerGroupKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="customerGroup",
    )
    country = marshmallow.fields.String(allow_none=True, missing=None)
    order_state = marshmallow_enum.EnumField(
        OrderState, by_value=True, allow_none=True, missing=None, data_key="orderState"
    )
    shipment_state = marshmallow_enum.EnumField(
        ShipmentState,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="shipmentState",
    )
    payment_state = marshmallow_enum.EnumField(
        PaymentState,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="paymentState",
    )
    shipping_info = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ShippingInfoImportDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="shippingInfo",
    )
    completed_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="completedAt"
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customfields.CustomSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    inventory_mode = marshmallow_enum.EnumField(
        InventoryMode,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="inventoryMode",
    )
    tax_rounding_mode = marshmallow_enum.EnumField(
        RoundingMode,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="taxRoundingMode",
    )
    tax_calculation_mode = marshmallow_enum.EnumField(
        TaxCalculationMode,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="taxCalculationMode",
    )
    origin = marshmallow_enum.EnumField(
        CartOrigin, by_value=True, allow_none=True, missing=None
    )
    item_shipping_addresses = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="itemShippingAddresses",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.OrderImport(**data)
