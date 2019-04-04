import typing
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
    def get_by_id(self, id: str) -> Optional[types.Order]:
        return self._client._get(f"orders/{id}", {}, schemas.OrderSchema)

    def get_by_key(self, key: str) -> types.Order:
        return self._client._get(f"orders/key={key}", {}, schemas.OrderSchema)

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
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

    def create(self, cart: types.OrderFromCartDraft) -> types.Order:
        return self._client._post(
            "orders", {}, cart, schemas.OrderFromCartDraftSchema, schemas.OrderSchema
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: List[types.OrderUpdateAction],
        *,
        force_update: bool = False,
    ) -> types.Order:
        update_action = types.OrderUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"orders/{id}",
            params={},
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
        *,
        force_update: bool = False,
    ) -> types.Order:
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
        *,
        force_delete: bool = True,
    ) -> types.Order:
        params = OrderDeleteSchema().dump(
            {"version": version, "data_erasure": data_erasure}
        )
        return self._client._delete(
            endpoint=f"orders/{id}",
            params=params,
            response_schema_cls=schemas.OrderSchema,
            force_delete=force_delete,
        )

    def delete_by_order_number(
        self,
        order_number: str,
        version: int,
        data_erasure: bool = False,
        *,
        force_delete: bool = True,
    ) -> types.Order:
        params = OrderDeleteSchema().dump(
            {"version": version, "data_erasure": data_erasure}
        )
        return self._client._delete(
            endpoint=f"orders/order-number={order_number}",
            params=params,
            response_schema_cls=schemas.OrderSchema,
            force_delete=force_delete,
        )
