import typing
from typing import Optional

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.typing import OptionalListStr

__all__ = ["CustomObjectService"]


class CustomObjectDeleteSchema(abstract.AbstractDeleteSchema):
    pass


class CustomObjectQuerySchema(abstract.AbstractQuerySchema):
    pass


class CustomObjectService(abstract.AbstractService):
    def get_by_id(self, id: str) -> Optional[types.CustomObject]:
        return self._client._get(f"custom-objects/{id}", {}, schemas.CustomObjectSchema)

    def get_by_container_key(
        self, container: str, key: str
    ) -> Optional[types.CustomObject]:
        return self._client._get(
            f"custom-objects/{container}/{key}", {}, schemas.CustomObjectSchema
        )

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> types.CustomObjectPagedQueryResponse:
        params = CustomObjectQuerySchema().dump(
            {"where": where, "sort": sort, "limit": limit, "offset": offset}
        )
        return self._client._get(
            "custom-objects",
            params,
            schema_cls=schemas.CustomObjectPagedQueryResponseSchema,
        )

    def create_or_update(self, draft: types.CustomObjectDraft) -> types.CustomObject:
        return self._client._post(
            endpoint="custom-objects",
            params={},
            data_object=draft,
            request_schema_cls=schemas.CustomObjectDraftSchema,
            response_schema_cls=schemas.CustomObjectSchema,
        )

    def delete_by_id(
        self, id: str, version: int, *, force_delete: bool = True
    ) -> types.CustomObject:
        params = CustomObjectDeleteSchema().dump({"version": version})
        return self._client._delete(
            endpoint=f"custom-objects/{id}",
            params=params,
            response_schema_cls=schemas.CustomObjectSchema,
            force_delete=force_delete,
        )

    def delete_by_container_key(
        self, container: str, key: str, version: int, *, force_delete: bool = True
    ) -> types.CustomObject:
        params = CustomObjectDeleteSchema().dump({"version": version})
        return self._client._delete(
            endpoint=f"custom-objects/{container}/{key}",
            params=params,
            response_schema_cls=schemas.CustomObjectSchema,
            force_delete=force_delete,
        )
