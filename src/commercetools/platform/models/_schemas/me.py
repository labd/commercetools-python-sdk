# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..cart import (
    CartOrigin,
    CartState,
    InventoryMode,
    RoundingMode,
    TaxCalculationMode,
    TaxMode,
)
from ..order import OrderState, PaymentState, ShipmentState
from ..payment import TransactionType
from .common import BaseResourceSchema, LocalizedStringField
from .type import FieldContainerField

# Fields


# Marshmallow Schemas
class MyCartSchema(BaseResourceSchema):
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
    cart_state = marshmallow_enum.EnumField(
        CartState, by_value=True, allow_none=True, missing=None, data_key="cartState"
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
    inventory_mode = marshmallow_enum.EnumField(
        InventoryMode,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="inventoryMode",
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
    tax_calculation_mode = marshmallow_enum.EnumField(
        TaxCalculationMode,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="taxCalculationMode",
    )
    customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer_group.CustomerGroupReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="customerGroup",
    )
    country = marshmallow.fields.String(allow_none=True, missing=None)
    shipping_info = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ShippingInfoSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="shippingInfo",
    )
    discount_codes = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.DiscountCodeInfoSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="discountCodes",
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    payment_info = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.PaymentInfoSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="paymentInfo",
    )
    locale = marshmallow.fields.String(allow_none=True, missing=None)
    delete_days_after_last_modification = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="deleteDaysAfterLastModification"
    )
    refused_gifts = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart_discount.CartDiscountReferenceSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="refusedGifts",
    )
    origin = marshmallow_enum.EnumField(
        CartOrigin, by_value=True, allow_none=True, missing=None
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

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MyCart(**data)


class MyCartDraftSchema(marshmallow.Schema):
    currency = marshmallow.fields.String(allow_none=True, missing=None)
    customer_email = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customerEmail"
    )
    country = marshmallow.fields.String(allow_none=True, missing=None)
    inventory_mode = marshmallow_enum.EnumField(
        InventoryMode,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="inventoryMode",
    )
    line_items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".MyLineItemDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="lineItems",
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
    shipping_method = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".shipping_method.ShippingMethodResourceIdentifierSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="shippingMethod",
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    locale = marshmallow.fields.String(allow_none=True, missing=None)
    tax_mode = marshmallow_enum.EnumField(
        TaxMode, by_value=True, allow_none=True, missing=None, data_key="taxMode"
    )
    delete_days_after_last_modification = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="deleteDaysAfterLastModification"
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
        nested=helpers.absmod(__name__, ".store.StoreKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    discount_codes = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.DiscountCodeInfoSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="discountCodes",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MyCartDraft(**data)


class MyCartUpdateSchema(marshmallow.Schema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addDiscountCode": helpers.absmod(
                    __name__, ".MyCartAddDiscountCodeActionSchema"
                ),
                "addItemShippingAddress": helpers.absmod(
                    __name__, ".MyCartAddItemShippingAddressActionSchema"
                ),
                "addLineItem": helpers.absmod(
                    __name__, ".MyCartAddLineItemActionSchema"
                ),
                "addPayment": helpers.absmod(__name__, ".MyCartAddPaymentActionSchema"),
                "applyDeltaToLineItemShippingDetailsTargets": helpers.absmod(
                    __name__,
                    ".MyCartApplyDeltaToLineItemShippingDetailsTargetsActionSchema",
                ),
                "changeLineItemQuantity": helpers.absmod(
                    __name__, ".MyCartChangeLineItemQuantityActionSchema"
                ),
                "changeTaxMode": helpers.absmod(
                    __name__, ".MyCartChangeTaxModeActionSchema"
                ),
                "recalculate": helpers.absmod(
                    __name__, ".MyCartRecalculateActionSchema"
                ),
                "removeDiscountCode": helpers.absmod(
                    __name__, ".MyCartRemoveDiscountCodeActionSchema"
                ),
                "removeItemShippingAddress": helpers.absmod(
                    __name__, ".MyCartRemoveItemShippingAddressActionSchema"
                ),
                "removeLineItem": helpers.absmod(
                    __name__, ".MyCartRemoveLineItemActionSchema"
                ),
                "removePayment": helpers.absmod(
                    __name__, ".MyCartRemovePaymentActionSchema"
                ),
                "setBillingAddress": helpers.absmod(
                    __name__, ".MyCartSetBillingAddressActionSchema"
                ),
                "setCountry": helpers.absmod(__name__, ".MyCartSetCountryActionSchema"),
                "setCustomField": helpers.absmod(
                    __name__, ".MyCartSetCustomFieldActionSchema"
                ),
                "setCustomShippingMethod": helpers.absmod(
                    __name__, ".MyCartSetCustomShippingMethodActionSchema"
                ),
                "setCustomType": helpers.absmod(
                    __name__, ".MyCartSetCustomTypeActionSchema"
                ),
                "setDeleteDaysAfterLastModification": helpers.absmod(
                    __name__, ".MyCartSetDeleteDaysAfterLastModificationActionSchema"
                ),
                "setLineItemCustomField": helpers.absmod(
                    __name__, ".MyCartSetLineItemCustomFieldActionSchema"
                ),
                "setLineItemCustomType": helpers.absmod(
                    __name__, ".MyCartSetLineItemCustomTypeActionSchema"
                ),
                "setLineItemDistributionChannel": helpers.absmod(
                    __name__, ".MyCartSetLineItemDistributionChannelActionSchema"
                ),
                "setLineItemShippingDetails": helpers.absmod(
                    __name__, ".MyCartSetLineItemShippingDetailsActionSchema"
                ),
                "setLocale": helpers.absmod(__name__, ".MyCartSetLocaleActionSchema"),
                "setShippingAddress": helpers.absmod(
                    __name__, ".MyCartSetShippingAddressActionSchema"
                ),
                "setShippingMethod": helpers.absmod(
                    __name__, ".MyCartSetShippingMethodActionSchema"
                ),
                "updateItemShippingAddress": helpers.absmod(
                    __name__, ".MyCartUpdateItemShippingAddressActionSchema"
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

        return models.MyCartUpdate(**data)


class MyCartUpdateActionSchema(marshmallow.Schema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCartUpdateAction(**data)


class MyCustomerSchema(BaseResourceSchema):
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
    customer_number = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customerNumber"
    )
    email = marshmallow.fields.String(allow_none=True, missing=None)
    password = marshmallow.fields.String(allow_none=True, missing=None)
    first_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="firstName"
    )
    last_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lastName"
    )
    middle_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="middleName"
    )
    title = marshmallow.fields.String(allow_none=True, missing=None)
    date_of_birth = marshmallow.fields.Date(
        allow_none=True, missing=None, data_key="dateOfBirth"
    )
    company_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="companyName"
    )
    vat_id = marshmallow.fields.String(allow_none=True, missing=None, data_key="vatId")
    addresses = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    default_shipping_address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="defaultShippingAddressId"
    )
    shipping_address_ids = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        missing=None,
        data_key="shippingAddressIds",
    )
    default_billing_address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="defaultBillingAddressId"
    )
    billing_address_ids = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        missing=None,
        data_key="billingAddressIds",
    )
    is_email_verified = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="isEmailVerified"
    )
    external_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="externalId"
    )
    customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer_group.CustomerGroupReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="customerGroup",
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    locale = marshmallow.fields.String(allow_none=True, missing=None)
    salutation = marshmallow.fields.String(allow_none=True, missing=None)
    key = marshmallow.fields.String(allow_none=True, missing=None)
    stores = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".store.StoreKeyReferenceSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MyCustomer(**data)


