# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import ImportResource

if typing.TYPE_CHECKING:
    from .common import (
        Address,
        CartDiscountKeyReference,
        ChannelKeyReference,
        CustomerGroupKeyReference,
        CustomerKeyReference,
        DiscountedPrice,
        Image,
        LocalizedString,
        Money,
        PriceTier,
        ProductKeyReference,
        ShippingMethodKeyReference,
        StateKeyReference,
        TaxCategoryKeyReference,
        TypedMoney,
    )
    from .customfields import Custom
    from .prices import SubRate, TaxRate
    from .productvariants import Attribute


class ItemState(_BaseType):
    """The item's state.
    
    """

    quantity: "float"
    #: Maps to `ItemState.state`.
    state: "StateKeyReference"

    def __init__(self, *, quantity: "float", state: "StateKeyReference"):
        self.quantity = quantity
        self.state = state
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ItemState":
        from ._schemas.orders import ItemStateSchema

        return ItemStateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.orders import ItemStateSchema

        return ItemStateSchema().dump(self)


class ItemShippingTarget(_BaseType):
    """The item's shipping target.
    
    """

    #: Maps to `ItemShippingTarget.addressKey`.
    address_key: "str"
    #: Maps to `ItemShippingTarget.quantity`.
    quantity: "float"

    def __init__(self, *, address_key: "str", quantity: "float"):
        self.address_key = address_key
        self.quantity = quantity
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ItemShippingTarget":
        from ._schemas.orders import ItemShippingTargetSchema

        return ItemShippingTargetSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.orders import ItemShippingTargetSchema

        return ItemShippingTargetSchema().dump(self)


class ItemShippingDetailsDraft(_BaseType):
    #: Maps to `ItemShippingDetailsDraft.targets`.
    targets: typing.List["ItemShippingTarget"]

    def __init__(self, *, targets: typing.List["ItemShippingTarget"]):
        self.targets = targets
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ItemShippingDetailsDraft":
        from ._schemas.orders import ItemShippingDetailsDraftSchema

        return ItemShippingDetailsDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.orders import ItemShippingDetailsDraftSchema

        return ItemShippingDetailsDraftSchema().dump(self)


class LineItemPrice(_BaseType):
    #: Maps to `Price.value`.
    value: "TypedMoney"
    #: Maps to `Price.county`.
    country: typing.Optional["str"]
    #: Maps to `Price.validFrom`.
    valid_from: typing.Optional["datetime.datetime"]
    #: Maps to `Price.validUntil`.
    valid_until: typing.Optional["datetime.datetime"]
    #: References a customer group by its key.
    customer_group: typing.Optional["CustomerGroupKeyReference"]
    #: References a channel by its key.
    channel: typing.Optional["ChannelKeyReference"]
    #: Sets a discounted price from an external service.
    discounted: typing.Optional["DiscountedPrice"]
    #: The tiered prices for this price.
    tiers: typing.Optional[typing.List["PriceTier"]]
    #: Maps to `Price.custom`.
    custom: typing.Optional["Custom"]

    def __init__(
        self,
        *,
        value: "TypedMoney",
        country: typing.Optional["str"] = None,
        valid_from: typing.Optional["datetime.datetime"] = None,
        valid_until: typing.Optional["datetime.datetime"] = None,
        customer_group: typing.Optional["CustomerGroupKeyReference"] = None,
        channel: typing.Optional["ChannelKeyReference"] = None,
        discounted: typing.Optional["DiscountedPrice"] = None,
        tiers: typing.Optional[typing.List["PriceTier"]] = None,
        custom: typing.Optional["Custom"] = None
    ):
        self.value = value
        self.country = country
        self.valid_from = valid_from
        self.valid_until = valid_until
        self.customer_group = customer_group
        self.channel = channel
        self.discounted = discounted
        self.tiers = tiers
        self.custom = custom
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "LineItemPrice":
        from ._schemas.orders import LineItemPriceSchema

        return LineItemPriceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.orders import LineItemPriceSchema

        return LineItemPriceSchema().dump(self)


