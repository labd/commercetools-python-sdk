# Generated file, please do not change!!!
import typing

from ...models.cart import Cart, CartDraft
from .by_project_key_in_store_key_by_store_key_carts_by_id_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyCartsByIDRequestBuilder,
)
from .by_project_key_in_store_key_by_store_key_carts_customer_id_by_customer_id_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyCartsCustomerIdByCustomerIdRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyInStoreKeyByStoreKeyCartsRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _store_key: str

    def __init__(
        self,
        project_key: str,
        store_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._store_key = store_key
        self._client = client

    def with_customer_id(
        self, customer_id: str
    ) -> ByProjectKeyInStoreKeyByStoreKeyCartsCustomerIdByCustomerIdRequestBuilder:
        return (
            ByProjectKeyInStoreKeyByStoreKeyCartsCustomerIdByCustomerIdRequestBuilder(
                customer_id=customer_id,
                project_key=self._project_key,
                store_key=self._store_key,
                client=self._client,
            )
        )

    def with_id(
        self, id: str
    ) -> ByProjectKeyInStoreKeyByStoreKeyCartsByIDRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyCartsByIDRequestBuilder(
            id=id,
            project_key=self._project_key,
            store_key=self._store_key,
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
    ) -> object:
        """Queries carts in a specific Store. The {storeKey} path parameter maps to a Store's key."""
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
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/carts",
            params=params,
            response_class=object,
            headers=headers,
        )

    def post(
        self,
        body: "CartDraft",
        *,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Cart":
        """Creates a cart in the store specified by {storeKey}. The {storeKey} path parameter maps to a Store's key.
        When using this endpoint the cart's store field is always set to the store specified in the path parameter.
        Creating a cart can fail with an InvalidOperation if the referenced shipping method
        in the CartDraft has a predicate which does not match the cart.

        """
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/carts",
            params={"expand": expand},
            data_object=body,
            response_class=Cart,
            headers={"Content-Type": "application/json", **headers},
        )
