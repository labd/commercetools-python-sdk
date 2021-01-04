# Generated file, please do not change!!!
import typing

from ...models.customer import CustomerSignin, CustomerSignInResult


class ByProjectKeyInStoreKeyByStoreKeyLoginRequestBuilder:

    _client: "Client"
    _project_key: str
    _store_key: str

    def __init__(self, projectKey: str, storeKey: str, client: "Client"):
        self._project_key = projectKey
        self._store_key = storeKey
        self._client = client

    def post(
        self, body: "CustomerSignin", *, headers: typing.Dict[str, str] = None
    ) -> "CustomerSignInResult":
        """Authenticate Customer (Sign In) in store
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/login",
            params={},
            data_object=body,
            response_object=CustomerSignInResult,
            headers={"Content-Type": "application/json", **headers},
        )
