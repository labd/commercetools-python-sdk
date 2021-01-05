# Generated file, please do not change!!!
import typing

from ...models.cart import Cart


class ByProjectKeyInStoreKeyByStoreKeyMeActiveCartRequestBuilder:

    _client: "Client"
    _project_key: str
    _store_key: str

    def __init__(
        self,
        projectKey: str,
        storeKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._store_key = storeKey
        self._client = client

    def get(self, *, headers: typing.Dict[str, str] = None) -> "Cart":
        return self._client._get(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/me/active-cart",
            params={},
            response_class=Cart,
            headers=headers,
        )
