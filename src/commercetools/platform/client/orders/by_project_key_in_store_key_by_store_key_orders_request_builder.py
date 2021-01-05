# Generated file, please do not change!!!
import typing

from ...models.order import Order, OrderFromCartDraft, OrderPagedQueryResponse
from .by_project_key_in_store_key_by_store_key_orders_by_id_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyOrdersByIDRequestBuilder,
)
from .by_project_key_in_store_key_by_store_key_orders_order_number_by_order_number_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyOrdersOrderNumberByOrderNumberRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyInStoreKeyByStoreKeyOrdersRequestBuilder:

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

    def with_order_number(
        self, order_number: str
    ) -> ByProjectKeyInStoreKeyByStoreKeyOrdersOrderNumberByOrderNumberRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyOrdersOrderNumberByOrderNumberRequestBuilder(
            order_number=order_number,
            project_key=self._project_key,
            store_key=self._store_key,
            client=self._client,
        )

    def with_id(
        self, id: str
    ) -> ByProjectKeyInStoreKeyByStoreKeyOrdersByIDRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyOrdersByIDRequestBuilder(
            id=id,
            project_key=self._project_key,
            store_key=self._store_key,
            client=self._client,
        )

    def get(
        self,
        *,
        expand: str = None,
        sort: str = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        where: str = None,
        predicate_var: typing.Dict[str, str] = None,
        headers: typing.Dict[str, str] = None,
    ) -> "OrderPagedQueryResponse":
        """Queries orders in a specific Store. The {storeKey} path parameter maps to a Store's key."""
        params = {
            "expand": expand,
            "sort": sort,
            "limit": limit,
            "offset": offset,
            "withTotal": with_total,
            "where": where,
        }
        predicate_var and params.update(
            {f"var.{k}": v for k, v in predicate_var.items()}
        )
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/orders",
            params=params,
            response_class=OrderPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "OrderFromCartDraft",
        *,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Order":
        """Creates an order from a Cart from a specific Store. The {storeKey} path parameter maps to a Store's key.
        When using this endpoint the orders's store field is always set to the store specified in the path parameter.
        The cart must have a shipping address set before creating an order. When using the Platform TaxMode,
        the shipping address is used for tax calculation.

        """
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/orders",
            params={"expand": expand},
            data_object=body,
            response_class=Order,
            headers={"Content-Type": "application/json", **headers},
        )
