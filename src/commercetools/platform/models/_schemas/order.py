# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..cart import (
    CartOrigin,
    InventoryMode,
    RoundingMode,
    ShippingMethodState,
    TaxCalculationMode,
    TaxMode,
)
from ..common import ReferenceTypeId
from ..order import (
    OrderState,
    PaymentState,
    ReturnPaymentState,
    ReturnShipmentState,
    ShipmentState,
)
from .common import (
    BaseResourceSchema,
    LocalizedStringField,
    ReferenceSchema,
    ResourceIdentifierSchema,
)
from .type import FieldContainerField

# Fields


# Marshmallow Schemas
class StagedOrderUpdateActionSchema(marshmallow.Schema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderUpdateAction(**data)


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


class DeliveryItemSchema(marshmallow.Schema):
    id = marshmallow.fields.String(allow_none=True, missing=None)
    quantity = marshmallow.fields.Float(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.DeliveryItem(**data)


class DiscountedLineItemPriceDraftSchema(marshmallow.Schema):
    value = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    included_discounts = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.DiscountedLineItemPortionSchema"),
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


class ItemStateSchema(marshmallow.Schema):
    quantity = marshmallow.fields.Float(allow_none=True, missing=None)
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ItemState(**data)


class LineItemImportDraftSchema(marshmallow.Schema):
    product_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="productId"
    )
    name = LocalizedStringField(allow_none=True, missing=None)
    variant = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductVariantImportDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.PriceDraftSchema"),
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
        nested=helpers.absmod(__name__, ".channel.ChannelResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="supplyChannel",
    )
    distribution_channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="distributionChannel",
    )
    tax_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".tax_category.TaxRateSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="taxRate",
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    shipping_details = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ItemShippingDetailsDraftSchema"),
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


class OrderSchema(BaseResourceSchema):
    last_modified_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.LastModifiedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="lastModifiedBy",
    )
    created_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.CreatedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="createdBy",
    )
    completed_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="completedAt"
    )
    order_number = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="orderNumber"
    )
    customer_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customerId"
    )
    customer_email = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customerEmail"
    )
    anonymous_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="anonymousId"
    )
    store = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".store.StoreKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    line_items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.LineItemSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="lineItems",
    )
    custom_line_items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.CustomLineItemSchema"),
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
            "centPrecision": helpers.absmod(
                __name__, ".common.CentPrecisionMoneySchema"
            ),
            "highPrecision": helpers.absmod(
                __name__, ".common.HighPrecisionMoneySchema"
            ),
        },
        missing=None,
        data_key="totalPrice",
    )
    taxed_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.TaxedPriceSchema"),
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
    tax_mode = marshmallow_enum.EnumField(
        TaxMode, by_value=True, allow_none=True, missing=None, data_key="taxMode"
    )
    tax_rounding_mode = marshmallow_enum.EnumField(
        RoundingMode,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="taxRoundingMode",
    )
    customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer_group.CustomerGroupReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="customerGroup",
    )
    country = marshmallow.fields.String(allow_none=True, missing=None)
    order_state = marshmallow_enum.EnumField(
        OrderState, by_value=True, allow_none=True, missing=None, data_key="orderState"
    )
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
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
        nested=helpers.absmod(__name__, ".cart.ShippingInfoSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="shippingInfo",
    )
    sync_info = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".SyncInfoSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="syncInfo",
    )
    return_info = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ReturnInfoSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="returnInfo",
    )
    discount_codes = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.DiscountCodeInfoSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="discountCodes",
    )
    last_message_sequence_number = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="lastMessageSequenceNumber"
    )
    cart = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.CartReferenceSchema"),
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
    payment_info = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".PaymentInfoSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="paymentInfo",
    )
    locale = marshmallow.fields.String(allow_none=True, missing=None)
    inventory_mode = marshmallow_enum.EnumField(
        InventoryMode,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="inventoryMode",
    )
    origin = marshmallow_enum.EnumField(
        CartOrigin, by_value=True, allow_none=True, missing=None
    )
    tax_calculation_mode = marshmallow_enum.EnumField(
        TaxCalculationMode,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="taxCalculationMode",
    )
    shipping_rate_input = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "Classification": helpers.absmod(
                __name__, ".cart.ClassificationShippingRateInputSchema"
            ),
            "Score": helpers.absmod(__name__, ".cart.ScoreShippingRateInputSchema"),
        },
        missing=None,
        data_key="shippingRateInput",
    )
    item_shipping_addresses = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="itemShippingAddresses",
    )
    refused_gifts = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart_discount.CartDiscountReferenceSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="refusedGifts",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Order(**data)


