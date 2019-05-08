import typing
from typing import Optional

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.typing import OptionalListStr

__all__ = ["StoreService"]


class StoreDeleteSchema(abstract.AbstractDeleteSchema):
    pass


class StoreQuerySchema(abstract.AbstractQuerySchema):
    pass


class StoreService(abstract.AbstractService):
    def get_by_id(self, id: str) -> Optional[types.Store]:
        return self._client._get(f"stores/{id}", {}, schemas.StoreSchema)

    def get_by_key(self, key: str) -> Optional[types.Store]:
        return self._client._get(f"stores/key={key}", {}, schemas.StoreSchema)

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> types.StorePagedQueryResponse:
        params = StoreQuerySchema().dump(
            {
                "where": where,
                "sort": sort,
                "expand": expand,
                "limit": limit,
                "offset": offset,
            }
        )
        return self._client._get("stores", params, schemas.StorePagedQueryResponseSchema)

    def create(self, draft: types.StoreDraft) -> types.Store:
        return self._client._post(
            "stores", {}, draft, schemas.StoreDraftSchema, schemas.StoreSchema
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: typing.List[types.StoreUpdateAction],
        *,
        force_update: bool = False,
    ) -> types.Store:
        update_action = types.StoreUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"stores/{id}",
            params={},
            data_object=update_action,
            request_schema_cls=schemas.StoreUpdateSchema,
            response_schema_cls=schemas.StoreSchema,
            force_update=force_update,
        )

    def update_by_key(
        self,
        key: str,
        version: int,
        actions: typing.List[types.StoreUpdateAction],
        *,
        force_update: bool = False,
    ) -> types.Store:
        update_action = types.StoreUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"stores/key={key}",
            params={},
            data_object=update_action,
            request_schema_cls=schemas.StoreUpdateSchema,
            response_schema_cls=schemas.StoreSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        *,
        force_delete: bool = False,
    ) -> types.Store:
        return self._client._delete(
            endpoint=f"stores/{id}",
            params={},
            response_schema_cls=schemas.StoreSchema,
            force_delete=force_delete,
        )

    def delete_by_key(
        self,
        key: str,
        *,
        force_delete: bool = False,
    ) -> types.Store:
        return self._client._delete(
            endpoint=f"stores/key={key}",
            params={},
            response_schema_cls=schemas.StoreSchema,
            force_delete=force_delete,
        )
