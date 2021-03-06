# Generated file, please do not change!!!
import typing
import warnings

from ...models.error import ErrorResponse
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

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyOrdersRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def import_order(self) -> ByProjectKeyOrdersImportRequestBuilder:
        return ByProjectKeyOrdersImportRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def with_order_number(
        self, order_number: str
    ) -> ByProjectKeyOrdersOrderNumberByOrderNumberRequestBuilder:
        return ByProjectKeyOrdersOrderNumberByOrderNumberRequestBuilder(
            order_number=order_number,
            project_key=self._project_key,
            client=self._client,
        )

    def edits(self) -> ByProjectKeyOrdersEditsRequestBuilder:
        """OrderEdit are containers for financial changes after an Order has been placed."""
        return ByProjectKeyOrdersEditsRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def with_id(self, id: str) -> ByProjectKeyOrdersByIDRequestBuilder:
        return ByProjectKeyOrdersByIDRequestBuilder(
            id=id,
            project_key=self._project_key,
            client=self._client,
        )

    def get(
        self,
        *,
        expand: typing.List["str"] = None,
        sort: typing.List["str"] = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        where: typing.List["str"] = None,
        predicate_var: typing.Dict[str, typing.List["str"]] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["OrderPagedQueryResponse"]:
        """Query orders"""
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
        response = self._client._get(
            endpoint=f"/{self._project_key}/orders",
            params=params,
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return OrderPagedQueryResponse.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        warnings.warn("Unhandled status code %d" % response.status_code)

    def post(
        self,
        body: "OrderFromCartDraft",
        *,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["Order"]:
        """Creates an order from a Cart.
        The cart must have a shipping address set before creating an order.
        When using the Platform TaxMode, the shipping address is used for tax calculation.

        """
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/orders",
            params={"expand": expand},
            json=body.serialize(),
            headers={"Content-Type": "application/json", **headers},
            options=options,
        )
        if response.status_code in (201, 200):
            return Order.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        elif response.status_code == 200:
            return None
        warnings.warn("Unhandled status code %d" % response.status_code)
