# Generated file, please do not change!!!
import typing

from ...models.common import Update
from ...models.order import Order

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyInStoreKeyByStoreKeyOrdersByIDRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _store_key: str
    _id: str

    def __init__(
        self,
        project_key: str,
        store_key: str,
        id: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._store_key = store_key
        self._id = id
        self._client = client

    def get(
        self, *, expand: str = None, headers: typing.Dict[str, str] = None
    ) -> "Order":
        """Returns an order by its ID from a specific Store. The {storeKey} path parameter maps to a Store's key.
        If the order exists in the commercetools project but does not have the store field,
        or the store field references a different store, this method returns a ResourceNotFound error.

        """
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/orders/{self._id}",
            params={"expand": expand},
            response_class=Order,
            headers=headers,
        )

    def post(
        self,
        body: "Update",
        *,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Order":
        """Updates an order in the store specified by {storeKey}. The {storeKey} path parameter maps to a Store's key.
        If the order exists in the commercetools project but does not have the store field,
        or the store field references a different store, this method returns a ResourceNotFound error.

        """
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/orders/{self._id}",
            params={"expand": expand},
            data_object=body,
            response_class=Order,
            headers={"Content-Type": "application/json", **headers},
        )

    def delete(
        self,
        *,
        data_erasure: bool = None,
        version: int,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Order":
        """Delete Order by ID"""
        headers = {} if headers is None else headers
        return self._client._delete(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/orders/{self._id}",
            params={"dataErasure": data_erasure, "version": version, "expand": expand},
            response_class=Order,
            headers=headers,
        )
