# Generated file, please do not change!!!
import typing

from ...models.customer import Customer
from ...models.error import ErrorResponse

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyInStoreKeyByStoreKeyCustomersEmailTokenByEmailTokenRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _store_key: str
    _email_token: str

    def __init__(
        self,
        project_key: str,
        store_key: str,
        email_token: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._store_key = store_key
        self._email_token = email_token
        self._client = client

    def get(
        self,
        *,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["Customer"]:
        """Get Customer by emailToken"""
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/customers/email-token={self._email_token}",
            params={"expand": expand},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return Customer.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        raise ValueError("Unhandled status code %s", response.status_code)
