# Generated file, please do not change!!!
import typing

from ...models.customer import CustomerCreateEmailToken, CustomerToken


class ByProjectKeyInStoreKeyByStoreKeyCustomersEmailTokenRequestBuilder:

    _client: "Client"
    _project_key: str
    _store_key: str

    def __init__(self, projectKey: str, storeKey: str, client: "Client"):
        self._project_key = projectKey
        self._store_key = storeKey
        self._client = client

    def post(
        self, body: "CustomerCreateEmailToken", *, headers: typing.Dict[str, str] = None
    ) -> "CustomerToken":
        """Create a Token for verifying the Customer's Email in store
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/customers/email-token",
            params={},
            data_object=body,
            response_object=CustomerToken,
            headers={"Content-Type": "application/json", **headers},
        )
