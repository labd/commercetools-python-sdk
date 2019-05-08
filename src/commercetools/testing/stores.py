import datetime
import typing
import uuid

from commercetools import schemas, types
from commercetools.testing.abstract import BaseModel, ServiceBackend
from commercetools.testing.utils import update_attribute


class StoresModel(BaseModel):
    _primary_type_name = "store"
    _resource_schema = schemas.StoreSchema

    def _create_from_draft(
        self, draft: types.StoreDraft, id: typing.Optional[str] = None
    ) -> types.Store:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        return types.Store(
            id=str(object_id),
            version=1,
            key=draft.key,
            name=draft.name,
            created_at=datetime.datetime.now(datetime.timezone.utc),
        )


class StoresBackend(ServiceBackend):
    service_path = "stores"
    model_class = StoresModel
    _schema_draft = schemas.StoreDraftSchema
    _schema_query_response = schemas.StorePagedQueryResponseSchema
    _schema_update = schemas.StoreUpdateSchema
    _verify_version = False

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^(?P<id>[^/]+)$", "DELETE", self.delete_by_id),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
            ("^key=(?P<key>[^/]+)$", "GET", self.get_by_key),
            ("^key=(?P<key>[^/]+)$", "DELETE", self.delete_by_key),
            ("^key=(?P<key>[^/]+)$", "POST", self.update_by_key),
        ]

    _actions = {
        "setName": update_attribute("name", "name"),
    }
