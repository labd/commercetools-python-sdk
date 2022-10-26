import typing

from marshmallow import fields

from commercetools.platform import models
from commercetools.platform.models._schemas.product import (
    ProductProjectionPagedQueryResponseSchema,
    ProductProjectionSchema,
    ProductSchema,
)
from commercetools.testing import traits, utils
from commercetools.testing.abstract import ServiceBackend
from commercetools.testing.utils import create_commercetools_response


class _ProductProjectionQuerySchema(
    traits.ExpandableSchema,
    traits.SortableSchema,
    traits.PagingSchema,
    traits.QuerySchema,
    traits.PriceSelectingSchema,
):
    staged = fields.Bool(required=False, missing=False)


class ProductProjectionsBackend(ServiceBackend):
    service_path = "product-projections"
    _schema_query_params = _ProductProjectionQuerySchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^search", "POST", self.search),
            ("^key=(?P<key>[^/]+)$", "GET", self.get_by_key),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
        ]

    def query(self, request):
        params = utils.parse_request_params(_ProductProjectionQuerySchema, request)
        limit = params.get("limit")

        results = []
        found = 0
        for obj in self.model.objects.values():
            expanded_obj = self._expand(request, obj)
            product = ProductSchema().load(expanded_obj)

            result = self._convert_product_projection(product, params["staged"])
            if result:
                results.append(result)
                found += 1

            if limit is not None and found == limit:
                break

        data = {
            "count": len(results),
            "total": len(results),
            "offset": 0,
            "results": results,
            "limit": limit,
        }
        content = ProductProjectionPagedQueryResponseSchema().dumps(data)
        return create_commercetools_response(request, text=content)

    def search(self, request):
        params = utils.parse_request_params(_ProductProjectionQuerySchema, request)

        limit = params.get("limit")

        results = []
        found = 0
        for obj in self.model.objects.values():
            expanded_obj = self._expand(request, obj)
            product = ProductSchema().load(expanded_obj)

            result = self._convert_product_projection(product, params["staged"])
            if result:
                results.append(results)
                found += 1

            if limit is not None and found == limit:
                break

        data = {
            "count": len(results),
            "total": len(results),  # FIXME
            "offset": 0,
            "results": results,
            "limit": limit,
        }
        content = ProductProjectionPagedQueryResponseSchema().dumps(data)
        return create_commercetools_response(request, text=content)

    def get_by_id(self, request, id):
        params = utils.parse_request_params(_ProductProjectionQuerySchema, request)
        obj = self.model.get_by_id(id)
        if obj:
            expanded_obj = self._expand(request, obj)
            product = ProductSchema().load(expanded_obj)

            result = self._convert_product_projection(product, params["staged"])
            if not result:
                return create_commercetools_response(request, status_code=404)
            content = ProductProjectionSchema().dumps(result)
            return create_commercetools_response(request, text=content)
        return create_commercetools_response(request, status_code=404)

    def get_by_key(self, request, key):
        params = utils.parse_request_params(_ProductProjectionQuerySchema, request)
        obj = self.model.get_by_key(key)
        if obj:
            expanded_obj = self._expand(request, obj)
            product = ProductSchema().load(expanded_obj)

            result = self._convert_product_projection(product, params["staged"])
            if not result:
                return create_commercetools_response(request, status_code=404)
            content = ProductProjectionSchema().dumps(result)
            return create_commercetools_response(request, text=content)
        return create_commercetools_response(request, status_code=404)

    def _convert_product_projection(
        self, product: models.Product, staged: bool = False
    ) -> typing.Optional[models.ProductProjection]:
        """Convert a Product object to a ProductProjection object"""
        if product.master_data is None:
            return None

        if staged:
            data: models.ProductData = product.master_data.staged
        else:
            data: models.ProductData = product.master_data.current

        if data is None:
            return None

        return models.ProductProjection(
            id=product.id,
            version=product.version,
            key=product.key,
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
