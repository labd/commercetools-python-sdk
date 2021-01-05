# Generated file, please do not change!!!
import typing

from ...models.product_discount import (
    ProductDiscount,
    ProductDiscountDraft,
    ProductDiscountPagedQueryResponse,
)
from ..matching.by_project_key_product_discounts_matching_request_builder import (
    ByProjectKeyProductDiscountsMatchingRequestBuilder,
)
from .by_project_key_product_discounts_by_id_request_builder import (
    ByProjectKeyProductDiscountsByIDRequestBuilder,
)
from .by_project_key_product_discounts_key_by_key_request_builder import (
    ByProjectKeyProductDiscountsKeyByKeyRequestBuilder,
)


class ByProjectKeyProductDiscountsRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def matching(self) -> ByProjectKeyProductDiscountsMatchingRequestBuilder:
        return ByProjectKeyProductDiscountsMatchingRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def withKey(self, key: str) -> ByProjectKeyProductDiscountsKeyByKeyRequestBuilder:
        return ByProjectKeyProductDiscountsKeyByKeyRequestBuilder(
            key=key,
            projectKey=self._project_key,
            client=self._client,
        )

    def withId(self, ID: str) -> ByProjectKeyProductDiscountsByIDRequestBuilder:
        return ByProjectKeyProductDiscountsByIDRequestBuilder(
            ID=ID,
            projectKey=self._project_key,
            client=self._client,
        )

    def get(
        self,
        *,
        expand: "str" = None,
        sort: "str" = None,
        limit: "int" = None,
        offset: "int" = None,
        with_total: "bool" = None,
        where: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ProductDiscountPagedQueryResponse":
        """Query product-discounts"""
        return self._client._get(
            endpoint=f"/{self._project_key}/product-discounts",
            params={
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_class=ProductDiscountPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "ProductDiscountDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ProductDiscount":
        """Create ProductDiscount"""
        return self._client._post(
            endpoint=f"/{self._project_key}/product-discounts",
            params={"expand": expand},
            data_object=body,
            response_class=ProductDiscount,
            headers={"Content-Type": "application/json", **headers},
        )
