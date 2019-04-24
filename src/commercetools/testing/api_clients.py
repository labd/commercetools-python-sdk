import datetime
import typing
import uuid

from commercetools import schemas, types
from commercetools.testing.abstract import BaseModel, ServiceBackend


class ApiClientsModel(BaseModel):
    _primary_type_name = "api-client"
    _resource_schema = schemas.ApiClientSchema

    def _create_from_draft(
        self, draft: types.ApiClientDraft, id: typing.Optional[str] = None
    ) -> types.ApiClient:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        return types.ApiClient(
            id=str(object_id),
            name=draft.name,
            scope=draft.scope,
            secret=str(uuid.uuid4()),
            created_at=datetime.datetime.now(datetime.timezone.utc),
        )


class ApiClientsBackend(ServiceBackend):
    service_path = "api-clients"
    model_class = ApiClientsModel
    _schema_draft = schemas.ApiClientDraftSchema
    _schema_query_response = schemas.ApiClientPagedQueryResponseSchema
    _verify_version = False

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^(?P<id>[^/]+)$", "DELETE", self.delete_by_id),
        ]
