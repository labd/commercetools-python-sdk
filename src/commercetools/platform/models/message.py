# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .cart import DiscountCodeState, ProductPublishScope
from .common import BaseResource
from .order import OrderState, PaymentState, ReturnShipmentState, ShipmentState
from .payment import TransactionState

if typing.TYPE_CHECKING:
    from .cart import (
        DiscountCodeState,
        DiscountedLineItemPriceForQuantity,
        LineItem,
        ProductPublishScope,
        ShippingInfo,
        ShippingRateInput,
        TaxedItemPrice,
    )
    from .category import Category, CategoryReference
    from .channel import ChannelReference
    from .common import (
        Address,
        CreatedBy,
        DiscountedPrice,
        Image,
        LastModifiedBy,
        LocalizedString,
        Money,
        Reference,
    )
    from .customer import Customer, CustomerReference
    from .customer_group import CustomerGroupReference
    from .discount_code import DiscountCodeReference
    from .inventory import InventoryEntry
    from .order import (
        Delivery,
        DeliveryItem,
        Order,
        OrderState,
        Parcel,
        ParcelMeasurements,
        PaymentState,
        ReturnInfo,
        ReturnShipmentState,
        ShipmentState,
        TrackingData,
    )
    from .order_edit import OrderEditApplied, OrderEditReference
    from .payment import Payment, Transaction, TransactionState
    from .product import ProductProjection, ProductVariant
    from .review import Review
    from .state import StateReference
    from .store import StoreKeyReference
    from .type import CustomFields


class Message(BaseResource):
    last_modified_by: typing.Optional["LastModifiedBy"]
    created_by: typing.Optional["CreatedBy"]
    sequence_number: "int"
    resource: "Reference"
    resource_version: "int"
    type: "str"
    resource_user_provided_identifiers: typing.Optional["UserProvidedIdentifiers"]

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        type: "str",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.sequence_number = sequence_number
        self.resource = resource
        self.resource_version = resource_version
        self.type = type
        self.resource_user_provided_identifiers = resource_user_provided_identifiers
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Message":
        from ._schemas.message import MessageSchema

        return MessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import MessageSchema

        return MessageSchema().dump(self)


class CategoryCreatedMessage(Message):
    category: "Category"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        category: "Category"
    ):
        self.category = category
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="CategoryCreated",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CategoryCreatedMessage":
        from ._schemas.message import CategoryCreatedMessageSchema

        return CategoryCreatedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import CategoryCreatedMessageSchema

        return CategoryCreatedMessageSchema().dump(self)


class CategorySlugChangedMessage(Message):
    slug: "LocalizedString"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        slug: "LocalizedString"
    ):
        self.slug = slug
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="CategorySlugChanged",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CategorySlugChangedMessage":
        from ._schemas.message import CategorySlugChangedMessageSchema

        return CategorySlugChangedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import CategorySlugChangedMessageSchema

        return CategorySlugChangedMessageSchema().dump(self)


class CustomLineItemStateTransitionMessage(Message):
    custom_line_item_id: "str"
    transition_date: "datetime.datetime"
    quantity: "int"
    from_state: "StateReference"
    to_state: "StateReference"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        custom_line_item_id: "str",
        transition_date: "datetime.datetime",
        quantity: "int",
        from_state: "StateReference",
        to_state: "StateReference"
    ):
        self.custom_line_item_id = custom_line_item_id
        self.transition_date = transition_date
        self.quantity = quantity
        self.from_state = from_state
        self.to_state = to_state
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="CustomLineItemStateTransition",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomLineItemStateTransitionMessage":
        from ._schemas.message import CustomLineItemStateTransitionMessageSchema

        return CustomLineItemStateTransitionMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import CustomLineItemStateTransitionMessageSchema

        return CustomLineItemStateTransitionMessageSchema().dump(self)


class CustomerAddressAddedMessage(Message):
    address: "Address"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        address: "Address"
    ):
        self.address = address
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="CustomerAddressAdded",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerAddressAddedMessage":
        from ._schemas.message import CustomerAddressAddedMessageSchema

        return CustomerAddressAddedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import CustomerAddressAddedMessageSchema

        return CustomerAddressAddedMessageSchema().dump(self)


class CustomerAddressChangedMessage(Message):
    address: "Address"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        address: "Address"
    ):
        self.address = address
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="CustomerAddressChanged",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerAddressChangedMessage":
        from ._schemas.message import CustomerAddressChangedMessageSchema

        return CustomerAddressChangedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import CustomerAddressChangedMessageSchema

        return CustomerAddressChangedMessageSchema().dump(self)


class CustomerAddressRemovedMessage(Message):
    address: "Address"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        address: "Address"
    ):
        self.address = address
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="CustomerAddressRemoved",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerAddressRemovedMessage":
        from ._schemas.message import CustomerAddressRemovedMessageSchema

        return CustomerAddressRemovedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import CustomerAddressRemovedMessageSchema

        return CustomerAddressRemovedMessageSchema().dump(self)


class CustomerCompanyNameSetMessage(Message):
    company_name: "str"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        company_name: "str"
    ):
        self.company_name = company_name
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="CustomerCompanyNameSet",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerCompanyNameSetMessage":
        from ._schemas.message import CustomerCompanyNameSetMessageSchema

        return CustomerCompanyNameSetMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import CustomerCompanyNameSetMessageSchema

        return CustomerCompanyNameSetMessageSchema().dump(self)


class CustomerCreatedMessage(Message):
    customer: "Customer"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        customer: "Customer"
    ):
        self.customer = customer
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="CustomerCreated",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerCreatedMessage":
        from ._schemas.message import CustomerCreatedMessageSchema

        return CustomerCreatedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import CustomerCreatedMessageSchema

        return CustomerCreatedMessageSchema().dump(self)


class CustomerDateOfBirthSetMessage(Message):
    date_of_birth: "datetime.date"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        date_of_birth: "datetime.date"
    ):
        self.date_of_birth = date_of_birth
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="CustomerDateOfBirthSet",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerDateOfBirthSetMessage":
        from ._schemas.message import CustomerDateOfBirthSetMessageSchema

        return CustomerDateOfBirthSetMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import CustomerDateOfBirthSetMessageSchema

        return CustomerDateOfBirthSetMessageSchema().dump(self)


class CustomerEmailChangedMessage(Message):
    email: "str"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        email: "str"
    ):
        self.email = email
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="CustomerEmailChanged",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerEmailChangedMessage":
        from ._schemas.message import CustomerEmailChangedMessageSchema

        return CustomerEmailChangedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import CustomerEmailChangedMessageSchema

        return CustomerEmailChangedMessageSchema().dump(self)


class CustomerEmailVerifiedMessage(Message):
    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None
    ):

        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="CustomerEmailVerified",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerEmailVerifiedMessage":
        from ._schemas.message import CustomerEmailVerifiedMessageSchema

        return CustomerEmailVerifiedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import CustomerEmailVerifiedMessageSchema

        return CustomerEmailVerifiedMessageSchema().dump(self)


class CustomerGroupSetMessage(Message):
    customer_group: "CustomerGroupReference"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        customer_group: "CustomerGroupReference"
    ):
        self.customer_group = customer_group
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="CustomerGroupSet",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerGroupSetMessage":
        from ._schemas.message import CustomerGroupSetMessageSchema

        return CustomerGroupSetMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import CustomerGroupSetMessageSchema

        return CustomerGroupSetMessageSchema().dump(self)


class DeliveryAddedMessage(Message):
    delivery: "Delivery"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        delivery: "Delivery"
    ):
        self.delivery = delivery
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="DeliveryAdded",
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "DeliveryAddedMessage":
        from ._schemas.message import DeliveryAddedMessageSchema

        return DeliveryAddedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import DeliveryAddedMessageSchema

        return DeliveryAddedMessageSchema().dump(self)


class DeliveryAddressSetMessage(Message):
    delivery_id: "str"
    address: typing.Optional["Address"]
    old_address: typing.Optional["Address"]

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        delivery_id: "str",
        address: typing.Optional["Address"] = None,
        old_address: typing.Optional["Address"] = None
    ):
        self.delivery_id = delivery_id
        self.address = address
        self.old_address = old_address
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="DeliveryAddressSet",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DeliveryAddressSetMessage":
        from ._schemas.message import DeliveryAddressSetMessageSchema

        return DeliveryAddressSetMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import DeliveryAddressSetMessageSchema

        return DeliveryAddressSetMessageSchema().dump(self)


class DeliveryItemsUpdatedMessage(Message):
    delivery_id: "str"
    items: typing.List["DeliveryItem"]
    old_items: typing.List["DeliveryItem"]

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        delivery_id: "str",
        items: typing.List["DeliveryItem"],
        old_items: typing.List["DeliveryItem"]
    ):
        self.delivery_id = delivery_id
        self.items = items
        self.old_items = old_items
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="DeliveryItemsUpdated",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DeliveryItemsUpdatedMessage":
        from ._schemas.message import DeliveryItemsUpdatedMessageSchema

        return DeliveryItemsUpdatedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import DeliveryItemsUpdatedMessageSchema

        return DeliveryItemsUpdatedMessageSchema().dump(self)


class DeliveryRemovedMessage(Message):
    delivery: "Delivery"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        delivery: "Delivery"
    ):
        self.delivery = delivery
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="DeliveryRemoved",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DeliveryRemovedMessage":
        from ._schemas.message import DeliveryRemovedMessageSchema

        return DeliveryRemovedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import DeliveryRemovedMessageSchema

        return DeliveryRemovedMessageSchema().dump(self)


class InventoryEntryCreatedMessage(Message):
    inventory_entry: "InventoryEntry"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        inventory_entry: "InventoryEntry"
    ):
        self.inventory_entry = inventory_entry
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="InventoryEntryCreated",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InventoryEntryCreatedMessage":
        from ._schemas.message import InventoryEntryCreatedMessageSchema

        return InventoryEntryCreatedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import InventoryEntryCreatedMessageSchema

        return InventoryEntryCreatedMessageSchema().dump(self)


class InventoryEntryDeletedMessage(Message):
    sku: "str"
    supply_channel: "ChannelReference"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        sku: "str",
        supply_channel: "ChannelReference"
    ):
        self.sku = sku
        self.supply_channel = supply_channel
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="InventoryEntryDeleted",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InventoryEntryDeletedMessage":
        from ._schemas.message import InventoryEntryDeletedMessageSchema

        return InventoryEntryDeletedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import InventoryEntryDeletedMessageSchema

        return InventoryEntryDeletedMessageSchema().dump(self)


class InventoryEntryQuantitySetMessage(Message):
    old_quantity_on_stock: "int"
    new_quantity_on_stock: "int"
    old_available_quantity: "int"
    new_available_quantity: "int"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        old_quantity_on_stock: "int",
        new_quantity_on_stock: "int",
        old_available_quantity: "int",
        new_available_quantity: "int"
    ):
        self.old_quantity_on_stock = old_quantity_on_stock
        self.new_quantity_on_stock = new_quantity_on_stock
        self.old_available_quantity = old_available_quantity
        self.new_available_quantity = new_available_quantity
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="InventoryEntryQuantitySet",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InventoryEntryQuantitySetMessage":
        from ._schemas.message import InventoryEntryQuantitySetMessageSchema

        return InventoryEntryQuantitySetMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import InventoryEntryQuantitySetMessageSchema

        return InventoryEntryQuantitySetMessageSchema().dump(self)


