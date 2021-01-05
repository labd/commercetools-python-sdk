# Generated file, please do not change!!!
import typing

from ...models.customer import CustomerCreatePasswordResetToken, CustomerToken

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyInStoreKeyByStoreKeyCustomersPasswordTokenRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _store_key: str

    def __init__(
        self,
        project_key: str,
        store_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._store_key = store_key
        self._client = client

    def post(
        self,
        body: "CustomerCreatePasswordResetToken",
        *,
        headers: typing.Dict[str, str] = None,
    ) -> "CustomerToken":
        """The token value is used to reset the password of the customer with the given email. The token is
        valid only for 10 minutes.

        """
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/customers/password-token",
            params={},
            data_object=body,
            response_class=CustomerToken,
            headers={"Content-Type": "application/json", **headers},
        )
