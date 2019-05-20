import copy
import datetime
import typing
import uuid

from commercetools import schemas, types
from commercetools.testing.abstract import BaseModel, ServiceBackend
from commercetools.testing.utils import update_attribute


class StateModel(BaseModel):
    _resource_schema = schemas.StateSchema
    _primary_type_name = "state"

    def _create_from_draft(
        self, draft: types.StateDraft, id: typing.Optional[str] = None
    ) -> types.State:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        return types.State(
            id=str(object_id),
            version=1,
            key=draft.key,
            type=draft.type,
            name=draft.name,
            description=draft.description,
            roles=draft.roles,
            initial=draft.initial or False,
            transitions=draft.transitions,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            last_modified_at=datetime.datetime.now(datetime.timezone.utc),
        )


def set_roles():
    def updater(self, obj: dict, action: types.StateSetRolesAction):
        roles = getattr(action, "roles")

        if roles:
            roles = schemas.StateSetRolesActionSchema().dump(action)["roles"]

        if obj["roles"] != roles:
            new = copy.deepcopy(obj)
            new["roles"] = roles
            return new
        return obj

    return updater


class StatesBackend(ServiceBackend):
    service_path = "states"
    model_class = StateModel
    _schema_draft = schemas.StateDraftSchema
    _schema_update = schemas.StateUpdateSchema
    _schema_query_response = schemas.StatePagedQueryResponseSchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
            ("^(?P<id>[^/]+)$", "DELETE", self.delete_by_id),
        ]

    _actions = {
        "setName": update_attribute("name", "name"),
        "setDescription": update_attribute("description", "description"),
        "changeKey": update_attribute("key", "key"),
        "changeType": update_attribute("type", "type"),
        "changeInitial": update_attribute("initial", "initial"),
        "setRoles": set_roles(),
    }



