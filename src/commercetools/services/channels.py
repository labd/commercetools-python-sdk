import typing
from typing import List, Optional

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.typing import OptionalListStr

__all__ = ["ChannelService"]


class ChannelDeleteSchema(abstract.AbstractDeleteSchema):
    pass


class ChannelQuerySchema(abstract.AbstractQuerySchema):
    pass


class ChannelService(abstract.AbstractService):
    def get_by_id(self, id: str) -> Optional[types.Channel]:
        return self._client._get(f"channels/{id}", {}, schemas.ChannelSchema)

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> types.ChannelPagedQueryResponse:
        params = ChannelQuerySchema().dump(
            {
                "where": where,
                "sort": sort,
                "expand": expand,
                "limit": limit,
                "offset": offset,
            }
        )
        return self._client._get(
            "channels", params, schemas.ChannelPagedQueryResponseSchema
        )

    def create(self, draft: types.ChannelDraft) -> types.Channel:
        return self._client._post(
            endpoint="channels",
            params={},
            data_object=draft,
            request_schema_cls=schemas.ChannelDraftSchema,
            response_schema_cls=schemas.ChannelSchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: List[types.ChannelUpdateAction],
        *,
        force_update: bool = False,
    ) -> types.Channel:
        update_action = types.ChannelUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"channels/{id}",
            params={},
            data_object=update_action,
            request_schema_cls=schemas.ChannelUpdateSchema,
            response_schema_cls=schemas.ChannelSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self, id: str, version: int, *, force_delete: bool = True
    ) -> types.Channel:
        params = ChannelDeleteSchema().dump({"version": version})
        return self._client._delete(
            endpoint=f"channels/{id}",
            params=params,
            response_schema_cls=schemas.ChannelSchema,
            force_delete=force_delete,
        )
