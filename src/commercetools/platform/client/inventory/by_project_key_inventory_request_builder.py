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


class ByProjectKeyInventoryRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def withId(self, ID: str) -> ByProjectKeyInventoryByIDRequestBuilder:
        return ByProjectKeyInventoryByIDRequestBuilder(
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
    ) -> "InventoryPagedQueryResponse":
        """Query inventory"""
        return self._client._get(
            endpoint=f"/{self._project_key}/inventory",
            params={
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_class=InventoryPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "InventoryEntryDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "InventoryEntry":
        """Create InventoryEntry"""
        return self._client._post(
            endpoint=f"/{self._project_key}/inventory",
            params={"expand": expand},
            data_object=body,
            response_class=InventoryEntry,
            headers={"Content-Type": "application/json", **headers},
        )