class LineItemProductVariantImportDraft(_BaseType):
    #: Maps to `ProductVariant.product`.
    product: typing.Optional["ProductKeyReference"]
    #: Maps to `ProductVariantImportDraft.sku`.
    sku: typing.Optional["str"]
    #: Maps to `ProductVariantImportDraft.prices`
    prices: typing.Optional[typing.List["LineItemPrice"]]
    #: Maps to `ProductVariantImportDraft.attributes`
    attributes: typing.Optional[typing.List["Attribute"]]
    #: Maps to `ProductVariantImportDraft.images`.
    images: typing.Optional[typing.List["Image"]]

    def __init__(
        self,
        *,
        product: typing.Optional["ProductKeyReference"] = None,
        sku: typing.Optional["str"] = None,
        prices: typing.Optional[typing.List["LineItemPrice"]] = None,
        attributes: typing.Optional[typing.List["Attribute"]] = None,
        images: typing.Optional[typing.List["Image"]] = None
    ):
        self.product = product
        self.sku = sku
        self.prices = prices
        self.attributes = attributes
        self.images = images
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "LineItemProductVariantImportDraft":
        from ._schemas.orders import LineItemProductVariantImportDraftSchema

        return LineItemProductVariantImportDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.orders import LineItemProductVariantImportDraftSchema

        return LineItemProductVariantImportDraftSchema().dump(self)


class LineItemImportDraft(_BaseType):
    """Represents an individual line item in an Order. A line item is a snapshot of a product at the time it was added to the order.
    
    You cannot create an order which includes line operations that do not exist in the project or have been deleted.
    Products and variants referenced by a line item must already exist in the commercetools project.
    
    """

    #: Maps to `LineItem.productId`.
    product: typing.Optional["ProductKeyReference"]
    #: Maps to `LineItem.name`.
    name: "LocalizedString"
    #: Maps to `ProductVariantImportDraft`.
    variant: "LineItemProductVariantImportDraft"
    #: Maps to `LineItem.price`.
    price: "LineItemPrice"
    #: Maps to `LineItem.quantity`.
    quantity: "float"
    state: typing.Optional[typing.List["ItemState"]]
    #: References a supply channel. Maps to `LineItem.supplyChannel`.
    #:
    #: The supply channel referenced must already exist
    #: in the commercetools project, or the
    #: import operation state is set to `Unresolved`.
    supply_channel: typing.Optional["ChannelKeyReference"]
    #: References a distribution channel. Maps to `LineItem.distributionChannel`.
    #:
    #: The distribution channel referenced must already exist
    #: in the commercetools project, or the
    #: import operation state is set to `Unresolved`.
    distribution_channel: typing.Optional["ChannelKeyReference"]
    #: Maps to `LineItem.taxRate`.
    tax_rate: typing.Optional["TaxRate"]
    #: Maps to LineItem.shippingDetails.
    shipping_details: typing.Optional["ItemShippingDetailsDraft"]

    def __init__(
        self,
        *,
        product: typing.Optional["ProductKeyReference"] = None,
        name: "LocalizedString",
        variant: "LineItemProductVariantImportDraft",
        price: "LineItemPrice",
        quantity: "float",
        state: typing.Optional[typing.List["ItemState"]] = None,
        supply_channel: typing.Optional["ChannelKeyReference"] = None,
        distribution_channel: typing.Optional["ChannelKeyReference"] = None,
        tax_rate: typing.Optional["TaxRate"] = None,
        shipping_details: typing.Optional["ItemShippingDetailsDraft"] = None
    ):
        self.product = product
        self.name = name
        self.variant = variant
        self.price = price
        self.quantity = quantity
        self.state = state
        self.supply_channel = supply_channel
        self.distribution_channel = distribution_channel
        self.tax_rate = tax_rate
        self.shipping_details = shipping_details
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "LineItemImportDraft":
        from ._schemas.orders import LineItemImportDraftSchema

        return LineItemImportDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.orders import LineItemImportDraftSchema

        return LineItemImportDraftSchema().dump(self)


class ShippingRateTierType(enum.Enum):
    CART_VALUE = "CartValue"
    CART_CLASSIFICATION = "CartClassification"
    CART_SCORE = "CartScore"


