# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import BaseResource, Reference, ReferenceTypeId, ResourceIdentifier

if typing.TYPE_CHECKING:
    from .common import Address, CreatedBy, LastModifiedBy, ReferenceTypeId
    from .customer_group import CustomerGroupReference, CustomerGroupResourceIdentifier
    from .store import StoreKeyReference, StoreResourceIdentifier
    from .type import (
        CustomFields,
        CustomFieldsDraft,
        FieldContainer,
        TypeResourceIdentifier,
    )

__all__ = [
    "AnonymousCartSignInMode",
    "Customer",
    "CustomerAddAddressAction",
    "CustomerAddBillingAddressIdAction",
    "CustomerAddShippingAddressIdAction",
    "CustomerAddStoreAction",
    "CustomerChangeAddressAction",
    "CustomerChangeEmailAction",
    "CustomerChangePassword",
    "CustomerCreateEmailToken",
    "CustomerCreatePasswordResetToken",
    "CustomerDraft",
    "CustomerEmailVerify",
    "CustomerPagedQueryResponse",
    "CustomerReference",
    "CustomerRemoveAddressAction",
    "CustomerRemoveBillingAddressIdAction",
    "CustomerRemoveShippingAddressIdAction",
    "CustomerRemoveStoreAction",
    "CustomerResetPassword",
    "CustomerResourceIdentifier",
    "CustomerSetCompanyNameAction",
    "CustomerSetCustomFieldAction",
    "CustomerSetCustomTypeAction",
    "CustomerSetCustomerGroupAction",
    "CustomerSetCustomerNumberAction",
    "CustomerSetDateOfBirthAction",
    "CustomerSetDefaultBillingAddressAction",
    "CustomerSetDefaultShippingAddressAction",
    "CustomerSetExternalIdAction",
    "CustomerSetFirstNameAction",
    "CustomerSetKeyAction",
    "CustomerSetLastNameAction",
    "CustomerSetLocaleAction",
    "CustomerSetMiddleNameAction",
    "CustomerSetSalutationAction",
    "CustomerSetStoresAction",
    "CustomerSetTitleAction",
    "CustomerSetVatIdAction",
    "CustomerSignInResult",
    "CustomerSignin",
    "CustomerToken",
    "CustomerUpdate",
    "CustomerUpdateAction",
]


class AnonymousCartSignInMode(enum.Enum):
    MERGE_WITH_EXISTING_CUSTOMER_CART = "MergeWithExistingCustomerCart"
    USE_AS_NEW_ACTIVE_CUSTOMER_CART = "UseAsNewActiveCustomerCart"


class Customer(BaseResource):
    #: Present on resources updated after 1/02/2019 except for events not tracked.
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Present on resources created after 1/02/2019 except for events not tracked.
    created_by: typing.Optional["CreatedBy"]
    #: The customer number can be used to create a more human-readable (in contrast to ID) identifier for the customer.
    #: It should be unique across a project.
    #: Once the field was set it cannot be changed anymore.
    customer_number: typing.Optional[str]
    #: The customer's email address and the main identifier of uniqueness for a customer account.
    #: Email addresses are either unique to the store they're specified for, _or_ for the entire project.
    #: For more information, see Email uniquenes.
    email: str
    password: str
    first_name: typing.Optional[str]
    last_name: typing.Optional[str]
    middle_name: typing.Optional[str]
    title: typing.Optional[str]
    date_of_birth: typing.Optional[datetime.date]
    company_name: typing.Optional[str]
    vat_id: typing.Optional[str]
    #: The addresses have unique IDs in the addresses list
    addresses: typing.List["Address"]
    #: The address ID in the addresses list
    default_shipping_address_id: typing.Optional[str]
    #: The IDs from the addresses list which are used as shipping addresses
    shipping_address_ids: typing.Optional[typing.List["str"]]
    #: The address ID in the addresses list
    default_billing_address_id: typing.Optional[str]
    #: The IDs from the addresses list which are used as billing addresses
    billing_address_ids: typing.Optional[typing.List["str"]]
    is_email_verified: bool
    external_id: typing.Optional[str]
    customer_group: typing.Optional["CustomerGroupReference"]
    custom: typing.Optional["CustomFields"]
    locale: typing.Optional[str]
    salutation: typing.Optional[str]
    #: User-specific unique identifier for a customer.
    #: Must be unique across a project.
    #: The field can be reset using the Set Key UpdateAction
    key: typing.Optional[str]
    #: References to the stores the customer account is associated with.
    #: If no stores are specified, the customer is a global customer, and can log in using the Password Flow for global Customers.
    #: If one or more stores are specified, the customer can only log in using the Password Flow for Customers in a Store for those specific stores.
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
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Customer":
        from ._schemas.customer import CustomerSchema

        return CustomerSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerSchema

        return CustomerSchema().dump(self)


