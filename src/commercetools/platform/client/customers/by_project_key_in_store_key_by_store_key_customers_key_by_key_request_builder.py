# Generated file, please do not change!!!
import typing

from ...models.common import Update
from ...models.customer import Customer

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyInStoreKeyByStoreKeyCustomersKeyByKeyRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _store_key: str
    _key: str

    def __init__(
        self,
        project_key: str,
        store_key: str,
        key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._store_key = store_key
        self._key = key
        self._client = client

    def get(
        self, *, expand: str = None, headers: typing.Dict[str, str] = None
    ) -> "Customer":
        """Returns a customer by its Key from a specific Store. The {storeKey} path parameter maps to a Store's key.
        It also considers customers that do not have the stores field.
        If the customer exists in the commercetools project but the stores field references different stores,
        this method returns a ResourceNotFound error.

        """
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/customers/key={self._key}",
            params={"expand": expand},
            response_class=Customer,
            headers=headers,
        )

    def post(
        self,
        body: "Update",
        *,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Customer":
        """If the customer exists in the commercetools project but the stores field references a different store,
        this method returns a ResourceNotFound error.

        """
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/customers/key={self._key}",
            params={"expand": expand},
            data_object=body,
            response_class=Customer,
            headers={"Content-Type": "application/json", **headers},
        )

    def delete(
        self,
        *,
        data_erasure: bool = None,
        version: int,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Customer":
        """Delete Customer by key"""
        headers = {} if headers is None else headers
        return self._client._delete(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/customers/key={self._key}",
            params={"dataErasure": data_erasure, "version": version, "expand": expand},
            response_class=Customer,
            headers=headers,
        )
