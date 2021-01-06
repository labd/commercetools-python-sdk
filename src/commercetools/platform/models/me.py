# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .cart import (
    CartOrigin,
    CartState,
    InventoryMode,
    RoundingMode,
    TaxCalculationMode,
    TaxMode,
)
from .common import BaseResource
from .order import OrderState, PaymentState, ShipmentState
from .payment import TransactionType

if typing.TYPE_CHECKING:
    from .cart import (
        CartOrigin,
        CartReference,
        CartState,
        CustomLineItem,
        DiscountCodeInfo,
        ExternalLineItemTotalPrice,
        ExternalTaxRateDraft,
        InventoryMode,
        ItemShippingDetailsDraft,
        ItemShippingTarget,
        LineItem,
        RoundingMode,
        ShippingInfo,
        ShippingRateInput,
        TaxCalculationMode,
        TaxedPrice,
        TaxMode,
    )
    from .cart_discount import CartDiscountReference
    from .channel import ChannelResourceIdentifier
    from .common import (
        Address,
        CreatedBy,
        LastModifiedBy,
        LocalizedString,
        Money,
        TypedMoney,
    )
    from .customer import CustomerReference
    from .customer_group import CustomerGroupReference
    from .discount_code import DiscountCodeReference
    from .order import (
        OrderState,
        PaymentInfo,
        PaymentState,
        ReturnInfo,
        ShipmentState,
        SyncInfo,
    )
    from .payment import (
        PaymentMethodInfo,
        PaymentResourceIdentifier,
        Transaction,
        TransactionDraft,
        TransactionType,
    )
    from .shipping_method import ShippingMethodResourceIdentifier, ShippingRateDraft
    from .shopping_list import ShoppingListLineItemDraft, TextLineItemDraft
    from .state import StateReference
    from .store import StoreKeyReference, StoreResourceIdentifier
    from .tax_category import TaxCategoryResourceIdentifier
    from .type import (
        CustomFields,
        CustomFieldsDraft,
        FieldContainer,
        TypeResourceIdentifier,
    )

__all__ = [
    "MyCart",
    "MyCartAddDiscountCodeAction",
    "MyCartAddItemShippingAddressAction",
    "MyCartAddLineItemAction",
    "MyCartAddPaymentAction",
    "MyCartApplyDeltaToLineItemShippingDetailsTargetsAction",
    "MyCartChangeLineItemQuantityAction",
    "MyCartChangeTaxModeAction",
    "MyCartDraft",
    "MyCartRecalculateAction",
    "MyCartRemoveDiscountCodeAction",
    "MyCartRemoveItemShippingAddressAction",
    "MyCartRemoveLineItemAction",
    "MyCartRemovePaymentAction",
    "MyCartSetBillingAddressAction",
    "MyCartSetCountryAction",
    "MyCartSetCustomFieldAction",
    "MyCartSetCustomShippingMethodAction",
    "MyCartSetCustomTypeAction",
    "MyCartSetDeleteDaysAfterLastModificationAction",
    "MyCartSetLineItemCustomFieldAction",
    "MyCartSetLineItemCustomTypeAction",
    "MyCartSetLineItemDistributionChannelAction",
    "MyCartSetLineItemShippingDetailsAction",
    "MyCartSetLocaleAction",
    "MyCartSetShippingAddressAction",
    "MyCartSetShippingMethodAction",
    "MyCartUpdate",
    "MyCartUpdateAction",
    "MyCartUpdateItemShippingAddressAction",
    "MyCustomer",
    "MyCustomerAddAddressAction",
    "MyCustomerAddBillingAddressIdAction",
    "MyCustomerAddShippingAddressIdAction",
    "MyCustomerChangeAddressAction",
    "MyCustomerChangeEmailAction",
    "MyCustomerDraft",
    "MyCustomerRemoveAddressAction",
    "MyCustomerRemoveBillingAddressIdAction",
    "MyCustomerRemoveShippingAddressIdAction",
    "MyCustomerSetCompanyNameAction",
    "MyCustomerSetCustomFieldAction",
    "MyCustomerSetCustomTypeAction",
    "MyCustomerSetDateOfBirthAction",
    "MyCustomerSetDefaultBillingAddressAction",
    "MyCustomerSetDefaultShippingAddressAction",
    "MyCustomerSetFirstNameAction",
    "MyCustomerSetLastNameAction",
    "MyCustomerSetLocaleAction",
    "MyCustomerSetMiddleNameAction",
    "MyCustomerSetSalutationAction",
    "MyCustomerSetTitleAction",
    "MyCustomerSetVatIdAction",
    "MyCustomerUpdate",
    "MyCustomerUpdateAction",
    "MyLineItemDraft",
    "MyOrder",
    "MyOrderFromCartDraft",
    "MyPayment",
    "MyPaymentAddTransactionAction",
    "MyPaymentChangeAmountPlannedAction",
    "MyPaymentDraft",
    "MyPaymentPagedQueryResponse",
    "MyPaymentSetCustomFieldAction",
    "MyPaymentSetMethodInfoInterfaceAction",
    "MyPaymentSetMethodInfoMethodAction",
    "MyPaymentSetMethodInfoNameAction",
    "MyPaymentUpdate",
    "MyPaymentUpdateAction",
    "MyShoppingListAddLineItemAction",
    "MyShoppingListAddTextLineItemAction",
    "MyShoppingListChangeLineItemQuantityAction",
    "MyShoppingListChangeLineItemsOrderAction",
    "MyShoppingListChangeNameAction",
    "MyShoppingListChangeTextLineItemNameAction",
    "MyShoppingListChangeTextLineItemQuantityAction",
    "MyShoppingListChangeTextLineItemsOrderAction",
    "MyShoppingListDraft",
    "MyShoppingListRemoveLineItemAction",
    "MyShoppingListRemoveTextLineItemAction",
    "MyShoppingListSetCustomFieldAction",
    "MyShoppingListSetCustomTypeAction",
    "MyShoppingListSetDeleteDaysAfterLastModificationAction",
    "MyShoppingListSetDescriptionAction",
    "MyShoppingListSetLineItemCustomFieldAction",
    "MyShoppingListSetLineItemCustomTypeAction",
    "MyShoppingListSetTextLineItemCustomFieldAction",
    "MyShoppingListSetTextLineItemCustomTypeAction",
    "MyShoppingListSetTextLineItemDescriptionAction",
    "MyShoppingListUpdate",
    "MyShoppingListUpdateAction",
    "MyTransactionDraft",
]


class MyCart(BaseResource):
    last_modified_by: typing.Optional["LastModifiedBy"]
    created_by: typing.Optional["CreatedBy"]
    customer_id: typing.Optional[str]
    customer_email: typing.Optional[str]
    anonymous_id: typing.Optional[str]
    store: typing.Optional["StoreKeyReference"]
    line_items: typing.List["LineItem"]
    custom_line_items: typing.List["CustomLineItem"]
    total_price: "TypedMoney"
    taxed_price: typing.Optional["TaxedPrice"]
    cart_state: "CartState"
    shipping_address: typing.Optional["Address"]
    billing_address: typing.Optional["Address"]
    inventory_mode: typing.Optional["InventoryMode"]
    tax_mode: "TaxMode"
    tax_rounding_mode: "RoundingMode"
    tax_calculation_mode: "TaxCalculationMode"
    customer_group: typing.Optional["CustomerGroupReference"]
    #: A two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    country: typing.Optional[str]
    shipping_info: typing.Optional["ShippingInfo"]
    discount_codes: typing.Optional[typing.List["DiscountCodeInfo"]]
    custom: typing.Optional["CustomFields"]
    payment_info: typing.Optional["PaymentInfo"]
    locale: typing.Optional[str]
    delete_days_after_last_modification: typing.Optional[int]
    refused_gifts: typing.List["CartDiscountReference"]
    origin: "CartOrigin"
    shipping_rate_input: typing.Optional["ShippingRateInput"]
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
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MyCart":
        from ._schemas.me import MyCartSchema

        return MyCartSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCartSchema

        return MyCartSchema().dump(self)


class MyCartDraft(_BaseType):
    #: A three-digit currency code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    currency: str
    customer_email: typing.Optional[str]
    #: A two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    country: typing.Optional[str]
    #: Default inventory mode is `None`.
    inventory_mode: typing.Optional["InventoryMode"]
    line_items: typing.Optional[typing.List["MyLineItemDraft"]]
    shipping_address: typing.Optional["Address"]
    billing_address: typing.Optional["Address"]
    shipping_method: typing.Optional["ShippingMethodResourceIdentifier"]
    #: The custom fields.
    custom: typing.Optional["CustomFieldsDraft"]
    locale: typing.Optional[str]
    #: The `TaxMode` `Disabled` can not be set on the My Carts endpoint.
    tax_mode: typing.Optional["TaxMode"]
    #: The cart will be deleted automatically if it hasn't been modified for the specified amount of days and it is in the `Active` CartState.
    #: If a ChangeSubscription for carts exists, a `ResourceDeleted` notification will be sent.
    delete_days_after_last_modification: typing.Optional[int]
    #: Contains addresses for orders with multiple shipping addresses.
    #: Each address must contain a key which is unique in this cart.
    item_shipping_addresses: typing.Optional[typing.List["Address"]]
    store: typing.Optional["StoreKeyReference"]
    discount_codes: typing.Optional[typing.List["DiscountCodeInfo"]]

    def __init__(
        self,
        *,
        currency: str,
        customer_email: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        inventory_mode: typing.Optional["InventoryMode"] = None,
        line_items: typing.Optional[typing.List["MyLineItemDraft"]] = None,
        shipping_address: typing.Optional["Address"] = None,
        billing_address: typing.Optional["Address"] = None,
        shipping_method: typing.Optional["ShippingMethodResourceIdentifier"] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        locale: typing.Optional[str] = None,
        tax_mode: typing.Optional["TaxMode"] = None,
        delete_days_after_last_modification: typing.Optional[int] = None,
        item_shipping_addresses: typing.Optional[typing.List["Address"]] = None,
        store: typing.Optional["StoreKeyReference"] = None,
        discount_codes: typing.Optional[typing.List["DiscountCodeInfo"]] = None
    ):
        self.currency = currency
        self.customer_email = customer_email
        self.country = country
        self.inventory_mode = inventory_mode
        self.line_items = line_items
        self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.shipping_method = shipping_method
        self.custom = custom
        self.locale = locale
        self.tax_mode = tax_mode
        self.delete_days_after_last_modification = delete_days_after_last_modification
        self.item_shipping_addresses = item_shipping_addresses
        self.store = store
        self.discount_codes = discount_codes
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MyCartDraft":
        from ._schemas.me import MyCartDraftSchema

        return MyCartDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCartDraftSchema

        return MyCartDraftSchema().dump(self)