class ShippingRatePriceTier(_BaseType):
    type: "ShippingRateTierType"

    def __init__(self, *, type: "ShippingRateTierType"):
        self.type = type
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ShippingRatePriceTier":
        from ._schemas.orders import ShippingRatePriceTierSchema

        return ShippingRatePriceTierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.orders import ShippingRatePriceTierSchema

        return ShippingRatePriceTierSchema().dump(self)


class CartClassificationTier(ShippingRatePriceTier):
    value: "str"
    price: "Money"
    tiers: typing.List["ShippingRatePriceTier"]
    is_matching: typing.Optional["bool"]

    def __init__(
        self,
        *,
        value: "str",
        price: "Money",
        tiers: typing.List["ShippingRatePriceTier"],
        is_matching: typing.Optional["bool"] = None
    ):
        self.value = value
        self.price = price
        self.tiers = tiers
        self.is_matching = is_matching
        super().__init__(type=ShippingRateTierType.CART_CLASSIFICATION)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartClassificationTier":
        from ._schemas.orders import CartClassificationTierSchema

        return CartClassificationTierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.orders import CartClassificationTierSchema

        return CartClassificationTierSchema().dump(self)


class ShippingRateDraft(_BaseType):
    price: "Money"
    free_above: typing.Optional["Money"]
    tiers: typing.Optional[typing.List["ShippingRatePriceTier"]]

    def __init__(
        self,
        *,
        price: "Money",
        free_above: typing.Optional["Money"] = None,
        tiers: typing.Optional[typing.List["ShippingRatePriceTier"]] = None
    ):
        self.price = price
        self.free_above = free_above
        self.tiers = tiers
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ShippingRateDraft":
        from ._schemas.orders import ShippingRateDraftSchema

        return ShippingRateDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.orders import ShippingRateDraftSchema

        return ShippingRateDraftSchema().dump(self)


class ParcelMeasurements(_BaseType):
    height_in_millimeter: typing.Optional["float"]
    length_in_millimeter: typing.Optional["float"]
    width_in_millimeter: typing.Optional["float"]
    weight_in_gram: typing.Optional["float"]

    def __init__(
        self,
        *,
        height_in_millimeter: typing.Optional["float"] = None,
        length_in_millimeter: typing.Optional["float"] = None,
        width_in_millimeter: typing.Optional["float"] = None,
        weight_in_gram: typing.Optional["float"] = None
    ):
        self.height_in_millimeter = height_in_millimeter
        self.length_in_millimeter = length_in_millimeter
        self.width_in_millimeter = width_in_millimeter
        self.weight_in_gram = weight_in_gram
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ParcelMeasurements":
        from ._schemas.orders import ParcelMeasurementsSchema

        return ParcelMeasurementsSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.orders import ParcelMeasurementsSchema

        return ParcelMeasurementsSchema().dump(self)


class TrackingData(_BaseType):
    tracking_id: typing.Optional["str"]
    carrier: typing.Optional["str"]
    provider: typing.Optional["str"]
    provider_transaction: typing.Optional["str"]
    is_return: typing.Optional["bool"]

    def __init__(
        self,
        *,
        tracking_id: typing.Optional["str"] = None,
        carrier: typing.Optional["str"] = None,
        provider: typing.Optional["str"] = None,
        provider_transaction: typing.Optional["str"] = None,
        is_return: typing.Optional["bool"] = None
    ):
        self.tracking_id = tracking_id
        self.carrier = carrier
        self.provider = provider
        self.provider_transaction = provider_transaction
        self.is_return = is_return
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TrackingData":
        from ._schemas.orders import TrackingDataSchema

        return TrackingDataSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.orders import TrackingDataSchema

        return TrackingDataSchema().dump(self)


class DeliveryItem(_BaseType):
    id: "str"
    quantity: "float"

    def __init__(self, *, id: "str", quantity: "float"):
        self.id = id
        self.quantity = quantity
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "DeliveryItem":
        from ._schemas.orders import DeliveryItemSchema

        return DeliveryItemSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.orders import DeliveryItemSchema

        return DeliveryItemSchema().dump(self)