class CustomerChangePassword(_BaseType):
    id: str
    version: int
    current_password: str
    new_password: str

    def __init__(
        self, *, id: str, version: int, current_password: str, new_password: str
    ):
        self.id = id
        self.version = version
        self.current_password = current_password
        self.new_password = new_password
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerChangePassword":
        from ._schemas.customer import CustomerChangePasswordSchema

        return CustomerChangePasswordSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerChangePasswordSchema

        return CustomerChangePasswordSchema().dump(self)


class CustomerCreateEmailToken(_BaseType):
    id: str
    version: typing.Optional[int]
    ttl_minutes: int

    def __init__(
        self, *, id: str, version: typing.Optional[int] = None, ttl_minutes: int
    ):
        self.id = id
        self.version = version
        self.ttl_minutes = ttl_minutes
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerCreateEmailToken":
        from ._schemas.customer import CustomerCreateEmailTokenSchema

        return CustomerCreateEmailTokenSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerCreateEmailTokenSchema

        return CustomerCreateEmailTokenSchema().dump(self)


class CustomerCreatePasswordResetToken(_BaseType):
    email: str
    ttl_minutes: typing.Optional[int]

    def __init__(self, *, email: str, ttl_minutes: typing.Optional[int] = None):
        self.email = email
        self.ttl_minutes = ttl_minutes
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerCreatePasswordResetToken":
        from ._schemas.customer import CustomerCreatePasswordResetTokenSchema

        return CustomerCreatePasswordResetTokenSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerCreatePasswordResetTokenSchema

        return CustomerCreatePasswordResetTokenSchema().dump(self)