class MyCartUpdate(_BaseType):
    version: int
    actions: typing.List["MyCartUpdateAction"]

    def __init__(self, *, version: int, actions: typing.List["MyCartUpdateAction"]):
        self.version = version
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MyCartUpdate":
        from ._schemas.me import MyCartUpdateSchema

        return MyCartUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCartUpdateSchema

        return MyCartUpdateSchema().dump(self)


class MyCartUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MyCartUpdateAction":
        if data["action"] == "addDiscountCode":
            from ._schemas.me import MyCartAddDiscountCodeActionSchema

            return MyCartAddDiscountCodeActionSchema().load(data)
        if data["action"] == "addItemShippingAddress":
            from ._schemas.me import MyCartAddItemShippingAddressActionSchema

            return MyCartAddItemShippingAddressActionSchema().load(data)
        if data["action"] == "addLineItem":
            from ._schemas.me import MyCartAddLineItemActionSchema

            return MyCartAddLineItemActionSchema().load(data)
        if data["action"] == "addPayment":
            from ._schemas.me import MyCartAddPaymentActionSchema

            return MyCartAddPaymentActionSchema().load(data)
        if data["action"] == "applyDeltaToLineItemShippingDetailsTargets":
            from ._schemas.me import (
                MyCartApplyDeltaToLineItemShippingDetailsTargetsActionSchema,
            )

            return MyCartApplyDeltaToLineItemShippingDetailsTargetsActionSchema().load(
                data
            )
        if data["action"] == "changeLineItemQuantity":
            from ._schemas.me import MyCartChangeLineItemQuantityActionSchema

            return MyCartChangeLineItemQuantityActionSchema().load(data)
        if data["action"] == "changeTaxMode":
            from ._schemas.me import MyCartChangeTaxModeActionSchema

            return MyCartChangeTaxModeActionSchema().load(data)
        if data["action"] == "recalculate":
            from ._schemas.me import MyCartRecalculateActionSchema

            return MyCartRecalculateActionSchema().load(data)
        if data["action"] == "removeDiscountCode":
            from ._schemas.me import MyCartRemoveDiscountCodeActionSchema

            return MyCartRemoveDiscountCodeActionSchema().load(data)
        if data["action"] == "removeItemShippingAddress":
            from ._schemas.me import MyCartRemoveItemShippingAddressActionSchema

            return MyCartRemoveItemShippingAddressActionSchema().load(data)
        if data["action"] == "removeLineItem":
            from ._schemas.me import MyCartRemoveLineItemActionSchema

            return MyCartRemoveLineItemActionSchema().load(data)
        if data["action"] == "removePayment":
            from ._schemas.me import MyCartRemovePaymentActionSchema

            return MyCartRemovePaymentActionSchema().load(data)
        if data["action"] == "setBillingAddress":
            from ._schemas.me import MyCartSetBillingAddressActionSchema

            return MyCartSetBillingAddressActionSchema().load(data)
        if data["action"] == "setCountry":
            from ._schemas.me import MyCartSetCountryActionSchema

            return MyCartSetCountryActionSchema().load(data)
        if data["action"] == "setCustomField":
            from ._schemas.me import MyCartSetCustomFieldActionSchema

            return MyCartSetCustomFieldActionSchema().load(data)
        if data["action"] == "setCustomShippingMethod":
            from ._schemas.me import MyCartSetCustomShippingMethodActionSchema

            return MyCartSetCustomShippingMethodActionSchema().load(data)
        if data["action"] == "setCustomType":
            from ._schemas.me import MyCartSetCustomTypeActionSchema

            return MyCartSetCustomTypeActionSchema().load(data)
        if data["action"] == "setDeleteDaysAfterLastModification":
            from ._schemas.me import (
                MyCartSetDeleteDaysAfterLastModificationActionSchema,
            )

            return MyCartSetDeleteDaysAfterLastModificationActionSchema().load(data)
        if data["action"] == "setLineItemCustomField":
            from ._schemas.me import MyCartSetLineItemCustomFieldActionSchema

            return MyCartSetLineItemCustomFieldActionSchema().load(data)
        if data["action"] == "setLineItemCustomType":
            from ._schemas.me import MyCartSetLineItemCustomTypeActionSchema

            return MyCartSetLineItemCustomTypeActionSchema().load(data)
        if data["action"] == "setLineItemDistributionChannel":
            from ._schemas.me import MyCartSetLineItemDistributionChannelActionSchema

            return MyCartSetLineItemDistributionChannelActionSchema().load(data)
        if data["action"] == "setLineItemShippingDetails":
            from ._schemas.me import MyCartSetLineItemShippingDetailsActionSchema

            return MyCartSetLineItemShippingDetailsActionSchema().load(data)
        if data["action"] == "setLocale":
            from ._schemas.me import MyCartSetLocaleActionSchema

            return MyCartSetLocaleActionSchema().load(data)
        if data["action"] == "setShippingAddress":
            from ._schemas.me import MyCartSetShippingAddressActionSchema

            return MyCartSetShippingAddressActionSchema().load(data)
        if data["action"] == "setShippingMethod":
            from ._schemas.me import MyCartSetShippingMethodActionSchema

            return MyCartSetShippingMethodActionSchema().load(data)
        if data["action"] == "updateItemShippingAddress":
            from ._schemas.me import MyCartUpdateItemShippingAddressActionSchema

            return MyCartUpdateItemShippingAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCartUpdateActionSchema

        return MyCartUpdateActionSchema().dump(self)


