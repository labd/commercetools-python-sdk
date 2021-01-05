# Generated file, please do not change!!!
import typing

from ...models.order import Order, OrderFromCartDraft, OrderPagedQueryResponse
from ..edits.by_project_key_orders_edits_request_builder import (
    ByProjectKeyOrdersEditsRequestBuilder,
)
from ..import_.by_project_key_orders_import_request_builder import (
    ByProjectKeyOrdersImportRequestBuilder,
)
from .by_project_key_orders_by_id_request_builder import (
    ByProjectKeyOrdersByIDRequestBuilder,
)
from .by_project_key_orders_order_number_by_order_number_request_builder import (
    ByProjectKeyOrdersOrderNumberByOrderNumberRequestBuilder,
)


class ByProjectKeyOrdersRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def importOrder(self) -> ByProjectKeyOrdersImportRequestBuilder:
        return ByProjectKeyOrdersImportRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def withOrderNumber(
        self, orderNumber: str
    ) -> ByProjectKeyOrdersOrderNumberByOrderNumberRequestBuilder:
        return ByProjectKeyOrdersOrderNumberByOrderNumberRequestBuilder(
            orderNumber=orderNumber,
            projectKey=self._project_key,
            client=self._client,
        )

    def edits(self) -> ByProjectKeyOrdersEditsRequestBuilder:
        """OrderEdit are containers for financial changes after an Order has been placed."""
        return ByProjectKeyOrdersEditsRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def withId(self, ID: str) -> ByProjectKeyOrdersByIDRequestBuilder:
        return ByProjectKeyOrdersByIDRequestBuilder(
            ID=ID,
            projectKey=self._project_key,
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
        """Query orders"""
        return self._client._get(
            endpoint=f"/{self._project_key}/orders",
            params={
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_class=OrderPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "OrderFromCartDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Order":
        """Creates an order from a Cart.
        The cart must have a shipping address set before creating an order.
        When using the Platform TaxMode, the shipping address is used for tax calculation.

        """
        return self._client._post(
            endpoint=f"/{self._project_key}/orders",
            params={"expand": expand},
            data_object=body,
            response_class=Order,
            headers={"Content-Type": "application/json", **headers},
        )
