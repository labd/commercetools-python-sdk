import typing
from typing import List, Optional

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.typing import OptionalListStr

__all__ = ["ShippingMethodService"]


class ShippingMethodDeleteSchema(abstract.AbstractDeleteSchema):
    pass


class ShippingMethodQuerySchema(abstract.AbstractQuerySchema):
    pass


class ShippingMethodService(abstract.AbstractService):
    def get_by_id(self, id: str) -> Optional[types.ShippingMethod]:
        return self._client._get(
            f"shipping-methods/{id}", {}, schemas.ShippingMethodSchema
        )

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> types.ShippingMethodPagedQueryResponse:
        params = ShippingMethodQuerySchema().dump(
            {
                "where": where,
                "sort": sort,
                "expand": expand,
                "limit": limit,
                "offset": offset,
            }
        )
        return self._client._get(
            "shipping-methods", params, schemas.ShippingMethodPagedQueryResponseSchema
        )

    def create(self, draft: types.ShippingMethodDraft) -> types.ShippingMethod:
        return self._client._post(
            "shipping-methods",
            {},
            draft,
            schemas.ShippingMethodDraftSchema,
            schemas.ShippingMethodSchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: List[types.ShippingMethodUpdateAction],
        *,
        force_update: bool = False,
    ) -> types.ShippingMethod:
        update_action = types.ShippingMethodUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"shipping-methods/{id}",
            params={},
            data_object=update_action,
            request_schema_cls=schemas.ShippingMethodUpdateSchema,
            response_schema_cls=schemas.ShippingMethodSchema,
            force_update=force_update,
        )

    def update_by_key(
        self,
        key: str,
        version: int,
        actions: List[types.ShippingMethodUpdateAction],
        *,
        force_update: bool = False,
    ) -> types.ShippingMethod:
        update_action = types.ShippingMethodUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"shipping-methods/key={key}",
            params={},
            data_object=update_action,
            request_schema_cls=schemas.ShippingMethodUpdateSchema,
            response_schema_cls=schemas.ShippingMethodSchema,
            force_update=force_update,
        )

    def delete(
        self, id: str, version: int, *, force_delete: bool = False
    ) -> types.ShippingMethod:
        params = ShippingMethodDeleteSchema().dump({"version": version})
        return self._client._delete(
            endpoint=f"shipping-methods/{id}",
            params=params,
            response_schema_cls=schemas.ShippingMethodSchema,
            force_delete=force_delete,
        )