class MyCustomer(BaseResource):
    last_modified_by: typing.Optional["LastModifiedBy"]
    created_by: typing.Optional["CreatedBy"]
    customer_number: typing.Optional[str]
    email: str
    password: str
    first_name: typing.Optional[str]
    last_name: typing.Optional[str]
    middle_name: typing.Optional[str]
    title: typing.Optional[str]
    date_of_birth: typing.Optional[datetime.date]
    company_name: typing.Optional[str]
    vat_id: typing.Optional[str]
    addresses: typing.List["Address"]
    default_shipping_address_id: typing.Optional[str]
    shipping_address_ids: typing.Optional[typing.List["str"]]
    default_billing_address_id: typing.Optional[str]
    billing_address_ids: typing.Optional[typing.List["str"]]
    is_email_verified: bool
    external_id: typing.Optional[str]
    customer_group: typing.Optional["CustomerGroupReference"]
    custom: typing.Optional["CustomFields"]
    locale: typing.Optional[str]
    salutation: typing.Optional[str]
    key: typing.Optional[str]
    stores: typing.Optional[typing.List["StoreKeyReference"]]

    def __init__(
        self,
        *,
        id: str,
        version: int,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        customer_number: typing.Optional[str] = None,
        email: str,
        password: str,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        date_of_birth: typing.Optional[datetime.date] = None,
        company_name: typing.Optional[str] = None,
        vat_id: typing.Optional[str] = None,
        addresses: typing.List["Address"],
        default_shipping_address_id: typing.Optional[str] = None,
        shipping_address_ids: typing.Optional[typing.List["str"]] = None,
        default_billing_address_id: typing.Optional[str] = None,
        billing_address_ids: typing.Optional[typing.List["str"]] = None,
        is_email_verified: bool,
        external_id: typing.Optional[str] = None,
        customer_group: typing.Optional["CustomerGroupReference"] = None,
        custom: typing.Optional["CustomFields"] = None,
        locale: typing.Optional[str] = None,
        salutation: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        stores: typing.Optional[typing.List["StoreKeyReference"]] = None
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.customer_number = customer_number
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.title = title
        self.date_of_birth = date_of_birth
        self.company_name = company_name
        self.vat_id = vat_id
        self.addresses = addresses
        self.default_shipping_address_id = default_shipping_address_id
        self.shipping_address_ids = shipping_address_ids
        self.default_billing_address_id = default_billing_address_id
        self.billing_address_ids = billing_address_ids
        self.is_email_verified = is_email_verified
        self.external_id = external_id
        self.customer_group = customer_group
        self.custom = custom
        self.locale = locale
        self.salutation = salutation
        self.key = key
        self.stores = stores
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MyCustomer":
        from ._schemas.me import MyCustomerSchema

        return MyCustomerSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCustomerSchema

        return MyCustomerSchema().dump(self)


class MyCustomerDraft(_BaseType):
    email: str
    password: str
    first_name: typing.Optional[str]
    last_name: typing.Optional[str]
    middle_name: typing.Optional[str]
    title: typing.Optional[str]
    date_of_birth: typing.Optional[datetime.date]
    company_name: typing.Optional[str]
    vat_id: typing.Optional[str]
    #: Sets the ID of each address to be unique in the addresses list.
    addresses: typing.Optional[typing.List["Address"]]
    #: The index of the address in the addresses array.
    #: The `defaultShippingAddressId` of the customer will be set to the ID of that address.
    default_shipping_address: typing.Optional[int]
    #: The index of the address in the addresses array.
    #: The `defaultBillingAddressId` of the customer will be set to the ID of that address.
    default_billing_address: typing.Optional[int]
    #: The custom fields.
    custom: typing.Optional["CustomFields"]
    locale: typing.Optional[str]
    stores: typing.Optional[typing.List["StoreResourceIdentifier"]]

    def __init__(
        self,
        *,
        email: str,
        password: str,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        date_of_birth: typing.Optional[datetime.date] = None,
        company_name: typing.Optional[str] = None,
        vat_id: typing.Optional[str] = None,
        addresses: typing.Optional[typing.List["Address"]] = None,
        default_shipping_address: typing.Optional[int] = None,
        default_billing_address: typing.Optional[int] = None,
        custom: typing.Optional["CustomFields"] = None,
        locale: typing.Optional[str] = None,
        stores: typing.Optional[typing.List["StoreResourceIdentifier"]] = None
    ):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.title = title
        self.date_of_birth = date_of_birth
        self.company_name = company_name
        self.vat_id = vat_id
        self.addresses = addresses
        self.default_shipping_address = default_shipping_address
        self.default_billing_address = default_billing_address
        self.custom = custom
        self.locale = locale
        self.stores = stores
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MyCustomerDraft":
        from ._schemas.me import MyCustomerDraftSchema

        return MyCustomerDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCustomerDraftSchema

        return MyCustomerDraftSchema().dump(self)


class MyCustomerUpdate(_BaseType):
    version: int
    actions: typing.List["MyCustomerUpdateAction"]

    def __init__(self, *, version: int, actions: typing.List["MyCustomerUpdateAction"]):
        self.version = version
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MyCustomerUpdate":
        from ._schemas.me import MyCustomerUpdateSchema

        return MyCustomerUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCustomerUpdateSchema

        return MyCustomerUpdateSchema().dump(self)


class MyCustomerUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCustomerUpdateAction":
        if data["action"] == "addAddress":
            from ._schemas.me import MyCustomerAddAddressActionSchema

            return MyCustomerAddAddressActionSchema().load(data)
        if data["action"] == "addBillingAddressId":
            from ._schemas.me import MyCustomerAddBillingAddressIdActionSchema

            return MyCustomerAddBillingAddressIdActionSchema().load(data)
        if data["action"] == "addShippingAddressId":
            from ._schemas.me import MyCustomerAddShippingAddressIdActionSchema

            return MyCustomerAddShippingAddressIdActionSchema().load(data)
        if data["action"] == "changeAddress":
            from ._schemas.me import MyCustomerChangeAddressActionSchema

            return MyCustomerChangeAddressActionSchema().load(data)
        if data["action"] == "changeEmail":
            from ._schemas.me import MyCustomerChangeEmailActionSchema

            return MyCustomerChangeEmailActionSchema().load(data)
        if data["action"] == "removeAddress":
            from ._schemas.me import MyCustomerRemoveAddressActionSchema

            return MyCustomerRemoveAddressActionSchema().load(data)
        if data["action"] == "removeBillingAddressId":
            from ._schemas.me import MyCustomerRemoveBillingAddressIdActionSchema

            return MyCustomerRemoveBillingAddressIdActionSchema().load(data)
        if data["action"] == "removeShippingAddressId":
            from ._schemas.me import MyCustomerRemoveShippingAddressIdActionSchema

            return MyCustomerRemoveShippingAddressIdActionSchema().load(data)
        if data["action"] == "setCompanyName":
            from ._schemas.me import MyCustomerSetCompanyNameActionSchema

            return MyCustomerSetCompanyNameActionSchema().load(data)
        if data["action"] == "setCustomField":
            from ._schemas.me import MyCustomerSetCustomFieldActionSchema

            return MyCustomerSetCustomFieldActionSchema().load(data)
        if data["action"] == "setCustomType":
            from ._schemas.me import MyCustomerSetCustomTypeActionSchema

            return MyCustomerSetCustomTypeActionSchema().load(data)
        if data["action"] == "setDateOfBirth":
            from ._schemas.me import MyCustomerSetDateOfBirthActionSchema

            return MyCustomerSetDateOfBirthActionSchema().load(data)
        if data["action"] == "setDefaultBillingAddress":
            from ._schemas.me import MyCustomerSetDefaultBillingAddressActionSchema

            return MyCustomerSetDefaultBillingAddressActionSchema().load(data)
        if data["action"] == "setDefaultShippingAddress":
            from ._schemas.me import MyCustomerSetDefaultShippingAddressActionSchema

            return MyCustomerSetDefaultShippingAddressActionSchema().load(data)
        if data["action"] == "setFirstName":
            from ._schemas.me import MyCustomerSetFirstNameActionSchema

            return MyCustomerSetFirstNameActionSchema().load(data)
        if data["action"] == "setLastName":
            from ._schemas.me import MyCustomerSetLastNameActionSchema

            return MyCustomerSetLastNameActionSchema().load(data)
        if data["action"] == "setLocale":
            from ._schemas.me import MyCustomerSetLocaleActionSchema

            return MyCustomerSetLocaleActionSchema().load(data)
        if data["action"] == "setMiddleName":
            from ._schemas.me import MyCustomerSetMiddleNameActionSchema

            return MyCustomerSetMiddleNameActionSchema().load(data)
        if data["action"] == "setSalutation":
            from ._schemas.me import MyCustomerSetSalutationActionSchema

            return MyCustomerSetSalutationActionSchema().load(data)
        if data["action"] == "setTitle":
            from ._schemas.me import MyCustomerSetTitleActionSchema

            return MyCustomerSetTitleActionSchema().load(data)
        if data["action"] == "setVatId":
            from ._schemas.me import MyCustomerSetVatIdActionSchema

            return MyCustomerSetVatIdActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCustomerUpdateActionSchema

        return MyCustomerUpdateActionSchema().dump(self)


class MyLineItemDraft(_BaseType):
    product_id: str
    variant_id: int
    quantity: float
    #: When the line item was added to the cart. Optional for backwards
    #: compatibility reasons only.
    added_at: typing.Optional[datetime.datetime]
    #: By providing supply channel information, you can unique identify
    #: inventory entries that should be reserved.
    #: The provided channel should have the InventorySupply role.
    supply_channel: typing.Optional["ChannelResourceIdentifier"]
    #: The channel is used to select a ProductPrice.
    #: The provided channel should have the ProductDistribution role.
    distribution_channel: typing.Optional["ChannelResourceIdentifier"]
    #: The custom fields.
    custom: typing.Optional["CustomFieldsDraft"]
    #: Container for line item specific address(es).
    shipping_details: typing.Optional["ItemShippingDetailsDraft"]
    sku: typing.Optional[str]

    def __init__(
        self,
        *,
        product_id: str,
        variant_id: int,
        quantity: float,
        added_at: typing.Optional[datetime.datetime] = None,
        supply_channel: typing.Optional["ChannelResourceIdentifier"] = None,
        distribution_channel: typing.Optional["ChannelResourceIdentifier"] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        shipping_details: typing.Optional["ItemShippingDetailsDraft"] = None,
        sku: typing.Optional[str] = None
    ):
        self.product_id = product_id
        self.variant_id = variant_id
        self.quantity = quantity
        self.added_at = added_at
        self.supply_channel = supply_channel
        self.distribution_channel = distribution_channel
        self.custom = custom
        self.shipping_details = shipping_details
        self.sku = sku
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MyLineItemDraft":
        from ._schemas.me import MyLineItemDraftSchema

        return MyLineItemDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyLineItemDraftSchema

        return MyLineItemDraftSchema().dump(self)


class MyOrder(BaseResource):
    last_modified_by: typing.Optional["LastModifiedBy"]
    created_by: typing.Optional["CreatedBy"]
    completed_at: typing.Optional[datetime.datetime]
    order_number: typing.Optional[str]
    customer_id: typing.Optional[str]
    customer_email: typing.Optional[str]
    anonymous_id: typing.Optional[str]
    store: typing.Optional["StoreKeyReference"]
    line_items: typing.List["LineItem"]
    custom_line_items: typing.List["CustomLineItem"]
    total_price: "TypedMoney"
    taxed_price: typing.Optional["TaxedPrice"]
    shipping_address: typing.Optional["Address"]
    billing_address: typing.Optional["Address"]
    tax_mode: typing.Optional["TaxMode"]
    tax_rounding_mode: typing.Optional["RoundingMode"]
    customer_group: typing.Optional["CustomerGroupReference"]
    country: typing.Optional[str]
    order_state: "OrderState"
    state: typing.Optional["StateReference"]
    shipment_state: typing.Optional["ShipmentState"]
    payment_state: typing.Optional["PaymentState"]
    shipping_info: typing.Optional["ShippingInfo"]
    sync_info: typing.List["SyncInfo"]
    return_info: typing.Optional[typing.List["ReturnInfo"]]
    discount_codes: typing.Optional[typing.List["DiscountCodeInfo"]]
    last_message_sequence_number: int
    cart: typing.Optional["CartReference"]
    custom: typing.Optional["CustomFields"]
    payment_info: typing.Optional["PaymentInfo"]
    locale: typing.Optional[str]
    inventory_mode: typing.Optional["InventoryMode"]
    origin: "CartOrigin"
    tax_calculation_mode: typing.Optional["TaxCalculationMode"]
    shipping_rate_input: typing.Optional["ShippingRateInput"]
    item_shipping_addresses: typing.Optional[typing.List["Address"]]
    refused_gifts: typing.List["CartDiscountReference"]

    def __init__(
        self,
        *,
        id: str,
        version: int,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        completed_at: typing.Optional[datetime.datetime] = None,
        order_number: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        customer_email: typing.Optional[str] = None,
        anonymous_id: typing.Optional[str] = None,
        store: typing.Optional["StoreKeyReference"] = None,
        line_items: typing.List["LineItem"],
        custom_line_items: typing.List["CustomLineItem"],
        total_price: "TypedMoney",
        taxed_price: typing.Optional["TaxedPrice"] = None,
        shipping_address: typing.Optional["Address"] = None,
        billing_address: typing.Optional["Address"] = None,
        tax_mode: typing.Optional["TaxMode"] = None,
        tax_rounding_mode: typing.Optional["RoundingMode"] = None,
        customer_group: typing.Optional["CustomerGroupReference"] = None,
        country: typing.Optional[str] = None,
        order_state: "OrderState",
        state: typing.Optional["StateReference"] = None,
        shipment_state: typing.Optional["ShipmentState"] = None,
        payment_state: typing.Optional["PaymentState"] = None,
        shipping_info: typing.Optional["ShippingInfo"] = None,
        sync_info: typing.List["SyncInfo"],
        return_info: typing.Optional[typing.List["ReturnInfo"]] = None,
        discount_codes: typing.Optional[typing.List["DiscountCodeInfo"]] = None,
        last_message_sequence_number: int,
        cart: typing.Optional["CartReference"] = None,
        custom: typing.Optional["CustomFields"] = None,
        payment_info: typing.Optional["PaymentInfo"] = None,
        locale: typing.Optional[str] = None,
        inventory_mode: typing.Optional["InventoryMode"] = None,
        origin: "CartOrigin",
        tax_calculation_mode: typing.Optional["TaxCalculationMode"] = None,
        shipping_rate_input: typing.Optional["ShippingRateInput"] = None,
        item_shipping_addresses: typing.Optional[typing.List["Address"]] = None,
        refused_gifts: typing.List["CartDiscountReference"]
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.completed_at = completed_at
        self.order_number = order_number
        self.customer_id = customer_id
        self.customer_email = customer_email
        self.anonymous_id = anonymous_id
        self.store = store
        self.line_items = line_items
        self.custom_line_items = custom_line_items
        self.total_price = total_price
        self.taxed_price = taxed_price
        self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.tax_mode = tax_mode
        self.tax_rounding_mode = tax_rounding_mode
        self.customer_group = customer_group
        self.country = country
        self.order_state = order_state
        self.state = state
        self.shipment_state = shipment_state
        self.payment_state = payment_state
        self.shipping_info = shipping_info
        self.sync_info = sync_info
        self.return_info = return_info
        self.discount_codes = discount_codes
        self.last_message_sequence_number = last_message_sequence_number
        self.cart = cart
        self.custom = custom
        self.payment_info = payment_info
        self.locale = locale
        self.inventory_mode = inventory_mode
        self.origin = origin
        self.tax_calculation_mode = tax_calculation_mode
        self.shipping_rate_input = shipping_rate_input
        self.item_shipping_addresses = item_shipping_addresses
        self.refused_gifts = refused_gifts
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MyOrder":
        from ._schemas.me import MyOrderSchema

        return MyOrderSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyOrderSchema

        return MyOrderSchema().dump(self)


class MyOrderFromCartDraft(_BaseType):
    #: The unique ID of the cart from which an order is created.
    id: str
    version: int

    def __init__(self, *, id: str, version: int):
        self.id = id
        self.version = version
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MyOrderFromCartDraft":
        from ._schemas.me import MyOrderFromCartDraftSchema

        return MyOrderFromCartDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyOrderFromCartDraftSchema

        return MyOrderFromCartDraftSchema().dump(self)


class MyPayment(_BaseType):
    id: str
    version: int
    #: A reference to the customer this payment belongs to.
    customer: typing.Optional["CustomerReference"]
    #: Identifies payments belonging to an anonymous session (the customer has not signed up/in yet).
    anonymous_id: typing.Optional[str]
    #: How much money this payment intends to receive from the customer.
    #: The value usually matches the cart or order gross total.
    amount_planned: "TypedMoney"
    payment_method_info: "PaymentMethodInfo"
    #: A list of financial transactions of different TransactionTypes
    #: with different TransactionStates.
    transactions: typing.List["Transaction"]
    custom: typing.Optional["CustomFields"]

    def __init__(
        self,
        *,
        id: str,
        version: int,
        customer: typing.Optional["CustomerReference"] = None,
        anonymous_id: typing.Optional[str] = None,
        amount_planned: "TypedMoney",
        payment_method_info: "PaymentMethodInfo",
        transactions: typing.List["Transaction"],
        custom: typing.Optional["CustomFields"] = None
    ):
        self.id = id
        self.version = version
        self.customer = customer
        self.anonymous_id = anonymous_id
        self.amount_planned = amount_planned
        self.payment_method_info = payment_method_info
        self.transactions = transactions
        self.custom = custom
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MyPayment":
        from ._schemas.me import MyPaymentSchema

        return MyPaymentSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyPaymentSchema

        return MyPaymentSchema().dump(self)


class MyPaymentDraft(_BaseType):
    #: How much money this payment intends to receive from the customer.
    #: The value usually matches the cart or order gross total.
    amount_planned: "Money"
    payment_method_info: typing.Optional["PaymentMethodInfo"]
    custom: typing.Optional["CustomFieldsDraft"]
    #: A list of financial transactions of the `Authorization` or `Charge`
    #: TransactionTypes.
    transaction: typing.Optional["MyTransactionDraft"]

    def __init__(
        self,
        *,
        amount_planned: "Money",
        payment_method_info: typing.Optional["PaymentMethodInfo"] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        transaction: typing.Optional["MyTransactionDraft"] = None
    ):
        self.amount_planned = amount_planned
        self.payment_method_info = payment_method_info
        self.custom = custom
        self.transaction = transaction
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MyPaymentDraft":
        from ._schemas.me import MyPaymentDraftSchema

        return MyPaymentDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyPaymentDraftSchema

        return MyPaymentDraftSchema().dump(self)


class MyPaymentPagedQueryResponse(_BaseType):
    limit: int
    count: int
    total: typing.Optional[int]
    offset: int
    results: typing.List["MyPayment"]

    def __init__(
        self,
        *,
        limit: int,
        count: int,
        total: typing.Optional[int] = None,
        offset: int,
        results: typing.List["MyPayment"]
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
    ) -> "MyPaymentPagedQueryResponse":
        from ._schemas.me import MyPaymentPagedQueryResponseSchema

        return MyPaymentPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyPaymentPagedQueryResponseSchema

        return MyPaymentPagedQueryResponseSchema().dump(self)


class MyPaymentUpdate(_BaseType):
    version: int
    actions: typing.List["MyPaymentUpdateAction"]

    def __init__(self, *, version: int, actions: typing.List["MyPaymentUpdateAction"]):
        self.version = version
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MyPaymentUpdate":
        from ._schemas.me import MyPaymentUpdateSchema

        return MyPaymentUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyPaymentUpdateSchema

        return MyPaymentUpdateSchema().dump(self)


class MyPaymentUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MyPaymentUpdateAction":
        if data["action"] == "addTransaction":
            from ._schemas.me import MyPaymentAddTransactionActionSchema

            return MyPaymentAddTransactionActionSchema().load(data)
        if data["action"] == "changeAmountPlanned":
            from ._schemas.me import MyPaymentChangeAmountPlannedActionSchema

            return MyPaymentChangeAmountPlannedActionSchema().load(data)
        if data["action"] == "setCustomField":
            from ._schemas.me import MyPaymentSetCustomFieldActionSchema

            return MyPaymentSetCustomFieldActionSchema().load(data)
        if data["action"] == "setMethodInfoInterface":
            from ._schemas.me import MyPaymentSetMethodInfoInterfaceActionSchema

            return MyPaymentSetMethodInfoInterfaceActionSchema().load(data)
        if data["action"] == "setMethodInfoMethod":
            from ._schemas.me import MyPaymentSetMethodInfoMethodActionSchema

            return MyPaymentSetMethodInfoMethodActionSchema().load(data)
        if data["action"] == "setMethodInfoName":
            from ._schemas.me import MyPaymentSetMethodInfoNameActionSchema

            return MyPaymentSetMethodInfoNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyPaymentUpdateActionSchema

        return MyPaymentUpdateActionSchema().dump(self)


class MyShoppingListDraft(_BaseType):
    name: "LocalizedString"
    description: typing.Optional["LocalizedString"]
    line_items: typing.Optional[typing.List["ShoppingListLineItemDraft"]]
    text_line_items: typing.Optional[typing.List["TextLineItemDraft"]]
    #: The custom fields.
    custom: typing.Optional["CustomFieldsDraft"]
    #: The shopping list will be deleted automatically if it hasn't been modified for the specified amount of days.
    delete_days_after_last_modification: typing.Optional[int]

    def __init__(
        self,
        *,
        name: "LocalizedString",
        description: typing.Optional["LocalizedString"] = None,
        line_items: typing.Optional[typing.List["ShoppingListLineItemDraft"]] = None,
        text_line_items: typing.Optional[typing.List["TextLineItemDraft"]] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        delete_days_after_last_modification: typing.Optional[int] = None
    ):
        self.name = name
        self.description = description
        self.line_items = line_items
        self.text_line_items = text_line_items
        self.custom = custom
        self.delete_days_after_last_modification = delete_days_after_last_modification
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MyShoppingListDraft":
        from ._schemas.me import MyShoppingListDraftSchema

        return MyShoppingListDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyShoppingListDraftSchema

        return MyShoppingListDraftSchema().dump(self)


class MyShoppingListUpdate(_BaseType):
    version: int
    actions: typing.List["MyShoppingListUpdateAction"]

    def __init__(
        self, *, version: int, actions: typing.List["MyShoppingListUpdateAction"]
    ):
        self.version = version
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MyShoppingListUpdate":
        from ._schemas.me import MyShoppingListUpdateSchema

        return MyShoppingListUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyShoppingListUpdateSchema

        return MyShoppingListUpdateSchema().dump(self)


class MyShoppingListUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyShoppingListUpdateAction":
        if data["action"] == "addLineItem":
            from ._schemas.me import MyShoppingListAddLineItemActionSchema

            return MyShoppingListAddLineItemActionSchema().load(data)
        if data["action"] == "addTextLineItem":
            from ._schemas.me import MyShoppingListAddTextLineItemActionSchema

            return MyShoppingListAddTextLineItemActionSchema().load(data)
        if data["action"] == "changeLineItemQuantity":
            from ._schemas.me import MyShoppingListChangeLineItemQuantityActionSchema

            return MyShoppingListChangeLineItemQuantityActionSchema().load(data)
        if data["action"] == "changeLineItemsOrder":
            from ._schemas.me import MyShoppingListChangeLineItemsOrderActionSchema

            return MyShoppingListChangeLineItemsOrderActionSchema().load(data)
        if data["action"] == "changeName":
            from ._schemas.me import MyShoppingListChangeNameActionSchema

            return MyShoppingListChangeNameActionSchema().load(data)
        if data["action"] == "changeTextLineItemName":
            from ._schemas.me import MyShoppingListChangeTextLineItemNameActionSchema

            return MyShoppingListChangeTextLineItemNameActionSchema().load(data)
        if data["action"] == "changeTextLineItemQuantity":
            from ._schemas.me import (
                MyShoppingListChangeTextLineItemQuantityActionSchema,
            )

            return MyShoppingListChangeTextLineItemQuantityActionSchema().load(data)
        if data["action"] == "changeTextLineItemsOrder":
            from ._schemas.me import MyShoppingListChangeTextLineItemsOrderActionSchema

            return MyShoppingListChangeTextLineItemsOrderActionSchema().load(data)
        if data["action"] == "removeLineItem":
            from ._schemas.me import MyShoppingListRemoveLineItemActionSchema

            return MyShoppingListRemoveLineItemActionSchema().load(data)
        if data["action"] == "removeTextLineItem":
            from ._schemas.me import MyShoppingListRemoveTextLineItemActionSchema

            return MyShoppingListRemoveTextLineItemActionSchema().load(data)
        if data["action"] == "setCustomField":
            from ._schemas.me import MyShoppingListSetCustomFieldActionSchema

            return MyShoppingListSetCustomFieldActionSchema().load(data)
        if data["action"] == "setCustomType":
            from ._schemas.me import MyShoppingListSetCustomTypeActionSchema

            return MyShoppingListSetCustomTypeActionSchema().load(data)
        if data["action"] == "setDeleteDaysAfterLastModification":
            from ._schemas.me import (
                MyShoppingListSetDeleteDaysAfterLastModificationActionSchema,
            )

            return MyShoppingListSetDeleteDaysAfterLastModificationActionSchema().load(
                data
            )
        if data["action"] == "setDescription":
            from ._schemas.me import MyShoppingListSetDescriptionActionSchema

            return MyShoppingListSetDescriptionActionSchema().load(data)
        if data["action"] == "setLineItemCustomField":
            from ._schemas.me import MyShoppingListSetLineItemCustomFieldActionSchema

            return MyShoppingListSetLineItemCustomFieldActionSchema().load(data)
        if data["action"] == "setLineItemCustomType":
            from ._schemas.me import MyShoppingListSetLineItemCustomTypeActionSchema

            return MyShoppingListSetLineItemCustomTypeActionSchema().load(data)
        if data["action"] == "setTextLineItemCustomField":
            from ._schemas.me import (
                MyShoppingListSetTextLineItemCustomFieldActionSchema,
            )

            return MyShoppingListSetTextLineItemCustomFieldActionSchema().load(data)
        if data["action"] == "setTextLineItemCustomType":
            from ._schemas.me import MyShoppingListSetTextLineItemCustomTypeActionSchema

            return MyShoppingListSetTextLineItemCustomTypeActionSchema().load(data)
        if data["action"] == "setTextLineItemDescription":
            from ._schemas.me import (
                MyShoppingListSetTextLineItemDescriptionActionSchema,
            )

            return MyShoppingListSetTextLineItemDescriptionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyShoppingListUpdateActionSchema

        return MyShoppingListUpdateActionSchema().dump(self)


class MyTransactionDraft(_BaseType):
    #: The time at which the transaction took place.
    timestamp: typing.Optional[datetime.datetime]
    #: The type of this transaction.
    #: Only the `Authorization` or `Charge`
    #: TransactionTypes are allowed here.
    type: "TransactionType"
    amount: "Money"
    #: The identifier that is used by the interface that managed the transaction (usually the PSP).
    #: If a matching interaction was logged in the interfaceInteractions array,
    #: the corresponding interaction should be findable with this ID.
    #: The `state` is set to the `Initial` TransactionState.
    interaction_id: typing.Optional[str]

    def __init__(
        self,
        *,
        timestamp: typing.Optional[datetime.datetime] = None,
        type: "TransactionType",
        amount: "Money",
        interaction_id: typing.Optional[str] = None
    ):
        self.timestamp = timestamp
        self.type = type
        self.amount = amount
        self.interaction_id = interaction_id
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MyTransactionDraft":
        from ._schemas.me import MyTransactionDraftSchema

        return MyTransactionDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyTransactionDraftSchema

        return MyTransactionDraftSchema().dump(self)


class MyCartAddDiscountCodeAction(MyCartUpdateAction):
    code: str

    def __init__(self, *, code: str):
        self.code = code
        super().__init__(action="addDiscountCode")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCartAddDiscountCodeAction":
        from ._schemas.me import MyCartAddDiscountCodeActionSchema

        return MyCartAddDiscountCodeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCartAddDiscountCodeActionSchema

        return MyCartAddDiscountCodeActionSchema().dump(self)


class MyCartAddItemShippingAddressAction(MyCartUpdateAction):
    address: "Address"

    def __init__(self, *, address: "Address"):
        self.address = address
        super().__init__(action="addItemShippingAddress")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCartAddItemShippingAddressAction":
        from ._schemas.me import MyCartAddItemShippingAddressActionSchema

        return MyCartAddItemShippingAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCartAddItemShippingAddressActionSchema

        return MyCartAddItemShippingAddressActionSchema().dump(self)


class MyCartAddLineItemAction(MyCartUpdateAction):
    custom: typing.Optional["CustomFieldsDraft"]
    distribution_channel: typing.Optional["ChannelResourceIdentifier"]
    external_tax_rate: typing.Optional["ExternalTaxRateDraft"]
    product_id: typing.Optional[str]
    variant_id: typing.Optional[int]
    sku: typing.Optional[str]
    quantity: typing.Optional[float]
    supply_channel: typing.Optional["ChannelResourceIdentifier"]
    external_price: typing.Optional["Money"]
    external_total_price: typing.Optional["ExternalLineItemTotalPrice"]
    shipping_details: typing.Optional["ItemShippingDetailsDraft"]
    added_at: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        distribution_channel: typing.Optional["ChannelResourceIdentifier"] = None,
        external_tax_rate: typing.Optional["ExternalTaxRateDraft"] = None,
        product_id: typing.Optional[str] = None,
        variant_id: typing.Optional[int] = None,
        sku: typing.Optional[str] = None,
        quantity: typing.Optional[float] = None,
        supply_channel: typing.Optional["ChannelResourceIdentifier"] = None,
        external_price: typing.Optional["Money"] = None,
        external_total_price: typing.Optional["ExternalLineItemTotalPrice"] = None,
        shipping_details: typing.Optional["ItemShippingDetailsDraft"] = None,
        added_at: typing.Optional[datetime.datetime] = None
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
        self.added_at = added_at
        super().__init__(action="addLineItem")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCartAddLineItemAction":
        from ._schemas.me import MyCartAddLineItemActionSchema

        return MyCartAddLineItemActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCartAddLineItemActionSchema

        return MyCartAddLineItemActionSchema().dump(self)


class MyCartAddPaymentAction(MyCartUpdateAction):
    payment: "PaymentResourceIdentifier"

    def __init__(self, *, payment: "PaymentResourceIdentifier"):
        self.payment = payment
        super().__init__(action="addPayment")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCartAddPaymentAction":
        from ._schemas.me import MyCartAddPaymentActionSchema

        return MyCartAddPaymentActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCartAddPaymentActionSchema

        return MyCartAddPaymentActionSchema().dump(self)


class MyCartApplyDeltaToLineItemShippingDetailsTargetsAction(MyCartUpdateAction):
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
    ) -> "MyCartApplyDeltaToLineItemShippingDetailsTargetsAction":
        from ._schemas.me import (
            MyCartApplyDeltaToLineItemShippingDetailsTargetsActionSchema,
        )

        return MyCartApplyDeltaToLineItemShippingDetailsTargetsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import (
            MyCartApplyDeltaToLineItemShippingDetailsTargetsActionSchema,
        )

        return MyCartApplyDeltaToLineItemShippingDetailsTargetsActionSchema().dump(self)


class MyCartChangeLineItemQuantityAction(MyCartUpdateAction):
    line_item_id: str
    quantity: float
    external_price: typing.Optional["Money"]
    external_total_price: typing.Optional["ExternalLineItemTotalPrice"]

    def __init__(
        self,
        *,
        line_item_id: str,
        quantity: float,
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
    ) -> "MyCartChangeLineItemQuantityAction":
        from ._schemas.me import MyCartChangeLineItemQuantityActionSchema

        return MyCartChangeLineItemQuantityActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCartChangeLineItemQuantityActionSchema

        return MyCartChangeLineItemQuantityActionSchema().dump(self)


class MyCartChangeTaxModeAction(MyCartUpdateAction):
    tax_mode: "TaxMode"

    def __init__(self, *, tax_mode: "TaxMode"):
        self.tax_mode = tax_mode
        super().__init__(action="changeTaxMode")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCartChangeTaxModeAction":
        from ._schemas.me import MyCartChangeTaxModeActionSchema

        return MyCartChangeTaxModeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCartChangeTaxModeActionSchema

        return MyCartChangeTaxModeActionSchema().dump(self)


class MyCartRecalculateAction(MyCartUpdateAction):
    update_product_data: typing.Optional[bool]

    def __init__(self, *, update_product_data: typing.Optional[bool] = None):
        self.update_product_data = update_product_data
        super().__init__(action="recalculate")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCartRecalculateAction":
        from ._schemas.me import MyCartRecalculateActionSchema

        return MyCartRecalculateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCartRecalculateActionSchema

        return MyCartRecalculateActionSchema().dump(self)


class MyCartRemoveDiscountCodeAction(MyCartUpdateAction):
    discount_code: "DiscountCodeReference"

    def __init__(self, *, discount_code: "DiscountCodeReference"):
        self.discount_code = discount_code
        super().__init__(action="removeDiscountCode")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCartRemoveDiscountCodeAction":
        from ._schemas.me import MyCartRemoveDiscountCodeActionSchema

        return MyCartRemoveDiscountCodeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCartRemoveDiscountCodeActionSchema

        return MyCartRemoveDiscountCodeActionSchema().dump(self)


class MyCartRemoveItemShippingAddressAction(MyCartUpdateAction):
    address_key: str

    def __init__(self, *, address_key: str):
        self.address_key = address_key
        super().__init__(action="removeItemShippingAddress")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCartRemoveItemShippingAddressAction":
        from ._schemas.me import MyCartRemoveItemShippingAddressActionSchema

        return MyCartRemoveItemShippingAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCartRemoveItemShippingAddressActionSchema

        return MyCartRemoveItemShippingAddressActionSchema().dump(self)


class MyCartRemoveLineItemAction(MyCartUpdateAction):
    line_item_id: str
    quantity: typing.Optional[float]
    external_price: typing.Optional["Money"]
    external_total_price: typing.Optional["ExternalLineItemTotalPrice"]
    shipping_details_to_remove: typing.Optional["ItemShippingDetailsDraft"]

    def __init__(
        self,
        *,
        line_item_id: str,
        quantity: typing.Optional[float] = None,
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
    ) -> "MyCartRemoveLineItemAction":
        from ._schemas.me import MyCartRemoveLineItemActionSchema

        return MyCartRemoveLineItemActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCartRemoveLineItemActionSchema

        return MyCartRemoveLineItemActionSchema().dump(self)


class MyCartRemovePaymentAction(MyCartUpdateAction):
    payment: "PaymentResourceIdentifier"

    def __init__(self, *, payment: "PaymentResourceIdentifier"):
        self.payment = payment
        super().__init__(action="removePayment")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCartRemovePaymentAction":
        from ._schemas.me import MyCartRemovePaymentActionSchema

        return MyCartRemovePaymentActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCartRemovePaymentActionSchema

        return MyCartRemovePaymentActionSchema().dump(self)


class MyCartSetBillingAddressAction(MyCartUpdateAction):
    address: typing.Optional["Address"]

    def __init__(self, *, address: typing.Optional["Address"] = None):
        self.address = address
        super().__init__(action="setBillingAddress")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCartSetBillingAddressAction":
        from ._schemas.me import MyCartSetBillingAddressActionSchema

        return MyCartSetBillingAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCartSetBillingAddressActionSchema

        return MyCartSetBillingAddressActionSchema().dump(self)


class MyCartSetCountryAction(MyCartUpdateAction):
    #: A two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    country: typing.Optional[str]

    def __init__(self, *, country: typing.Optional[str] = None):
        self.country = country
        super().__init__(action="setCountry")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCartSetCountryAction":
        from ._schemas.me import MyCartSetCountryActionSchema

        return MyCartSetCountryActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCartSetCountryActionSchema

        return MyCartSetCountryActionSchema().dump(self)


class MyCartSetCustomFieldAction(MyCartUpdateAction):
    name: str
    value: typing.Optional[typing.Any]

    def __init__(self, *, name: str, value: typing.Optional[typing.Any] = None):
        self.name = name
        self.value = value
        super().__init__(action="setCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCartSetCustomFieldAction":
        from ._schemas.me import MyCartSetCustomFieldActionSchema

        return MyCartSetCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCartSetCustomFieldActionSchema

        return MyCartSetCustomFieldActionSchema().dump(self)


class MyCartSetCustomShippingMethodAction(MyCartUpdateAction):
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
    ) -> "MyCartSetCustomShippingMethodAction":
        from ._schemas.me import MyCartSetCustomShippingMethodActionSchema

        return MyCartSetCustomShippingMethodActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCartSetCustomShippingMethodActionSchema

        return MyCartSetCustomShippingMethodActionSchema().dump(self)


class MyCartSetCustomTypeAction(MyCartUpdateAction):
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
    ) -> "MyCartSetCustomTypeAction":
        from ._schemas.me import MyCartSetCustomTypeActionSchema

        return MyCartSetCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCartSetCustomTypeActionSchema

        return MyCartSetCustomTypeActionSchema().dump(self)


