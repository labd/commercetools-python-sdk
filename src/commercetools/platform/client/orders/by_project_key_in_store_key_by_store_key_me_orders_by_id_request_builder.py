# Generated file, please do not change!!!
import typing

from ...models.order import Order


class ByProjectKeyInStoreKeyByStoreKeyMeOrdersByIDRequestBuilder:

    _client: "Client"
    _project_key: str
    _store_key: str
    _id: str

    def __init__(
        self,
        projectKey: str,
        storeKey: str,
        ID: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._store_key = storeKey
        self._id = ID
        self._client = client

    def get(
        self, *, expand: "str" = None, headers: typing.Dict[str, str] = None
    ) -> "Order":
        """Get Order by ID"""
        return self._client._get(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/me/orders/{self._id}",
            params={"expand": expand},
            response_class=Order,
            headers=headers,
        )
