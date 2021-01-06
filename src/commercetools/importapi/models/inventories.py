# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import ImportResource

if typing.TYPE_CHECKING:
    from .common import ChannelKeyReference
    from .customfields import Custom

__all__ = ["InventoryImport"]


class InventoryImport(ImportResource):
    """Import representation for a inventory."""

    sku: str
    #: Maps to `Inventory.quantityOnStock`
    quantity_on_stock: float
    #: Maps to `Inventory.restockableInDays`
    restockable_in_days: typing.Optional[float]
    expected_delivery: typing.Optional[datetime.datetime]
    #: References a channel by its key.
    supply_channel: typing.Optional["ChannelKeyReference"]
    #: Maps to `Inventory.custom`.
    custom: typing.Optional["Custom"]

    def __init__(
        self,
        *,
        key: str,
        sku: str,
        quantity_on_stock: float,
        restockable_in_days: typing.Optional[float] = None,
        expected_delivery: typing.Optional[datetime.datetime] = None,
        supply_channel: typing.Optional["ChannelKeyReference"] = None,
        custom: typing.Optional["Custom"] = None
    ):
        self.sku = sku
        self.quantity_on_stock = quantity_on_stock
        self.restockable_in_days = restockable_in_days
        self.expected_delivery = expected_delivery
        self.supply_channel = supply_channel
        self.custom = custom
        super().__init__(key=key)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "InventoryImport":
        from ._schemas.inventories import InventoryImportSchema

        return InventoryImportSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.inventories import InventoryImportSchema

        return InventoryImportSchema().dump(self)
