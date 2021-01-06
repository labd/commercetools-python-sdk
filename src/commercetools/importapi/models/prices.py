# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import ImportResource

if typing.TYPE_CHECKING:
    from .common import (
        ChannelKeyReference,
        CustomerGroupKeyReference,
        DiscountedPrice,
        PriceTier,
        ProductKeyReference,
        ProductVariantKeyReference,
        TypedMoney,
    )
    from .customfields import Custom

__all__ = ["PriceImport", "SubRate", "TaxRate"]


class SubRate(_BaseType):
    name: str
    amount: float

    def __init__(self, *, name: str, amount: float):
        self.name = name
        self.amount = amount
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SubRate":
        from ._schemas.prices import SubRateSchema

        return SubRateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.prices import SubRateSchema

        return SubRateSchema().dump(self)


class TaxRate(_BaseType):
    id: typing.Optional[str]
    name: str
    amount: float
    included_in_price: bool
    #: A two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    country: str
    state: typing.Optional[str]
    sub_rates: typing.Optional[typing.List["SubRate"]]

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        name: str,
        amount: float,
        included_in_price: bool,
        country: str,
        state: typing.Optional[str] = None,
        sub_rates: typing.Optional[typing.List["SubRate"]] = None
    ):
        self.id = id
        self.name = name
        self.amount = amount
        self.included_in_price = included_in_price
        self.country = country
        self.state = state
        self.sub_rates = sub_rates
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TaxRate":
        from ._schemas.prices import TaxRateSchema

        return TaxRateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.prices import TaxRateSchema

        return TaxRateSchema().dump(self)


class PriceImport(ImportResource):
    """Imports a product variant's prices."""

    #: Maps to `Price.value`.
    #:
    #: The Import API **only** supports `centPrecision` prices.
    value: "TypedMoney"
    #: Maps to `Price.county`.
    country: typing.Optional[str]
    #: Maps to `Price.validFrom`.
    valid_from: typing.Optional[datetime.datetime]
    #: Maps to `Price.validUntil`.
    valid_until: typing.Optional[datetime.datetime]
    #: References a customer group by its key.
    #:
    #: The customer group referenced
    #: must already exist in the commercetools project, or the
    #: import operation state is set to `Unresolved`.
    customer_group: typing.Optional["CustomerGroupKeyReference"]
    #: References a channel by its key.
    #:
    #: The channel referenced
    #: must already exist in the commercetools project, or the
    #: import operation state is set to `Unresolved`.
    channel: typing.Optional["ChannelKeyReference"]
    #: Sets a discounted price from an external service.
    discounted: typing.Optional["DiscountedPrice"]
    #: Only the Price updates will be published to `staged` and `current` projection.
    publish: typing.Optional[bool]
    #: The tiered prices for this price.
    tiers: typing.Optional[typing.List["PriceTier"]]
    #: The custom fields for this price.
    custom: typing.Optional["Custom"]
    #: The product variant in which this price is contained.
    #:
    #: The product variant referenced
    #: must already exist in the commercetools project, or the
    #: import operation state is set to `Unresolved`.
    product_variant: "ProductVariantKeyReference"
    #: The product in which this product variant containong the price is contained. Maps to `ProductVariant.product`.
    #:
    #: The product referenced
    #: must already exist in the commercetools project, or the
    #: import operation state is set to `Unresolved`.
    product: "ProductKeyReference"

    def __init__(
        self,
        *,
        key: str,
        value: "TypedMoney",
        country: typing.Optional[str] = None,
        valid_from: typing.Optional[datetime.datetime] = None,
        valid_until: typing.Optional[datetime.datetime] = None,
        customer_group: typing.Optional["CustomerGroupKeyReference"] = None,
        channel: typing.Optional["ChannelKeyReference"] = None,
        discounted: typing.Optional["DiscountedPrice"] = None,
        publish: typing.Optional[bool] = None,
        tiers: typing.Optional[typing.List["PriceTier"]] = None,
        custom: typing.Optional["Custom"] = None,
        product_variant: "ProductVariantKeyReference",
        product: "ProductKeyReference"
    ):
        self.value = value
        self.country = country
        self.valid_from = valid_from
        self.valid_until = valid_until
        self.customer_group = customer_group
        self.channel = channel
        self.discounted = discounted
        self.publish = publish
        self.tiers = tiers
        self.custom = custom
        self.product_variant = product_variant
        self.product = product
        super().__init__(key=key)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "PriceImport":
        from ._schemas.prices import PriceImportSchema

        return PriceImportSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.prices import PriceImportSchema

        return PriceImportSchema().dump(self)