class OrderFromCartDraftSchema(marshmallow.Schema):
    id = marshmallow.fields.String(allow_none=True, missing=None)
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    order_number = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="orderNumber"
    )
    payment_state = marshmallow_enum.EnumField(
        PaymentState,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="paymentState",
    )
    shipment_state = marshmallow_enum.EnumField(
        ShipmentState,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="shipmentState",
    )
    order_state = marshmallow_enum.EnumField(
        OrderState, by_value=True, allow_none=True, missing=None, data_key="orderState"
    )
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.OrderFromCartDraft(**data)


class OrderImportDraftSchema(marshmallow.Schema):
    order_number = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="orderNumber"
    )
    customer_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customerId"
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
        nested=helpers.absmod(__name__, ".cart.CustomLineItemDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="customLineItems",
    )
    total_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="totalPrice",
    )
    taxed_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.TaxedPriceDraftSchema"),
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
        nested=helpers.absmod(
            __name__, ".customer_group.CustomerGroupResourceIdentifierSchema"
        ),
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
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
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
    item_shipping_addresses = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="itemShippingAddresses",
    )
    store = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".store.StoreResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    origin = marshmallow_enum.EnumField(
        CartOrigin, by_value=True, allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.OrderImportDraft(**data)


class OrderPagedQueryResponseSchema(marshmallow.Schema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".OrderSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.OrderPagedQueryResponse(**data)


class OrderReferenceSchema(ReferenceSchema):
    obj = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".OrderSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.OrderReference(**data)


class OrderResourceIdentifierSchema(ResourceIdentifierSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.OrderResourceIdentifier(**data)


class OrderUpdateSchema(marshmallow.Schema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addDelivery": helpers.absmod(
                    __name__, ".OrderAddDeliveryActionSchema"
                ),
                "addItemShippingAddress": helpers.absmod(
                    __name__, ".OrderAddItemShippingAddressActionSchema"
                ),
                "addParcelToDelivery": helpers.absmod(
                    __name__, ".OrderAddParcelToDeliveryActionSchema"
                ),
                "addPayment": helpers.absmod(__name__, ".OrderAddPaymentActionSchema"),
                "addReturnInfo": helpers.absmod(
                    __name__, ".OrderAddReturnInfoActionSchema"
                ),
                "changeOrderState": helpers.absmod(
                    __name__, ".OrderChangeOrderStateActionSchema"
                ),
                "changePaymentState": helpers.absmod(
                    __name__, ".OrderChangePaymentStateActionSchema"
                ),
                "changeShipmentState": helpers.absmod(
                    __name__, ".OrderChangeShipmentStateActionSchema"
                ),
                "importCustomLineItemState": helpers.absmod(
                    __name__, ".OrderImportCustomLineItemStateActionSchema"
                ),
                "importLineItemState": helpers.absmod(
                    __name__, ".OrderImportLineItemStateActionSchema"
                ),
                "removeDelivery": helpers.absmod(
                    __name__, ".OrderRemoveDeliveryActionSchema"
                ),
                "removeItemShippingAddress": helpers.absmod(
                    __name__, ".OrderRemoveItemShippingAddressActionSchema"
                ),
                "removeParcelFromDelivery": helpers.absmod(
                    __name__, ".OrderRemoveParcelFromDeliveryActionSchema"
                ),
                "removePayment": helpers.absmod(
                    __name__, ".OrderRemovePaymentActionSchema"
                ),
                "setBillingAddress": helpers.absmod(
                    __name__, ".OrderSetBillingAddressActionSchema"
                ),
                "setCustomField": helpers.absmod(
                    __name__, ".OrderSetCustomFieldActionSchema"
                ),
                "setCustomLineItemCustomField": helpers.absmod(
                    __name__, ".OrderSetCustomLineItemCustomFieldActionSchema"
                ),
                "setCustomLineItemCustomType": helpers.absmod(
                    __name__, ".OrderSetCustomLineItemCustomTypeActionSchema"
                ),
                "setCustomLineItemShippingDetails": helpers.absmod(
                    __name__, ".OrderSetCustomLineItemShippingDetailsActionSchema"
                ),
                "setCustomType": helpers.absmod(
                    __name__, ".OrderSetCustomTypeActionSchema"
                ),
                "setCustomerEmail": helpers.absmod(
                    __name__, ".OrderSetCustomerEmailActionSchema"
                ),
                "setCustomerId": helpers.absmod(
                    __name__, ".OrderSetCustomerIdActionSchema"
                ),
                "setDeliveryAddress": helpers.absmod(
                    __name__, ".OrderSetDeliveryAddressActionSchema"
                ),
                "setDeliveryItems": helpers.absmod(
                    __name__, ".OrderSetDeliveryItemsActionSchema"
                ),
                "setLineItemCustomField": helpers.absmod(
                    __name__, ".OrderSetLineItemCustomFieldActionSchema"
                ),
                "setLineItemCustomType": helpers.absmod(
                    __name__, ".OrderSetLineItemCustomTypeActionSchema"
                ),
                "setLineItemShippingDetails": helpers.absmod(
                    __name__, ".OrderSetLineItemShippingDetailsActionSchema"
                ),
                "setLocale": helpers.absmod(__name__, ".OrderSetLocaleActionSchema"),
                "setOrderNumber": helpers.absmod(
                    __name__, ".OrderSetOrderNumberActionSchema"
                ),
                "setParcelItems": helpers.absmod(
                    __name__, ".OrderSetParcelItemsActionSchema"
                ),
                "setParcelMeasurements": helpers.absmod(
                    __name__, ".OrderSetParcelMeasurementsActionSchema"
                ),
                "setParcelTrackingData": helpers.absmod(
                    __name__, ".OrderSetParcelTrackingDataActionSchema"
                ),
                "setReturnPaymentState": helpers.absmod(
                    __name__, ".OrderSetReturnPaymentStateActionSchema"
                ),
                "setReturnShipmentState": helpers.absmod(
                    __name__, ".OrderSetReturnShipmentStateActionSchema"
                ),
                "setShippingAddress": helpers.absmod(
                    __name__, ".OrderSetShippingAddressActionSchema"
                ),
                "setStore": helpers.absmod(__name__, ".OrderSetStoreActionSchema"),
                "transitionCustomLineItemState": helpers.absmod(
                    __name__, ".OrderTransitionCustomLineItemStateActionSchema"
                ),
                "transitionLineItemState": helpers.absmod(
                    __name__, ".OrderTransitionLineItemStateActionSchema"
                ),
                "transitionState": helpers.absmod(
                    __name__, ".OrderTransitionStateActionSchema"
                ),
                "updateItemShippingAddress": helpers.absmod(
                    __name__, ".OrderUpdateItemShippingAddressActionSchema"
                ),
                "updateSyncInfo": helpers.absmod(
                    __name__, ".OrderUpdateSyncInfoActionSchema"
                ),
            },
        ),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.OrderUpdate(**data)