class LineItemStateTransitionMessage(Message):
    line_item_id: "str"
    transition_date: "datetime.datetime"
    quantity: "int"
    from_state: "StateReference"
    to_state: "StateReference"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        line_item_id: "str",
        transition_date: "datetime.datetime",
        quantity: "int",
        from_state: "StateReference",
        to_state: "StateReference"
    ):
        self.line_item_id = line_item_id
        self.transition_date = transition_date
        self.quantity = quantity
        self.from_state = from_state
        self.to_state = to_state
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="LineItemStateTransition",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "LineItemStateTransitionMessage":
        from ._schemas.message import LineItemStateTransitionMessageSchema

        return LineItemStateTransitionMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import LineItemStateTransitionMessageSchema

        return LineItemStateTransitionMessageSchema().dump(self)


class MessageConfiguration(_BaseType):
    enabled: "bool"
    delete_days_after_creation: typing.Optional["int"]

    def __init__(
        self,
        *,
        enabled: "bool",
        delete_days_after_creation: typing.Optional["int"] = None
    ):
        self.enabled = enabled
        self.delete_days_after_creation = delete_days_after_creation
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MessageConfiguration":
        from ._schemas.message import MessageConfigurationSchema

        return MessageConfigurationSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import MessageConfigurationSchema

        return MessageConfigurationSchema().dump(self)


class MessageConfigurationDraft(_BaseType):
    enabled: "bool"
    delete_days_after_creation: "int"

    def __init__(self, *, enabled: "bool", delete_days_after_creation: "int"):
        self.enabled = enabled
        self.delete_days_after_creation = delete_days_after_creation
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MessageConfigurationDraft":
        from ._schemas.message import MessageConfigurationDraftSchema

        return MessageConfigurationDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import MessageConfigurationDraftSchema

        return MessageConfigurationDraftSchema().dump(self)


class MessagePagedQueryResponse(_BaseType):
    limit: "int"
    count: "int"
    total: typing.Optional["int"]
    offset: "int"
    results: typing.List["Message"]

    def __init__(
        self,
        *,
        limit: "int",
        count: "int",
        total: typing.Optional["int"] = None,
        offset: "int",
        results: typing.List["Message"]
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
    ) -> "MessagePagedQueryResponse":
        from ._schemas.message import MessagePagedQueryResponseSchema

        return MessagePagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import MessagePagedQueryResponseSchema

        return MessagePagedQueryResponseSchema().dump(self)


class OrderBillingAddressSetMessage(Message):
    address: typing.Optional["Address"]
    old_address: typing.Optional["Address"]

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        address: typing.Optional["Address"] = None,
        old_address: typing.Optional["Address"] = None
    ):
        self.address = address
        self.old_address = old_address
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="OrderBillingAddressSet",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderBillingAddressSetMessage":
        from ._schemas.message import OrderBillingAddressSetMessageSchema

        return OrderBillingAddressSetMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderBillingAddressSetMessageSchema

        return OrderBillingAddressSetMessageSchema().dump(self)


class OrderCreatedMessage(Message):
    order: "Order"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        order: "Order"
    ):
        self.order = order
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="OrderCreated",
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OrderCreatedMessage":
        from ._schemas.message import OrderCreatedMessageSchema

        return OrderCreatedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderCreatedMessageSchema

        return OrderCreatedMessageSchema().dump(self)


class OrderCustomLineItemDiscountSetMessage(Message):
    custom_line_item_id: "str"
    discounted_price_per_quantity: typing.List["DiscountedLineItemPriceForQuantity"]
    taxed_price: typing.Optional["TaxedItemPrice"]

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        custom_line_item_id: "str",
        discounted_price_per_quantity: typing.List[
            "DiscountedLineItemPriceForQuantity"
        ],
        taxed_price: typing.Optional["TaxedItemPrice"] = None
    ):
        self.custom_line_item_id = custom_line_item_id
        self.discounted_price_per_quantity = discounted_price_per_quantity
        self.taxed_price = taxed_price
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="OrderCustomLineItemDiscountSet",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderCustomLineItemDiscountSetMessage":
        from ._schemas.message import OrderCustomLineItemDiscountSetMessageSchema

        return OrderCustomLineItemDiscountSetMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderCustomLineItemDiscountSetMessageSchema

        return OrderCustomLineItemDiscountSetMessageSchema().dump(self)


class OrderCustomerEmailSetMessage(Message):
    email: typing.Optional["str"]
    old_email: typing.Optional["str"]

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        email: typing.Optional["str"] = None,
        old_email: typing.Optional["str"] = None
    ):
        self.email = email
        self.old_email = old_email
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="OrderCustomerEmailSet",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderCustomerEmailSetMessage":
        from ._schemas.message import OrderCustomerEmailSetMessageSchema

        return OrderCustomerEmailSetMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderCustomerEmailSetMessageSchema

        return OrderCustomerEmailSetMessageSchema().dump(self)


class OrderCustomerGroupSetMessage(Message):
    customer_group: typing.Optional["CustomerGroupReference"]
    old_customer_group: typing.Optional["CustomerGroupReference"]

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        customer_group: typing.Optional["CustomerGroupReference"] = None,
        old_customer_group: typing.Optional["CustomerGroupReference"] = None
    ):
        self.customer_group = customer_group
        self.old_customer_group = old_customer_group
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="OrderCustomerGroupSet",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderCustomerGroupSetMessage":
        from ._schemas.message import OrderCustomerGroupSetMessageSchema

        return OrderCustomerGroupSetMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderCustomerGroupSetMessageSchema

        return OrderCustomerGroupSetMessageSchema().dump(self)


class OrderCustomerSetMessage(Message):
    customer: typing.Optional["CustomerReference"]
    customer_group: typing.Optional["CustomerGroupReference"]
    old_customer: typing.Optional["CustomerReference"]
    old_customer_group: typing.Optional["CustomerGroupReference"]

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        customer: typing.Optional["CustomerReference"] = None,
        customer_group: typing.Optional["CustomerGroupReference"] = None,
        old_customer: typing.Optional["CustomerReference"] = None,
        old_customer_group: typing.Optional["CustomerGroupReference"] = None
    ):
        self.customer = customer
        self.customer_group = customer_group
        self.old_customer = old_customer
        self.old_customer_group = old_customer_group
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="OrderCustomerSet",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderCustomerSetMessage":
        from ._schemas.message import OrderCustomerSetMessageSchema

        return OrderCustomerSetMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderCustomerSetMessageSchema

        return OrderCustomerSetMessageSchema().dump(self)


class OrderDeletedMessage(Message):
    order: "Order"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        order: "Order"
    ):
        self.order = order
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="OrderDeleted",
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OrderDeletedMessage":
        from ._schemas.message import OrderDeletedMessageSchema

        return OrderDeletedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderDeletedMessageSchema

        return OrderDeletedMessageSchema().dump(self)


class OrderDiscountCodeAddedMessage(Message):
    discount_code: "DiscountCodeReference"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        discount_code: "DiscountCodeReference"
    ):
        self.discount_code = discount_code
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="OrderDiscountCodeAdded",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderDiscountCodeAddedMessage":
        from ._schemas.message import OrderDiscountCodeAddedMessageSchema

        return OrderDiscountCodeAddedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderDiscountCodeAddedMessageSchema

        return OrderDiscountCodeAddedMessageSchema().dump(self)


class OrderDiscountCodeRemovedMessage(Message):
    discount_code: "DiscountCodeReference"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        discount_code: "DiscountCodeReference"
    ):
        self.discount_code = discount_code
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="OrderDiscountCodeRemoved",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderDiscountCodeRemovedMessage":
        from ._schemas.message import OrderDiscountCodeRemovedMessageSchema

        return OrderDiscountCodeRemovedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderDiscountCodeRemovedMessageSchema

        return OrderDiscountCodeRemovedMessageSchema().dump(self)


class OrderDiscountCodeStateSetMessage(Message):
    discount_code: "DiscountCodeReference"
    state: "DiscountCodeState"
    old_state: typing.Optional["DiscountCodeState"]

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        discount_code: "DiscountCodeReference",
        state: "DiscountCodeState",
        old_state: typing.Optional["DiscountCodeState"] = None
    ):
        self.discount_code = discount_code
        self.state = state
        self.old_state = old_state
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="OrderDiscountCodeStateSet",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderDiscountCodeStateSetMessage":
        from ._schemas.message import OrderDiscountCodeStateSetMessageSchema

        return OrderDiscountCodeStateSetMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderDiscountCodeStateSetMessageSchema

        return OrderDiscountCodeStateSetMessageSchema().dump(self)


class OrderEditAppliedMessage(Message):
    edit: "OrderEditReference"
    result: "OrderEditApplied"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        edit: "OrderEditReference",
        result: "OrderEditApplied"
    ):
        self.edit = edit
        self.result = result
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="OrderEditApplied",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderEditAppliedMessage":
        from ._schemas.message import OrderEditAppliedMessageSchema

        return OrderEditAppliedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderEditAppliedMessageSchema

        return OrderEditAppliedMessageSchema().dump(self)


class OrderImportedMessage(Message):
    order: "Order"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        order: "Order"
    ):
        self.order = order
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="OrderImported",
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OrderImportedMessage":
        from ._schemas.message import OrderImportedMessageSchema

        return OrderImportedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderImportedMessageSchema

        return OrderImportedMessageSchema().dump(self)


class OrderLineItemAddedMessage(Message):
    line_item: "LineItem"
    added_quantity: "int"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        line_item: "LineItem",
        added_quantity: "int"
    ):
        self.line_item = line_item
        self.added_quantity = added_quantity
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="OrderLineItemAdded",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderLineItemAddedMessage":
        from ._schemas.message import OrderLineItemAddedMessageSchema

        return OrderLineItemAddedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderLineItemAddedMessageSchema

        return OrderLineItemAddedMessageSchema().dump(self)


class OrderLineItemDiscountSetMessage(Message):
    line_item_id: "str"
    discounted_price_per_quantity: typing.List["DiscountedLineItemPriceForQuantity"]
    total_price: "Money"
    taxed_price: typing.Optional["TaxedItemPrice"]

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        line_item_id: "str",
        discounted_price_per_quantity: typing.List[
            "DiscountedLineItemPriceForQuantity"
        ],
        total_price: "Money",
        taxed_price: typing.Optional["TaxedItemPrice"] = None
    ):
        self.line_item_id = line_item_id
        self.discounted_price_per_quantity = discounted_price_per_quantity
        self.total_price = total_price
        self.taxed_price = taxed_price
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="OrderLineItemDiscountSet",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderLineItemDiscountSetMessage":
        from ._schemas.message import OrderLineItemDiscountSetMessageSchema

        return OrderLineItemDiscountSetMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderLineItemDiscountSetMessageSchema

        return OrderLineItemDiscountSetMessageSchema().dump(self)


class OrderPaymentStateChangedMessage(Message):
    payment_state: "PaymentState"
    old_payment_state: typing.Optional["PaymentState"]

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        payment_state: "PaymentState",
        old_payment_state: typing.Optional["PaymentState"] = None
    ):
        self.payment_state = payment_state
        self.old_payment_state = old_payment_state
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="OrderPaymentStateChanged",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderPaymentStateChangedMessage":
        from ._schemas.message import OrderPaymentStateChangedMessageSchema

        return OrderPaymentStateChangedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderPaymentStateChangedMessageSchema

        return OrderPaymentStateChangedMessageSchema().dump(self)


class OrderReturnInfoAddedMessage(Message):
    return_info: "ReturnInfo"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        return_info: "ReturnInfo"
    ):
        self.return_info = return_info
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="ReturnInfoAdded",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderReturnInfoAddedMessage":
        from ._schemas.message import OrderReturnInfoAddedMessageSchema

        return OrderReturnInfoAddedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderReturnInfoAddedMessageSchema

        return OrderReturnInfoAddedMessageSchema().dump(self)


