import typing

from commercetools import schemas, types
from commercetools.services.product_projections import ProductProjectionsQuerySchema
from commercetools.testing import utils
from commercetools.testing.abstract import ServiceBackend
from commercetools.testing.utils import create_commercetools_response


class ProductProjectionsBackend(ServiceBackend):
    service_path = "product-projections"

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^search", "POST", self.search),
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
        return create_commercetools_response(request, text=content)

    def search(self, request):
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
        return create_commercetools_response(request, text=content)

    def get_by_id(self, request, id):
        obj = self.model.get_by_id(id)
        if obj:
            content = schemas.ProductProjectionSchema().dumps(obj)
            return create_commercetools_response(request, text=content)
        return create_commercetools_response(request, status_code=404)

    def get_by_key(self, request, key):
        obj = self.model.get_by_key(key)
        if obj:
            content = schemas.ProductProjectionSchema().dumps(obj)
            return create_commercetools_response(request, text=content)
        return create_commercetools_response(request, status_code=404)

    def _convert_product_projection(
        self, product: typing.Dict, staged: bool = False
    ) -> typing.Optional[types.ProductProjection]:
        """Convert a Product object to a ProductProjection object"""
        if product["masterData"] is None:
            return None

        if staged:
            data = product["masterData"]["staged"]
        else:
            data = product["masterData"]["current"]

        if data is None:
            return None

        return schemas.ProductProjectionSchema().load(
            {
                "id": product["id"],
                "key": product["key"],
                "version": product["version"],
                "createdAt": product["createdAt"],
                "lastModifiedAt": product["lastModifiedAt"],
                "productType": product["productType"],
                "name": data["name"],
                "description": data["description"],
                "slug": data["slug"],
                "categories": data["categories"],
                "categoryOrderHints": data["categoryOrderHints"],
                "metaTitle": data["metaTitle"],
                "metaDescription": data["metaDescription"],
                "metaKeywords": data["metaKeywords"],
                "searchKeywords": data["searchKeywords"],
                "hasStagedChanges": product["masterData"]["hasStagedChanges"],
                "published": product["masterData"]["published"],
                "masterVariant": data["masterVariant"],
                "variants": data["variants"],
                "taxCategory": product["taxCategory"],
                "state": product["state"],
                "reviewRatingStatistics": product["reviewRatingStatistics"],
            }
        )
