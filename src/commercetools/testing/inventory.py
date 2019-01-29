import datetime
import typing
import uuid

from commercetools import schemas, types
from commercetools.testing import utils
from commercetools.testing.abstract import BaseModel, ServiceBackend


class InventoryEntryModel(BaseModel):
    _primary_type_name = "inventory-entry"
    _resource_schema = schemas.InventoryEntrySchema

    def _create_from_draft(
        self, draft: types.InventoryEntryDraft, id: typing.Optional[str] = None
    ) -> types.InventoryEntry:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        return types.InventoryEntry(
            id=str(object_id),
            version=1,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            expected_delivery=draft.expected_delivery,
            last_modified_at=datetime.datetime.now(datetime.timezone.utc),
            quantity_on_stock=draft.quantity_on_stock,
            restockable_in_days=draft.restockable_in_days,
            sku=draft.sku,
            supply_channel=draft.supply_channel,
            custom=utils.create_from_draft(draft.custom),
        )


class InventoryEntryBackend(ServiceBackend):
    service_path = "inventory"
    model_class = InventoryEntryModel
    _schema_draft = schemas.InventoryEntryDraftSchema
    _schema_update = schemas.InventoryUpdateSchema
    _schema_query_response = schemas.InventoryPagedQueryResponseSchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
            ("^(?P<id>[^/]+)$", "DELETE", self.delete_by_id),
            ("^key=(?P<key>[^/]+)$", "DELETE", self.delete_by_key),
        ]
