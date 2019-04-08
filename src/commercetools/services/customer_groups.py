from typing import List, Optional

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.typing import OptionalListStr


class CustomerGroupQuerySchema(abstract.AbstractQuerySchema):
    pass


class CustomerGroupDeleteSchema(abstract.AbstractDeleteSchema):
    pass


class CustomerGroupService(abstract.AbstractService):
    def get_by_id(self, id: str) -> Optional[types.CustomerGroup]:
        return self._client._get(
            f"customer-groups/{id}", {}, schemas.CustomerGroupSchema
        )

    def get_by_key(self, key: str) -> Optional[types.CustomerGroup]:
        return self._client._get(
            f"customer-groups/key={key}", {}, schemas.CustomerGroupSchema
        )

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
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

    def create(self, draft: types.CustomerGroupDraft) -> types.CustomerGroup:
        return self._client._post(
            "customer-groups",
            {},
            draft,
            schemas.CustomerGroupDraftSchema,
            schemas.CustomerGroupSchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: List[types.CustomerGroupUpdateAction],
        *,
        force_update: bool = False,
    ) -> types.CustomerGroup:
        update_action = types.CustomerGroupUpdate(version=version, actions=actions)
        return self._client._post(
            f"customer-groups/{id}",
            {},
            data_object=update_action,
            request_schema_cls=schemas.CustomerGroupUpdateSchema,
            response_schema_cls=schemas.CustomerGroupSchema,
        )

    def update_by_key(
        self,
        key: str,
        version: int,
        actions: List[types.CustomerGroupUpdateAction],
        *,
        force_update: bool = False,
    ) -> types.CustomerGroup:
        update_action = types.CustomerGroupUpdate(version=version, actions=actions)
        return self._client._post(
            f"customer-groups/key={key}",
            {},
            data_object=update_action,
            request_schema_cls=schemas.CustomerGroupUpdateSchema,
            response_schema_cls=schemas.CustomerGroupSchema,
        )

    def delete_by_id(
        self, id: str, version: int, *, force_delete: bool = False
    ) -> types.CustomerGroup:
        params = CustomerGroupDeleteSchema().dump({"version": version})
        return self._client._delete(
            f"customer-groups/{id}",
            params=params,
            response_schema_cls=schemas.CustomerGroupSchema,
            force_delete=force_delete,
        )

    def delete_by_key(
        self, key: str, version: int, *, force_delete: bool = False
    ) -> types.CustomerGroup:
        params = CustomerGroupDeleteSchema().dump({"version": version})
        return self._client._delete(
            f"customer-groups/key={key}",
            params=params,
            response_schema_cls=schemas.CustomerGroupSchema,
            force_delete=force_delete,
        )
