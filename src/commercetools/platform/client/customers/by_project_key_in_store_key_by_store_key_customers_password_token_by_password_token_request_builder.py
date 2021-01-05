# Generated file, please do not change!!!
import typing

from ...models.customer import Customer


class ByProjectKeyInStoreKeyByStoreKeyCustomersPasswordTokenByPasswordTokenRequestBuilder:

    _client: "Client"
    _project_key: str
    _store_key: str
    _password_token: str

    def __init__(
        self,
        projectKey: str,
        storeKey: str,
        passwordToken: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._store_key = storeKey
        self._password_token = passwordToken
        self._client = client

    def get(
        self, *, expand: "str" = None, headers: typing.Dict[str, str] = None
    ) -> "Customer":
        """Get Customer by passwordToken"""
        return self._client._get(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/customers/password-token={self._password_token}",
            params={"expand": expand},
            response_class=Customer,
            headers=headers,
        )
