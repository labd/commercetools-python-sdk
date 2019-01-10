import datetime
import typing
import uuid

from commercetools import schemas, types
from commercetools.testing.abstract import BaseModel, ServiceBackend


class ProductTypesModel(BaseModel):
    _primary_type_name = "product-type"
    _resource_schema = schemas.ProductTypeSchema

    def _create_from_draft(
        self, obj: types.ProductTypeDraft, id: typing.Optional[str] = None
    ) -> types.ProductType:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        return types.ProductType(
            id=str(object_id),
            version=1,
            name=obj.name,
            description=obj.description,
            key=obj.key,
            created_at=datetime.datetime.now(),
            last_modified_at=datetime.datetime.now(),
            attributes=obj.attributes,
        )


class ProductTypesBackend(ServiceBackend):
    service_path = "product-types"
    model_class = ProductTypesModel

    _schema_draft = schemas.ProductTypeDraftSchema
    _schema_query_response = schemas.ProductTypePagedQueryResponseSchema

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
