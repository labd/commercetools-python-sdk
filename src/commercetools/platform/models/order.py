# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .cart import (
    CartOrigin,
    InventoryMode,
    RoundingMode,
    ShippingMethodState,
    TaxCalculationMode,
    TaxMode,
)
from .common import BaseResource, Reference, ReferenceTypeId, ResourceIdentifier

if typing.TYPE_CHECKING:
    from .cart import (
        CartOrigin,
        CartReference,
        CustomLineItem,
        CustomLineItemDraft,
        DiscountCodeInfo,
        DiscountedLineItemPortion,
        InventoryMode,
        ItemShippingDetailsDraft,
        LineItem,
        RoundingMode,
        ShippingInfo,
        ShippingMethodState,
        ShippingRateInput,
        TaxCalculationMode,
        TaxedPrice,
        TaxedPriceDraft,
        TaxMode,
    )
    from .cart_discount import CartDiscountReference
    from .channel import ChannelReference, ChannelResourceIdentifier
    from .common import (
        Address,
        CreatedBy,
        Image,
        LastModifiedBy,
        LocalizedString,
        Money,
        PriceDraft,
        ReferenceTypeId,
        TypedMoney,
    )
    from .customer_group import CustomerGroupReference, CustomerGroupResourceIdentifier
    from .payment import PaymentReference, PaymentResourceIdentifier
    from .product import Attribute
    from .shipping_method import ShippingMethodResourceIdentifier, ShippingRateDraft
    from .state import StateReference, StateResourceIdentifier
    from .store import StoreKeyReference, StoreResourceIdentifier
    from .tax_category import TaxCategoryResourceIdentifier, TaxRate
    from .type import (
        CustomFields,
        CustomFieldsDraft,
        FieldContainer,
        TypeResourceIdentifier,
    )


class StagedOrderUpdateAction(_BaseType):
    action: "str"

    def __init__(self, *, action: "str"):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderUpdateAction":
        from ._schemas.order import StagedOrderUpdateActionSchema

        return StagedOrderUpdateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import StagedOrderUpdateActionSchema

        return StagedOrderUpdateActionSchema().dump(self)


class Delivery(_BaseType):
    id: "str"
    created_at: "datetime.datetime"
    #: Items which are shipped in this delivery regardless their distribution over several parcels.
    #: Can also be specified individually for each Parcel.
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
        from ._schemas.order import DeliverySchema

        return DeliverySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import DeliverySchema

        return DeliverySchema().dump(self)


class DeliveryItem(_BaseType):
    id: "str"
    quantity: "float"

    def __init__(self, *, id: "str", quantity: "float"):
        self.id = id
        self.quantity = quantity
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "DeliveryItem":
        from ._schemas.order import DeliveryItemSchema

        return DeliveryItemSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import DeliveryItemSchema

        return DeliveryItemSchema().dump(self)


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
        from ._schemas.order import DiscountedLineItemPriceDraftSchema

        return DiscountedLineItemPriceDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import DiscountedLineItemPriceDraftSchema

        return DiscountedLineItemPriceDraftSchema().dump(self)


class ItemState(_BaseType):
    quantity: "float"
    state: "StateReference"

    def __init__(self, *, quantity: "float", state: "StateReference"):
        self.quantity = quantity
        self.state = state
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ItemState":
        from ._schemas.order import ItemStateSchema

        return ItemStateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import ItemStateSchema

        return ItemStateSchema().dump(self)


class LineItemImportDraft(_BaseType):
    #: ID of the existing product.
    #: You also need to specify the ID of the variant if this property is set or alternatively you can just specify SKU of the product variant.
    product_id: typing.Optional["str"]
    #: The product name.
    name: "LocalizedString"
    variant: "ProductVariantImportDraft"
    price: "PriceDraft"
    quantity: "float"
    state: typing.Optional[typing.List["ItemState"]]
    #: Optional connection to a particular supplier.
    #: By providing supply channel information, you can uniquely identify
    #: inventory entries that should be reserved.
    #: The provided channel should have the
    #: InventorySupply role.
    supply_channel: typing.Optional["ChannelResourceIdentifier"]
    #: The channel is used to select a ProductPrice.
    #: The provided channel should have the ProductDistribution role.
    distribution_channel: typing.Optional["ChannelResourceIdentifier"]
    tax_rate: typing.Optional["TaxRate"]
    #: The custom fields.
    custom: typing.Optional["CustomFieldsDraft"]
    shipping_details: typing.Optional["ItemShippingDetailsDraft"]

    def __init__(
        self,
        *,
        product_id: typing.Optional["str"] = None,
        name: "LocalizedString",
        variant: "ProductVariantImportDraft",
        price: "PriceDraft",
        quantity: "float",
        state: typing.Optional[typing.List["ItemState"]] = None,
        supply_channel: typing.Optional["ChannelResourceIdentifier"] = None,
        distribution_channel: typing.Optional["ChannelResourceIdentifier"] = None,
        tax_rate: typing.Optional["TaxRate"] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        shipping_details: typing.Optional["ItemShippingDetailsDraft"] = None
    ):
        self.product_id = product_id
        self.name = name
        self.variant = variant
        self.price = price
        self.quantity = quantity
        self.state = state
        self.supply_channel = supply_channel
        self.distribution_channel = distribution_channel
        self.tax_rate = tax_rate
        self.custom = custom
        self.shipping_details = shipping_details
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "LineItemImportDraft":
        from ._schemas.order import LineItemImportDraftSchema

        return LineItemImportDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import LineItemImportDraftSchema

        return LineItemImportDraftSchema().dump(self)