class OrderReturnShipmentStateChangedMessage(Message):
    return_item_id: "str"
    return_shipment_state: "ReturnShipmentState"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        return_item_id: "str",
        return_shipment_state: "ReturnShipmentState"
    ):
        self.return_item_id = return_item_id
        self.return_shipment_state = return_shipment_state
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="OrderReturnShipmentStateChanged",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderReturnShipmentStateChangedMessage":
        from ._schemas.message import OrderReturnShipmentStateChangedMessageSchema

        return OrderReturnShipmentStateChangedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderReturnShipmentStateChangedMessageSchema

        return OrderReturnShipmentStateChangedMessageSchema().dump(self)


class OrderShipmentStateChangedMessage(Message):
    shipment_state: "ShipmentState"
    old_shipment_state: typing.Optional["ShipmentState"]

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        shipment_state: "ShipmentState",
        old_shipment_state: typing.Optional["ShipmentState"] = None
    ):
        self.shipment_state = shipment_state
        self.old_shipment_state = old_shipment_state
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="OrderShipmentStateChanged",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderShipmentStateChangedMessage":
        from ._schemas.message import OrderShipmentStateChangedMessageSchema

        return OrderShipmentStateChangedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderShipmentStateChangedMessageSchema

        return OrderShipmentStateChangedMessageSchema().dump(self)


class OrderShippingAddressSetMessage(Message):
    address: typing.Optional["Address"]
    old_address: typing.Optional["Address"]

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        address: typing.Optional["Address"] = None,
        old_address: typing.Optional["Address"] = None
    ):
        self.address = address
        self.old_address = old_address
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="OrderShippingAddressSet",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderShippingAddressSetMessage":
        from ._schemas.message import OrderShippingAddressSetMessageSchema

        return OrderShippingAddressSetMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderShippingAddressSetMessageSchema

        return OrderShippingAddressSetMessageSchema().dump(self)


class OrderShippingInfoSetMessage(Message):
    shipping_info: typing.Optional["ShippingInfo"]
    old_shipping_info: typing.Optional["ShippingInfo"]

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        shipping_info: typing.Optional["ShippingInfo"] = None,
        old_shipping_info: typing.Optional["ShippingInfo"] = None
    ):
        self.shipping_info = shipping_info
        self.old_shipping_info = old_shipping_info
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="OrderShippingInfoSet",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderShippingInfoSetMessage":
        from ._schemas.message import OrderShippingInfoSetMessageSchema

        return OrderShippingInfoSetMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderShippingInfoSetMessageSchema

        return OrderShippingInfoSetMessageSchema().dump(self)


class OrderShippingRateInputSetMessage(Message):
    shipping_rate_input: typing.Optional["ShippingRateInput"]
    old_shipping_rate_input: typing.Optional["ShippingRateInput"]

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        shipping_rate_input: typing.Optional["ShippingRateInput"] = None,
        old_shipping_rate_input: typing.Optional["ShippingRateInput"] = None
    ):
        self.shipping_rate_input = shipping_rate_input
        self.old_shipping_rate_input = old_shipping_rate_input
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="OrderShippingRateInputSet",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderShippingRateInputSetMessage":
        from ._schemas.message import OrderShippingRateInputSetMessageSchema

        return OrderShippingRateInputSetMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderShippingRateInputSetMessageSchema

        return OrderShippingRateInputSetMessageSchema().dump(self)


class OrderStateChangedMessage(Message):
    order_state: "OrderState"
    old_order_state: "OrderState"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        order_state: "OrderState",
        old_order_state: "OrderState"
    ):
        self.order_state = order_state
        self.old_order_state = old_order_state
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="OrderStateChanged",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderStateChangedMessage":
        from ._schemas.message import OrderStateChangedMessageSchema

        return OrderStateChangedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderStateChangedMessageSchema

        return OrderStateChangedMessageSchema().dump(self)


class OrderStateTransitionMessage(Message):
    state: "StateReference"
    force: "bool"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        state: "StateReference",
        force: "bool"
    ):
        self.state = state
        self.force = force
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="OrderStateTransition",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderStateTransitionMessage":
        from ._schemas.message import OrderStateTransitionMessageSchema

        return OrderStateTransitionMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderStateTransitionMessageSchema

        return OrderStateTransitionMessageSchema().dump(self)


class OrderStoreSetMessage(Message):
    store: "StoreKeyReference"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        store: "StoreKeyReference"
    ):
        self.store = store
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="OrderStoreSet",
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OrderStoreSetMessage":
        from ._schemas.message import OrderStoreSetMessageSchema

        return OrderStoreSetMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderStoreSetMessageSchema

        return OrderStoreSetMessageSchema().dump(self)


class ParcelAddedToDeliveryMessage(Message):
    delivery: "Delivery"
    parcel: "Parcel"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        delivery: "Delivery",
        parcel: "Parcel"
    ):
        self.delivery = delivery
        self.parcel = parcel
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="ParcelAddedToDelivery",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ParcelAddedToDeliveryMessage":
        from ._schemas.message import ParcelAddedToDeliveryMessageSchema

        return ParcelAddedToDeliveryMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ParcelAddedToDeliveryMessageSchema

        return ParcelAddedToDeliveryMessageSchema().dump(self)


class ParcelItemsUpdatedMessage(Message):
    parcel_id: "str"
    delivery_id: typing.Optional["str"]
    items: typing.List["DeliveryItem"]
    old_items: typing.List["DeliveryItem"]

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        parcel_id: "str",
        delivery_id: typing.Optional["str"] = None,
        items: typing.List["DeliveryItem"],
        old_items: typing.List["DeliveryItem"]
    ):
        self.parcel_id = parcel_id
        self.delivery_id = delivery_id
        self.items = items
        self.old_items = old_items
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="ParcelItemsUpdated",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ParcelItemsUpdatedMessage":
        from ._schemas.message import ParcelItemsUpdatedMessageSchema

        return ParcelItemsUpdatedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ParcelItemsUpdatedMessageSchema

        return ParcelItemsUpdatedMessageSchema().dump(self)


class ParcelMeasurementsUpdatedMessage(Message):
    delivery_id: "str"
    parcel_id: "str"
    measurements: typing.Optional["ParcelMeasurements"]

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        delivery_id: "str",
        parcel_id: "str",
        measurements: typing.Optional["ParcelMeasurements"] = None
    ):
        self.delivery_id = delivery_id
        self.parcel_id = parcel_id
        self.measurements = measurements
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="ParcelMeasurementsUpdated",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ParcelMeasurementsUpdatedMessage":
        from ._schemas.message import ParcelMeasurementsUpdatedMessageSchema

        return ParcelMeasurementsUpdatedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ParcelMeasurementsUpdatedMessageSchema

        return ParcelMeasurementsUpdatedMessageSchema().dump(self)


class ParcelRemovedFromDeliveryMessage(Message):
    delivery_id: "str"
    parcel: "Parcel"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        delivery_id: "str",
        parcel: "Parcel"
    ):
        self.delivery_id = delivery_id
        self.parcel = parcel
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="ParcelRemovedFromDelivery",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ParcelRemovedFromDeliveryMessage":
        from ._schemas.message import ParcelRemovedFromDeliveryMessageSchema

        return ParcelRemovedFromDeliveryMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ParcelRemovedFromDeliveryMessageSchema

        return ParcelRemovedFromDeliveryMessageSchema().dump(self)


class ParcelTrackingDataUpdatedMessage(Message):
    delivery_id: "str"
    parcel_id: "str"
    tracking_data: typing.Optional["TrackingData"]

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        delivery_id: "str",
        parcel_id: "str",
        tracking_data: typing.Optional["TrackingData"] = None
    ):
        self.delivery_id = delivery_id
        self.parcel_id = parcel_id
        self.tracking_data = tracking_data
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="ParcelTrackingDataUpdated",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ParcelTrackingDataUpdatedMessage":
        from ._schemas.message import ParcelTrackingDataUpdatedMessageSchema

        return ParcelTrackingDataUpdatedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ParcelTrackingDataUpdatedMessageSchema

        return ParcelTrackingDataUpdatedMessageSchema().dump(self)


class PaymentCreatedMessage(Message):
    payment: "Payment"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        payment: "Payment"
    ):
        self.payment = payment
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="PaymentCreated",
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "PaymentCreatedMessage":
        from ._schemas.message import PaymentCreatedMessageSchema

        return PaymentCreatedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import PaymentCreatedMessageSchema

        return PaymentCreatedMessageSchema().dump(self)


class PaymentInteractionAddedMessage(Message):
    interaction: "CustomFields"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        interaction: "CustomFields"
    ):
        self.interaction = interaction
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="PaymentInteractionAdded",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentInteractionAddedMessage":
        from ._schemas.message import PaymentInteractionAddedMessageSchema

        return PaymentInteractionAddedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import PaymentInteractionAddedMessageSchema

        return PaymentInteractionAddedMessageSchema().dump(self)


class PaymentStatusInterfaceCodeSetMessage(Message):
    payment_id: "str"
    interface_code: "str"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        payment_id: "str",
        interface_code: "str"
    ):
        self.payment_id = payment_id
        self.interface_code = interface_code
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="PaymentStatusInterfaceCodeSet",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentStatusInterfaceCodeSetMessage":
        from ._schemas.message import PaymentStatusInterfaceCodeSetMessageSchema

        return PaymentStatusInterfaceCodeSetMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import PaymentStatusInterfaceCodeSetMessageSchema

        return PaymentStatusInterfaceCodeSetMessageSchema().dump(self)


class PaymentStatusStateTransitionMessage(Message):
    state: "StateReference"
    force: "bool"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        state: "StateReference",
        force: "bool"
    ):
        self.state = state
        self.force = force
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="PaymentStatusStateTransition",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentStatusStateTransitionMessage":
        from ._schemas.message import PaymentStatusStateTransitionMessageSchema

        return PaymentStatusStateTransitionMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import PaymentStatusStateTransitionMessageSchema

        return PaymentStatusStateTransitionMessageSchema().dump(self)


class PaymentTransactionAddedMessage(Message):
    transaction: "Transaction"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        transaction: "Transaction"
    ):
        self.transaction = transaction
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="PaymentTransactionAdded",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentTransactionAddedMessage":
        from ._schemas.message import PaymentTransactionAddedMessageSchema

        return PaymentTransactionAddedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import PaymentTransactionAddedMessageSchema

        return PaymentTransactionAddedMessageSchema().dump(self)


class PaymentTransactionStateChangedMessage(Message):
    transaction_id: "str"
    state: "TransactionState"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        transaction_id: "str",
        state: "TransactionState"
    ):
        self.transaction_id = transaction_id
        self.state = state
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="PaymentTransactionStateChanged",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentTransactionStateChangedMessage":
        from ._schemas.message import PaymentTransactionStateChangedMessageSchema

        return PaymentTransactionStateChangedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import PaymentTransactionStateChangedMessageSchema

        return PaymentTransactionStateChangedMessageSchema().dump(self)


class ProductAddedToCategoryMessage(Message):
    category: "CategoryReference"
    staged: "bool"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        category: "CategoryReference",
        staged: "bool"
    ):
        self.category = category
        self.staged = staged
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="ProductAddedToCategory",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductAddedToCategoryMessage":
        from ._schemas.message import ProductAddedToCategoryMessageSchema

        return ProductAddedToCategoryMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ProductAddedToCategoryMessageSchema

        return ProductAddedToCategoryMessageSchema().dump(self)


