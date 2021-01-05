# Generated file, please do not change!!!
import typing

from ..carts.by_project_key_in_store_key_by_store_key_carts_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyCartsRequestBuilder,
)
from ..customers.by_project_key_in_store_key_by_store_key_customers_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyCustomersRequestBuilder,
)
from ..login.by_project_key_in_store_key_by_store_key_login_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyLoginRequestBuilder,
)
from ..me.by_project_key_in_store_key_by_store_key_me_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyMeRequestBuilder,
)
from ..orders.by_project_key_in_store_key_by_store_key_orders_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyOrdersRequestBuilder,
)
from ..shipping_methods.by_project_key_in_store_key_by_store_key_shipping_methods_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyShippingMethodsRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyInStoreKeyByStoreKeyRequestBuilder:

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

    def carts(self) -> ByProjectKeyInStoreKeyByStoreKeyCartsRequestBuilder:
        """A shopping cart holds product variants and can be ordered."""
        return ByProjectKeyInStoreKeyByStoreKeyCartsRequestBuilder(
            project_key=self._project_key,
            store_key=self._store_key,
            client=self._client,
        )

    def orders(self) -> ByProjectKeyInStoreKeyByStoreKeyOrdersRequestBuilder:
        """An order can be created from a cart, usually after a checkout process has been completed."""
        return ByProjectKeyInStoreKeyByStoreKeyOrdersRequestBuilder(
            project_key=self._project_key,
            store_key=self._store_key,
            client=self._client,
        )

    def me(self) -> ByProjectKeyInStoreKeyByStoreKeyMeRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyMeRequestBuilder(
            project_key=self._project_key,
            store_key=self._store_key,
            client=self._client,
        )

    def customers(self) -> ByProjectKeyInStoreKeyByStoreKeyCustomersRequestBuilder:
        """A customer is a person purchasing products. customers, Orders,
        Comments and Reviews can be associated to a customer.

        """
        return ByProjectKeyInStoreKeyByStoreKeyCustomersRequestBuilder(
            project_key=self._project_key,
            store_key=self._store_key,
            client=self._client,
        )

    def login(self) -> ByProjectKeyInStoreKeyByStoreKeyLoginRequestBuilder:
        """Retrieves the authenticated customer."""
        return ByProjectKeyInStoreKeyByStoreKeyLoginRequestBuilder(
            project_key=self._project_key,
            store_key=self._store_key,
            client=self._client,
        )

    def shipping_methods(
        self,
    ) -> ByProjectKeyInStoreKeyByStoreKeyShippingMethodsRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyShippingMethodsRequestBuilder(
            project_key=self._project_key,
            store_key=self._store_key,
            client=self._client,
        )
