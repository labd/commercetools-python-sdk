import datetime
import typing
import uuid

from commercetools import schemas, types
from commercetools.testing.abstract import BaseModel, ServiceBackend


class TypesModel(BaseModel):
    _primary_type_name = "type"
    _resource_schema = schemas.TypeSchema

    def _create_from_draft(
        self, obj: types.TypeDraft, id: typing.Optional[str] = None
    ) -> types.Type:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        return types.Type(
            id=str(object_id),
            version=1,
            name=obj.name,
            description=obj.description,
            key=obj.key,
            created_at=datetime.datetime.now(),
            last_modified_at=datetime.datetime.now(),
            resource_type_ids=obj.resource_type_ids,
            field_definitions=obj.field_definitions,
        )


class TypesBackend(ServiceBackend):
    service_path = "types"
    model_class = TypesModel
    _schema_draft = schemas.TypeDraftSchema
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
