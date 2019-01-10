import datetime
import typing
import uuid

from commercetools import schemas, types
from commercetools.testing import utils
from commercetools.testing.abstract import BaseModel, ServiceBackend


class CategoriesModel(BaseModel):
    _primary_type_name = "category"
    _resource_schema = schemas.CategorySchema

    def _create_from_draft(
        self, obj: types.CategoryDraft, id: typing.Optional[str] = None
    ) -> types.Category:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        return types.Category(
            id=str(object_id),
            version=1,
            name=obj.name,
            description=obj.description,
            slug=obj.slug,
            key=obj.key,
            created_at=datetime.datetime.now(),
            last_modified_at=datetime.datetime.now(),
            custom=utils.create_from_draft(obj.custom),
        )


class CategoriesBackend(ServiceBackend):
    service_path = "categories"
    model_class = CategoriesModel
    _schema_draft = schemas.CategoryDraftSchema
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