class ProductCreatedMessage(Message):
    product_projection: "ProductProjection"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        product_projection: "ProductProjection"
    ):
        self.product_projection = product_projection
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="ProductCreated",
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductCreatedMessage":
        from ._schemas.message import ProductCreatedMessageSchema

        return ProductCreatedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ProductCreatedMessageSchema

        return ProductCreatedMessageSchema().dump(self)


class ProductDeletedMessage(Message):
    removed_image_urls: typing.List["str"]
    current_projection: "ProductProjection"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        removed_image_urls: typing.List["str"],
        current_projection: "ProductProjection"
    ):
        self.removed_image_urls = removed_image_urls
        self.current_projection = current_projection
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="ProductDeleted",
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductDeletedMessage":
        from ._schemas.message import ProductDeletedMessageSchema

        return ProductDeletedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ProductDeletedMessageSchema

        return ProductDeletedMessageSchema().dump(self)


class ProductImageAddedMessage(Message):
    variant_id: "int"
    image: "Image"
    staged: "bool"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        variant_id: "int",
        image: "Image",
        staged: "bool"
    ):
        self.variant_id = variant_id
        self.image = image
        self.staged = staged
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="ProductImageAdded",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductImageAddedMessage":
        from ._schemas.message import ProductImageAddedMessageSchema

        return ProductImageAddedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ProductImageAddedMessageSchema

        return ProductImageAddedMessageSchema().dump(self)


class ProductPriceDiscountsSetMessage(Message):
    updated_prices: typing.List["ProductPriceDiscountsSetUpdatedPrice"]

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        updated_prices: typing.List["ProductPriceDiscountsSetUpdatedPrice"]
    ):
        self.updated_prices = updated_prices
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="ProductPriceDiscountsSet",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductPriceDiscountsSetMessage":
        from ._schemas.message import ProductPriceDiscountsSetMessageSchema

        return ProductPriceDiscountsSetMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ProductPriceDiscountsSetMessageSchema

        return ProductPriceDiscountsSetMessageSchema().dump(self)


class ProductPriceDiscountsSetUpdatedPrice(_BaseType):
    variant_id: "int"
    variant_key: typing.Optional["str"]
    sku: typing.Optional["str"]
    price_id: "str"
    discounted: typing.Optional["DiscountedPrice"]
    staged: "bool"

    def __init__(
        self,
        *,
        variant_id: "int",
        variant_key: typing.Optional["str"] = None,
        sku: typing.Optional["str"] = None,
        price_id: "str",
        discounted: typing.Optional["DiscountedPrice"] = None,
        staged: "bool"
    ):
        self.variant_id = variant_id
        self.variant_key = variant_key
        self.sku = sku
        self.price_id = price_id
        self.discounted = discounted
        self.staged = staged
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductPriceDiscountsSetUpdatedPrice":
        from ._schemas.message import ProductPriceDiscountsSetUpdatedPriceSchema

        return ProductPriceDiscountsSetUpdatedPriceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ProductPriceDiscountsSetUpdatedPriceSchema

        return ProductPriceDiscountsSetUpdatedPriceSchema().dump(self)


class ProductPriceExternalDiscountSetMessage(Message):
    variant_id: "int"
    variant_key: typing.Optional["str"]
    sku: typing.Optional["str"]
    price_id: "str"
    discounted: typing.Optional["DiscountedPrice"]
    staged: "bool"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        variant_id: "int",
        variant_key: typing.Optional["str"] = None,
        sku: typing.Optional["str"] = None,
        price_id: "str",
        discounted: typing.Optional["DiscountedPrice"] = None,
        staged: "bool"
    ):
        self.variant_id = variant_id
        self.variant_key = variant_key
        self.sku = sku
        self.price_id = price_id
        self.discounted = discounted
        self.staged = staged
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="ProductPriceExternalDiscountSet",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductPriceExternalDiscountSetMessage":
        from ._schemas.message import ProductPriceExternalDiscountSetMessageSchema

        return ProductPriceExternalDiscountSetMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ProductPriceExternalDiscountSetMessageSchema

        return ProductPriceExternalDiscountSetMessageSchema().dump(self)


class ProductPublishedMessage(Message):
    removed_image_urls: typing.List["str"]
    product_projection: "ProductProjection"
    scope: "ProductPublishScope"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        removed_image_urls: typing.List["str"],
        product_projection: "ProductProjection",
        scope: "ProductPublishScope"
    ):
        self.removed_image_urls = removed_image_urls
        self.product_projection = product_projection
        self.scope = scope
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="ProductPublished",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductPublishedMessage":
        from ._schemas.message import ProductPublishedMessageSchema

        return ProductPublishedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ProductPublishedMessageSchema

        return ProductPublishedMessageSchema().dump(self)


class ProductRemovedFromCategoryMessage(Message):
    category: "CategoryReference"
    staged: "bool"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        category: "CategoryReference",
        staged: "bool"
    ):
        self.category = category
        self.staged = staged
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="ProductRemovedFromCategory",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductRemovedFromCategoryMessage":
        from ._schemas.message import ProductRemovedFromCategoryMessageSchema

        return ProductRemovedFromCategoryMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ProductRemovedFromCategoryMessageSchema

        return ProductRemovedFromCategoryMessageSchema().dump(self)


class ProductRevertedStagedChangesMessage(Message):
    removed_image_urls: typing.List["str"]

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        removed_image_urls: typing.List["str"]
    ):
        self.removed_image_urls = removed_image_urls
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="ProductRevertedStagedChanges",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductRevertedStagedChangesMessage":
        from ._schemas.message import ProductRevertedStagedChangesMessageSchema

        return ProductRevertedStagedChangesMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ProductRevertedStagedChangesMessageSchema

        return ProductRevertedStagedChangesMessageSchema().dump(self)


class ProductSlugChangedMessage(Message):
    slug: "LocalizedString"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        slug: "LocalizedString"
    ):
        self.slug = slug
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="ProductSlugChanged",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSlugChangedMessage":
        from ._schemas.message import ProductSlugChangedMessageSchema

        return ProductSlugChangedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ProductSlugChangedMessageSchema

        return ProductSlugChangedMessageSchema().dump(self)


class ProductStateTransitionMessage(Message):
    state: "StateReference"
    force: "bool"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        state: "StateReference",
        force: "bool"
    ):
        self.state = state
        self.force = force
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="ProductStateTransition",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductStateTransitionMessage":
        from ._schemas.message import ProductStateTransitionMessageSchema

        return ProductStateTransitionMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ProductStateTransitionMessageSchema

        return ProductStateTransitionMessageSchema().dump(self)


class ProductUnpublishedMessage(Message):
    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None
    ):

        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="ProductUnpublished",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductUnpublishedMessage":
        from ._schemas.message import ProductUnpublishedMessageSchema

        return ProductUnpublishedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ProductUnpublishedMessageSchema

        return ProductUnpublishedMessageSchema().dump(self)


class ProductVariantAddedMessage(Message):
    variant: "ProductVariant"
    staged: "bool"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        variant: "ProductVariant",
        staged: "bool"
    ):
        self.variant = variant
        self.staged = staged
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="ProductVariantAdded",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductVariantAddedMessage":
        from ._schemas.message import ProductVariantAddedMessageSchema

        return ProductVariantAddedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ProductVariantAddedMessageSchema

        return ProductVariantAddedMessageSchema().dump(self)


class ProductVariantDeletedMessage(Message):
    variant: "ProductVariant"
    removed_image_urls: typing.List["str"]

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        variant: "ProductVariant",
        removed_image_urls: typing.List["str"]
    ):
        self.variant = variant
        self.removed_image_urls = removed_image_urls
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="ProductVariantDeleted",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductVariantDeletedMessage":
        from ._schemas.message import ProductVariantDeletedMessageSchema

        return ProductVariantDeletedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ProductVariantDeletedMessageSchema

        return ProductVariantDeletedMessageSchema().dump(self)


class ReviewCreatedMessage(Message):
    review: "Review"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        review: "Review"
    ):
        self.review = review
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="ReviewCreated",
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ReviewCreatedMessage":
        from ._schemas.message import ReviewCreatedMessageSchema

        return ReviewCreatedMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ReviewCreatedMessageSchema

        return ReviewCreatedMessageSchema().dump(self)


class ReviewRatingSetMessage(Message):
    old_rating: typing.Optional["float"]
    new_rating: typing.Optional["float"]
    included_in_statistics: "bool"
    target: typing.Optional["Reference"]

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        old_rating: typing.Optional["float"] = None,
        new_rating: typing.Optional["float"] = None,
        included_in_statistics: "bool",
        target: typing.Optional["Reference"] = None
    ):
        self.old_rating = old_rating
        self.new_rating = new_rating
        self.included_in_statistics = included_in_statistics
        self.target = target
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="ReviewRatingSet",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ReviewRatingSetMessage":
        from ._schemas.message import ReviewRatingSetMessageSchema

        return ReviewRatingSetMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ReviewRatingSetMessageSchema

        return ReviewRatingSetMessageSchema().dump(self)


class ReviewStateTransitionMessage(Message):
    old_state: "StateReference"
    new_state: "StateReference"
    old_included_in_statistics: "bool"
    new_included_in_statistics: "bool"
    target: "Reference"
    force: "bool"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sequence_number: "int",
        resource: "Reference",
        resource_version: "int",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        old_state: "StateReference",
        new_state: "StateReference",
        old_included_in_statistics: "bool",
        new_included_in_statistics: "bool",
        target: "Reference",
        force: "bool"
    ):
        self.old_state = old_state
        self.new_state = new_state
        self.old_included_in_statistics = old_included_in_statistics
        self.new_included_in_statistics = new_included_in_statistics
        self.target = target
        self.force = force
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            sequence_number=sequence_number,
            resource=resource,
            resource_version=resource_version,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            type="ReviewStateTransition",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ReviewStateTransitionMessage":
        from ._schemas.message import ReviewStateTransitionMessageSchema

        return ReviewStateTransitionMessageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ReviewStateTransitionMessageSchema

        return ReviewStateTransitionMessageSchema().dump(self)


class UserProvidedIdentifiers(_BaseType):
    key: typing.Optional["str"]
    external_id: typing.Optional["str"]
    order_number: typing.Optional["str"]
    customer_number: typing.Optional["str"]
    sku: typing.Optional["str"]
    slug: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        key: typing.Optional["str"] = None,
        external_id: typing.Optional["str"] = None,
        order_number: typing.Optional["str"] = None,
        customer_number: typing.Optional["str"] = None,
        sku: typing.Optional["str"] = None,
        slug: typing.Optional["LocalizedString"] = None
    ):
        self.key = key
        self.external_id = external_id
        self.order_number = order_number
        self.customer_number = customer_number
        self.sku = sku
        self.slug = slug
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "UserProvidedIdentifiers":
        from ._schemas.message import UserProvidedIdentifiersSchema

        return UserProvidedIdentifiersSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import UserProvidedIdentifiersSchema

        return UserProvidedIdentifiersSchema().dump(self)


class MessagePayload(_BaseType):
    type: "str"

    def __init__(self, *, type: "str"):
        self.type = type
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MessagePayload":
        from ._schemas.message import MessagePayloadSchema

        return MessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import MessagePayloadSchema

        return MessagePayloadSchema().dump(self)


class CategoryCreatedMessagePayload(MessagePayload):
    category: "Category"

    def __init__(self, *, category: "Category"):
        self.category = category
        super().__init__(type="CategoryCreated")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CategoryCreatedMessagePayload":
        from ._schemas.message import CategoryCreatedMessagePayloadSchema

        return CategoryCreatedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import CategoryCreatedMessagePayloadSchema

        return CategoryCreatedMessagePayloadSchema().dump(self)


