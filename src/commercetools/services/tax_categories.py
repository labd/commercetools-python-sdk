import typing
from typing import List, Optional

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.typing import OptionalListStr

__all__ = ["TaxCategoryService"]


class TaxCategoryDeleteSchema(abstract.AbstractDeleteSchema):
    pass


class TaxCategoryQuerySchema(abstract.AbstractQuerySchema):
    pass


class TaxCategoryService(abstract.AbstractService):
    def get_by_id(self, id: str, expand: OptionalListStr = None) -> Optional[types.TaxCategory]:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._get(f"tax-categories/{id}", query_params, schemas.TaxCategorySchema)

    def get_by_key(self, key: str, expand: OptionalListStr = None) -> Optional[types.TaxCategory]:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._get(
            f"tax-categories/key={key}", query_params, schemas.TaxCategorySchema
        )

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: OptionalListStr = None,
        limit: int = None,
        offset: int = None,
    ) -> types.TaxCategoryPagedQueryResponse:
        params = TaxCategoryQuerySchema().dump(
            {
                "where": where,
                "sort": sort,
                "expand": expand,
                "limit": limit,
                "offset": offset,
            }
        )
        return self._client._get(
            "tax-categories", params, schemas.TaxCategoryPagedQueryResponseSchema
        )

    def create(self, draft: types.TaxCategoryDraft, expand: OptionalListStr = None) -> types.Channel:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._post(
            "tax-categories",
            query_params,
            draft,
            schemas.TaxCategoryDraftSchema,
            schemas.TaxCategorySchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: List[types.TaxCategoryUpdateAction],
        expand: OptionalListStr = None,
        *,
        force_update: bool = False,
    ) -> types.TaxCategory:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        update_action = types.TaxCategoryUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"tax-categories/{id}",
            params=query_params,
            data_object=update_action,
            request_schema_cls=schemas.TaxCategoryUpdateSchema,
            response_schema_cls=schemas.TaxCategorySchema,
            force_update=force_update,
        )

    def delete_by_id(
        self, id: str, version: int, expand: OptionalListStr = None, *, force_delete: bool = False
    ) -> types.TaxCategory:
        params = {"version": version}
        if expand:
            params["expand"] = expand
        query_params = TaxCategoryDeleteSchema().dump(params)
        return self._client._delete(
            endpoint=f"tax-categories/{id}",
            params=query_params,
            response_schema_cls=schemas.TaxCategorySchema,
            force_delete=force_delete,
        )