class CustomerDraft(_BaseType):
    #: String that uniquely identifies a customer.
    #: It can be used to create more human-readable (in contrast to ID) identifier for the customer.
    #: It should be **unique** across a project.
    #: Once it's set it cannot be changed.
    customer_number: typing.Optional[str]
    #: The customer's email address and the main identifier of uniqueness for a customer account.
    #: Email addresses are either unique to the store they're specified for, _or_ for the entire project, and are case insensitive.
    #: For more information, see Email uniquenes.
    email: str
    password: str
    first_name: typing.Optional[str]
    last_name: typing.Optional[str]
    middle_name: typing.Optional[str]
    title: typing.Optional[str]
    #: Identifies a single cart that will be assigned to the new customer account.
    anonymous_cart_id: typing.Optional[str]
    #: Identifies carts and orders belonging to an anonymous session that will be assigned to the new customer account.
    anonymous_id: typing.Optional[str]
    date_of_birth: typing.Optional[datetime.date]
    company_name: typing.Optional[str]
    vat_id: typing.Optional[str]
    #: Sets the ID of each address to be unique in the addresses list.
    addresses: typing.Optional[typing.List["Address"]]
    #: The index of the address in the addresses array.
    #: The `defaultShippingAddressId` of the customer will be set to the ID of that address.
    default_shipping_address: typing.Optional[int]
    #: The indices of the shipping addresses in the addresses array.
    #: The `shippingAddressIds` of the Customer will be set to the IDs of that addresses.
    shipping_addresses: typing.Optional[typing.List["int"]]
    #: The index of the address in the addresses array.
    #: The `defaultBillingAddressId` of the customer will be set to the ID of that address.
    default_billing_address: typing.Optional[int]
    #: The indices of the billing addresses in the addresses array.
    #: The `billingAddressIds` of the customer will be set to the IDs of that addresses.
    billing_addresses: typing.Optional[typing.List["int"]]
    is_email_verified: typing.Optional[bool]
    external_id: typing.Optional[str]
    customer_group: typing.Optional["CustomerGroupResourceIdentifier"]
    #: The custom fields.
    custom: typing.Optional["CustomFieldsDraft"]
    #: Must be one of the languages supported for this project
    locale: typing.Optional[str]
    salutation: typing.Optional[str]
    #: User-specific unique identifier for a customer.
    #: Must be unique across a project.
    #: The field can be reset using the Set Key UpdateAction
    key: typing.Optional[str]
    #: References to the stores the customer account is associated with.
    #: If no stores are specified, the customer is a global customer, and can log in using the Password Flow for global Customers.
    #: If one or more stores are specified, the customer can only log in using the Password Flow for Customers in a Store for those specific stores.
    stores: typing.Optional[typing.List["StoreResourceIdentifier"]]

    def __init__(
        self,
        *,
        customer_number: typing.Optional[str] = None,
        email: str,
        password: str,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        anonymous_cart_id: typing.Optional[str] = None,
        anonymous_id: typing.Optional[str] = None,
        date_of_birth: typing.Optional[datetime.date] = None,
        company_name: typing.Optional[str] = None,
        vat_id: typing.Optional[str] = None,
        addresses: typing.Optional[typing.List["Address"]] = None,
        default_shipping_address: typing.Optional[int] = None,
        shipping_addresses: typing.Optional[typing.List["int"]] = None,
        default_billing_address: typing.Optional[int] = None,
        billing_addresses: typing.Optional[typing.List["int"]] = None,
        is_email_verified: typing.Optional[bool] = None,
        external_id: typing.Optional[str] = None,
        customer_group: typing.Optional["CustomerGroupResourceIdentifier"] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        locale: typing.Optional[str] = None,
        salutation: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        stores: typing.Optional[typing.List["StoreResourceIdentifier"]] = None
    ):
        self.customer_number = customer_number
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.title = title
        self.anonymous_cart_id = anonymous_cart_id
        self.anonymous_id = anonymous_id
        self.date_of_birth = date_of_birth
        self.company_name = company_name
        self.vat_id = vat_id
        self.addresses = addresses
        self.default_shipping_address = default_shipping_address
        self.shipping_addresses = shipping_addresses
        self.default_billing_address = default_billing_address
        self.billing_addresses = billing_addresses
        self.is_email_verified = is_email_verified
        self.external_id = external_id
        self.customer_group = customer_group
        self.custom = custom
        self.locale = locale
        self.salutation = salutation
        self.key = key
        self.stores = stores
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomerDraft":
        from ._schemas.customer import CustomerDraftSchema

        return CustomerDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerDraftSchema

        return CustomerDraftSchema().dump(self)


class CustomerEmailVerify(_BaseType):
    version: typing.Optional[int]
    token_value: str

    def __init__(self, *, version: typing.Optional[int] = None, token_value: str):
        self.version = version
        self.token_value = token_value
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomerEmailVerify":
        from ._schemas.customer import CustomerEmailVerifySchema

        return CustomerEmailVerifySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerEmailVerifySchema

        return CustomerEmailVerifySchema().dump(self)


class CustomerPagedQueryResponse(_BaseType):
    limit: int
    count: int
    total: typing.Optional[int]
    offset: int
    results: typing.List["Customer"]

    def __init__(
        self,
        *,
        limit: int,
        count: int,
        total: typing.Optional[int] = None,
        offset: int,
        results: typing.List["Customer"]
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
    ) -> "CustomerPagedQueryResponse":
        from ._schemas.customer import CustomerPagedQueryResponseSchema

        return CustomerPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerPagedQueryResponseSchema

        return CustomerPagedQueryResponseSchema().dump(self)


class CustomerReference(Reference):
    obj: typing.Optional["Customer"]

    def __init__(self, *, id: str, obj: typing.Optional["Customer"] = None):
        self.obj = obj
        super().__init__(id=id, type_id=ReferenceTypeId.CUSTOMER)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomerReference":
        from ._schemas.customer import CustomerReferenceSchema

        return CustomerReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerReferenceSchema

        return CustomerReferenceSchema().dump(self)


class CustomerResetPassword(_BaseType):
    token_value: str
    new_password: str
    version: typing.Optional[int]

    def __init__(
        self,
        *,
        token_value: str,
        new_password: str,
        version: typing.Optional[int] = None
    ):
        self.token_value = token_value
        self.new_password = new_password
        self.version = version
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomerResetPassword":
        from ._schemas.customer import CustomerResetPasswordSchema

        return CustomerResetPasswordSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerResetPasswordSchema

        return CustomerResetPasswordSchema().dump(self)