class CategorySlugChangedMessagePayload(MessagePayload):
    slug: "LocalizedString"

    def __init__(self, *, slug: "LocalizedString"):
        self.slug = slug
        super().__init__(type="CategorySlugChanged")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CategorySlugChangedMessagePayload":
        from ._schemas.message import CategorySlugChangedMessagePayloadSchema

        return CategorySlugChangedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import CategorySlugChangedMessagePayloadSchema

        return CategorySlugChangedMessagePayloadSchema().dump(self)


class CustomLineItemStateTransitionMessagePayload(MessagePayload):
    custom_line_item_id: "str"
    transition_date: "datetime.datetime"
    quantity: "int"
    from_state: "StateReference"
    to_state: "StateReference"

    def __init__(
        self,
        *,
        custom_line_item_id: "str",
        transition_date: "datetime.datetime",
        quantity: "int",
        from_state: "StateReference",
        to_state: "StateReference"
    ):
        self.custom_line_item_id = custom_line_item_id
        self.transition_date = transition_date
        self.quantity = quantity
        self.from_state = from_state
        self.to_state = to_state
        super().__init__(type="CustomLineItemStateTransition")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomLineItemStateTransitionMessagePayload":
        from ._schemas.message import CustomLineItemStateTransitionMessagePayloadSchema

        return CustomLineItemStateTransitionMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import CustomLineItemStateTransitionMessagePayloadSchema

        return CustomLineItemStateTransitionMessagePayloadSchema().dump(self)


class CustomerAddressAddedMessagePayload(MessagePayload):
    address: "Address"

    def __init__(self, *, address: "Address"):
        self.address = address
        super().__init__(type="CustomerAddressAdded")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerAddressAddedMessagePayload":
        from ._schemas.message import CustomerAddressAddedMessagePayloadSchema

        return CustomerAddressAddedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import CustomerAddressAddedMessagePayloadSchema

        return CustomerAddressAddedMessagePayloadSchema().dump(self)


class CustomerAddressChangedMessagePayload(MessagePayload):
    address: "Address"

    def __init__(self, *, address: "Address"):
        self.address = address
        super().__init__(type="CustomerAddressChanged")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerAddressChangedMessagePayload":
        from ._schemas.message import CustomerAddressChangedMessagePayloadSchema

        return CustomerAddressChangedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import CustomerAddressChangedMessagePayloadSchema

        return CustomerAddressChangedMessagePayloadSchema().dump(self)


class CustomerAddressRemovedMessagePayload(MessagePayload):
    address: "Address"

    def __init__(self, *, address: "Address"):
        self.address = address
        super().__init__(type="CustomerAddressRemoved")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerAddressRemovedMessagePayload":
        from ._schemas.message import CustomerAddressRemovedMessagePayloadSchema

        return CustomerAddressRemovedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import CustomerAddressRemovedMessagePayloadSchema

        return CustomerAddressRemovedMessagePayloadSchema().dump(self)


class CustomerCompanyNameSetMessagePayload(MessagePayload):
    company_name: "str"

    def __init__(self, *, company_name: "str"):
        self.company_name = company_name
        super().__init__(type="CustomerCompanyNameSet")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerCompanyNameSetMessagePayload":
        from ._schemas.message import CustomerCompanyNameSetMessagePayloadSchema

        return CustomerCompanyNameSetMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import CustomerCompanyNameSetMessagePayloadSchema

        return CustomerCompanyNameSetMessagePayloadSchema().dump(self)


class CustomerCreatedMessagePayload(MessagePayload):
    customer: "Customer"

    def __init__(self, *, customer: "Customer"):
        self.customer = customer
        super().__init__(type="CustomerCreated")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerCreatedMessagePayload":
        from ._schemas.message import CustomerCreatedMessagePayloadSchema

        return CustomerCreatedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import CustomerCreatedMessagePayloadSchema

        return CustomerCreatedMessagePayloadSchema().dump(self)


class CustomerDateOfBirthSetMessagePayload(MessagePayload):
    date_of_birth: "datetime.date"

    def __init__(self, *, date_of_birth: "datetime.date"):
        self.date_of_birth = date_of_birth
        super().__init__(type="CustomerDateOfBirthSet")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerDateOfBirthSetMessagePayload":
        from ._schemas.message import CustomerDateOfBirthSetMessagePayloadSchema

        return CustomerDateOfBirthSetMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import CustomerDateOfBirthSetMessagePayloadSchema

        return CustomerDateOfBirthSetMessagePayloadSchema().dump(self)


class CustomerEmailChangedMessagePayload(MessagePayload):
    email: "str"

    def __init__(self, *, email: "str"):
        self.email = email
        super().__init__(type="CustomerEmailChanged")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerEmailChangedMessagePayload":
        from ._schemas.message import CustomerEmailChangedMessagePayloadSchema

        return CustomerEmailChangedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import CustomerEmailChangedMessagePayloadSchema

        return CustomerEmailChangedMessagePayloadSchema().dump(self)


class CustomerEmailVerifiedMessagePayload(MessagePayload):
    def __init__(self):

        super().__init__(type="CustomerEmailVerified")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerEmailVerifiedMessagePayload":
        from ._schemas.message import CustomerEmailVerifiedMessagePayloadSchema

        return CustomerEmailVerifiedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import CustomerEmailVerifiedMessagePayloadSchema

        return CustomerEmailVerifiedMessagePayloadSchema().dump(self)


class CustomerGroupSetMessagePayload(MessagePayload):
    customer_group: "CustomerGroupReference"

    def __init__(self, *, customer_group: "CustomerGroupReference"):
        self.customer_group = customer_group
        super().__init__(type="CustomerGroupSet")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerGroupSetMessagePayload":
        from ._schemas.message import CustomerGroupSetMessagePayloadSchema

        return CustomerGroupSetMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import CustomerGroupSetMessagePayloadSchema

        return CustomerGroupSetMessagePayloadSchema().dump(self)


class DeliveryAddedMessagePayload(MessagePayload):
    delivery: "Delivery"

    def __init__(self, *, delivery: "Delivery"):
        self.delivery = delivery
        super().__init__(type="DeliveryAdded")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DeliveryAddedMessagePayload":
        from ._schemas.message import DeliveryAddedMessagePayloadSchema

        return DeliveryAddedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import DeliveryAddedMessagePayloadSchema

        return DeliveryAddedMessagePayloadSchema().dump(self)


class DeliveryAddressSetMessagePayload(MessagePayload):
    delivery_id: "str"
    address: typing.Optional["Address"]
    old_address: typing.Optional["Address"]

    def __init__(
        self,
        *,
        delivery_id: "str",
        address: typing.Optional["Address"] = None,
        old_address: typing.Optional["Address"] = None
    ):
        self.delivery_id = delivery_id
        self.address = address
        self.old_address = old_address
        super().__init__(type="DeliveryAddressSet")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DeliveryAddressSetMessagePayload":
        from ._schemas.message import DeliveryAddressSetMessagePayloadSchema

        return DeliveryAddressSetMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import DeliveryAddressSetMessagePayloadSchema

        return DeliveryAddressSetMessagePayloadSchema().dump(self)


class DeliveryItemsUpdatedMessagePayload(MessagePayload):
    delivery_id: "str"
    items: typing.List["DeliveryItem"]
    old_items: typing.List["DeliveryItem"]

    def __init__(
        self,
        *,
        delivery_id: "str",
        items: typing.List["DeliveryItem"],
        old_items: typing.List["DeliveryItem"]
    ):
        self.delivery_id = delivery_id
        self.items = items
        self.old_items = old_items
        super().__init__(type="DeliveryItemsUpdated")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DeliveryItemsUpdatedMessagePayload":
        from ._schemas.message import DeliveryItemsUpdatedMessagePayloadSchema

        return DeliveryItemsUpdatedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import DeliveryItemsUpdatedMessagePayloadSchema

        return DeliveryItemsUpdatedMessagePayloadSchema().dump(self)


class DeliveryRemovedMessagePayload(MessagePayload):
    delivery: "Delivery"

    def __init__(self, *, delivery: "Delivery"):
        self.delivery = delivery
        super().__init__(type="DeliveryRemoved")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DeliveryRemovedMessagePayload":
        from ._schemas.message import DeliveryRemovedMessagePayloadSchema

        return DeliveryRemovedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import DeliveryRemovedMessagePayloadSchema

        return DeliveryRemovedMessagePayloadSchema().dump(self)


class InventoryEntryCreatedMessagePayload(MessagePayload):
    inventory_entry: "InventoryEntry"

    def __init__(self, *, inventory_entry: "InventoryEntry"):
        self.inventory_entry = inventory_entry
        super().__init__(type="InventoryEntryCreated")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InventoryEntryCreatedMessagePayload":
        from ._schemas.message import InventoryEntryCreatedMessagePayloadSchema

        return InventoryEntryCreatedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import InventoryEntryCreatedMessagePayloadSchema

        return InventoryEntryCreatedMessagePayloadSchema().dump(self)


class InventoryEntryDeletedMessagePayload(MessagePayload):
    sku: "str"
    supply_channel: "ChannelReference"

    def __init__(self, *, sku: "str", supply_channel: "ChannelReference"):
        self.sku = sku
        self.supply_channel = supply_channel
        super().__init__(type="InventoryEntryDeleted")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InventoryEntryDeletedMessagePayload":
        from ._schemas.message import InventoryEntryDeletedMessagePayloadSchema

        return InventoryEntryDeletedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import InventoryEntryDeletedMessagePayloadSchema

        return InventoryEntryDeletedMessagePayloadSchema().dump(self)


class InventoryEntryQuantitySetMessagePayload(MessagePayload):
    old_quantity_on_stock: "int"
    new_quantity_on_stock: "int"
    old_available_quantity: "int"
    new_available_quantity: "int"

    def __init__(
        self,
        *,
        old_quantity_on_stock: "int",
        new_quantity_on_stock: "int",
        old_available_quantity: "int",
        new_available_quantity: "int"
    ):
        self.old_quantity_on_stock = old_quantity_on_stock
        self.new_quantity_on_stock = new_quantity_on_stock
        self.old_available_quantity = old_available_quantity
        self.new_available_quantity = new_available_quantity
        super().__init__(type="InventoryEntryQuantitySet")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InventoryEntryQuantitySetMessagePayload":
        from ._schemas.message import InventoryEntryQuantitySetMessagePayloadSchema

        return InventoryEntryQuantitySetMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import InventoryEntryQuantitySetMessagePayloadSchema

        return InventoryEntryQuantitySetMessagePayloadSchema().dump(self)


class LineItemStateTransitionMessagePayload(MessagePayload):
    line_item_id: "str"
    transition_date: "datetime.datetime"
    quantity: "int"
    from_state: "StateReference"
    to_state: "StateReference"

    def __init__(
        self,
        *,
        line_item_id: "str",
        transition_date: "datetime.datetime",
        quantity: "int",
        from_state: "StateReference",
        to_state: "StateReference"
    ):
        self.line_item_id = line_item_id
        self.transition_date = transition_date
        self.quantity = quantity
        self.from_state = from_state
        self.to_state = to_state
        super().__init__(type="LineItemStateTransition")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "LineItemStateTransitionMessagePayload":
        from ._schemas.message import LineItemStateTransitionMessagePayloadSchema

        return LineItemStateTransitionMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import LineItemStateTransitionMessagePayloadSchema

        return LineItemStateTransitionMessagePayloadSchema().dump(self)


