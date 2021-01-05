# Generated file, please do not change!!!
import typing

from ..matching_cart.by_project_key_in_store_key_by_store_key_shipping_methods_matching_cart_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyShippingMethodsMatchingCartRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyInStoreKeyByStoreKeyShippingMethodsRequestBuilder:

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

    def matching_cart(
        self,
    ) -> ByProjectKeyInStoreKeyByStoreKeyShippingMethodsMatchingCartRequestBuilder:
        """Get ShippingMethods for a cart in a store"""
        return (
            ByProjectKeyInStoreKeyByStoreKeyShippingMethodsMatchingCartRequestBuilder(
                project_key=self._project_key,
                store_key=self._store_key,
                client=self._client,
            )
        )
