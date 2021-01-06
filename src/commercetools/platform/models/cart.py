# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import BaseResource, Reference, ReferenceTypeId, ResourceIdentifier

if typing.TYPE_CHECKING:
    from .cart_discount import CartDiscountReference
    from .channel import ChannelReference, ChannelResourceIdentifier
    from .common import (
        Address,
        CreatedBy,
        LastModifiedBy,
        LocalizedString,
        Money,
        Price,
        ReferenceTypeId,
        TypedMoney,
    )
    from .customer_group import CustomerGroupReference, CustomerGroupResourceIdentifier
    from .discount_code import DiscountCodeReference
    from .order import Delivery, ItemState, OrderReference, PaymentInfo
    from .payment import PaymentResourceIdentifier
    from .product import ProductVariant
    from .product_type import ProductTypeReference
    from .shipping_method import (
        ShippingMethodReference,
        ShippingMethodResourceIdentifier,
        ShippingRate,
        ShippingRateDraft,
    )
    from .shopping_list import ShoppingListResourceIdentifier
    from .store import StoreKeyReference, StoreResourceIdentifier
    from .tax_category import (
        SubRate,
        TaxCategoryReference,
        TaxCategoryResourceIdentifier,
        TaxRate,
    )
    from .type import (
        CustomFields,
        CustomFieldsDraft,
        FieldContainer,
        TypeResourceIdentifier,
    )

__all__ = [
    "Cart",
    "CartAddCustomLineItemAction",
    "CartAddDiscountCodeAction",
    "CartAddItemShippingAddressAction",
    "CartAddLineItemAction",
    "CartAddPaymentAction",
    "CartAddShoppingListAction",
    "CartApplyDeltaToCustomLineItemShippingDetailsTargetsAction",
    "CartApplyDeltaToLineItemShippingDetailsTargetsAction",
    "CartChangeCustomLineItemMoneyAction",
    "CartChangeCustomLineItemQuantityAction",
    "CartChangeLineItemQuantityAction",
    "CartChangeTaxCalculationModeAction",
    "CartChangeTaxModeAction",
    "CartChangeTaxRoundingModeAction",
    "CartDraft",
    "CartOrigin",
    "CartPagedQueryResponse",
    "CartRecalculateAction",
    "CartReference",
    "CartRemoveCustomLineItemAction",
    "CartRemoveDiscountCodeAction",
    "CartRemoveItemShippingAddressAction",
    "CartRemoveLineItemAction",
    "CartRemovePaymentAction",
    "CartResourceIdentifier",
    "CartSetAnonymousIdAction",
    "CartSetBillingAddressAction",
    "CartSetCartTotalTaxAction",
    "CartSetCountryAction",
    "CartSetCustomFieldAction",
    "CartSetCustomLineItemCustomFieldAction",
    "CartSetCustomLineItemCustomTypeAction",
    "CartSetCustomLineItemShippingDetailsAction",
    "CartSetCustomLineItemTaxAmountAction",
    "CartSetCustomLineItemTaxRateAction",
    "CartSetCustomShippingMethodAction",
    "CartSetCustomTypeAction",
    "CartSetCustomerEmailAction",
    "CartSetCustomerGroupAction",
    "CartSetCustomerIdAction",
    "CartSetDeleteDaysAfterLastModificationAction",
    "CartSetLineItemCustomFieldAction",
    "CartSetLineItemCustomTypeAction",
    "CartSetLineItemDistributionChannelAction",
    "CartSetLineItemPriceAction",
    "CartSetLineItemShippingDetailsAction",
    "CartSetLineItemTaxAmountAction",
    "CartSetLineItemTaxRateAction",
    "CartSetLineItemTotalPriceAction",
    "CartSetLocaleAction",
    "CartSetShippingAddressAction",
    "CartSetShippingMethodAction",
    "CartSetShippingMethodTaxAmountAction",
    "CartSetShippingMethodTaxRateAction",
    "CartSetShippingRateInputAction",
    "CartState",
    "CartUpdate",
    "CartUpdateAction",
    "CartUpdateItemShippingAddressAction",
    "ClassificationShippingRateInput",
    "ClassificationShippingRateInputDraft",
    "CustomLineItem",
    "CustomLineItemDraft",
    "DiscountCodeInfo",
    "DiscountCodeState",
    "DiscountedLineItemPortion",
    "DiscountedLineItemPrice",
    "DiscountedLineItemPriceForQuantity",
    "ExternalLineItemTotalPrice",
    "ExternalTaxAmountDraft",
    "ExternalTaxRateDraft",
    "InventoryMode",
    "ItemShippingDetails",
    "ItemShippingDetailsDraft",
    "ItemShippingTarget",
    "LineItem",
    "LineItemDraft",
    "LineItemMode",
    "LineItemPriceMode",
    "ProductPublishScope",
    "ReplicaCartDraft",
    "RoundingMode",
    "ScoreShippingRateInput",
    "ScoreShippingRateInputDraft",
    "ShippingInfo",
    "ShippingMethodState",
    "ShippingRateInput",
    "ShippingRateInputDraft",
    "TaxCalculationMode",
    "TaxMode",
    "TaxPortion",
    "TaxPortionDraft",
    "TaxedItemPrice",
    "TaxedPrice",
    "TaxedPriceDraft",
]


