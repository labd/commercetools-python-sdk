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
    def get_by_id(self, id: str, expand: OptionalListStr = None) -> Optional[types.Category]:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._get(f"categories/{id}", query_params, schemas.CategorySchema)

    def get_by_key(self, key: str, expand: OptionalListStr = None) -> types.Category:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._get(f"categories/key={key}", query_params, schemas.CategorySchema)

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: OptionalListStr = None,
        limit: int = None,
        offset: int = None,
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

    def create(self, draft: types.CategoryDraft, expand: OptionalListStr = None) -> types.Category:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._post(
            "categories", query_params, draft, schemas.CategoryDraftSchema, schemas.CategorySchema
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: List[types.CategoryUpdateAction],
        expand: OptionalListStr = None,
        *,
        force_update: bool = False,
    ) -> types.Category:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        update_action = types.CategoryUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"categories/{id}",
            params=query_params,
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
        expand: OptionalListStr = None,
        *,
        force_update: bool = False,
    ) -> types.Category:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        update_action = types.CategoryUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"categories/key={key}",
            params=query_params,
            data_object=update_action,
            request_schema_cls=schemas.CategoryUpdateSchema,
            response_schema_cls=schemas.CategorySchema,
            force_update=force_update,
        )

    def delete_by_id(
        self, id: str, version: int, expand: OptionalListStr = None, *, force_delete: bool = True
    ) -> types.Category:
        params = {"version": version}
        if expand:
            params["expand"] = expand
        query_params = CategoryDeleteSchema().dump(params)
        return self._client._delete(
            endpoint=f"categories/{id}",
            params=query_params,
            response_schema_cls=schemas.CategorySchema,
            force_delete=force_delete,
        )

    def delete_by_key(
        self, key: str, version: int, expand: OptionalListStr = None, *, force_delete: bool = True
    ) -> types.Category:
        params = {"version": version}
        if expand:
            params["expand"] = expand
        query_params = CategoryDeleteSchema().dump(params)
        return self._client._delete(
            endpoint=f"categories/key={key}",
            params=query_params,
            response_schema_cls=schemas.CategorySchema,
            force_delete=force_delete,
        )
