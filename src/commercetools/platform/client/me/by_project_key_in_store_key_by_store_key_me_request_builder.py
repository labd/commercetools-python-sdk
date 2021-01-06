# Generated file, please do not change!!!
import typing

from ..active_cart.by_project_key_in_store_key_by_store_key_me_active_cart_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyMeActiveCartRequestBuilder,
)
from ..carts.by_project_key_in_store_key_by_store_key_me_carts_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyMeCartsRequestBuilder,
)
from ..orders.by_project_key_in_store_key_by_store_key_me_orders_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyMeOrdersRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyInStoreKeyByStoreKeyMeRequestBuilder:

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

    def carts(self) -> ByProjectKeyInStoreKeyByStoreKeyMeCartsRequestBuilder:
        """A shopping cart holds product variants and can be ordered."""
        return ByProjectKeyInStoreKeyByStoreKeyMeCartsRequestBuilder(
            project_key=self._project_key,
            store_key=self._store_key,
            client=self._client,
        )

    def orders(self) -> ByProjectKeyInStoreKeyByStoreKeyMeOrdersRequestBuilder:
        """An order can be created from a order, usually after a checkout process has been completed."""
        return ByProjectKeyInStoreKeyByStoreKeyMeOrdersRequestBuilder(
            project_key=self._project_key,
            store_key=self._store_key,
            client=self._client,
        )

    def active_cart(self) -> ByProjectKeyInStoreKeyByStoreKeyMeActiveCartRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyMeActiveCartRequestBuilder(
            project_key=self._project_key,
            store_key=self._store_key,
            client=self._client,
        )
