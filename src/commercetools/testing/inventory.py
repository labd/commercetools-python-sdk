import copy
import datetime
import typing
import uuid

from commercetools.platform import models
from commercetools.platform.models._schemas.inventory import (
    InventoryEntryDraftSchema,
    InventoryEntrySchema,
    InventoryEntryUpdateSchema,
    InventoryPagedQueryResponseSchema,
)
from commercetools.testing import utils
from commercetools.testing.abstract import BaseModel, ServiceBackend
from commercetools.testing.utils import InternalUpdateError, update_attribute


class InventoryEntryModel(BaseModel):
    _primary_type_name = "inventory-entry"
    _resource_schema = InventoryEntrySchema

    def _create_from_draft(
        self, draft: models.InventoryEntryDraft, id: typing.Optional[str] = None
    ) -> models.InventoryEntry:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        return models.InventoryEntry(
            id=str(object_id),
            version=1,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            expected_delivery=draft.expected_delivery,
            last_modified_at=datetime.datetime.now(datetime.timezone.utc),
            quantity_on_stock=draft.quantity_on_stock,
            available_quantity=draft.quantity_on_stock,
            restockable_in_days=draft.restockable_in_days,
            sku=draft.sku,
            supply_channel=draft.supply_channel,
            custom=utils.create_from_draft(draft.custom),
        )


def change_stock():
    def updater(self, obj, action: models.InventoryEntryUpdateAction):
        quantity = getattr(action, "quantity")

        new = copy.deepcopy(obj)

        if isinstance(action, models.InventoryEntryAddQuantityAction):
            new["availableQuantity"] += quantity
        elif isinstance(action, models.InventoryEntryRemoveQuantityAction):
            new["availableQuantity"] -= quantity
        elif isinstance(action, models.InventoryEntryChangeQuantityAction):
            new["availableQuantity"] = quantity
        else:
            raise InternalUpdateError("Unknown action to change stock: %r", action)

        # For now we don't reserve stock
        new["quantityOnStock"] = new["availableQuantity"]
        return new

    return updater


class InventoryEntryBackend(ServiceBackend):
    service_path = "inventory"
    model_class = InventoryEntryModel
    _schema_draft = InventoryEntryDraftSchema
    _schema_update = InventoryEntryUpdateSchema
    _schema_query_response = InventoryPagedQueryResponseSchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
            ("^(?P<id>[^/]+)$", "DELETE", self.delete_by_id),
            ("^key=(?P<key>[^/]+)$", "DELETE", self.delete_by_key),
        ]

    _actions = {
        "addQuantity": change_stock(),
        "removeQuantity": change_stock(),
        "changeQuantity": change_stock(),
        "setRestockableInDays": update_attribute(
            "restockableInDays", "restockableInDays"
        ),
        "setExpectedDelivery": update_attribute("expectedDelivery", "expectedDelivery"),
    }