class OrderUpdateActionSchema(marshmallow.Schema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderUpdateAction(**data)


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


class ParcelDraftSchema(marshmallow.Schema):
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

        return models.ParcelDraft(**data)


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


class PaymentInfoSchema(marshmallow.Schema):
    payments = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".payment.PaymentReferenceSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.PaymentInfo(**data)


class ProductVariantImportDraftSchema(marshmallow.Schema):
    id = marshmallow.fields.Integer(allow_none=True, missing=None)
    sku = marshmallow.fields.String(allow_none=True, missing=None)
    prices = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.PriceDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    attributes = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".product.AttributeSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
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

        return models.ProductVariantImportDraft(**data)


class ReturnInfoSchema(marshmallow.Schema):
    items = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("type", "type"),
            discriminator_schemas={
                "CustomLineItemReturnItem": helpers.absmod(
                    __name__, ".CustomLineItemReturnItemSchema"
                ),
                "LineItemReturnItem": helpers.absmod(
                    __name__, ".LineItemReturnItemSchema"
                ),
            },
        ),
        allow_none=True,
        missing=None,
    )
    return_tracking_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="returnTrackingId"
    )
    return_date = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="returnDate"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ReturnInfo(**data)


class ReturnItemSchema(marshmallow.Schema):
    id = marshmallow.fields.String(allow_none=True, missing=None)
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)
    type = marshmallow.fields.String(allow_none=True, missing=None)
    comment = marshmallow.fields.String(allow_none=True, missing=None)
    shipment_state = marshmallow_enum.EnumField(
        ReturnShipmentState,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="shipmentState",
    )
    payment_state = marshmallow_enum.EnumField(
        ReturnPaymentState,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="paymentState",
    )
    last_modified_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="lastModifiedAt"
    )
    created_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="createdAt"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ReturnItem(**data)


class CustomLineItemReturnItemSchema(ReturnItemSchema):
    custom_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customLineItemId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CustomLineItemReturnItem(**data)


