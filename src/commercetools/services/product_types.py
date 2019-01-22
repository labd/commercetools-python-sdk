import typing

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.typing import OptionalListStr

__all__ = ["ProductTypeService"]


class ProductTypeDeleteSchema(abstract.AbstractDeleteSchema):
    pass


class ProductTypeQuerySchema(abstract.AbstractQuerySchema):
    pass


class ProductTypeService(abstract.AbstractService):
    def get_by_id(self, id: str) -> types.ProductType:
        return self._client._get(f"product-types/{id}", {}, schemas.ProductTypeSchema)

    def get_by_key(self, key: str) -> types.ProductType:
        return self._client._get(
            f"product-types/key={key}", {}, schemas.ProductTypeSchema
        )

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> types.ProductTypePagedQueryResponse:
        params = ProductTypeQuerySchema().dump(
            {
                "where": where,
                "sort": sort,
                "expand": expand,
                "limit": limit,
                "offset": offset,
            }
        )
        return self._client._get(
            "product-types", params, schemas.ProductTypePagedQueryResponseSchema
        )

    def create(self, draft: types.ProductTypeDraft) -> types.ProductType:
        return self._client._post(
            "product-types",
            {},
            draft,
            schemas.ProductTypeDraftSchema,
            schemas.ProductTypeSchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: typing.List[types.ProductTypeUpdateAction],
        *,
        force_update: bool = False,
    ) -> types.ProductType:
        update_action = types.ProductTypeUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"product-types/{id}",
            params={},
            data_object=update_action,
            request_schema_cls=schemas.ProductTypeUpdateSchema,
            response_schema_cls=schemas.ProductTypeSchema,
            force_update=force_update,
        )

    def update_by_key(
        self,
        key: str,
        version: int,
        actions: typing.List[types.ProductTypeUpdateAction],
        *,
        force_update: bool = False,
    ) -> types.ProductType:
        update_action = types.ProductTypeUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"product-types/key={key}",
            params={},
            data_object=update_action,
            request_schema_cls=schemas.ProductTypeUpdateSchema,
            response_schema_cls=schemas.ProductTypeSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self, id: str, version: int, *, force_delete: bool = True
    ) -> types.ProductType:
        params = ProductTypeDeleteSchema().dump({"version": version})
        return self._client._delete(
            endpoint=f"product-types/{id}",
            params=params,
            response_schema_cls=schemas.ProductTypeSchema,
            force_delete=force_delete,
        )

    def delete_by_key(
        self, key: str, version: int, *, force_delete: bool = True
    ) -> types.ProductType:
        params = ProductTypeDeleteSchema().dump({"version": version})
        return self._client._delete(
            endpoint=f"product-types/key={key}",
            params=params,
            response_schema_cls=schemas.ProductTypeSchema,
            force_delete=force_delete,
        )
