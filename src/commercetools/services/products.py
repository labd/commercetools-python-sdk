import typing
from typing import List, Optional
from uuid import UUID

from marshmallow import fields

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.typing import OptionalListStr

__all__ = ["ProductService"]


class ProductDeleteSchema(abstract.AbstractDeleteSchema):
    price_currency = fields.String(data_key="priceCurrency", required=False)
    price_country = fields.String(data_key="priceCountry", required=False)
    price_customer_group = fields.UUID(data_key="priceCustomerGroup", required=False)
    price_channel = fields.UUID(data_key="priceChannel", required=False)


class ProductQuerySchema(abstract.AbstractQuerySchema):
    price_currency = fields.String(data_key="priceCurrency", required=False)
    price_country = fields.String(data_key="priceCountry", required=False)
    price_customer_group = fields.UUID(data_key="priceCustomerGroup", required=False)
    price_channel = fields.UUID(data_key="priceChannel", required=False)


class ProductService(abstract.AbstractService):
    def get_by_id(self, id: str, price_currency: str = None,
                  price_country: str = None, price_customer_group: UUID = None,
                  price_channel: UUID = None, expand: OptionalListStr = None
                  ) -> Optional[types.Product]:
        params = ProductQuerySchema().dump(
            {
                "expand": expand,
                "price_currency": price_currency,
                "price_country": price_country,
                "price_customer_group": price_customer_group,
                "price_channel": price_channel,
            }
        )
        return self._client._get(f"products/{id}", params, schemas.ProductSchema)

    def get_by_key(self, key: str, price_currency: str = None, price_country: str = None,
                   price_customer_group: UUID = None, price_channel: UUID = None,
                   expand: OptionalListStr = None) -> Optional[types.Product]:
        params = ProductQuerySchema().dump(
            {
                "expand": expand,
                "price_currency": price_currency,
                "price_country": price_country,
                "price_customer_group": price_customer_group,
                "price_channel": price_channel,
            }
        )
        return self._client._get(f"products/key={key}", params, schemas.ProductSchema)

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: OptionalListStr = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        price_currency: typing.Optional[str] = None,
        price_country: typing.Optional[str] = None,
        price_customer_group: typing.Optional[UUID] = None,
        price_channel: typing.Optional[UUID] = None,
    ) -> types.ProductPagedQueryResponse:
        params = ProductQuerySchema().dump(
            {
                "where": where,
                "sort": sort,
                "expand": expand,
                "limit": limit,
                "offset": offset,
                "price_currency": price_currency,
                "price_country": price_country,
                "price_customer_group": price_customer_group,
                "price_channel": price_channel,
            }
        )
        return self._client._get(
            "products", params, schemas.ProductPagedQueryResponseSchema
        )

    def create(self, draft: types.ProductDraft, expand: OptionalListStr = None) -> types.Product:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._post(
            "products", query_params, draft, schemas.ProductDraftSchema, schemas.ProductSchema
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: List[types.ProductUpdateAction],
        expand: OptionalListStr = None,
        *,
        force_update: bool = False,
    ) -> types.Product:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        update_action = types.ProductUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"products/{id}",
            params=expand,
            data_object=update_action,
            request_schema_cls=schemas.ProductUpdateSchema,
            response_schema_cls=schemas.ProductSchema,
            force_update=force_update,
        )

    def update_by_key(
        self,
        key: str,
        version: int,
        actions: List[types.ProductUpdateAction],
        expand: OptionalListStr = None,
        *,
        force_update: bool = False,
    ) -> types.Product:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        update_action = types.ProductUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"products/key={key}",
            params=query_params,
            data_object=update_action,
            request_schema_cls=schemas.ProductUpdateSchema,
            response_schema_cls=schemas.ProductSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        price_currency: str = None,
        price_country: str = None,
        price_customer_group: UUID = None,
        price_channel: UUID = None,
        expand: OptionalListStr = None,
        *,
        force_delete: bool = False,
    ) -> types.Product:
        params = ProductDeleteSchema().dump(
            {
                "version": version,
                "price_currency": price_currency,
                "price_country": price_country,
                "price_customer_group": price_customer_group,
                "price_channel": price_channel,
                "expand": expand,
            }
        )
        return self._client._delete(
            endpoint=f"products/{id}",
            params=params,
            response_schema_cls=schemas.ProductSchema,
            force_delete=force_delete,
        )

    def delete_by_key(
        self,
        key: str,
        version: int,
        price_currency: str = None,
        price_country: str = None,
        price_customer_group: UUID = None,
        price_channel: UUID = None,
        expand: OptionalListStr = None,
        *,
        force_delete: bool = False,
    ) -> types.Product:
        params = ProductDeleteSchema().dump(
            {
                "version": version,
                "price_currency": price_currency,
                "price_country": price_country,
                "price_customer_group": price_customer_group,
                "price_channel": price_channel,
                "expand": expand,
            }
        )
        return self._client._delete(
            endpoint=f"products/key={key}",
            params=params,
            response_schema_cls=schemas.ProductSchema,
            force_delete=force_delete,
        )

    def upload_image(
        self,
        product_id: str,
        fh: typing.BinaryIO,
        sku: str = None,
        filename: str = "img",
        staged: bool = True,
    ):
        params = {"filename": filename, "staged": staged}
        if sku:
            params["sku"] = sku

        return self._client._upload(
            endpoint=f"products/{product_id}/images",
            params=params,
            file=fh,
            response_schema_cls=schemas.ProductSchema,
        )
