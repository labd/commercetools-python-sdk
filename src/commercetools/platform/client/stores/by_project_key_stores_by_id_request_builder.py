# Generated file, please do not change!!!
import typing

from ...models.common import Update
from ...models.store import Store

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyStoresByIDRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _id: str

    def __init__(
        self,
        project_key: str,
        id: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._id = id
        self._client = client

    def get(
        self, *, expand: str = None, headers: typing.Dict[str, str] = None
    ) -> "Store":
        """Get Store by ID"""
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/stores/{self._id}",
            params={"expand": expand},
            response_class=Store,
            headers=headers,
        )

    def post(
        self,
        body: "Update",
        *,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Store":
        """Update Store by ID"""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/stores/{self._id}",
            params={"expand": expand},
            data_object=body,
            response_class=Store,
            headers={"Content-Type": "application/json", **headers},
        )

    def delete(
        self, *, version: int, expand: str = None, headers: typing.Dict[str, str] = None
    ) -> "Store":
        """Delete Store by ID"""
        headers = {} if headers is None else headers
        return self._client._delete(
            endpoint=f"/{self._project_key}/stores/{self._id}",
            params={"version": version, "expand": expand},
            response_class=Store,
            headers=headers,
        )