class CustomerResourceIdentifier(ResourceIdentifier):
    def __init__(
        self, *, id: typing.Optional[str] = None, key: typing.Optional[str] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.CUSTOMER)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerResourceIdentifier":
        from ._schemas.customer import CustomerResourceIdentifierSchema

        return CustomerResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerResourceIdentifierSchema

        return CustomerResourceIdentifierSchema().dump(self)


class CustomerSignInResult(_BaseType):
    customer: "Customer"
    #: A cart that is associated to the customer.
    #: Empty if the customer does not have a cart yet.
    cart: typing.Optional[object]

    def __init__(self, *, customer: "Customer", cart: typing.Optional[object] = None):
        self.customer = customer
        self.cart = cart
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomerSignInResult":
        from ._schemas.customer import CustomerSignInResultSchema

        return CustomerSignInResultSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerSignInResultSchema

        return CustomerSignInResultSchema().dump(self)


class CustomerSignin(_BaseType):
    email: str
    password: str
    anonymous_cart_id: typing.Optional[str]
    anonymous_cart_sign_in_mode: typing.Optional["AnonymousCartSignInMode"]
    anonymous_id: typing.Optional[str]
    update_product_data: typing.Optional[bool]

    def __init__(
        self,
        *,
        email: str,
        password: str,
        anonymous_cart_id: typing.Optional[str] = None,
        anonymous_cart_sign_in_mode: typing.Optional["AnonymousCartSignInMode"] = None,
        anonymous_id: typing.Optional[str] = None,
        update_product_data: typing.Optional[bool] = None
    ):
        self.email = email
        self.password = password
        self.anonymous_cart_id = anonymous_cart_id
        self.anonymous_cart_sign_in_mode = anonymous_cart_sign_in_mode
        self.anonymous_id = anonymous_id
        self.update_product_data = update_product_data
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomerSignin":
        from ._schemas.customer import CustomerSigninSchema

        return CustomerSigninSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerSigninSchema

        return CustomerSigninSchema().dump(self)


class CustomerToken(_BaseType):
    id: str
    created_at: datetime.datetime
    last_modified_at: typing.Optional[datetime.datetime]
    customer_id: str
    expires_at: datetime.datetime
    value: str

    def __init__(
        self,
        *,
        id: str,
        created_at: datetime.datetime,
        last_modified_at: typing.Optional[datetime.datetime] = None,
        customer_id: str,
        expires_at: datetime.datetime,
        value: str
    ):
        self.id = id
        self.created_at = created_at
        self.last_modified_at = last_modified_at
        self.customer_id = customer_id
        self.expires_at = expires_at
        self.value = value
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomerToken":
        from ._schemas.customer import CustomerTokenSchema

        return CustomerTokenSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerTokenSchema

        return CustomerTokenSchema().dump(self)


class CustomerUpdate(_BaseType):
    version: int
    actions: typing.List["CustomerUpdateAction"]

    def __init__(self, *, version: int, actions: typing.List["CustomerUpdateAction"]):
        self.version = version
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomerUpdate":
        from ._schemas.customer import CustomerUpdateSchema

        return CustomerUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerUpdateSchema

        return CustomerUpdateSchema().dump(self)


class CustomerUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomerUpdateAction":
        if data["action"] == "addAddress":
            from ._schemas.customer import CustomerAddAddressActionSchema

            return CustomerAddAddressActionSchema().load(data)
        if data["action"] == "addBillingAddressId":
            from ._schemas.customer import CustomerAddBillingAddressIdActionSchema

            return CustomerAddBillingAddressIdActionSchema().load(data)
        if data["action"] == "addShippingAddressId":
            from ._schemas.customer import CustomerAddShippingAddressIdActionSchema

            return CustomerAddShippingAddressIdActionSchema().load(data)
        if data["action"] == "addStore":
            from ._schemas.customer import CustomerAddStoreActionSchema

            return CustomerAddStoreActionSchema().load(data)
        if data["action"] == "changeAddress":
            from ._schemas.customer import CustomerChangeAddressActionSchema

            return CustomerChangeAddressActionSchema().load(data)
        if data["action"] == "changeEmail":
            from ._schemas.customer import CustomerChangeEmailActionSchema

            return CustomerChangeEmailActionSchema().load(data)
        if data["action"] == "removeAddress":
            from ._schemas.customer import CustomerRemoveAddressActionSchema

            return CustomerRemoveAddressActionSchema().load(data)
        if data["action"] == "removeBillingAddressId":
            from ._schemas.customer import CustomerRemoveBillingAddressIdActionSchema

            return CustomerRemoveBillingAddressIdActionSchema().load(data)
        if data["action"] == "removeShippingAddressId":
            from ._schemas.customer import CustomerRemoveShippingAddressIdActionSchema

            return CustomerRemoveShippingAddressIdActionSchema().load(data)
        if data["action"] == "removeStore":
            from ._schemas.customer import CustomerRemoveStoreActionSchema

            return CustomerRemoveStoreActionSchema().load(data)
        if data["action"] == "setCompanyName":
            from ._schemas.customer import CustomerSetCompanyNameActionSchema

            return CustomerSetCompanyNameActionSchema().load(data)
        if data["action"] == "setCustomField":
            from ._schemas.customer import CustomerSetCustomFieldActionSchema

            return CustomerSetCustomFieldActionSchema().load(data)
        if data["action"] == "setCustomType":
            from ._schemas.customer import CustomerSetCustomTypeActionSchema

            return CustomerSetCustomTypeActionSchema().load(data)
        if data["action"] == "setCustomerGroup":
            from ._schemas.customer import CustomerSetCustomerGroupActionSchema

            return CustomerSetCustomerGroupActionSchema().load(data)
        if data["action"] == "setCustomerNumber":
            from ._schemas.customer import CustomerSetCustomerNumberActionSchema

            return CustomerSetCustomerNumberActionSchema().load(data)
        if data["action"] == "setDateOfBirth":
            from ._schemas.customer import CustomerSetDateOfBirthActionSchema

            return CustomerSetDateOfBirthActionSchema().load(data)
        if data["action"] == "setDefaultBillingAddress":
            from ._schemas.customer import CustomerSetDefaultBillingAddressActionSchema

            return CustomerSetDefaultBillingAddressActionSchema().load(data)
        if data["action"] == "setDefaultShippingAddress":
            from ._schemas.customer import CustomerSetDefaultShippingAddressActionSchema

            return CustomerSetDefaultShippingAddressActionSchema().load(data)
        if data["action"] == "setExternalId":
            from ._schemas.customer import CustomerSetExternalIdActionSchema

            return CustomerSetExternalIdActionSchema().load(data)
        if data["action"] == "setFirstName":
            from ._schemas.customer import CustomerSetFirstNameActionSchema

            return CustomerSetFirstNameActionSchema().load(data)
        if data["action"] == "setKey":
            from ._schemas.customer import CustomerSetKeyActionSchema

            return CustomerSetKeyActionSchema().load(data)
        if data["action"] == "setLastName":
            from ._schemas.customer import CustomerSetLastNameActionSchema

            return CustomerSetLastNameActionSchema().load(data)
        if data["action"] == "setLocale":
            from ._schemas.customer import CustomerSetLocaleActionSchema

            return CustomerSetLocaleActionSchema().load(data)
        if data["action"] == "setMiddleName":
            from ._schemas.customer import CustomerSetMiddleNameActionSchema

            return CustomerSetMiddleNameActionSchema().load(data)
        if data["action"] == "setSalutation":
            from ._schemas.customer import CustomerSetSalutationActionSchema

            return CustomerSetSalutationActionSchema().load(data)
        if data["action"] == "setStores":
            from ._schemas.customer import CustomerSetStoresActionSchema

            return CustomerSetStoresActionSchema().load(data)
        if data["action"] == "setTitle":
            from ._schemas.customer import CustomerSetTitleActionSchema

            return CustomerSetTitleActionSchema().load(data)
        if data["action"] == "setVatId":
            from ._schemas.customer import CustomerSetVatIdActionSchema

            return CustomerSetVatIdActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerUpdateActionSchema

        return CustomerUpdateActionSchema().dump(self)