class OrderBillingAddressSetMessagePayload(MessagePayload):
    address: typing.Optional["Address"]
    old_address: typing.Optional["Address"]

    def __init__(
        self,
        *,
        address: typing.Optional["Address"] = None,
        old_address: typing.Optional["Address"] = None
    ):
        self.address = address
        self.old_address = old_address
        super().__init__(type="OrderBillingAddressSet")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderBillingAddressSetMessagePayload":
        from ._schemas.message import OrderBillingAddressSetMessagePayloadSchema

        return OrderBillingAddressSetMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderBillingAddressSetMessagePayloadSchema

        return OrderBillingAddressSetMessagePayloadSchema().dump(self)


class OrderCreatedMessagePayload(MessagePayload):
    order: "Order"

    def __init__(self, *, order: "Order"):
        self.order = order
        super().__init__(type="OrderCreated")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderCreatedMessagePayload":
        from ._schemas.message import OrderCreatedMessagePayloadSchema

        return OrderCreatedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderCreatedMessagePayloadSchema

        return OrderCreatedMessagePayloadSchema().dump(self)


class OrderCustomLineItemDiscountSetMessagePayload(MessagePayload):
    custom_line_item_id: "str"
    discounted_price_per_quantity: typing.List["DiscountedLineItemPriceForQuantity"]
    taxed_price: typing.Optional["TaxedItemPrice"]

    def __init__(
        self,
        *,
        custom_line_item_id: "str",
        discounted_price_per_quantity: typing.List[
            "DiscountedLineItemPriceForQuantity"
        ],
        taxed_price: typing.Optional["TaxedItemPrice"] = None
    ):
        self.custom_line_item_id = custom_line_item_id
        self.discounted_price_per_quantity = discounted_price_per_quantity
        self.taxed_price = taxed_price
        super().__init__(type="OrderCustomLineItemDiscountSet")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderCustomLineItemDiscountSetMessagePayload":
        from ._schemas.message import OrderCustomLineItemDiscountSetMessagePayloadSchema

        return OrderCustomLineItemDiscountSetMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderCustomLineItemDiscountSetMessagePayloadSchema

        return OrderCustomLineItemDiscountSetMessagePayloadSchema().dump(self)


class OrderCustomerEmailSetMessagePayload(MessagePayload):
    email: typing.Optional["str"]
    old_email: typing.Optional["str"]

    def __init__(
        self,
        *,
        email: typing.Optional["str"] = None,
        old_email: typing.Optional["str"] = None
    ):
        self.email = email
        self.old_email = old_email
        super().__init__(type="OrderCustomerEmailSet")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderCustomerEmailSetMessagePayload":
        from ._schemas.message import OrderCustomerEmailSetMessagePayloadSchema

        return OrderCustomerEmailSetMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderCustomerEmailSetMessagePayloadSchema

        return OrderCustomerEmailSetMessagePayloadSchema().dump(self)


class OrderCustomerGroupSetMessagePayload(MessagePayload):
    customer_group: typing.Optional["CustomerGroupReference"]
    old_customer_group: typing.Optional["CustomerGroupReference"]

    def __init__(
        self,
        *,
        customer_group: typing.Optional["CustomerGroupReference"] = None,
        old_customer_group: typing.Optional["CustomerGroupReference"] = None
    ):
        self.customer_group = customer_group
        self.old_customer_group = old_customer_group
        super().__init__(type="OrderCustomerGroupSet")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderCustomerGroupSetMessagePayload":
        from ._schemas.message import OrderCustomerGroupSetMessagePayloadSchema

        return OrderCustomerGroupSetMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderCustomerGroupSetMessagePayloadSchema

        return OrderCustomerGroupSetMessagePayloadSchema().dump(self)


class OrderCustomerSetMessagePayload(MessagePayload):
    customer: typing.Optional["CustomerReference"]
    customer_group: typing.Optional["CustomerGroupReference"]
    old_customer: typing.Optional["CustomerReference"]
    old_customer_group: typing.Optional["CustomerGroupReference"]

    def __init__(
        self,
        *,
        customer: typing.Optional["CustomerReference"] = None,
        customer_group: typing.Optional["CustomerGroupReference"] = None,
        old_customer: typing.Optional["CustomerReference"] = None,
        old_customer_group: typing.Optional["CustomerGroupReference"] = None
    ):
        self.customer = customer
        self.customer_group = customer_group
        self.old_customer = old_customer
        self.old_customer_group = old_customer_group
        super().__init__(type="OrderCustomerSet")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderCustomerSetMessagePayload":
        from ._schemas.message import OrderCustomerSetMessagePayloadSchema

        return OrderCustomerSetMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderCustomerSetMessagePayloadSchema

        return OrderCustomerSetMessagePayloadSchema().dump(self)


class OrderDeletedMessagePayload(MessagePayload):
    order: "Order"

    def __init__(self, *, order: "Order"):
        self.order = order
        super().__init__(type="OrderDeleted")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderDeletedMessagePayload":
        from ._schemas.message import OrderDeletedMessagePayloadSchema

        return OrderDeletedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderDeletedMessagePayloadSchema

        return OrderDeletedMessagePayloadSchema().dump(self)


class OrderDiscountCodeAddedMessagePayload(MessagePayload):
    discount_code: "DiscountCodeReference"

    def __init__(self, *, discount_code: "DiscountCodeReference"):
        self.discount_code = discount_code
        super().__init__(type="OrderDiscountCodeAdded")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderDiscountCodeAddedMessagePayload":
        from ._schemas.message import OrderDiscountCodeAddedMessagePayloadSchema

        return OrderDiscountCodeAddedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderDiscountCodeAddedMessagePayloadSchema

        return OrderDiscountCodeAddedMessagePayloadSchema().dump(self)


class OrderDiscountCodeRemovedMessagePayload(MessagePayload):
    discount_code: "DiscountCodeReference"

    def __init__(self, *, discount_code: "DiscountCodeReference"):
        self.discount_code = discount_code
        super().__init__(type="OrderDiscountCodeRemoved")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderDiscountCodeRemovedMessagePayload":
        from ._schemas.message import OrderDiscountCodeRemovedMessagePayloadSchema

        return OrderDiscountCodeRemovedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderDiscountCodeRemovedMessagePayloadSchema

        return OrderDiscountCodeRemovedMessagePayloadSchema().dump(self)


class OrderDiscountCodeStateSetMessagePayload(MessagePayload):
    discount_code: "DiscountCodeReference"
    state: "DiscountCodeState"
    old_state: typing.Optional["DiscountCodeState"]

    def __init__(
        self,
        *,
        discount_code: "DiscountCodeReference",
        state: "DiscountCodeState",
        old_state: typing.Optional["DiscountCodeState"] = None
    ):
        self.discount_code = discount_code
        self.state = state
        self.old_state = old_state
        super().__init__(type="OrderDiscountCodeStateSet")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderDiscountCodeStateSetMessagePayload":
        from ._schemas.message import OrderDiscountCodeStateSetMessagePayloadSchema

        return OrderDiscountCodeStateSetMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderDiscountCodeStateSetMessagePayloadSchema

        return OrderDiscountCodeStateSetMessagePayloadSchema().dump(self)


class OrderEditAppliedMessagePayload(MessagePayload):
    edit: "OrderEditReference"
    result: "OrderEditApplied"

    def __init__(self, *, edit: "OrderEditReference", result: "OrderEditApplied"):
        self.edit = edit
        self.result = result
        super().__init__(type="OrderEditApplied")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderEditAppliedMessagePayload":
        from ._schemas.message import OrderEditAppliedMessagePayloadSchema

        return OrderEditAppliedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderEditAppliedMessagePayloadSchema

        return OrderEditAppliedMessagePayloadSchema().dump(self)


class OrderImportedMessagePayload(MessagePayload):
    order: "Order"

    def __init__(self, *, order: "Order"):
        self.order = order
        super().__init__(type="OrderImported")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderImportedMessagePayload":
        from ._schemas.message import OrderImportedMessagePayloadSchema

        return OrderImportedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderImportedMessagePayloadSchema

        return OrderImportedMessagePayloadSchema().dump(self)


class OrderLineItemAddedMessagePayload(MessagePayload):
    line_item: "LineItem"
    added_quantity: "int"

    def __init__(self, *, line_item: "LineItem", added_quantity: "int"):
        self.line_item = line_item
        self.added_quantity = added_quantity
        super().__init__(type="OrderLineItemAdded")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderLineItemAddedMessagePayload":
        from ._schemas.message import OrderLineItemAddedMessagePayloadSchema

        return OrderLineItemAddedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderLineItemAddedMessagePayloadSchema

        return OrderLineItemAddedMessagePayloadSchema().dump(self)


class OrderLineItemDiscountSetMessagePayload(MessagePayload):
    line_item_id: "str"
    discounted_price_per_quantity: typing.List["DiscountedLineItemPriceForQuantity"]
    total_price: "Money"
    taxed_price: typing.Optional["TaxedItemPrice"]

    def __init__(
        self,
        *,
        line_item_id: "str",
        discounted_price_per_quantity: typing.List[
            "DiscountedLineItemPriceForQuantity"
        ],
        total_price: "Money",
        taxed_price: typing.Optional["TaxedItemPrice"] = None
    ):
        self.line_item_id = line_item_id
        self.discounted_price_per_quantity = discounted_price_per_quantity
        self.total_price = total_price
        self.taxed_price = taxed_price
        super().__init__(type="OrderLineItemDiscountSet")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderLineItemDiscountSetMessagePayload":
        from ._schemas.message import OrderLineItemDiscountSetMessagePayloadSchema

        return OrderLineItemDiscountSetMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderLineItemDiscountSetMessagePayloadSchema

        return OrderLineItemDiscountSetMessagePayloadSchema().dump(self)


class OrderPaymentStateChangedMessagePayload(MessagePayload):
    payment_state: "PaymentState"
    old_payment_state: typing.Optional["PaymentState"]

    def __init__(
        self,
        *,
        payment_state: "PaymentState",
        old_payment_state: typing.Optional["PaymentState"] = None
    ):
        self.payment_state = payment_state
        self.old_payment_state = old_payment_state
        super().__init__(type="OrderPaymentStateChanged")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderPaymentStateChangedMessagePayload":
        from ._schemas.message import OrderPaymentStateChangedMessagePayloadSchema

        return OrderPaymentStateChangedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderPaymentStateChangedMessagePayloadSchema

        return OrderPaymentStateChangedMessagePayloadSchema().dump(self)


class OrderReturnInfoAddedMessagePayload(MessagePayload):
    return_info: "ReturnInfo"

    def __init__(self, *, return_info: "ReturnInfo"):
        self.return_info = return_info
        super().__init__(type="ReturnInfoAdded")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderReturnInfoAddedMessagePayload":
        from ._schemas.message import OrderReturnInfoAddedMessagePayloadSchema

        return OrderReturnInfoAddedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderReturnInfoAddedMessagePayloadSchema

        return OrderReturnInfoAddedMessagePayloadSchema().dump(self)


class OrderReturnShipmentStateChangedMessagePayload(MessagePayload):
    return_item_id: "str"
    return_shipment_state: "ReturnShipmentState"

    def __init__(
        self, *, return_item_id: "str", return_shipment_state: "ReturnShipmentState"
    ):
        self.return_item_id = return_item_id
        self.return_shipment_state = return_shipment_state
        super().__init__(type="OrderReturnShipmentStateChanged")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderReturnShipmentStateChangedMessagePayload":
        from ._schemas.message import (
            OrderReturnShipmentStateChangedMessagePayloadSchema,
        )

        return OrderReturnShipmentStateChangedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import (
            OrderReturnShipmentStateChangedMessagePayloadSchema,
        )

        return OrderReturnShipmentStateChangedMessagePayloadSchema().dump(self)


