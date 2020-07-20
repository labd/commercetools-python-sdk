import copy
import datetime
import uuid
from typing import Dict, List, Optional

from commercetools import schemas, types
from commercetools.testing.abstract import BaseModel, ServiceBackend
from commercetools.testing.utils import InternalUpdateError, update_attribute


class StoresModel(BaseModel):
    _primary_type_name = "store"
    _resource_schema = schemas.StoreSchema
    _unique_values = ["key"]

    def _create_from_draft(
        self, draft: types.StoreDraft, id: Optional[str] = None
    ) -> types.Store:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        distribution_channels: List[types.ChannelReference] = []
        if draft.distribution_channels:
            distribution_channels = convert_identifiers_to_references(
                self._storage._stores["channel"], draft.distribution_channels
            )

        return types.Store(
            id=str(object_id),
            version=1,
            key=draft.key,
            name=draft.name,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            languages=draft.languages,
            distribution_channels=distribution_channels,
        )


def convert_identifiers_to_references(
    channel_store: Dict, channel_identifiers: List[types.ChannelResourceIdentifier]
) -> List[types.ChannelReference]:
    channel_references: List[types.ChannelReference] = []
    for ci in channel_identifiers:
        channel_data: Optional[Dict] = None
        for c in channel_store.values():
            if ci.key and c["key"] == ci.key:
                channel_data = c
                break
            if ci.id and c["id"] == ci.id:
                channel_data = c
                break
        if not channel_data:
            raise InternalUpdateError("Channel not found.")
        channel: types.Channel = schemas.ChannelSchema().load(data=channel_data)
        if types.ChannelRoleEnum.PRODUCT_DISTRIBUTION not in channel.roles:
            raise InternalUpdateError(
                "Channel does not have product distribution role."
            )
        channel_references.append(types.ChannelReference(id=channel.id))
    return channel_references


def set_languages():
    def updater(self, obj, action):
        value = getattr(action, "languages")
        new = copy.deepcopy(obj)
        new["languages"] = value
        return new

    return updater


def set_distribution_channels(
    backend: "StoresBackend",
    obj: Dict,
    action: types.StoresSetDistributionChannelsAction,
):
    channel_references = []
    if action.distribution_channels:
        channel_references = convert_identifiers_to_references(
            backend.model._storage._stores["channel"], action.distribution_channels
        )
    new = copy.deepcopy(obj)
    new["distributionChannels"] = schemas.ChannelResourceIdentifierSchema().dump(
        channel_references, many=True
    )
    return new


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
        "setLanguages": set_languages(),
        "setDistributionChannels": set_distribution_channels,
    }
