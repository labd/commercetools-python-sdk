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


class ByProjectKeyInStoreKeyByStoreKeyMeRequestBuilder:

    _client: "Client"
    _project_key: str
    _store_key: str

    def __init__(self, projectKey: str, storeKey: str, client: "Client"):
        self._project_key = projectKey
        self._store_key = storeKey
        self._client = client

    def carts(self) -> ByProjectKeyInStoreKeyByStoreKeyMeCartsRequestBuilder:
        """A shopping cart holds product variants and can be ordered.
        """
        return ByProjectKeyInStoreKeyByStoreKeyMeCartsRequestBuilder(
            projectKey=self._project_key, storeKey=self._store_key, client=self._client
        )

    def orders(self) -> ByProjectKeyInStoreKeyByStoreKeyMeOrdersRequestBuilder:
        """An order can be created from a order, usually after a checkout process has been completed.
        """
        return ByProjectKeyInStoreKeyByStoreKeyMeOrdersRequestBuilder(
            projectKey=self._project_key, storeKey=self._store_key, client=self._client
        )

    def activeCart(self) -> ByProjectKeyInStoreKeyByStoreKeyMeActiveCartRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyMeActiveCartRequestBuilder(
            projectKey=self._project_key, storeKey=self._store_key, client=self._client
        )
