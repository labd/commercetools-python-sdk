# Generated file, please do not change!!!
import typing

from ...models.common import Update
from ...models.payment import Payment


class ByProjectKeyPaymentsKeyByKeyRequestBuilder:

    _client: "Client"
    _project_key: str
    _key: str

    def __init__(self, projectKey: str, key: str, client: "Client"):
        self._project_key = projectKey
        self._key = key
        self._client = client

    def get(
        self, *, expand: "str" = None, headers: typing.Dict[str, str] = None
    ) -> "Payment":
        """Get Payment by key
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/payments/key={self._key}",
            params={"expand": expand},
            response_object=Payment,
            headers=headers,
        )

    def post(
        self,
        body: "Update",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Payment":
        """Update Payment by key
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/payments/key={self._key}",
            params={"expand": expand},
            data_object=body,
            response_object=Payment,
            headers={"Content-Type": "application/json", **headers},
        )

    def delete(
        self,
        *,
        data_erasure: "bool" = None,
        version: "int",
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Payment":
        """Delete Payment by key
        """
        return self._client._delete(
            endpoint=f"/{self._project_key}/payments/key={self._key}",
            params={"dataErasure": data_erasure, "version": version, "expand": expand},
            response_object=Payment,
            headers=headers,
        )