class OrderShipmentStateChangedMessagePayload(MessagePayload):
    shipment_state: "ShipmentState"
    old_shipment_state: typing.Optional["ShipmentState"]

    def __init__(
        self,
        *,
        shipment_state: "ShipmentState",
        old_shipment_state: typing.Optional["ShipmentState"] = None
    ):
        self.shipment_state = shipment_state
        self.old_shipment_state = old_shipment_state
        super().__init__(type="OrderShipmentStateChanged")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderShipmentStateChangedMessagePayload":
        from ._schemas.message import OrderShipmentStateChangedMessagePayloadSchema

        return OrderShipmentStateChangedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderShipmentStateChangedMessagePayloadSchema

        return OrderShipmentStateChangedMessagePayloadSchema().dump(self)


class OrderShippingAddressSetMessagePayload(MessagePayload):
    address: typing.Optional["Address"]
    old_address: typing.Optional["Address"]

    def __init__(
        self,
        *,
        address: typing.Optional["Address"] = None,
        old_address: typing.Optional["Address"] = None
    ):
        self.address = address
        self.old_address = old_address
        super().__init__(type="OrderShippingAddressSet")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderShippingAddressSetMessagePayload":
        from ._schemas.message import OrderShippingAddressSetMessagePayloadSchema

        return OrderShippingAddressSetMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderShippingAddressSetMessagePayloadSchema

        return OrderShippingAddressSetMessagePayloadSchema().dump(self)


class OrderShippingInfoSetMessagePayload(MessagePayload):
    shipping_info: typing.Optional["ShippingInfo"]
    old_shipping_info: typing.Optional["ShippingInfo"]

    def __init__(
        self,
        *,
        shipping_info: typing.Optional["ShippingInfo"] = None,
        old_shipping_info: typing.Optional["ShippingInfo"] = None
    ):
        self.shipping_info = shipping_info
        self.old_shipping_info = old_shipping_info
        super().__init__(type="OrderShippingInfoSet")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderShippingInfoSetMessagePayload":
        from ._schemas.message import OrderShippingInfoSetMessagePayloadSchema

        return OrderShippingInfoSetMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderShippingInfoSetMessagePayloadSchema

        return OrderShippingInfoSetMessagePayloadSchema().dump(self)


class OrderShippingRateInputSetMessagePayload(MessagePayload):
    shipping_rate_input: typing.Optional["ShippingRateInput"]
    old_shipping_rate_input: typing.Optional["ShippingRateInput"]

    def __init__(
        self,
        *,
        shipping_rate_input: typing.Optional["ShippingRateInput"] = None,
        old_shipping_rate_input: typing.Optional["ShippingRateInput"] = None
    ):
        self.shipping_rate_input = shipping_rate_input
        self.old_shipping_rate_input = old_shipping_rate_input
        super().__init__(type="OrderShippingRateInputSet")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderShippingRateInputSetMessagePayload":
        from ._schemas.message import OrderShippingRateInputSetMessagePayloadSchema

        return OrderShippingRateInputSetMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderShippingRateInputSetMessagePayloadSchema

        return OrderShippingRateInputSetMessagePayloadSchema().dump(self)


class OrderStateChangedMessagePayload(MessagePayload):
    order_state: "OrderState"
    old_order_state: "OrderState"

    def __init__(self, *, order_state: "OrderState", old_order_state: "OrderState"):
        self.order_state = order_state
        self.old_order_state = old_order_state
        super().__init__(type="OrderStateChanged")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderStateChangedMessagePayload":
        from ._schemas.message import OrderStateChangedMessagePayloadSchema

        return OrderStateChangedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderStateChangedMessagePayloadSchema

        return OrderStateChangedMessagePayloadSchema().dump(self)


class OrderStateTransitionMessagePayload(MessagePayload):
    state: "StateReference"
    force: "bool"

    def __init__(self, *, state: "StateReference", force: "bool"):
        self.state = state
        self.force = force
        super().__init__(type="OrderStateTransition")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderStateTransitionMessagePayload":
        from ._schemas.message import OrderStateTransitionMessagePayloadSchema

        return OrderStateTransitionMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderStateTransitionMessagePayloadSchema

        return OrderStateTransitionMessagePayloadSchema().dump(self)


class OrderStoreSetMessagePayload(MessagePayload):
    store: "StoreKeyReference"

    def __init__(self, *, store: "StoreKeyReference"):
        self.store = store
        super().__init__(type="OrderStoreSet")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderStoreSetMessagePayload":
        from ._schemas.message import OrderStoreSetMessagePayloadSchema

        return OrderStoreSetMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import OrderStoreSetMessagePayloadSchema

        return OrderStoreSetMessagePayloadSchema().dump(self)


class ParcelAddedToDeliveryMessagePayload(MessagePayload):
    delivery: "Delivery"
    parcel: "Parcel"

    def __init__(self, *, delivery: "Delivery", parcel: "Parcel"):
        self.delivery = delivery
        self.parcel = parcel
        super().__init__(type="ParcelAddedToDelivery")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ParcelAddedToDeliveryMessagePayload":
        from ._schemas.message import ParcelAddedToDeliveryMessagePayloadSchema

        return ParcelAddedToDeliveryMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ParcelAddedToDeliveryMessagePayloadSchema

        return ParcelAddedToDeliveryMessagePayloadSchema().dump(self)


class ParcelItemsUpdatedMessagePayload(MessagePayload):
    parcel_id: "str"
    delivery_id: typing.Optional["str"]
    items: typing.List["DeliveryItem"]
    old_items: typing.List["DeliveryItem"]

    def __init__(
        self,
        *,
        parcel_id: "str",
        delivery_id: typing.Optional["str"] = None,
        items: typing.List["DeliveryItem"],
        old_items: typing.List["DeliveryItem"]
    ):
        self.parcel_id = parcel_id
        self.delivery_id = delivery_id
        self.items = items
        self.old_items = old_items
        super().__init__(type="ParcelItemsUpdated")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ParcelItemsUpdatedMessagePayload":
        from ._schemas.message import ParcelItemsUpdatedMessagePayloadSchema

        return ParcelItemsUpdatedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ParcelItemsUpdatedMessagePayloadSchema

        return ParcelItemsUpdatedMessagePayloadSchema().dump(self)


class ParcelMeasurementsUpdatedMessagePayload(MessagePayload):
    delivery_id: "str"
    parcel_id: "str"
    measurements: typing.Optional["ParcelMeasurements"]

    def __init__(
        self,
        *,
        delivery_id: "str",
        parcel_id: "str",
        measurements: typing.Optional["ParcelMeasurements"] = None
    ):
        self.delivery_id = delivery_id
        self.parcel_id = parcel_id
        self.measurements = measurements
        super().__init__(type="ParcelMeasurementsUpdated")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ParcelMeasurementsUpdatedMessagePayload":
        from ._schemas.message import ParcelMeasurementsUpdatedMessagePayloadSchema

        return ParcelMeasurementsUpdatedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ParcelMeasurementsUpdatedMessagePayloadSchema

        return ParcelMeasurementsUpdatedMessagePayloadSchema().dump(self)


class ParcelRemovedFromDeliveryMessagePayload(MessagePayload):
    delivery_id: "str"
    parcel: "Parcel"

    def __init__(self, *, delivery_id: "str", parcel: "Parcel"):
        self.delivery_id = delivery_id
        self.parcel = parcel
        super().__init__(type="ParcelRemovedFromDelivery")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ParcelRemovedFromDeliveryMessagePayload":
        from ._schemas.message import ParcelRemovedFromDeliveryMessagePayloadSchema

        return ParcelRemovedFromDeliveryMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ParcelRemovedFromDeliveryMessagePayloadSchema

        return ParcelRemovedFromDeliveryMessagePayloadSchema().dump(self)


class ParcelTrackingDataUpdatedMessagePayload(MessagePayload):
    delivery_id: "str"
    parcel_id: "str"
    tracking_data: typing.Optional["TrackingData"]

    def __init__(
        self,
        *,
        delivery_id: "str",
        parcel_id: "str",
        tracking_data: typing.Optional["TrackingData"] = None
    ):
        self.delivery_id = delivery_id
        self.parcel_id = parcel_id
        self.tracking_data = tracking_data
        super().__init__(type="ParcelTrackingDataUpdated")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ParcelTrackingDataUpdatedMessagePayload":
        from ._schemas.message import ParcelTrackingDataUpdatedMessagePayloadSchema

        return ParcelTrackingDataUpdatedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ParcelTrackingDataUpdatedMessagePayloadSchema

        return ParcelTrackingDataUpdatedMessagePayloadSchema().dump(self)


class PaymentCreatedMessagePayload(MessagePayload):
    payment: "Payment"

    def __init__(self, *, payment: "Payment"):
        self.payment = payment
        super().__init__(type="PaymentCreated")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentCreatedMessagePayload":
        from ._schemas.message import PaymentCreatedMessagePayloadSchema

        return PaymentCreatedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import PaymentCreatedMessagePayloadSchema

        return PaymentCreatedMessagePayloadSchema().dump(self)


class PaymentInteractionAddedMessagePayload(MessagePayload):
    interaction: "CustomFields"

    def __init__(self, *, interaction: "CustomFields"):
        self.interaction = interaction
        super().__init__(type="PaymentInteractionAdded")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentInteractionAddedMessagePayload":
        from ._schemas.message import PaymentInteractionAddedMessagePayloadSchema

        return PaymentInteractionAddedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import PaymentInteractionAddedMessagePayloadSchema

        return PaymentInteractionAddedMessagePayloadSchema().dump(self)


class PaymentStatusInterfaceCodeSetMessagePayload(MessagePayload):
    payment_id: "str"
    interface_code: "str"

    def __init__(self, *, payment_id: "str", interface_code: "str"):
        self.payment_id = payment_id
        self.interface_code = interface_code
        super().__init__(type="PaymentStatusInterfaceCodeSet")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentStatusInterfaceCodeSetMessagePayload":
        from ._schemas.message import PaymentStatusInterfaceCodeSetMessagePayloadSchema

        return PaymentStatusInterfaceCodeSetMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import PaymentStatusInterfaceCodeSetMessagePayloadSchema

        return PaymentStatusInterfaceCodeSetMessagePayloadSchema().dump(self)


class PaymentStatusStateTransitionMessagePayload(MessagePayload):
    state: "StateReference"
    force: "bool"

    def __init__(self, *, state: "StateReference", force: "bool"):
        self.state = state
        self.force = force
        super().__init__(type="PaymentStatusStateTransition")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentStatusStateTransitionMessagePayload":
        from ._schemas.message import PaymentStatusStateTransitionMessagePayloadSchema

        return PaymentStatusStateTransitionMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import PaymentStatusStateTransitionMessagePayloadSchema

        return PaymentStatusStateTransitionMessagePayloadSchema().dump(self)


class PaymentTransactionAddedMessagePayload(MessagePayload):
    transaction: "Transaction"

    def __init__(self, *, transaction: "Transaction"):
        self.transaction = transaction
        super().__init__(type="PaymentTransactionAdded")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentTransactionAddedMessagePayload":
        from ._schemas.message import PaymentTransactionAddedMessagePayloadSchema

        return PaymentTransactionAddedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import PaymentTransactionAddedMessagePayloadSchema

        return PaymentTransactionAddedMessagePayloadSchema().dump(self)


