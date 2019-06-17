from typing import List, Optional

from marshmallow import fields

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.typing import OptionalListStr


class CustomerDeleteSchema(abstract.AbstractDeleteSchema):
    data_erasure = fields.Bool(data_key="dataErasure", required=False)


class CustomerQuerySchema(abstract.AbstractQuerySchema):
    pass


class CustomerService(abstract.AbstractService):
    def get_by_id(self, id: str, expand: OptionalListStr = None) -> Optional[types.Customer]:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._get(f"customers/{id}", query_params, schemas.CustomerSchema)

    def get_by_key(self, key: str, expand: OptionalListStr = None) -> Optional[types.Customer]:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._get(f"customers/key={key}", query_params, schemas.CustomerSchema)

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: OptionalListStr = None,
        limit: int = None,
        offset: int = None,
    ) -> types.CustomerPagedQueryResponse:
        params = CustomerQuerySchema().dump(
            {
                "where": where,
                "sort": sort,
                "expand": expand,
                "limit": limit,
                "offset": offset,
            }
        )
        return self._client._get(
            "customers", params, schemas.CustomerPagedQueryResponseSchema
        )

    def create(self, draft: types.CustomerDraft, expand: OptionalListStr = None) -> types.Customer:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._post(
            "customers", query_params, draft, schemas.CustomerDraftSchema, schemas.CustomerSchema
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: List[types.CustomerUpdateAction],
        expand: OptionalListStr = None,
        *,
        force_update: bool = False,
    ) -> types.Customer:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        update_action = types.CustomerUpdate(version=version, actions=actions)
        return self._client._post(
            f"customers/{id}",
            query_params,
            data_object=update_action,
            request_schema_cls=schemas.CustomerUpdateSchema,
            response_schema_cls=schemas.CustomerSchema,
            force_update=force_update,
        )

    def update_by_key(
        self,
        key: str,
        version: int,
        actions: List[types.CustomerUpdateAction],
        expand: OptionalListStr = None,
        *,
        force_update: bool = False,
    ) -> types.Customer:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        update_action = types.CustomerUpdate(version=version, actions=actions)
        return self._client._post(
            f"customers/key={key}",
            query_params,
            data_object=update_action,
            request_schema_cls=schemas.CustomerUpdateSchema,
            response_schema_cls=schemas.CustomerSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        data_erasure: bool = False,
        expand: OptionalListStr = None,
        *,
        force_delete: bool = False,
    ) -> types.Customer:
        params = {"version": version, "data_erasure": data_erasure}
        if expand:
            params["expand"] = expand
        query_params = CustomerDeleteSchema().dump(params)
        return self._client._delete(
            f"customers/{id}",
            params=query_params,
            response_schema_cls=schemas.CustomerSchema,
            force_delete=force_delete,
        )

    def delete_by_key(
        self,
        key: str,
        version: int,
        data_erasure: bool = False,
        expand: OptionalListStr = None,
        *,
        force_delete: bool = False,
    ) -> types.Customer:
        params = {"version": version, "data_erasure": data_erasure}
        if expand:
            params["expand"] = expand
        query_params = CustomerDeleteSchema().dump(params)
        return self._client._delete(
            f"customers/key={key}",
            params=query_params,
            response_schema_cls=schemas.CustomerSchema,
            force_delete=force_delete,
        )