class MyCustomerDraftSchema(marshmallow.Schema):
    email = marshmallow.fields.String(allow_none=True, missing=None)
    password = marshmallow.fields.String(allow_none=True, missing=None)
    first_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="firstName"
    )
    last_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lastName"
    )
    middle_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="middleName"
    )
    title = marshmallow.fields.String(allow_none=True, missing=None)
    date_of_birth = marshmallow.fields.Date(
        allow_none=True, missing=None, data_key="dateOfBirth"
    )
    company_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="companyName"
    )
    vat_id = marshmallow.fields.String(allow_none=True, missing=None, data_key="vatId")
    addresses = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    default_shipping_address = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="defaultShippingAddress"
    )
    default_billing_address = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="defaultBillingAddress"
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    locale = marshmallow.fields.String(allow_none=True, missing=None)
    stores = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".store.StoreResourceIdentifierSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MyCustomerDraft(**data)


class MyCustomerUpdateSchema(marshmallow.Schema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addAddress": helpers.absmod(
                    __name__, ".MyCustomerAddAddressActionSchema"
                ),
                "addBillingAddressId": helpers.absmod(
                    __name__, ".MyCustomerAddBillingAddressIdActionSchema"
                ),
                "addShippingAddressId": helpers.absmod(
                    __name__, ".MyCustomerAddShippingAddressIdActionSchema"
                ),
                "changeAddress": helpers.absmod(
                    __name__, ".MyCustomerChangeAddressActionSchema"
                ),
                "changeEmail": helpers.absmod(
                    __name__, ".MyCustomerChangeEmailActionSchema"
                ),
                "removeAddress": helpers.absmod(
                    __name__, ".MyCustomerRemoveAddressActionSchema"
                ),
                "removeBillingAddressId": helpers.absmod(
                    __name__, ".MyCustomerRemoveBillingAddressIdActionSchema"
                ),
                "removeShippingAddressId": helpers.absmod(
                    __name__, ".MyCustomerRemoveShippingAddressIdActionSchema"
                ),
                "setCompanyName": helpers.absmod(
                    __name__, ".MyCustomerSetCompanyNameActionSchema"
                ),
                "setCustomField": helpers.absmod(
                    __name__, ".MyCustomerSetCustomFieldActionSchema"
                ),
                "setCustomType": helpers.absmod(
                    __name__, ".MyCustomerSetCustomTypeActionSchema"
                ),
                "setDateOfBirth": helpers.absmod(
                    __name__, ".MyCustomerSetDateOfBirthActionSchema"
                ),
                "setDefaultBillingAddress": helpers.absmod(
                    __name__, ".MyCustomerSetDefaultBillingAddressActionSchema"
                ),
                "setDefaultShippingAddress": helpers.absmod(
                    __name__, ".MyCustomerSetDefaultShippingAddressActionSchema"
                ),
                "setFirstName": helpers.absmod(
                    __name__, ".MyCustomerSetFirstNameActionSchema"
                ),
                "setLastName": helpers.absmod(
                    __name__, ".MyCustomerSetLastNameActionSchema"
                ),
                "setLocale": helpers.absmod(
                    __name__, ".MyCustomerSetLocaleActionSchema"
                ),
                "setMiddleName": helpers.absmod(
                    __name__, ".MyCustomerSetMiddleNameActionSchema"
                ),
                "setSalutation": helpers.absmod(
                    __name__, ".MyCustomerSetSalutationActionSchema"
                ),
                "setTitle": helpers.absmod(__name__, ".MyCustomerSetTitleActionSchema"),
                "setVatId": helpers.absmod(__name__, ".MyCustomerSetVatIdActionSchema"),
            },
        ),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MyCustomerUpdate(**data)


