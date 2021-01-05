# Generated file, please do not change!!!
import typing

from ...models.common import Update
from ...models.extension import Extension


class ByProjectKeyExtensionsByIDRequestBuilder:

    _client: "Client"
    _project_key: str
    _id: str

    def __init__(
        self,
        projectKey: str,
        ID: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._id = ID
        self._client = client

    def get(
        self, *, expand: "str" = None, headers: typing.Dict[str, str] = None
    ) -> "Extension":
        """Retrieves the representation of an extension by its id."""
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
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Extension":
        """Update Extension by ID"""
        return self._client._post(
            endpoint=f"/{self._project_key}/extensions/{self._id}",
            params={"expand": expand},
            data_object=body,
            response_class=Extension,
            headers={"Content-Type": "application/json", **headers},
        )

    def delete(
        self,
        *,
        version: "int",
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Extension":
        """Delete Extension by ID"""
        return self._client._delete(
            endpoint=f"/{self._project_key}/extensions/{self._id}",
            params={"version": version, "expand": expand},
            response_class=Extension,
            headers=headers,
        )
