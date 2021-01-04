# Generated file, please do not change!!!
import typing

from ...models.common import Update
from ...models.type import Type


class ByProjectKeyTypesKeyByKeyRequestBuilder:

    _client: "Client"
    _project_key: str
    _key: str

    def __init__(self, projectKey: str, key: str, client: "Client"):
        self._project_key = projectKey
        self._key = key
        self._client = client

    def get(
        self, *, expand: "str" = None, headers: typing.Dict[str, str] = None
    ) -> "Type":
        """Get Type by key
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/types/key={self._key}",
            params={"expand": expand},
            response_object=Type,
            headers=headers,
        )

    def post(
        self,
        body: "Update",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Type":
        """Update Type by key
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/types/key={self._key}",
            params={"expand": expand},
            data_object=body,
            response_object=Type,
            headers={"Content-Type": "application/json", **headers},
        )

    def delete(
        self,
        *,
        version: "int",
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Type":
        """Delete Type by key
        """
        return self._client._delete(
            endpoint=f"/{self._project_key}/types/key={self._key}",
            params={"version": version, "expand": expand},
            response_object=Type,
            headers=headers,
        )