class Order(BaseResource):
    #: Present on resources updated after 1/02/2019 except for events not tracked.
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Present on resources created after 1/02/2019 except for events not tracked.
    created_by: typing.Optional["CreatedBy"]
    #: This field will only be present if it was set for Order Import
    completed_at: typing.Optional["datetime.datetime"]
    #: String that uniquely identifies an order.
    #: It can be used to create more human-readable (in contrast to ID) identifier for the order.
    #: It should be unique across a project.
    #: Once it's set it cannot be changed.
    order_number: typing.Optional["str"]
    customer_id: typing.Optional["str"]
    customer_email: typing.Optional["str"]
    #: Identifies carts and orders belonging to an anonymous session (the customer has not signed up/in yet).
    anonymous_id: typing.Optional["str"]
    store: typing.Optional["StoreKeyReference"]
    line_items: typing.List["LineItem"]
    custom_line_items: typing.List["CustomLineItem"]
    total_price: "TypedMoney"
    #: The taxes are calculated based on the shipping address.
    taxed_price: typing.Optional["TaxedPrice"]
    shipping_address: typing.Optional["Address"]
    billing_address: typing.Optional["Address"]
    tax_mode: typing.Optional["TaxMode"]
    #: When calculating taxes for `taxedPrice`, the selected mode is used for rouding.
    tax_rounding_mode: typing.Optional["RoundingMode"]
    #: Set when the customer is set and the customer is a member of a customer group.
    #: Used for product variant price selection.
    customer_group: typing.Optional["CustomerGroupReference"]
    #: A two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    #: Used for product variant price selection.
    country: typing.Optional["str"]
    #: One of the four predefined OrderStates.
    order_state: "OrderState"
    #: This reference can point to a state in a custom workflow.
    state: typing.Optional["StateReference"]
    shipment_state: typing.Optional["ShipmentState"]
    payment_state: typing.Optional["PaymentState"]
    #: Set if the ShippingMethod is set.
    shipping_info: typing.Optional["ShippingInfo"]
    sync_info: typing.List["SyncInfo"]
    return_info: typing.Optional[typing.List["ReturnInfo"]]
    discount_codes: typing.Optional[typing.List["DiscountCodeInfo"]]
    #: The sequence number of the last order message produced by changes to this order.
    #: `0` means, that no messages were created yet.
    last_message_sequence_number: "int"
    #: Set when this order was created from a cart.
    #: The cart will have the state `Ordered`.
    cart: typing.Optional["CartReference"]
    custom: typing.Optional["CustomFields"]
    payment_info: typing.Optional["PaymentInfo"]
    locale: typing.Optional["str"]
    inventory_mode: typing.Optional["InventoryMode"]
    origin: "CartOrigin"
    #: When calculating taxes for `taxedPrice`, the selected mode is used for calculating the price with LineItemLevel (horizontally) or UnitPriceLevel (vertically) calculation mode.
    tax_calculation_mode: typing.Optional["TaxCalculationMode"]
    #: The shippingRateInput is used as an input to select a ShippingRatePriceTier.
    shipping_rate_input: typing.Optional["ShippingRateInput"]
    #: Contains addresses for orders with multiple shipping addresses.
    item_shipping_addresses: typing.Optional[typing.List["Address"]]
    #: Automatically filled when a line item with LineItemMode `GiftLineItem` is removed from this order.
    refused_gifts: typing.List["CartDiscountReference"]

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        completed_at: typing.Optional["datetime.datetime"] = None,
        order_number: typing.Optional["str"] = None,
        customer_id: typing.Optional["str"] = None,
        customer_email: typing.Optional["str"] = None,
        anonymous_id: typing.Optional["str"] = None,
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
        country: typing.Optional["str"] = None,
        order_state: "OrderState",
        state: typing.Optional["StateReference"] = None,
        shipment_state: typing.Optional["ShipmentState"] = None,
        payment_state: typing.Optional["PaymentState"] = None,
        shipping_info: typing.Optional["ShippingInfo"] = None,
        sync_info: typing.List["SyncInfo"],
        return_info: typing.Optional[typing.List["ReturnInfo"]] = None,
        discount_codes: typing.Optional[typing.List["DiscountCodeInfo"]] = None,
        last_message_sequence_number: "int",
        cart: typing.Optional["CartReference"] = None,
        custom: typing.Optional["CustomFields"] = None,
        payment_info: typing.Optional["PaymentInfo"] = None,
        locale: typing.Optional["str"] = None,
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
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Order":
        from ._schemas.order import OrderSchema

        return OrderSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderSchema

        return OrderSchema().dump(self)


class OrderFromCartDraft(_BaseType):
    #: The unique id of the cart from which an order is created.
    id: "str"
    version: "int"
    #: String that uniquely identifies an order.
    #: It can be used to create more human-readable (in contrast to ID) identifier for the order.
    #: It should be unique across a project.
    #: Once it's set it cannot be changed.
    #: For easier use on Get, Update and Delete actions we suggest assigning order numbers that match the regular expression `[a-z0-9_\-]{2,36}`.
    order_number: typing.Optional["str"]
    payment_state: typing.Optional["PaymentState"]
    shipment_state: typing.Optional["ShipmentState"]
    #: Order will be created with `Open` status by default.
    order_state: typing.Optional["OrderState"]
    state: typing.Optional["StateResourceIdentifier"]

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        order_number: typing.Optional["str"] = None,
        payment_state: typing.Optional["PaymentState"] = None,
        shipment_state: typing.Optional["ShipmentState"] = None,
        order_state: typing.Optional["OrderState"] = None,
        state: typing.Optional["StateResourceIdentifier"] = None
    ):
        self.id = id
        self.version = version
        self.order_number = order_number
        self.payment_state = payment_state
        self.shipment_state = shipment_state
        self.order_state = order_state
        self.state = state
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OrderFromCartDraft":
        from ._schemas.order import OrderFromCartDraftSchema

        return OrderFromCartDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderFromCartDraftSchema

        return OrderFromCartDraftSchema().dump(self)


class OrderImportDraft(_BaseType):
    #: String that unique identifies an order.
    #: It can be used to create more human-readable (in contrast to ID) identifier for the order.
    #: It should be unique within a project.
    order_number: typing.Optional["str"]
    #: If given the customer with that ID must exist in the project.
    customer_id: typing.Optional["str"]
    #: The customer email can be used when no check against existing Customers is desired during order import.
    customer_email: typing.Optional["str"]
    #: If not given `customLineItems` must not be empty.
    line_items: typing.Optional[typing.List["LineItemImportDraft"]]
    #: If not given `lineItems` must not be empty.
    custom_line_items: typing.Optional[typing.List["CustomLineItemDraft"]]
    total_price: "Money"
    #: Order Import does not support calculation of taxes.
    #: When setting the draft the taxedPrice is to be provided.
    taxed_price: typing.Optional["TaxedPriceDraft"]
    shipping_address: typing.Optional["Address"]
    billing_address: typing.Optional["Address"]
    #: Set when the customer is set and the customer is a member of a customer group.
    #: Used for product variant price selection.
    customer_group: typing.Optional["CustomerGroupResourceIdentifier"]
    #: A two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    #: Used for product variant price selection.
    country: typing.Optional["str"]
    #: If not given the `Open` state will be assigned by default.
    order_state: typing.Optional["OrderState"]
    shipment_state: typing.Optional["ShipmentState"]
    payment_state: typing.Optional["PaymentState"]
    #: Set if the ShippingMethod is set.
    shipping_info: typing.Optional["ShippingInfoImportDraft"]
    completed_at: typing.Optional["datetime.datetime"]
    #: The custom fields.
    custom: typing.Optional["CustomFieldsDraft"]
    #: If not given the mode `None` will be assigned by default.
    inventory_mode: typing.Optional["InventoryMode"]
    #: If not given the tax rounding mode `HalfEven` will be assigned by default.
    tax_rounding_mode: typing.Optional["RoundingMode"]
    #: Contains addresses for orders with multiple shipping addresses.
    item_shipping_addresses: typing.Optional[typing.List["Address"]]
    store: typing.Optional["StoreResourceIdentifier"]
    #: The default origin is `Customer`.
    origin: typing.Optional["CartOrigin"]

    def __init__(
        self,
        *,
        order_number: typing.Optional["str"] = None,
        customer_id: typing.Optional["str"] = None,
        customer_email: typing.Optional["str"] = None,
        line_items: typing.Optional[typing.List["LineItemImportDraft"]] = None,
        custom_line_items: typing.Optional[typing.List["CustomLineItemDraft"]] = None,
        total_price: "Money",
        taxed_price: typing.Optional["TaxedPriceDraft"] = None,
        shipping_address: typing.Optional["Address"] = None,
        billing_address: typing.Optional["Address"] = None,
        customer_group: typing.Optional["CustomerGroupResourceIdentifier"] = None,
        country: typing.Optional["str"] = None,
        order_state: typing.Optional["OrderState"] = None,
        shipment_state: typing.Optional["ShipmentState"] = None,
        payment_state: typing.Optional["PaymentState"] = None,
        shipping_info: typing.Optional["ShippingInfoImportDraft"] = None,
        completed_at: typing.Optional["datetime.datetime"] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        inventory_mode: typing.Optional["InventoryMode"] = None,
        tax_rounding_mode: typing.Optional["RoundingMode"] = None,
        item_shipping_addresses: typing.Optional[typing.List["Address"]] = None,
        store: typing.Optional["StoreResourceIdentifier"] = None,
        origin: typing.Optional["CartOrigin"] = None
    ):
        self.order_number = order_number
        self.customer_id = customer_id
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
        self.item_shipping_addresses = item_shipping_addresses
        self.store = store
        self.origin = origin
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OrderImportDraft":
        from ._schemas.order import OrderImportDraftSchema

        return OrderImportDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderImportDraftSchema

        return OrderImportDraftSchema().dump(self)


