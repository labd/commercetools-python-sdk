import typing
from typing import List, Optional

from commercetools import abstract, schemas, types

__all__ = ["CategoriesService"]


class CategoryDeleteSchema(abstract.AbstractDeleteSchema):
    pass


class CategoryQuerySchema(abstract.AbstractQuerySchema):
    pass


class CategoriesService:
    def __init__(self, client):
        self._client = client

    def get_by_id(self, id: str) -> Optional[types.Category]:
        return self._client._get(f"categories/{id}", [], schemas.CategorySchema)

    def get_by_key(self, key: str) -> types.Category:
        return self._client._get(f"categories/key={key}", [], schemas.CategorySchema)

    def query(
        self,
        where: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        expand: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> List[types.Category]:
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
            "categories",
            [],
            draft,
            schemas.CategoryUpdateSchema,
            schemas.CategorySchema,
        )

    def update_by_id(
        self, id: str, version: int, actions: List[types.CategoryUpdateAction]
    ) -> types.Category:
        update_action = types.CategoryUpdate(version=version, actions=actions)
        return self._client._post(
            f"categories/{id}",
            [],
            update_action,
            schemas.CategoryUpdateSchema,
            schemas.CategorySchema,
        )

    def update_by_key(
        self, key: str, version: int, actions: List[types.CategoryUpdateAction]
    ) -> types.Category:
        update_action = types.CategoryUpdate(version=version, actions=actions)
        return self._client._post(
            f"categories/key={key}",
            [],
            update_action,
            schemas.CategoryUpdateSchema,
            schemas.CategorySchema,
        )

    def delete_by_id(self, id: str, version: int) -> types.Category:
        params = CategoryDeleteSchema().dump({"version": version})
        return self._client._delete(f"categories/{id}", params, schemas.CategorySchema)

    def delete_by_key(self, key: str, version: int) -> types.Category:
        params = CategoryDeleteSchema().dump({"version": version})
        return self._client._delete(
            f"categories/key={key}", params, schemas.CategorySchema
        )
