# Generated file, please do not change!!!
import typing

from ...models.cart_discount import (
    CartDiscount,
    CartDiscountDraft,
    CartDiscountPagedQueryResponse,
)
from .by_project_key_cart_discounts_by_id_request_builder import (
    ByProjectKeyCartDiscountsByIDRequestBuilder,
)
from .by_project_key_cart_discounts_key_by_key_request_builder import (
    ByProjectKeyCartDiscountsKeyByKeyRequestBuilder,
)


class ByProjectKeyCartDiscountsRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def withKey(self, key: str) -> ByProjectKeyCartDiscountsKeyByKeyRequestBuilder:
        return ByProjectKeyCartDiscountsKeyByKeyRequestBuilder(
            key=key,
            projectKey=self._project_key,
            client=self._client,
        )

    def withId(self, ID: str) -> ByProjectKeyCartDiscountsByIDRequestBuilder:
        return ByProjectKeyCartDiscountsByIDRequestBuilder(
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
    ) -> "CartDiscountPagedQueryResponse":
        """Query cart-discounts"""
        return self._client._get(
            endpoint=f"/{self._project_key}/cart-discounts",
            params={
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_class=CartDiscountPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "CartDiscountDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "CartDiscount":
        """Create CartDiscount"""
        return self._client._post(
            endpoint=f"/{self._project_key}/cart-discounts",
            params={"expand": expand},
            data_object=body,
            response_class=CartDiscount,
            headers={"Content-Type": "application/json", **headers},
        )
