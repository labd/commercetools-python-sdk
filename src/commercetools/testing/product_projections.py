import datetime

from requests_mock import create_response

from commercetools import abstract, schemas, types
from commercetools.testing.abstract import BaseModel, ServiceBackend


class ProductProjectionsModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.add_projection("0001", "product-1")
        self.add_projection("0002", "product-2")

    def add_projection(self, id, key):
        obj = types.ProductProjection(
            id=id,
            version=1,
            key=key,
            created_at=datetime.datetime.now(),
            last_modified_at=datetime.datetime.now(),
        )
        self.add(obj.id, obj)


class ProductProjectionsBackend(ServiceBackend):
    service_path = "product_projections"
    model_class = ProductProjectionsModel

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^key=(?P<key>[^/]+)$", "GET", self.get_by_key),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
        ]

    @property
    def path_prefix(self):
        return r"/(?P<project>[^/]+)/product-projections/?(?P<path>.*)?"

    def query(self, request):
        obj = abstract.AbstractQuerySchema().load(request.qs)
        data = {
            "count": len(self.model.objects),
            "total": len(self.model.objects),
            "offset": 0,
            "results": self.model.objects.values(),
        }
        content = schemas.ProductProjectionPagedQueryResponseSchema().dumps(data)
        return create_response(request, text=content)

    def get_by_id(self, request, id):
        obj = self.model.get_by_id(id)
        if obj:
            content = schemas.ProductProjectionSchema().dumps(obj)
            return create_response(request, text=content)
        return create_response(request, status_code=404)

    def get_by_key(self, request, key):
        obj = self.model.get_by_key(key)
        if obj:
            content = schemas.ProductProjectionSchema().dumps(obj)
            return create_response(request, text=content)
        return create_response(request, status_code=404)
