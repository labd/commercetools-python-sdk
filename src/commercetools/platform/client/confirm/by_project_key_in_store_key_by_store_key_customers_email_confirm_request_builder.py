# Generated file, please do not change!!!
import typing

from ...models.customer import CustomerEmailVerify


class ByProjectKeyInStoreKeyByStoreKeyCustomersEmailConfirmRequestBuilder:

    _client: "Client"
    _project_key: str
    _store_key: str

    def __init__(self, projectKey: str, storeKey: str, client: "Client"):
        self._project_key = projectKey
        self._store_key = storeKey
        self._client = client

    def post(
        self, body: "CustomerEmailVerify", *, headers: typing.Dict[str, str] = None
    ) -> None:
        """Verifies customer's email using a token.
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/customers/email/confirm",
            params={},
            data_object=body,
            response_object=None,
            headers={"Content-Type": "application/json", **headers},
        )