class Parcel(_BaseType):
    id: "str"
    created_at: "datetime.datetime"
    measurements: typing.Optional["ParcelMeasurements"]
    tracking_data: typing.Optional["TrackingData"]
    items: typing.Optional[typing.List["DeliveryItem"]]

    def __init__(
        self,
        *,
        id: "str",
        created_at: "datetime.datetime",
        measurements: typing.Optional["ParcelMeasurements"] = None,
        tracking_data: typing.Optional["TrackingData"] = None,
        items: typing.Optional[typing.List["DeliveryItem"]] = None
    ):
        self.id = id
        self.created_at = created_at
        self.measurements = measurements
        self.tracking_data = tracking_data
        self.items = items
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Parcel":
        from ._schemas.orders import ParcelSchema

        return ParcelSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.orders import ParcelSchema

        return ParcelSchema().dump(self)


class Delivery(_BaseType):
    id: "str"
    created_at: "datetime.datetime"
    items: typing.List["DeliveryItem"]
    parcels: typing.List["Parcel"]
    address: typing.Optional["Address"]

    def __init__(
        self,
        *,
        id: "str",
        created_at: "datetime.datetime",
        items: typing.List["DeliveryItem"],
        parcels: typing.List["Parcel"],
        address: typing.Optional["Address"] = None
    ):
        self.id = id
        self.created_at = created_at
        self.items = items
        self.parcels = parcels
        self.address = address
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Delivery":
        from ._schemas.orders import DeliverySchema

        return DeliverySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.orders import DeliverySchema

        return DeliverySchema().dump(self)


class DiscountedLineItemPortion(_BaseType):
    #: References a cart discount by its key.
    discount: "CartDiscountKeyReference"
    discounted_amount: "Money"

    def __init__(
        self, *, discount: "CartDiscountKeyReference", discounted_amount: "Money"
    ):
        self.discount = discount
        self.discounted_amount = discounted_amount
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DiscountedLineItemPortion":
        from ._schemas.orders import DiscountedLineItemPortionSchema

        return DiscountedLineItemPortionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.orders import DiscountedLineItemPortionSchema

        return DiscountedLineItemPortionSchema().dump(self)


class DiscountedLineItemPriceDraft(_BaseType):
    value: "Money"
    included_discounts: typing.List["DiscountedLineItemPortion"]

    def __init__(
        self,
        *,
        value: "Money",
        included_discounts: typing.List["DiscountedLineItemPortion"]
    ):
        self.value = value
        self.included_discounts = included_discounts
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DiscountedLineItemPriceDraft":
        from ._schemas.orders import DiscountedLineItemPriceDraftSchema

        return DiscountedLineItemPriceDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.orders import DiscountedLineItemPriceDraftSchema

        return DiscountedLineItemPriceDraftSchema().dump(self)


class ShippingMethodState(enum.Enum):
    DOES_NOT_MATCH_CART = "DoesNotMatchCart"
    MATCHES_CART = "MatchesCart"


class ShippingInfoImportDraft(_BaseType):
    """Maps to an order's `shippingInfo` property. This field is usually populated by the cart assosciated with
    the order, but when importing orders you must provide a draft representation as a part of the OrderImport.
    
    """

    shipping_method_name: "str"
    price: "TypedMoney"
    shipping_rate: "ShippingRateDraft"
    tax_rate: typing.Optional["TaxRate"]
    #: References a tax category by its key.
    tax_category: typing.Optional["TaxCategoryKeyReference"]
    #: References a shipping method by its key.
    shipping_method: typing.Optional["ShippingMethodKeyReference"]
    deliveries: typing.Optional[typing.List["Delivery"]]
    discounted_price: typing.Optional["DiscountedLineItemPriceDraft"]
    shipping_method_state: typing.Optional["ShippingMethodState"]

    def __init__(
        self,
        *,
        shipping_method_name: "str",
        price: "TypedMoney",
        shipping_rate: "ShippingRateDraft",
        tax_rate: typing.Optional["TaxRate"] = None,
        tax_category: typing.Optional["TaxCategoryKeyReference"] = None,
        shipping_method: typing.Optional["ShippingMethodKeyReference"] = None,
        deliveries: typing.Optional[typing.List["Delivery"]] = None,
        discounted_price: typing.Optional["DiscountedLineItemPriceDraft"] = None,
        shipping_method_state: typing.Optional["ShippingMethodState"] = None
    ):
        self.shipping_method_name = shipping_method_name
        self.price = price
        self.shipping_rate = shipping_rate
        self.tax_rate = tax_rate
        self.tax_category = tax_category
        self.shipping_method = shipping_method
        self.deliveries = deliveries
        self.discounted_price = discounted_price
        self.shipping_method_state = shipping_method_state
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShippingInfoImportDraft":
        from ._schemas.orders import ShippingInfoImportDraftSchema

        return ShippingInfoImportDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.orders import ShippingInfoImportDraftSchema

        return ShippingInfoImportDraftSchema().dump(self)


