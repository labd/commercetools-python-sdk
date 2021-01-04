import datetime
import typing
import uuid

from commercetools.platform import models
from commercetools.platform.models._schemas.channel import (
    ChannelDraftSchema,
    ChannelPagedQueryResponseSchema,
    ChannelSchema,
    ChannelUpdateSchema,
)
from commercetools.testing import utils
from commercetools.testing.abstract import BaseModel, ServiceBackend


class ChannelsModel(BaseModel):
    _resource_schema = ChannelSchema
    _primary_type_name = "channel"
    _unique_values = ["key"]

    def _create_from_draft(
        self, draft: models.ChannelDraft, id: typing.Optional[str] = None
    ) -> models.Channel:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        return models.Channel(
            id=str(object_id),
            version=1,
            name=draft.name,
            description=draft.description,
            roles=draft.roles,
            key=draft.key,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            last_modified_at=datetime.datetime.now(datetime.timezone.utc),
            custom=utils.create_from_draft(draft.custom),
        )


class ChannelsBackend(ServiceBackend):
    service_path = "channels"
    model_class = ChannelsModel
    _schema_draft = ChannelDraftSchema
    _schema_update = ChannelUpdateSchema
    _schema_query_response = ChannelPagedQueryResponseSchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
            ("^(?P<id>[^/]+)$", "DELETE", self.delete_by_id),
        ]
