# Generated file, please do not change!!!
import typing

from ...models.cart import Cart
from ...models.common import Update


class ByProjectKeyInStoreKeyByStoreKeyMeCartsByIDRequestBuilder:

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
        """Get Cart by ID
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/me/carts/{self._id}",
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
        """Update Cart by ID
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/me/carts/{self._id}",
            params={"expand": expand},
            data_object=body,
            response_object=Cart,
            headers={"Content-Type": "application/json", **headers},
        )

    def delete(
        self,
        *,
        version: "int",
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Cart":
        """Delete Cart by ID
        """
        return self._client._delete(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/me/carts/{self._id}",
            params={"version": version, "expand": expand},
            response_object=Cart,
            headers=headers,
        )
