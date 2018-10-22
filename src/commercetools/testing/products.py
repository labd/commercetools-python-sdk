import datetime
import uuid

from requests_mock import create_response

from commercetools import abstract, schemas, types
from commercetools.testing.abstract import BaseModel, ServiceBackend


class ProductsModel(BaseModel):
    def add(self, id, obj):
        obj = self.convert_product_draft(obj)
        self.objects[obj.id] = obj
        return obj

    def convert_product_draft(self, obj: types.ProductDraft):
        product = types.Product(
            id=str(uuid.uuid4()),
            key=obj.key,
            version=1,
            created_at=datetime.datetime.now(),
            last_modified_at=datetime.datetime.now(),
        )

        product_data = types.ProductData(
            name=obj.name,
            categories=obj.categories,
            category_order_hints=obj.category_order_hints,
            description=obj.description,
            slug=obj.slug,
        )

        if obj.publish:
            product.master_data = types.ProductCatalogData(
                staged=None, current=product_data, published=True
            )
        else:
            product.master_data = types.ProductCatalogData(
                staged=product_data, current=None, published=False
            )

        return product


class ProductsBackend(ServiceBackend):
    service_path = "products"
    model_class = ProductsModel

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
        return r"/(?P<project>[^/]+)/products/?(?P<path>.*)?"

    def query(self, request):
        obj = abstract.AbstractQuerySchema().load(request.qs)
        data = {
            "count": len(self.model.objects),
            "total": len(self.model.objects),
            "offset": 0,
            "results": self.model.objects.values(),
        }
        content = schemas.ProductPagedQueryResponseSchema().dumps(data)
        return create_response(request, text=content)

    def create(self, request):
        obj = schemas.ProductDraftSchema().loads(request.body)
        data = self.model.add(id, obj)
        content = schemas.ProductSchema().dumps(data)
        return create_response(request, text=content)

    def get_by_id(self, request, id):
        obj = self.model.get_by_id(id)
        if obj:
            content = schemas.ProductSchema().dumps(obj)
            return create_response(request, text=content)
        return create_response(request, status_code=404)

    def get_by_key(self, request, key):
        obj = self.model.get_by_key(key)
        if obj:
            content = schemas.ProductSchema().dumps(obj)
            return create_response(request, text=content)
        return create_response(request, status_code=404)

    def update_by_id(self, request, id):
        obj = self.model.get_by_id(id)
        if obj:
            schemas.ProductUpdateSchema().loads(request.body)
            content = schemas.ProductSchema().dumps(obj)
            return create_response(request, text=content)
        return create_response(request, status_code=404)

    def update_by_key(self, request, key):
        obj = self.model.get_by_key(key)
        if obj:
            schemas.ProductUpdateSchema().loads(request.body)
            content = schemas.ProductSchema().dumps(obj)
            return create_response(request, text=content)
        return create_response(request, status_code=404)
