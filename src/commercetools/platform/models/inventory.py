# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import BaseResource, Reference, ReferenceTypeId, ResourceIdentifier

if typing.TYPE_CHECKING:
    from .channel import ChannelResourceIdentifier
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
    "InventoryEntrySetRestockableInDaysAction",
    "InventoryEntrySetSupplyChannelAction",
    "InventoryEntryUpdate",
    "InventoryEntryUpdateAction",
    "InventoryPagedQueryResponse",
]


class InventoryEntry(BaseResource):
    #: Present on resources updated after 1/02/2019 except for events not tracked.
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Present on resources created after 1/02/2019 except for events not tracked.
    created_by: typing.Optional["CreatedBy"]
    sku: str
    #: Optional connection to a particular supplier.
    supply_channel: typing.Optional["ChannelResourceIdentifier"]
    #: Overall amount of stock.
    #: (available + reserved)
    quantity_on_stock: int
    #: Available amount of stock.
    #: (available means: `quantityOnStock` - reserved quantity)
    available_quantity: int
    #: The time period in days, that tells how often this inventory entry is restocked.
    restockable_in_days: typing.Optional[int]
    #: The date and time of the next restock.
    expected_delivery: typing.Optional[datetime.datetime]
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
        sku: str,
        supply_channel: typing.Optional["ChannelResourceIdentifier"] = None,
        quantity_on_stock: int,
        available_quantity: int,
        restockable_in_days: typing.Optional[int] = None,
        expected_delivery: typing.Optional[datetime.datetime] = None,
        custom: typing.Optional["CustomFields"] = None
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
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
    sku: str
    supply_channel: typing.Optional["ChannelResourceIdentifier"]
    quantity_on_stock: int
    restockable_in_days: typing.Optional[int]
    expected_delivery: typing.Optional[datetime.datetime]
    #: The custom fields.
    custom: typing.Optional["CustomFieldsDraft"]

    def __init__(
        self,
        *,
        sku: str,
        supply_channel: typing.Optional["ChannelResourceIdentifier"] = None,
        quantity_on_stock: int,
        restockable_in_days: typing.Optional[int] = None,
        expected_delivery: typing.Optional[datetime.datetime] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None
    ):
        self.sku = sku
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
    version: int
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
    limit: int
    count: int
    total: typing.Optional[int]
    offset: int
    results: typing.List["InventoryEntry"]

    def __init__(
        self,
        *,
        limit: int,
        count: int,
        total: typing.Optional[int] = None,
        offset: int,
        results: typing.List["InventoryEntry"]
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
    ) -> "InventoryPagedQueryResponse":
        from ._schemas.inventory import InventoryPagedQueryResponseSchema

        return InventoryPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.inventory import InventoryPagedQueryResponseSchema

        return InventoryPagedQueryResponseSchema().dump(self)


class InventoryEntryAddQuantityAction(InventoryEntryUpdateAction):
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
    name: str
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
    #: If absent, the custom type and any existing CustomFields are removed.
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
    ) -> "InventoryEntrySetCustomTypeAction":
        from ._schemas.inventory import InventoryEntrySetCustomTypeActionSchema

        return InventoryEntrySetCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.inventory import InventoryEntrySetCustomTypeActionSchema

        return InventoryEntrySetCustomTypeActionSchema().dump(self)


class InventoryEntrySetExpectedDeliveryAction(InventoryEntryUpdateAction):
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


class InventoryEntrySetRestockableInDaysAction(InventoryEntryUpdateAction):
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
    #: If absent, the supply channel is removed.
    #: This action will fail if an entry with the combination of sku and supplyChannel already exists.
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
