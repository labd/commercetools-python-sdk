import typing

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.typing import OptionalListStr

__all__ = ["TypeService"]


class TypeDeleteSchema(abstract.AbstractDeleteSchema):
    pass


class TypeQuerySchema(abstract.AbstractQuerySchema):
    pass


class TypeService(abstract.AbstractService):
    def get_by_id(self, id: str) -> types.Type:
        return self._client._get(f"types/{id}", {}, schemas.TypeSchema)

    def get_by_key(self, key: str) -> types.Type:
        return self._client._get(f"types/key={key}", {}, schemas.TypeSchema)

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> types.TypePagedQueryResponse:
        params = TypeQuerySchema().dump(
            {
                "where": where,
                "sort": sort,
                "expand": expand,
                "limit": limit,
                "offset": offset,
            }
        )
        return self._client._get("types", params, schemas.TypePagedQueryResponseSchema)

    def create(self, draft: types.TypeDraft) -> types.Type:
        return self._client._post(
            "types", {}, draft, schemas.TypeDraftSchema, schemas.TypeSchema
        )

    def update_by_id(
        self, id: str, version: int, actions: typing.List[types.TypeUpdateAction]
    ) -> types.Type:
        update_action = types.TypeUpdate(version=version, actions=actions)
        return self._client._post(
            f"types/{id}",
            {},
            update_action,
            schemas.TypeUpdateSchema,
            schemas.TypeSchema,
        )

    def update_by_key(
        self, key: str, version: int, actions: typing.List[types.TypeUpdateAction]
    ) -> types.Type:
        update_action = types.TypeUpdate(version=version, actions=actions)
        return self._client._post(
            f"types/key={key}",
            {},
            update_action,
            schemas.TypeUpdateSchema,
            schemas.TypeSchema,
        )

    def delete_by_id(self, id: str, version: int) -> types.Type:
        params = TypeDeleteSchema().dump({"version": version})
        return self._client._delete(f"types/{id}", params, schemas.TypeSchema)

    def delete_by_key(self, key: str, version: int) -> types.Type:
        params = TypeDeleteSchema().dump({"version": version})
        return self._client._delete(f"types/key={key}", params, schemas.TypeSchema)
