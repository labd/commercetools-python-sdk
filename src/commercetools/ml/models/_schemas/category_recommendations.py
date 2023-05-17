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

# Fields


# Marshmallow Schemas
class ProjectCategoryRecommendationSchema(helpers.BaseSchema):
    category = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.CategoryReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    confidence = marshmallow.fields.Float(allow_none=True, load_default=None)
    path = marshmallow.fields.String(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return models.ProjectCategoryRecommendation(**data)


class ProjectCategoryRecommendationMetaSchema(helpers.BaseSchema):
    product_name = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="productName",
    )
    product_image_url = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="productImageUrl",
    )
    general_category_names = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        load_default=None,
        data_key="generalCategoryNames",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return models.ProjectCategoryRecommendationMeta(**data)


class ProjectCategoryRecommendationPagedQueryResponseSchema(helpers.BaseSchema):
    count = marshmallow.fields.Integer(allow_none=True, load_default=None)
    total = marshmallow.fields.Integer(allow_none=True, load_default=None)
    offset = marshmallow.fields.Integer(allow_none=True, load_default=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProjectCategoryRecommendationSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    meta = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProjectCategoryRecommendationMetaSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return models.ProjectCategoryRecommendationPagedQueryResponse(**data)