class OrderPagedQueryResponse(_BaseType):
    limit: "int"
    count: "int"
    total: typing.Optional["int"]
    offset: "int"
    results: typing.List["Order"]

    def __init__(
        self,
        *,
        limit: "int",
        count: "int",
        total: typing.Optional["int"] = None,
        offset: "int",
        results: typing.List["Order"]
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
    ) -> "OrderPagedQueryResponse":
        from ._schemas.order import OrderPagedQueryResponseSchema

        return OrderPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderPagedQueryResponseSchema

        return OrderPagedQueryResponseSchema().dump(self)


class OrderReference(Reference):
    obj: typing.Optional["Order"]

    def __init__(self, *, id: "str", obj: typing.Optional["Order"] = None):
        self.obj = obj
        super().__init__(id=id, type_id=ReferenceTypeId.ORDER)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OrderReference":
        from ._schemas.order import OrderReferenceSchema

        return OrderReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderReferenceSchema

        return OrderReferenceSchema().dump(self)


class OrderResourceIdentifier(ResourceIdentifier):
    def __init__(
        self, *, id: typing.Optional["str"] = None, key: typing.Optional["str"] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.ORDER)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderResourceIdentifier":
        from ._schemas.order import OrderResourceIdentifierSchema

        return OrderResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderResourceIdentifierSchema

        return OrderResourceIdentifierSchema().dump(self)


class OrderState(enum.Enum):
    OPEN = "Open"
    CONFIRMED = "Confirmed"
    COMPLETE = "Complete"
    CANCELLED = "Cancelled"


class OrderUpdate(_BaseType):
    version: "int"
    actions: typing.List["OrderUpdateAction"]

    def __init__(self, *, version: "int", actions: typing.List["OrderUpdateAction"]):
        self.version = version
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OrderUpdate":
        from ._schemas.order import OrderUpdateSchema

        return OrderUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderUpdateSchema

        return OrderUpdateSchema().dump(self)


class OrderUpdateAction(_BaseType):
    action: "str"

    def __init__(self, *, action: "str"):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OrderUpdateAction":
        from ._schemas.order import OrderUpdateActionSchema

        return OrderUpdateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderUpdateActionSchema

        return OrderUpdateActionSchema().dump(self)


class Parcel(_BaseType):
    id: "str"
    created_at: "datetime.datetime"
    measurements: typing.Optional["ParcelMeasurements"]
    tracking_data: typing.Optional["TrackingData"]
    #: The delivery items contained in this parcel.
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
        from ._schemas.order import ParcelSchema

        return ParcelSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import ParcelSchema

        return ParcelSchema().dump(self)


class ParcelDraft(_BaseType):
    measurements: typing.Optional["ParcelMeasurements"]
    tracking_data: typing.Optional["TrackingData"]
    #: The delivery items contained in this parcel.
    items: typing.Optional[typing.List["DeliveryItem"]]

    def __init__(
        self,
        *,
        measurements: typing.Optional["ParcelMeasurements"] = None,
        tracking_data: typing.Optional["TrackingData"] = None,
        items: typing.Optional[typing.List["DeliveryItem"]] = None
    ):
        self.measurements = measurements
        self.tracking_data = tracking_data
        self.items = items
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ParcelDraft":
        from ._schemas.order import ParcelDraftSchema

        return ParcelDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import ParcelDraftSchema

        return ParcelDraftSchema().dump(self)


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
        from ._schemas.order import ParcelMeasurementsSchema

        return ParcelMeasurementsSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import ParcelMeasurementsSchema

        return ParcelMeasurementsSchema().dump(self)


class PaymentInfo(_BaseType):
    payments: typing.List["PaymentReference"]

    def __init__(self, *, payments: typing.List["PaymentReference"]):
        self.payments = payments
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "PaymentInfo":
        from ._schemas.order import PaymentInfoSchema

        return PaymentInfoSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import PaymentInfoSchema

        return PaymentInfoSchema().dump(self)


class PaymentState(enum.Enum):
    BALANCE_DUE = "BalanceDue"
    FAILED = "Failed"
    PENDING = "Pending"
    CREDIT_OWED = "CreditOwed"
    PAID = "Paid"


