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
    _unique_values = ["key"]

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
            transitions=create_references_from_resources(self, draft.transitions),
            created_at=datetime.datetime.now(datetime.timezone.utc),
            last_modified_at=datetime.datetime.now(datetime.timezone.utc),
        )


def create_references_from_resources(
    model: StateModel,
    state_transitions: typing.Optional[typing.List[types.StateResourceIdentifier]],
) -> typing.List[types.StateReference]:
    if not state_transitions:
        return []
    references = []
    for state_identifier in state_transitions:
        if state_identifier.id:
            references.append(types.StateReference(id=state_identifier.id))
        if state_identifier.key:
            obj = model.get_by_key(state_identifier.key)
            if obj:
                references.append(types.StateReference(id=obj["id"]))

    return references


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


def set_transitions():
    def updater(self, obj: dict, action: types.StateSetTransitionsAction):
        transitions = action.transitions
        references = []
        if action.transitions:
            for reference in create_references_from_resources(self.model, transitions):
                references.append(schemas.StateReferenceSchema().dump(reference))

        if obj["transitions"] != references:
            new = copy.deepcopy(obj)
            new["transitions"] = references
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
        "setTransitions": set_transitions(),
    }
