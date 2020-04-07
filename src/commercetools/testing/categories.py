import datetime
import typing
import uuid

from commercetools import schemas, types
from commercetools.testing import utils
from commercetools.testing.abstract import BaseModel, ServiceBackend


class CategoriesModel(BaseModel):
    _primary_type_name = "category"
    _resource_schema = schemas.CategorySchema
    _unique_values = ["key"]

    def _create_from_draft(
        self, draft: types.CategoryDraft, id: typing.Optional[str] = None
    ) -> types.Category:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        return types.Category(
            id=str(object_id),
            version=1,
            name=draft.name,
            description=draft.description,
            slug=draft.slug,
            key=draft.key,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            last_modified_at=datetime.datetime.now(datetime.timezone.utc),
            custom=utils.create_from_draft(draft.custom),
        )


class CategoriesBackend(ServiceBackend):
    service_path = "categories"
    model_class = CategoriesModel
    _schema_draft = schemas.CategoryDraftSchema
    _schema_update = schemas.CategoryUpdateSchema
    _schema_query_response = schemas.CategoryPagedQueryResponseSchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^key=(?P<key>[^/]+)$", "GET", self.get_by_key),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^key=(?P<key>[^/]+)$", "POST", self.update_by_key),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
        ]