class ExternalTaxRateDraft(_BaseType):
    name: "str"
    amount: typing.Optional["float"]
    country: "str"
    state: typing.Optional["str"]
    sub_rates: typing.Optional[typing.List["SubRate"]]
    included_in_price: typing.Optional["bool"]

    def __init__(
        self,
        *,
        name: "str",
        amount: typing.Optional["float"] = None,
        country: "str",
        state: typing.Optional["str"] = None,
        sub_rates: typing.Optional[typing.List["SubRate"]] = None,
        included_in_price: typing.Optional["bool"] = None
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
        from ._schemas.orders import ExternalTaxRateDraftSchema

        return ExternalTaxRateDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.orders import ExternalTaxRateDraftSchema

        return ExternalTaxRateDraftSchema().dump(self)


class CustomLineItemTaxedPrice(_BaseType):
    total_net: "TypedMoney"
    total_gross: "TypedMoney"

    def __init__(self, *, total_net: "TypedMoney", total_gross: "TypedMoney"):
        self.total_net = total_net
        self.total_gross = total_gross
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomLineItemTaxedPrice":
        from ._schemas.orders import CustomLineItemTaxedPriceSchema

        return CustomLineItemTaxedPriceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.orders import CustomLineItemTaxedPriceSchema

        return CustomLineItemTaxedPriceSchema().dump(self)


class CustomLineItemDraft(_BaseType):
    name: "LocalizedString"
    money: "TypedMoney"
    taxed_price: typing.Optional["CustomLineItemTaxedPrice"]
    total_price: "TypedMoney"
    slug: "str"
    quantity: "float"
    state: typing.Optional[typing.List["ItemState"]]
    #: References a tax category by its key.
    tax_category: typing.Optional["TaxCategoryKeyReference"]
    tax_rate: typing.Optional["TaxRate"]
    external_tax_rate: typing.Optional["ExternalTaxRateDraft"]
    discounted_price_per_quantity: typing.Optional[
        typing.List["DiscountedLineItemPriceDraft"]
    ]
    shipping_details: typing.Optional["ItemShippingDetailsDraft"]

    def __init__(
        self,
        *,
        name: "LocalizedString",
        money: "TypedMoney",
        taxed_price: typing.Optional["CustomLineItemTaxedPrice"] = None,
        total_price: "TypedMoney",
        slug: "str",
        quantity: "float",
        state: typing.Optional[typing.List["ItemState"]] = None,
        tax_category: typing.Optional["TaxCategoryKeyReference"] = None,
        tax_rate: typing.Optional["TaxRate"] = None,
        external_tax_rate: typing.Optional["ExternalTaxRateDraft"] = None,
        discounted_price_per_quantity: typing.Optional[
            typing.List["DiscountedLineItemPriceDraft"]
        ] = None,
        shipping_details: typing.Optional["ItemShippingDetailsDraft"] = None
    ):
        self.name = name
        self.money = money
        self.taxed_price = taxed_price
        self.total_price = total_price
        self.slug = slug
        self.quantity = quantity
        self.state = state
        self.tax_category = tax_category
        self.tax_rate = tax_rate
        self.external_tax_rate = external_tax_rate
        self.discounted_price_per_quantity = discounted_price_per_quantity
        self.shipping_details = shipping_details
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomLineItemDraft":
        from ._schemas.orders import CustomLineItemDraftSchema

        return CustomLineItemDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.orders import CustomLineItemDraftSchema

        return CustomLineItemDraftSchema().dump(self)


class TaxPortion(_BaseType):
    name: typing.Optional["str"]
    rate: "float"
    amount: "TypedMoney"

    def __init__(
        self,
        *,
        name: typing.Optional["str"] = None,
        rate: "float",
        amount: "TypedMoney"
    ):
        self.name = name
        self.rate = rate
        self.amount = amount
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TaxPortion":
        from ._schemas.orders import TaxPortionSchema

        return TaxPortionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.orders import TaxPortionSchema

        return TaxPortionSchema().dump(self)


class TaxedPrice(_BaseType):
    #: Maps to `TaxedPrice.totalNet`.
    total_net: "Money"
    #: Maps to `TaxedPrice.totalGross`.
    total_gross: "Money"
    #: Maps to `TaxedPrice.taxPortions`.
    tax_portions: typing.List["TaxPortion"]

    def __init__(
        self,
        *,
        total_net: "Money",
        total_gross: "Money",
        tax_portions: typing.List["TaxPortion"]
    ):
        self.total_net = total_net
        self.total_gross = total_gross
        self.tax_portions = tax_portions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TaxedPrice":
        from ._schemas.orders import TaxedPriceSchema

        return TaxedPriceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.orders import TaxedPriceSchema

        return TaxedPriceSchema().dump(self)


class OrderState(enum.Enum):
    """Maps to `Order.orderState`.
   """

    OPEN = "Open"
    CONFIRMED = "Confirmed"
    COMPLETE = "Complete"
    CANCELLED = "Cancelled"


class ShipmentState(enum.Enum):
    """Maps to `Order.shipmentState`.
   """

    SHIPPED = "Shipped"
    READY = "Ready"
    PENDING = "Pending"
    DELAYED = "Delayed"
    PARTIAL = "Partial"
    BACKORDER = "Backorder"


class PaymentState(enum.Enum):
    """Maps to `Order.paymentState`.
   """

    BALANCE_DUE = "BalanceDue"
    FAILED = "Failed"
    PENDING = "Pending"
    CREDIT_OWED = "CreditOwed"
    PAID = "Paid"


class InventoryMode(enum.Enum):
    """Maps to `Order.inventoryMode`.
   """

    TRACK_ONLY = "TrackOnly"
    RESERVE_ON_ORDER = "ReserveOnOrder"


class RoundingMode(enum.Enum):
    """Maps to `Order.taxRoundingMode`.
   """

    HALF_EVEN = "HalfEven"
    HALF_UP = "HalfUp"
    HALF_DOWN = "HalfDown"


class TaxCalculationMode(enum.Enum):
    """Maps to `Order.taxCalculationMode`.
   """

    LINE_ITEM_LEVEL = "LineItemLevel"
    UNIT_PRICE_LEVEL = "UnitPriceLevel"


class CartOrigin(enum.Enum):
    """Maps to `Order.origin`.
   """

    CUSTOMER = "Customer"
    MERCHANT = "Merchant"


class OrderImport(ImportResource):
    """Import representation for an order.
    
    In commercetools, you can import an order using the
    [Create Order by Import](https://docs.commercetools.com/http-api-projects-orders-import.html#create-an-order-by-import)
    endpoint method instead of creating it from a cart.
    
    The order import draft is a snapshot of an order at the time it was imported.
    
    """

    #: Maps to `Order.orderNumber`.
    order_number: typing.Optional["str"]
    #: References a customer by its key.
    customer: typing.Optional["CustomerKeyReference"]
    #: Maps to `Order.customerEmail`.
    customer_email: typing.Optional["str"]
    #: Maps to `Order.lineItems`.
    line_items: typing.Optional[typing.List["LineItemImportDraft"]]
    #: Maps to `Order.customLineItems`
    custom_line_items: typing.Optional[typing.List["CustomLineItemDraft"]]
    #: Maps to `Order.totalPrice`.
    total_price: "TypedMoney"
    #: Maps to `Order.taxedPrice`.
    taxed_price: typing.Optional["TaxedPrice"]
    #: Maps to `Order.shippingAddress`.
    shipping_address: typing.Optional["Address"]
    #: Maps to `Order.billingAddress`.
    billing_address: typing.Optional["Address"]
    #: Maps to `Order.customerGroup`.
    customer_group: typing.Optional["CustomerGroupKeyReference"]
    #: Maps to `Order.country`.
    country: typing.Optional["str"]
    #: Maps to `Order.orderState`.
    order_state: typing.Optional["OrderState"]
    #: Maps to `Order.shipmentState`.
    shipment_state: typing.Optional["ShipmentState"]
    #: Maps to `Order.paymentState`.
    payment_state: typing.Optional["PaymentState"]
    #: Maps to `Order.shippingInfo`.
    shipping_info: typing.Optional["ShippingInfoImportDraft"]
    #: Maps to `Order.completedAt`.
    completed_at: typing.Optional["datetime.datetime"]
    #: Maps to `Order.custom`.
    custom: typing.Optional["Custom"]
    #: Maps to `Order.inventoryMode`.
    inventory_mode: typing.Optional["InventoryMode"]
    #: Maps to `Order.taxRoundingMode`.
    tax_rounding_mode: typing.Optional["RoundingMode"]
    #: Maps to `Order.taxCalculationMode`.
    tax_calculation_mode: typing.Optional["TaxCalculationMode"]
    #: Maps to `Order.origin`.
    origin: typing.Optional["CartOrigin"]
    #: Maps to `Order.itemShippingAddresses`.
    item_shipping_addresses: typing.Optional[typing.List["Address"]]

    def __init__(
        self,
        *,
        key: "str",
        order_number: typing.Optional["str"] = None,
        customer: typing.Optional["CustomerKeyReference"] = None,
        customer_email: typing.Optional["str"] = None,
        line_items: typing.Optional[typing.List["LineItemImportDraft"]] = None,
        custom_line_items: typing.Optional[typing.List["CustomLineItemDraft"]] = None,
        total_price: "TypedMoney",
        taxed_price: typing.Optional["TaxedPrice"] = None,
        shipping_address: typing.Optional["Address"] = None,
        billing_address: typing.Optional["Address"] = None,
        customer_group: typing.Optional["CustomerGroupKeyReference"] = None,
        country: typing.Optional["str"] = None,
        order_state: typing.Optional["OrderState"] = None,
        shipment_state: typing.Optional["ShipmentState"] = None,
        payment_state: typing.Optional["PaymentState"] = None,
        shipping_info: typing.Optional["ShippingInfoImportDraft"] = None,
        completed_at: typing.Optional["datetime.datetime"] = None,
        custom: typing.Optional["Custom"] = None,
        inventory_mode: typing.Optional["InventoryMode"] = None,
        tax_rounding_mode: typing.Optional["RoundingMode"] = None,
        tax_calculation_mode: typing.Optional["TaxCalculationMode"] = None,
        origin: typing.Optional["CartOrigin"] = None,
        item_shipping_addresses: typing.Optional[typing.List["Address"]] = None
    ):
        self.order_number = order_number
        self.customer = customer
        self.customer_email = customer_email
        self.line_items = line_items
        self.custom_line_items = custom_line_items
        self.total_price = total_price
        self.taxed_price = taxed_price
        self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.customer_group = customer_group
        self.country = country
        self.order_state = order_state
        self.shipment_state = shipment_state
        self.payment_state = payment_state
        self.shipping_info = shipping_info
        self.completed_at = completed_at
        self.custom = custom
        self.inventory_mode = inventory_mode
        self.tax_rounding_mode = tax_rounding_mode
        self.tax_calculation_mode = tax_calculation_mode
        self.origin = origin
        self.item_shipping_addresses = item_shipping_addresses
        super().__init__(key=key)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OrderImport":
        from ._schemas.orders import OrderImportSchema

        return OrderImportSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.orders import OrderImportSchema

        return OrderImportSchema().dump(self)