class MyCartSetDeleteDaysAfterLastModificationAction(MyCartUpdateAction):
    delete_days_after_last_modification: typing.Optional[int]

    def __init__(
        self, *, delete_days_after_last_modification: typing.Optional[int] = None
    ):
        self.delete_days_after_last_modification = delete_days_after_last_modification
        super().__init__(action="setDeleteDaysAfterLastModification")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCartSetDeleteDaysAfterLastModificationAction":
        from ._schemas.me import MyCartSetDeleteDaysAfterLastModificationActionSchema

        return MyCartSetDeleteDaysAfterLastModificationActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCartSetDeleteDaysAfterLastModificationActionSchema

        return MyCartSetDeleteDaysAfterLastModificationActionSchema().dump(self)


class MyCartSetLineItemCustomFieldAction(MyCartUpdateAction):
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
    ) -> "MyCartSetLineItemCustomFieldAction":
        from ._schemas.me import MyCartSetLineItemCustomFieldActionSchema

        return MyCartSetLineItemCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCartSetLineItemCustomFieldActionSchema

        return MyCartSetLineItemCustomFieldActionSchema().dump(self)


class MyCartSetLineItemCustomTypeAction(MyCartUpdateAction):
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
    ) -> "MyCartSetLineItemCustomTypeAction":
        from ._schemas.me import MyCartSetLineItemCustomTypeActionSchema

        return MyCartSetLineItemCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCartSetLineItemCustomTypeActionSchema

        return MyCartSetLineItemCustomTypeActionSchema().dump(self)