class CustomerAddAddressAction(CustomerUpdateAction):
    address: "Address"

    def __init__(self, *, address: "Address"):
        self.address = address
        super().__init__(action="addAddress")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerAddAddressAction":
        from ._schemas.customer import CustomerAddAddressActionSchema

        return CustomerAddAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerAddAddressActionSchema

        return CustomerAddAddressActionSchema().dump(self)


class CustomerAddBillingAddressIdAction(CustomerUpdateAction):
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
    ) -> "CustomerAddBillingAddressIdAction":
        from ._schemas.customer import CustomerAddBillingAddressIdActionSchema

        return CustomerAddBillingAddressIdActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerAddBillingAddressIdActionSchema

        return CustomerAddBillingAddressIdActionSchema().dump(self)


class CustomerAddShippingAddressIdAction(CustomerUpdateAction):
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
    ) -> "CustomerAddShippingAddressIdAction":
        from ._schemas.customer import CustomerAddShippingAddressIdActionSchema

        return CustomerAddShippingAddressIdActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerAddShippingAddressIdActionSchema

        return CustomerAddShippingAddressIdActionSchema().dump(self)


class CustomerAddStoreAction(CustomerUpdateAction):
    store: "StoreResourceIdentifier"

    def __init__(self, *, store: "StoreResourceIdentifier"):
        self.store = store
        super().__init__(action="addStore")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerAddStoreAction":
        from ._schemas.customer import CustomerAddStoreActionSchema

        return CustomerAddStoreActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerAddStoreActionSchema

        return CustomerAddStoreActionSchema().dump(self)


class CustomerChangeAddressAction(CustomerUpdateAction):
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
    ) -> "CustomerChangeAddressAction":
        from ._schemas.customer import CustomerChangeAddressActionSchema

        return CustomerChangeAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerChangeAddressActionSchema

        return CustomerChangeAddressActionSchema().dump(self)


class CustomerChangeEmailAction(CustomerUpdateAction):
    email: str

    def __init__(self, *, email: str):
        self.email = email
        super().__init__(action="changeEmail")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerChangeEmailAction":
        from ._schemas.customer import CustomerChangeEmailActionSchema

        return CustomerChangeEmailActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerChangeEmailActionSchema

        return CustomerChangeEmailActionSchema().dump(self)


class CustomerRemoveAddressAction(CustomerUpdateAction):
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
    ) -> "CustomerRemoveAddressAction":
        from ._schemas.customer import CustomerRemoveAddressActionSchema

        return CustomerRemoveAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerRemoveAddressActionSchema

        return CustomerRemoveAddressActionSchema().dump(self)


class CustomerRemoveBillingAddressIdAction(CustomerUpdateAction):
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
    ) -> "CustomerRemoveBillingAddressIdAction":
        from ._schemas.customer import CustomerRemoveBillingAddressIdActionSchema

        return CustomerRemoveBillingAddressIdActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerRemoveBillingAddressIdActionSchema

        return CustomerRemoveBillingAddressIdActionSchema().dump(self)


class CustomerRemoveShippingAddressIdAction(CustomerUpdateAction):
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
    ) -> "CustomerRemoveShippingAddressIdAction":
        from ._schemas.customer import CustomerRemoveShippingAddressIdActionSchema

        return CustomerRemoveShippingAddressIdActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerRemoveShippingAddressIdActionSchema

        return CustomerRemoveShippingAddressIdActionSchema().dump(self)


class CustomerRemoveStoreAction(CustomerUpdateAction):
    store: "StoreResourceIdentifier"

    def __init__(self, *, store: "StoreResourceIdentifier"):
        self.store = store
        super().__init__(action="removeStore")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerRemoveStoreAction":
        from ._schemas.customer import CustomerRemoveStoreActionSchema

        return CustomerRemoveStoreActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerRemoveStoreActionSchema

        return CustomerRemoveStoreActionSchema().dump(self)