class PaymentTransactionStateChangedMessagePayload(MessagePayload):
    transaction_id: "str"
    state: "TransactionState"

    def __init__(self, *, transaction_id: "str", state: "TransactionState"):
        self.transaction_id = transaction_id
        self.state = state
        super().__init__(type="PaymentTransactionStateChanged")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentTransactionStateChangedMessagePayload":
        from ._schemas.message import PaymentTransactionStateChangedMessagePayloadSchema

        return PaymentTransactionStateChangedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import PaymentTransactionStateChangedMessagePayloadSchema

        return PaymentTransactionStateChangedMessagePayloadSchema().dump(self)


class ProductAddedToCategoryMessagePayload(MessagePayload):
    category: "CategoryReference"
    staged: "bool"

    def __init__(self, *, category: "CategoryReference", staged: "bool"):
        self.category = category
        self.staged = staged
        super().__init__(type="ProductAddedToCategory")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductAddedToCategoryMessagePayload":
        from ._schemas.message import ProductAddedToCategoryMessagePayloadSchema

        return ProductAddedToCategoryMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ProductAddedToCategoryMessagePayloadSchema

        return ProductAddedToCategoryMessagePayloadSchema().dump(self)


class ProductCreatedMessagePayload(MessagePayload):
    product_projection: "ProductProjection"

    def __init__(self, *, product_projection: "ProductProjection"):
        self.product_projection = product_projection
        super().__init__(type="ProductCreated")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductCreatedMessagePayload":
        from ._schemas.message import ProductCreatedMessagePayloadSchema

        return ProductCreatedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ProductCreatedMessagePayloadSchema

        return ProductCreatedMessagePayloadSchema().dump(self)


class ProductDeletedMessagePayload(MessagePayload):
    removed_image_urls: typing.List["str"]
    current_projection: "ProductProjection"

    def __init__(
        self,
        *,
        removed_image_urls: typing.List["str"],
        current_projection: "ProductProjection"
    ):
        self.removed_image_urls = removed_image_urls
        self.current_projection = current_projection
        super().__init__(type="ProductDeleted")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductDeletedMessagePayload":
        from ._schemas.message import ProductDeletedMessagePayloadSchema

        return ProductDeletedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ProductDeletedMessagePayloadSchema

        return ProductDeletedMessagePayloadSchema().dump(self)


class ProductImageAddedMessagePayload(MessagePayload):
    variant_id: "int"
    image: "Image"
    staged: "bool"

    def __init__(self, *, variant_id: "int", image: "Image", staged: "bool"):
        self.variant_id = variant_id
        self.image = image
        self.staged = staged
        super().__init__(type="ProductImageAdded")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductImageAddedMessagePayload":
        from ._schemas.message import ProductImageAddedMessagePayloadSchema

        return ProductImageAddedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ProductImageAddedMessagePayloadSchema

        return ProductImageAddedMessagePayloadSchema().dump(self)


class ProductPriceDiscountsSetMessagePayload(MessagePayload):
    updated_prices: typing.List["ProductPriceDiscountsSetUpdatedPrice"]

    def __init__(
        self, *, updated_prices: typing.List["ProductPriceDiscountsSetUpdatedPrice"]
    ):
        self.updated_prices = updated_prices
        super().__init__(type="ProductPriceDiscountsSet")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductPriceDiscountsSetMessagePayload":
        from ._schemas.message import ProductPriceDiscountsSetMessagePayloadSchema

        return ProductPriceDiscountsSetMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ProductPriceDiscountsSetMessagePayloadSchema

        return ProductPriceDiscountsSetMessagePayloadSchema().dump(self)


class ProductPriceExternalDiscountSetMessagePayload(MessagePayload):
    variant_id: "int"
    variant_key: typing.Optional["str"]
    sku: typing.Optional["str"]
    price_id: "str"
    discounted: typing.Optional["DiscountedPrice"]
    staged: "bool"

    def __init__(
        self,
        *,
        variant_id: "int",
        variant_key: typing.Optional["str"] = None,
        sku: typing.Optional["str"] = None,
        price_id: "str",
        discounted: typing.Optional["DiscountedPrice"] = None,
        staged: "bool"
    ):
        self.variant_id = variant_id
        self.variant_key = variant_key
        self.sku = sku
        self.price_id = price_id
        self.discounted = discounted
        self.staged = staged
        super().__init__(type="ProductPriceExternalDiscountSet")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductPriceExternalDiscountSetMessagePayload":
        from ._schemas.message import (
            ProductPriceExternalDiscountSetMessagePayloadSchema,
        )

        return ProductPriceExternalDiscountSetMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import (
            ProductPriceExternalDiscountSetMessagePayloadSchema,
        )

        return ProductPriceExternalDiscountSetMessagePayloadSchema().dump(self)


class ProductPublishedMessagePayload(MessagePayload):
    removed_image_urls: typing.List["str"]
    product_projection: "ProductProjection"
    scope: "ProductPublishScope"

    def __init__(
        self,
        *,
        removed_image_urls: typing.List["str"],
        product_projection: "ProductProjection",
        scope: "ProductPublishScope"
    ):
        self.removed_image_urls = removed_image_urls
        self.product_projection = product_projection
        self.scope = scope
        super().__init__(type="ProductPublished")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductPublishedMessagePayload":
        from ._schemas.message import ProductPublishedMessagePayloadSchema

        return ProductPublishedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ProductPublishedMessagePayloadSchema

        return ProductPublishedMessagePayloadSchema().dump(self)


class ProductRemovedFromCategoryMessagePayload(MessagePayload):
    category: "CategoryReference"
    staged: "bool"

    def __init__(self, *, category: "CategoryReference", staged: "bool"):
        self.category = category
        self.staged = staged
        super().__init__(type="ProductRemovedFromCategory")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductRemovedFromCategoryMessagePayload":
        from ._schemas.message import ProductRemovedFromCategoryMessagePayloadSchema

        return ProductRemovedFromCategoryMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ProductRemovedFromCategoryMessagePayloadSchema

        return ProductRemovedFromCategoryMessagePayloadSchema().dump(self)


class ProductRevertedStagedChangesMessagePayload(MessagePayload):
    removed_image_urls: typing.List["str"]

    def __init__(self, *, removed_image_urls: typing.List["str"]):
        self.removed_image_urls = removed_image_urls
        super().__init__(type="ProductRevertedStagedChanges")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductRevertedStagedChangesMessagePayload":
        from ._schemas.message import ProductRevertedStagedChangesMessagePayloadSchema

        return ProductRevertedStagedChangesMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ProductRevertedStagedChangesMessagePayloadSchema

        return ProductRevertedStagedChangesMessagePayloadSchema().dump(self)


class ProductSlugChangedMessagePayload(MessagePayload):
    slug: "LocalizedString"

    def __init__(self, *, slug: "LocalizedString"):
        self.slug = slug
        super().__init__(type="ProductSlugChanged")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSlugChangedMessagePayload":
        from ._schemas.message import ProductSlugChangedMessagePayloadSchema

        return ProductSlugChangedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ProductSlugChangedMessagePayloadSchema

        return ProductSlugChangedMessagePayloadSchema().dump(self)


class ProductStateTransitionMessagePayload(MessagePayload):
    state: "StateReference"
    force: "bool"

    def __init__(self, *, state: "StateReference", force: "bool"):
        self.state = state
        self.force = force
        super().__init__(type="ProductStateTransition")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductStateTransitionMessagePayload":
        from ._schemas.message import ProductStateTransitionMessagePayloadSchema

        return ProductStateTransitionMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ProductStateTransitionMessagePayloadSchema

        return ProductStateTransitionMessagePayloadSchema().dump(self)


class ProductUnpublishedMessagePayload(MessagePayload):
    def __init__(self):

        super().__init__(type="ProductUnpublished")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductUnpublishedMessagePayload":
        from ._schemas.message import ProductUnpublishedMessagePayloadSchema

        return ProductUnpublishedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ProductUnpublishedMessagePayloadSchema

        return ProductUnpublishedMessagePayloadSchema().dump(self)


class ProductVariantAddedMessagePayload(MessagePayload):
    variant: "ProductVariant"
    staged: "bool"

    def __init__(self, *, variant: "ProductVariant", staged: "bool"):
        self.variant = variant
        self.staged = staged
        super().__init__(type="ProductVariantAdded")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductVariantAddedMessagePayload":
        from ._schemas.message import ProductVariantAddedMessagePayloadSchema

        return ProductVariantAddedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ProductVariantAddedMessagePayloadSchema

        return ProductVariantAddedMessagePayloadSchema().dump(self)


class ProductVariantDeletedMessagePayload(MessagePayload):
    variant: "ProductVariant"
    removed_image_urls: typing.List["str"]

    def __init__(
        self, *, variant: "ProductVariant", removed_image_urls: typing.List["str"]
    ):
        self.variant = variant
        self.removed_image_urls = removed_image_urls
        super().__init__(type="ProductVariantDeleted")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductVariantDeletedMessagePayload":
        from ._schemas.message import ProductVariantDeletedMessagePayloadSchema

        return ProductVariantDeletedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ProductVariantDeletedMessagePayloadSchema

        return ProductVariantDeletedMessagePayloadSchema().dump(self)


class ReviewCreatedMessagePayload(MessagePayload):
    review: "Review"

    def __init__(self, *, review: "Review"):
        self.review = review
        super().__init__(type="ReviewCreated")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ReviewCreatedMessagePayload":
        from ._schemas.message import ReviewCreatedMessagePayloadSchema

        return ReviewCreatedMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ReviewCreatedMessagePayloadSchema

        return ReviewCreatedMessagePayloadSchema().dump(self)


class ReviewRatingSetMessagePayload(MessagePayload):
    old_rating: typing.Optional["float"]
    new_rating: typing.Optional["float"]
    included_in_statistics: "bool"
    target: typing.Optional["Reference"]

    def __init__(
        self,
        *,
        old_rating: typing.Optional["float"] = None,
        new_rating: typing.Optional["float"] = None,
        included_in_statistics: "bool",
        target: typing.Optional["Reference"] = None
    ):
        self.old_rating = old_rating
        self.new_rating = new_rating
        self.included_in_statistics = included_in_statistics
        self.target = target
        super().__init__(type="ReviewRatingSet")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ReviewRatingSetMessagePayload":
        from ._schemas.message import ReviewRatingSetMessagePayloadSchema

        return ReviewRatingSetMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ReviewRatingSetMessagePayloadSchema

        return ReviewRatingSetMessagePayloadSchema().dump(self)


class ReviewStateTransitionMessagePayload(MessagePayload):
    old_state: "StateReference"
    new_state: "StateReference"
    old_included_in_statistics: "bool"
    new_included_in_statistics: "bool"
    target: "Reference"
    force: "bool"

    def __init__(
        self,
        *,
        old_state: "StateReference",
        new_state: "StateReference",
        old_included_in_statistics: "bool",
        new_included_in_statistics: "bool",
        target: "Reference",
        force: "bool"
    ):
        self.old_state = old_state
        self.new_state = new_state
        self.old_included_in_statistics = old_included_in_statistics
        self.new_included_in_statistics = new_included_in_statistics
        self.target = target
        self.force = force
        super().__init__(type="ReviewStateTransition")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ReviewStateTransitionMessagePayload":
        from ._schemas.message import ReviewStateTransitionMessagePayloadSchema

        return ReviewStateTransitionMessagePayloadSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.message import ReviewStateTransitionMessagePayloadSchema

        return ReviewStateTransitionMessagePayloadSchema().dump(self)
