import datetime
import typing
import uuid

from requests_mock import create_response

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.testing import utils
from commercetools.testing.abstract import BaseModel, ServiceBackend


class InventoryEntryModel(BaseModel):
    def _create_from_draft(
        self, obj: types.InventoryEntryDraft, id: typing.Optional[str] = None
    ) -> types.CustomObject:
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
        )


class InventoryEntryBackend(ServiceBackend):
    service_path = "inventory"
    model_class = InventoryEntryModel

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
        ]

    def query(self, request):
        params = utils.parse_request_params(abstract.AbstractQuerySchema, request)
        results = list(self.model.objects.values())
        if params.get("limit"):
            results = results[: params["limit"]]

        data = {
            "count": len(results),
            "total": len(self.model.objects),
            "offset": 0,
            "results": results,
        }
        content = schemas.InventoryEntryPagedQueryResponseSchema().dumps(data)
        return create_response(request, text=content)

    def create(self, request):
        obj = schemas.InventoryEntryDraftSchema().loads(request.body)
        data = self.model.add(obj)
        content = schemas.InventoryEntrySchema().dumps(data)
        return create_response(request, text=content)

    def get_by_id(self, request, id):
        obj = self.model.get_by_id(id)
        if obj:
            content = schemas.InventoryEntrySchema().dumps(obj)
            return create_response(request, text=content)
        return create_response(request, status_code=404)

    def update_by_id(self, request, id):
        obj = self.model.get_by_id(id)
        if obj:
            schemas.InventoryUpdateSchema().loads(request.body)
            content = schemas.InventoryEntrySchema().dumps(obj)
            return create_response(request, text=content)
        return create_response(request, status_code=404)
