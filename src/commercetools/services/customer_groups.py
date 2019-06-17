from typing import List, Optional

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.typing import OptionalListStr


class CustomerGroupQuerySchema(abstract.AbstractQuerySchema):
    pass


class CustomerGroupDeleteSchema(abstract.AbstractDeleteSchema):
    pass


class CustomerGroupService(abstract.AbstractService):
    def get_by_id(self, id: str, expand: OptionalListStr = None) -> Optional[types.CustomerGroup]:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._get(
            f"customer-groups/{id}", query_params, schemas.CustomerGroupSchema
        )

    def get_by_key(self, key: str, expand: OptionalListStr = None) -> Optional[types.CustomerGroup]:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._get(
            f"customer-groups/key={key}", query_params, schemas.CustomerGroupSchema
        )

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: OptionalListStr = None,
        limit: int = None,
        offset: int = None,
    ) -> types.CustomerGroupPagedQueryResponse:
        params = CustomerGroupQuerySchema().dump(
            {
                "where": where,
                "sort": sort,
                "expand": expand,
                "limit": limit,
                "offset": offset,
            }
        )
        return self._client._get(
            "customer-groups", params, schemas.CustomerGroupPagedQueryResponseSchema
        )

    def create(self, draft: types.CustomerGroupDraft, expand: OptionalListStr = None) -> types.CustomerGroup:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._post(
            "customer-groups",
            query_params,
            draft,
            schemas.CustomerGroupDraftSchema,
            schemas.CustomerGroupSchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: List[types.CustomerGroupUpdateAction],
        expand: OptionalListStr = None,
        *,
        force_update: bool = False,
    ) -> types.CustomerGroup:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        update_action = types.CustomerGroupUpdate(version=version, actions=actions)
        return self._client._post(
            f"customer-groups/{id}",
            query_params,
            data_object=update_action,
            request_schema_cls=schemas.CustomerGroupUpdateSchema,
            response_schema_cls=schemas.CustomerGroupSchema,
            force_update=force_update,
        )

    def update_by_key(
        self,
        key: str,
        version: int,
        actions: List[types.CustomerGroupUpdateAction],
        expand: OptionalListStr = None,
        *,
        force_update: bool = False,
    ) -> types.CustomerGroup:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        update_action = types.CustomerGroupUpdate(version=version, actions=actions)
        return self._client._post(
            f"customer-groups/key={key}",
            query_params,
            data_object=update_action,
            request_schema_cls=schemas.CustomerGroupUpdateSchema,
            response_schema_cls=schemas.CustomerGroupSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self, id: str, version: int, expand: OptionalListStr = None, *, force_delete: bool = False
    ) -> types.CustomerGroup:
        params = {"version": version}
        if expand:
            params["expand"] = expand
        query_params = CustomerGroupDeleteSchema().dump(params)
        return self._client._delete(
            f"customer-groups/{id}",
            params=query_params,
            response_schema_cls=schemas.CustomerGroupSchema,
            force_delete=force_delete,
        )

    def delete_by_key(
        self, key: str, version: int, expand: OptionalListStr = None, *, force_delete: bool = False
    ) -> types.CustomerGroup:
        params = {"version": version}
        if expand:
            params["expand"] = expand
        query_params = CustomerGroupDeleteSchema().dump(params)
        return self._client._delete(
            f"customer-groups/key={key}",
            params=query_params,
            response_schema_cls=schemas.CustomerGroupSchema,
            force_delete=force_delete,
        )
