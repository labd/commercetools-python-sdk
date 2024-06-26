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
from .common import BaseResource, Reference, ReferenceTypeId, ResourceIdentifier

if typing.TYPE_CHECKING:
    from .channel import ChannelReference, ChannelResourceIdentifier
    from .common import CreatedBy, LastModifiedBy, ReferenceTypeId
    from .type import (
        CustomFields,
        CustomFieldsDraft,
        FieldContainer,
        TypeResourceIdentifier,
    )

__all__ = [
    "InventoryEntry",
    "InventoryEntryAddQuantityAction",
    "InventoryEntryChangeQuantityAction",
    "InventoryEntryDraft",
    "InventoryEntryReference",
    "InventoryEntryRemoveQuantityAction",
    "InventoryEntryResourceIdentifier",
    "InventoryEntrySetCustomFieldAction",
    "InventoryEntrySetCustomTypeAction",
    "InventoryEntrySetExpectedDeliveryAction",
    "InventoryEntrySetKeyAction",
    "InventoryEntrySetRestockableInDaysAction",
    "InventoryEntrySetSupplyChannelAction",
    "InventoryEntryUpdate",
    "InventoryEntryUpdateAction",
    "InventoryPagedQueryResponse",
]


class InventoryEntry(BaseResource):
    #: IDs and references that last modified the InventoryEntry.
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: IDs and references that created the InventoryEntry.
    created_by: typing.Optional["CreatedBy"]
    #: User-defined unique identifier of the InventoryEntry.
    key: typing.Optional[str]
    #: [ProductVariant](ctp:api:type:ProductVariant) `sku` of the InventoryEntry.
    sku: str
    #: [Channel](ctp:api:type:Channel) that supplies this InventoryEntry.
    supply_channel: typing.Optional["ChannelReference"]
    #: Overall amount of stock (`availableQuantity` + reserved).
    quantity_on_stock: int
    #: Available amount of stock (`quantityOnStock` - reserved).
    available_quantity: int
    #: How often the InventoryEntry is restocked (in days).
    restockable_in_days: typing.Optional[int]
    #: Date and time of the next restock.
    expected_delivery: typing.Optional[datetime.datetime]
    #: Custom Fields of the InventoryEntry.
    custom: typing.Optional["CustomFields"]

    def __init__(
        self,
        *,
        id: str,
        version: int,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        key: typing.Optional[str] = None,
        sku: str,
        supply_channel: typing.Optional["ChannelReference"] = None,
        quantity_on_stock: int,
        available_quantity: int,
        restockable_in_days: typing.Optional[int] = None,
        expected_delivery: typing.Optional[datetime.datetime] = None,
        custom: typing.Optional["CustomFields"] = None
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.key = key
        self.sku = sku
        self.supply_channel = supply_channel
        self.quantity_on_stock = quantity_on_stock
        self.available_quantity = available_quantity
        self.restockable_in_days = restockable_in_days
        self.expected_delivery = expected_delivery
        self.custom = custom

        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "InventoryEntry":
        from ._schemas.inventory import InventoryEntrySchema

        return InventoryEntrySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.inventory import InventoryEntrySchema

        return InventoryEntrySchema().dump(self)


class InventoryEntryDraft(_BaseType):
    #: [ProductVariant](ctp:api:type:ProductVariant) `sku` of the InventoryEntry.
    sku: str
    #: User-defined unique identifier for the InventoryEntry.
    key: typing.Optional[str]
    #: [Channel](ctp:api:type:Channel) that supplies this InventoryEntry.
    supply_channel: typing.Optional["ChannelResourceIdentifier"]
    #: Overall amount of stock.
    quantity_on_stock: int
    #: How often the InventoryEntry is restocked (in days).
    restockable_in_days: typing.Optional[int]
    #: Date and time of the next restock.
    expected_delivery: typing.Optional[datetime.datetime]
    #: Custom Fields of the InventoryEntry.
    custom: typing.Optional["CustomFieldsDraft"]

    def __init__(
        self,
        *,
        sku: str,
        key: typing.Optional[str] = None,
        supply_channel: typing.Optional["ChannelResourceIdentifier"] = None,
        quantity_on_stock: int,
        restockable_in_days: typing.Optional[int] = None,
        expected_delivery: typing.Optional[datetime.datetime] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None
    ):
        self.sku = sku
        self.key = key
        self.supply_channel = supply_channel
        self.quantity_on_stock = quantity_on_stock
        self.restockable_in_days = restockable_in_days
        self.expected_delivery = expected_delivery
        self.custom = custom

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "InventoryEntryDraft":
        from ._schemas.inventory import InventoryEntryDraftSchema

        return InventoryEntryDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.inventory import InventoryEntryDraftSchema

        return InventoryEntryDraftSchema().dump(self)


class InventoryEntryReference(Reference):
    """[Reference](ctp:api:type:Reference) to an [InventoryEntry](ctp:api:type:InventoryEntry)."""

    #: Contains the representation of the expanded InventoryEntry. Only present in responses to requests with [Reference Expansion](/../api/general-concepts#reference-expansion) for InventoryEntries.
    obj: typing.Optional["InventoryEntry"]

    def __init__(self, *, id: str, obj: typing.Optional["InventoryEntry"] = None):
        self.obj = obj

        super().__init__(id=id, type_id=ReferenceTypeId.INVENTORY_ENTRY)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InventoryEntryReference":
        from ._schemas.inventory import InventoryEntryReferenceSchema

        return InventoryEntryReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.inventory import InventoryEntryReferenceSchema

        return InventoryEntryReferenceSchema().dump(self)


class InventoryEntryResourceIdentifier(ResourceIdentifier):
    """[ResourceIdentifier](ctp:api:type:ResourceIdentifier) to an [InventoryEntry](ctp:api:type:InventoryEntry). Either `id` or `key` is required. If both are set, an [InvalidJsonInput](/../api/errors#invalidjsoninput) error is returned."""

    def __init__(
        self, *, id: typing.Optional[str] = None, key: typing.Optional[str] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.INVENTORY_ENTRY)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InventoryEntryResourceIdentifier":
        from ._schemas.inventory import InventoryEntryResourceIdentifierSchema

        return InventoryEntryResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.inventory import InventoryEntryResourceIdentifierSchema

        return InventoryEntryResourceIdentifierSchema().dump(self)


class InventoryEntryUpdate(_BaseType):
    #: Expected version of the InventoryEntry on which the changes should be applied.
    #: If the expected version does not match the actual version, a [ConcurrentModification](ctp:api:type:ConcurrentModificationError) error will be returned.
    version: int
    #: Update actions to be performed on the InventoryEntry.
    actions: typing.List["InventoryEntryUpdateAction"]

    def __init__(
        self, *, version: int, actions: typing.List["InventoryEntryUpdateAction"]
    ):
        self.version = version
        self.actions = actions

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "InventoryEntryUpdate":
        from ._schemas.inventory import InventoryEntryUpdateSchema

        return InventoryEntryUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.inventory import InventoryEntryUpdateSchema

        return InventoryEntryUpdateSchema().dump(self)


class InventoryEntryUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InventoryEntryUpdateAction":
        if data["action"] == "addQuantity":
            from ._schemas.inventory import InventoryEntryAddQuantityActionSchema

            return InventoryEntryAddQuantityActionSchema().load(data)
        if data["action"] == "changeQuantity":
            from ._schemas.inventory import InventoryEntryChangeQuantityActionSchema

            return InventoryEntryChangeQuantityActionSchema().load(data)
        if data["action"] == "removeQuantity":
            from ._schemas.inventory import InventoryEntryRemoveQuantityActionSchema

            return InventoryEntryRemoveQuantityActionSchema().load(data)
        if data["action"] == "setCustomField":
            from ._schemas.inventory import InventoryEntrySetCustomFieldActionSchema

            return InventoryEntrySetCustomFieldActionSchema().load(data)
        if data["action"] == "setCustomType":
            from ._schemas.inventory import InventoryEntrySetCustomTypeActionSchema

            return InventoryEntrySetCustomTypeActionSchema().load(data)
        if data["action"] == "setExpectedDelivery":
            from ._schemas.inventory import (
                InventoryEntrySetExpectedDeliveryActionSchema,
            )

            return InventoryEntrySetExpectedDeliveryActionSchema().load(data)
        if data["action"] == "setKey":
            from ._schemas.inventory import InventoryEntrySetKeyActionSchema

            return InventoryEntrySetKeyActionSchema().load(data)
        if data["action"] == "setRestockableInDays":
            from ._schemas.inventory import (
                InventoryEntrySetRestockableInDaysActionSchema,
            )

            return InventoryEntrySetRestockableInDaysActionSchema().load(data)
        if data["action"] == "setSupplyChannel":
            from ._schemas.inventory import InventoryEntrySetSupplyChannelActionSchema

            return InventoryEntrySetSupplyChannelActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.inventory import InventoryEntryUpdateActionSchema

        return InventoryEntryUpdateActionSchema().dump(self)


class InventoryPagedQueryResponse(_BaseType):
    #: Number of [results requested](/../api/general-concepts#limit).
    limit: int
    #: Number of [elements skipped](/../api/general-concepts#offset).
    offset: int
    #: Actual number of results returned.
    count: int
    #: Total number of results matching the query.
    #: This number is an estimation that is not [strongly consistent](/../api/general-concepts#strong-consistency).
    #: This field is returned by default.
    #: For improved performance, calculating this field can be deactivated by using the query parameter `withTotal=false`.
    #: When the results are filtered with a [Query Predicate](/../api/predicates/query), `total` is subject to a [limit](/../api/limits#queries).
    total: typing.Optional[int]
    #: [Inventory entries](ctp:api:type:InventoryEntry) matching the query.
    results: typing.List["InventoryEntry"]

    def __init__(
        self,
        *,
        limit: int,
        offset: int,
        count: int,
        total: typing.Optional[int] = None,
        results: typing.List["InventoryEntry"]
    ):
        self.limit = limit
        self.offset = offset
        self.count = count
        self.total = total
        self.results = results

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InventoryPagedQueryResponse":
        from ._schemas.inventory import InventoryPagedQueryResponseSchema

        return InventoryPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.inventory import InventoryPagedQueryResponseSchema

        return InventoryPagedQueryResponseSchema().dump(self)


class InventoryEntryAddQuantityAction(InventoryEntryUpdateAction):
    """Updates `availableQuantity` based on the new `quantityOnStock` and amount of active reservations."""

    #: Value to add to `quantityOnStock`.
    quantity: int

    def __init__(self, *, quantity: int):
        self.quantity = quantity

        super().__init__(action="addQuantity")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InventoryEntryAddQuantityAction":
        from ._schemas.inventory import InventoryEntryAddQuantityActionSchema

        return InventoryEntryAddQuantityActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.inventory import InventoryEntryAddQuantityActionSchema

        return InventoryEntryAddQuantityActionSchema().dump(self)


class InventoryEntryChangeQuantityAction(InventoryEntryUpdateAction):
    """Updates `availableQuantity` based on the new `quantityOnStock` and amount of active reservations."""

    #: Value to set for `quantityOnStock`.
    quantity: int

    def __init__(self, *, quantity: int):
        self.quantity = quantity

        super().__init__(action="changeQuantity")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InventoryEntryChangeQuantityAction":
        from ._schemas.inventory import InventoryEntryChangeQuantityActionSchema

        return InventoryEntryChangeQuantityActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.inventory import InventoryEntryChangeQuantityActionSchema

        return InventoryEntryChangeQuantityActionSchema().dump(self)


class InventoryEntryRemoveQuantityAction(InventoryEntryUpdateAction):
    """Updates `availableQuantity` based on the new `quantityOnStock` and amount of active reservations."""

    #: Value to remove from `quantityOnStock`.
    quantity: int

    def __init__(self, *, quantity: int):
        self.quantity = quantity

        super().__init__(action="removeQuantity")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InventoryEntryRemoveQuantityAction":
        from ._schemas.inventory import InventoryEntryRemoveQuantityActionSchema

        return InventoryEntryRemoveQuantityActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.inventory import InventoryEntryRemoveQuantityActionSchema

        return InventoryEntryRemoveQuantityActionSchema().dump(self)


class InventoryEntrySetCustomFieldAction(InventoryEntryUpdateAction):
    #: Name of the [Custom Field](/../api/projects/custom-fields).
    name: str
    #: If `value` is absent or `null`, this field will be removed if it exists.
    #: Removing a field that does not exist returns an [InvalidOperation](ctp:api:type:InvalidOperationError) error.
    #: If `value` is provided, it is set for the field defined by `name`.
    value: typing.Optional[typing.Any]

    def __init__(self, *, name: str, value: typing.Optional[typing.Any] = None):
        self.name = name
        self.value = value

        super().__init__(action="setCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InventoryEntrySetCustomFieldAction":
        from ._schemas.inventory import InventoryEntrySetCustomFieldActionSchema

        return InventoryEntrySetCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.inventory import InventoryEntrySetCustomFieldActionSchema

        return InventoryEntrySetCustomFieldActionSchema().dump(self)


class InventoryEntrySetCustomTypeAction(InventoryEntryUpdateAction):
    #: Defines the [Type](ctp:api:type:Type) that extends the InventoryEntry with [Custom Fields](/../api/projects/custom-fields).
    #: If absent, any existing Type and Custom Fields are removed from the InventoryEntry.
    type: typing.Optional["TypeResourceIdentifier"]
    #: Sets the [Custom Fields](/../api/projects/custom-fields) fields for the InventoryEntry.
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
    ) -> "InventoryEntrySetCustomTypeAction":
        from ._schemas.inventory import InventoryEntrySetCustomTypeActionSchema

        return InventoryEntrySetCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.inventory import InventoryEntrySetCustomTypeActionSchema

        return InventoryEntrySetCustomTypeActionSchema().dump(self)


class InventoryEntrySetExpectedDeliveryAction(InventoryEntryUpdateAction):
    #: Value to set. If empty, any existing value will be removed.
    expected_delivery: typing.Optional[datetime.datetime]

    def __init__(self, *, expected_delivery: typing.Optional[datetime.datetime] = None):
        self.expected_delivery = expected_delivery

        super().__init__(action="setExpectedDelivery")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InventoryEntrySetExpectedDeliveryAction":
        from ._schemas.inventory import InventoryEntrySetExpectedDeliveryActionSchema

        return InventoryEntrySetExpectedDeliveryActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.inventory import InventoryEntrySetExpectedDeliveryActionSchema

        return InventoryEntrySetExpectedDeliveryActionSchema().dump(self)


class InventoryEntrySetKeyAction(InventoryEntryUpdateAction):
    #: Value to set. If empty, any existing value will be removed.
    key: typing.Optional[str]

    def __init__(self, *, key: typing.Optional[str] = None):
        self.key = key

        super().__init__(action="setKey")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InventoryEntrySetKeyAction":
        from ._schemas.inventory import InventoryEntrySetKeyActionSchema

        return InventoryEntrySetKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.inventory import InventoryEntrySetKeyActionSchema

        return InventoryEntrySetKeyActionSchema().dump(self)


class InventoryEntrySetRestockableInDaysAction(InventoryEntryUpdateAction):
    #: Value to set. If empty, any existing value will be removed.
    restockable_in_days: typing.Optional[int]

    def __init__(self, *, restockable_in_days: typing.Optional[int] = None):
        self.restockable_in_days = restockable_in_days

        super().__init__(action="setRestockableInDays")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InventoryEntrySetRestockableInDaysAction":
        from ._schemas.inventory import InventoryEntrySetRestockableInDaysActionSchema

        return InventoryEntrySetRestockableInDaysActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.inventory import InventoryEntrySetRestockableInDaysActionSchema

        return InventoryEntrySetRestockableInDaysActionSchema().dump(self)


class InventoryEntrySetSupplyChannelAction(InventoryEntryUpdateAction):
    """If an entry with the same `sku` and `supplyChannel` already exists, an [DuplicateField](ctp:api:type:DuplicateFieldError) error is returned."""

    #: Value to set. If empty, any existing value will be removed.
    supply_channel: typing.Optional["ChannelResourceIdentifier"]

    def __init__(
        self, *, supply_channel: typing.Optional["ChannelResourceIdentifier"] = None
    ):
        self.supply_channel = supply_channel

        super().__init__(action="setSupplyChannel")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InventoryEntrySetSupplyChannelAction":
        from ._schemas.inventory import InventoryEntrySetSupplyChannelActionSchema

        return InventoryEntrySetSupplyChannelActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.inventory import InventoryEntrySetSupplyChannelActionSchema

        return InventoryEntrySetSupplyChannelActionSchema().dump(self)
