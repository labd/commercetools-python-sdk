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


class ByProjectKeyCartsRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(self, projectKey: str, client: "Client"):
        self._project_key = projectKey
        self._client = client

    def replicate(self) -> ByProjectKeyCartsReplicateRequestBuilder:
        return ByProjectKeyCartsReplicateRequestBuilder(
            projectKey=self._project_key, client=self._client
        )

    def withCustomerId(
        self, customerId: str
    ) -> ByProjectKeyCartsCustomerIdByCustomerIdRequestBuilder:
        return ByProjectKeyCartsCustomerIdByCustomerIdRequestBuilder(
            customerId=customerId, projectKey=self._project_key, client=self._client
        )

    def withId(self, ID: str) -> ByProjectKeyCartsByIDRequestBuilder:
        return ByProjectKeyCartsByIDRequestBuilder(
            ID=ID, projectKey=self._project_key, client=self._client
        )

    def get(
        self,
        *,
        customer_id: "str" = None,
        expand: "str" = None,
        sort: "str" = None,
        limit: "int" = None,
        offset: "int" = None,
        with_total: "bool" = None,
        where: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "CartPagedQueryResponse":
        """Query carts
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/carts",
            params={
                "customerId": customer_id,
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_object=CartPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "CartDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Cart":
        """Creating a cart can fail with an InvalidOperation if the referenced shipping method in the
        CartDraft has a predicate which does not match the cart.
        
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/carts",
            params={"expand": expand},
            data_object=body,
            response_object=Cart,
            headers={"Content-Type": "application/json", **headers},
        )
