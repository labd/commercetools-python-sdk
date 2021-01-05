# Generated file, please do not change!!!
import typing

from ...models.customer import Customer


class ByProjectKeyInStoreKeyByStoreKeyCustomersEmailTokenByEmailTokenRequestBuilder:

    _client: "Client"
    _project_key: str
    _store_key: str
    _email_token: str

    def __init__(
        self,
        projectKey: str,
        storeKey: str,
        emailToken: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._store_key = storeKey
        self._email_token = emailToken
        self._client = client

    def get(
        self, *, expand: "str" = None, headers: typing.Dict[str, str] = None
    ) -> "Customer":
        """Get Customer by emailToken"""
        return self._client._get(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/customers/email-token={self._email_token}",
            params={"expand": expand},
            response_class=Customer,
            headers=headers,
        )
