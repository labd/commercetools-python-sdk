# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import ImportResource

if typing.TYPE_CHECKING:
    from .common import Address, CustomerGroupKeyReference
    from .customfields import Custom


class CustomerImport(ImportResource):
    """Import representation for a customer."""

    #: Maps to `Customer.customerNumber`.
    customer_number: typing.Optional["str"]
    #: Maps to `Customer.email`.
    email: "str"
    #: Maps to `Customer.password`.
    password: "str"
    #: Maps to `Customer.firstName`.
    first_name: typing.Optional["str"]
    #: Maps to `Customer.lastName`.
    last_name: typing.Optional["str"]
    #: Maps to `Customer.middleName`.
    middle_name: typing.Optional["str"]
    #: Maps to `Customer.title`.
    title: typing.Optional["str"]
    #: Maps to `Customer.salutation`.
    salutation: typing.Optional["str"]
    #: Maps to `Customer.externalId`.
    external_id: typing.Optional["str"]
    #: Maps to `Customer.dateOfBirth`.
    date_of_birth: typing.Optional["datetime.date"]
    #: Maps to `Customer.companyName`.
    company_name: typing.Optional["str"]
    #: Maps to `Customer.vatId`.
    vat_id: typing.Optional["str"]
    #: Maps to `Customer.isEmailVerified`.
    is_email_verified: typing.Optional["bool"]
    #: References a customer group by its key.
    #:
    #: The customer group referenced
    #: must already exist in the commercetools project, or the
    #: import operation state is set to `Unresolved`.
    customer_group: typing.Optional["CustomerGroupKeyReference"]
    #: Maps to `Customer.addresses`.
    addresses: typing.Optional[typing.List["Address"]]
    #: Maps to `Customer.defaultBillingAddress`.
    default_billing_address: typing.Optional["Address"]
    #: Maps to `Customer.billingAddresses`.
    billing_addresses: typing.Optional["Address"]
    #: Maps to `Customer.defaultShippingAddress`.
    default_shipping_address: typing.Optional["Address"]
    #: Maps to `Customer.shippingAddresses`.
    shipping_addresses: typing.Optional["Address"]
    #: Maps to `Customer.locale`.
    locale: typing.Optional["str"]
    #: The custom fields for this Customer.
    custom: typing.Optional["Custom"]

    def __init__(
        self,
        *,
        key: "str",
        customer_number: typing.Optional["str"] = None,
        email: "str",
        password: "str",
        first_name: typing.Optional["str"] = None,
        last_name: typing.Optional["str"] = None,
        middle_name: typing.Optional["str"] = None,
        title: typing.Optional["str"] = None,
        salutation: typing.Optional["str"] = None,
        external_id: typing.Optional["str"] = None,
        date_of_birth: typing.Optional["datetime.date"] = None,
        company_name: typing.Optional["str"] = None,
        vat_id: typing.Optional["str"] = None,
        is_email_verified: typing.Optional["bool"] = None,
        customer_group: typing.Optional["CustomerGroupKeyReference"] = None,
        addresses: typing.Optional[typing.List["Address"]] = None,
        default_billing_address: typing.Optional["Address"] = None,
        billing_addresses: typing.Optional["Address"] = None,
        default_shipping_address: typing.Optional["Address"] = None,
        shipping_addresses: typing.Optional["Address"] = None,
        locale: typing.Optional["str"] = None,
        custom: typing.Optional["Custom"] = None
    ):
        self.customer_number = customer_number
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.title = title
        self.salutation = salutation
        self.external_id = external_id
        self.date_of_birth = date_of_birth
        self.company_name = company_name
        self.vat_id = vat_id
        self.is_email_verified = is_email_verified
        self.customer_group = customer_group
        self.addresses = addresses
        self.default_billing_address = default_billing_address
        self.billing_addresses = billing_addresses
        self.default_shipping_address = default_shipping_address
        self.shipping_addresses = shipping_addresses
        self.locale = locale
        self.custom = custom
        super().__init__(key=key)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomerImport":
        from ._schemas.customers import CustomerImportSchema

        return CustomerImportSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customers import CustomerImportSchema

        return CustomerImportSchema().dump(self)
