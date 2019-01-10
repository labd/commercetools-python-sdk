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
        self, obj: types.InventoryEntryDraft, id: typing.Optional[str] = None
    ) -> types.InventoryEntry:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        return types.InventoryEntry(
            id=str(object_id),
            version=1,
            created_at=datetime.datetime.now(),
            expected_delivery=obj.expected_delivery,
            last_modified_at=datetime.datetime.now(),
            quantity_on_stock=obj.quantity_on_stock,
            restockable_in_days=obj.restockable_in_days,
            sku=obj.sku,
            supply_channel=obj.supply_channel,
            custom=utils.create_from_draft(obj.custom),
        )


class InventoryEntryBackend(ServiceBackend):
    service_path = "inventory"
    model_class = InventoryEntryModel
    _schema_draft = schemas.InventoryEntryDraftSchema
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
