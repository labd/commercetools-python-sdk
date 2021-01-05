# Generated file, please do not change!!!
import typing

from ...models.order import Order

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyInStoreKeyByStoreKeyMeOrdersByIDRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _store_key: str
    _id: str

    def __init__(
        self,
        project_key: str,
        store_key: str,
        id: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._store_key = store_key
        self._id = id
        self._client = client

    def get(
        self, *, expand: str = None, headers: typing.Dict[str, str] = None
    ) -> "Order":
        """Get Order by ID"""
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/me/orders/{self._id}",
            params={"expand": expand},
            response_class=Order,
            headers=headers,
        )