class MyCartSetLineItemDistributionChannelAction(MyCartUpdateAction):
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
    ) -> "MyCartSetLineItemDistributionChannelAction":
        from ._schemas.me import MyCartSetLineItemDistributionChannelActionSchema

        return MyCartSetLineItemDistributionChannelActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCartSetLineItemDistributionChannelActionSchema

        return MyCartSetLineItemDistributionChannelActionSchema().dump(self)


class MyCartSetLineItemShippingDetailsAction(MyCartUpdateAction):
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
    ) -> "MyCartSetLineItemShippingDetailsAction":
        from ._schemas.me import MyCartSetLineItemShippingDetailsActionSchema

        return MyCartSetLineItemShippingDetailsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCartSetLineItemShippingDetailsActionSchema

        return MyCartSetLineItemShippingDetailsActionSchema().dump(self)


class MyCartSetLocaleAction(MyCartUpdateAction):
    locale: typing.Optional[str]

    def __init__(self, *, locale: typing.Optional[str] = None):
        self.locale = locale
        super().__init__(action="setLocale")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MyCartSetLocaleAction":
        from ._schemas.me import MyCartSetLocaleActionSchema

        return MyCartSetLocaleActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCartSetLocaleActionSchema

        return MyCartSetLocaleActionSchema().dump(self)


