import datetime
import uuid

from requests_mock import create_response

from commercetools import abstract, schemas, types
from commercetools.testing.abstract import BaseModel, ServiceBackend


class CategoriesModel(BaseModel):
    def add(self, id, obj):
        obj = self.add_category(obj)
        self.objects[obj.id] = obj
        return obj

    def add_category(self, obj):
        return types.Category(
            id=str(uuid.uuid4()),
            version=1,
            name=obj.name,
            description=obj.description,
            slug=obj.slug,
            key=obj.key,
            created_at=datetime.datetime.now(),
            last_modified_at=datetime.datetime.now(),
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

    @property
    def path_prefix(self):
        return r"/(?P<project>[^/]+)/categories/?(?P<path>.*)?"

    def query(self, request):
        obj = abstract.AbstractQuerySchema().load(request.qs)
        data = {
            "count": len(self.model.objects),
            "total": len(self.model.objects),
            "offset": 0,
            "results": self.model.objects.values(),
        }
        content = schemas.CategoryPagedQueryResponseSchema().dumps(data)
        return create_response(request, text=content)

    def create(self, request):
        obj = schemas.CategoryDraftSchema().loads(request.body)
        data = self.model.add(id, obj)
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
