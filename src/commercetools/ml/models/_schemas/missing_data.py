# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..common import TaskStatusEnum

# Fields


# Marshmallow Schemas
class AttributeCountSchema(marshmallow.Schema):
    product_type_attributes = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="productTypeAttributes"
    )
    variant_attributes = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="variantAttributes"
    )
    missing_attribute_values = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="missingAttributeValues"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.AttributeCount(**data)


class AttributeCoverageSchema(marshmallow.Schema):
    names = marshmallow.fields.Float(allow_none=True, missing=None)
    values = marshmallow.fields.Float(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.AttributeCoverage(**data)


class MissingAttributesDetailsSchema(marshmallow.Schema):
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    missing_attribute_names = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="missingAttributeNames"
    )
    missing_attribute_values = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="missingAttributeValues"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MissingAttributesDetails(**data)


class MissingAttributesSchema(marshmallow.Schema):
    product = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.ProductReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    product_type = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.ProductTypeReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="productType",
    )
    variant_id = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="variantId"
    )
    missing_attribute_values = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        missing=None,
        data_key="missingAttributeValues",
    )
    missing_attribute_names = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        missing=None,
        data_key="missingAttributeNames",
    )
    attribute_count = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".AttributeCountSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="attributeCount",
    )
    attribute_coverage = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".AttributeCoverageSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="attributeCoverage",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MissingAttributes(**data)


class MissingAttributesMetaSchema(marshmallow.Schema):
    product_level = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".MissingAttributesDetailsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="productLevel",
    )
    variant_level = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".MissingAttributesDetailsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="variantLevel",
    )
    product_type_ids = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        missing=None,
        data_key="productTypeIds",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MissingAttributesMeta(**data)


class MissingAttributesSearchRequestSchema(marshmallow.Schema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    staged = marshmallow.fields.Boolean(allow_none=True, missing=None)
    product_set_limit = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="productSetLimit"
    )
    include_variants = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="includeVariants"
    )
    coverage_min = marshmallow.fields.Float(
        allow_none=True, missing=None, data_key="coverageMin"
    )
    coverage_max = marshmallow.fields.Float(
        allow_none=True, missing=None, data_key="coverageMax"
    )
    sort_by = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="sortBy"
    )
    show_missing_attribute_names = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="showMissingAttributeNames"
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
    attribute_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="attributeName"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MissingAttributesSearchRequest(**data)


class MissingAttributesPagedQueryResultSchema(marshmallow.Schema):
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".MissingAttributesSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    meta = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".MissingAttributesMetaSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MissingAttributesPagedQueryResult(**data)


class MissingDataTaskStatusSchema(marshmallow.Schema):
    state = marshmallow_enum.EnumField(
        TaskStatusEnum, by_value=True, allow_none=True, missing=None
    )
    expires = marshmallow.fields.DateTime(allow_none=True, missing=None)
    result = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".MissingAttributesPagedQueryResultSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MissingDataTaskStatus(**data)


class MissingImagesSchema(marshmallow.Schema):
    product = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.ProductReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    variant_id = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="variantId"
    )
    image_count = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="imageCount"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MissingImages(**data)


class MissingImagesCountSchema(marshmallow.Schema):
    missing_images = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="missingImages"
    )
    total = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MissingImagesCount(**data)


class MissingImagesProductLevelSchema(MissingImagesCountSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MissingImagesProductLevel(**data)


class MissingImagesVariantLevelSchema(MissingImagesCountSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MissingImagesVariantLevel(**data)


class MissingImagesMetaSchema(marshmallow.Schema):
    product_level = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".MissingImagesProductLevelSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="productLevel",
    )
    variant_level = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".MissingImagesVariantLevelSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="variantLevel",
    )
    threshold = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MissingImagesMeta(**data)


class MissingImagesSearchRequestSchema(marshmallow.Schema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    staged = marshmallow.fields.Boolean(allow_none=True, missing=None)
    product_set_limit = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="productSetLimit"
    )
    include_variants = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="includeVariants"
    )
    auto_threshold = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="autoThreshold"
    )
    threshold = marshmallow.fields.Integer(allow_none=True, missing=None)
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

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MissingImagesSearchRequest(**data)


class MissingImagesPagedQueryResultSchema(marshmallow.Schema):
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".MissingImagesSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    meta = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".MissingImagesMetaSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MissingImagesPagedQueryResult(**data)


class MissingImagesTaskStatusSchema(marshmallow.Schema):
    state = marshmallow_enum.EnumField(
        TaskStatusEnum, by_value=True, allow_none=True, missing=None
    )
    expires = marshmallow.fields.DateTime(allow_none=True, missing=None)
    result = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".MissingImagesPagedQueryResultSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MissingImagesTaskStatus(**data)


class MissingPricesSchema(marshmallow.Schema):
    product = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.ProductReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    variant_id = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="variantId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MissingPrices(**data)


class MissingPricesProductCountSchema(marshmallow.Schema):
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    missing_prices = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="missingPrices"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MissingPricesProductCount(**data)


class MissingPricesProductLevelSchema(MissingPricesProductCountSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MissingPricesProductLevel(**data)


class MissingPricesVariantLevelSchema(MissingPricesProductCountSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MissingPricesVariantLevel(**data)


class MissingPricesMetaSchema(marshmallow.Schema):
    product_level = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".MissingPricesProductLevelSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="productLevel",
    )
    variant_level = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".MissingPricesVariantLevelSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="variantLevel",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MissingPricesMeta(**data)


class MissingPricesSearchRequestSchema(marshmallow.Schema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    staged = marshmallow.fields.Boolean(allow_none=True, missing=None)
    product_set_limit = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="productSetLimit"
    )
    include_variants = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="includeVariants"
    )
    currency_code = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="currencyCode"
    )
    check_date = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="checkDate"
    )
    valid_from = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validFrom"
    )
    valid_until = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validUntil"
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

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MissingPricesSearchRequest(**data)


class MissingPricesPagedQueryResultSchema(marshmallow.Schema):
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".MissingPricesSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    meta = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".MissingPricesMetaSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MissingPricesPagedQueryResult(**data)


class MissingPricesTaskStatusSchema(marshmallow.Schema):
    state = marshmallow_enum.EnumField(
        TaskStatusEnum, by_value=True, allow_none=True, missing=None
    )
    expires = marshmallow.fields.DateTime(allow_none=True, missing=None)
    result = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".MissingPricesPagedQueryResultSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MissingPricesTaskStatus(**data)
