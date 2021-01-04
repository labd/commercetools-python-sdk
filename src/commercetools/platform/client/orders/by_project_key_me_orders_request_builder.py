# Generated file, please do not change!!!
import typing

from ...models.me import MyOrder, MyOrderFromCartDraft
from ...models.order import OrderPagedQueryResponse
from .by_project_key_me_orders_by_id_request_builder import (
    ByProjectKeyMeOrdersByIDRequestBuilder,
)


class ByProjectKeyMeOrdersRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(self, projectKey: str, client: "Client"):
        self._project_key = projectKey
        self._client = client

    def withId(self, ID: str) -> ByProjectKeyMeOrdersByIDRequestBuilder:
        return ByProjectKeyMeOrdersByIDRequestBuilder(
            ID=ID, projectKey=self._project_key, client=self._client
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
        """Query orders
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/me/orders",
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
        body: "MyOrderFromCartDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "MyOrder":
        """Create MyOrder
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/me/orders",
            params={"expand": expand},
            data_object=body,
            response_object=MyOrder,
            headers={"Content-Type": "application/json", **headers},
        )