class ProductVariantImportDraft(_BaseType):
    #: The sequential ID of the variant within the product.
    #: The variant with provided ID should exist in some existing product, so you also need to specify the productId if this property is set,
    #: or alternatively you can just specify SKU of the product variant.
    id: typing.Optional["int"]
    #: The SKU of the existing variant.
    sku: typing.Optional["str"]
    #: The prices of the variant.
    #: The prices should not contain two prices for the same price scope (same currency, country and customer group).
    #: If this property is defined, then it will override the `prices` property from the original product variant, otherwise `prices` property from the original product variant would be copied in the resulting order.
    prices: typing.Optional[typing.List["PriceDraft"]]
    #: If this property is defined, then it will override the `attributes` property from the original
    #: product variant, otherwise `attributes` property from the original product variant would be copied in the resulting order.
    attributes: typing.Optional[typing.List["Attribute"]]
    #: If this property is defined, then it will override the `images` property from the original
    #: product variant, otherwise `images` property from the original product variant would be copied in the resulting order.
    images: typing.Optional[typing.List["Image"]]

    def __init__(
        self,
        *,
        id: typing.Optional["int"] = None,
        sku: typing.Optional["str"] = None,
        prices: typing.Optional[typing.List["PriceDraft"]] = None,
        attributes: typing.Optional[typing.List["Attribute"]] = None,
        images: typing.Optional[typing.List["Image"]] = None
    ):
        self.id = id
        self.sku = sku
        self.prices = prices
        self.attributes = attributes
        self.images = images
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductVariantImportDraft":
        from ._schemas.order import ProductVariantImportDraftSchema

        return ProductVariantImportDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import ProductVariantImportDraftSchema

        return ProductVariantImportDraftSchema().dump(self)


class ReturnInfo(_BaseType):
    items: typing.List["ReturnItem"]
    #: Identifies, which return tracking ID is connected to this particular return.
    return_tracking_id: typing.Optional["str"]
    return_date: typing.Optional["datetime.datetime"]

    def __init__(
        self,
        *,
        items: typing.List["ReturnItem"],
        return_tracking_id: typing.Optional["str"] = None,
        return_date: typing.Optional["datetime.datetime"] = None
    ):
        self.items = items
        self.return_tracking_id = return_tracking_id
        self.return_date = return_date
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ReturnInfo":
        from ._schemas.order import ReturnInfoSchema

        return ReturnInfoSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import ReturnInfoSchema

        return ReturnInfoSchema().dump(self)


class ReturnItem(_BaseType):
    id: "str"
    quantity: "int"
    type: "str"
    comment: typing.Optional["str"]
    shipment_state: "ReturnShipmentState"
    payment_state: "ReturnPaymentState"
    last_modified_at: "datetime.datetime"
    created_at: "datetime.datetime"

    def __init__(
        self,
        *,
        id: "str",
        quantity: "int",
        type: "str",
        comment: typing.Optional["str"] = None,
        shipment_state: "ReturnShipmentState",
        payment_state: "ReturnPaymentState",
        last_modified_at: "datetime.datetime",
        created_at: "datetime.datetime"
    ):
        self.id = id
        self.quantity = quantity
        self.type = type
        self.comment = comment
        self.shipment_state = shipment_state
        self.payment_state = payment_state
        self.last_modified_at = last_modified_at
        self.created_at = created_at
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ReturnItem":
        from ._schemas.order import ReturnItemSchema

        return ReturnItemSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import ReturnItemSchema

        return ReturnItemSchema().dump(self)


