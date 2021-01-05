# Generated file, please do not change!!!
import typing

from ...models.cart import Cart, CartDraft, CartPagedQueryResponse
from ..replicate.by_project_key_carts_replicate_request_builder import (
    ByProjectKeyCartsReplicateRequestBuilder,
)
from .by_project_key_carts_by_id_request_builder import (
    ByProjectKeyCartsByIDRequestBuilder,
)
from .by_project_key_carts_customer_id_by_customer_id_request_builder import (
    ByProjectKeyCartsCustomerIdByCustomerIdRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyCartsRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def replicate(self) -> ByProjectKeyCartsReplicateRequestBuilder:
        return ByProjectKeyCartsReplicateRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def with_customer_id(
        self, customer_id: str
    ) -> ByProjectKeyCartsCustomerIdByCustomerIdRequestBuilder:
        return ByProjectKeyCartsCustomerIdByCustomerIdRequestBuilder(
            customer_id=customer_id,
            project_key=self._project_key,
            client=self._client,
        )

    def with_id(self, id: str) -> ByProjectKeyCartsByIDRequestBuilder:
        return ByProjectKeyCartsByIDRequestBuilder(
            id=id,
            project_key=self._project_key,
            client=self._client,
        )

    def get(
        self,
        *,
        customer_id: str = None,
        expand: str = None,
        sort: str = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        where: str = None,
        predicate_var: typing.Dict[str, str] = None,
        headers: typing.Dict[str, str] = None,
    ) -> "CartPagedQueryResponse":
        """Query carts"""
        params = {
            "customerId": customer_id,
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
            endpoint=f"/{self._project_key}/carts",
            params=params,
            response_class=CartPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "CartDraft",
        *,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Cart":
        """Creating a cart can fail with an InvalidOperation if the referenced shipping method in the
        CartDraft has a predicate which does not match the cart.

        """
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/carts",
            params={"expand": expand},
            data_object=body,
            response_class=Cart,
            headers={"Content-Type": "application/json", **headers},
        )
