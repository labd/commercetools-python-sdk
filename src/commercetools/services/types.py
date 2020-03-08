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
    def get_by_id(self, id: str, expand: OptionalListStr = None) -> types.Type:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._get(f"types/{id}", query_params, schemas.TypeSchema)

    def get_by_key(self, key: str, expand: OptionalListStr = None) -> types.Type:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._get(f"types/key={key}", query_params, schemas.TypeSchema)

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: OptionalListStr = None,
        limit: int = None,
        offset: int = None,
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

    def create(
        self, draft: types.TypeDraft, expand: OptionalListStr = None
    ) -> types.Type:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._post(
            "types", query_params, draft, schemas.TypeDraftSchema, schemas.TypeSchema
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: typing.List[types.TypeUpdateAction],
        expand: OptionalListStr = None,
        *,
        force_update: bool = False,
    ) -> types.Type:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        update_action = types.TypeUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"types/{id}",
            params=query_params,
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
        expand: OptionalListStr = None,
        *,
        force_update: bool = False,
    ) -> types.Type:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        update_action = types.TypeUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"types/key={key}",
            params=query_params,
            data_object=update_action,
            request_schema_cls=schemas.TypeUpdateSchema,
            response_schema_cls=schemas.TypeSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        expand: OptionalListStr = None,
        *,
        force_delete: bool = False,
    ) -> types.Type:
        params = {"version": version}
        if expand:
            params["expand"] = expand
        query_params = TypeDeleteSchema().dump(params)
        return self._client._delete(
            endpoint=f"types/{id}",
            params=query_params,
            response_schema_cls=schemas.TypeSchema,
            force_delete=force_delete,
        )

    def delete_by_key(
        self,
        key: str,
        version: int,
        expand: OptionalListStr = None,
        *,
        force_delete: bool = False,
    ) -> types.Type:
        params = {"version": version}
        if expand:
            params["expand"] = expand
        query_params = TypeDeleteSchema().dump(params)
        return self._client._delete(
            endpoint=f"types/key={key}",
            params=query_params,
            response_schema_cls=schemas.TypeSchema,
            force_delete=force_delete,
        )
