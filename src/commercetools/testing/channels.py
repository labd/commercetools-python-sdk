import datetime
import typing
import uuid

from commercetools import schemas, types
from commercetools.testing import utils
from commercetools.testing.abstract import BaseModel, ServiceBackend


class ChannelsModel(BaseModel):
    _resource_schema = schemas.ChannelSchema
    _primary_type_name = "channel"

    def _create_from_draft(
        self, obj: types.ChannelDraft, id: typing.Optional[str] = None
    ) -> types.Channel:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        return types.Channel(
            id=str(object_id),
            version=1,
            name=obj.name,
            description=obj.description,
            roles=obj.roles,
            key=obj.key,
            created_at=datetime.datetime.now(),
            last_modified_at=datetime.datetime.now(),
            custom=utils.create_from_draft(obj.custom),
        )


class ChannelsBackend(ServiceBackend):
    service_path = "channels"
    model_class = ChannelsModel
    _schema_draft = schemas.ChannelDraftSchema
    _schema_query_response = schemas.ChannelPagedQueryResponseSchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
        ]
