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
    DiscountCodeState,
    InventoryMode,
    LineItemMode,
    LineItemPriceMode,
    RoundingMode,
    ShippingMethodState,
    TaxCalculationMode,
    TaxMode,
)
from ..common import ReferenceTypeId
from .common import (
    BaseResourceSchema,
    LocalizedStringField,
    ReferenceSchema,
    ResourceIdentifierSchema,
)
from .type import FieldContainerField

# Fields


# Marshmallow Schemas
class CartSchema(BaseResourceSchema):
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
        nested=helpers.absmod(__name__, ".LineItemSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="lineItems",
    )
    custom_line_items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".CustomLineItemSchema"),
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
        nested=helpers.absmod(__name__, ".TaxedPriceSchema"),
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
        nested=helpers.absmod(__name__, ".ShippingInfoSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="shippingInfo",
    )
    discount_codes = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".DiscountCodeInfoSchema"),
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
                __name__, ".ClassificationShippingRateInputSchema"
            ),
            "Score": helpers.absmod(__name__, ".ScoreShippingRateInputSchema"),
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

        return models.Cart(**data)


class CartDraftSchema(marshmallow.Schema):
    currency = marshmallow.fields.String(allow_none=True, missing=None)
    customer_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customerId"
    )
    customer_email = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customerEmail"
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
    anonymous_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="anonymousId"
    )
    store = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".store.StoreResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    country = marshmallow.fields.String(allow_none=True, missing=None)
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
    line_items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".LineItemDraftSchema"),
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
    external_tax_rate_for_shipping_method = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ExternalTaxRateDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="externalTaxRateForShippingMethod",
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    locale = marshmallow.fields.String(allow_none=True, missing=None)
    delete_days_after_last_modification = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="deleteDaysAfterLastModification"
    )
    origin = marshmallow_enum.EnumField(
        CartOrigin, by_value=True, allow_none=True, missing=None
    )
    shipping_rate_input = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "Classification": helpers.absmod(
                __name__, ".ClassificationShippingRateInputDraftSchema"
            ),
            "Score": helpers.absmod(__name__, ".ScoreShippingRateInputDraftSchema"),
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
    discount_codes = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        missing=None,
        data_key="discountCodes",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CartDraft(**data)


