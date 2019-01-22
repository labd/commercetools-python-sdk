import typing
from typing import List, Optional

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.typing import OptionalListStr

__all__ = ["ExtensionService"]


class ExtensionDeleteSchema(abstract.AbstractDeleteSchema):
    pass


class ExtensionQuerySchema(abstract.AbstractQuerySchema):
    pass


class ExtensionService(abstract.AbstractService):
    def get_by_id(self, id: str) -> Optional[types.Extension]:
        return self._client._get(f"channels/{id}", {}, schemas.ExtensionSchema)

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> types.ExtensionPagedQueryResponse:
        params = ExtensionQuerySchema().dump(
            {
                "where": where,
                "sort": sort,
                "expand": expand,
                "limit": limit,
                "offset": offset,
            }
        )
        return self._client._get(
            "channels", params, schemas.ExtensionPagedQueryResponseSchema
        )

    def create(self, draft: types.ExtensionDraft) -> types.Extension:
        return self._client._post(
            "channels", {}, draft, schemas.ExtensionDraftSchema, schemas.ExtensionSchema
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: List[types.ExtensionUpdateAction],
        *,
        force_update: bool = False,
    ) -> types.Extension:
        update_action = types.ExtensionUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"channels/{id}",
            params={},
            data_object=update_action,
            request_schema_cls=schemas.ExtensionUpdateSchema,
            response_schema_cls=schemas.ExtensionSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self, id: str, version: int, *, force_delete: bool = True
    ) -> types.Extension:
        params = ExtensionDeleteSchema().dump({"version": version})
        return self._client._delete(
            endpoint=f"channels/{id}",
            params=params,
            response_schema_cls=schemas.ExtensionSchema,
            force_delete=force_delete,
        )
