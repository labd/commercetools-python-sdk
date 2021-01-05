# Generated file, please do not change!!!
import typing

from ...models.common import Update
from ...models.me import MyPayment


class ByProjectKeyMePaymentsByIDRequestBuilder:

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
    ) -> "MyPayment":
        """Get MyPayment by ID"""
        return self._client._get(
            endpoint=f"/{self._project_key}/me/payments/{self._id}",
            params={"expand": expand},
            response_class=MyPayment,
            headers=headers,
        )

    def post(
        self,
        body: "Update",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "MyPayment":
        """Update MyPayment by ID"""
        return self._client._post(
            endpoint=f"/{self._project_key}/me/payments/{self._id}",
            params={"expand": expand},
            data_object=body,
            response_class=MyPayment,
            headers={"Content-Type": "application/json", **headers},
        )

    def delete(
        self,
        *,
        version: "int",
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "MyPayment":
        """Delete MyPayment by ID"""
        return self._client._delete(
            endpoint=f"/{self._project_key}/me/payments/{self._id}",
            params={"version": version, "expand": expand},
            response_class=MyPayment,
            headers=headers,
        )