class CartPagedQueryResponseSchema(marshmallow.Schema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".CartSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CartPagedQueryResponse(**data)


class CartReferenceSchema(ReferenceSchema):
    obj = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".CartSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.CartReference(**data)


class CartResourceIdentifierSchema(ResourceIdentifierSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.CartResourceIdentifier(**data)


class CartUpdateSchema(marshmallow.Schema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addCustomLineItem": helpers.absmod(
                    __name__, ".CartAddCustomLineItemActionSchema"
                ),
                "addDiscountCode": helpers.absmod(
                    __name__, ".CartAddDiscountCodeActionSchema"
                ),
                "addItemShippingAddress": helpers.absmod(
                    __name__, ".CartAddItemShippingAddressActionSchema"
                ),
                "addLineItem": helpers.absmod(__name__, ".CartAddLineItemActionSchema"),
                "addPayment": helpers.absmod(__name__, ".CartAddPaymentActionSchema"),
                "addShoppingList": helpers.absmod(
                    __name__, ".CartAddShoppingListActionSchema"
                ),
                "applyDeltaToCustomLineItemShippingDetailsTargets": helpers.absmod(
                    __name__,
                    ".CartApplyDeltaToCustomLineItemShippingDetailsTargetsActionSchema",
                ),
                "applyDeltaToLineItemShippingDetailsTargets": helpers.absmod(
                    __name__,
                    ".CartApplyDeltaToLineItemShippingDetailsTargetsActionSchema",
                ),
                "changeCustomLineItemMoney": helpers.absmod(
                    __name__, ".CartChangeCustomLineItemMoneyActionSchema"
                ),
                "changeCustomLineItemQuantity": helpers.absmod(
                    __name__, ".CartChangeCustomLineItemQuantityActionSchema"
                ),
                "changeLineItemQuantity": helpers.absmod(
                    __name__, ".CartChangeLineItemQuantityActionSchema"
                ),
                "changeTaxCalculationMode": helpers.absmod(
                    __name__, ".CartChangeTaxCalculationModeActionSchema"
                ),
                "changeTaxMode": helpers.absmod(
                    __name__, ".CartChangeTaxModeActionSchema"
                ),
                "changeTaxRoundingMode": helpers.absmod(
                    __name__, ".CartChangeTaxRoundingModeActionSchema"
                ),
                "recalculate": helpers.absmod(__name__, ".CartRecalculateActionSchema"),
                "removeCustomLineItem": helpers.absmod(
                    __name__, ".CartRemoveCustomLineItemActionSchema"
                ),
                "removeDiscountCode": helpers.absmod(
                    __name__, ".CartRemoveDiscountCodeActionSchema"
                ),
                "removeItemShippingAddress": helpers.absmod(
                    __name__, ".CartRemoveItemShippingAddressActionSchema"
                ),
                "removeLineItem": helpers.absmod(
                    __name__, ".CartRemoveLineItemActionSchema"
                ),
                "removePayment": helpers.absmod(
                    __name__, ".CartRemovePaymentActionSchema"
                ),
                "setAnonymousId": helpers.absmod(
                    __name__, ".CartSetAnonymousIdActionSchema"
                ),
                "setBillingAddress": helpers.absmod(
                    __name__, ".CartSetBillingAddressActionSchema"
                ),
                "setCartTotalTax": helpers.absmod(
                    __name__, ".CartSetCartTotalTaxActionSchema"
                ),
                "setCountry": helpers.absmod(__name__, ".CartSetCountryActionSchema"),
                "setCustomField": helpers.absmod(
                    __name__, ".CartSetCustomFieldActionSchema"
                ),
                "setCustomLineItemCustomField": helpers.absmod(
                    __name__, ".CartSetCustomLineItemCustomFieldActionSchema"
                ),
                "setCustomLineItemCustomType": helpers.absmod(
                    __name__, ".CartSetCustomLineItemCustomTypeActionSchema"
                ),
                "setCustomLineItemShippingDetails": helpers.absmod(
                    __name__, ".CartSetCustomLineItemShippingDetailsActionSchema"
                ),
                "setCustomLineItemTaxAmount": helpers.absmod(
                    __name__, ".CartSetCustomLineItemTaxAmountActionSchema"
                ),
                "setCustomLineItemTaxRate": helpers.absmod(
                    __name__, ".CartSetCustomLineItemTaxRateActionSchema"
                ),
                "setCustomShippingMethod": helpers.absmod(
                    __name__, ".CartSetCustomShippingMethodActionSchema"
                ),
                "setCustomType": helpers.absmod(
                    __name__, ".CartSetCustomTypeActionSchema"
                ),
                "setCustomerEmail": helpers.absmod(
                    __name__, ".CartSetCustomerEmailActionSchema"
                ),
                "setCustomerGroup": helpers.absmod(
                    __name__, ".CartSetCustomerGroupActionSchema"
                ),
                "setCustomerId": helpers.absmod(
                    __name__, ".CartSetCustomerIdActionSchema"
                ),
                "setDeleteDaysAfterLastModification": helpers.absmod(
                    __name__, ".CartSetDeleteDaysAfterLastModificationActionSchema"
                ),
                "setLineItemCustomField": helpers.absmod(
                    __name__, ".CartSetLineItemCustomFieldActionSchema"
                ),
                "setLineItemCustomType": helpers.absmod(
                    __name__, ".CartSetLineItemCustomTypeActionSchema"
                ),
                "setLineItemDistributionChannel": helpers.absmod(
                    __name__, ".CartSetLineItemDistributionChannelActionSchema"
                ),
                "setLineItemPrice": helpers.absmod(
                    __name__, ".CartSetLineItemPriceActionSchema"
                ),
                "setLineItemShippingDetails": helpers.absmod(
                    __name__, ".CartSetLineItemShippingDetailsActionSchema"
                ),
                "setLineItemTaxAmount": helpers.absmod(
                    __name__, ".CartSetLineItemTaxAmountActionSchema"
                ),
                "setLineItemTaxRate": helpers.absmod(
                    __name__, ".CartSetLineItemTaxRateActionSchema"
                ),
                "setLineItemTotalPrice": helpers.absmod(
                    __name__, ".CartSetLineItemTotalPriceActionSchema"
                ),
                "setLocale": helpers.absmod(__name__, ".CartSetLocaleActionSchema"),
                "setShippingAddress": helpers.absmod(
                    __name__, ".CartSetShippingAddressActionSchema"
                ),
                "setShippingMethod": helpers.absmod(
                    __name__, ".CartSetShippingMethodActionSchema"
                ),
                "setShippingMethodTaxAmount": helpers.absmod(
                    __name__, ".CartSetShippingMethodTaxAmountActionSchema"
                ),
                "setShippingMethodTaxRate": helpers.absmod(
                    __name__, ".CartSetShippingMethodTaxRateActionSchema"
                ),
                "setShippingRateInput": helpers.absmod(
                    __name__, ".CartSetShippingRateInputActionSchema"
                ),
                "updateItemShippingAddress": helpers.absmod(
                    __name__, ".CartUpdateItemShippingAddressActionSchema"
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

        return models.CartUpdate(**data)


class CartUpdateActionSchema(marshmallow.Schema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartUpdateAction(**data)


class CustomLineItemSchema(marshmallow.Schema):
    id = marshmallow.fields.String(allow_none=True, missing=None)
    name = LocalizedStringField(allow_none=True, missing=None)
    money = helpers.Discriminator(
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
    )
    taxed_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".TaxedItemPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="taxedPrice",
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
    slug = marshmallow.fields.String(allow_none=True, missing=None)
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.ItemStateSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    tax_category = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".tax_category.TaxCategoryReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="taxCategory",
    )
    tax_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".tax_category.TaxRateSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="taxRate",
    )
    discounted_price_per_quantity = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".DiscountedLineItemPriceForQuantitySchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="discountedPricePerQuantity",
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    shipping_details = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ItemShippingDetailsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="shippingDetails",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CustomLineItem(**data)


class CustomLineItemDraftSchema(marshmallow.Schema):
    name = LocalizedStringField(allow_none=True, missing=None)
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)
    money = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    slug = marshmallow.fields.String(allow_none=True, missing=None)
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
        nested=helpers.absmod(__name__, ".ExternalTaxRateDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="externalTaxRate",
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
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


class DiscountCodeInfoSchema(marshmallow.Schema):
    discount_code = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".discount_code.DiscountCodeReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="discountCode",
    )
    state = marshmallow_enum.EnumField(
        DiscountCodeState, by_value=True, allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.DiscountCodeInfo(**data)


class DiscountedLineItemPortionSchema(marshmallow.Schema):
    discount = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart_discount.CartDiscountReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    discounted_amount = helpers.Discriminator(
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
        data_key="discountedAmount",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.DiscountedLineItemPortion(**data)


class DiscountedLineItemPriceSchema(marshmallow.Schema):
    value = helpers.Discriminator(
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

        return models.DiscountedLineItemPrice(**data)


class DiscountedLineItemPriceForQuantitySchema(marshmallow.Schema):
    quantity = marshmallow.fields.Float(allow_none=True, missing=None)
    discounted_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".DiscountedLineItemPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="discountedPrice",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.DiscountedLineItemPriceForQuantity(**data)


class ExternalLineItemTotalPriceSchema(marshmallow.Schema):
    price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    total_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="totalPrice",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ExternalLineItemTotalPrice(**data)


class ExternalTaxAmountDraftSchema(marshmallow.Schema):
    total_gross = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="totalGross",
    )
    tax_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ExternalTaxRateDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="taxRate",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ExternalTaxAmountDraft(**data)


class ExternalTaxRateDraftSchema(marshmallow.Schema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    amount = marshmallow.fields.Float(allow_none=True, missing=None)
    country = marshmallow.fields.String(allow_none=True, missing=None)
    state = marshmallow.fields.String(allow_none=True, missing=None)
    sub_rates = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".tax_category.SubRateSchema"),
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


class ItemShippingDetailsSchema(marshmallow.Schema):
    targets = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ItemShippingTargetSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    valid = marshmallow.fields.Boolean(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ItemShippingDetails(**data)


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


class LineItemSchema(marshmallow.Schema):
    id = marshmallow.fields.String(allow_none=True, missing=None)
    product_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="productId"
    )
    name = LocalizedStringField(allow_none=True, missing=None)
    product_slug = LocalizedStringField(
        allow_none=True, missing=None, data_key="productSlug"
    )
    product_type = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".product_type.ProductTypeReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="productType",
    )
    variant = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".product.ProductVariantSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.PriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    taxed_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".TaxedItemPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="taxedPrice",
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
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)
    added_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="addedAt"
    )
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.ItemStateSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    tax_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".tax_category.TaxRateSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="taxRate",
    )
    supply_channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="supplyChannel",
    )
    distribution_channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="distributionChannel",
    )
    discounted_price_per_quantity = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".DiscountedLineItemPriceForQuantitySchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="discountedPricePerQuantity",
    )
    price_mode = marshmallow_enum.EnumField(
        LineItemPriceMode,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="priceMode",
    )
    line_item_mode = marshmallow_enum.EnumField(
        LineItemMode,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="lineItemMode",
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    shipping_details = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ItemShippingDetailsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="shippingDetails",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.LineItem(**data)


class LineItemDraftSchema(marshmallow.Schema):
    product_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="productId"
    )
    variant_id = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="variantId"
    )
    sku = marshmallow.fields.String(allow_none=True, missing=None)
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)
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
    external_tax_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ExternalTaxRateDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="externalTaxRate",
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    external_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="externalPrice",
    )
    external_total_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ExternalLineItemTotalPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="externalTotalPrice",
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

        return models.LineItemDraft(**data)