class CustomerSetCompanyNameAction(CustomerUpdateAction):
    #: If not defined, the company name is unset.
    company_name: typing.Optional[str]

    def __init__(self, *, company_name: typing.Optional[str] = None):
        self.company_name = company_name
        super().__init__(action="setCompanyName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerSetCompanyNameAction":
        from ._schemas.customer import CustomerSetCompanyNameActionSchema

        return CustomerSetCompanyNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerSetCompanyNameActionSchema

        return CustomerSetCompanyNameActionSchema().dump(self)


class CustomerSetCustomFieldAction(CustomerUpdateAction):
    name: str
    value: typing.Optional[typing.Any]

    def __init__(self, *, name: str, value: typing.Optional[typing.Any] = None):
        self.name = name
        self.value = value
        super().__init__(action="setCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerSetCustomFieldAction":
        from ._schemas.customer import CustomerSetCustomFieldActionSchema

        return CustomerSetCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerSetCustomFieldActionSchema

        return CustomerSetCustomFieldActionSchema().dump(self)


class CustomerSetCustomTypeAction(CustomerUpdateAction):
    #: If absent, the custom type and any existing custom fields are removed.
    type: typing.Optional["TypeResourceIdentifier"]
    #: A valid JSON object, based on the FieldDefinitions of the Type.
    #: Sets the custom fields to this value.
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
    ) -> "CustomerSetCustomTypeAction":
        from ._schemas.customer import CustomerSetCustomTypeActionSchema

        return CustomerSetCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerSetCustomTypeActionSchema

        return CustomerSetCustomTypeActionSchema().dump(self)


class CustomerSetCustomerGroupAction(CustomerUpdateAction):
    #: If not defined, the customer group is unset.
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
    ) -> "CustomerSetCustomerGroupAction":
        from ._schemas.customer import CustomerSetCustomerGroupActionSchema

        return CustomerSetCustomerGroupActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerSetCustomerGroupActionSchema

        return CustomerSetCustomerGroupActionSchema().dump(self)


class CustomerSetCustomerNumberAction(CustomerUpdateAction):
    #: It should be **unique** across a project.
    #: Once it's set, it cannot be changed.
    customer_number: typing.Optional[str]

    def __init__(self, *, customer_number: typing.Optional[str] = None):
        self.customer_number = customer_number
        super().__init__(action="setCustomerNumber")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerSetCustomerNumberAction":
        from ._schemas.customer import CustomerSetCustomerNumberActionSchema

        return CustomerSetCustomerNumberActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerSetCustomerNumberActionSchema

        return CustomerSetCustomerNumberActionSchema().dump(self)


class CustomerSetDateOfBirthAction(CustomerUpdateAction):
    #: If not defined, the date of birth is unset.
    date_of_birth: typing.Optional[datetime.date]

    def __init__(self, *, date_of_birth: typing.Optional[datetime.date] = None):
        self.date_of_birth = date_of_birth
        super().__init__(action="setDateOfBirth")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerSetDateOfBirthAction":
        from ._schemas.customer import CustomerSetDateOfBirthActionSchema

        return CustomerSetDateOfBirthActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerSetDateOfBirthActionSchema

        return CustomerSetDateOfBirthActionSchema().dump(self)


class CustomerSetDefaultBillingAddressAction(CustomerUpdateAction):
    #: If not defined, the customer's `defaultBillingAddress` is unset.
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
    ) -> "CustomerSetDefaultBillingAddressAction":
        from ._schemas.customer import CustomerSetDefaultBillingAddressActionSchema

        return CustomerSetDefaultBillingAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerSetDefaultBillingAddressActionSchema

        return CustomerSetDefaultBillingAddressActionSchema().dump(self)


class CustomerSetDefaultShippingAddressAction(CustomerUpdateAction):
    #: If not defined, the customer's `defaultShippingAddress` is unset.
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
    ) -> "CustomerSetDefaultShippingAddressAction":
        from ._schemas.customer import CustomerSetDefaultShippingAddressActionSchema

        return CustomerSetDefaultShippingAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerSetDefaultShippingAddressActionSchema

        return CustomerSetDefaultShippingAddressActionSchema().dump(self)


class CustomerSetExternalIdAction(CustomerUpdateAction):
    #: If not defined, the external ID is unset.
    external_id: typing.Optional[str]

    def __init__(self, *, external_id: typing.Optional[str] = None):
        self.external_id = external_id
        super().__init__(action="setExternalId")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerSetExternalIdAction":
        from ._schemas.customer import CustomerSetExternalIdActionSchema

        return CustomerSetExternalIdActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerSetExternalIdActionSchema

        return CustomerSetExternalIdActionSchema().dump(self)


