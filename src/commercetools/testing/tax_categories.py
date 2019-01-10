import datetime
import typing
import uuid

from commercetools import schemas, types
from commercetools.testing.abstract import BaseModel, ServiceBackend


class TaxCategoryModel(BaseModel):
    _primary_type_name = "tax-category"
    _resource_schema = schemas.TaxCategorySchema

    def _create_from_draft(
        self, obj: types.TaxCategoryDraft, id: typing.Optional[str] = None
    ) -> types.TaxCategory:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        return types.TaxCategory(
            id=str(object_id),
            key=obj.key,
            version=1,
            created_at=datetime.datetime.now(),
            last_modified_at=datetime.datetime.now(),
            name=obj.name,
            description=obj.description,
        )


class TaxCategoryBackend(ServiceBackend):
    service_path = "tax-categories"
    model_class = TaxCategoryModel
    _schema_draft = schemas.TaxCategorySchema
    _schema_query_response = schemas.TaxCategoryPagedQueryResponseSchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^key=(?P<key>[^/]+)$", "GET", self.get_by_key),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^key=(?P<key>[^/]+)$", "POST", self.update_by_key),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
        ]
