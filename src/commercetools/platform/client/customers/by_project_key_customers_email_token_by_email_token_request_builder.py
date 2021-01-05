# Generated file, please do not change!!!
import typing

from ...models.customer import Customer


class ByProjectKeyCustomersEmailTokenByEmailTokenRequestBuilder:

    _client: "Client"
    _project_key: str
    _email_token: str

    def __init__(
        self,
        projectKey: str,
        emailToken: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._email_token = emailToken
        self._client = client

    def get(
        self, *, expand: "str" = None, headers: typing.Dict[str, str] = None
    ) -> "Customer":
        """Get Customer by emailToken"""
        return self._client._get(
            endpoint=f"/{self._project_key}/customers/email-token={self._email_token}",
            params={"expand": expand},
            response_class=Customer,
            headers=headers,
        )