class MyCartSetShippingAddressAction(MyCartUpdateAction):
    address: typing.Optional["Address"]

    def __init__(self, *, address: typing.Optional["Address"] = None):
        self.address = address
        super().__init__(action="setShippingAddress")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCartSetShippingAddressAction":
        from ._schemas.me import MyCartSetShippingAddressActionSchema

        return MyCartSetShippingAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCartSetShippingAddressActionSchema

        return MyCartSetShippingAddressActionSchema().dump(self)


class MyCartSetShippingMethodAction(MyCartUpdateAction):
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
    ) -> "MyCartSetShippingMethodAction":
        from ._schemas.me import MyCartSetShippingMethodActionSchema

        return MyCartSetShippingMethodActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCartSetShippingMethodActionSchema

        return MyCartSetShippingMethodActionSchema().dump(self)


class MyCartUpdateItemShippingAddressAction(MyCartUpdateAction):
    address: "Address"

    def __init__(self, *, address: "Address"):
        self.address = address
        super().__init__(action="updateItemShippingAddress")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCartUpdateItemShippingAddressAction":
        from ._schemas.me import MyCartUpdateItemShippingAddressActionSchema

        return MyCartUpdateItemShippingAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCartUpdateItemShippingAddressActionSchema

        return MyCartUpdateItemShippingAddressActionSchema().dump(self)


class MyCustomerAddAddressAction(MyCustomerUpdateAction):
    address: "Address"

    def __init__(self, *, address: "Address"):
        self.address = address
        super().__init__(action="addAddress")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCustomerAddAddressAction":
        from ._schemas.me import MyCustomerAddAddressActionSchema

        return MyCustomerAddAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCustomerAddAddressActionSchema

        return MyCustomerAddAddressActionSchema().dump(self)


class MyCustomerAddBillingAddressIdAction(MyCustomerUpdateAction):
    address_id: typing.Optional[str]
    address_key: typing.Optional[str]

    def __init__(
        self,
        *,
        address_id: typing.Optional[str] = None,
        address_key: typing.Optional[str] = None
    ):
        self.address_id = address_id
        self.address_key = address_key
        super().__init__(action="addBillingAddressId")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCustomerAddBillingAddressIdAction":
        from ._schemas.me import MyCustomerAddBillingAddressIdActionSchema

        return MyCustomerAddBillingAddressIdActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCustomerAddBillingAddressIdActionSchema

        return MyCustomerAddBillingAddressIdActionSchema().dump(self)


class MyCustomerAddShippingAddressIdAction(MyCustomerUpdateAction):
    address_id: typing.Optional[str]
    address_key: typing.Optional[str]

    def __init__(
        self,
        *,
        address_id: typing.Optional[str] = None,
        address_key: typing.Optional[str] = None
    ):
        self.address_id = address_id
        self.address_key = address_key
        super().__init__(action="addShippingAddressId")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCustomerAddShippingAddressIdAction":
        from ._schemas.me import MyCustomerAddShippingAddressIdActionSchema

        return MyCustomerAddShippingAddressIdActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCustomerAddShippingAddressIdActionSchema

        return MyCustomerAddShippingAddressIdActionSchema().dump(self)


class MyCustomerChangeAddressAction(MyCustomerUpdateAction):
    address_id: typing.Optional[str]
    address_key: typing.Optional[str]
    address: "Address"

    def __init__(
        self,
        *,
        address_id: typing.Optional[str] = None,
        address_key: typing.Optional[str] = None,
        address: "Address"
    ):
        self.address_id = address_id
        self.address_key = address_key
        self.address = address
        super().__init__(action="changeAddress")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCustomerChangeAddressAction":
        from ._schemas.me import MyCustomerChangeAddressActionSchema

        return MyCustomerChangeAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCustomerChangeAddressActionSchema

        return MyCustomerChangeAddressActionSchema().dump(self)


class MyCustomerChangeEmailAction(MyCustomerUpdateAction):
    email: str

    def __init__(self, *, email: str):
        self.email = email
        super().__init__(action="changeEmail")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCustomerChangeEmailAction":
        from ._schemas.me import MyCustomerChangeEmailActionSchema

        return MyCustomerChangeEmailActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCustomerChangeEmailActionSchema

        return MyCustomerChangeEmailActionSchema().dump(self)


class MyCustomerRemoveAddressAction(MyCustomerUpdateAction):
    address_id: typing.Optional[str]
    address_key: typing.Optional[str]

    def __init__(
        self,
        *,
        address_id: typing.Optional[str] = None,
        address_key: typing.Optional[str] = None
    ):
        self.address_id = address_id
        self.address_key = address_key
        super().__init__(action="removeAddress")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCustomerRemoveAddressAction":
        from ._schemas.me import MyCustomerRemoveAddressActionSchema

        return MyCustomerRemoveAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCustomerRemoveAddressActionSchema

        return MyCustomerRemoveAddressActionSchema().dump(self)


class MyCustomerRemoveBillingAddressIdAction(MyCustomerUpdateAction):
    address_id: typing.Optional[str]
    address_key: typing.Optional[str]

    def __init__(
        self,
        *,
        address_id: typing.Optional[str] = None,
        address_key: typing.Optional[str] = None
    ):
        self.address_id = address_id
        self.address_key = address_key
        super().__init__(action="removeBillingAddressId")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCustomerRemoveBillingAddressIdAction":
        from ._schemas.me import MyCustomerRemoveBillingAddressIdActionSchema

        return MyCustomerRemoveBillingAddressIdActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCustomerRemoveBillingAddressIdActionSchema

        return MyCustomerRemoveBillingAddressIdActionSchema().dump(self)


class MyCustomerRemoveShippingAddressIdAction(MyCustomerUpdateAction):
    address_id: typing.Optional[str]
    address_key: typing.Optional[str]

    def __init__(
        self,
        *,
        address_id: typing.Optional[str] = None,
        address_key: typing.Optional[str] = None
    ):
        self.address_id = address_id
        self.address_key = address_key
        super().__init__(action="removeShippingAddressId")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCustomerRemoveShippingAddressIdAction":
        from ._schemas.me import MyCustomerRemoveShippingAddressIdActionSchema

        return MyCustomerRemoveShippingAddressIdActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCustomerRemoveShippingAddressIdActionSchema

        return MyCustomerRemoveShippingAddressIdActionSchema().dump(self)


