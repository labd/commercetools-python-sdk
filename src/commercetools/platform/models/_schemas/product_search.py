# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..product_search import (
    ProductSearchFacetCountLevelEnum,
    ProductSearchFacetDistinctBucketSortBy,
    ProductSearchFacetScopeEnum,
)
from ..search import SearchFieldType, SearchSortOrder
from .error import ErrorResponseSchema

# Fields


# Marshmallow Schemas
class ProductPagedSearchResponseSchema(helpers.BaseSchema):
    total = marshmallow.fields.Integer(allow_none=True, load_default=None)
    offset = marshmallow.fields.Integer(allow_none=True, load_default=None)
    limit = marshmallow.fields.Integer(allow_none=True, load_default=None)
    facets = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductSearchFacetResultSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductSearchResultSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductPagedSearchResponse(**data)


class ProductSearchErrorResponseSchema(ErrorResponseSchema):

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductSearchErrorResponse(**data)


class ProductSearchMatchingVariantEntrySchema(helpers.BaseSchema):
    id = marshmallow.fields.Integer(allow_none=True, load_default=None)
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductSearchMatchingVariantEntry(**data)


class ProductSearchMatchingVariantsSchema(helpers.BaseSchema):
    all_matched = marshmallow.fields.Boolean(
        allow_none=True, load_default=None, data_key="allMatched"
    )
    matched_variants = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductSearchMatchingVariantEntrySchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
        data_key="matchedVariants",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductSearchMatchingVariants(**data)


class ProductSearchProjectionParamsSchema(helpers.BaseSchema):
    expand = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    price_currency = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="priceCurrency",
    )
    price_country = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="priceCountry",
    )
    price_customer_group = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="priceCustomerGroup",
    )
    price_channel = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="priceChannel",
    )
    locale_projection = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="localeProjection",
    )
    store_projection = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="storeProjection",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductSearchProjectionParams(**data)


class ProductSearchRequestSchema(helpers.BaseSchema):
    query = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".search.SearchQuerySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )
    sort = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".search.SearchSortingSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )
    limit = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    offset = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    mark_matching_variants = marshmallow.fields.Boolean(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="markMatchingVariants",
    )
    product_projection_parameters = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductSearchProjectionParamsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="productProjectionParameters",
    )
    facets = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductSearchFacetExpressionSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductSearchRequest(**data)


class ProductSearchResultSchema(helpers.BaseSchema):
    id = marshmallow.fields.String(allow_none=True, load_default=None)
    product_projection = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".product.ProductProjectionSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="productProjection",
    )
    matching_variants = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductSearchMatchingVariantsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="matchingVariants",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductSearchResult(**data)


class ProductSearchFacetCountValueSchema(helpers.BaseSchema):
    name = marshmallow.fields.String(allow_none=True, load_default=None)
    scope = marshmallow_enum.EnumField(
        ProductSearchFacetScopeEnum,
        by_value=True,
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
    )
    filter = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".search.SearchQuerySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )
    level = marshmallow_enum.EnumField(
        ProductSearchFacetCountLevelEnum,
        by_value=True,
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductSearchFacetCountValue(**data)


class ProductSearchFacetDistinctBucketSortExpressionSchema(helpers.BaseSchema):
    by = marshmallow_enum.EnumField(
        ProductSearchFacetDistinctBucketSortBy,
        by_value=True,
        allow_none=True,
        load_default=None,
    )
    order = marshmallow_enum.EnumField(
        SearchSortOrder, by_value=True, allow_none=True, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductSearchFacetDistinctBucketSortExpression(**data)


class ProductSearchFacetDistinctValueSchema(helpers.BaseSchema):
    name = marshmallow.fields.String(allow_none=True, load_default=None)
    scope = marshmallow_enum.EnumField(
        ProductSearchFacetScopeEnum,
        by_value=True,
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
    )
    filter = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".search.SearchQuerySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )
    level = marshmallow_enum.EnumField(
        ProductSearchFacetCountLevelEnum,
        by_value=True,
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
    )
    field = marshmallow.fields.String(allow_none=True, load_default=None)
    includes = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
    )
    sort = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".ProductSearchFacetDistinctBucketSortExpressionSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )
    limit = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    language = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    field_type = marshmallow_enum.EnumField(
        SearchFieldType,
        by_value=True,
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="fieldType",
    )
    missing = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductSearchFacetDistinctValue(**data)


class ProductSearchFacetExpressionSchema(helpers.BaseSchema):

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductSearchFacetExpression(**data)


class ProductSearchFacetCountExpressionSchema(ProductSearchFacetExpressionSchema):
    count = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductSearchFacetCountValueSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductSearchFacetCountExpression(**data)


class ProductSearchFacetDistinctExpressionSchema(ProductSearchFacetExpressionSchema):
    distinct = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductSearchFacetDistinctValueSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductSearchFacetDistinctExpression(**data)


class ProductSearchFacetRangesExpressionSchema(ProductSearchFacetExpressionSchema):
    ranges = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductSearchFacetRangesValueSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductSearchFacetRangesExpression(**data)


class ProductSearchFacetRangesFacetRangeSchema(helpers.BaseSchema):
    from_ = marshmallow.fields.Raw(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="from",
    )
    to = marshmallow.fields.Raw(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductSearchFacetRangesFacetRange(**data)


class ProductSearchFacetRangesValueSchema(helpers.BaseSchema):
    name = marshmallow.fields.String(allow_none=True, load_default=None)
    scope = marshmallow_enum.EnumField(
        ProductSearchFacetScopeEnum,
        by_value=True,
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
    )
    filter = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".search.SearchQuerySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )
    level = marshmallow_enum.EnumField(
        ProductSearchFacetCountLevelEnum,
        by_value=True,
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
    )
    field = marshmallow.fields.String(allow_none=True, load_default=None)
    ranges = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductSearchFacetRangesFacetRangeSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    language = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    field_type = marshmallow_enum.EnumField(
        SearchFieldType,
        by_value=True,
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="fieldType",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductSearchFacetRangesValue(**data)


class ProductSearchFacetResultSchema(helpers.BaseSchema):
    name = marshmallow.fields.String(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductSearchFacetResult(**data)


class ProductSearchFacetResultBucketSchema(ProductSearchFacetResultSchema):
    buckets = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductSearchFacetResultBucketEntrySchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductSearchFacetResultBucket(**data)


class ProductSearchFacetResultBucketEntrySchema(helpers.BaseSchema):
    key = marshmallow.fields.String(allow_none=True, load_default=None)
    count = marshmallow.fields.Integer(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductSearchFacetResultBucketEntry(**data)


class ProductSearchFacetResultCountSchema(ProductSearchFacetResultSchema):
    value = marshmallow.fields.Integer(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductSearchFacetResultCount(**data)