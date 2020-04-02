from typing import List, Optional

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.typing import OptionalListStr

__all__ = ["DiscountCodeService"]


class DiscountCodeDeleteSchema(abstract.AbstractDeleteSchema):
    pass


class DiscountCodeQuerySchema(abstract.AbstractQuerySchema):
    pass


class DiscountCodeService(abstract.AbstractService):
    def get_by_id(self, id: str, expand: OptionalListStr = None) -> types.DiscountCode:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._get(
            f"discount-codes/{id}", query_params, schemas.DiscountCodeSchema
        )

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: OptionalListStr = None,
        limit: int = None,
        offset: int = None,
    ) -> types.DiscountCodePagedQueryResponse:
        params = DiscountCodeQuerySchema().dump(
            {
                "where": where,
                "sort": sort,
                "expand": expand,
                "limit": limit,
                "offset": offset,
            }
        )
        return self._client._get(
            "discount-codes", params, schemas.DiscountCodePagedQueryResponseSchema
        )

    def create(
        self, draft: types.DiscountCodeDraft, expand: OptionalListStr = None
    ) -> types.DiscountCode:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._post(
            endpoint="discount-codes",
            params=query_params,
            data_object=draft,
            request_schema_cls=schemas.DiscountCodeDraftSchema,
            response_schema_cls=schemas.DiscountCodeSchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: List[types.DiscountCodeUpdateAction],
        expand: OptionalListStr = None,
        *,
        force_update: bool = False,
    ) -> types.DiscountCode:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        update_action = types.DiscountCodeUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"discount-codes/{id}",
            params=query_params,
            data_object=update_action,
            request_schema_cls=schemas.DiscountCodeUpdateSchema,
            response_schema_cls=schemas.DiscountCodeSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        expand: OptionalListStr = None,
        *,
        force_delete: bool = True,
    ) -> types.DiscountCode:
        params = {"version": version}
        if expand:
            params["expand"] = expand
        query_params = DiscountCodeDeleteSchema().dump(params)
        return self._client._delete(
            endpoint=f"discount-codes/{id}",
            params=query_params,
            response_schema_cls=schemas.DiscountCodeSchema,
            force_delete=force_delete,
        )
