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
    def get_by_id(self, id: str) -> Optional[types.Customer]:
        return self._client._get(f"customers/{id}", {}, schemas.CustomerSchema)

    def get_by_key(self, key: str) -> Optional[types.Customer]:
        return self._client._get(f"customers/key={key}", {}, schemas.CustomerSchema)

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
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

    def create(self, draft: types.CustomerDraft) -> types.Customer:
        return self._client._post(
            "customers", {}, draft, schemas.CustomerDraftSchema, schemas.CustomerSchema
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: List[types.CustomerUpdateAction],
        *,
        force_update: bool = False,
    ) -> types.Customer:
        update_action = types.CustomerUpdate(version=version, actions=actions)
        return self._client._post(
            f"customers/{id}",
            {},
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
        *,
        force_update: bool = False,
    ) -> types.Customer:
        update_action = types.CustomerUpdate(version=version, actions=actions)
        return self._client._post(
            f"customers/key={key}",
            {},
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
        *,
        force_delete: bool = False,
    ) -> types.Customer:
        params = CustomerDeleteSchema().dump(
            {"version": version, "data_erasure": data_erasure}
        )
        return self._client._delete(
            f"customers/{id}",
            params=params,
            response_schema_cls=schemas.CustomerSchema,
            force_delete=force_delete,
        )

    def delete_by_key(
        self,
        key: str,
        version: int,
        data_erasure: bool = False,
        *,
        force_delete: bool = False,
    ) -> types.Customer:
        params = CustomerDeleteSchema().dump(
            {"version": version, "data_erasure": data_erasure}
        )
        return self._client._delete(
            f"customers/key={key}",
            params=params,
            response_schema_cls=schemas.CustomerSchema,
            force_delete=force_delete,
        )