class MyCustomerUpdateActionSchema(marshmallow.Schema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCustomerUpdateAction(**data)


class MyLineItemDraftSchema(marshmallow.Schema):
    product_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="productId"
    )
    variant_id = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="variantId"
    )
    quantity = marshmallow.fields.Float(allow_none=True, missing=None)
    added_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="addedAt"
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
    sku = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MyLineItemDraft(**data)


class MyOrderSchema(BaseResourceSchema):
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
        nested=helpers.absmod(__name__, ".order.SyncInfoSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="syncInfo",
    )
    return_info = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.ReturnInfoSchema"),
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
        nested=helpers.absmod(__name__, ".order.PaymentInfoSchema"),
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

        return models.MyOrder(**data)


class MyOrderFromCartDraftSchema(marshmallow.Schema):
    id = marshmallow.fields.String(allow_none=True, missing=None)
    version = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MyOrderFromCartDraft(**data)


class MyPaymentSchema(marshmallow.Schema):
    id = marshmallow.fields.String(allow_none=True, missing=None)
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    customer = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer.CustomerReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    anonymous_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="anonymousId"
    )
    amount_planned = helpers.Discriminator(
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
        data_key="amountPlanned",
    )
    payment_method_info = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".payment.PaymentMethodInfoSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="paymentMethodInfo",
    )
    transactions = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".payment.TransactionSchema"),
        allow_none=True,
        many=True,
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

        return models.MyPayment(**data)


