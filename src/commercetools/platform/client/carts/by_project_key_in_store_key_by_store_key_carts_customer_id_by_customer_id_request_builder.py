# Generated file, please do not change!!!
import typing

from ...models.cart import Cart


class ByProjectKeyInStoreKeyByStoreKeyCartsCustomerIdByCustomerIdRequestBuilder:

    _client: "Client"
    _project_key: str
    _store_key: str
    _customer_id: str

    def __init__(
        self,
        projectKey: str,
        storeKey: str,
        customerId: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._store_key = storeKey
        self._customer_id = customerId
        self._client = client

    def get(
        self, *, expand: "str" = None, headers: typing.Dict[str, str] = None
    ) -> "Cart":
        """Retrieves the active cart of the customer that has been modified most recently in a specific Store.
        The {storeKey} path parameter maps to a Store's key.

        If the cart exists in the commercetools project but does not have the store field, or the store field
        references a different store, this method returns a ResourceNotFound error.

        The cart may not contain up-to-date prices, discounts etc. If you want to ensure they're up-to-date,
        send an Update request with the Recalculate update action instead.

        """
        return self._client._get(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/carts/customer-id={self._customer_id}",
            params={"expand": expand},
            response_class=Cart,
            headers=headers,
        )
