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
    def get_by_id(self, id: str) -> Optional[types.TaxCategory]:
        return self._client._get(f"tax-categories/{id}", {}, schemas.TaxCategorySchema)

    def get_by_key(self, key: str) -> Optional[types.TaxCategory]:
        return self._client._get(
            f"tax-categories/key={key}", {}, schemas.TaxCategorySchema
        )

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
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

    def create(self, draft: types.TaxCategoryDraft) -> types.Channel:
        return self._client._post(
            "tax-categories",
            {},
            draft,
            schemas.TaxCategoryDraftSchema,
            schemas.TaxCategorySchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: List[types.TaxCategoryUpdateAction],
        *,
        force_update: bool = False,
    ) -> types.TaxCategory:
        update_action = types.TaxCategoryUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"tax-categories/{id}",
            params={},
            data_object=update_action,
            request_schema_cls=schemas.TaxCategoryUpdateSchema,
            response_schema_cls=schemas.TaxCategorySchema,
            force_update=force_update,
        )

    def delete_by_id(
        self, id: str, version: int, *, force_delete: bool = False
    ) -> types.TaxCategory:
        params = TaxCategoryDeleteSchema().dump({"version": version})
        return self._client._delete(
            endpoint=f"tax-categories/{id}",
            params=params,
            response_schema_cls=schemas.TaxCategorySchema,
            force_delete=force_delete,
        )
