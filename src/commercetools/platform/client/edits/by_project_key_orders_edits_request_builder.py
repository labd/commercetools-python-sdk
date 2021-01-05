# Generated file, please do not change!!!
import typing

from ...models.order_edit import OrderEdit, OrderEditDraft, OrderEditPagedQueryResponse
from .by_project_key_orders_edits_by_id_request_builder import (
    ByProjectKeyOrdersEditsByIDRequestBuilder,
)
from .by_project_key_orders_edits_key_by_key_request_builder import (
    ByProjectKeyOrdersEditsKeyByKeyRequestBuilder,
)


class ByProjectKeyOrdersEditsRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def withKey(self, key: str) -> ByProjectKeyOrdersEditsKeyByKeyRequestBuilder:
        return ByProjectKeyOrdersEditsKeyByKeyRequestBuilder(
            key=key,
            projectKey=self._project_key,
            client=self._client,
        )

    def withId(self, ID: str) -> ByProjectKeyOrdersEditsByIDRequestBuilder:
        return ByProjectKeyOrdersEditsByIDRequestBuilder(
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
    ) -> "OrderEditPagedQueryResponse":
        """Query edits"""
        return self._client._get(
            endpoint=f"/{self._project_key}/orders/edits",
            params={
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_class=OrderEditPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "OrderEditDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "OrderEdit":
        """Create OrderEdit"""
        return self._client._post(
            endpoint=f"/{self._project_key}/orders/edits",
            params={"expand": expand},
            data_object=body,
            response_class=OrderEdit,
            headers={"Content-Type": "application/json", **headers},
        )
