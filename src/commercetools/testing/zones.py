import datetime
import typing
import uuid

from commercetools import schemas, types
from commercetools.testing.abstract import BaseModel, ServiceBackend
from commercetools.testing.utils import (
    update_attribute,
    update_attribute_add_item,
    update_attribute_delete_item,
)


class ZonesModel(BaseModel):
    _primary_type_name = "zones"
    _resource_schema = schemas.ZoneSchema
    _unique_values = ["key"]

    def _create_from_draft(
        self, draft: types.ZoneDraft, id: typing.Optional[str] = None
    ) -> types.Zone:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        return types.Zone(
            id=str(object_id),
            version=1,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            last_modified_at=datetime.datetime.now(datetime.timezone.utc),
            key=draft.key,
            name=draft.name,
            description=draft.description,
            locations=draft.locations,
        )


class ZonesBackend(ServiceBackend):
    service_path = "zones"
    model_class = ZonesModel
    _schema_draft = schemas.ZoneDraftSchema
    _schema_update = schemas.ZoneUpdateSchema
    _schema_query_response = schemas.ZonePagedQueryResponseSchema

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
        "changeName": update_attribute("name", "name"),
        "setKey": update_attribute("key", "key"),
        "setDescription": update_attribute("description", "description"),
        "addLocation": update_attribute_add_item(
            "locations", "location", schemas.LocationSchema
        ),
        "removeLocation": update_attribute_delete_item(
            "locations", "location", schemas.LocationSchema
        ),
    }
