import typing
from typing import Optional
from uuid import UUID

from marshmallow import Schema, fields, post_dump

from commercetools import helpers, schemas, types
from commercetools.services import abstract
from commercetools.typing import OptionalListInt, OptionalListStr, OptionalListUUID

__all__ = ["ProductProjectionService"]


class _ProductProjectionsBaseSchema(Schema, abstract.RemoveEmptyValuesMixin):
    sort = helpers.OptionalList(fields.String())
    limit = fields.Int()
    offset = fields.Int()

    staged = fields.Bool(data_key="staged", required=False, missing=False)
    price_currency = fields.String(data_key="priceCurrency")
    price_country = fields.String(data_key="priceCountry")
    price_customer_group = fields.UUID(data_key="priceCustomerGroup")
    price_channel = fields.UUID(data_key="priceChannel")


class ProductProjectionsQuerySchema(_ProductProjectionsBaseSchema):
    where = helpers.OptionalList(fields.String())
    expand = helpers.OptionalList(fields.String())


class ProductProjectionsSearchSchema(_ProductProjectionsBaseSchema):
    text = fields.Method("text_serialize")
    fuzzy = fields.Bool()
    fuzzy_level = fields.Integer(data_key="fuzzy.level")
    filter = helpers.OptionalList(fields.String())
    filter_query = helpers.OptionalList(fields.String(), data_key="filter.query")
    filter_facets = helpers.OptionalList(fields.String(), data_key="filter.facets")
    facet = helpers.OptionalList(fields.String())
    mark_matching_variants = fields.Bool(data_key="markMatchingVariants")

    def text_serialize(self, value):
        result = {}
        data = value.get("text") or {}
        for k, v in data.items():
            result[f"text.{k}"] = v
        return result

    @post_dump
    def merge_text(self, data):
        value = data.pop("text")
        data.update(value)
        return data


class ProductProjectionService(abstract.AbstractService):
    def get_by_id(
        self,
        id: str,
        staged: bool = False,
        price_currency: OptionalListStr = None,
        price_country: OptionalListStr = None,
        price_customer_group: typing.Optional[UUID] = None,
        price_channel: typing.Optional[UUID] = None,
    ) -> Optional[types.ProductProjection]:
        return self._client._get(
            f"product-projections/{id}", {}, schemas.ProductProjectionSchema
        )

    def get_by_key(
        self,
        key: str,
        staged: bool = False,
        price_currency: OptionalListStr = None,
        price_country: OptionalListStr = None,
        price_customer_group: typing.Optional[UUID] = None,
        price_channel: typing.Optional[UUID] = None,
    ) -> types.ProductProjection:
        return self._client._get(
            f"product-projections/key={key}", {}, schemas.ProductProjectionSchema
        )

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: OptionalListStr = None,
        limit: OptionalListInt = None,
        offset: OptionalListInt = None,
        staged: bool = False,
        price_currency: OptionalListStr = None,
        price_country: OptionalListStr = None,
        price_customer_group: OptionalListUUID = None,
        price_channel: OptionalListUUID = None,
    ) -> types.ProductProjectionPagedQueryResponse:
        params = ProductProjectionsQuerySchema().dump(
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
            "product-projections",
            params,
            schemas.ProductProjectionPagedQueryResponseSchema,
        )

    def search(
        self,
        text: typing.Optional[typing.Dict[str, str]] = None,
        fuzzy: typing.Optional[bool] = None,
        fuzzy_level: typing.Optional[int] = None,
        filter: OptionalListStr = None,
        filter_query: OptionalListStr = None,
        filter_facets: OptionalListStr = None,
        facet: OptionalListStr = None,
        sort: OptionalListStr = None,
        limit: OptionalListInt = None,
        offset: OptionalListInt = None,
        staged: bool = False,
        mark_matching_variants: bool = False,
        price_currency: OptionalListStr = None,
        price_country: OptionalListStr = None,
        price_customer_group: OptionalListUUID = None,
        price_channel: OptionalListUUID = None,
    ) -> types.ProductProjectionPagedSearchResponse:
        params = {
            "text": text,
            "fuzzy": fuzzy,
            "fuzzy_level": fuzzy_level,
            "filter": filter,
            "filter_query": filter_query,
            "filter_facets": filter_facets,
            "facet": facet,
            "sort": sort,
            "limit": limit,
            "offset": offset,
            "staged": staged,
            "mark_matching_variants": mark_matching_variants,
            "price_currency": price_currency,
            "price_country": price_country,
            "price_customer_group": price_customer_group,
            "price_channel": price_channel,
        }
        return self._client._post(
            "product-projections/search",
            {},
            params,
            ProductProjectionsSearchSchema,
            response_schema_cls=schemas.ProductProjectionPagedSearchResponseSchema,
            form_encoded=True,
        )