class MyPaymentDraftSchema(marshmallow.Schema):
    amount_planned = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="amountPlanned",
    )
    payment_method_info = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".payment.PaymentMethodInfoSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="paymentMethodInfo",
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    transaction = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".MyTransactionDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MyPaymentDraft(**data)


class MyPaymentPagedQueryResponseSchema(marshmallow.Schema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".MyPaymentSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MyPaymentPagedQueryResponse(**data)


class MyPaymentUpdateSchema(marshmallow.Schema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addTransaction": helpers.absmod(
                    __name__, ".MyPaymentAddTransactionActionSchema"
                ),
                "changeAmountPlanned": helpers.absmod(
                    __name__, ".MyPaymentChangeAmountPlannedActionSchema"
                ),
                "setCustomField": helpers.absmod(
                    __name__, ".MyPaymentSetCustomFieldActionSchema"
                ),
                "setMethodInfoInterface": helpers.absmod(
                    __name__, ".MyPaymentSetMethodInfoInterfaceActionSchema"
                ),
                "setMethodInfoMethod": helpers.absmod(
                    __name__, ".MyPaymentSetMethodInfoMethodActionSchema"
                ),
                "setMethodInfoName": helpers.absmod(
                    __name__, ".MyPaymentSetMethodInfoNameActionSchema"
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

        return models.MyPaymentUpdate(**data)


class MyPaymentUpdateActionSchema(marshmallow.Schema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyPaymentUpdateAction(**data)


class MyShoppingListDraftSchema(marshmallow.Schema):
    name = LocalizedStringField(allow_none=True, missing=None)
    description = LocalizedStringField(allow_none=True, missing=None)
    line_items = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".shopping_list.ShoppingListLineItemDraftSchema"
        ),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="lineItems",
    )
    text_line_items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".shopping_list.TextLineItemDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="textLineItems",
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    delete_days_after_last_modification = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="deleteDaysAfterLastModification"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MyShoppingListDraft(**data)


class MyShoppingListUpdateSchema(marshmallow.Schema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addLineItem": helpers.absmod(
                    __name__, ".MyShoppingListAddLineItemActionSchema"
                ),
                "addTextLineItem": helpers.absmod(
                    __name__, ".MyShoppingListAddTextLineItemActionSchema"
                ),
                "changeLineItemQuantity": helpers.absmod(
                    __name__, ".MyShoppingListChangeLineItemQuantityActionSchema"
                ),
                "changeLineItemsOrder": helpers.absmod(
                    __name__, ".MyShoppingListChangeLineItemsOrderActionSchema"
                ),
                "changeName": helpers.absmod(
                    __name__, ".MyShoppingListChangeNameActionSchema"
                ),
                "changeTextLineItemName": helpers.absmod(
                    __name__, ".MyShoppingListChangeTextLineItemNameActionSchema"
                ),
                "changeTextLineItemQuantity": helpers.absmod(
                    __name__, ".MyShoppingListChangeTextLineItemQuantityActionSchema"
                ),
                "changeTextLineItemsOrder": helpers.absmod(
                    __name__, ".MyShoppingListChangeTextLineItemsOrderActionSchema"
                ),
                "removeLineItem": helpers.absmod(
                    __name__, ".MyShoppingListRemoveLineItemActionSchema"
                ),
                "removeTextLineItem": helpers.absmod(
                    __name__, ".MyShoppingListRemoveTextLineItemActionSchema"
                ),
                "setCustomField": helpers.absmod(
                    __name__, ".MyShoppingListSetCustomFieldActionSchema"
                ),
                "setCustomType": helpers.absmod(
                    __name__, ".MyShoppingListSetCustomTypeActionSchema"
                ),
                "setDeleteDaysAfterLastModification": helpers.absmod(
                    __name__,
                    ".MyShoppingListSetDeleteDaysAfterLastModificationActionSchema",
                ),
                "setDescription": helpers.absmod(
                    __name__, ".MyShoppingListSetDescriptionActionSchema"
                ),
                "setLineItemCustomField": helpers.absmod(
                    __name__, ".MyShoppingListSetLineItemCustomFieldActionSchema"
                ),
                "setLineItemCustomType": helpers.absmod(
                    __name__, ".MyShoppingListSetLineItemCustomTypeActionSchema"
                ),
                "setTextLineItemCustomField": helpers.absmod(
                    __name__, ".MyShoppingListSetTextLineItemCustomFieldActionSchema"
                ),
                "setTextLineItemCustomType": helpers.absmod(
                    __name__, ".MyShoppingListSetTextLineItemCustomTypeActionSchema"
                ),
                "setTextLineItemDescription": helpers.absmod(
                    __name__, ".MyShoppingListSetTextLineItemDescriptionActionSchema"
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

        return models.MyShoppingListUpdate(**data)


class MyShoppingListUpdateActionSchema(marshmallow.Schema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyShoppingListUpdateAction(**data)


class MyTransactionDraftSchema(marshmallow.Schema):
    timestamp = marshmallow.fields.DateTime(allow_none=True, missing=None)
    type = marshmallow_enum.EnumField(
        TransactionType, by_value=True, allow_none=True, missing=None
    )
    amount = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    interaction_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="interactionId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MyTransactionDraft(**data)


class MyCartAddDiscountCodeActionSchema(MyCartUpdateActionSchema):
    code = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCartAddDiscountCodeAction(**data)


class MyCartAddItemShippingAddressActionSchema(MyCartUpdateActionSchema):
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
        return models.MyCartAddItemShippingAddressAction(**data)


class MyCartAddLineItemActionSchema(MyCartUpdateActionSchema):
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    distribution_channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="distributionChannel",
    )
    external_tax_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ExternalTaxRateDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="externalTaxRate",
    )
    product_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="productId"
    )
    variant_id = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="variantId"
    )
    sku = marshmallow.fields.String(allow_none=True, missing=None)
    quantity = marshmallow.fields.Float(allow_none=True, missing=None)
    supply_channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="supplyChannel",
    )
    external_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="externalPrice",
    )
    external_total_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ExternalLineItemTotalPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="externalTotalPrice",
    )
    shipping_details = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ItemShippingDetailsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="shippingDetails",
    )
    added_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="addedAt"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCartAddLineItemAction(**data)