class Cart(BaseResource):
    #: Present on resources updated after 1/02/2019 except for events not tracked.
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Present on resources created after 1/02/2019 except for events not tracked.
    created_by: typing.Optional["CreatedBy"]
    customer_id: typing.Optional[str]
    customer_email: typing.Optional[str]
    #: Identifies carts and orders belonging to an anonymous session (the customer has not signed up/in yet).
    anonymous_id: typing.Optional[str]
    store: typing.Optional["StoreKeyReference"]
    line_items: typing.List["LineItem"]
    custom_line_items: typing.List["CustomLineItem"]
    #: The sum of all `totalPrice` fields of the `lineItems` and `customLineItems`, as well as the `price` field of `shippingInfo` (if it exists).
    #: `totalPrice` may or may not include the taxes: it depends on the taxRate.includedInPrice property of each price.
    total_price: "TypedMoney"
    #: Not set until the shipping address is set.
    #: Will be set automatically in the `Platform` TaxMode.
    #: For the `External` tax mode it will be set  as soon as the external tax rates for all line items, custom line items, and shipping in the cart are set.
    taxed_price: typing.Optional["TaxedPrice"]
    cart_state: "CartState"
    #: The shipping address is used to determine the eligible shipping methods and rates as well as the tax rate of the line items.
    shipping_address: typing.Optional["Address"]
    billing_address: typing.Optional["Address"]
    inventory_mode: typing.Optional["InventoryMode"]
    tax_mode: "TaxMode"
    #: When calculating taxes for `taxedPrice`, the selected mode is used for rounding.
    tax_rounding_mode: "RoundingMode"
    #: When calculating taxes for `taxedPrice`, the selected mode is used for calculating the price with `LineItemLevel` (horizontally) or `UnitPriceLevel` (vertically) calculation mode.
    tax_calculation_mode: "TaxCalculationMode"
    #: Set automatically when the customer is set and the customer is a member of a customer group.
    #: Used for product variant
    #: price selection.
    customer_group: typing.Optional["CustomerGroupReference"]
    #: A two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    #: Used for product variant price selection.
    country: typing.Optional[str]
    #: Set automatically once the ShippingMethod is set.
    shipping_info: typing.Optional["ShippingInfo"]
    discount_codes: typing.Optional[typing.List["DiscountCodeInfo"]]
    custom: typing.Optional["CustomFields"]
    payment_info: typing.Optional["PaymentInfo"]
    locale: typing.Optional[str]
    #: The cart will be deleted automatically if it hasn't been modified for the specified amount of days and it is in the `Active` CartState.
    delete_days_after_last_modification: typing.Optional[int]
    #: Automatically filled when a line item with LineItemMode `GiftLineItem` is removed from the cart.
    refused_gifts: typing.List["CartDiscountReference"]
    #: The origin field indicates how this cart was created.
    #: The value `Customer` indicates, that the cart was created by the customer.
    origin: "CartOrigin"
    #: The shippingRateInput is used as an input to select a ShippingRatePriceTier.
    shipping_rate_input: typing.Optional["ShippingRateInput"]
    #: Contains addresses for carts with multiple shipping addresses.
    #: Line items reference these addresses under their `shippingDetails`.
    #: The addresses captured here are not used to determine eligible shipping methods or the applicable tax rate.
    #: Only the cart's `shippingAddress` is used for this.
    item_shipping_addresses: typing.Optional[typing.List["Address"]]

    def __init__(
        self,
        *,
        id: str,
        version: int,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        customer_id: typing.Optional[str] = None,
        customer_email: typing.Optional[str] = None,
        anonymous_id: typing.Optional[str] = None,
        store: typing.Optional["StoreKeyReference"] = None,
        line_items: typing.List["LineItem"],
        custom_line_items: typing.List["CustomLineItem"],
        total_price: "TypedMoney",
        taxed_price: typing.Optional["TaxedPrice"] = None,
        cart_state: "CartState",
        shipping_address: typing.Optional["Address"] = None,
        billing_address: typing.Optional["Address"] = None,
        inventory_mode: typing.Optional["InventoryMode"] = None,
        tax_mode: "TaxMode",
        tax_rounding_mode: "RoundingMode",
        tax_calculation_mode: "TaxCalculationMode",
        customer_group: typing.Optional["CustomerGroupReference"] = None,
        country: typing.Optional[str] = None,
        shipping_info: typing.Optional["ShippingInfo"] = None,
        discount_codes: typing.Optional[typing.List["DiscountCodeInfo"]] = None,
        custom: typing.Optional["CustomFields"] = None,
        payment_info: typing.Optional["PaymentInfo"] = None,
        locale: typing.Optional[str] = None,
        delete_days_after_last_modification: typing.Optional[int] = None,
        refused_gifts: typing.List["CartDiscountReference"],
        origin: "CartOrigin",
        shipping_rate_input: typing.Optional["ShippingRateInput"] = None,
        item_shipping_addresses: typing.Optional[typing.List["Address"]] = None
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.customer_id = customer_id
        self.customer_email = customer_email
        self.anonymous_id = anonymous_id
        self.store = store
        self.line_items = line_items
        self.custom_line_items = custom_line_items
        self.total_price = total_price
        self.taxed_price = taxed_price
        self.cart_state = cart_state
        self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.inventory_mode = inventory_mode
        self.tax_mode = tax_mode
        self.tax_rounding_mode = tax_rounding_mode
        self.tax_calculation_mode = tax_calculation_mode
        self.customer_group = customer_group
        self.country = country
        self.shipping_info = shipping_info
        self.discount_codes = discount_codes
        self.custom = custom
        self.payment_info = payment_info
        self.locale = locale
        self.delete_days_after_last_modification = delete_days_after_last_modification
        self.refused_gifts = refused_gifts
        self.origin = origin
        self.shipping_rate_input = shipping_rate_input
        self.item_shipping_addresses = item_shipping_addresses
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Cart":
        from ._schemas.cart import CartSchema

        return CartSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSchema

        return CartSchema().dump(self)


class CartDraft(_BaseType):
    #: A three-digit currency code as per [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).
    currency: str
    #: Id of an existing Customer.
    customer_id: typing.Optional[str]
    customer_email: typing.Optional[str]
    #: Will be set automatically when the `customerId` is set and the customer is a member of a customer group.
    #: Can be set explicitly when no `customerId` is present.
    customer_group: typing.Optional["CustomerGroupResourceIdentifier"]
    #: Assigns the new cart to an anonymous session (the customer has not signed up/in yet).
    anonymous_id: typing.Optional[str]
    #: Assigns the new cart to the store.
    #: The store assignment can not be modified.
    store: typing.Optional["StoreResourceIdentifier"]
    #: A two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    country: typing.Optional[str]
    #: Default inventory mode is `None`.
    inventory_mode: typing.Optional["InventoryMode"]
    #: The default tax mode is `Platform`.
    tax_mode: typing.Optional["TaxMode"]
    #: The default tax rounding mode is `HalfEven`.
    tax_rounding_mode: typing.Optional["RoundingMode"]
    #: The default tax calculation mode is `LineItemLevel`.
    tax_calculation_mode: typing.Optional["TaxCalculationMode"]
    line_items: typing.Optional[typing.List["LineItemDraft"]]
    custom_line_items: typing.Optional[typing.List["CustomLineItemDraft"]]
    #: The shipping address is used to determine the eligible shipping methods and rates as well as the tax rate of the line items.
    shipping_address: typing.Optional["Address"]
    billing_address: typing.Optional["Address"]
    shipping_method: typing.Optional["ShippingMethodResourceIdentifier"]
    #: An external tax rate can be set for the `shippingMethod` if the cart has the `External` TaxMode.
    external_tax_rate_for_shipping_method: typing.Optional["ExternalTaxRateDraft"]
    #: The custom fields.
    custom: typing.Optional["CustomFieldsDraft"]
    #: Must be one of the languages supported for this project
    locale: typing.Optional[str]
    #: The cart will be deleted automatically if it hasn't been modified for the specified amount of days and it is in the `Active` CartState.
    #: If a ChangeSubscription for carts exists, a `ResourceDeleted` notification will be sent.
    delete_days_after_last_modification: typing.Optional[int]
    #: The default origin is `Customer`.
    origin: typing.Optional["CartOrigin"]
    #: The shippingRateInput is used as an input to select a ShippingRatePriceTier.
    #: Based on the definition of ShippingRateInputType.
    #: If CartClassification is defined, it must be ClassificationShippingRateInput.
    #: If CartScore is defined, it must be ScoreShippingRateInput.
    #: Otherwise it can not bet set.
    shipping_rate_input: typing.Optional["ShippingRateInputDraft"]
    #: Contains addresses for carts with multiple shipping addresses.
    #: Each address must contain a key which is unique in this cart.
    #: Line items will use these keys to reference the addresses under their `shippingDetails`.
    #: The addresses captured here are not used to determine eligible shipping methods or the applicable tax rate.
    #: Only the cart's `shippingAddress` is used for this.
    item_shipping_addresses: typing.Optional[typing.List["Address"]]
    #: The code of existing DiscountCodes.
    discount_codes: typing.Optional[typing.List["str"]]

    def __init__(
        self,
        *,
        currency: str,
        customer_id: typing.Optional[str] = None,
        customer_email: typing.Optional[str] = None,
        customer_group: typing.Optional["CustomerGroupResourceIdentifier"] = None,
        anonymous_id: typing.Optional[str] = None,
        store: typing.Optional["StoreResourceIdentifier"] = None,
        country: typing.Optional[str] = None,
        inventory_mode: typing.Optional["InventoryMode"] = None,
        tax_mode: typing.Optional["TaxMode"] = None,
        tax_rounding_mode: typing.Optional["RoundingMode"] = None,
        tax_calculation_mode: typing.Optional["TaxCalculationMode"] = None,
        line_items: typing.Optional[typing.List["LineItemDraft"]] = None,
        custom_line_items: typing.Optional[typing.List["CustomLineItemDraft"]] = None,
        shipping_address: typing.Optional["Address"] = None,
        billing_address: typing.Optional["Address"] = None,
        shipping_method: typing.Optional["ShippingMethodResourceIdentifier"] = None,
        external_tax_rate_for_shipping_method: typing.Optional[
            "ExternalTaxRateDraft"
        ] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        locale: typing.Optional[str] = None,
        delete_days_after_last_modification: typing.Optional[int] = None,
        origin: typing.Optional["CartOrigin"] = None,
        shipping_rate_input: typing.Optional["ShippingRateInputDraft"] = None,
        item_shipping_addresses: typing.Optional[typing.List["Address"]] = None,
        discount_codes: typing.Optional[typing.List["str"]] = None
    ):
        self.currency = currency
        self.customer_id = customer_id
        self.customer_email = customer_email
        self.customer_group = customer_group
        self.anonymous_id = anonymous_id
        self.store = store
        self.country = country
        self.inventory_mode = inventory_mode
        self.tax_mode = tax_mode
        self.tax_rounding_mode = tax_rounding_mode
        self.tax_calculation_mode = tax_calculation_mode
        self.line_items = line_items
        self.custom_line_items = custom_line_items
        self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.shipping_method = shipping_method
        self.external_tax_rate_for_shipping_method = (
            external_tax_rate_for_shipping_method
        )
        self.custom = custom
        self.locale = locale
        self.delete_days_after_last_modification = delete_days_after_last_modification
        self.origin = origin
        self.shipping_rate_input = shipping_rate_input
        self.item_shipping_addresses = item_shipping_addresses
        self.discount_codes = discount_codes
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CartDraft":
        from ._schemas.cart import CartDraftSchema

        return CartDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartDraftSchema

        return CartDraftSchema().dump(self)


class CartOrigin(enum.Enum):
    CUSTOMER = "Customer"
    MERCHANT = "Merchant"


class CartPagedQueryResponse(_BaseType):
    limit: int
    count: int
    total: typing.Optional[int]
    offset: int
    results: typing.List["Cart"]

    def __init__(
        self,
        *,
        limit: int,
        count: int,
        total: typing.Optional[int] = None,
        offset: int,
        results: typing.List["Cart"]
    ):
        self.limit = limit
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartPagedQueryResponse":
        from ._schemas.cart import CartPagedQueryResponseSchema

        return CartPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartPagedQueryResponseSchema

        return CartPagedQueryResponseSchema().dump(self)


class CartReference(Reference):
    obj: typing.Optional["Cart"]

    def __init__(self, *, id: str, obj: typing.Optional["Cart"] = None):
        self.obj = obj
        super().__init__(id=id, type_id=ReferenceTypeId.CART)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CartReference":
        from ._schemas.cart import CartReferenceSchema

        return CartReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartReferenceSchema

        return CartReferenceSchema().dump(self)


class CartResourceIdentifier(ResourceIdentifier):
    def __init__(
        self, *, id: typing.Optional[str] = None, key: typing.Optional[str] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.CART)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartResourceIdentifier":
        from ._schemas.cart import CartResourceIdentifierSchema

        return CartResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartResourceIdentifierSchema

        return CartResourceIdentifierSchema().dump(self)


class CartState(enum.Enum):
    ACTIVE = "Active"
    MERGED = "Merged"
    ORDERED = "Ordered"


class CartUpdate(_BaseType):
    version: int
    actions: typing.List["CartUpdateAction"]

    def __init__(self, *, version: int, actions: typing.List["CartUpdateAction"]):
        self.version = version
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CartUpdate":
        from ._schemas.cart import CartUpdateSchema

        return CartUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartUpdateSchema

        return CartUpdateSchema().dump(self)


class CartUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CartUpdateAction":
        if data["action"] == "addCustomLineItem":
            from ._schemas.cart import CartAddCustomLineItemActionSchema

            return CartAddCustomLineItemActionSchema().load(data)
        if data["action"] == "addDiscountCode":
            from ._schemas.cart import CartAddDiscountCodeActionSchema

            return CartAddDiscountCodeActionSchema().load(data)
        if data["action"] == "addItemShippingAddress":
            from ._schemas.cart import CartAddItemShippingAddressActionSchema

            return CartAddItemShippingAddressActionSchema().load(data)
        if data["action"] == "addLineItem":
            from ._schemas.cart import CartAddLineItemActionSchema

            return CartAddLineItemActionSchema().load(data)
        if data["action"] == "addPayment":
            from ._schemas.cart import CartAddPaymentActionSchema

            return CartAddPaymentActionSchema().load(data)
        if data["action"] == "addShoppingList":
            from ._schemas.cart import CartAddShoppingListActionSchema

            return CartAddShoppingListActionSchema().load(data)
        if data["action"] == "applyDeltaToCustomLineItemShippingDetailsTargets":
            from ._schemas.cart import (
                CartApplyDeltaToCustomLineItemShippingDetailsTargetsActionSchema,
            )

            return (
                CartApplyDeltaToCustomLineItemShippingDetailsTargetsActionSchema().load(
                    data
                )
            )
        if data["action"] == "applyDeltaToLineItemShippingDetailsTargets":
            from ._schemas.cart import (
                CartApplyDeltaToLineItemShippingDetailsTargetsActionSchema,
            )

            return CartApplyDeltaToLineItemShippingDetailsTargetsActionSchema().load(
                data
            )
        if data["action"] == "changeCustomLineItemMoney":
            from ._schemas.cart import CartChangeCustomLineItemMoneyActionSchema

            return CartChangeCustomLineItemMoneyActionSchema().load(data)
        if data["action"] == "changeCustomLineItemQuantity":
            from ._schemas.cart import CartChangeCustomLineItemQuantityActionSchema

            return CartChangeCustomLineItemQuantityActionSchema().load(data)
        if data["action"] == "changeLineItemQuantity":
            from ._schemas.cart import CartChangeLineItemQuantityActionSchema

            return CartChangeLineItemQuantityActionSchema().load(data)
        if data["action"] == "changeTaxCalculationMode":
            from ._schemas.cart import CartChangeTaxCalculationModeActionSchema

            return CartChangeTaxCalculationModeActionSchema().load(data)
        if data["action"] == "changeTaxMode":
            from ._schemas.cart import CartChangeTaxModeActionSchema

            return CartChangeTaxModeActionSchema().load(data)
        if data["action"] == "changeTaxRoundingMode":
            from ._schemas.cart import CartChangeTaxRoundingModeActionSchema

            return CartChangeTaxRoundingModeActionSchema().load(data)
        if data["action"] == "recalculate":
            from ._schemas.cart import CartRecalculateActionSchema

            return CartRecalculateActionSchema().load(data)
        if data["action"] == "removeCustomLineItem":
            from ._schemas.cart import CartRemoveCustomLineItemActionSchema

            return CartRemoveCustomLineItemActionSchema().load(data)
        if data["action"] == "removeDiscountCode":
            from ._schemas.cart import CartRemoveDiscountCodeActionSchema

            return CartRemoveDiscountCodeActionSchema().load(data)
        if data["action"] == "removeItemShippingAddress":
            from ._schemas.cart import CartRemoveItemShippingAddressActionSchema

            return CartRemoveItemShippingAddressActionSchema().load(data)
        if data["action"] == "removeLineItem":
            from ._schemas.cart import CartRemoveLineItemActionSchema

            return CartRemoveLineItemActionSchema().load(data)
        if data["action"] == "removePayment":
            from ._schemas.cart import CartRemovePaymentActionSchema

            return CartRemovePaymentActionSchema().load(data)
        if data["action"] == "setAnonymousId":
            from ._schemas.cart import CartSetAnonymousIdActionSchema

            return CartSetAnonymousIdActionSchema().load(data)
        if data["action"] == "setBillingAddress":
            from ._schemas.cart import CartSetBillingAddressActionSchema

            return CartSetBillingAddressActionSchema().load(data)
        if data["action"] == "setCartTotalTax":
            from ._schemas.cart import CartSetCartTotalTaxActionSchema

            return CartSetCartTotalTaxActionSchema().load(data)
        if data["action"] == "setCountry":
            from ._schemas.cart import CartSetCountryActionSchema

            return CartSetCountryActionSchema().load(data)
        if data["action"] == "setCustomField":
            from ._schemas.cart import CartSetCustomFieldActionSchema

            return CartSetCustomFieldActionSchema().load(data)
        if data["action"] == "setCustomLineItemCustomField":
            from ._schemas.cart import CartSetCustomLineItemCustomFieldActionSchema

            return CartSetCustomLineItemCustomFieldActionSchema().load(data)
        if data["action"] == "setCustomLineItemCustomType":
            from ._schemas.cart import CartSetCustomLineItemCustomTypeActionSchema

            return CartSetCustomLineItemCustomTypeActionSchema().load(data)
        if data["action"] == "setCustomLineItemShippingDetails":
            from ._schemas.cart import CartSetCustomLineItemShippingDetailsActionSchema

            return CartSetCustomLineItemShippingDetailsActionSchema().load(data)
        if data["action"] == "setCustomLineItemTaxAmount":
            from ._schemas.cart import CartSetCustomLineItemTaxAmountActionSchema

            return CartSetCustomLineItemTaxAmountActionSchema().load(data)
        if data["action"] == "setCustomLineItemTaxRate":
            from ._schemas.cart import CartSetCustomLineItemTaxRateActionSchema

            return CartSetCustomLineItemTaxRateActionSchema().load(data)
        if data["action"] == "setCustomShippingMethod":
            from ._schemas.cart import CartSetCustomShippingMethodActionSchema

            return CartSetCustomShippingMethodActionSchema().load(data)
        if data["action"] == "setCustomType":
            from ._schemas.cart import CartSetCustomTypeActionSchema

            return CartSetCustomTypeActionSchema().load(data)
        if data["action"] == "setCustomerEmail":
            from ._schemas.cart import CartSetCustomerEmailActionSchema

            return CartSetCustomerEmailActionSchema().load(data)
        if data["action"] == "setCustomerGroup":
            from ._schemas.cart import CartSetCustomerGroupActionSchema

            return CartSetCustomerGroupActionSchema().load(data)
        if data["action"] == "setCustomerId":
            from ._schemas.cart import CartSetCustomerIdActionSchema

            return CartSetCustomerIdActionSchema().load(data)
        if data["action"] == "setDeleteDaysAfterLastModification":
            from ._schemas.cart import (
                CartSetDeleteDaysAfterLastModificationActionSchema,
            )

            return CartSetDeleteDaysAfterLastModificationActionSchema().load(data)
        if data["action"] == "setLineItemCustomField":
            from ._schemas.cart import CartSetLineItemCustomFieldActionSchema

            return CartSetLineItemCustomFieldActionSchema().load(data)
        if data["action"] == "setLineItemCustomType":
            from ._schemas.cart import CartSetLineItemCustomTypeActionSchema

            return CartSetLineItemCustomTypeActionSchema().load(data)
        if data["action"] == "setLineItemDistributionChannel":
            from ._schemas.cart import CartSetLineItemDistributionChannelActionSchema

            return CartSetLineItemDistributionChannelActionSchema().load(data)
        if data["action"] == "setLineItemPrice":
            from ._schemas.cart import CartSetLineItemPriceActionSchema

            return CartSetLineItemPriceActionSchema().load(data)
        if data["action"] == "setLineItemShippingDetails":
            from ._schemas.cart import CartSetLineItemShippingDetailsActionSchema

            return CartSetLineItemShippingDetailsActionSchema().load(data)
        if data["action"] == "setLineItemTaxAmount":
            from ._schemas.cart import CartSetLineItemTaxAmountActionSchema

            return CartSetLineItemTaxAmountActionSchema().load(data)
        if data["action"] == "setLineItemTaxRate":
            from ._schemas.cart import CartSetLineItemTaxRateActionSchema

            return CartSetLineItemTaxRateActionSchema().load(data)
        if data["action"] == "setLineItemTotalPrice":
            from ._schemas.cart import CartSetLineItemTotalPriceActionSchema

            return CartSetLineItemTotalPriceActionSchema().load(data)
        if data["action"] == "setLocale":
            from ._schemas.cart import CartSetLocaleActionSchema

            return CartSetLocaleActionSchema().load(data)
        if data["action"] == "setShippingAddress":
            from ._schemas.cart import CartSetShippingAddressActionSchema

            return CartSetShippingAddressActionSchema().load(data)
        if data["action"] == "setShippingMethod":
            from ._schemas.cart import CartSetShippingMethodActionSchema

            return CartSetShippingMethodActionSchema().load(data)
        if data["action"] == "setShippingMethodTaxAmount":
            from ._schemas.cart import CartSetShippingMethodTaxAmountActionSchema

            return CartSetShippingMethodTaxAmountActionSchema().load(data)
        if data["action"] == "setShippingMethodTaxRate":
            from ._schemas.cart import CartSetShippingMethodTaxRateActionSchema

            return CartSetShippingMethodTaxRateActionSchema().load(data)
        if data["action"] == "setShippingRateInput":
            from ._schemas.cart import CartSetShippingRateInputActionSchema

            return CartSetShippingRateInputActionSchema().load(data)
        if data["action"] == "updateItemShippingAddress":
            from ._schemas.cart import CartUpdateItemShippingAddressActionSchema

            return CartUpdateItemShippingAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartUpdateActionSchema

        return CartUpdateActionSchema().dump(self)


class CustomLineItem(_BaseType):
    #: The unique ID of this CustomLineItem.
    id: str
    #: The name of this CustomLineItem.
    name: "LocalizedString"
    #: The cost to add to the cart.
    #: The amount can be negative.
    money: "TypedMoney"
    #: Set once the `taxRate` is set.
    taxed_price: typing.Optional["TaxedItemPrice"]
    #: The total price of this custom line item.
    #: If custom line item is discounted, then the `totalPrice` would be the discounted custom line item price multiplied by `quantity`.
    #: Otherwise a total price is just a `money` multiplied by the `quantity`.
    #: `totalPrice` may or may not include the taxes: it depends on the taxRate.includedInPrice property.
    total_price: "TypedMoney"
    #: A unique String in the cart to identify this CustomLineItem.
    slug: str
    #: The amount of a CustomLineItem in the cart.
    #: Must be a positive integer.
    quantity: int
    state: typing.List["ItemState"]
    tax_category: typing.Optional["TaxCategoryReference"]
    #: Will be set automatically in the `Platform` TaxMode once the shipping address is set is set.
    #: For the `External` tax mode the tax rate has to be set explicitly with the ExternalTaxRateDraft.
    tax_rate: typing.Optional["TaxRate"]
    discounted_price_per_quantity: typing.List["DiscountedLineItemPriceForQuantity"]
    custom: typing.Optional["CustomFields"]
    #: Container for custom line item specific address(es).
    #: CustomLineItem fields that can be used in query predicates: `slug`, `name`, `quantity`,
    #: `money`, `state`, `discountedPricePerQuantity`.
    shipping_details: typing.Optional["ItemShippingDetails"]

    def __init__(
        self,
        *,
        id: str,
        name: "LocalizedString",
        money: "TypedMoney",
        taxed_price: typing.Optional["TaxedItemPrice"] = None,
        total_price: "TypedMoney",
        slug: str,
        quantity: int,
        state: typing.List["ItemState"],
        tax_category: typing.Optional["TaxCategoryReference"] = None,
        tax_rate: typing.Optional["TaxRate"] = None,
        discounted_price_per_quantity: typing.List[
            "DiscountedLineItemPriceForQuantity"
        ],
        custom: typing.Optional["CustomFields"] = None,
        shipping_details: typing.Optional["ItemShippingDetails"] = None
    ):
        self.id = id
        self.name = name
        self.money = money
        self.taxed_price = taxed_price
        self.total_price = total_price
        self.slug = slug
        self.quantity = quantity
        self.state = state
        self.tax_category = tax_category
        self.tax_rate = tax_rate
        self.discounted_price_per_quantity = discounted_price_per_quantity
        self.custom = custom
        self.shipping_details = shipping_details
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomLineItem":
        from ._schemas.cart import CustomLineItemSchema

        return CustomLineItemSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CustomLineItemSchema

        return CustomLineItemSchema().dump(self)


class CustomLineItemDraft(_BaseType):
    name: "LocalizedString"
    #: The amount of a CustomLineItemin the cart.
    #: Must be a positive integer.
    quantity: int
    money: "Money"
    slug: str
    #: The given tax category will be used to select a tax rate when a cart has the TaxMode `Platform`.
    tax_category: typing.Optional["TaxCategoryResourceIdentifier"]
    #: An external tax rate can be set if the cart has the `External` TaxMode.
    external_tax_rate: typing.Optional["ExternalTaxRateDraft"]
    #: The custom fields.
    custom: typing.Optional["CustomFieldsDraft"]
    #: Container for custom line item specific address(es).
    shipping_details: typing.Optional["ItemShippingDetailsDraft"]

    def __init__(
        self,
        *,
        name: "LocalizedString",
        quantity: int,
        money: "Money",
        slug: str,
        tax_category: typing.Optional["TaxCategoryResourceIdentifier"] = None,
        external_tax_rate: typing.Optional["ExternalTaxRateDraft"] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        shipping_details: typing.Optional["ItemShippingDetailsDraft"] = None
    ):
        self.name = name
        self.quantity = quantity
        self.money = money
        self.slug = slug
        self.tax_category = tax_category
        self.external_tax_rate = external_tax_rate
        self.custom = custom
        self.shipping_details = shipping_details
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomLineItemDraft":
        from ._schemas.cart import CustomLineItemDraftSchema

        return CustomLineItemDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CustomLineItemDraftSchema

        return CustomLineItemDraftSchema().dump(self)


class DiscountCodeInfo(_BaseType):
    discount_code: "DiscountCodeReference"
    state: "DiscountCodeState"

    def __init__(
        self, *, discount_code: "DiscountCodeReference", state: "DiscountCodeState"
    ):
        self.discount_code = discount_code
        self.state = state
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "DiscountCodeInfo":
        from ._schemas.cart import DiscountCodeInfoSchema

        return DiscountCodeInfoSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import DiscountCodeInfoSchema

        return DiscountCodeInfoSchema().dump(self)


class DiscountCodeState(enum.Enum):
    NOT_ACTIVE = "NotActive"
    DOES_NOT_MATCH_CART = "DoesNotMatchCart"
    MATCHES_CART = "MatchesCart"
    MAX_APPLICATION_REACHED = "MaxApplicationReached"
    APPLICATION_STOPPED_BY_PREVIOUS_DISCOUNT = "ApplicationStoppedByPreviousDiscount"
    NOT_VALID = "NotValid"


class DiscountedLineItemPortion(_BaseType):
    discount: "CartDiscountReference"
    discounted_amount: "TypedMoney"

    def __init__(
        self, *, discount: "CartDiscountReference", discounted_amount: "TypedMoney"
    ):
        self.discount = discount
        self.discounted_amount = discounted_amount
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DiscountedLineItemPortion":
        from ._schemas.cart import DiscountedLineItemPortionSchema

        return DiscountedLineItemPortionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import DiscountedLineItemPortionSchema

        return DiscountedLineItemPortionSchema().dump(self)


class DiscountedLineItemPrice(_BaseType):
    value: "TypedMoney"
    included_discounts: typing.List["DiscountedLineItemPortion"]

    def __init__(
        self,
        *,
        value: "TypedMoney",
        included_discounts: typing.List["DiscountedLineItemPortion"]
    ):
        self.value = value
        self.included_discounts = included_discounts
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DiscountedLineItemPrice":
        from ._schemas.cart import DiscountedLineItemPriceSchema

        return DiscountedLineItemPriceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import DiscountedLineItemPriceSchema

        return DiscountedLineItemPriceSchema().dump(self)


class DiscountedLineItemPriceForQuantity(_BaseType):
    quantity: float
    discounted_price: "DiscountedLineItemPrice"

    def __init__(self, *, quantity: float, discounted_price: "DiscountedLineItemPrice"):
        self.quantity = quantity
        self.discounted_price = discounted_price
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DiscountedLineItemPriceForQuantity":
        from ._schemas.cart import DiscountedLineItemPriceForQuantitySchema

        return DiscountedLineItemPriceForQuantitySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import DiscountedLineItemPriceForQuantitySchema

        return DiscountedLineItemPriceForQuantitySchema().dump(self)


class ExternalLineItemTotalPrice(_BaseType):
    price: "Money"
    total_price: "Money"

    def __init__(self, *, price: "Money", total_price: "Money"):
        self.price = price
        self.total_price = total_price
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ExternalLineItemTotalPrice":
        from ._schemas.cart import ExternalLineItemTotalPriceSchema

        return ExternalLineItemTotalPriceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import ExternalLineItemTotalPriceSchema

        return ExternalLineItemTotalPriceSchema().dump(self)


class ExternalTaxAmountDraft(_BaseType):
    #: The total gross amount of the item (totalNet + taxes).
    total_gross: "Money"
    tax_rate: "ExternalTaxRateDraft"

    def __init__(self, *, total_gross: "Money", tax_rate: "ExternalTaxRateDraft"):
        self.total_gross = total_gross
        self.tax_rate = tax_rate
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ExternalTaxAmountDraft":
        from ._schemas.cart import ExternalTaxAmountDraftSchema

        return ExternalTaxAmountDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import ExternalTaxAmountDraftSchema

        return ExternalTaxAmountDraftSchema().dump(self)


class ExternalTaxRateDraft(_BaseType):
    name: str
    #: Percentage in the range of [0..1].
    #: Must be supplied if no `subRates` are specified.
    #: If `subRates` are specified
    #: then the `amount` can be omitted or it must be the sum of the amounts of all `subRates`.
    amount: typing.Optional[float]
    #: A two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    country: str
    #: The state in the country
    state: typing.Optional[str]
    #: For countries (e.g.
    #: the US) where the total tax is a combination of multiple taxes (e.g.
    #: state and local taxes).
    sub_rates: typing.Optional[typing.List["SubRate"]]
    #: The default value for `includedInPrice` is FALSE.
    included_in_price: typing.Optional[bool]

    def __init__(
        self,
        *,
        name: str,
        amount: typing.Optional[float] = None,
        country: str,
        state: typing.Optional[str] = None,
        sub_rates: typing.Optional[typing.List["SubRate"]] = None,
        included_in_price: typing.Optional[bool] = None
    ):
        self.name = name
        self.amount = amount
        self.country = country
        self.state = state
        self.sub_rates = sub_rates
        self.included_in_price = included_in_price
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ExternalTaxRateDraft":
        from ._schemas.cart import ExternalTaxRateDraftSchema

        return ExternalTaxRateDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import ExternalTaxRateDraftSchema

        return ExternalTaxRateDraftSchema().dump(self)


class InventoryMode(enum.Enum):
    TRACK_ONLY = "TrackOnly"
    RESERVE_ON_ORDER = "ReserveOnOrder"
    NONE = "None"


class ItemShippingDetails(_BaseType):
    #: Used to map what sub-quantity should be shipped to which address.
    #: Duplicate address keys are not allowed.
    targets: typing.List["ItemShippingTarget"]
    #: `true` if the quantity of the (custom) line item is equal to the sum of the sub-quantities in `targets`, `false` otherwise.
    #: A cart cannot be ordered when the value is `false`.
    #: The error InvalidItemShippingDetails will be triggered.
    valid: bool

    def __init__(self, *, targets: typing.List["ItemShippingTarget"], valid: bool):
        self.targets = targets
        self.valid = valid
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ItemShippingDetails":
        from ._schemas.cart import ItemShippingDetailsSchema

        return ItemShippingDetailsSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import ItemShippingDetailsSchema

        return ItemShippingDetailsSchema().dump(self)


class ItemShippingDetailsDraft(_BaseType):
    #: Used to capture one or more (custom) line item specific shipping addresses.
    #: By specifying sub-quantities, it is possible to set multiple shipping addresses for one line item.
    #: A cart can have `shippingDetails` where the `targets` sum does not match the quantity of the line item or custom line item.
    #: For the order creation and order updates the `targets` sum must match the quantity.
    targets: typing.List["ItemShippingTarget"]

    def __init__(self, *, targets: typing.List["ItemShippingTarget"]):
        self.targets = targets
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ItemShippingDetailsDraft":
        from ._schemas.cart import ItemShippingDetailsDraftSchema

        return ItemShippingDetailsDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import ItemShippingDetailsDraftSchema

        return ItemShippingDetailsDraftSchema().dump(self)


class ItemShippingTarget(_BaseType):
    #: The key of the address in the cart's `itemShippingAddresses`
    address_key: str
    #: The quantity of items that should go to the address with the specified `addressKey`.
    #: Only positive values are allowed.
    #: Using `0` as quantity is also possible in a draft object, but the element will not be present in the resulting ItemShippingDetails.
    quantity: float

    def __init__(self, *, address_key: str, quantity: float):
        self.address_key = address_key
        self.quantity = quantity
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ItemShippingTarget":
        from ._schemas.cart import ItemShippingTargetSchema

        return ItemShippingTargetSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import ItemShippingTargetSchema

        return ItemShippingTargetSchema().dump(self)


class LineItem(_BaseType):
    #: The unique ID of this LineItem.
    id: str
    product_id: str
    #: The product name.
    name: "LocalizedString"
    #: The slug of a product is inserted on the fly.
    #: It is always up-to-date and can therefore be used to link to the product detail page of the product.
    #: It is empty if the product has been deleted.
    #: The slug is also empty if the cart or order is retrieved via Reference Expansion or is a snapshot in a Message.
    product_slug: typing.Optional["LocalizedString"]
    product_type: "ProductTypeReference"
    #: The variant data is saved when the variant is added to the cart, and not updated automatically.
    #: It can manually be updated with the Recalculate update action.
    variant: "ProductVariant"
    #: The price of a line item is selected from the prices array of the product variant.
    #: If the `variant` field hasn't been updated, the price may not correspond to a price in `variant.prices`.
    price: "Price"
    #: Set once the `taxRate` is set.
    taxed_price: typing.Optional["TaxedItemPrice"]
    #: The total price of this line item.
    #: If the line item is discounted, then the `totalPrice` is the DiscountedLineItemPriceForQuantity multiplied by `quantity`.
    #: Otherwise the total price is the product price multiplied by the `quantity`.
    #: `totalPrice` may or may not include the taxes: it depends on the taxRate.includedInPrice property.
    total_price: "TypedMoney"
    #: The amount of a LineItem in the cart.
    #: Must be a positive integer.
    quantity: int
    #: When the line item was added to the cart. Optional for backwards
    #: compatibility reasons only.
    added_at: typing.Optional[datetime.datetime]
    state: typing.List["ItemState"]
    #: Will be set automatically in the `Platform` TaxMode once the shipping address is set is set.
    #: For the `External` tax mode the tax rate has to be set explicitly with the ExternalTaxRateDraft.
    tax_rate: typing.Optional["TaxRate"]
    #: The supply channel identifies the inventory entries that should be reserved.
    #: The channel has
    #: the role InventorySupply.
    supply_channel: typing.Optional["ChannelReference"]
    #: The distribution channel is used to select a ProductPrice.
    #: The channel has the role ProductDistribution.
    distribution_channel: typing.Optional["ChannelReference"]
    discounted_price_per_quantity: typing.List["DiscountedLineItemPriceForQuantity"]
    price_mode: "LineItemPriceMode"
    line_item_mode: "LineItemMode"
    custom: typing.Optional["CustomFields"]
    #: Container for line item specific address(es).
    shipping_details: typing.Optional["ItemShippingDetails"]

    def __init__(
        self,
        *,
        id: str,
        product_id: str,
        name: "LocalizedString",
        product_slug: typing.Optional["LocalizedString"] = None,
        product_type: "ProductTypeReference",
        variant: "ProductVariant",
        price: "Price",
        taxed_price: typing.Optional["TaxedItemPrice"] = None,
        total_price: "TypedMoney",
        quantity: int,
        added_at: typing.Optional[datetime.datetime] = None,
        state: typing.List["ItemState"],
        tax_rate: typing.Optional["TaxRate"] = None,
        supply_channel: typing.Optional["ChannelReference"] = None,
        distribution_channel: typing.Optional["ChannelReference"] = None,
        discounted_price_per_quantity: typing.List[
            "DiscountedLineItemPriceForQuantity"
        ],
        price_mode: "LineItemPriceMode",
        line_item_mode: "LineItemMode",
        custom: typing.Optional["CustomFields"] = None,
        shipping_details: typing.Optional["ItemShippingDetails"] = None
    ):
        self.id = id
        self.product_id = product_id
        self.name = name
        self.product_slug = product_slug
        self.product_type = product_type
        self.variant = variant
        self.price = price
        self.taxed_price = taxed_price
        self.total_price = total_price
        self.quantity = quantity
        self.added_at = added_at
        self.state = state
        self.tax_rate = tax_rate
        self.supply_channel = supply_channel
        self.distribution_channel = distribution_channel
        self.discounted_price_per_quantity = discounted_price_per_quantity
        self.price_mode = price_mode
        self.line_item_mode = line_item_mode
        self.custom = custom
        self.shipping_details = shipping_details
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "LineItem":
        from ._schemas.cart import LineItemSchema

        return LineItemSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import LineItemSchema

        return LineItemSchema().dump(self)


class LineItemDraft(_BaseType):
    product_id: typing.Optional[str]
    variant_id: typing.Optional[int]
    sku: typing.Optional[str]
    #: The amount of a `LineItem`in the cart.
    #: Must be a positive integer.
    quantity: typing.Optional[int]
    #: When the line item was added to the cart. Optional for backwards
    #: compatibility reasons only.
    added_at: typing.Optional[datetime.datetime]
    #: By providing supply channel information, you can unique identify
    #: inventory entries that should be reserved.
    #: The provided channel should have
    #: the InventorySupply role.
    supply_channel: typing.Optional["ChannelResourceIdentifier"]
    #: The channel is used to select a ProductPrice.
    #: The provided channel should have the ProductDistribution role.
    distribution_channel: typing.Optional["ChannelResourceIdentifier"]
    #: An external tax rate can be set if the cart has the `External` TaxMode.
    external_tax_rate: typing.Optional["ExternalTaxRateDraft"]
    #: The custom fields.
    custom: typing.Optional["CustomFieldsDraft"]
    #: Sets the line item `price` to the given value and sets the line item `priceMode` to `ExternalPrice` LineItemPriceMode.
    external_price: typing.Optional["Money"]
    #: Sets the line item `price` and `totalPrice` to the given values and sets the line item `priceMode` to `ExternalTotal` LineItemPriceMode.
    external_total_price: typing.Optional["ExternalLineItemTotalPrice"]
    #: Container for line item specific address(es).
    shipping_details: typing.Optional["ItemShippingDetailsDraft"]

    def __init__(
        self,
        *,
        product_id: typing.Optional[str] = None,
        variant_id: typing.Optional[int] = None,
        sku: typing.Optional[str] = None,
        quantity: typing.Optional[int] = None,
        added_at: typing.Optional[datetime.datetime] = None,
        supply_channel: typing.Optional["ChannelResourceIdentifier"] = None,
        distribution_channel: typing.Optional["ChannelResourceIdentifier"] = None,
        external_tax_rate: typing.Optional["ExternalTaxRateDraft"] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        external_price: typing.Optional["Money"] = None,
        external_total_price: typing.Optional["ExternalLineItemTotalPrice"] = None,
        shipping_details: typing.Optional["ItemShippingDetailsDraft"] = None
    ):
        self.product_id = product_id
        self.variant_id = variant_id
        self.sku = sku
        self.quantity = quantity
        self.added_at = added_at
        self.supply_channel = supply_channel
        self.distribution_channel = distribution_channel
        self.external_tax_rate = external_tax_rate
        self.custom = custom
        self.external_price = external_price
        self.external_total_price = external_total_price
        self.shipping_details = shipping_details
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "LineItemDraft":
        from ._schemas.cart import LineItemDraftSchema

        return LineItemDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import LineItemDraftSchema

        return LineItemDraftSchema().dump(self)


class LineItemMode(enum.Enum):
    STANDARD = "Standard"
    GIFT_LINE_ITEM = "GiftLineItem"


class LineItemPriceMode(enum.Enum):
    PLATFORM = "Platform"
    EXTERNAL_TOTAL = "ExternalTotal"
    EXTERNAL_PRICE = "ExternalPrice"


class ReplicaCartDraft(_BaseType):
    reference: typing.Union["CartReference", "OrderReference"]

    def __init__(self, *, reference: typing.Union["CartReference", "OrderReference"]):
        self.reference = reference
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ReplicaCartDraft":
        from ._schemas.cart import ReplicaCartDraftSchema

        return ReplicaCartDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import ReplicaCartDraftSchema

        return ReplicaCartDraftSchema().dump(self)


class RoundingMode(enum.Enum):
    HALF_EVEN = "HalfEven"
    HALF_UP = "HalfUp"
    HALF_DOWN = "HalfDown"


class ShippingInfo(_BaseType):
    shipping_method_name: str
    #: Determined based on the ShippingRate and its tiered prices, and either the sum of LineItem prices or the `shippingRateInput` field.
    price: "TypedMoney"
    #: The shipping rate used to determine the price.
    shipping_rate: "ShippingRate"
    #: Set once the `taxRate` is set.
    taxed_price: typing.Optional["TaxedItemPrice"]
    #: Will be set automatically in the `Platform` TaxMode once the shipping address is set is set.
    #: For the `External` tax mode the tax rate has to be set explicitly with the ExternalTaxRateDraft.
    tax_rate: typing.Optional["TaxRate"]
    tax_category: typing.Optional["TaxCategoryReference"]
    #: Not set if custom shipping method is used.
    shipping_method: typing.Optional["ShippingMethodReference"]
    #: Deliveries are compilations of information on how the articles are being delivered to the customers.
    deliveries: typing.Optional[typing.List["Delivery"]]
    discounted_price: typing.Optional["DiscountedLineItemPrice"]
    #: Indicates whether the ShippingMethod referenced in this ShippingInfo is allowed for the cart or not.
    shipping_method_state: "ShippingMethodState"

    def __init__(
        self,
        *,
        shipping_method_name: str,
        price: "TypedMoney",
        shipping_rate: "ShippingRate",
        taxed_price: typing.Optional["TaxedItemPrice"] = None,
        tax_rate: typing.Optional["TaxRate"] = None,
        tax_category: typing.Optional["TaxCategoryReference"] = None,
        shipping_method: typing.Optional["ShippingMethodReference"] = None,
        deliveries: typing.Optional[typing.List["Delivery"]] = None,
        discounted_price: typing.Optional["DiscountedLineItemPrice"] = None,
        shipping_method_state: "ShippingMethodState"
    ):
        self.shipping_method_name = shipping_method_name
        self.price = price
        self.shipping_rate = shipping_rate
        self.taxed_price = taxed_price
        self.tax_rate = tax_rate
        self.tax_category = tax_category
        self.shipping_method = shipping_method
        self.deliveries = deliveries
        self.discounted_price = discounted_price
        self.shipping_method_state = shipping_method_state
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ShippingInfo":
        from ._schemas.cart import ShippingInfoSchema

        return ShippingInfoSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import ShippingInfoSchema

        return ShippingInfoSchema().dump(self)


class ShippingMethodState(enum.Enum):
    DOES_NOT_MATCH_CART = "DoesNotMatchCart"
    MATCHES_CART = "MatchesCart"


class ShippingRateInput(_BaseType):
    type: str

    def __init__(self, *, type: str):
        self.type = type
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ShippingRateInput":
        if data["type"] == "Classification":
            from ._schemas.cart import ClassificationShippingRateInputSchema

            return ClassificationShippingRateInputSchema().load(data)
        if data["type"] == "Score":
            from ._schemas.cart import ScoreShippingRateInputSchema

            return ScoreShippingRateInputSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import ShippingRateInputSchema

        return ShippingRateInputSchema().dump(self)


class ClassificationShippingRateInput(ShippingRateInput):
    key: str
    label: "LocalizedString"

    def __init__(self, *, key: str, label: "LocalizedString"):
        self.key = key
        self.label = label
        super().__init__(type="Classification")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ClassificationShippingRateInput":
        from ._schemas.cart import ClassificationShippingRateInputSchema

        return ClassificationShippingRateInputSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import ClassificationShippingRateInputSchema

        return ClassificationShippingRateInputSchema().dump(self)


class ScoreShippingRateInput(ShippingRateInput):
    score: float

    def __init__(self, *, score: float):
        self.score = score
        super().__init__(type="Score")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ScoreShippingRateInput":
        from ._schemas.cart import ScoreShippingRateInputSchema

        return ScoreShippingRateInputSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import ScoreShippingRateInputSchema

        return ScoreShippingRateInputSchema().dump(self)


class ShippingRateInputDraft(_BaseType):
    type: str

    def __init__(self, *, type: str):
        self.type = type
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShippingRateInputDraft":
        if data["type"] == "Classification":
            from ._schemas.cart import ClassificationShippingRateInputDraftSchema

            return ClassificationShippingRateInputDraftSchema().load(data)
        if data["type"] == "Score":
            from ._schemas.cart import ScoreShippingRateInputDraftSchema

            return ScoreShippingRateInputDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import ShippingRateInputDraftSchema

        return ShippingRateInputDraftSchema().dump(self)


class ClassificationShippingRateInputDraft(ShippingRateInputDraft):
    key: str

    def __init__(self, *, key: str):
        self.key = key
        super().__init__(type="Classification")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ClassificationShippingRateInputDraft":
        from ._schemas.cart import ClassificationShippingRateInputDraftSchema

        return ClassificationShippingRateInputDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import ClassificationShippingRateInputDraftSchema

        return ClassificationShippingRateInputDraftSchema().dump(self)


class ScoreShippingRateInputDraft(ShippingRateInputDraft):
    score: float

    def __init__(self, *, score: float):
        self.score = score
        super().__init__(type="Score")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ScoreShippingRateInputDraft":
        from ._schemas.cart import ScoreShippingRateInputDraftSchema

        return ScoreShippingRateInputDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import ScoreShippingRateInputDraftSchema

        return ScoreShippingRateInputDraftSchema().dump(self)


class TaxCalculationMode(enum.Enum):
    LINE_ITEM_LEVEL = "LineItemLevel"
    UNIT_PRICE_LEVEL = "UnitPriceLevel"


class TaxMode(enum.Enum):
    PLATFORM = "Platform"
    EXTERNAL = "External"
    EXTERNAL_AMOUNT = "ExternalAmount"
    DISABLED = "Disabled"


class TaxPortion(_BaseType):
    name: typing.Optional[str]
    #: A number in the range [0..1]
    rate: float
    amount: "TypedMoney"

    def __init__(
        self, *, name: typing.Optional[str] = None, rate: float, amount: "TypedMoney"
    ):
        self.name = name
        self.rate = rate
        self.amount = amount
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TaxPortion":
        from ._schemas.cart import TaxPortionSchema

        return TaxPortionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import TaxPortionSchema

        return TaxPortionSchema().dump(self)


class TaxPortionDraft(_BaseType):
    name: typing.Optional[str]
    rate: float
    amount: "Money"

    def __init__(
        self, *, name: typing.Optional[str] = None, rate: float, amount: "Money"
    ):
        self.name = name
        self.rate = rate
        self.amount = amount
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TaxPortionDraft":
        from ._schemas.cart import TaxPortionDraftSchema

        return TaxPortionDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import TaxPortionDraftSchema

        return TaxPortionDraftSchema().dump(self)


class TaxedItemPrice(_BaseType):
    total_net: "TypedMoney"
    #: TaxedItemPrice fields can not be used in query predicates.
    total_gross: "TypedMoney"

    def __init__(self, *, total_net: "TypedMoney", total_gross: "TypedMoney"):
        self.total_net = total_net
        self.total_gross = total_gross
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TaxedItemPrice":
        from ._schemas.cart import TaxedItemPriceSchema

        return TaxedItemPriceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import TaxedItemPriceSchema

        return TaxedItemPriceSchema().dump(self)


class TaxedPrice(_BaseType):
    total_net: "TypedMoney"
    total_gross: "TypedMoney"
    #: TaxedPrice fields that can be used in query predicates: `totalNet`, `totalGross`.
    tax_portions: typing.List["TaxPortion"]

    def __init__(
        self,
        *,
        total_net: "TypedMoney",
        total_gross: "TypedMoney",
        tax_portions: typing.List["TaxPortion"]
    ):
        self.total_net = total_net
        self.total_gross = total_gross
        self.tax_portions = tax_portions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TaxedPrice":
        from ._schemas.cart import TaxedPriceSchema

        return TaxedPriceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import TaxedPriceSchema

        return TaxedPriceSchema().dump(self)


class TaxedPriceDraft(_BaseType):
    total_net: "Money"
    total_gross: "Money"
    tax_portions: typing.List["TaxPortionDraft"]

    def __init__(
        self,
        *,
        total_net: "Money",
        total_gross: "Money",
        tax_portions: typing.List["TaxPortionDraft"]
    ):
        self.total_net = total_net
        self.total_gross = total_gross
        self.tax_portions = tax_portions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TaxedPriceDraft":
        from ._schemas.cart import TaxedPriceDraftSchema

        return TaxedPriceDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import TaxedPriceDraftSchema

        return TaxedPriceDraftSchema().dump(self)


class CartAddCustomLineItemAction(CartUpdateAction):
    money: "Money"
    name: "LocalizedString"
    quantity: int
    slug: str
    tax_category: typing.Optional["TaxCategoryResourceIdentifier"]
    custom: typing.Optional["CustomFieldsDraft"]
    external_tax_rate: typing.Optional["ExternalTaxRateDraft"]

    def __init__(
        self,
        *,
        money: "Money",
        name: "LocalizedString",
        quantity: int,
        slug: str,
        tax_category: typing.Optional["TaxCategoryResourceIdentifier"] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        external_tax_rate: typing.Optional["ExternalTaxRateDraft"] = None
    ):
        self.money = money
        self.name = name
        self.quantity = quantity
        self.slug = slug
        self.tax_category = tax_category
        self.custom = custom
        self.external_tax_rate = external_tax_rate
        super().__init__(action="addCustomLineItem")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartAddCustomLineItemAction":
        from ._schemas.cart import CartAddCustomLineItemActionSchema

        return CartAddCustomLineItemActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartAddCustomLineItemActionSchema

        return CartAddCustomLineItemActionSchema().dump(self)


class CartAddDiscountCodeAction(CartUpdateAction):
    code: str

    def __init__(self, *, code: str):
        self.code = code
        super().__init__(action="addDiscountCode")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartAddDiscountCodeAction":
        from ._schemas.cart import CartAddDiscountCodeActionSchema

        return CartAddDiscountCodeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartAddDiscountCodeActionSchema

        return CartAddDiscountCodeActionSchema().dump(self)


class CartAddItemShippingAddressAction(CartUpdateAction):
    address: "Address"

    def __init__(self, *, address: "Address"):
        self.address = address
        super().__init__(action="addItemShippingAddress")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartAddItemShippingAddressAction":
        from ._schemas.cart import CartAddItemShippingAddressActionSchema

        return CartAddItemShippingAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartAddItemShippingAddressActionSchema

        return CartAddItemShippingAddressActionSchema().dump(self)


class CartAddLineItemAction(CartUpdateAction):
    custom: typing.Optional["CustomFieldsDraft"]
    distribution_channel: typing.Optional["ChannelResourceIdentifier"]
    external_tax_rate: typing.Optional["ExternalTaxRateDraft"]
    product_id: typing.Optional[str]
    variant_id: typing.Optional[int]
    sku: typing.Optional[str]
    quantity: typing.Optional[int]
    supply_channel: typing.Optional["ChannelResourceIdentifier"]
    external_price: typing.Optional["Money"]
    external_total_price: typing.Optional["ExternalLineItemTotalPrice"]
    shipping_details: typing.Optional["ItemShippingDetailsDraft"]

    def __init__(
        self,
        *,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        distribution_channel: typing.Optional["ChannelResourceIdentifier"] = None,
        external_tax_rate: typing.Optional["ExternalTaxRateDraft"] = None,
        product_id: typing.Optional[str] = None,
        variant_id: typing.Optional[int] = None,
        sku: typing.Optional[str] = None,
        quantity: typing.Optional[int] = None,
        supply_channel: typing.Optional["ChannelResourceIdentifier"] = None,
        external_price: typing.Optional["Money"] = None,
        external_total_price: typing.Optional["ExternalLineItemTotalPrice"] = None,
        shipping_details: typing.Optional["ItemShippingDetailsDraft"] = None
    ):
        self.custom = custom
        self.distribution_channel = distribution_channel
        self.external_tax_rate = external_tax_rate
        self.product_id = product_id
        self.variant_id = variant_id
        self.sku = sku
        self.quantity = quantity
        self.supply_channel = supply_channel
        self.external_price = external_price
        self.external_total_price = external_total_price
        self.shipping_details = shipping_details
        super().__init__(action="addLineItem")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CartAddLineItemAction":
        from ._schemas.cart import CartAddLineItemActionSchema

        return CartAddLineItemActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartAddLineItemActionSchema

        return CartAddLineItemActionSchema().dump(self)


class CartAddPaymentAction(CartUpdateAction):
    payment: "PaymentResourceIdentifier"

    def __init__(self, *, payment: "PaymentResourceIdentifier"):
        self.payment = payment
        super().__init__(action="addPayment")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CartAddPaymentAction":
        from ._schemas.cart import CartAddPaymentActionSchema

        return CartAddPaymentActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartAddPaymentActionSchema

        return CartAddPaymentActionSchema().dump(self)


class CartAddShoppingListAction(CartUpdateAction):
    shopping_list: "ShoppingListResourceIdentifier"
    supply_channel: typing.Optional["ChannelResourceIdentifier"]
    distribution_channel: typing.Optional["ChannelResourceIdentifier"]

    def __init__(
        self,
        *,
        shopping_list: "ShoppingListResourceIdentifier",
        supply_channel: typing.Optional["ChannelResourceIdentifier"] = None,
        distribution_channel: typing.Optional["ChannelResourceIdentifier"] = None
    ):
        self.shopping_list = shopping_list
        self.supply_channel = supply_channel
        self.distribution_channel = distribution_channel
        super().__init__(action="addShoppingList")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartAddShoppingListAction":
        from ._schemas.cart import CartAddShoppingListActionSchema

        return CartAddShoppingListActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartAddShoppingListActionSchema

        return CartAddShoppingListActionSchema().dump(self)


class CartApplyDeltaToCustomLineItemShippingDetailsTargetsAction(CartUpdateAction):
    custom_line_item_id: str
    targets_delta: typing.List["ItemShippingTarget"]

    def __init__(
        self,
        *,
        custom_line_item_id: str,
        targets_delta: typing.List["ItemShippingTarget"]
    ):
        self.custom_line_item_id = custom_line_item_id
        self.targets_delta = targets_delta
        super().__init__(action="applyDeltaToCustomLineItemShippingDetailsTargets")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartApplyDeltaToCustomLineItemShippingDetailsTargetsAction":
        from ._schemas.cart import (
            CartApplyDeltaToCustomLineItemShippingDetailsTargetsActionSchema,
        )

        return CartApplyDeltaToCustomLineItemShippingDetailsTargetsActionSchema().load(
            data
        )

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import (
            CartApplyDeltaToCustomLineItemShippingDetailsTargetsActionSchema,
        )

        return CartApplyDeltaToCustomLineItemShippingDetailsTargetsActionSchema().dump(
            self
        )


class CartApplyDeltaToLineItemShippingDetailsTargetsAction(CartUpdateAction):
    line_item_id: str
    targets_delta: typing.List["ItemShippingTarget"]

    def __init__(
        self, *, line_item_id: str, targets_delta: typing.List["ItemShippingTarget"]
    ):
        self.line_item_id = line_item_id
        self.targets_delta = targets_delta
        super().__init__(action="applyDeltaToLineItemShippingDetailsTargets")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartApplyDeltaToLineItemShippingDetailsTargetsAction":
        from ._schemas.cart import (
            CartApplyDeltaToLineItemShippingDetailsTargetsActionSchema,
        )

        return CartApplyDeltaToLineItemShippingDetailsTargetsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import (
            CartApplyDeltaToLineItemShippingDetailsTargetsActionSchema,
        )

        return CartApplyDeltaToLineItemShippingDetailsTargetsActionSchema().dump(self)


class CartChangeCustomLineItemMoneyAction(CartUpdateAction):
    custom_line_item_id: str
    money: "Money"

    def __init__(self, *, custom_line_item_id: str, money: "Money"):
        self.custom_line_item_id = custom_line_item_id
        self.money = money
        super().__init__(action="changeCustomLineItemMoney")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartChangeCustomLineItemMoneyAction":
        from ._schemas.cart import CartChangeCustomLineItemMoneyActionSchema

        return CartChangeCustomLineItemMoneyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartChangeCustomLineItemMoneyActionSchema

        return CartChangeCustomLineItemMoneyActionSchema().dump(self)


class CartChangeCustomLineItemQuantityAction(CartUpdateAction):
    custom_line_item_id: str
    quantity: int

    def __init__(self, *, custom_line_item_id: str, quantity: int):
        self.custom_line_item_id = custom_line_item_id
        self.quantity = quantity
        super().__init__(action="changeCustomLineItemQuantity")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartChangeCustomLineItemQuantityAction":
        from ._schemas.cart import CartChangeCustomLineItemQuantityActionSchema

        return CartChangeCustomLineItemQuantityActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartChangeCustomLineItemQuantityActionSchema

        return CartChangeCustomLineItemQuantityActionSchema().dump(self)


class CartChangeLineItemQuantityAction(CartUpdateAction):
    line_item_id: str
    quantity: int
    external_price: typing.Optional["Money"]
    external_total_price: typing.Optional["ExternalLineItemTotalPrice"]

    def __init__(
        self,
        *,
        line_item_id: str,
        quantity: int,
        external_price: typing.Optional["Money"] = None,
        external_total_price: typing.Optional["ExternalLineItemTotalPrice"] = None
    ):
        self.line_item_id = line_item_id
        self.quantity = quantity
        self.external_price = external_price
        self.external_total_price = external_total_price
        super().__init__(action="changeLineItemQuantity")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartChangeLineItemQuantityAction":
        from ._schemas.cart import CartChangeLineItemQuantityActionSchema

        return CartChangeLineItemQuantityActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartChangeLineItemQuantityActionSchema

        return CartChangeLineItemQuantityActionSchema().dump(self)


class CartChangeTaxCalculationModeAction(CartUpdateAction):
    tax_calculation_mode: "TaxCalculationMode"

    def __init__(self, *, tax_calculation_mode: "TaxCalculationMode"):
        self.tax_calculation_mode = tax_calculation_mode
        super().__init__(action="changeTaxCalculationMode")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartChangeTaxCalculationModeAction":
        from ._schemas.cart import CartChangeTaxCalculationModeActionSchema

        return CartChangeTaxCalculationModeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartChangeTaxCalculationModeActionSchema

        return CartChangeTaxCalculationModeActionSchema().dump(self)


class CartChangeTaxModeAction(CartUpdateAction):
    tax_mode: "TaxMode"

    def __init__(self, *, tax_mode: "TaxMode"):
        self.tax_mode = tax_mode
        super().__init__(action="changeTaxMode")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartChangeTaxModeAction":
        from ._schemas.cart import CartChangeTaxModeActionSchema

        return CartChangeTaxModeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartChangeTaxModeActionSchema

        return CartChangeTaxModeActionSchema().dump(self)


class CartChangeTaxRoundingModeAction(CartUpdateAction):
    tax_rounding_mode: "RoundingMode"

    def __init__(self, *, tax_rounding_mode: "RoundingMode"):
        self.tax_rounding_mode = tax_rounding_mode
        super().__init__(action="changeTaxRoundingMode")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartChangeTaxRoundingModeAction":
        from ._schemas.cart import CartChangeTaxRoundingModeActionSchema

        return CartChangeTaxRoundingModeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartChangeTaxRoundingModeActionSchema

        return CartChangeTaxRoundingModeActionSchema().dump(self)


class CartRecalculateAction(CartUpdateAction):
    #: If set to `true`, the line item product data (`name`, `variant` and `productType`) will also be updated.
    #: If set to `false`,
    #: only the prices and tax rates of the line item will be updated.
    #: The updated price of a line item may not correspond to a price in `variant.prices` anymore.
    update_product_data: typing.Optional[bool]

    def __init__(self, *, update_product_data: typing.Optional[bool] = None):
        self.update_product_data = update_product_data
        super().__init__(action="recalculate")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CartRecalculateAction":
        from ._schemas.cart import CartRecalculateActionSchema

        return CartRecalculateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartRecalculateActionSchema

        return CartRecalculateActionSchema().dump(self)


class CartRemoveCustomLineItemAction(CartUpdateAction):
    custom_line_item_id: str

    def __init__(self, *, custom_line_item_id: str):
        self.custom_line_item_id = custom_line_item_id
        super().__init__(action="removeCustomLineItem")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartRemoveCustomLineItemAction":
        from ._schemas.cart import CartRemoveCustomLineItemActionSchema

        return CartRemoveCustomLineItemActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartRemoveCustomLineItemActionSchema

        return CartRemoveCustomLineItemActionSchema().dump(self)


class CartRemoveDiscountCodeAction(CartUpdateAction):
    discount_code: "DiscountCodeReference"

    def __init__(self, *, discount_code: "DiscountCodeReference"):
        self.discount_code = discount_code
        super().__init__(action="removeDiscountCode")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartRemoveDiscountCodeAction":
        from ._schemas.cart import CartRemoveDiscountCodeActionSchema

        return CartRemoveDiscountCodeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartRemoveDiscountCodeActionSchema

        return CartRemoveDiscountCodeActionSchema().dump(self)


class CartRemoveItemShippingAddressAction(CartUpdateAction):
    address_key: str

    def __init__(self, *, address_key: str):
        self.address_key = address_key
        super().__init__(action="removeItemShippingAddress")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartRemoveItemShippingAddressAction":
        from ._schemas.cart import CartRemoveItemShippingAddressActionSchema

        return CartRemoveItemShippingAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartRemoveItemShippingAddressActionSchema

        return CartRemoveItemShippingAddressActionSchema().dump(self)


class CartRemoveLineItemAction(CartUpdateAction):
    line_item_id: str
    quantity: typing.Optional[int]
    external_price: typing.Optional["Money"]
    external_total_price: typing.Optional["ExternalLineItemTotalPrice"]
    shipping_details_to_remove: typing.Optional["ItemShippingDetailsDraft"]

    def __init__(
        self,
        *,
        line_item_id: str,
        quantity: typing.Optional[int] = None,
        external_price: typing.Optional["Money"] = None,
        external_total_price: typing.Optional["ExternalLineItemTotalPrice"] = None,
        shipping_details_to_remove: typing.Optional["ItemShippingDetailsDraft"] = None
    ):
        self.line_item_id = line_item_id
        self.quantity = quantity
        self.external_price = external_price
        self.external_total_price = external_total_price
        self.shipping_details_to_remove = shipping_details_to_remove
        super().__init__(action="removeLineItem")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartRemoveLineItemAction":
        from ._schemas.cart import CartRemoveLineItemActionSchema

        return CartRemoveLineItemActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartRemoveLineItemActionSchema

        return CartRemoveLineItemActionSchema().dump(self)


class CartRemovePaymentAction(CartUpdateAction):
    payment: "PaymentResourceIdentifier"

    def __init__(self, *, payment: "PaymentResourceIdentifier"):
        self.payment = payment
        super().__init__(action="removePayment")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartRemovePaymentAction":
        from ._schemas.cart import CartRemovePaymentActionSchema

        return CartRemovePaymentActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartRemovePaymentActionSchema

        return CartRemovePaymentActionSchema().dump(self)


class CartSetAnonymousIdAction(CartUpdateAction):
    #: If not set, any existing anonymous ID will be removed.
    anonymous_id: typing.Optional[str]

    def __init__(self, *, anonymous_id: typing.Optional[str] = None):
        self.anonymous_id = anonymous_id
        super().__init__(action="setAnonymousId")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartSetAnonymousIdAction":
        from ._schemas.cart import CartSetAnonymousIdActionSchema

        return CartSetAnonymousIdActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSetAnonymousIdActionSchema

        return CartSetAnonymousIdActionSchema().dump(self)


class CartSetBillingAddressAction(CartUpdateAction):
    address: typing.Optional["Address"]

    def __init__(self, *, address: typing.Optional["Address"] = None):
        self.address = address
        super().__init__(action="setBillingAddress")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartSetBillingAddressAction":
        from ._schemas.cart import CartSetBillingAddressActionSchema

        return CartSetBillingAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSetBillingAddressActionSchema

        return CartSetBillingAddressActionSchema().dump(self)


class CartSetCartTotalTaxAction(CartUpdateAction):
    #: The total gross amount of the cart (totalNet + taxes).
    external_total_gross: "Money"
    external_tax_portions: typing.Optional[typing.List["TaxPortionDraft"]]

    def __init__(
        self,
        *,
        external_total_gross: "Money",
        external_tax_portions: typing.Optional[typing.List["TaxPortionDraft"]] = None
    ):
        self.external_total_gross = external_total_gross
        self.external_tax_portions = external_tax_portions
        super().__init__(action="setCartTotalTax")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartSetCartTotalTaxAction":
        from ._schemas.cart import CartSetCartTotalTaxActionSchema

        return CartSetCartTotalTaxActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSetCartTotalTaxActionSchema

        return CartSetCartTotalTaxActionSchema().dump(self)


class CartSetCountryAction(CartUpdateAction):
    #: A two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    country: typing.Optional[str]

    def __init__(self, *, country: typing.Optional[str] = None):
        self.country = country
        super().__init__(action="setCountry")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CartSetCountryAction":
        from ._schemas.cart import CartSetCountryActionSchema

        return CartSetCountryActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSetCountryActionSchema

        return CartSetCountryActionSchema().dump(self)


class CartSetCustomFieldAction(CartUpdateAction):
    name: str
    value: typing.Optional[typing.Any]

    def __init__(self, *, name: str, value: typing.Optional[typing.Any] = None):
        self.name = name
        self.value = value
        super().__init__(action="setCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartSetCustomFieldAction":
        from ._schemas.cart import CartSetCustomFieldActionSchema

        return CartSetCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSetCustomFieldActionSchema

        return CartSetCustomFieldActionSchema().dump(self)


class CartSetCustomLineItemCustomFieldAction(CartUpdateAction):
    custom_line_item_id: str
    name: str
    value: typing.Optional[typing.Any]

    def __init__(
        self,
        *,
        custom_line_item_id: str,
        name: str,
        value: typing.Optional[typing.Any] = None
    ):
        self.custom_line_item_id = custom_line_item_id
        self.name = name
        self.value = value
        super().__init__(action="setCustomLineItemCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartSetCustomLineItemCustomFieldAction":
        from ._schemas.cart import CartSetCustomLineItemCustomFieldActionSchema

        return CartSetCustomLineItemCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSetCustomLineItemCustomFieldActionSchema

        return CartSetCustomLineItemCustomFieldActionSchema().dump(self)


class CartSetCustomLineItemCustomTypeAction(CartUpdateAction):
    custom_line_item_id: str
    type: typing.Optional["TypeResourceIdentifier"]
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        custom_line_item_id: str,
        type: typing.Optional["TypeResourceIdentifier"] = None,
        fields: typing.Optional["FieldContainer"] = None
    ):
        self.custom_line_item_id = custom_line_item_id
        self.type = type
        self.fields = fields
        super().__init__(action="setCustomLineItemCustomType")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartSetCustomLineItemCustomTypeAction":
        from ._schemas.cart import CartSetCustomLineItemCustomTypeActionSchema

        return CartSetCustomLineItemCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSetCustomLineItemCustomTypeActionSchema

        return CartSetCustomLineItemCustomTypeActionSchema().dump(self)


class CartSetCustomLineItemShippingDetailsAction(CartUpdateAction):
    custom_line_item_id: str
    shipping_details: typing.Optional["ItemShippingDetailsDraft"]

    def __init__(
        self,
        *,
        custom_line_item_id: str,
        shipping_details: typing.Optional["ItemShippingDetailsDraft"] = None
    ):
        self.custom_line_item_id = custom_line_item_id
        self.shipping_details = shipping_details
        super().__init__(action="setCustomLineItemShippingDetails")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartSetCustomLineItemShippingDetailsAction":
        from ._schemas.cart import CartSetCustomLineItemShippingDetailsActionSchema

        return CartSetCustomLineItemShippingDetailsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSetCustomLineItemShippingDetailsActionSchema

        return CartSetCustomLineItemShippingDetailsActionSchema().dump(self)


class CartSetCustomLineItemTaxAmountAction(CartUpdateAction):
    custom_line_item_id: str
    external_tax_amount: typing.Optional["ExternalTaxAmountDraft"]

    def __init__(
        self,
        *,
        custom_line_item_id: str,
        external_tax_amount: typing.Optional["ExternalTaxAmountDraft"] = None
    ):
        self.custom_line_item_id = custom_line_item_id
        self.external_tax_amount = external_tax_amount
        super().__init__(action="setCustomLineItemTaxAmount")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartSetCustomLineItemTaxAmountAction":
        from ._schemas.cart import CartSetCustomLineItemTaxAmountActionSchema

        return CartSetCustomLineItemTaxAmountActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSetCustomLineItemTaxAmountActionSchema

        return CartSetCustomLineItemTaxAmountActionSchema().dump(self)


class CartSetCustomLineItemTaxRateAction(CartUpdateAction):
    custom_line_item_id: str
    external_tax_rate: typing.Optional["ExternalTaxRateDraft"]

    def __init__(
        self,
        *,
        custom_line_item_id: str,
        external_tax_rate: typing.Optional["ExternalTaxRateDraft"] = None
    ):
        self.custom_line_item_id = custom_line_item_id
        self.external_tax_rate = external_tax_rate
        super().__init__(action="setCustomLineItemTaxRate")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartSetCustomLineItemTaxRateAction":
        from ._schemas.cart import CartSetCustomLineItemTaxRateActionSchema

        return CartSetCustomLineItemTaxRateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSetCustomLineItemTaxRateActionSchema

        return CartSetCustomLineItemTaxRateActionSchema().dump(self)


class CartSetCustomShippingMethodAction(CartUpdateAction):
    shipping_method_name: str
    shipping_rate: "ShippingRateDraft"
    tax_category: typing.Optional["TaxCategoryResourceIdentifier"]
    external_tax_rate: typing.Optional["ExternalTaxRateDraft"]

    def __init__(
        self,
        *,
        shipping_method_name: str,
        shipping_rate: "ShippingRateDraft",
        tax_category: typing.Optional["TaxCategoryResourceIdentifier"] = None,
        external_tax_rate: typing.Optional["ExternalTaxRateDraft"] = None
    ):
        self.shipping_method_name = shipping_method_name
        self.shipping_rate = shipping_rate
        self.tax_category = tax_category
        self.external_tax_rate = external_tax_rate
        super().__init__(action="setCustomShippingMethod")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartSetCustomShippingMethodAction":
        from ._schemas.cart import CartSetCustomShippingMethodActionSchema

        return CartSetCustomShippingMethodActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSetCustomShippingMethodActionSchema

        return CartSetCustomShippingMethodActionSchema().dump(self)


class CartSetCustomTypeAction(CartUpdateAction):
    type: typing.Optional["TypeResourceIdentifier"]
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        type: typing.Optional["TypeResourceIdentifier"] = None,
        fields: typing.Optional["FieldContainer"] = None
    ):
        self.type = type
        self.fields = fields
        super().__init__(action="setCustomType")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartSetCustomTypeAction":
        from ._schemas.cart import CartSetCustomTypeActionSchema

        return CartSetCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSetCustomTypeActionSchema

        return CartSetCustomTypeActionSchema().dump(self)


class CartSetCustomerEmailAction(CartUpdateAction):
    email: str

    def __init__(self, *, email: str):
        self.email = email
        super().__init__(action="setCustomerEmail")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartSetCustomerEmailAction":
        from ._schemas.cart import CartSetCustomerEmailActionSchema

        return CartSetCustomerEmailActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSetCustomerEmailActionSchema

        return CartSetCustomerEmailActionSchema().dump(self)


class CartSetCustomerGroupAction(CartUpdateAction):
    customer_group: typing.Optional["CustomerGroupResourceIdentifier"]

    def __init__(
        self,
        *,
        customer_group: typing.Optional["CustomerGroupResourceIdentifier"] = None
    ):
        self.customer_group = customer_group
        super().__init__(action="setCustomerGroup")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartSetCustomerGroupAction":
        from ._schemas.cart import CartSetCustomerGroupActionSchema

        return CartSetCustomerGroupActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSetCustomerGroupActionSchema

        return CartSetCustomerGroupActionSchema().dump(self)


class CartSetCustomerIdAction(CartUpdateAction):
    #: If set, a customer with the given ID must exist in the project.
    customer_id: typing.Optional[str]

    def __init__(self, *, customer_id: typing.Optional[str] = None):
        self.customer_id = customer_id
        super().__init__(action="setCustomerId")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartSetCustomerIdAction":
        from ._schemas.cart import CartSetCustomerIdActionSchema

        return CartSetCustomerIdActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSetCustomerIdActionSchema

        return CartSetCustomerIdActionSchema().dump(self)


class CartSetDeleteDaysAfterLastModificationAction(CartUpdateAction):
    delete_days_after_last_modification: typing.Optional[int]

    def __init__(
        self, *, delete_days_after_last_modification: typing.Optional[int] = None
    ):
        self.delete_days_after_last_modification = delete_days_after_last_modification
        super().__init__(action="setDeleteDaysAfterLastModification")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartSetDeleteDaysAfterLastModificationAction":
        from ._schemas.cart import CartSetDeleteDaysAfterLastModificationActionSchema

        return CartSetDeleteDaysAfterLastModificationActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSetDeleteDaysAfterLastModificationActionSchema

        return CartSetDeleteDaysAfterLastModificationActionSchema().dump(self)


class CartSetLineItemCustomFieldAction(CartUpdateAction):
    line_item_id: str
    name: str
    value: typing.Optional[typing.Any]

    def __init__(
        self, *, line_item_id: str, name: str, value: typing.Optional[typing.Any] = None
    ):
        self.line_item_id = line_item_id
        self.name = name
        self.value = value
        super().__init__(action="setLineItemCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartSetLineItemCustomFieldAction":
        from ._schemas.cart import CartSetLineItemCustomFieldActionSchema

        return CartSetLineItemCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSetLineItemCustomFieldActionSchema

        return CartSetLineItemCustomFieldActionSchema().dump(self)


class CartSetLineItemCustomTypeAction(CartUpdateAction):
    line_item_id: str
    type: typing.Optional["TypeResourceIdentifier"]
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        line_item_id: str,
        type: typing.Optional["TypeResourceIdentifier"] = None,
        fields: typing.Optional["FieldContainer"] = None
    ):
        self.line_item_id = line_item_id
        self.type = type
        self.fields = fields
        super().__init__(action="setLineItemCustomType")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartSetLineItemCustomTypeAction":
        from ._schemas.cart import CartSetLineItemCustomTypeActionSchema

        return CartSetLineItemCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSetLineItemCustomTypeActionSchema

        return CartSetLineItemCustomTypeActionSchema().dump(self)


class CartSetLineItemDistributionChannelAction(CartUpdateAction):
    line_item_id: str
    distribution_channel: typing.Optional["ChannelResourceIdentifier"]

    def __init__(
        self,
        *,
        line_item_id: str,
        distribution_channel: typing.Optional["ChannelResourceIdentifier"] = None
    ):
        self.line_item_id = line_item_id
        self.distribution_channel = distribution_channel
        super().__init__(action="setLineItemDistributionChannel")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartSetLineItemDistributionChannelAction":
        from ._schemas.cart import CartSetLineItemDistributionChannelActionSchema

        return CartSetLineItemDistributionChannelActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSetLineItemDistributionChannelActionSchema

        return CartSetLineItemDistributionChannelActionSchema().dump(self)


class CartSetLineItemPriceAction(CartUpdateAction):
    line_item_id: str
    external_price: typing.Optional["Money"]

    def __init__(
        self, *, line_item_id: str, external_price: typing.Optional["Money"] = None
    ):
        self.line_item_id = line_item_id
        self.external_price = external_price
        super().__init__(action="setLineItemPrice")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartSetLineItemPriceAction":
        from ._schemas.cart import CartSetLineItemPriceActionSchema

        return CartSetLineItemPriceActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSetLineItemPriceActionSchema

        return CartSetLineItemPriceActionSchema().dump(self)


class CartSetLineItemShippingDetailsAction(CartUpdateAction):
    line_item_id: str
    shipping_details: typing.Optional["ItemShippingDetailsDraft"]

    def __init__(
        self,
        *,
        line_item_id: str,
        shipping_details: typing.Optional["ItemShippingDetailsDraft"] = None
    ):
        self.line_item_id = line_item_id
        self.shipping_details = shipping_details
        super().__init__(action="setLineItemShippingDetails")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartSetLineItemShippingDetailsAction":
        from ._schemas.cart import CartSetLineItemShippingDetailsActionSchema

        return CartSetLineItemShippingDetailsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSetLineItemShippingDetailsActionSchema

        return CartSetLineItemShippingDetailsActionSchema().dump(self)


class CartSetLineItemTaxAmountAction(CartUpdateAction):
    line_item_id: str
    external_tax_amount: typing.Optional["ExternalTaxAmountDraft"]

    def __init__(
        self,
        *,
        line_item_id: str,
        external_tax_amount: typing.Optional["ExternalTaxAmountDraft"] = None
    ):
        self.line_item_id = line_item_id
        self.external_tax_amount = external_tax_amount
        super().__init__(action="setLineItemTaxAmount")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartSetLineItemTaxAmountAction":
        from ._schemas.cart import CartSetLineItemTaxAmountActionSchema

        return CartSetLineItemTaxAmountActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSetLineItemTaxAmountActionSchema

        return CartSetLineItemTaxAmountActionSchema().dump(self)


class CartSetLineItemTaxRateAction(CartUpdateAction):
    line_item_id: str
    external_tax_rate: typing.Optional["ExternalTaxRateDraft"]

    def __init__(
        self,
        *,
        line_item_id: str,
        external_tax_rate: typing.Optional["ExternalTaxRateDraft"] = None
    ):
        self.line_item_id = line_item_id
        self.external_tax_rate = external_tax_rate
        super().__init__(action="setLineItemTaxRate")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartSetLineItemTaxRateAction":
        from ._schemas.cart import CartSetLineItemTaxRateActionSchema

        return CartSetLineItemTaxRateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSetLineItemTaxRateActionSchema

        return CartSetLineItemTaxRateActionSchema().dump(self)


class CartSetLineItemTotalPriceAction(CartUpdateAction):
    line_item_id: str
    external_total_price: typing.Optional["ExternalLineItemTotalPrice"]

    def __init__(
        self,
        *,
        line_item_id: str,
        external_total_price: typing.Optional["ExternalLineItemTotalPrice"] = None
    ):
        self.line_item_id = line_item_id
        self.external_total_price = external_total_price
        super().__init__(action="setLineItemTotalPrice")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartSetLineItemTotalPriceAction":
        from ._schemas.cart import CartSetLineItemTotalPriceActionSchema

        return CartSetLineItemTotalPriceActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSetLineItemTotalPriceActionSchema

        return CartSetLineItemTotalPriceActionSchema().dump(self)


class CartSetLocaleAction(CartUpdateAction):
    locale: typing.Optional[str]

    def __init__(self, *, locale: typing.Optional[str] = None):
        self.locale = locale
        super().__init__(action="setLocale")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CartSetLocaleAction":
        from ._schemas.cart import CartSetLocaleActionSchema

        return CartSetLocaleActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSetLocaleActionSchema

        return CartSetLocaleActionSchema().dump(self)


class CartSetShippingAddressAction(CartUpdateAction):
    address: typing.Optional["Address"]

    def __init__(self, *, address: typing.Optional["Address"] = None):
        self.address = address
        super().__init__(action="setShippingAddress")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartSetShippingAddressAction":
        from ._schemas.cart import CartSetShippingAddressActionSchema

        return CartSetShippingAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSetShippingAddressActionSchema

        return CartSetShippingAddressActionSchema().dump(self)


class CartSetShippingMethodAction(CartUpdateAction):
    shipping_method: typing.Optional["ShippingMethodResourceIdentifier"]
    external_tax_rate: typing.Optional["ExternalTaxRateDraft"]

    def __init__(
        self,
        *,
        shipping_method: typing.Optional["ShippingMethodResourceIdentifier"] = None,
        external_tax_rate: typing.Optional["ExternalTaxRateDraft"] = None
    ):
        self.shipping_method = shipping_method
        self.external_tax_rate = external_tax_rate
        super().__init__(action="setShippingMethod")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartSetShippingMethodAction":
        from ._schemas.cart import CartSetShippingMethodActionSchema

        return CartSetShippingMethodActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSetShippingMethodActionSchema

        return CartSetShippingMethodActionSchema().dump(self)


class CartSetShippingMethodTaxAmountAction(CartUpdateAction):
    external_tax_amount: typing.Optional["ExternalTaxAmountDraft"]

    def __init__(
        self, *, external_tax_amount: typing.Optional["ExternalTaxAmountDraft"] = None
    ):
        self.external_tax_amount = external_tax_amount
        super().__init__(action="setShippingMethodTaxAmount")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartSetShippingMethodTaxAmountAction":
        from ._schemas.cart import CartSetShippingMethodTaxAmountActionSchema

        return CartSetShippingMethodTaxAmountActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSetShippingMethodTaxAmountActionSchema

        return CartSetShippingMethodTaxAmountActionSchema().dump(self)


class CartSetShippingMethodTaxRateAction(CartUpdateAction):
    external_tax_rate: typing.Optional["ExternalTaxRateDraft"]

    def __init__(
        self, *, external_tax_rate: typing.Optional["ExternalTaxRateDraft"] = None
    ):
        self.external_tax_rate = external_tax_rate
        super().__init__(action="setShippingMethodTaxRate")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartSetShippingMethodTaxRateAction":
        from ._schemas.cart import CartSetShippingMethodTaxRateActionSchema

        return CartSetShippingMethodTaxRateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSetShippingMethodTaxRateActionSchema

        return CartSetShippingMethodTaxRateActionSchema().dump(self)


class CartSetShippingRateInputAction(CartUpdateAction):
    #: Based on the definition of ShippingRateInputType.
    #: If CartClassification is defined, it must be ClassificationShippingRateInput.
    #: If CartScore is defined, it must be ScoreShippingRateInput.
    #: Otherwise it can not bet set.
    shipping_rate_input: typing.Optional["ShippingRateInputDraft"]

    def __init__(
        self, *, shipping_rate_input: typing.Optional["ShippingRateInputDraft"] = None
    ):
        self.shipping_rate_input = shipping_rate_input
        super().__init__(action="setShippingRateInput")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartSetShippingRateInputAction":
        from ._schemas.cart import CartSetShippingRateInputActionSchema

        return CartSetShippingRateInputActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartSetShippingRateInputActionSchema

        return CartSetShippingRateInputActionSchema().dump(self)


class CartUpdateItemShippingAddressAction(CartUpdateAction):
    address: "Address"

    def __init__(self, *, address: "Address"):
        self.address = address
        super().__init__(action="updateItemShippingAddress")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartUpdateItemShippingAddressAction":
        from ._schemas.cart import CartUpdateItemShippingAddressActionSchema

        return CartUpdateItemShippingAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart import CartUpdateItemShippingAddressActionSchema

        return CartUpdateItemShippingAddressActionSchema().dump(self)


class ProductPublishScope(enum.Enum):
    ALL = "All"
    PRICES = "Prices"
