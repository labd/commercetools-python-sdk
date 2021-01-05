# Generated file, please do not change!!!
import typing

from ...models.category import Category
from ...models.common import Update

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyCategoriesKeyByKeyRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _key: str

    def __init__(
        self,
        project_key: str,
        key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._key = key
        self._client = client

    def get(
        self, *, expand: str = None, headers: typing.Dict[str, str] = None
    ) -> "Category":
        """Get Category by key"""
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/categories/key={self._key}",
            params={"expand": expand},
            response_class=Category,
            headers=headers,
        )

    def post(
        self,
        body: "Update",
        *,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Category":
        """Update Category by key"""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/categories/key={self._key}",
            params={"expand": expand},
            data_object=body,
            response_class=Category,
            headers={"Content-Type": "application/json", **headers},
        )

    def delete(
        self, *, version: int, expand: str = None, headers: typing.Dict[str, str] = None
    ) -> "Category":
        """Delete Category by key"""
        headers = {} if headers is None else headers
        return self._client._delete(
            endpoint=f"/{self._project_key}/categories/key={self._key}",
            params={"version": version, "expand": expand},
            response_class=Category,
            headers=headers,
        )