class MyCartAddPaymentActionSchema(MyCartUpdateActionSchema):
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
        return models.MyCartAddPaymentAction(**data)


class MyCartApplyDeltaToLineItemShippingDetailsTargetsActionSchema(
    MyCartUpdateActionSchema
):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    targets_delta = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ItemShippingTargetSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="targetsDelta",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCartApplyDeltaToLineItemShippingDetailsTargetsAction(**data)


class MyCartChangeLineItemQuantityActionSchema(MyCartUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    quantity = marshmallow.fields.Float(allow_none=True, missing=None)
    external_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="externalPrice",
    )
    external_total_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ExternalLineItemTotalPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="externalTotalPrice",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCartChangeLineItemQuantityAction(**data)


class MyCartChangeTaxModeActionSchema(MyCartUpdateActionSchema):
    tax_mode = marshmallow_enum.EnumField(
        TaxMode, by_value=True, allow_none=True, missing=None, data_key="taxMode"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCartChangeTaxModeAction(**data)


class MyCartRecalculateActionSchema(MyCartUpdateActionSchema):
    update_product_data = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="updateProductData"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCartRecalculateAction(**data)


class MyCartRemoveDiscountCodeActionSchema(MyCartUpdateActionSchema):
    discount_code = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".discount_code.DiscountCodeReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="discountCode",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCartRemoveDiscountCodeAction(**data)


class MyCartRemoveItemShippingAddressActionSchema(MyCartUpdateActionSchema):
    address_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCartRemoveItemShippingAddressAction(**data)


class MyCartRemoveLineItemActionSchema(MyCartUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    quantity = marshmallow.fields.Float(allow_none=True, missing=None)
    external_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="externalPrice",
    )
    external_total_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ExternalLineItemTotalPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="externalTotalPrice",
    )
    shipping_details_to_remove = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ItemShippingDetailsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="shippingDetailsToRemove",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCartRemoveLineItemAction(**data)


