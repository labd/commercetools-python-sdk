# Generated file, please do not change!!!
import typing

from ...models.customer import Customer

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyCustomersEmailTokenByEmailTokenRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _email_token: str

    def __init__(
        self,
        project_key: str,
        email_token: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._email_token = email_token
        self._client = client

    def get(
        self, *, expand: str = None, headers: typing.Dict[str, str] = None
    ) -> "Customer":
        """Get Customer by emailToken"""
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/customers/email-token={self._email_token}",
            params={"expand": expand},
            response_class=Customer,
            headers=headers,
        )
