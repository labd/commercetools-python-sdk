# Generated file, please do not change!!!
import typing

from ...models.common import Update
from ...models.extension import Extension

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyExtensionsByIDRequestBuilder:

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
    ) -> "Extension":
        """Retrieves the representation of an extension by its id."""
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/extensions/{self._id}",
            params={"expand": expand},
            response_class=Extension,
            headers=headers,
        )

    def post(
        self,
        body: "Update",
        *,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Extension":
        """Update Extension by ID"""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/extensions/{self._id}",
            params={"expand": expand},
            data_object=body,
            response_class=Extension,
            headers={"Content-Type": "application/json", **headers},
        )

    def delete(
        self, *, version: int, expand: str = None, headers: typing.Dict[str, str] = None
    ) -> "Extension":
        """Delete Extension by ID"""
        headers = {} if headers is None else headers
        return self._client._delete(
            endpoint=f"/{self._project_key}/extensions/{self._id}",
            params={"version": version, "expand": expand},
            response_class=Extension,
            headers=headers,
        )
