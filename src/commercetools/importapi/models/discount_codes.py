# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import ImportResource

if typing.TYPE_CHECKING:
    from .common import CartDiscountKeyReference, LocalizedString
    from .customfields import Custom

__all__ = ["DiscountCodeImport"]


class DiscountCodeImport(ImportResource):
    """The data representation for a Discount Code to be imported that is persisted as a [Discount Code](/../api/projects/discountCodes#discountcode) in the Project."""

    #: Maps to `DiscountCode.name`.
    name: typing.Optional["LocalizedString"]
    #: Maps to `DiscountCode.description`.
    description: typing.Optional["LocalizedString"]
    #: User-defined unique identifier of the DiscountCode that is used by the customer to apply the discount.
    code: str
    #: Reference to CartDiscounts that can be applied to the Cart once the DiscountCode is applied.
    cart_discounts: typing.List["CartDiscountKeyReference"]
    #: DiscountCode can only be applied to Carts that match this predicate.
    cart_predicate: typing.Optional[str]
    #: Indicates if the DiscountCode is active and can be applied to the Cart.
    is_active: bool
    #: Number of times the DiscountCode can be applied. DiscountCode application is counted at the time of Order creation or update. However, Order cancellation or deletion does not decrement the count.
    max_applications: typing.Optional[int]
    #: Number of times the DiscountCode can be applied per Customer (anonymous Carts are not supported). DiscountCode application is counted at the time of Order creation or update. However, Order cancellation or deletion does not decrement the count.
    max_applications_per_customer: typing.Optional[int]
    #: Groups to which the DiscountCode belongs.
    groups: typing.Optional[typing.List["str"]]
    #: Date and time (UTC) from which the DiscountCode is effective.
    valid_from: typing.Optional[datetime.datetime]
    #: Date and time (UTC) until which the DiscountCode is effective.
    valid_until: typing.Optional[datetime.datetime]
    #: Custom Fields of the DiscountCode.
    custom: typing.Optional["Custom"]

    def __init__(
        self,
        *,
        key: str,
        name: typing.Optional["LocalizedString"] = None,
        description: typing.Optional["LocalizedString"] = None,
        code: str,
        cart_discounts: typing.List["CartDiscountKeyReference"],
        cart_predicate: typing.Optional[str] = None,
        is_active: bool,
        max_applications: typing.Optional[int] = None,
        max_applications_per_customer: typing.Optional[int] = None,
        groups: typing.Optional[typing.List["str"]] = None,
        valid_from: typing.Optional[datetime.datetime] = None,
        valid_until: typing.Optional[datetime.datetime] = None,
        custom: typing.Optional["Custom"] = None
    ):
        self.name = name
        self.description = description
        self.code = code
        self.cart_discounts = cart_discounts
        self.cart_predicate = cart_predicate
        self.is_active = is_active
        self.max_applications = max_applications
        self.max_applications_per_customer = max_applications_per_customer
        self.groups = groups
        self.valid_from = valid_from
        self.valid_until = valid_until
        self.custom = custom

        super().__init__(key=key)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "DiscountCodeImport":
        from ._schemas.discount_codes import DiscountCodeImportSchema

        return DiscountCodeImportSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.discount_codes import DiscountCodeImportSchema

        return DiscountCodeImportSchema().dump(self)
