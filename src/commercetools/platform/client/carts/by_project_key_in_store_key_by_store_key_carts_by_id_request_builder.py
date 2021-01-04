# Generated file, please do not change!!!
import typing

from ...models.cart import Cart
from ...models.common import Update


class ByProjectKeyInStoreKeyByStoreKeyCartsByIDRequestBuilder:

    _client: "Client"
    _project_key: str
    _store_key: str
    _id: str

    def __init__(self, projectKey: str, storeKey: str, ID: str, client: "Client"):
        self._project_key = projectKey
        self._store_key = storeKey
        self._id = ID
        self._client = client

    def get(
        self, *, expand: "str" = None, headers: typing.Dict[str, str] = None
    ) -> "Cart":
        """Returns a cart by its ID from a specific Store. The {storeKey} path parameter maps to a Store's key.
        If the cart exists in the commercetools project but does not have the store field,
        or the store field references a different store, this method returns a ResourceNotFound error.
        The cart may not contain up-to-date prices, discounts etc.
        If you want to ensure they're up-to-date, send an Update request with the Recalculate update action instead.
        
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/carts/{self._id}",
            params={"expand": expand},
            response_object=Cart,
            headers=headers,
        )

    def post(
        self,
        body: "Update",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Cart":
        """Updates a cart in the store specified by {storeKey}. The {storeKey} path parameter maps to a Store's key.
        If the cart exists in the commercetools project but does not have the store field,
        or the store field references a different store, this method returns a ResourceNotFound error.
        
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/carts/{self._id}",
            params={"expand": expand},
            data_object=body,
            response_object=Cart,
            headers={"Content-Type": "application/json", **headers},
        )

    def delete(
        self,
        *,
        data_erasure: "bool" = None,
        version: "int",
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Cart":
        """Delete Cart by ID
        """
        return self._client._delete(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/carts/{self._id}",
            params={"dataErasure": data_erasure, "version": version, "expand": expand},
            response_object=Cart,
            headers=headers,
        )
