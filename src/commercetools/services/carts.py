from typing import List, Optional

from marshmallow import fields

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.typing import OptionalListStr

__all__ = ["CartService"]


class CartDeleteSchema(abstract.AbstractDeleteSchema):
    data_erasure = fields.Bool(data_key="dataErasure", required=False)


class CartQuerySchema(abstract.AbstractQuerySchema):
    pass


class CartService(abstract.AbstractService):
    def get_by_id(self, id: str, expand: OptionalListStr = None) -> types.Cart:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._get(f"carts/{id}", query_params, schemas.CartSchema)

    def get_by_customer_id(
        self, customer_id: str, expand: OptionalListStr = None
    ) -> types.Cart:
        query_params = {"customerId": customer_id}
        if expand:
            query_params["expand"] = expand
        return self._client._get(f"carts/", query_params, schemas.CartSchema)

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: OptionalListStr = None,
        limit: int = None,
        offset: int = None,
    ) -> types.CartPagedQueryResponse:
        params = CartQuerySchema().dump(
            {
                "where": where,
                "sort": sort,
                "expand": expand,
                "limit": limit,
                "offset": offset,
            }
        )
        return self._client._get("carts", params, schemas.CartPagedQueryResponseSchema)

    def create(
        self, draft: types.CartDraft, expand: OptionalListStr = None
    ) -> types.Cart:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._post(
            "carts", query_params, draft, schemas.CartDraftSchema, schemas.CartSchema
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: List[types.CartUpdateAction],
        expand: OptionalListStr = None,
        *,
        force_update: bool = False,
    ) -> types.Cart:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        update_action = types.CartUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"carts/{id}",
            params=query_params,
            data_object=update_action,
            request_schema_cls=schemas.CartUpdateSchema,
            response_schema_cls=schemas.CartSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        data_erasure: bool = False,
        expand: OptionalListStr = None,
        *,
        force_delete: bool = False,
    ) -> types.Cart:
        params = {"version": version, "data_erasure": data_erasure}
        if expand:
            params["expand"] = expand
        query_params = CartDeleteSchema().dump(params)
        return self._client._delete(
            endpoint=f"carts/{id}",
            params=query_params,
            response_schema_cls=schemas.CartSchema,
            force_delete=force_delete,
        )

    def replicate(self, draft: types.ReplicaCartDraft) -> types.Cart:
        return self._client._post(
            endpoint="carts/replicate",
            params={},
            data_object=draft,
            request_schema_cls=schemas.ReplicaCartDraftSchema,
            response_schema_cls=schemas.CartSchema,
        )