class LineItemReturnItemSchema(ReturnItemSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.LineItemReturnItem(**data)


class ReturnItemDraftSchema(marshmallow.Schema):
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    custom_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customLineItemId"
    )
    comment = marshmallow.fields.String(allow_none=True, missing=None)
    shipment_state = marshmallow_enum.EnumField(
        ReturnShipmentState,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="shipmentState",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ReturnItemDraft(**data)


class ShippingInfoImportDraftSchema(marshmallow.Schema):
    shipping_method_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="shippingMethodName"
    )
    price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    shipping_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".shipping_method.ShippingRateDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="shippingRate",
    )
    tax_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".tax_category.TaxRateSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="taxRate",
    )
    tax_category = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".tax_category.TaxCategoryResourceIdentifierSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="taxCategory",
    )
    shipping_method = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".shipping_method.ShippingMethodResourceIdentifierSchema"
        ),
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


class SyncInfoSchema(marshmallow.Schema):
    channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    external_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="externalId"
    )
    synced_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="syncedAt"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.SyncInfo(**data)


class TaxedItemPriceDraftSchema(marshmallow.Schema):
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

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.TaxedItemPriceDraft(**data)


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


class OrderAddDeliveryActionSchema(OrderUpdateActionSchema):
    items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".DeliveryItemSchema"),
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
    parcels = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ParcelDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderAddDeliveryAction(**data)


class OrderAddItemShippingAddressActionSchema(OrderUpdateActionSchema):
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
        del data["action"]
        return models.OrderAddItemShippingAddressAction(**data)


class OrderAddParcelToDeliveryActionSchema(OrderUpdateActionSchema):
    delivery_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="deliveryId"
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
        del data["action"]
        return models.OrderAddParcelToDeliveryAction(**data)


class OrderAddPaymentActionSchema(OrderUpdateActionSchema):
    payment = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".payment.PaymentResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderAddPaymentAction(**data)


class OrderAddReturnInfoActionSchema(OrderUpdateActionSchema):
    return_tracking_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="returnTrackingId"
    )
    items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ReturnItemDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    return_date = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="returnDate"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderAddReturnInfoAction(**data)


