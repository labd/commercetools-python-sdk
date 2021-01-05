# Generated file, please do not change!!!
import typing

from ...models.customer import Customer

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyInStoreKeyByStoreKeyCustomersPasswordTokenByPasswordTokenRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _store_key: str
    _password_token: str

    def __init__(
        self,
        project_key: str,
        store_key: str,
        password_token: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._store_key = store_key
        self._password_token = password_token
        self._client = client

    def get(
        self, *, expand: str = None, headers: typing.Dict[str, str] = None
    ) -> "Customer":
        """Get Customer by passwordToken"""
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/customers/password-token={self._password_token}",
            params={"expand": expand},
            response_class=Customer,
            headers=headers,
        )
