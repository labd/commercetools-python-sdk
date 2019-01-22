import typing
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
    def get_by_id(self, id: str) -> Optional[types.InventoryEntry]:
        return self._client._get(f"inventory/{id}", {}, schemas.InventoryEntrySchema)

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
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

    def create(self, draft: types.InventoryEntryDraft) -> types.InventoryEntry:
        return self._client._post(
            "inventory",
            {},
            draft,
            schemas.InventoryEntryDraftSchema,
            schemas.InventoryEntrySchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: List[types.InventoryUpdateAction],
        *,
        force_update: bool = False,
    ) -> types.InventoryEntry:
        update_action = types.InventoryUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"inventory/{id}",
            params={},
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
        *,
        force_delete: bool = True,
    ) -> types.InventoryEntry:
        params = InventoryDeleteSchema().dump(
            {"version": version, "data_erasure": data_erasure}
        )
        return self._client._delete(
            endpoint=f"inventory/{id}",
            params=params,
            response_schema_cls=schemas.InventoryEntrySchema,
            force_delete=force_delete,
        )
