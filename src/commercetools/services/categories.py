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
        self, id: str, version: int, actions: List[types.CategoryUpdateAction]
    ) -> types.Category:
        update_action = types.CategoryUpdate(version=version, actions=actions)
        return self._client._post(
            f"categories/{id}",
            {},
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
            {},
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