class MyCustomerSetCompanyNameAction(MyCustomerUpdateAction):
    company_name: typing.Optional[str]

    def __init__(self, *, company_name: typing.Optional[str] = None):
        self.company_name = company_name
        super().__init__(action="setCompanyName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCustomerSetCompanyNameAction":
        from ._schemas.me import MyCustomerSetCompanyNameActionSchema

        return MyCustomerSetCompanyNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCustomerSetCompanyNameActionSchema

        return MyCustomerSetCompanyNameActionSchema().dump(self)


class MyCustomerSetCustomFieldAction(MyCustomerUpdateAction):
    name: str
    value: typing.Optional[typing.Any]

    def __init__(self, *, name: str, value: typing.Optional[typing.Any] = None):
        self.name = name
        self.value = value
        super().__init__(action="setCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCustomerSetCustomFieldAction":
        from ._schemas.me import MyCustomerSetCustomFieldActionSchema

        return MyCustomerSetCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCustomerSetCustomFieldActionSchema

        return MyCustomerSetCustomFieldActionSchema().dump(self)


class MyCustomerSetCustomTypeAction(MyCustomerUpdateAction):
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
    ) -> "MyCustomerSetCustomTypeAction":
        from ._schemas.me import MyCustomerSetCustomTypeActionSchema

        return MyCustomerSetCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCustomerSetCustomTypeActionSchema

        return MyCustomerSetCustomTypeActionSchema().dump(self)


class MyCustomerSetDateOfBirthAction(MyCustomerUpdateAction):
    date_of_birth: typing.Optional[datetime.date]

    def __init__(self, *, date_of_birth: typing.Optional[datetime.date] = None):
        self.date_of_birth = date_of_birth
        super().__init__(action="setDateOfBirth")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCustomerSetDateOfBirthAction":
        from ._schemas.me import MyCustomerSetDateOfBirthActionSchema

        return MyCustomerSetDateOfBirthActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCustomerSetDateOfBirthActionSchema

        return MyCustomerSetDateOfBirthActionSchema().dump(self)


class MyCustomerSetDefaultBillingAddressAction(MyCustomerUpdateAction):
    address_id: typing.Optional[str]
    address_key: typing.Optional[str]

    def __init__(
        self,
        *,
        address_id: typing.Optional[str] = None,
        address_key: typing.Optional[str] = None
    ):
        self.address_id = address_id
        self.address_key = address_key
        super().__init__(action="setDefaultBillingAddress")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCustomerSetDefaultBillingAddressAction":
        from ._schemas.me import MyCustomerSetDefaultBillingAddressActionSchema

        return MyCustomerSetDefaultBillingAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCustomerSetDefaultBillingAddressActionSchema

        return MyCustomerSetDefaultBillingAddressActionSchema().dump(self)


class MyCustomerSetDefaultShippingAddressAction(MyCustomerUpdateAction):
    address_id: typing.Optional[str]
    address_key: typing.Optional[str]

    def __init__(
        self,
        *,
        address_id: typing.Optional[str] = None,
        address_key: typing.Optional[str] = None
    ):
        self.address_id = address_id
        self.address_key = address_key
        super().__init__(action="setDefaultShippingAddress")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCustomerSetDefaultShippingAddressAction":
        from ._schemas.me import MyCustomerSetDefaultShippingAddressActionSchema

        return MyCustomerSetDefaultShippingAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCustomerSetDefaultShippingAddressActionSchema

        return MyCustomerSetDefaultShippingAddressActionSchema().dump(self)


class MyCustomerSetFirstNameAction(MyCustomerUpdateAction):
    first_name: typing.Optional[str]

    def __init__(self, *, first_name: typing.Optional[str] = None):
        self.first_name = first_name
        super().__init__(action="setFirstName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCustomerSetFirstNameAction":
        from ._schemas.me import MyCustomerSetFirstNameActionSchema

        return MyCustomerSetFirstNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCustomerSetFirstNameActionSchema

        return MyCustomerSetFirstNameActionSchema().dump(self)


class MyCustomerSetLastNameAction(MyCustomerUpdateAction):
    last_name: typing.Optional[str]

    def __init__(self, *, last_name: typing.Optional[str] = None):
        self.last_name = last_name
        super().__init__(action="setLastName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCustomerSetLastNameAction":
        from ._schemas.me import MyCustomerSetLastNameActionSchema

        return MyCustomerSetLastNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCustomerSetLastNameActionSchema

        return MyCustomerSetLastNameActionSchema().dump(self)


class MyCustomerSetLocaleAction(MyCustomerUpdateAction):
    locale: typing.Optional[str]

    def __init__(self, *, locale: typing.Optional[str] = None):
        self.locale = locale
        super().__init__(action="setLocale")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCustomerSetLocaleAction":
        from ._schemas.me import MyCustomerSetLocaleActionSchema

        return MyCustomerSetLocaleActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCustomerSetLocaleActionSchema

        return MyCustomerSetLocaleActionSchema().dump(self)


class MyCustomerSetMiddleNameAction(MyCustomerUpdateAction):
    middle_name: typing.Optional[str]

    def __init__(self, *, middle_name: typing.Optional[str] = None):
        self.middle_name = middle_name
        super().__init__(action="setMiddleName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCustomerSetMiddleNameAction":
        from ._schemas.me import MyCustomerSetMiddleNameActionSchema

        return MyCustomerSetMiddleNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCustomerSetMiddleNameActionSchema

        return MyCustomerSetMiddleNameActionSchema().dump(self)


class MyCustomerSetSalutationAction(MyCustomerUpdateAction):
    salutation: typing.Optional[str]

    def __init__(self, *, salutation: typing.Optional[str] = None):
        self.salutation = salutation
        super().__init__(action="setSalutation")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCustomerSetSalutationAction":
        from ._schemas.me import MyCustomerSetSalutationActionSchema

        return MyCustomerSetSalutationActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCustomerSetSalutationActionSchema

        return MyCustomerSetSalutationActionSchema().dump(self)


class MyCustomerSetTitleAction(MyCustomerUpdateAction):
    title: typing.Optional[str]

    def __init__(self, *, title: typing.Optional[str] = None):
        self.title = title
        super().__init__(action="setTitle")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCustomerSetTitleAction":
        from ._schemas.me import MyCustomerSetTitleActionSchema

        return MyCustomerSetTitleActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCustomerSetTitleActionSchema

        return MyCustomerSetTitleActionSchema().dump(self)


class MyCustomerSetVatIdAction(MyCustomerUpdateAction):
    vat_id: typing.Optional[str]

    def __init__(self, *, vat_id: typing.Optional[str] = None):
        self.vat_id = vat_id
        super().__init__(action="setVatId")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyCustomerSetVatIdAction":
        from ._schemas.me import MyCustomerSetVatIdActionSchema

        return MyCustomerSetVatIdActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyCustomerSetVatIdActionSchema

        return MyCustomerSetVatIdActionSchema().dump(self)


class MyPaymentAddTransactionAction(MyPaymentUpdateAction):
    transaction: "TransactionDraft"

    def __init__(self, *, transaction: "TransactionDraft"):
        self.transaction = transaction
        super().__init__(action="addTransaction")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyPaymentAddTransactionAction":
        from ._schemas.me import MyPaymentAddTransactionActionSchema

        return MyPaymentAddTransactionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyPaymentAddTransactionActionSchema

        return MyPaymentAddTransactionActionSchema().dump(self)


class MyPaymentChangeAmountPlannedAction(MyPaymentUpdateAction):
    amount: "Money"

    def __init__(self, *, amount: "Money"):
        self.amount = amount
        super().__init__(action="changeAmountPlanned")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyPaymentChangeAmountPlannedAction":
        from ._schemas.me import MyPaymentChangeAmountPlannedActionSchema

        return MyPaymentChangeAmountPlannedActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyPaymentChangeAmountPlannedActionSchema

        return MyPaymentChangeAmountPlannedActionSchema().dump(self)


class MyPaymentSetCustomFieldAction(MyPaymentUpdateAction):
    name: str
    value: typing.Optional[typing.Any]

    def __init__(self, *, name: str, value: typing.Optional[typing.Any] = None):
        self.name = name
        self.value = value
        super().__init__(action="setCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyPaymentSetCustomFieldAction":
        from ._schemas.me import MyPaymentSetCustomFieldActionSchema

        return MyPaymentSetCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyPaymentSetCustomFieldActionSchema

        return MyPaymentSetCustomFieldActionSchema().dump(self)


class MyPaymentSetMethodInfoInterfaceAction(MyPaymentUpdateAction):
    interface: str

    def __init__(self, *, interface: str):
        self.interface = interface
        super().__init__(action="setMethodInfoInterface")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyPaymentSetMethodInfoInterfaceAction":
        from ._schemas.me import MyPaymentSetMethodInfoInterfaceActionSchema

        return MyPaymentSetMethodInfoInterfaceActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyPaymentSetMethodInfoInterfaceActionSchema

        return MyPaymentSetMethodInfoInterfaceActionSchema().dump(self)


class MyPaymentSetMethodInfoMethodAction(MyPaymentUpdateAction):
    method: typing.Optional[str]

    def __init__(self, *, method: typing.Optional[str] = None):
        self.method = method
        super().__init__(action="setMethodInfoMethod")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyPaymentSetMethodInfoMethodAction":
        from ._schemas.me import MyPaymentSetMethodInfoMethodActionSchema

        return MyPaymentSetMethodInfoMethodActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyPaymentSetMethodInfoMethodActionSchema

        return MyPaymentSetMethodInfoMethodActionSchema().dump(self)


class MyPaymentSetMethodInfoNameAction(MyPaymentUpdateAction):
    name: typing.Optional["LocalizedString"]

    def __init__(self, *, name: typing.Optional["LocalizedString"] = None):
        self.name = name
        super().__init__(action="setMethodInfoName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyPaymentSetMethodInfoNameAction":
        from ._schemas.me import MyPaymentSetMethodInfoNameActionSchema

        return MyPaymentSetMethodInfoNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyPaymentSetMethodInfoNameActionSchema

        return MyPaymentSetMethodInfoNameActionSchema().dump(self)


class MyShoppingListAddLineItemAction(MyShoppingListUpdateAction):
    sku: typing.Optional[str]
    product_id: typing.Optional[str]
    variant_id: typing.Optional[int]
    quantity: typing.Optional[int]
    added_at: typing.Optional[datetime.datetime]
    custom: typing.Optional["CustomFieldsDraft"]

    def __init__(
        self,
        *,
        sku: typing.Optional[str] = None,
        product_id: typing.Optional[str] = None,
        variant_id: typing.Optional[int] = None,
        quantity: typing.Optional[int] = None,
        added_at: typing.Optional[datetime.datetime] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None
    ):
        self.sku = sku
        self.product_id = product_id
        self.variant_id = variant_id
        self.quantity = quantity
        self.added_at = added_at
        self.custom = custom
        super().__init__(action="addLineItem")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyShoppingListAddLineItemAction":
        from ._schemas.me import MyShoppingListAddLineItemActionSchema

        return MyShoppingListAddLineItemActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyShoppingListAddLineItemActionSchema

        return MyShoppingListAddLineItemActionSchema().dump(self)


class MyShoppingListAddTextLineItemAction(MyShoppingListUpdateAction):
    name: "LocalizedString"
    description: typing.Optional["LocalizedString"]
    quantity: typing.Optional[int]
    added_at: typing.Optional[datetime.datetime]
    custom: typing.Optional["CustomFieldsDraft"]

    def __init__(
        self,
        *,
        name: "LocalizedString",
        description: typing.Optional["LocalizedString"] = None,
        quantity: typing.Optional[int] = None,
        added_at: typing.Optional[datetime.datetime] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None
    ):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.added_at = added_at
        self.custom = custom
        super().__init__(action="addTextLineItem")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyShoppingListAddTextLineItemAction":
        from ._schemas.me import MyShoppingListAddTextLineItemActionSchema

        return MyShoppingListAddTextLineItemActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyShoppingListAddTextLineItemActionSchema

        return MyShoppingListAddTextLineItemActionSchema().dump(self)


class MyShoppingListChangeLineItemQuantityAction(MyShoppingListUpdateAction):
    line_item_id: str
    quantity: int

    def __init__(self, *, line_item_id: str, quantity: int):
        self.line_item_id = line_item_id
        self.quantity = quantity
        super().__init__(action="changeLineItemQuantity")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyShoppingListChangeLineItemQuantityAction":
        from ._schemas.me import MyShoppingListChangeLineItemQuantityActionSchema

        return MyShoppingListChangeLineItemQuantityActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyShoppingListChangeLineItemQuantityActionSchema

        return MyShoppingListChangeLineItemQuantityActionSchema().dump(self)


class MyShoppingListChangeLineItemsOrderAction(MyShoppingListUpdateAction):
    line_item_order: typing.List["str"]

    def __init__(self, *, line_item_order: typing.List["str"]):
        self.line_item_order = line_item_order
        super().__init__(action="changeLineItemsOrder")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyShoppingListChangeLineItemsOrderAction":
        from ._schemas.me import MyShoppingListChangeLineItemsOrderActionSchema

        return MyShoppingListChangeLineItemsOrderActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyShoppingListChangeLineItemsOrderActionSchema

        return MyShoppingListChangeLineItemsOrderActionSchema().dump(self)


class MyShoppingListChangeNameAction(MyShoppingListUpdateAction):
    name: "LocalizedString"

    def __init__(self, *, name: "LocalizedString"):
        self.name = name
        super().__init__(action="changeName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyShoppingListChangeNameAction":
        from ._schemas.me import MyShoppingListChangeNameActionSchema

        return MyShoppingListChangeNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyShoppingListChangeNameActionSchema

        return MyShoppingListChangeNameActionSchema().dump(self)


class MyShoppingListChangeTextLineItemNameAction(MyShoppingListUpdateAction):
    text_line_item_id: str
    name: "LocalizedString"

    def __init__(self, *, text_line_item_id: str, name: "LocalizedString"):
        self.text_line_item_id = text_line_item_id
        self.name = name
        super().__init__(action="changeTextLineItemName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyShoppingListChangeTextLineItemNameAction":
        from ._schemas.me import MyShoppingListChangeTextLineItemNameActionSchema

        return MyShoppingListChangeTextLineItemNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyShoppingListChangeTextLineItemNameActionSchema

        return MyShoppingListChangeTextLineItemNameActionSchema().dump(self)


class MyShoppingListChangeTextLineItemQuantityAction(MyShoppingListUpdateAction):
    text_line_item_id: str
    quantity: int

    def __init__(self, *, text_line_item_id: str, quantity: int):
        self.text_line_item_id = text_line_item_id
        self.quantity = quantity
        super().__init__(action="changeTextLineItemQuantity")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyShoppingListChangeTextLineItemQuantityAction":
        from ._schemas.me import MyShoppingListChangeTextLineItemQuantityActionSchema

        return MyShoppingListChangeTextLineItemQuantityActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyShoppingListChangeTextLineItemQuantityActionSchema

        return MyShoppingListChangeTextLineItemQuantityActionSchema().dump(self)


class MyShoppingListChangeTextLineItemsOrderAction(MyShoppingListUpdateAction):
    text_line_item_order: typing.List["str"]

    def __init__(self, *, text_line_item_order: typing.List["str"]):
        self.text_line_item_order = text_line_item_order
        super().__init__(action="changeTextLineItemsOrder")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyShoppingListChangeTextLineItemsOrderAction":
        from ._schemas.me import MyShoppingListChangeTextLineItemsOrderActionSchema

        return MyShoppingListChangeTextLineItemsOrderActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyShoppingListChangeTextLineItemsOrderActionSchema

        return MyShoppingListChangeTextLineItemsOrderActionSchema().dump(self)


class MyShoppingListRemoveLineItemAction(MyShoppingListUpdateAction):
    line_item_id: str
    quantity: typing.Optional[int]

    def __init__(self, *, line_item_id: str, quantity: typing.Optional[int] = None):
        self.line_item_id = line_item_id
        self.quantity = quantity
        super().__init__(action="removeLineItem")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyShoppingListRemoveLineItemAction":
        from ._schemas.me import MyShoppingListRemoveLineItemActionSchema

        return MyShoppingListRemoveLineItemActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyShoppingListRemoveLineItemActionSchema

        return MyShoppingListRemoveLineItemActionSchema().dump(self)


class MyShoppingListRemoveTextLineItemAction(MyShoppingListUpdateAction):
    text_line_item_id: str
    quantity: typing.Optional[int]

    def __init__(
        self, *, text_line_item_id: str, quantity: typing.Optional[int] = None
    ):
        self.text_line_item_id = text_line_item_id
        self.quantity = quantity
        super().__init__(action="removeTextLineItem")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyShoppingListRemoveTextLineItemAction":
        from ._schemas.me import MyShoppingListRemoveTextLineItemActionSchema

        return MyShoppingListRemoveTextLineItemActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyShoppingListRemoveTextLineItemActionSchema

        return MyShoppingListRemoveTextLineItemActionSchema().dump(self)


class MyShoppingListSetCustomFieldAction(MyShoppingListUpdateAction):
    name: str
    value: typing.Optional[typing.Any]

    def __init__(self, *, name: str, value: typing.Optional[typing.Any] = None):
        self.name = name
        self.value = value
        super().__init__(action="setCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyShoppingListSetCustomFieldAction":
        from ._schemas.me import MyShoppingListSetCustomFieldActionSchema

        return MyShoppingListSetCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyShoppingListSetCustomFieldActionSchema

        return MyShoppingListSetCustomFieldActionSchema().dump(self)


class MyShoppingListSetCustomTypeAction(MyShoppingListUpdateAction):
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
    ) -> "MyShoppingListSetCustomTypeAction":
        from ._schemas.me import MyShoppingListSetCustomTypeActionSchema

        return MyShoppingListSetCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyShoppingListSetCustomTypeActionSchema

        return MyShoppingListSetCustomTypeActionSchema().dump(self)


class MyShoppingListSetDeleteDaysAfterLastModificationAction(
    MyShoppingListUpdateAction
):
    delete_days_after_last_modification: typing.Optional[int]

    def __init__(
        self, *, delete_days_after_last_modification: typing.Optional[int] = None
    ):
        self.delete_days_after_last_modification = delete_days_after_last_modification
        super().__init__(action="setDeleteDaysAfterLastModification")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyShoppingListSetDeleteDaysAfterLastModificationAction":
        from ._schemas.me import (
            MyShoppingListSetDeleteDaysAfterLastModificationActionSchema,
        )

        return MyShoppingListSetDeleteDaysAfterLastModificationActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import (
            MyShoppingListSetDeleteDaysAfterLastModificationActionSchema,
        )

        return MyShoppingListSetDeleteDaysAfterLastModificationActionSchema().dump(self)


class MyShoppingListSetDescriptionAction(MyShoppingListUpdateAction):
    description: typing.Optional["LocalizedString"]

    def __init__(self, *, description: typing.Optional["LocalizedString"] = None):
        self.description = description
        super().__init__(action="setDescription")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyShoppingListSetDescriptionAction":
        from ._schemas.me import MyShoppingListSetDescriptionActionSchema

        return MyShoppingListSetDescriptionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyShoppingListSetDescriptionActionSchema

        return MyShoppingListSetDescriptionActionSchema().dump(self)


class MyShoppingListSetLineItemCustomFieldAction(MyShoppingListUpdateAction):
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
    ) -> "MyShoppingListSetLineItemCustomFieldAction":
        from ._schemas.me import MyShoppingListSetLineItemCustomFieldActionSchema

        return MyShoppingListSetLineItemCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyShoppingListSetLineItemCustomFieldActionSchema

        return MyShoppingListSetLineItemCustomFieldActionSchema().dump(self)


class MyShoppingListSetLineItemCustomTypeAction(MyShoppingListUpdateAction):
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
    ) -> "MyShoppingListSetLineItemCustomTypeAction":
        from ._schemas.me import MyShoppingListSetLineItemCustomTypeActionSchema

        return MyShoppingListSetLineItemCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyShoppingListSetLineItemCustomTypeActionSchema

        return MyShoppingListSetLineItemCustomTypeActionSchema().dump(self)


class MyShoppingListSetTextLineItemCustomFieldAction(MyShoppingListUpdateAction):
    text_line_item_id: str
    name: str
    value: typing.Optional[typing.Any]

    def __init__(
        self,
        *,
        text_line_item_id: str,
        name: str,
        value: typing.Optional[typing.Any] = None
    ):
        self.text_line_item_id = text_line_item_id
        self.name = name
        self.value = value
        super().__init__(action="setTextLineItemCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyShoppingListSetTextLineItemCustomFieldAction":
        from ._schemas.me import MyShoppingListSetTextLineItemCustomFieldActionSchema

        return MyShoppingListSetTextLineItemCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyShoppingListSetTextLineItemCustomFieldActionSchema

        return MyShoppingListSetTextLineItemCustomFieldActionSchema().dump(self)


class MyShoppingListSetTextLineItemCustomTypeAction(MyShoppingListUpdateAction):
    text_line_item_id: str
    type: typing.Optional["TypeResourceIdentifier"]
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        text_line_item_id: str,
        type: typing.Optional["TypeResourceIdentifier"] = None,
        fields: typing.Optional["FieldContainer"] = None
    ):
        self.text_line_item_id = text_line_item_id
        self.type = type
        self.fields = fields
        super().__init__(action="setTextLineItemCustomType")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyShoppingListSetTextLineItemCustomTypeAction":
        from ._schemas.me import MyShoppingListSetTextLineItemCustomTypeActionSchema

        return MyShoppingListSetTextLineItemCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyShoppingListSetTextLineItemCustomTypeActionSchema

        return MyShoppingListSetTextLineItemCustomTypeActionSchema().dump(self)


class MyShoppingListSetTextLineItemDescriptionAction(MyShoppingListUpdateAction):
    text_line_item_id: str
    description: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        text_line_item_id: str,
        description: typing.Optional["LocalizedString"] = None
    ):
        self.text_line_item_id = text_line_item_id
        self.description = description
        super().__init__(action="setTextLineItemDescription")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MyShoppingListSetTextLineItemDescriptionAction":
        from ._schemas.me import MyShoppingListSetTextLineItemDescriptionActionSchema

        return MyShoppingListSetTextLineItemDescriptionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.me import MyShoppingListSetTextLineItemDescriptionActionSchema

        return MyShoppingListSetTextLineItemDescriptionActionSchema().dump(self)