class ReplicaCartDraftSchema(marshmallow.Schema):
    reference = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ReplicaCartDraft(**data)


class ShippingInfoSchema(marshmallow.Schema):
    shipping_method_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="shippingMethodName"
    )
    price = helpers.Discriminator(
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
    )
    shipping_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".shipping_method.ShippingRateSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="shippingRate",
    )
    taxed_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".TaxedItemPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="taxedPrice",
    )
    tax_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".tax_category.TaxRateSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="taxRate",
    )
    tax_category = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".tax_category.TaxCategoryReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="taxCategory",
    )
    shipping_method = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".shipping_method.ShippingMethodReferenceSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="shippingMethod",
    )
    deliveries = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.DeliverySchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    discounted_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".DiscountedLineItemPriceSchema"),
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

        return models.ShippingInfo(**data)


class ShippingRateInputSchema(marshmallow.Schema):
    type = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ShippingRateInput(**data)


class ClassificationShippingRateInputSchema(ShippingRateInputSchema):
    key = marshmallow.fields.String(allow_none=True, missing=None)
    label = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ClassificationShippingRateInput(**data)


class ScoreShippingRateInputSchema(ShippingRateInputSchema):
    score = marshmallow.fields.Float(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ScoreShippingRateInput(**data)


class ShippingRateInputDraftSchema(marshmallow.Schema):
    type = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ShippingRateInputDraft(**data)


class ClassificationShippingRateInputDraftSchema(ShippingRateInputDraftSchema):
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ClassificationShippingRateInputDraft(**data)


class ScoreShippingRateInputDraftSchema(ShippingRateInputDraftSchema):
    score = marshmallow.fields.Float(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ScoreShippingRateInputDraft(**data)


class TaxPortionSchema(marshmallow.Schema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    rate = marshmallow.fields.Float(allow_none=True, missing=None)
    amount = helpers.Discriminator(
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
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.TaxPortion(**data)


class TaxPortionDraftSchema(marshmallow.Schema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    rate = marshmallow.fields.Float(allow_none=True, missing=None)
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

        return models.TaxPortionDraft(**data)


class TaxedItemPriceSchema(marshmallow.Schema):
    total_net = helpers.Discriminator(
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
        data_key="totalNet",
    )
    total_gross = helpers.Discriminator(
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
        data_key="totalGross",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.TaxedItemPrice(**data)


class TaxedPriceSchema(marshmallow.Schema):
    total_net = helpers.Discriminator(
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
        data_key="totalNet",
    )
    total_gross = helpers.Discriminator(
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


class TaxedPriceDraftSchema(marshmallow.Schema):
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
        nested=helpers.absmod(__name__, ".TaxPortionDraftSchema"),
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

        return models.TaxedPriceDraft(**data)


class CartAddCustomLineItemActionSchema(CartUpdateActionSchema):
    money = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    name = LocalizedStringField(allow_none=True, missing=None)
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)
    slug = marshmallow.fields.String(allow_none=True, missing=None)
    tax_category = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".tax_category.TaxCategoryResourceIdentifierSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="taxCategory",
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    external_tax_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ExternalTaxRateDraftSchema"),
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
        return models.CartAddCustomLineItemAction(**data)


class CartAddDiscountCodeActionSchema(CartUpdateActionSchema):
    code = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartAddDiscountCodeAction(**data)


class CartAddItemShippingAddressActionSchema(CartUpdateActionSchema):
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
        return models.CartAddItemShippingAddressAction(**data)


class CartAddLineItemActionSchema(CartUpdateActionSchema):
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
        nested=helpers.absmod(__name__, ".ExternalTaxRateDraftSchema"),
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
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)
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
        nested=helpers.absmod(__name__, ".ExternalLineItemTotalPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="externalTotalPrice",
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
        del data["action"]
        return models.CartAddLineItemAction(**data)


class CartAddPaymentActionSchema(CartUpdateActionSchema):
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
        return models.CartAddPaymentAction(**data)


class CartAddShoppingListActionSchema(CartUpdateActionSchema):
    shopping_list = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".shopping_list.ShoppingListResourceIdentifierSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="shoppingList",
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

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartAddShoppingListAction(**data)


class CartApplyDeltaToCustomLineItemShippingDetailsTargetsActionSchema(
    CartUpdateActionSchema
):
    custom_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customLineItemId"
    )
    targets_delta = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ItemShippingTargetSchema"),
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
        return models.CartApplyDeltaToCustomLineItemShippingDetailsTargetsAction(**data)


class CartApplyDeltaToLineItemShippingDetailsTargetsActionSchema(
    CartUpdateActionSchema
):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    targets_delta = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ItemShippingTargetSchema"),
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
        return models.CartApplyDeltaToLineItemShippingDetailsTargetsAction(**data)


class CartChangeCustomLineItemMoneyActionSchema(CartUpdateActionSchema):
    custom_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customLineItemId"
    )
    money = helpers.LazyNestedField(
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
        return models.CartChangeCustomLineItemMoneyAction(**data)


class CartChangeCustomLineItemQuantityActionSchema(CartUpdateActionSchema):
    custom_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customLineItemId"
    )
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartChangeCustomLineItemQuantityAction(**data)


class CartChangeLineItemQuantityActionSchema(CartUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)
    external_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="externalPrice",
    )
    external_total_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ExternalLineItemTotalPriceSchema"),
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
        return models.CartChangeLineItemQuantityAction(**data)


class CartChangeTaxCalculationModeActionSchema(CartUpdateActionSchema):
    tax_calculation_mode = marshmallow_enum.EnumField(
        TaxCalculationMode,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="taxCalculationMode",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartChangeTaxCalculationModeAction(**data)


class CartChangeTaxModeActionSchema(CartUpdateActionSchema):
    tax_mode = marshmallow_enum.EnumField(
        TaxMode, by_value=True, allow_none=True, missing=None, data_key="taxMode"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartChangeTaxModeAction(**data)


class CartChangeTaxRoundingModeActionSchema(CartUpdateActionSchema):
    tax_rounding_mode = marshmallow_enum.EnumField(
        RoundingMode,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="taxRoundingMode",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartChangeTaxRoundingModeAction(**data)


class CartRecalculateActionSchema(CartUpdateActionSchema):
    update_product_data = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="updateProductData"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartRecalculateAction(**data)


class CartRemoveCustomLineItemActionSchema(CartUpdateActionSchema):
    custom_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customLineItemId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartRemoveCustomLineItemAction(**data)


class CartRemoveDiscountCodeActionSchema(CartUpdateActionSchema):
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
        return models.CartRemoveDiscountCodeAction(**data)


class CartRemoveItemShippingAddressActionSchema(CartUpdateActionSchema):
    address_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartRemoveItemShippingAddressAction(**data)


class CartRemoveLineItemActionSchema(CartUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)
    external_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="externalPrice",
    )
    external_total_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ExternalLineItemTotalPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="externalTotalPrice",
    )
    shipping_details_to_remove = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ItemShippingDetailsDraftSchema"),
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
        return models.CartRemoveLineItemAction(**data)


class CartRemovePaymentActionSchema(CartUpdateActionSchema):
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
        return models.CartRemovePaymentAction(**data)


class CartSetAnonymousIdActionSchema(CartUpdateActionSchema):
    anonymous_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="anonymousId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartSetAnonymousIdAction(**data)


class CartSetBillingAddressActionSchema(CartUpdateActionSchema):
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
        return models.CartSetBillingAddressAction(**data)


class CartSetCartTotalTaxActionSchema(CartUpdateActionSchema):
    external_total_gross = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="externalTotalGross",
    )
    external_tax_portions = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".TaxPortionDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="externalTaxPortions",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartSetCartTotalTaxAction(**data)


class CartSetCountryActionSchema(CartUpdateActionSchema):
    country = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartSetCountryAction(**data)


class CartSetCustomFieldActionSchema(CartUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartSetCustomFieldAction(**data)


class CartSetCustomLineItemCustomFieldActionSchema(CartUpdateActionSchema):
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
        return models.CartSetCustomLineItemCustomFieldAction(**data)


class CartSetCustomLineItemCustomTypeActionSchema(CartUpdateActionSchema):
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
        return models.CartSetCustomLineItemCustomTypeAction(**data)


class CartSetCustomLineItemShippingDetailsActionSchema(CartUpdateActionSchema):
    custom_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customLineItemId"
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
        del data["action"]
        return models.CartSetCustomLineItemShippingDetailsAction(**data)


class CartSetCustomLineItemTaxAmountActionSchema(CartUpdateActionSchema):
    custom_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customLineItemId"
    )
    external_tax_amount = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ExternalTaxAmountDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="externalTaxAmount",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartSetCustomLineItemTaxAmountAction(**data)


class CartSetCustomLineItemTaxRateActionSchema(CartUpdateActionSchema):
    custom_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customLineItemId"
    )
    external_tax_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ExternalTaxRateDraftSchema"),
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
        return models.CartSetCustomLineItemTaxRateAction(**data)


class CartSetCustomShippingMethodActionSchema(CartUpdateActionSchema):
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
        nested=helpers.absmod(__name__, ".ExternalTaxRateDraftSchema"),
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
        return models.CartSetCustomShippingMethodAction(**data)


class CartSetCustomTypeActionSchema(CartUpdateActionSchema):
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
        return models.CartSetCustomTypeAction(**data)


class CartSetCustomerEmailActionSchema(CartUpdateActionSchema):
    email = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartSetCustomerEmailAction(**data)


class CartSetCustomerGroupActionSchema(CartUpdateActionSchema):
    customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".customer_group.CustomerGroupResourceIdentifierSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="customerGroup",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartSetCustomerGroupAction(**data)


class CartSetCustomerIdActionSchema(CartUpdateActionSchema):
    customer_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customerId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartSetCustomerIdAction(**data)


class CartSetDeleteDaysAfterLastModificationActionSchema(CartUpdateActionSchema):
    delete_days_after_last_modification = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="deleteDaysAfterLastModification"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartSetDeleteDaysAfterLastModificationAction(**data)


class CartSetLineItemCustomFieldActionSchema(CartUpdateActionSchema):
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
        return models.CartSetLineItemCustomFieldAction(**data)


class CartSetLineItemCustomTypeActionSchema(CartUpdateActionSchema):
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
        return models.CartSetLineItemCustomTypeAction(**data)


class CartSetLineItemDistributionChannelActionSchema(CartUpdateActionSchema):
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
        return models.CartSetLineItemDistributionChannelAction(**data)


class CartSetLineItemPriceActionSchema(CartUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    external_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="externalPrice",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartSetLineItemPriceAction(**data)


class CartSetLineItemShippingDetailsActionSchema(CartUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
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
        del data["action"]
        return models.CartSetLineItemShippingDetailsAction(**data)


class CartSetLineItemTaxAmountActionSchema(CartUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    external_tax_amount = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ExternalTaxAmountDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="externalTaxAmount",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartSetLineItemTaxAmountAction(**data)


class CartSetLineItemTaxRateActionSchema(CartUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    external_tax_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ExternalTaxRateDraftSchema"),
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
        return models.CartSetLineItemTaxRateAction(**data)


class CartSetLineItemTotalPriceActionSchema(CartUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    external_total_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ExternalLineItemTotalPriceSchema"),
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
        return models.CartSetLineItemTotalPriceAction(**data)


class CartSetLocaleActionSchema(CartUpdateActionSchema):
    locale = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartSetLocaleAction(**data)


class CartSetShippingAddressActionSchema(CartUpdateActionSchema):
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
        return models.CartSetShippingAddressAction(**data)


class CartSetShippingMethodActionSchema(CartUpdateActionSchema):
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
        nested=helpers.absmod(__name__, ".ExternalTaxRateDraftSchema"),
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
        return models.CartSetShippingMethodAction(**data)


class CartSetShippingMethodTaxAmountActionSchema(CartUpdateActionSchema):
    external_tax_amount = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ExternalTaxAmountDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="externalTaxAmount",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartSetShippingMethodTaxAmountAction(**data)


class CartSetShippingMethodTaxRateActionSchema(CartUpdateActionSchema):
    external_tax_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ExternalTaxRateDraftSchema"),
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
        return models.CartSetShippingMethodTaxRateAction(**data)


class CartSetShippingRateInputActionSchema(CartUpdateActionSchema):
    shipping_rate_input = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "Classification": helpers.absmod(
                __name__, ".ClassificationShippingRateInputDraftSchema"
            ),
            "Score": helpers.absmod(__name__, ".ScoreShippingRateInputDraftSchema"),
        },
        missing=None,
        data_key="shippingRateInput",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartSetShippingRateInputAction(**data)


class CartUpdateItemShippingAddressActionSchema(CartUpdateActionSchema):
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
        return models.CartUpdateItemShippingAddressAction(**data)
