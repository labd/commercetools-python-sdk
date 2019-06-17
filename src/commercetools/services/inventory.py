from typing import List, Optional

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.typing import OptionalListStr

__all__ = ["InventoryService"]


class InventoryDeleteSchema(abstract.AbstractDeleteSchema):
    pass


class InventoryQuerySchema(abstract.AbstractQuerySchema):
    pass


class InventoryService(abstract.AbstractService):
    def get_by_id(self, id: str, expand: OptionalListStr = None) -> Optional[types.InventoryEntry]:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._get(f"inventory/{id}", query_params, schemas.InventoryEntrySchema)

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: OptionalListStr = None,
        limit: int = None,
        offset: int = None,
    ) -> types.InventoryPagedQueryResponse:
        params = InventoryQuerySchema().dump(
            {
                "where": where,
                "sort": sort,
                "expand": expand,
                "limit": limit,
                "offset": offset,
            }
        )
        return self._client._get(
            "inventory", params, schemas.InventoryPagedQueryResponseSchema
        )

    def create(self, draft: types.InventoryEntryDraft, expand: OptionalListStr = None) -> types.InventoryEntry:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._post(
            "inventory",
            query_params,
            draft,
            schemas.InventoryEntryDraftSchema,
            schemas.InventoryEntrySchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: List[types.InventoryUpdateAction],
        expand: OptionalListStr = None,
        *,
        force_update: bool = False,
    ) -> types.InventoryEntry:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        update_action = types.InventoryUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"inventory/{id}",
            params=query_params,
            data_object=update_action,
            request_schema_cls=schemas.InventoryUpdateSchema,
            response_schema_cls=schemas.InventoryEntrySchema,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        data_erasure: bool = False,
        expand: OptionalListStr = None,
        *,
        force_delete: bool = True,
    ) -> types.InventoryEntry:
        params = {"version": version, "data_erasure": data_erasure}
        if expand:
            params["expand"] = expand
        query_params = InventoryDeleteSchema().dump(params)
        return self._client._delete(
            endpoint=f"inventory/{id}",
            params=query_params,
            response_schema_cls=schemas.InventoryEntrySchema,
            force_delete=force_delete,
        )
