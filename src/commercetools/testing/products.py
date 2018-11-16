import datetime
import typing
import uuid

from requests_mock import create_response

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.testing import utils
from commercetools.testing.abstract import BaseModel, ServiceBackend


class ProductsModel(BaseModel):
    def _create_from_draft(
        self, obj: types.ProductDraft, id: typing.Optional[str] = None
    ) -> types.Product:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())

        product = types.Product(
            id=str(object_id),
            key=obj.key,
            product_type=obj.product_type,
            version=1,
            created_at=datetime.datetime.now(),
            last_modified_at=datetime.datetime.now(),
        )

        product_data = types.ProductData(
            name=obj.name,
            categories=obj.categories,
            category_order_hints=obj.category_order_hints,
            description=obj.description,
            master_variant=obj.master_variant,
            slug=obj.slug or types.LocalizedString(),
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
        content = schemas.ProductPagedQueryResponseSchema().dumps(data)
        return create_response(request, text=content)

    def create(self, request):
        obj = schemas.ProductDraftSchema().loads(request.body)
        data = self.model.add(obj)
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
