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
    def get_by_id(self, id: str, expand: OptionalListStr = None) -> types.ProductType:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._get(f"product-types/{id}", query_params, schemas.ProductTypeSchema)

    def get_by_key(self, key: str, expand: OptionalListStr = None) -> types.ProductType:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._get(
            f"product-types/key={key}", query_params, schemas.ProductTypeSchema
        )

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: OptionalListStr = None,
        limit: int = None,
        offset: int = None,
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

    def create(self, draft: types.ProductTypeDraft, expand: OptionalListStr = None) -> types.ProductType:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._post(
            "product-types",
            query_params,
            draft,
            schemas.ProductTypeDraftSchema,
            schemas.ProductTypeSchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: typing.List[types.ProductTypeUpdateAction],
        expand: OptionalListStr = None,
        *,
        force_update: bool = False,
    ) -> types.ProductType:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        update_action = types.ProductTypeUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"product-types/{id}",
            params=query_params,
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
        expand: OptionalListStr = None,
        *,
        force_update: bool = False,
    ) -> types.ProductType:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        update_action = types.ProductTypeUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"product-types/key={key}",
            params=query_params,
            data_object=update_action,
            request_schema_cls=schemas.ProductTypeUpdateSchema,
            response_schema_cls=schemas.ProductTypeSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self, id: str, version: int, expand: OptionalListStr = None, *, force_delete: bool = True
    ) -> types.ProductType:
        params = {"version": version}
        if expand:
            params["expand"] = expand
        query_params = ProductTypeDeleteSchema().dump(params)
        return self._client._delete(
            endpoint=f"product-types/{id}",
            params=query_params,
            response_schema_cls=schemas.ProductTypeSchema,
            force_delete=force_delete,
        )

    def delete_by_key(
        self, key: str, version: int, expand: OptionalListStr = None, *, force_delete: bool = True
    ) -> types.ProductType:
        params = {"version": version}
        if expand:
            params["expand"] = expand
        query_params = ProductTypeDeleteSchema().dump(params)
        return self._client._delete(
            endpoint=f"product-types/key={key}",
            params=query_params,
            response_schema_cls=schemas.ProductTypeSchema,
            force_delete=force_delete,
        )