class MyCartRemovePaymentActionSchema(MyCartUpdateActionSchema):
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
        return models.MyCartRemovePaymentAction(**data)


class MyCartSetBillingAddressActionSchema(MyCartUpdateActionSchema):
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
        return models.MyCartSetBillingAddressAction(**data)


class MyCartSetCountryActionSchema(MyCartUpdateActionSchema):
    country = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCartSetCountryAction(**data)


class MyCartSetCustomFieldActionSchema(MyCartUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCartSetCustomFieldAction(**data)


class MyCartSetCustomShippingMethodActionSchema(MyCartUpdateActionSchema):
    shipping_method_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="shippingMethodName"
    )
    shipping_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".shipping_method.ShippingRateDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="shippingRate",
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
    external_tax_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ExternalTaxRateDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="externalTaxRate",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCartSetCustomShippingMethodAction(**data)


class MyCartSetCustomTypeActionSchema(MyCartUpdateActionSchema):
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
        return models.MyCartSetCustomTypeAction(**data)


class MyCartSetDeleteDaysAfterLastModificationActionSchema(MyCartUpdateActionSchema):
    delete_days_after_last_modification = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="deleteDaysAfterLastModification"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCartSetDeleteDaysAfterLastModificationAction(**data)


class MyCartSetLineItemCustomFieldActionSchema(MyCartUpdateActionSchema):
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
        return models.MyCartSetLineItemCustomFieldAction(**data)


class MyCartSetLineItemCustomTypeActionSchema(MyCartUpdateActionSchema):
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
        return models.MyCartSetLineItemCustomTypeAction(**data)


class MyCartSetLineItemDistributionChannelActionSchema(MyCartUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    distribution_channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="distributionChannel",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCartSetLineItemDistributionChannelAction(**data)


class MyCartSetLineItemShippingDetailsActionSchema(MyCartUpdateActionSchema):
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
        return models.MyCartSetLineItemShippingDetailsAction(**data)


class MyCartSetLocaleActionSchema(MyCartUpdateActionSchema):
    locale = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCartSetLocaleAction(**data)


class MyCartSetShippingAddressActionSchema(MyCartUpdateActionSchema):
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
        return models.MyCartSetShippingAddressAction(**data)


class MyCartSetShippingMethodActionSchema(MyCartUpdateActionSchema):
    shipping_method = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".shipping_method.ShippingMethodResourceIdentifierSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="shippingMethod",
    )
    external_tax_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ExternalTaxRateDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="externalTaxRate",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCartSetShippingMethodAction(**data)


class MyCartUpdateItemShippingAddressActionSchema(MyCartUpdateActionSchema):
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
        return models.MyCartUpdateItemShippingAddressAction(**data)


class MyCustomerAddAddressActionSchema(MyCustomerUpdateActionSchema):
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
        return models.MyCustomerAddAddressAction(**data)


class MyCustomerAddBillingAddressIdActionSchema(MyCustomerUpdateActionSchema):
    address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressId"
    )
    address_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCustomerAddBillingAddressIdAction(**data)


class MyCustomerAddShippingAddressIdActionSchema(MyCustomerUpdateActionSchema):
    address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressId"
    )
    address_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCustomerAddShippingAddressIdAction(**data)


class MyCustomerChangeAddressActionSchema(MyCustomerUpdateActionSchema):
    address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressId"
    )
    address_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressKey"
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
        return models.MyCustomerChangeAddressAction(**data)


