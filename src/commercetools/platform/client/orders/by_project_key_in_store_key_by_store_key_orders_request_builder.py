# Generated file, please do not change!!!
import typing

from ...models.order import Order, OrderFromCartDraft, OrderPagedQueryResponse
from .by_project_key_in_store_key_by_store_key_orders_by_id_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyOrdersByIDRequestBuilder,
)
from .by_project_key_in_store_key_by_store_key_orders_order_number_by_order_number_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyOrdersOrderNumberByOrderNumberRequestBuilder,
)


class ByProjectKeyInStoreKeyByStoreKeyOrdersRequestBuilder:

    _client: "Client"
    _project_key: str
    _store_key: str

    def __init__(self, projectKey: str, storeKey: str, client: "Client"):
        self._project_key = projectKey
        self._store_key = storeKey
        self._client = client

    def withOrderNumber(
        self, orderNumber: str
    ) -> ByProjectKeyInStoreKeyByStoreKeyOrdersOrderNumberByOrderNumberRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyOrdersOrderNumberByOrderNumberRequestBuilder(
            orderNumber=orderNumber,
            projectKey=self._project_key,
            storeKey=self._store_key,
            client=self._client,
        )

    def withId(
        self, ID: str
    ) -> ByProjectKeyInStoreKeyByStoreKeyOrdersByIDRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyOrdersByIDRequestBuilder(
            ID=ID,
            projectKey=self._project_key,
            storeKey=self._store_key,
            client=self._client,
        )

    def get(
        self,
        *,
        expand: "str" = None,
        sort: "str" = None,
        limit: "int" = None,
        offset: "int" = None,
        with_total: "bool" = None,
        where: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "OrderPagedQueryResponse":
        """Queries orders in a specific Store. The {storeKey} path parameter maps to a Store's key.
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/orders",
            params={
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_object=OrderPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "OrderFromCartDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Order":
        """Creates an order from a Cart from a specific Store. The {storeKey} path parameter maps to a Store's key.
        When using this endpoint the orders's store field is always set to the store specified in the path parameter.
        The cart must have a shipping address set before creating an order. When using the Platform TaxMode,
        the shipping address is used for tax calculation.
        
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/orders",
            params={"expand": expand},
            data_object=body,
            response_object=Order,
            headers={"Content-Type": "application/json", **headers},
        )
