import typing
from typing import Optional

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.typing import OptionalListStr

__all__ = ["ApiClientService"]


class ApiClientDeleteSchema(abstract.AbstractDeleteSchema):
    pass


class ApiClientQuerySchema(abstract.AbstractQuerySchema):
    pass


class ApiClientService(abstract.AbstractService):
    def get_by_id(self, id: str) -> Optional[types.ApiClient]:
        return self._client._get(f"api-clients/{id}", {}, schemas.ApiClientSchemaSchema)

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> types.ApiClientPagedQueryResponse:
        params = ApiClientQuerySchema().dump(
            {
                "where": where,
                "sort": sort,
                "expand": expand,
                "limit": limit,
                "offset": offset,
            }
        )
        return self._client._get("api-clients", params, schemas.ApiClientPagedQueryResponseSchema)

    def create(self, draft: types.ApiClientDraft) -> types.ApiClient:
        return self._client._post(
            "api-clients", {}, draft, schemas.ApiClientDraftSchema, schemas.ApiClientSchema
        )

    def delete_by_id(
        self,
        id: str,
        *,
        force_delete: bool = False,
    ) -> types.ApiClient:
        return self._client._delete(
            endpoint=f"api-clients/{id}",
            params={},
            response_schema_cls=schemas.ApiClientSchema,
            force_delete=force_delete,
        )
