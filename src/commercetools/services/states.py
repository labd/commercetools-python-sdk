import typing
from typing import List, Optional

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.typing import OptionalListStr

__all__ = ["StateService"]


class StateDeleteSchema(abstract.AbstractDeleteSchema):
    pass


class StateQuerySchema(abstract.AbstractQuerySchema):
    pass


class StateService(abstract.AbstractService):
    def get_by_id(self, id: str, expand: OptionalListStr = None) -> Optional[types.State]:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._get(f"states/{id}", query_params, schemas.StateSchema)

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: OptionalListStr = None,
        limit: int = None,
        offset: int = None,
    ) -> types.StatePagedQueryResponse:
        params = StateQuerySchema().dump(
            {
                "where": where,
                "sort": sort,
                "expand": expand,
                "limit": limit,
                "offset": offset,
            }
        )
        return self._client._get(
            "states", params, schemas.StatePagedQueryResponseSchema
        )

    def create(self, draft: types.StateDraft, expand: OptionalListStr = None) -> types.State:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._post(
            endpoint="states",
            params=query_params,
            data_object=draft,
            request_schema_cls=schemas.StateDraftSchema,
            response_schema_cls=schemas.StateSchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: List[types.StateUpdateAction],
        expand: OptionalListStr = None,
        *,
        force_update: bool = False,
    ) -> types.State:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        update_action = types.StateUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"states/{id}",
            params=query_params,
            data_object=update_action,
            request_schema_cls=schemas.StateUpdateSchema,
            response_schema_cls=schemas.StateSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self, id: str, version: int, expand: OptionalListStr = None, *, force_delete: bool = True
    ) -> types.State:
        params = {"version": version}
        if expand:
            params["expand"] = expand
        query_params = StateDeleteSchema().dump(params)
        return self._client._delete(
            endpoint=f"states/{id}",
            params=query_params,
            response_schema_cls=schemas.StateSchema,
            force_delete=force_delete,
        )