class MyCustomerChangeEmailActionSchema(MyCustomerUpdateActionSchema):
    email = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCustomerChangeEmailAction(**data)


class MyCustomerRemoveAddressActionSchema(MyCustomerUpdateActionSchema):
    address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressId"
    )
    address_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCustomerRemoveAddressAction(**data)


class MyCustomerRemoveBillingAddressIdActionSchema(MyCustomerUpdateActionSchema):
    address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressId"
    )
    address_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCustomerRemoveBillingAddressIdAction(**data)


class MyCustomerRemoveShippingAddressIdActionSchema(MyCustomerUpdateActionSchema):
    address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressId"
    )
    address_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCustomerRemoveShippingAddressIdAction(**data)


class MyCustomerSetCompanyNameActionSchema(MyCustomerUpdateActionSchema):
    company_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="companyName"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCustomerSetCompanyNameAction(**data)


class MyCustomerSetCustomFieldActionSchema(MyCustomerUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCustomerSetCustomFieldAction(**data)


class MyCustomerSetCustomTypeActionSchema(MyCustomerUpdateActionSchema):
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
        return models.MyCustomerSetCustomTypeAction(**data)


class MyCustomerSetDateOfBirthActionSchema(MyCustomerUpdateActionSchema):
    date_of_birth = marshmallow.fields.Date(
        allow_none=True, missing=None, data_key="dateOfBirth"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCustomerSetDateOfBirthAction(**data)


class MyCustomerSetDefaultBillingAddressActionSchema(MyCustomerUpdateActionSchema):
    address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressId"
    )
    address_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCustomerSetDefaultBillingAddressAction(**data)


class MyCustomerSetDefaultShippingAddressActionSchema(MyCustomerUpdateActionSchema):
    address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressId"
    )
    address_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCustomerSetDefaultShippingAddressAction(**data)


class MyCustomerSetFirstNameActionSchema(MyCustomerUpdateActionSchema):
    first_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="firstName"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCustomerSetFirstNameAction(**data)


class MyCustomerSetLastNameActionSchema(MyCustomerUpdateActionSchema):
    last_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lastName"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCustomerSetLastNameAction(**data)


class MyCustomerSetLocaleActionSchema(MyCustomerUpdateActionSchema):
    locale = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCustomerSetLocaleAction(**data)


class MyCustomerSetMiddleNameActionSchema(MyCustomerUpdateActionSchema):
    middle_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="middleName"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCustomerSetMiddleNameAction(**data)


class MyCustomerSetSalutationActionSchema(MyCustomerUpdateActionSchema):
    salutation = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCustomerSetSalutationAction(**data)


class MyCustomerSetTitleActionSchema(MyCustomerUpdateActionSchema):
    title = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCustomerSetTitleAction(**data)


class MyCustomerSetVatIdActionSchema(MyCustomerUpdateActionSchema):
    vat_id = marshmallow.fields.String(allow_none=True, missing=None, data_key="vatId")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyCustomerSetVatIdAction(**data)


class MyPaymentAddTransactionActionSchema(MyPaymentUpdateActionSchema):
    transaction = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".payment.TransactionDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyPaymentAddTransactionAction(**data)


class MyPaymentChangeAmountPlannedActionSchema(MyPaymentUpdateActionSchema):
    amount = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyPaymentChangeAmountPlannedAction(**data)


class MyPaymentSetCustomFieldActionSchema(MyPaymentUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyPaymentSetCustomFieldAction(**data)


class MyPaymentSetMethodInfoInterfaceActionSchema(MyPaymentUpdateActionSchema):
    interface = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyPaymentSetMethodInfoInterfaceAction(**data)


class MyPaymentSetMethodInfoMethodActionSchema(MyPaymentUpdateActionSchema):
    method = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyPaymentSetMethodInfoMethodAction(**data)


class MyPaymentSetMethodInfoNameActionSchema(MyPaymentUpdateActionSchema):
    name = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyPaymentSetMethodInfoNameAction(**data)


class MyShoppingListAddLineItemActionSchema(MyShoppingListUpdateActionSchema):
    sku = marshmallow.fields.String(allow_none=True, missing=None)
    product_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="productId"
    )
    variant_id = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="variantId"
    )
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)
    added_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="addedAt"
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyShoppingListAddLineItemAction(**data)


