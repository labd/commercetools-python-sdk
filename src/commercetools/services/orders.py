from typing import List, Optional

from marshmallow import fields

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.typing import OptionalListStr

__all__ = ["OrderService"]


class OrderDeleteSchema(abstract.AbstractDeleteSchema):
    data_erasure = fields.Bool(data_key="dataErasure", required=False)


class OrderQuerySchema(abstract.AbstractQuerySchema):
    pass


class OrderService(abstract.AbstractService):
    def get_by_id(self, id: str, expand: OptionalListStr = None) -> Optional[types.Order]:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._get(f"orders/{id}", query_params, schemas.OrderSchema)

    def get_by_key(self, key: str, expand: OptionalListStr = None) -> types.Order:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._get(f"orders/key={key}", query_params, schemas.OrderSchema)

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: OptionalListStr = None,
        limit: int = None,
        offset: int = None,
    ) -> types.OrderPagedQueryResponse:
        params = OrderQuerySchema().dump(
            {
                "where": where,
                "sort": sort,
                "expand": expand,
                "limit": limit,
                "offset": offset,
            }
        )
        return self._client._get(
            "orders", params, schemas.OrderPagedQueryResponseSchema
        )

    def create(self, cart: types.OrderFromCartDraft, expand: OptionalListStr = None) -> types.Order:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._post(
            "orders", query_params, cart, schemas.OrderFromCartDraftSchema, schemas.OrderSchema
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: List[types.OrderUpdateAction],
        expand: OptionalListStr = None,
        *,
        force_update: bool = False,
    ) -> types.Order:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        update_action = types.OrderUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"orders/{id}",
            params=query_params,
            data_object=update_action,
            request_schema_cls=schemas.OrderUpdateSchema,
            response_schema_cls=schemas.OrderSchema,
            force_update=force_update,
        )

    def update_by_key(
        self,
        key: str,
        version: int,
        actions: List[types.OrderUpdateAction],
        expand: OptionalListStr = None,
        *,
        force_update: bool = False,
    ) -> types.Order:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        update_action = types.OrderUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"orders/key={key}",
            params={},
            data_object=update_action,
            request_schema_cls=schemas.OrderUpdateSchema,
            response_schema_cls=schemas.OrderSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        data_erasure: bool = False,
        expand: OptionalListStr = None,
        *,
        force_delete: bool = True,
    ) -> types.Order:
        params = {"version": version, "data_erasure": data_erasure}
        if expand:
            params["expand"] = expand

        query_params = OrderDeleteSchema().dump(params)
        return self._client._delete(
            endpoint=f"orders/{id}",
            params=query_params,
            response_schema_cls=schemas.OrderSchema,
            force_delete=force_delete,
        )

    def delete_by_order_number(
        self,
        order_number: str,
        version: int,
        data_erasure: bool = False,
        expand: OptionalListStr = None,
        *,
        force_delete: bool = True,
    ) -> types.Order:
        params = {"version": version, "data_erasure": data_erasure}
        if expand:
            params["expand"] = expand
        query_params = OrderDeleteSchema().dump(params)
        return self._client._delete(
            endpoint=f"orders/order-number={order_number}",
            params=query_params,
            response_schema_cls=schemas.OrderSchema,
            force_delete=force_delete,
        )
