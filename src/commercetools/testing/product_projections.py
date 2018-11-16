import typing

from requests_mock import create_response

from commercetools import schemas, types
from commercetools.services.product_projections import ProductProjectionsQuerySchema
from commercetools.testing import utils
from commercetools.testing.abstract import ServiceBackend


class ProductProjectionsBackend(ServiceBackend):
    service_path = "product-projections"

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^key=(?P<key>[^/]+)$", "GET", self.get_by_key),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
        ]

    def query(self, request):
        params = utils.parse_request_params(ProductProjectionsQuerySchema, request)
        results = [
            self._convert_product_projection(product, params["staged"])
            for product in self.model.objects.values()
        ]
        results = [x for x in results if x]
        if params.get("limit"):
            results = results[: params["limit"]]

        data = {
            "count": len(results),
            "total": len(results),
            "offset": 0,
            "results": results,
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

    def _convert_product_projection(
        self, product: types.Product, staged: bool = False
    ) -> typing.Optional[types.ProductProjection]:
        """Convert a Product object to a ProductProjection object"""
        if product.master_data is None:
            return None

        if staged:
            data = product.master_data.staged
        else:
            data = product.master_data.current

        if data is None:
            return None

        return types.ProductProjection(
            id=product.id,
            key=product.key,
            version=product.version,
            created_at=product.created_at,
            last_modified_at=product.last_modified_at,
            product_type=product.product_type,
            name=data.name,
            description=data.description,
            slug=data.slug,
            categories=data.categories,
            category_order_hints=data.category_order_hints,
            meta_title=data.meta_title,
            meta_description=data.meta_description,
            meta_keywords=data.meta_keywords,
            search_keywords=data.search_keywords,
            has_staged_changes=product.master_data.has_staged_changes,
            published=product.master_data.published,
            master_variant=data.master_variant,
            variants=data.variants,
            tax_category=product.tax_category,
            state=product.state,
            review_rating_statistics=product.review_rating_statistics,
        )
