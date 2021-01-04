# Generated file, please do not change!!!
import typing

from ..matching_cart.by_project_key_in_store_key_by_store_key_shipping_methods_matching_cart_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyShippingMethodsMatchingCartRequestBuilder,
)


class ByProjectKeyInStoreKeyByStoreKeyShippingMethodsRequestBuilder:

    _client: "Client"
    _project_key: str
    _store_key: str

    def __init__(self, projectKey: str, storeKey: str, client: "Client"):
        self._project_key = projectKey
        self._store_key = storeKey
        self._client = client

    def matchingCart(
        self
    ) -> ByProjectKeyInStoreKeyByStoreKeyShippingMethodsMatchingCartRequestBuilder:
        """Get ShippingMethods for a cart in a store
        """
        return ByProjectKeyInStoreKeyByStoreKeyShippingMethodsMatchingCartRequestBuilder(
            projectKey=self._project_key, storeKey=self._store_key, client=self._client
        )