class CustomerSetFirstNameAction(CustomerUpdateAction):
    first_name: typing.Optional[str]

    def __init__(self, *, first_name: typing.Optional[str] = None):
        self.first_name = first_name
        super().__init__(action="setFirstName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerSetFirstNameAction":
        from ._schemas.customer import CustomerSetFirstNameActionSchema

        return CustomerSetFirstNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerSetFirstNameActionSchema

        return CustomerSetFirstNameActionSchema().dump(self)


class CustomerSetKeyAction(CustomerUpdateAction):
    #: If `key` is absent or `null`, this field will be removed if it exists.
    key: typing.Optional[str]

    def __init__(self, *, key: typing.Optional[str] = None):
        self.key = key
        super().__init__(action="setKey")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomerSetKeyAction":
        from ._schemas.customer import CustomerSetKeyActionSchema

        return CustomerSetKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerSetKeyActionSchema

        return CustomerSetKeyActionSchema().dump(self)


class CustomerSetLastNameAction(CustomerUpdateAction):
    last_name: typing.Optional[str]

    def __init__(self, *, last_name: typing.Optional[str] = None):
        self.last_name = last_name
        super().__init__(action="setLastName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerSetLastNameAction":
        from ._schemas.customer import CustomerSetLastNameActionSchema

        return CustomerSetLastNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerSetLastNameActionSchema

        return CustomerSetLastNameActionSchema().dump(self)


class CustomerSetLocaleAction(CustomerUpdateAction):
    locale: typing.Optional[str]

    def __init__(self, *, locale: typing.Optional[str] = None):
        self.locale = locale
        super().__init__(action="setLocale")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerSetLocaleAction":
        from ._schemas.customer import CustomerSetLocaleActionSchema

        return CustomerSetLocaleActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerSetLocaleActionSchema

        return CustomerSetLocaleActionSchema().dump(self)


class CustomerSetMiddleNameAction(CustomerUpdateAction):
    middle_name: typing.Optional[str]

    def __init__(self, *, middle_name: typing.Optional[str] = None):
        self.middle_name = middle_name
        super().__init__(action="setMiddleName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerSetMiddleNameAction":
        from ._schemas.customer import CustomerSetMiddleNameActionSchema

        return CustomerSetMiddleNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerSetMiddleNameActionSchema

        return CustomerSetMiddleNameActionSchema().dump(self)


class CustomerSetSalutationAction(CustomerUpdateAction):
    salutation: typing.Optional[str]

    def __init__(self, *, salutation: typing.Optional[str] = None):
        self.salutation = salutation
        super().__init__(action="setSalutation")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerSetSalutationAction":
        from ._schemas.customer import CustomerSetSalutationActionSchema

        return CustomerSetSalutationActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerSetSalutationActionSchema

        return CustomerSetSalutationActionSchema().dump(self)


class CustomerSetStoresAction(CustomerUpdateAction):
    stores: typing.Optional[typing.List["StoreResourceIdentifier"]]

    def __init__(
        self, *, stores: typing.Optional[typing.List["StoreResourceIdentifier"]] = None
    ):
        self.stores = stores
        super().__init__(action="setStores")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerSetStoresAction":
        from ._schemas.customer import CustomerSetStoresActionSchema

        return CustomerSetStoresActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerSetStoresActionSchema

        return CustomerSetStoresActionSchema().dump(self)


class CustomerSetTitleAction(CustomerUpdateAction):
    title: typing.Optional[str]

    def __init__(self, *, title: typing.Optional[str] = None):
        self.title = title
        super().__init__(action="setTitle")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerSetTitleAction":
        from ._schemas.customer import CustomerSetTitleActionSchema

        return CustomerSetTitleActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerSetTitleActionSchema

        return CustomerSetTitleActionSchema().dump(self)


class CustomerSetVatIdAction(CustomerUpdateAction):
    #: If not defined, the vat Id is unset.
    vat_id: typing.Optional[str]

    def __init__(self, *, vat_id: typing.Optional[str] = None):
        self.vat_id = vat_id
        super().__init__(action="setVatId")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerSetVatIdAction":
        from ._schemas.customer import CustomerSetVatIdActionSchema

        return CustomerSetVatIdActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer import CustomerSetVatIdActionSchema

        return CustomerSetVatIdActionSchema().dump(self)