class CustomLineItemReturnItem(ReturnItem):
    custom_line_item_id: "str"

    def __init__(
        self,
        *,
        id: "str",
        quantity: "int",
        comment: typing.Optional["str"] = None,
        shipment_state: "ReturnShipmentState",
        payment_state: "ReturnPaymentState",
        last_modified_at: "datetime.datetime",
        created_at: "datetime.datetime",
        custom_line_item_id: "str"
    ):
        self.custom_line_item_id = custom_line_item_id
        super().__init__(
            id=id,
            quantity=quantity,
            comment=comment,
            shipment_state=shipment_state,
            payment_state=payment_state,
            last_modified_at=last_modified_at,
            created_at=created_at,
            type="CustomLineItemReturnItem",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomLineItemReturnItem":
        from ._schemas.order import CustomLineItemReturnItemSchema

        return CustomLineItemReturnItemSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import CustomLineItemReturnItemSchema

        return CustomLineItemReturnItemSchema().dump(self)


class LineItemReturnItem(ReturnItem):
    line_item_id: "str"

    def __init__(
        self,
        *,
        id: "str",
        quantity: "int",
        comment: typing.Optional["str"] = None,
        shipment_state: "ReturnShipmentState",
        payment_state: "ReturnPaymentState",
        last_modified_at: "datetime.datetime",
        created_at: "datetime.datetime",
        line_item_id: "str"
    ):
        self.line_item_id = line_item_id
        super().__init__(
            id=id,
            quantity=quantity,
            comment=comment,
            shipment_state=shipment_state,
            payment_state=payment_state,
            last_modified_at=last_modified_at,
            created_at=created_at,
            type="LineItemReturnItem",
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "LineItemReturnItem":
        from ._schemas.order import LineItemReturnItemSchema

        return LineItemReturnItemSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import LineItemReturnItemSchema

        return LineItemReturnItemSchema().dump(self)


class ReturnItemDraft(_BaseType):
    quantity: "int"
    line_item_id: typing.Optional["str"]
    custom_line_item_id: typing.Optional["str"]
    comment: typing.Optional["str"]
    shipment_state: "ReturnShipmentState"

    def __init__(
        self,
        *,
        quantity: "int",
        line_item_id: typing.Optional["str"] = None,
        custom_line_item_id: typing.Optional["str"] = None,
        comment: typing.Optional["str"] = None,
        shipment_state: "ReturnShipmentState"
    ):
        self.quantity = quantity
        self.line_item_id = line_item_id
        self.custom_line_item_id = custom_line_item_id
        self.comment = comment
        self.shipment_state = shipment_state
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ReturnItemDraft":
        from ._schemas.order import ReturnItemDraftSchema

        return ReturnItemDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import ReturnItemDraftSchema

        return ReturnItemDraftSchema().dump(self)


class ReturnPaymentState(enum.Enum):
    NON_REFUNDABLE = "NonRefundable"
    INITIAL = "Initial"
    REFUNDED = "Refunded"
    NOT_REFUNDED = "NotRefunded"


class ReturnShipmentState(enum.Enum):
    ADVISED = "Advised"
    RETURNED = "Returned"
    BACK_IN_STOCK = "BackInStock"
    UNUSABLE = "Unusable"


class ShipmentState(enum.Enum):
    SHIPPED = "Shipped"
    READY = "Ready"
    PENDING = "Pending"
    DELAYED = "Delayed"
    PARTIAL = "Partial"
    BACKORDER = "Backorder"


class ShippingInfoImportDraft(_BaseType):
    shipping_method_name: "str"
    price: "Money"
    #: The shipping rate used to determine the price.
    shipping_rate: "ShippingRateDraft"
    tax_rate: typing.Optional["TaxRate"]
    tax_category: typing.Optional["TaxCategoryResourceIdentifier"]
    #: Not set if custom shipping method is used.
    shipping_method: typing.Optional["ShippingMethodResourceIdentifier"]
    #: Deliveries are compilations of information on how the articles are being delivered to the customers.
    deliveries: typing.Optional[typing.List["Delivery"]]
    discounted_price: typing.Optional["DiscountedLineItemPriceDraft"]
    #: Indicates whether the ShippingMethod referenced is allowed for the cart or not.
    shipping_method_state: typing.Optional["ShippingMethodState"]

    def __init__(
        self,
        *,
        shipping_method_name: "str",
        price: "Money",
        shipping_rate: "ShippingRateDraft",
        tax_rate: typing.Optional["TaxRate"] = None,
        tax_category: typing.Optional["TaxCategoryResourceIdentifier"] = None,
        shipping_method: typing.Optional["ShippingMethodResourceIdentifier"] = None,
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
        from ._schemas.order import ShippingInfoImportDraftSchema

        return ShippingInfoImportDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import ShippingInfoImportDraftSchema

        return ShippingInfoImportDraftSchema().dump(self)


class SyncInfo(_BaseType):
    #: Connection to a particular synchronization destination.
    channel: "ChannelReference"
    #: Can be used to reference an external order instance, file etc.
    external_id: typing.Optional["str"]
    synced_at: "datetime.datetime"

    def __init__(
        self,
        *,
        channel: "ChannelReference",
        external_id: typing.Optional["str"] = None,
        synced_at: "datetime.datetime"
    ):
        self.channel = channel
        self.external_id = external_id
        self.synced_at = synced_at
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SyncInfo":
        from ._schemas.order import SyncInfoSchema

        return SyncInfoSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import SyncInfoSchema

        return SyncInfoSchema().dump(self)


class TaxedItemPriceDraft(_BaseType):
    total_net: "Money"
    total_gross: "Money"

    def __init__(self, *, total_net: "Money", total_gross: "Money"):
        self.total_net = total_net
        self.total_gross = total_gross
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TaxedItemPriceDraft":
        from ._schemas.order import TaxedItemPriceDraftSchema

        return TaxedItemPriceDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import TaxedItemPriceDraftSchema

        return TaxedItemPriceDraftSchema().dump(self)


class TrackingData(_BaseType):
    #: The ID to track one parcel.
    tracking_id: typing.Optional["str"]
    #: The carrier that delivers the parcel.
    carrier: typing.Optional["str"]
    provider: typing.Optional["str"]
    provider_transaction: typing.Optional["str"]
    #: Flag to distinguish if the parcel is on the way to the customer (false) or on the way back (true).
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
        from ._schemas.order import TrackingDataSchema

        return TrackingDataSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import TrackingDataSchema

        return TrackingDataSchema().dump(self)


class OrderAddDeliveryAction(OrderUpdateAction):
    items: typing.Optional[typing.List["DeliveryItem"]]
    address: typing.Optional["Address"]
    parcels: typing.Optional[typing.List["ParcelDraft"]]

    def __init__(
        self,
        *,
        items: typing.Optional[typing.List["DeliveryItem"]] = None,
        address: typing.Optional["Address"] = None,
        parcels: typing.Optional[typing.List["ParcelDraft"]] = None
    ):
        self.items = items
        self.address = address
        self.parcels = parcels
        super().__init__(action="addDelivery")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderAddDeliveryAction":
        from ._schemas.order import OrderAddDeliveryActionSchema

        return OrderAddDeliveryActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderAddDeliveryActionSchema

        return OrderAddDeliveryActionSchema().dump(self)


class OrderAddItemShippingAddressAction(OrderUpdateAction):
    address: "Address"

    def __init__(self, *, address: "Address"):
        self.address = address
        super().__init__(action="addItemShippingAddress")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderAddItemShippingAddressAction":
        from ._schemas.order import OrderAddItemShippingAddressActionSchema

        return OrderAddItemShippingAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderAddItemShippingAddressActionSchema

        return OrderAddItemShippingAddressActionSchema().dump(self)


class OrderAddParcelToDeliveryAction(OrderUpdateAction):
    delivery_id: "str"
    measurements: typing.Optional["ParcelMeasurements"]
    tracking_data: typing.Optional["TrackingData"]
    items: typing.Optional[typing.List["DeliveryItem"]]

    def __init__(
        self,
        *,
        delivery_id: "str",
        measurements: typing.Optional["ParcelMeasurements"] = None,
        tracking_data: typing.Optional["TrackingData"] = None,
        items: typing.Optional[typing.List["DeliveryItem"]] = None
    ):
        self.delivery_id = delivery_id
        self.measurements = measurements
        self.tracking_data = tracking_data
        self.items = items
        super().__init__(action="addParcelToDelivery")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderAddParcelToDeliveryAction":
        from ._schemas.order import OrderAddParcelToDeliveryActionSchema

        return OrderAddParcelToDeliveryActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderAddParcelToDeliveryActionSchema

        return OrderAddParcelToDeliveryActionSchema().dump(self)


class OrderAddPaymentAction(OrderUpdateAction):
    payment: "PaymentResourceIdentifier"

    def __init__(self, *, payment: "PaymentResourceIdentifier"):
        self.payment = payment
        super().__init__(action="addPayment")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OrderAddPaymentAction":
        from ._schemas.order import OrderAddPaymentActionSchema

        return OrderAddPaymentActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderAddPaymentActionSchema

        return OrderAddPaymentActionSchema().dump(self)


class OrderAddReturnInfoAction(OrderUpdateAction):
    return_tracking_id: typing.Optional["str"]
    items: typing.List["ReturnItemDraft"]
    return_date: typing.Optional["datetime.datetime"]

    def __init__(
        self,
        *,
        return_tracking_id: typing.Optional["str"] = None,
        items: typing.List["ReturnItemDraft"],
        return_date: typing.Optional["datetime.datetime"] = None
    ):
        self.return_tracking_id = return_tracking_id
        self.items = items
        self.return_date = return_date
        super().__init__(action="addReturnInfo")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderAddReturnInfoAction":
        from ._schemas.order import OrderAddReturnInfoActionSchema

        return OrderAddReturnInfoActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderAddReturnInfoActionSchema

        return OrderAddReturnInfoActionSchema().dump(self)


class OrderChangeOrderStateAction(OrderUpdateAction):
    order_state: "OrderState"

    def __init__(self, *, order_state: "OrderState"):
        self.order_state = order_state
        super().__init__(action="changeOrderState")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderChangeOrderStateAction":
        from ._schemas.order import OrderChangeOrderStateActionSchema

        return OrderChangeOrderStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderChangeOrderStateActionSchema

        return OrderChangeOrderStateActionSchema().dump(self)


class OrderChangePaymentStateAction(OrderUpdateAction):
    payment_state: typing.Optional["PaymentState"]

    def __init__(self, *, payment_state: typing.Optional["PaymentState"] = None):
        self.payment_state = payment_state
        super().__init__(action="changePaymentState")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderChangePaymentStateAction":
        from ._schemas.order import OrderChangePaymentStateActionSchema

        return OrderChangePaymentStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderChangePaymentStateActionSchema

        return OrderChangePaymentStateActionSchema().dump(self)


class OrderChangeShipmentStateAction(OrderUpdateAction):
    shipment_state: typing.Optional["ShipmentState"]

    def __init__(self, *, shipment_state: typing.Optional["ShipmentState"] = None):
        self.shipment_state = shipment_state
        super().__init__(action="changeShipmentState")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderChangeShipmentStateAction":
        from ._schemas.order import OrderChangeShipmentStateActionSchema

        return OrderChangeShipmentStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderChangeShipmentStateActionSchema

        return OrderChangeShipmentStateActionSchema().dump(self)


class OrderImportCustomLineItemStateAction(OrderUpdateAction):
    custom_line_item_id: "str"
    state: typing.List["ItemState"]

    def __init__(self, *, custom_line_item_id: "str", state: typing.List["ItemState"]):
        self.custom_line_item_id = custom_line_item_id
        self.state = state
        super().__init__(action="importCustomLineItemState")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderImportCustomLineItemStateAction":
        from ._schemas.order import OrderImportCustomLineItemStateActionSchema

        return OrderImportCustomLineItemStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderImportCustomLineItemStateActionSchema

        return OrderImportCustomLineItemStateActionSchema().dump(self)


class OrderImportLineItemStateAction(OrderUpdateAction):
    line_item_id: "str"
    state: typing.List["ItemState"]

    def __init__(self, *, line_item_id: "str", state: typing.List["ItemState"]):
        self.line_item_id = line_item_id
        self.state = state
        super().__init__(action="importLineItemState")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderImportLineItemStateAction":
        from ._schemas.order import OrderImportLineItemStateActionSchema

        return OrderImportLineItemStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderImportLineItemStateActionSchema

        return OrderImportLineItemStateActionSchema().dump(self)


class OrderRemoveDeliveryAction(OrderUpdateAction):
    delivery_id: "str"

    def __init__(self, *, delivery_id: "str"):
        self.delivery_id = delivery_id
        super().__init__(action="removeDelivery")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderRemoveDeliveryAction":
        from ._schemas.order import OrderRemoveDeliveryActionSchema

        return OrderRemoveDeliveryActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderRemoveDeliveryActionSchema

        return OrderRemoveDeliveryActionSchema().dump(self)


class OrderRemoveItemShippingAddressAction(OrderUpdateAction):
    address_key: "str"

    def __init__(self, *, address_key: "str"):
        self.address_key = address_key
        super().__init__(action="removeItemShippingAddress")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderRemoveItemShippingAddressAction":
        from ._schemas.order import OrderRemoveItemShippingAddressActionSchema

        return OrderRemoveItemShippingAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderRemoveItemShippingAddressActionSchema

        return OrderRemoveItemShippingAddressActionSchema().dump(self)


class OrderRemoveParcelFromDeliveryAction(OrderUpdateAction):
    parcel_id: "str"

    def __init__(self, *, parcel_id: "str"):
        self.parcel_id = parcel_id
        super().__init__(action="removeParcelFromDelivery")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderRemoveParcelFromDeliveryAction":
        from ._schemas.order import OrderRemoveParcelFromDeliveryActionSchema

        return OrderRemoveParcelFromDeliveryActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderRemoveParcelFromDeliveryActionSchema

        return OrderRemoveParcelFromDeliveryActionSchema().dump(self)


class OrderRemovePaymentAction(OrderUpdateAction):
    payment: "PaymentResourceIdentifier"

    def __init__(self, *, payment: "PaymentResourceIdentifier"):
        self.payment = payment
        super().__init__(action="removePayment")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderRemovePaymentAction":
        from ._schemas.order import OrderRemovePaymentActionSchema

        return OrderRemovePaymentActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderRemovePaymentActionSchema

        return OrderRemovePaymentActionSchema().dump(self)


class OrderSetBillingAddressAction(OrderUpdateAction):
    address: typing.Optional["Address"]

    def __init__(self, *, address: typing.Optional["Address"] = None):
        self.address = address
        super().__init__(action="setBillingAddress")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderSetBillingAddressAction":
        from ._schemas.order import OrderSetBillingAddressActionSchema

        return OrderSetBillingAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderSetBillingAddressActionSchema

        return OrderSetBillingAddressActionSchema().dump(self)


class OrderSetCustomFieldAction(OrderUpdateAction):
    name: "str"
    value: typing.Optional["any"]

    def __init__(self, *, name: "str", value: typing.Optional["any"] = None):
        self.name = name
        self.value = value
        super().__init__(action="setCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderSetCustomFieldAction":
        from ._schemas.order import OrderSetCustomFieldActionSchema

        return OrderSetCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderSetCustomFieldActionSchema

        return OrderSetCustomFieldActionSchema().dump(self)


class OrderSetCustomLineItemCustomFieldAction(OrderUpdateAction):
    custom_line_item_id: "str"
    name: "str"
    value: typing.Optional["any"]

    def __init__(
        self,
        *,
        custom_line_item_id: "str",
        name: "str",
        value: typing.Optional["any"] = None
    ):
        self.custom_line_item_id = custom_line_item_id
        self.name = name
        self.value = value
        super().__init__(action="setCustomLineItemCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderSetCustomLineItemCustomFieldAction":
        from ._schemas.order import OrderSetCustomLineItemCustomFieldActionSchema

        return OrderSetCustomLineItemCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderSetCustomLineItemCustomFieldActionSchema

        return OrderSetCustomLineItemCustomFieldActionSchema().dump(self)


class OrderSetCustomLineItemCustomTypeAction(OrderUpdateAction):
    custom_line_item_id: "str"
    type: typing.Optional["TypeResourceIdentifier"]
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        custom_line_item_id: "str",
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
    ) -> "OrderSetCustomLineItemCustomTypeAction":
        from ._schemas.order import OrderSetCustomLineItemCustomTypeActionSchema

        return OrderSetCustomLineItemCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderSetCustomLineItemCustomTypeActionSchema

        return OrderSetCustomLineItemCustomTypeActionSchema().dump(self)


class OrderSetCustomLineItemShippingDetailsAction(OrderUpdateAction):
    custom_line_item_id: "str"
    shipping_details: typing.Optional["ItemShippingDetailsDraft"]

    def __init__(
        self,
        *,
        custom_line_item_id: "str",
        shipping_details: typing.Optional["ItemShippingDetailsDraft"] = None
    ):
        self.custom_line_item_id = custom_line_item_id
        self.shipping_details = shipping_details
        super().__init__(action="setCustomLineItemShippingDetails")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderSetCustomLineItemShippingDetailsAction":
        from ._schemas.order import OrderSetCustomLineItemShippingDetailsActionSchema

        return OrderSetCustomLineItemShippingDetailsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderSetCustomLineItemShippingDetailsActionSchema

        return OrderSetCustomLineItemShippingDetailsActionSchema().dump(self)


class OrderSetCustomTypeAction(OrderUpdateAction):
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
    ) -> "OrderSetCustomTypeAction":
        from ._schemas.order import OrderSetCustomTypeActionSchema

        return OrderSetCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderSetCustomTypeActionSchema

        return OrderSetCustomTypeActionSchema().dump(self)


class OrderSetCustomerEmailAction(OrderUpdateAction):
    email: typing.Optional["str"]

    def __init__(self, *, email: typing.Optional["str"] = None):
        self.email = email
        super().__init__(action="setCustomerEmail")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderSetCustomerEmailAction":
        from ._schemas.order import OrderSetCustomerEmailActionSchema

        return OrderSetCustomerEmailActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderSetCustomerEmailActionSchema

        return OrderSetCustomerEmailActionSchema().dump(self)


class OrderSetCustomerIdAction(OrderUpdateAction):
    customer_id: typing.Optional["str"]

    def __init__(self, *, customer_id: typing.Optional["str"] = None):
        self.customer_id = customer_id
        super().__init__(action="setCustomerId")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderSetCustomerIdAction":
        from ._schemas.order import OrderSetCustomerIdActionSchema

        return OrderSetCustomerIdActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderSetCustomerIdActionSchema

        return OrderSetCustomerIdActionSchema().dump(self)


class OrderSetDeliveryAddressAction(OrderUpdateAction):
    delivery_id: "str"
    address: typing.Optional["Address"]

    def __init__(
        self, *, delivery_id: "str", address: typing.Optional["Address"] = None
    ):
        self.delivery_id = delivery_id
        self.address = address
        super().__init__(action="setDeliveryAddress")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderSetDeliveryAddressAction":
        from ._schemas.order import OrderSetDeliveryAddressActionSchema

        return OrderSetDeliveryAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderSetDeliveryAddressActionSchema

        return OrderSetDeliveryAddressActionSchema().dump(self)


class OrderSetDeliveryItemsAction(OrderUpdateAction):
    delivery_id: "str"
    items: typing.List["DeliveryItem"]

    def __init__(self, *, delivery_id: "str", items: typing.List["DeliveryItem"]):
        self.delivery_id = delivery_id
        self.items = items
        super().__init__(action="setDeliveryItems")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderSetDeliveryItemsAction":
        from ._schemas.order import OrderSetDeliveryItemsActionSchema

        return OrderSetDeliveryItemsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderSetDeliveryItemsActionSchema

        return OrderSetDeliveryItemsActionSchema().dump(self)


class OrderSetLineItemCustomFieldAction(OrderUpdateAction):
    line_item_id: "str"
    name: "str"
    value: typing.Optional["any"]

    def __init__(
        self, *, line_item_id: "str", name: "str", value: typing.Optional["any"] = None
    ):
        self.line_item_id = line_item_id
        self.name = name
        self.value = value
        super().__init__(action="setLineItemCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderSetLineItemCustomFieldAction":
        from ._schemas.order import OrderSetLineItemCustomFieldActionSchema

        return OrderSetLineItemCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderSetLineItemCustomFieldActionSchema

        return OrderSetLineItemCustomFieldActionSchema().dump(self)


class OrderSetLineItemCustomTypeAction(OrderUpdateAction):
    line_item_id: "str"
    type: typing.Optional["TypeResourceIdentifier"]
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        line_item_id: "str",
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
    ) -> "OrderSetLineItemCustomTypeAction":
        from ._schemas.order import OrderSetLineItemCustomTypeActionSchema

        return OrderSetLineItemCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderSetLineItemCustomTypeActionSchema

        return OrderSetLineItemCustomTypeActionSchema().dump(self)


class OrderSetLineItemShippingDetailsAction(OrderUpdateAction):
    line_item_id: "str"
    shipping_details: typing.Optional["ItemShippingDetailsDraft"]

    def __init__(
        self,
        *,
        line_item_id: "str",
        shipping_details: typing.Optional["ItemShippingDetailsDraft"] = None
    ):
        self.line_item_id = line_item_id
        self.shipping_details = shipping_details
        super().__init__(action="setLineItemShippingDetails")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderSetLineItemShippingDetailsAction":
        from ._schemas.order import OrderSetLineItemShippingDetailsActionSchema

        return OrderSetLineItemShippingDetailsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderSetLineItemShippingDetailsActionSchema

        return OrderSetLineItemShippingDetailsActionSchema().dump(self)


class OrderSetLocaleAction(OrderUpdateAction):
    locale: typing.Optional["str"]

    def __init__(self, *, locale: typing.Optional["str"] = None):
        self.locale = locale
        super().__init__(action="setLocale")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OrderSetLocaleAction":
        from ._schemas.order import OrderSetLocaleActionSchema

        return OrderSetLocaleActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderSetLocaleActionSchema

        return OrderSetLocaleActionSchema().dump(self)


class OrderSetOrderNumberAction(OrderUpdateAction):
    order_number: typing.Optional["str"]

    def __init__(self, *, order_number: typing.Optional["str"] = None):
        self.order_number = order_number
        super().__init__(action="setOrderNumber")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderSetOrderNumberAction":
        from ._schemas.order import OrderSetOrderNumberActionSchema

        return OrderSetOrderNumberActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderSetOrderNumberActionSchema

        return OrderSetOrderNumberActionSchema().dump(self)


class OrderSetParcelItemsAction(OrderUpdateAction):
    parcel_id: "str"
    items: typing.List["DeliveryItem"]

    def __init__(self, *, parcel_id: "str", items: typing.List["DeliveryItem"]):
        self.parcel_id = parcel_id
        self.items = items
        super().__init__(action="setParcelItems")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderSetParcelItemsAction":
        from ._schemas.order import OrderSetParcelItemsActionSchema

        return OrderSetParcelItemsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderSetParcelItemsActionSchema

        return OrderSetParcelItemsActionSchema().dump(self)


class OrderSetParcelMeasurementsAction(OrderUpdateAction):
    parcel_id: "str"
    measurements: typing.Optional["ParcelMeasurements"]

    def __init__(
        self,
        *,
        parcel_id: "str",
        measurements: typing.Optional["ParcelMeasurements"] = None
    ):
        self.parcel_id = parcel_id
        self.measurements = measurements
        super().__init__(action="setParcelMeasurements")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderSetParcelMeasurementsAction":
        from ._schemas.order import OrderSetParcelMeasurementsActionSchema

        return OrderSetParcelMeasurementsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderSetParcelMeasurementsActionSchema

        return OrderSetParcelMeasurementsActionSchema().dump(self)


class OrderSetParcelTrackingDataAction(OrderUpdateAction):
    parcel_id: "str"
    tracking_data: typing.Optional["TrackingData"]

    def __init__(
        self, *, parcel_id: "str", tracking_data: typing.Optional["TrackingData"] = None
    ):
        self.parcel_id = parcel_id
        self.tracking_data = tracking_data
        super().__init__(action="setParcelTrackingData")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderSetParcelTrackingDataAction":
        from ._schemas.order import OrderSetParcelTrackingDataActionSchema

        return OrderSetParcelTrackingDataActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderSetParcelTrackingDataActionSchema

        return OrderSetParcelTrackingDataActionSchema().dump(self)


class OrderSetReturnPaymentStateAction(OrderUpdateAction):
    return_item_id: "str"
    payment_state: "ReturnPaymentState"

    def __init__(self, *, return_item_id: "str", payment_state: "ReturnPaymentState"):
        self.return_item_id = return_item_id
        self.payment_state = payment_state
        super().__init__(action="setReturnPaymentState")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderSetReturnPaymentStateAction":
        from ._schemas.order import OrderSetReturnPaymentStateActionSchema

        return OrderSetReturnPaymentStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderSetReturnPaymentStateActionSchema

        return OrderSetReturnPaymentStateActionSchema().dump(self)


class OrderSetReturnShipmentStateAction(OrderUpdateAction):
    return_item_id: "str"
    shipment_state: "ReturnShipmentState"

    def __init__(self, *, return_item_id: "str", shipment_state: "ReturnShipmentState"):
        self.return_item_id = return_item_id
        self.shipment_state = shipment_state
        super().__init__(action="setReturnShipmentState")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderSetReturnShipmentStateAction":
        from ._schemas.order import OrderSetReturnShipmentStateActionSchema

        return OrderSetReturnShipmentStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderSetReturnShipmentStateActionSchema

        return OrderSetReturnShipmentStateActionSchema().dump(self)


class OrderSetShippingAddressAction(OrderUpdateAction):
    address: typing.Optional["Address"]

    def __init__(self, *, address: typing.Optional["Address"] = None):
        self.address = address
        super().__init__(action="setShippingAddress")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderSetShippingAddressAction":
        from ._schemas.order import OrderSetShippingAddressActionSchema

        return OrderSetShippingAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderSetShippingAddressActionSchema

        return OrderSetShippingAddressActionSchema().dump(self)


class OrderSetStoreAction(OrderUpdateAction):
    store: typing.Optional["StoreResourceIdentifier"]

    def __init__(self, *, store: typing.Optional["StoreResourceIdentifier"] = None):
        self.store = store
        super().__init__(action="setStore")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OrderSetStoreAction":
        from ._schemas.order import OrderSetStoreActionSchema

        return OrderSetStoreActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderSetStoreActionSchema

        return OrderSetStoreActionSchema().dump(self)


class OrderTransitionCustomLineItemStateAction(OrderUpdateAction):
    custom_line_item_id: "str"
    quantity: "int"
    from_state: "StateResourceIdentifier"
    to_state: "StateResourceIdentifier"
    actual_transition_date: typing.Optional["datetime.datetime"]

    def __init__(
        self,
        *,
        custom_line_item_id: "str",
        quantity: "int",
        from_state: "StateResourceIdentifier",
        to_state: "StateResourceIdentifier",
        actual_transition_date: typing.Optional["datetime.datetime"] = None
    ):
        self.custom_line_item_id = custom_line_item_id
        self.quantity = quantity
        self.from_state = from_state
        self.to_state = to_state
        self.actual_transition_date = actual_transition_date
        super().__init__(action="transitionCustomLineItemState")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderTransitionCustomLineItemStateAction":
        from ._schemas.order import OrderTransitionCustomLineItemStateActionSchema

        return OrderTransitionCustomLineItemStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderTransitionCustomLineItemStateActionSchema

        return OrderTransitionCustomLineItemStateActionSchema().dump(self)


class OrderTransitionLineItemStateAction(OrderUpdateAction):
    line_item_id: "str"
    quantity: "int"
    from_state: "StateResourceIdentifier"
    to_state: "StateResourceIdentifier"
    actual_transition_date: typing.Optional["datetime.datetime"]

    def __init__(
        self,
        *,
        line_item_id: "str",
        quantity: "int",
        from_state: "StateResourceIdentifier",
        to_state: "StateResourceIdentifier",
        actual_transition_date: typing.Optional["datetime.datetime"] = None
    ):
        self.line_item_id = line_item_id
        self.quantity = quantity
        self.from_state = from_state
        self.to_state = to_state
        self.actual_transition_date = actual_transition_date
        super().__init__(action="transitionLineItemState")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderTransitionLineItemStateAction":
        from ._schemas.order import OrderTransitionLineItemStateActionSchema

        return OrderTransitionLineItemStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderTransitionLineItemStateActionSchema

        return OrderTransitionLineItemStateActionSchema().dump(self)


class OrderTransitionStateAction(OrderUpdateAction):
    state: "StateResourceIdentifier"
    force: typing.Optional["bool"]

    def __init__(
        self, *, state: "StateResourceIdentifier", force: typing.Optional["bool"] = None
    ):
        self.state = state
        self.force = force
        super().__init__(action="transitionState")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderTransitionStateAction":
        from ._schemas.order import OrderTransitionStateActionSchema

        return OrderTransitionStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderTransitionStateActionSchema

        return OrderTransitionStateActionSchema().dump(self)


class OrderUpdateItemShippingAddressAction(OrderUpdateAction):
    address: "Address"

    def __init__(self, *, address: "Address"):
        self.address = address
        super().__init__(action="updateItemShippingAddress")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderUpdateItemShippingAddressAction":
        from ._schemas.order import OrderUpdateItemShippingAddressActionSchema

        return OrderUpdateItemShippingAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderUpdateItemShippingAddressActionSchema

        return OrderUpdateItemShippingAddressActionSchema().dump(self)


class OrderUpdateSyncInfoAction(OrderUpdateAction):
    channel: "ChannelResourceIdentifier"
    external_id: typing.Optional["str"]
    synced_at: typing.Optional["datetime.datetime"]

    def __init__(
        self,
        *,
        channel: "ChannelResourceIdentifier",
        external_id: typing.Optional["str"] = None,
        synced_at: typing.Optional["datetime.datetime"] = None
    ):
        self.channel = channel
        self.external_id = external_id
        self.synced_at = synced_at
        super().__init__(action="updateSyncInfo")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderUpdateSyncInfoAction":
        from ._schemas.order import OrderUpdateSyncInfoActionSchema

        return OrderUpdateSyncInfoActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order import OrderUpdateSyncInfoActionSchema

        return OrderUpdateSyncInfoActionSchema().dump(self)
