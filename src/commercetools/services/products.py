import typing
from typing import List, Optional
from uuid import UUID

from marshmallow import Schema, fields

from commercetools import schemas, types

__all__ = ["ProductService"]


class ProductDeleteSchema(Schema):
    version = fields.Integer()
    price_currency = fields.String(data_key="priceCurrency", required=False)
    price_country = fields.String(data_key="priceCountry", required=False)
    price_customer_group = fields.UUID(data_key="priceCustomerGroup", required=False)
    price_channel = fields.UUID(data_key="priceChannel", required=False)


class ProductService:
    def __init__(self, client):
        self._client = client

    def get_by_id(self, id: str) -> Optional[types.Product]:
        return self._client._get(f"products/{id}", [], schemas.ProductSchema)

    def get_by_key(self, key: str) -> types.Product:
        return self._client._get(f"products/key={key}", [], schemas.ProductSchema)

    def query(self) -> List[types.Product]:
        pass

    def create(self, draft: types.ProductDraft) -> types.Product:
        return self._client._create(
            "products", [], draft, schemas.ProductUpdateSchema, schemas.ProductSchema
        )

    def update_by_id(
        self, id: str, version: int, actions: List[types.ProductUpdateAction]
    ) -> types.Product:
        update_action = types.ProductUpdate(version=version, actions=actions)
        return self._client._update(
            f"products/{id}",
            [],
            update_action,
            schemas.ProductUpdateSchema,
            schemas.ProductSchema,
        )

    def update_by_key(
        self, key: str, version: int, actions: List[types.ProductUpdateAction]
    ) -> types.Product:
        update_action = types.ProductUpdate(version=version, actions=actions)
        return self._client._update(
            f"products/key={key}",
            [],
            update_action,
            schemas.ProductUpdateSchema,
            schemas.ProductSchema,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        price_currency: typing.Optional[str] = None,
        price_country: typing.Optional[str] = None,
        price_customer_group: typing.Optional[UUID] = None,
        price_channel: typing.Optional[UUID] = None,
    ) -> types.Product:
        params = ProductDeleteSchema().dump(
            {
                "version": version,
                "price_currency": price_currency,
                "price_country": price_country,
                "price_customer_group": price_customer_group,
                "price_channel": price_channel,
            }
        )
        return self._client._delete(f"products/{id}", params, schemas.ProductSchema)

    def delete_by_key(
        self,
        key: str,
        version: int,
        price_currency: typing.Optional[str] = None,
        price_country: typing.Optional[str] = None,
        price_customer_group: typing.Optional[UUID] = None,
        price_channel: typing.Optional[UUID] = None,
    ) -> types.Product:
        params = ProductDeleteSchema().dump(
            {
                "version": version,
                "price_currency": price_currency,
                "price_country": price_country,
                "price_customer_group": price_customer_group,
                "price_channel": price_channel,
            }
        )
        return self._client._delete(
            f"products/key={key}", params, schemas.ProductSchema
        )
