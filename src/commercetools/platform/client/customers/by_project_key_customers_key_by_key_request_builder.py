# Generated file, please do not change!!!
import typing

from ...models.common import Update
from ...models.customer import Customer


class ByProjectKeyCustomersKeyByKeyRequestBuilder:

    _client: "Client"
    _project_key: str
    _key: str

    def __init__(self, projectKey: str, key: str, client: "Client"):
        self._project_key = projectKey
        self._key = key
        self._client = client

    def get(
        self, *, expand: "str" = None, headers: typing.Dict[str, str] = None
    ) -> "Customer":
        """Get Customer by key
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/customers/key={self._key}",
            params={"expand": expand},
            response_object=Customer,
            headers=headers,
        )

    def post(
        self,
        body: "Update",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Customer":
        """Update Customer by key
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/customers/key={self._key}",
            params={"expand": expand},
            data_object=body,
            response_object=Customer,
            headers={"Content-Type": "application/json", **headers},
        )

    def delete(
        self,
        *,
        data_erasure: "bool" = None,
        version: "int",
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Customer":
        """Delete Customer by key
        """
        return self._client._delete(
            endpoint=f"/{self._project_key}/customers/key={self._key}",
            params={"dataErasure": data_erasure, "version": version, "expand": expand},
            response_object=Customer,
            headers=headers,
        )
