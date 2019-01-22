import typing
from typing import List, Optional

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.typing import OptionalListStr

__all__ = ["CategoryService"]


class CategoryDeleteSchema(abstract.AbstractDeleteSchema):
    pass


class CategoryQuerySchema(abstract.AbstractQuerySchema):
    pass


class CategoryService(abstract.AbstractService):
    def get_by_id(self, id: str) -> Optional[types.Category]:
        return self._client._get(f"categories/{id}", {}, schemas.CategorySchema)

    def get_by_key(self, key: str) -> types.Category:
        return self._client._get(f"categories/key={key}", {}, schemas.CategorySchema)

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> types.CategoryPagedQueryResponse:
        params = CategoryQuerySchema().dump(
            {
                "where": where,
                "sort": sort,
                "expand": expand,
                "limit": limit,
                "offset": offset,
            }
        )
        return self._client._get(
            "categories", params, schemas.CategoryPagedQueryResponseSchema
        )

    def create(self, draft: types.CategoryDraft) -> types.Category:
        return self._client._post(
            "categories", {}, draft, schemas.CategoryDraftSchema, schemas.CategorySchema
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: List[types.CategoryUpdateAction],
        *,
        force_update: bool = False,
    ) -> types.Category:
        update_action = types.CategoryUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"categories/{id}",
            params={},
            data_object=update_action,
            request_schema_cls=schemas.CategoryUpdateSchema,
            response_schema_cls=schemas.CategorySchema,
            force_update=force_update,
        )

    def update_by_key(
        self,
        key: str,
        version: int,
        actions: List[types.CategoryUpdateAction],
        *,
        force_update: bool = False,
    ) -> types.Category:
        update_action = types.CategoryUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"categories/key={key}",
            params={},
            data_object=update_action,
            request_schema_cls=schemas.CategoryUpdateSchema,
            response_schema_cls=schemas.CategorySchema,
            force_update=force_update,
        )

    def delete_by_id(
        self, id: str, version: int, *, force_delete: bool = True
    ) -> types.Category:
        params = CategoryDeleteSchema().dump({"version": version})
        return self._client._delete(
            endpoint=f"categories/{id}",
            params=params,
            response_schema_cls=schemas.CategorySchema,
            force_delete=force_delete,
        )

    def delete_by_key(
        self, key: str, version: int, *, force_delete: bool = True
    ) -> types.Category:
        params = CategoryDeleteSchema().dump({"version": version})
        return self._client._delete(
            endpoint=f"categories/key={key}",
            params=params,
            response_schema_cls=schemas.CategorySchema,
            force_delete=force_delete,
        )
