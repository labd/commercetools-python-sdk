# Generated file, please do not change!!!
import typing

from ...models.me import MyOrderFromCartDraft
from ...models.order import Order, OrderPagedQueryResponse
from .by_project_key_in_store_key_by_store_key_me_orders_by_id_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyMeOrdersByIDRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyInStoreKeyByStoreKeyMeOrdersRequestBuilder:

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

    def with_id(
        self, id: str
    ) -> ByProjectKeyInStoreKeyByStoreKeyMeOrdersByIDRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyMeOrdersByIDRequestBuilder(
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
        return self._client._get(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/me/orders",
            params=params,
            response_class=OrderPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "MyOrderFromCartDraft",
        *,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Order":
        """Create Order"""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/me/orders",
            params={"expand": expand},
            data_object=body,
            response_class=Order,
            headers={"Content-Type": "application/json", **headers},
        )
