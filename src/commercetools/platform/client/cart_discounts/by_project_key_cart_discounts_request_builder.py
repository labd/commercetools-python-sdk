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

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyCartDiscountsRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def with_key(self, key: str) -> ByProjectKeyCartDiscountsKeyByKeyRequestBuilder:
        return ByProjectKeyCartDiscountsKeyByKeyRequestBuilder(
            key=key,
            project_key=self._project_key,
            client=self._client,
        )

    def with_id(self, id: str) -> ByProjectKeyCartDiscountsByIDRequestBuilder:
        return ByProjectKeyCartDiscountsByIDRequestBuilder(
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
    ) -> "CartDiscountPagedQueryResponse":
        """Query cart-discounts"""
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
            endpoint=f"/{self._project_key}/cart-discounts",
            params=params,
            response_class=CartDiscountPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "CartDiscountDraft",
        *,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "CartDiscount":
        """Create CartDiscount"""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/cart-discounts",
            params={"expand": expand},
            data_object=body,
            response_class=CartDiscount,
            headers={"Content-Type": "application/json", **headers},
        )
