import datetime
import uuid

from requests_mock import create_response

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.testing import utils
from commercetools.testing.abstract import BaseModel, ServiceBackend


class CategoriesModel(BaseModel):
    def _create_from_draft(self, obj: types.CategoryDraft, id: str) -> types.Category:
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

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^key=(?P<key>[^/]+)$", "GET", self.get_by_key),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^key=(?P<key>[^/]+)$", "POST", self.update_by_key),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
        ]

    def query(self, request):
        params = utils.parse_request_params(abstract.AbstractQuerySchema, request)
        results = list(self.model.objects.values())
        if params.get("limit"):
            results = results[: params["limit"]]

        data = {
            "count": len(results),
            "total": len(self.model.objects),
            "offset": 0,
            "results": results,
        }
        content = schemas.CategoryPagedQueryResponseSchema().dumps(data)
        return create_response(request, text=content)

    def create(self, request):
        obj = schemas.CategoryDraftSchema().loads(request.body)
        data = self.model.add(obj)
        content = schemas.CategorySchema().dumps(data)
        return create_response(request, text=content)

    def get_by_id(self, request, id):
        obj = self.model.get_by_id(id)
        if obj:
            content = schemas.CategorySchema().dumps(obj)
            return create_response(request, text=content)
        return create_response(request, status_code=404)

    def get_by_key(self, request, key):
        obj = self.model.get_by_key(key)
        if obj:
            content = schemas.CategorySchema().dumps(obj)
            return create_response(request, text=content)
        return create_response(request, status_code=404)

    def update_by_id(self, request, id):
        obj = self.model.get_by_id(id)
        if obj:
            schemas.CategoryUpdateSchema().loads(request.body)
            content = schemas.CategorySchema().dumps(obj)
            return create_response(request, text=content)
        return create_response(request, status_code=404)

    def update_by_key(self, request, key):
        obj = self.model.get_by_key(key)
        if obj:
            schemas.CategoryUpdateSchema().loads(request.body)
            content = schemas.CategorySchema().dumps(obj)
            return create_response(request, text=content)
        return create_response(request, status_code=404)
