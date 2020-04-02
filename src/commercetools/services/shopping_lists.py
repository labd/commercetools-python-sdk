from typing import List, Optional

from marshmallow import fields

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.typing import OptionalListStr


class ShoppingListDeleteSchema(abstract.AbstractDeleteSchema):
    data_erasure = fields.Bool(data_key="dataErasure", required=False)


class ShoppingListQuerySchema(abstract.AbstractQuerySchema):
    pass


class ShoppingListService(abstract.AbstractService):
    def get_by_id(self, id: str) -> types.ShoppingList:
        return self._client._get(f"shopping-lists/{id}", {}, schemas.ShoppingListSchema)

    def get_by_key(self, key: str) -> types.ShoppingList:
        return self._client._get(
            f"shopping-lists/key={key}", {}, schemas.ShoppingListSchema
        )

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> types.ShoppingListPagedQueryResponse:
        params = ShoppingListQuerySchema().dump(
            {
                "where": where,
                "sort": sort,
                "expand": expand,
                "limit": limit,
                "offset": offset,
            }
        )
        return self._client._get(
            "shopping-lists", params, schemas.ShoppingListPagedQueryResponseSchema
        )

    def create(self, draft: types.ShoppingListDraft) -> types.ShoppingList:
        return self._client._post(
            "shopping-lists",
            {},
            draft,
            schemas.ShoppingListDraftSchema,
            schemas.ShoppingListSchema,
        )

    def _update(
        self,
        endpoint: str,
        version: int,
        actions: List[types.ShoppingListUpdateAction],
        force_update: bool = False,
    ) -> types.ShoppingList:
        update_action = types.ShoppingListUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint,
            {},
            data_object=update_action,
            request_schema_cls=schemas.ShoppingListUpdateSchema,
            response_schema_cls=schemas.ShoppingListSchema,
            force_update=force_update,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: List[types.ShoppingListUpdateAction],
        *,
        force_update: bool = False,
    ) -> types.ShoppingList:
        return self._update(
            endpoint=f"shopping-lists/{id}",
            version=version,
            actions=actions,
            force_update=force_update,
        )

    def update_by_key(
        self,
        key: str,
        version: int,
        actions: List[types.ShoppingListUpdateAction],
        *,
        force_update: bool = False,
    ) -> types.ShoppingList:
        return self._update(
            endpoint=f"shopping-lists/key={key}",
            version=version,
            actions=actions,
            force_update=force_update,
        )

    def _delete(
        self,
        endpoint: str,
        version: int,
        data_erasure: bool = False,
        force_delete: bool = False,
    ):
        params = ShoppingListDeleteSchema().dump(
            {"version": version, "data_erasure": data_erasure}
        )
        return self._client._delete(
            endpoint,
            params=params,
            response_schema_cls=schemas.ShoppingListSchema,
            force_delete=force_delete,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        data_erasure: bool = False,
        *,
        force_delete: bool = False,
    ) -> types.ShoppingList:
        return self._delete(
            endpoint=f"shopping-lists/{id}",
            version=version,
            data_erasure=data_erasure,
            force_delete=force_delete,
        )

    def delete_by_key(
        self,
        key: str,
        version: int,
        data_erasure: bool = False,
        *,
        force_delete: bool = False,
    ) -> types.ShoppingList:
        return self._delete(
            endpoint=f"shopping-lists/key={key}",
            version=version,
            data_erasure=data_erasure,
            force_delete=force_delete,
        )
