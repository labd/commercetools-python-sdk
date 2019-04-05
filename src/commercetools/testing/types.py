import datetime
import typing
import uuid

from commercetools import schemas, types
from commercetools.testing.abstract import BaseModel, ServiceBackend
from commercetools.testing.utils import update_attribute_add_item, update_attribute


class TypesModel(BaseModel):
    _primary_type_name = "type"
    _resource_schema = schemas.TypeSchema

    def _create_from_draft(
        self, draft: types.TypeDraft, id: typing.Optional[str] = None
    ) -> types.Type:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        return types.Type(
            id=str(object_id),
            version=1,
            name=draft.name,
            description=draft.description,
            key=draft.key,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            last_modified_at=datetime.datetime.now(datetime.timezone.utc),
            resource_type_ids=draft.resource_type_ids,
            field_definitions=draft.field_definitions,
        )


class TypesBackend(ServiceBackend):
    service_path = "types"
    model_class = TypesModel
    _schema_draft = schemas.TypeDraftSchema
    _schema_update = schemas.TypeUpdateSchema
    _schema_query_response = schemas.TypePagedQueryResponseSchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^key=(?P<key>[^/]+)$", "GET", self.get_by_key),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^key=(?P<key>[^/]+)$", "POST", self.update_by_key),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
            ("^(?P<id>[^/]+)$", "DELETE", self.delete_by_id),
            ("^key=(?P<key>[^/]+)$", "DELETE", self.delete_by_key),
        ]

    # Fixme: use decorator for this
    _actions = {
        "addFieldDefinition": update_attribute_add_item(
            "fieldDefinitions", "field_definition", schemas.FieldDefinitionSchema
        ),
        "setDescription": update_attribute("description", "description")
    }
