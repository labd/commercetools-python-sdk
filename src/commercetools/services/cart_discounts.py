from typing import List, Optional

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.typing import OptionalListStr

__all__ = ["CartDiscountService"]


class CartDiscountDeleteSchema(abstract.AbstractDeleteSchema):
    pass


class CartDiscountQuerySchema(abstract.AbstractQuerySchema):
    pass


class CartDiscountService(abstract.AbstractService):
    def get_by_id(self, id: str, expand: OptionalListStr = None) -> Optional[types.CartDiscount]:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._get(f"cart-discounts/{id}", query_params, schemas.CartDiscountSchema)

    def get_by_key(self, key: str, expand: OptionalListStr = None) -> Optional[types.CartDiscount]:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._get(f"cart-discounts/key={key}", query_params, schemas.CartDiscountSchema)

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: OptionalListStr = None,
        limit: int = None,
        offset: int = None,
    ) -> types.CartDiscountPagedQueryResponse:
        params = CartDiscountQuerySchema().dump(
            {
                "where": where,
                "sort": sort,
                "expand": expand,
                "limit": limit,
                "offset": offset,
            }
        )
        return self._client._get(
            "cart-discounts", params, schemas.CartDiscountPagedQueryResponseSchema
        )

    def create(self, draft: types.CartDiscountDraft, expand: OptionalListStr = None) -> types.CartDiscount:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._post(
            endpoint="cart-discounts",
            params=query_params,
            data_object=draft,
            request_schema_cls=schemas.CartDiscountDraftSchema,
            response_schema_cls=schemas.CartDiscountSchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: List[types.CartDiscountUpdateAction],
        expand: OptionalListStr = None,
        *,
        force_update: bool = False,
    ) -> types.CartDiscount:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        update_action = types.CartDiscountUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"cart-discounts/{id}",
            params=query_params,
            data_object=update_action,
            request_schema_cls=schemas.CartDiscountUpdateSchema,
            response_schema_cls=schemas.CartDiscountSchema,
            force_update=force_update,
        )

    def update_by_key(
        self,
        key: str,
        version: int,
        actions: List[types.CartDiscountUpdateAction],
        expand: OptionalListStr = None,
        *,
        force_update: bool = False,
    ) -> types.CartDiscount:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        update_action = types.CartDiscountUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"cart-discounts/key={key}",
            params=query_params,
            data_object=update_action,
            request_schema_cls=schemas.CartDiscountUpdateSchema,
            response_schema_cls=schemas.CartDiscountSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self, id: str, version: int, expand: OptionalListStr = None, *, force_delete: bool = True
    ) -> types.CartDiscount:
        params = {"version": version}
        if expand:
            params["expand"] = expand
        query_params = CartDiscountDeleteSchema().dump(params)
        return self._client._delete(
            endpoint=f"cart-discounts/{id}",
            params=query_params,
            response_schema_cls=schemas.CartDiscountSchema,
            force_delete=force_delete,
        )

    def delete_by_key(
        self, key: str, version: int, expand: OptionalListStr = None, *, force_delete: bool = True
    ) -> types.CartDiscount:
        params = {"version": version}
        if expand:
            params["expand"] = expand
        query_params = CartDiscountDeleteSchema().dump(params)
        return self._client._delete(
            endpoint=f"cart-discounts/key={key}",
            params=query_params,
            response_schema_cls=schemas.CartDiscountSchema,
            force_delete=force_delete,
        )
