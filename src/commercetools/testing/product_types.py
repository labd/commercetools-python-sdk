import datetime
import uuid

from requests_mock import create_response

from commercetools import abstract, schemas, types
from commercetools.testing.abstract import BaseModel, ServiceBackend


class ProductTypesModel(BaseModel):
    def add(self, id, obj):
        obj = self.add_product_type(obj)
        self.objects[obj.id] = obj
        return obj

    def add_product_type(self, obj):
        return types.ProductType(
            id=str(uuid.uuid4()),
            version=1,
            name=obj.name,
            description=obj.description,
            key=obj.key,
            created_at=datetime.datetime.now(),
            last_modified_at=datetime.datetime.now(),
        )


class ProductTypesBackend(ServiceBackend):
    service_path = "product-types"
    model_class = ProductTypesModel

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
        return r"/(?P<project>[^/]+)/product-types/?(?P<path>.*)?"

    def query(self, request):
        obj = abstract.AbstractQuerySchema().load(request.qs)
        data = {
            "count": len(self.model.objects),
            "total": len(self.model.objects),
            "offset": 0,
            "results": self.model.objects.values(),
        }
        content = schemas.ProductTypePagedQueryResponseSchema().dumps(data)
        return create_response(request, text=content)

    def create(self, request):
        obj = schemas.ProductTypeDraftSchema().loads(request.body)
        data = self.model.add(id, obj)
        content = schemas.ProductTypeSchema().dumps(data)
        return create_response(request, text=content)

    def get_by_id(self, request, id):
        obj = self.model.get_by_id(id)
        if obj:
            content = schemas.ProductTypeSchema().dumps(obj)
            return create_response(request, text=content)
        return create_response(request, status_code=404)

    def get_by_key(self, request, key):
        obj = self.model.get_by_key(key)
        if obj:
            content = schemas.ProductTypeSchema().dumps(obj)
            return create_response(request, text=content)
        return create_response(request, status_code=404)

    def update_by_id(self, request, id):
        obj = self.model.get_by_id(id)
        if obj:
            schemas.ProductTypeUpdateSchema().loads(request.body)
            content = schemas.ProductTypeSchema().dumps(obj)
            return create_response(request, text=content)
        return create_response(request, status_code=404)

    def update_by_key(self, request, key):
        obj = self.model.get_by_key(key)
        if obj:
            schemas.ProductTypeUpdateSchema().loads(request.body)
            content = schemas.ProductTypeSchema().dumps(obj)
            return create_response(request, text=content)
        return create_response(request, status_code=404)
