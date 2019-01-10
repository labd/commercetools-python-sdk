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
        self, id: str, version: int, actions: List[types.ShippingMethodUpdateAction]
    ) -> types.ShippingMethod:
        update_action = types.ShippingMethodUpdate(version=version, actions=actions)
        return self._client._post(
            f"shipping-methods/{id}",
            {},
            update_action,
            schemas.ShippingMethodUpdateSchema,
            schemas.ShippingMethodSchema,
        )

    def update_by_key(
        self, key: str, version: int, actions: List[types.ShippingMethodUpdateAction]
    ) -> types.ShippingMethod:
        update_action = types.ShippingMethodUpdate(version=version, actions=actions)
        return self._client._post(
            f"shipping-methods/key={key}",
            {},
            update_action,
            schemas.ShippingMethodUpdateSchema,
            schemas.ShippingMethodSchema,
        )

    def delete(self, id: str, version: int) -> types.ShippingMethod:
        params = ShippingMethodDeleteSchema().dump({"version": version})
        return self._client._delete(
            f"shipping-methods/{id}", params, schemas.ShippingMethodSchema
        )
