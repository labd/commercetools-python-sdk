import typing
from typing import List, Optional

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.typing import OptionalListStr

__all__ = ["SubscriptionService"]


class SubscriptionDeleteSchema(abstract.AbstractDeleteSchema):
    pass


class SubscriptionQuerySchema(abstract.AbstractQuerySchema):
    pass


class SubscriptionService(abstract.AbstractService):
    def get_by_id(self, id: str) -> Optional[types.Subscription]:
        return self._client._get(f"subscriptions/{id}", {}, schemas.SubscriptionSchema)

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> types.SubscriptionPagedQueryResponse:
        params = SubscriptionQuerySchema().dump(
            {
                "where": where,
                "sort": sort,
                "expand": expand,
                "limit": limit,
                "offset": offset,
            }
        )
        return self._client._get(
            "subscriptions", params, schemas.SubscriptionPagedQueryResponseSchema
        )

    def create(self, draft: types.SubscriptionDraft) -> types.Subscription:
        return self._client._post(
            "subscriptions",
            {},
            draft,
            schemas.SubscriptionDraftSchema,
            schemas.SubscriptionSchema,
        )

    def update_by_id(
        self, id: str, version: int, actions: List[types.SubscriptionUpdateAction]
    ) -> types.Subscription:
        update_action = types.SubscriptionUpdate(version=version, actions=actions)
        return self._client._post(
            f"subscriptions/{id}",
            {},
            update_action,
            schemas.SubscriptionUpdateSchema,
            schemas.SubscriptionSchema,
        )

    def delete_by_id(self, id: str, version: int) -> types.Subscription:
        params = SubscriptionDeleteSchema().dump({"version": version})
        return self._client._delete(
            f"subscriptions/{id}", params, schemas.SubscriptionSchema
        )
