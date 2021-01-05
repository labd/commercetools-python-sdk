# Generated file, please do not change!!!
import typing

from ...models.inventory import (
    InventoryEntry,
    InventoryEntryDraft,
    InventoryPagedQueryResponse,
)
from .by_project_key_inventory_by_id_request_builder import (
    ByProjectKeyInventoryByIDRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyInventoryRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def with_id(self, id: str) -> ByProjectKeyInventoryByIDRequestBuilder:
        return ByProjectKeyInventoryByIDRequestBuilder(
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
    ) -> "InventoryPagedQueryResponse":
        """Query inventory"""
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
            endpoint=f"/{self._project_key}/inventory",
            params=params,
            response_class=InventoryPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "InventoryEntryDraft",
        *,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "InventoryEntry":
        """Create InventoryEntry"""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/inventory",
            params={"expand": expand},
            data_object=body,
            response_class=InventoryEntry,
            headers={"Content-Type": "application/json", **headers},
        )
