# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models

# Fields


# Marshmallow Schemas
class ProjectCategoryRecommendationSchema(helpers.BaseSchema):
    category = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.CategoryReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    confidence = marshmallow.fields.Float(allow_none=True, missing=None)
    path = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProjectCategoryRecommendation(**data)


class ProjectCategoryRecommendationMetaSchema(helpers.BaseSchema):
    product_name = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="productName",
    )
    product_image_url = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="productImageUrl",
    )
    general_category_names = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        missing=None,
        data_key="generalCategoryNames",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProjectCategoryRecommendationMeta(**data)


class ProjectCategoryRecommendationPagedQueryResponseSchema(helpers.BaseSchema):
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProjectCategoryRecommendationSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    meta = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProjectCategoryRecommendationMetaSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProjectCategoryRecommendationPagedQueryResponse(**data)