class OrderChangeOrderStateActionSchema(OrderUpdateActionSchema):
    order_state = marshmallow_enum.EnumField(
        OrderState, by_value=True, allow_none=True, missing=None, data_key="orderState"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderChangeOrderStateAction(**data)


class OrderChangePaymentStateActionSchema(OrderUpdateActionSchema):
    payment_state = marshmallow_enum.EnumField(
        PaymentState,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="paymentState",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderChangePaymentStateAction(**data)


class OrderChangeShipmentStateActionSchema(OrderUpdateActionSchema):
    shipment_state = marshmallow_enum.EnumField(
        ShipmentState,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="shipmentState",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderChangeShipmentStateAction(**data)


class OrderImportCustomLineItemStateActionSchema(OrderUpdateActionSchema):
    custom_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customLineItemId"
    )
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ItemStateSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderImportCustomLineItemStateAction(**data)


class OrderImportLineItemStateActionSchema(OrderUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ItemStateSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderImportLineItemStateAction(**data)


class OrderRemoveDeliveryActionSchema(OrderUpdateActionSchema):
    delivery_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="deliveryId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderRemoveDeliveryAction(**data)


class OrderRemoveItemShippingAddressActionSchema(OrderUpdateActionSchema):
    address_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderRemoveItemShippingAddressAction(**data)


class OrderRemoveParcelFromDeliveryActionSchema(OrderUpdateActionSchema):
    parcel_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="parcelId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderRemoveParcelFromDeliveryAction(**data)


class OrderRemovePaymentActionSchema(OrderUpdateActionSchema):
    payment = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".payment.PaymentResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderRemovePaymentAction(**data)


class OrderSetBillingAddressActionSchema(OrderUpdateActionSchema):
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
        del data["action"]
        return models.OrderSetBillingAddressAction(**data)


class OrderSetCustomFieldActionSchema(OrderUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderSetCustomFieldAction(**data)


class OrderSetCustomLineItemCustomFieldActionSchema(OrderUpdateActionSchema):
    custom_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customLineItemId"
    )
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderSetCustomLineItemCustomFieldAction(**data)


class OrderSetCustomLineItemCustomTypeActionSchema(OrderUpdateActionSchema):
    custom_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customLineItemId"
    )
    type = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.TypeResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    fields = FieldContainerField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderSetCustomLineItemCustomTypeAction(**data)


class OrderSetCustomLineItemShippingDetailsActionSchema(OrderUpdateActionSchema):
    custom_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customLineItemId"
    )
    shipping_details = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ItemShippingDetailsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="shippingDetails",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderSetCustomLineItemShippingDetailsAction(**data)


class OrderSetCustomTypeActionSchema(OrderUpdateActionSchema):
    type = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.TypeResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    fields = FieldContainerField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderSetCustomTypeAction(**data)


class OrderSetCustomerEmailActionSchema(OrderUpdateActionSchema):
    email = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderSetCustomerEmailAction(**data)


class OrderSetCustomerIdActionSchema(OrderUpdateActionSchema):
    customer_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customerId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderSetCustomerIdAction(**data)


class OrderSetDeliveryAddressActionSchema(OrderUpdateActionSchema):
    delivery_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="deliveryId"
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
        del data["action"]
        return models.OrderSetDeliveryAddressAction(**data)


class OrderSetDeliveryItemsActionSchema(OrderUpdateActionSchema):
    delivery_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="deliveryId"
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
        del data["action"]
        return models.OrderSetDeliveryItemsAction(**data)


class OrderSetLineItemCustomFieldActionSchema(OrderUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderSetLineItemCustomFieldAction(**data)


class OrderSetLineItemCustomTypeActionSchema(OrderUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    type = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.TypeResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    fields = FieldContainerField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderSetLineItemCustomTypeAction(**data)


class OrderSetLineItemShippingDetailsActionSchema(OrderUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    shipping_details = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ItemShippingDetailsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="shippingDetails",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderSetLineItemShippingDetailsAction(**data)


class OrderSetLocaleActionSchema(OrderUpdateActionSchema):
    locale = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderSetLocaleAction(**data)


class OrderSetOrderNumberActionSchema(OrderUpdateActionSchema):
    order_number = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="orderNumber"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderSetOrderNumberAction(**data)


class OrderSetParcelItemsActionSchema(OrderUpdateActionSchema):
    parcel_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="parcelId"
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
        del data["action"]
        return models.OrderSetParcelItemsAction(**data)


class OrderSetParcelMeasurementsActionSchema(OrderUpdateActionSchema):
    parcel_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="parcelId"
    )
    measurements = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ParcelMeasurementsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderSetParcelMeasurementsAction(**data)


class OrderSetParcelTrackingDataActionSchema(OrderUpdateActionSchema):
    parcel_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="parcelId"
    )
    tracking_data = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".TrackingDataSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="trackingData",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderSetParcelTrackingDataAction(**data)


class OrderSetReturnPaymentStateActionSchema(OrderUpdateActionSchema):
    return_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="returnItemId"
    )
    payment_state = marshmallow_enum.EnumField(
        ReturnPaymentState,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="paymentState",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderSetReturnPaymentStateAction(**data)


class OrderSetReturnShipmentStateActionSchema(OrderUpdateActionSchema):
    return_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="returnItemId"
    )
    shipment_state = marshmallow_enum.EnumField(
        ReturnShipmentState,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="shipmentState",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderSetReturnShipmentStateAction(**data)


class OrderSetShippingAddressActionSchema(OrderUpdateActionSchema):
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
        del data["action"]
        return models.OrderSetShippingAddressAction(**data)


class OrderSetStoreActionSchema(OrderUpdateActionSchema):
    store = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".store.StoreResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderSetStoreAction(**data)


class OrderTransitionCustomLineItemStateActionSchema(OrderUpdateActionSchema):
    custom_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customLineItemId"
    )
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)
    from_state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="fromState",
    )
    to_state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="toState",
    )
    actual_transition_date = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="actualTransitionDate"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderTransitionCustomLineItemStateAction(**data)


class OrderTransitionLineItemStateActionSchema(OrderUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)
    from_state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="fromState",
    )
    to_state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="toState",
    )
    actual_transition_date = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="actualTransitionDate"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderTransitionLineItemStateAction(**data)


class OrderTransitionStateActionSchema(OrderUpdateActionSchema):
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    force = marshmallow.fields.Boolean(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderTransitionStateAction(**data)


class OrderUpdateItemShippingAddressActionSchema(OrderUpdateActionSchema):
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
        del data["action"]
        return models.OrderUpdateItemShippingAddressAction(**data)


class OrderUpdateSyncInfoActionSchema(OrderUpdateActionSchema):
    channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    external_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="externalId"
    )
    synced_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="syncedAt"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderUpdateSyncInfoAction(**data)
