import datetime
import typing
import uuid

from commercetools.platform import models
from commercetools.platform.models._schemas.zone import (
    LocationSchema,
    ZoneDraftSchema,
    ZonePagedQueryResponseSchema,
    ZoneSchema,
    ZoneUpdateSchema,
)
from commercetools.testing.abstract import BaseModel, ServiceBackend
from commercetools.testing.utils import (
    update_attribute,
    update_attribute_add_item,
    update_attribute_delete_item,
)


class ZonesModel(BaseModel):
    _primary_type_name = "zones"
    _resource_schema = ZoneSchema
    _unique_values = ["key"]

    def _create_from_draft(
        self, draft: models.ZoneDraft, id: typing.Optional[str] = None
    ) -> models.Zone:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        return models.Zone(
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
    _schema_draft = ZoneDraftSchema
    _schema_update = ZoneUpdateSchema
    _schema_query_response = ZonePagedQueryResponseSchema

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
            "locations", "location", LocationSchema
        ),
        "removeLocation": update_attribute_delete_item(
            "locations", "location", LocationSchema
        ),
    }
