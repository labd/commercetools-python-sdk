# Generated file, please do not change!!!
import typing

from ...models.customer import Customer


class ByProjectKeyCustomersPasswordTokenByPasswordTokenRequestBuilder:

    _client: "Client"
    _project_key: str
    _password_token: str

    def __init__(
        self,
        projectKey: str,
        passwordToken: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._password_token = passwordToken
        self._client = client

    def get(
        self, *, expand: "str" = None, headers: typing.Dict[str, str] = None
    ) -> "Customer":
        """Get Customer by passwordToken"""
        return self._client._get(
            endpoint=f"/{self._project_key}/customers/password-token={self._password_token}",
            params={"expand": expand},
            response_class=Customer,
            headers=headers,
        )
