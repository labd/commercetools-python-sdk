import typing
from typing import List, Optional

from marshmallow import fields

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.typing import OptionalListStr

__all__ = ["PaymentService"]


class PaymentDeleteSchema(abstract.AbstractDeleteSchema):
    data_erasure = fields.Bool(data_key="dataErasure", required=False)


class PaymentQuerySchema(abstract.AbstractQuerySchema):
    pass


class PaymentService(abstract.AbstractService):
    def get_by_id(self, id: str) -> Optional[types.Payment]:
        return self._client._get(f"payments/{id}", {}, schemas.PaymentSchema)

    def get_by_key(self, key: str) -> types.Payment:
        return self._client._get(f"payments/key={key}", {}, schemas.PaymentSchema)

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> types.PaymentPagedQueryResponse:
        params = PaymentQuerySchema().dump(
            {
                "where": where,
                "sort": sort,
                "expand": expand,
                "limit": limit,
                "offset": offset,
            }
        )
        return self._client._get(
            "payments", params, schemas.PaymentPagedQueryResponseSchema
        )

    def create(self, draft: types.PaymentDraft) -> types.Payment:
        return self._client._post(
            "payments", {}, draft, schemas.PaymentDraftSchema, schemas.PaymentSchema
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: List[types.PaymentUpdateAction],
        *,
        force_update: bool = False,
    ) -> types.Payment:
        update_action = types.PaymentUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"payments/{id}",
            params={},
            data_object=update_action,
            request_schema_cls=schemas.PaymentUpdateSchema,
            response_schema_cls=schemas.PaymentSchema,
            force_update=force_update,
        )

    def update_by_key(
        self,
        key: str,
        version: int,
        actions: List[types.PaymentUpdateAction],
        *,
        force_update: bool = False,
    ) -> types.Payment:
        update_action = types.PaymentUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"payments/key={key}",
            params={},
            data_object=update_action,
            request_schema_cls=schemas.PaymentUpdateSchema,
            response_schema_cls=schemas.PaymentSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        data_erasure: bool = False,
        *,
        force_delete: bool = True,
    ) -> types.Payment:
        params = PaymentDeleteSchema().dump(
            {"version": version, "data_erasure": data_erasure}
        )
        return self._client._delete(
            endpoint=f"payments/{id}",
            params=params,
            response_schema_cls=schemas.PaymentSchema,
            force_delete=force_delete,
        )

    def delete_by_key(
        self,
        key: str,
        version: int,
        data_erasure: bool = False,
        *,
        force_delete: bool = True,
    ) -> types.Payment:
        params = PaymentDeleteSchema().dump(
            {"version": version, "data_erasure": data_erasure}
        )
        return self._client._delete(
            endpoint=f"payments/key={key}",
            params=params,
            response_schema_cls=schemas.PaymentSchema,
            force_delete=force_delete,
        )
