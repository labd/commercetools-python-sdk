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

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyProductDiscountsRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def matching(self) -> ByProjectKeyProductDiscountsMatchingRequestBuilder:
        return ByProjectKeyProductDiscountsMatchingRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def with_key(self, key: str) -> ByProjectKeyProductDiscountsKeyByKeyRequestBuilder:
        return ByProjectKeyProductDiscountsKeyByKeyRequestBuilder(
            key=key,
            project_key=self._project_key,
            client=self._client,
        )

    def with_id(self, id: str) -> ByProjectKeyProductDiscountsByIDRequestBuilder:
        return ByProjectKeyProductDiscountsByIDRequestBuilder(
            id=id,
            project_key=self._project_key,
            client=self._client,
        )

    def get(
        self,
        *,
        expand: str = None,
        sort: str = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        where: str = None,
        predicate_var: typing.Dict[str, str] = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ProductDiscountPagedQueryResponse":
        """Query product-discounts"""
        params = {
            "expand": expand,
            "sort": sort,
            "limit": limit,
            "offset": offset,
            "withTotal": with_total,
            "where": where,
        }
        predicate_var and params.update(
            {f"var.{k}": v for k, v in predicate_var.items()}
        )
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/product-discounts",
            params=params,
            response_class=ProductDiscountPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "ProductDiscountDraft",
        *,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ProductDiscount":
        """Create ProductDiscount"""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/product-discounts",
            params={"expand": expand},
            data_object=body,
            response_class=ProductDiscount,
            headers={"Content-Type": "application/json", **headers},
        )
