# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..common import TaskStatusEnum
from .common import LocalizedStringField

# Fields


# Marshmallow Schemas
class ProductSetSelectorSchema(marshmallow.Schema):
    project_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="projectKey"
    )
    product_ids = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        missing=None,
        data_key="productIds",
    )
    product_type_ids = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        missing=None,
        data_key="productTypeIds",
    )
    staged = marshmallow.fields.Boolean(allow_none=True, missing=None)
    include_variants = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="includeVariants"
    )
    product_set_limit = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="productSetLimit"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductSetSelector(**data)


class SimilarityMeasuresSchema(marshmallow.Schema):
    name = marshmallow.fields.Integer(allow_none=True, missing=None)
    description = marshmallow.fields.Integer(allow_none=True, missing=None)
    attribute = marshmallow.fields.Integer(allow_none=True, missing=None)
    variant_count = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="variantCount"
    )
    price = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.SimilarityMeasures(**data)


class SimilarProductSearchRequestSchema(marshmallow.Schema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    language = marshmallow.fields.String(allow_none=True, missing=None)
    currency_code = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="currencyCode"
    )
    similarity_measures = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".SimilarityMeasuresSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="similarityMeasures",
    )
    product_set_selectors = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductSetSelectorSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="productSetSelectors",
    )
    confidence_min = marshmallow.fields.Float(
        allow_none=True, missing=None, data_key="confidenceMin"
    )
    confidence_max = marshmallow.fields.Float(
        allow_none=True, missing=None, data_key="confidenceMax"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.SimilarProductSearchRequest(**data)


class SimilarProductSchema(marshmallow.Schema):
    product = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.ProductReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    variant_id = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="variantId"
    )
    meta = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".SimilarProductMetaSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.SimilarProduct(**data)


class SimilarProductMetaSchema(marshmallow.Schema):
    name = LocalizedStringField(allow_none=True, missing=None)
    description = LocalizedStringField(allow_none=True, missing=None)
    price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    variant_count = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="variantCount"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.SimilarProductMeta(**data)


class SimilarProductPairSchema(marshmallow.Schema):
    confidence = marshmallow.fields.Float(allow_none=True, missing=None)
    products = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".SimilarProductSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.SimilarProductPair(**data)


class SimilarProductSearchRequestMetaSchema(marshmallow.Schema):
    similarity_measures = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".SimilarityMeasuresSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="similarityMeasures",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.SimilarProductSearchRequestMeta(**data)


class SimilarProductsPagedQueryResultSchema(marshmallow.Schema):
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".SimilarProductPairSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    meta = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".SimilarProductSearchRequestMetaSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.SimilarProductsPagedQueryResult(**data)


class SimilarProductsTaskStatusSchema(marshmallow.Schema):
    state = marshmallow_enum.EnumField(
        TaskStatusEnum, by_value=True, allow_none=True, missing=None
    )
    expires = marshmallow.fields.DateTime(allow_none=True, missing=None)
    result = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".SimilarProductsPagedQueryResultSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.SimilarProductsTaskStatus(**data)
