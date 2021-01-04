# Generated file, please do not change!!!
import typing

from ...models.cart import Cart, CartDraft
from .by_project_key_in_store_key_by_store_key_carts_by_id_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyCartsByIDRequestBuilder,
)
from .by_project_key_in_store_key_by_store_key_carts_customer_id_by_customer_id_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyCartsCustomerIdByCustomerIdRequestBuilder,
)


class ByProjectKeyInStoreKeyByStoreKeyCartsRequestBuilder:

    _client: "Client"
    _project_key: str
    _store_key: str

    def __init__(self, projectKey: str, storeKey: str, client: "Client"):
        self._project_key = projectKey
        self._store_key = storeKey
        self._client = client

    def withCustomerId(
        self, customerId: str
    ) -> ByProjectKeyInStoreKeyByStoreKeyCartsCustomerIdByCustomerIdRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyCartsCustomerIdByCustomerIdRequestBuilder(
            customerId=customerId,
            projectKey=self._project_key,
            storeKey=self._store_key,
            client=self._client,
        )

    def withId(
        self, ID: str
    ) -> ByProjectKeyInStoreKeyByStoreKeyCartsByIDRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyCartsByIDRequestBuilder(
            ID=ID,
            projectKey=self._project_key,
            storeKey=self._store_key,
            client=self._client,
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
    ) -> "any":
        """Queries carts in a specific Store. The {storeKey} path parameter maps to a Store's key.
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/carts",
            params={
                "customerId": customer_id,
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_object=any,
            headers=headers,
        )

    def post(
        self,
        body: "CartDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Cart":
        """Creates a cart in the store specified by {storeKey}. The {storeKey} path parameter maps to a Store's key.
        When using this endpoint the cart's store field is always set to the store specified in the path parameter.
        Creating a cart can fail with an InvalidOperation if the referenced shipping method
        in the CartDraft has a predicate which does not match the cart.
        
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/carts",
            params={"expand": expand},
            data_object=body,
            response_object=Cart,
            headers={"Content-Type": "application/json", **headers},
        )
