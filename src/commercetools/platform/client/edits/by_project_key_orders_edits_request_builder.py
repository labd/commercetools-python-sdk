# Generated file, please do not change!!!
import typing

from ...models.order_edit import OrderEdit, OrderEditDraft, OrderEditPagedQueryResponse
from .by_project_key_orders_edits_by_id_request_builder import (
    ByProjectKeyOrdersEditsByIDRequestBuilder,
)
from .by_project_key_orders_edits_key_by_key_request_builder import (
    ByProjectKeyOrdersEditsKeyByKeyRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyOrdersEditsRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def with_key(self, key: str) -> ByProjectKeyOrdersEditsKeyByKeyRequestBuilder:
        return ByProjectKeyOrdersEditsKeyByKeyRequestBuilder(
            key=key,
            project_key=self._project_key,
            client=self._client,
        )

    def with_id(self, id: str) -> ByProjectKeyOrdersEditsByIDRequestBuilder:
        return ByProjectKeyOrdersEditsByIDRequestBuilder(
            id=id,
            project_key=self._project_key,
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
    ) -> "OrderEditPagedQueryResponse":
        """Query edits"""
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
            endpoint=f"/{self._project_key}/orders/edits",
            params=params,
            response_class=OrderEditPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "OrderEditDraft",
        *,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "OrderEdit":
        """Create OrderEdit"""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/orders/edits",
            params={"expand": expand},
            data_object=body,
            response_class=OrderEdit,
            headers={"Content-Type": "application/json", **headers},
        )