class MyShoppingListAddTextLineItemActionSchema(MyShoppingListUpdateActionSchema):
    name = LocalizedStringField(allow_none=True, missing=None)
    description = LocalizedStringField(allow_none=True, missing=None)
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)
    added_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="addedAt"
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyShoppingListAddTextLineItemAction(**data)


class MyShoppingListChangeLineItemQuantityActionSchema(
    MyShoppingListUpdateActionSchema
):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyShoppingListChangeLineItemQuantityAction(**data)


class MyShoppingListChangeLineItemsOrderActionSchema(MyShoppingListUpdateActionSchema):
    line_item_order = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        missing=None,
        data_key="lineItemOrder",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyShoppingListChangeLineItemsOrderAction(**data)


class MyShoppingListChangeNameActionSchema(MyShoppingListUpdateActionSchema):
    name = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyShoppingListChangeNameAction(**data)


class MyShoppingListChangeTextLineItemNameActionSchema(
    MyShoppingListUpdateActionSchema
):
    text_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="textLineItemId"
    )
    name = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyShoppingListChangeTextLineItemNameAction(**data)


class MyShoppingListChangeTextLineItemQuantityActionSchema(
    MyShoppingListUpdateActionSchema
):
    text_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="textLineItemId"
    )
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyShoppingListChangeTextLineItemQuantityAction(**data)


class MyShoppingListChangeTextLineItemsOrderActionSchema(
    MyShoppingListUpdateActionSchema
):
    text_line_item_order = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        missing=None,
        data_key="textLineItemOrder",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyShoppingListChangeTextLineItemsOrderAction(**data)


class MyShoppingListRemoveLineItemActionSchema(MyShoppingListUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyShoppingListRemoveLineItemAction(**data)


class MyShoppingListRemoveTextLineItemActionSchema(MyShoppingListUpdateActionSchema):
    text_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="textLineItemId"
    )
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyShoppingListRemoveTextLineItemAction(**data)


class MyShoppingListSetCustomFieldActionSchema(MyShoppingListUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyShoppingListSetCustomFieldAction(**data)


class MyShoppingListSetCustomTypeActionSchema(MyShoppingListUpdateActionSchema):
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
        return models.MyShoppingListSetCustomTypeAction(**data)


class MyShoppingListSetDeleteDaysAfterLastModificationActionSchema(
    MyShoppingListUpdateActionSchema
):
    delete_days_after_last_modification = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="deleteDaysAfterLastModification"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyShoppingListSetDeleteDaysAfterLastModificationAction(**data)


class MyShoppingListSetDescriptionActionSchema(MyShoppingListUpdateActionSchema):
    description = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyShoppingListSetDescriptionAction(**data)


class MyShoppingListSetLineItemCustomFieldActionSchema(
    MyShoppingListUpdateActionSchema
):
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
        return models.MyShoppingListSetLineItemCustomFieldAction(**data)


class MyShoppingListSetLineItemCustomTypeActionSchema(MyShoppingListUpdateActionSchema):
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
        return models.MyShoppingListSetLineItemCustomTypeAction(**data)


class MyShoppingListSetTextLineItemCustomFieldActionSchema(
    MyShoppingListUpdateActionSchema
):
    text_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="textLineItemId"
    )
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyShoppingListSetTextLineItemCustomFieldAction(**data)


class MyShoppingListSetTextLineItemCustomTypeActionSchema(
    MyShoppingListUpdateActionSchema
):
    text_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="textLineItemId"
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
        return models.MyShoppingListSetTextLineItemCustomTypeAction(**data)


class MyShoppingListSetTextLineItemDescriptionActionSchema(
    MyShoppingListUpdateActionSchema
):
    text_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="textLineItemId"
    )
    description = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.MyShoppingListSetTextLineItemDescriptionAction(**data)
