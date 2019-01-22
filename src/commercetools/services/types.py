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
        self,
        id: str,
        version: int,
        actions: typing.List[types.TypeUpdateAction],
        *,
        force_update: bool = False,
    ) -> types.Type:
        update_action = types.TypeUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"types/{id}",
            params={},
            data_object=update_action,
            request_schema_cls=schemas.TypeUpdateSchema,
            response_schema_cls=schemas.TypeSchema,
            force_update=force_update,
        )

    def update_by_key(
        self,
        key: str,
        version: int,
        actions: typing.List[types.TypeUpdateAction],
        *,
        force_update: bool = False,
    ) -> types.Type:
        update_action = types.TypeUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"types/key={key}",
            params={},
            data_object=update_action,
            request_schema_cls=schemas.TypeUpdateSchema,
            response_schema_cls=schemas.TypeSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self, id: str, version: int, *, force_delete: bool = False
    ) -> types.Type:
        params = TypeDeleteSchema().dump({"version": version})
        return self._client._delete(
            endpoint=f"types/{id}",
            params=params,
            response_schema_cls=schemas.TypeSchema,
            force_delete=force_delete,
        )

    def delete_by_key(
        self, key: str, version: int, *, force_delete: bool = False
    ) -> types.Type:
        params = TypeDeleteSchema().dump({"version": version})
        return self._client._delete(
            endpoint=f"types/key={key}",
            params=params,
            response_schema_cls=schemas.TypeSchema,
            force_delete=force_delete,
        )
