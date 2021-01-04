# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models

# Fields


# Marshmallow Schemas
class GeneralCategoryRecommendationSchema(marshmallow.Schema):
    category_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="categoryName"
    )
    confidence = marshmallow.fields.Float(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.GeneralCategoryRecommendation(**data)


class GeneralCategoryRecommendationPagedQueryResponseSchema(marshmallow.Schema):
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".GeneralCategoryRecommendationSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.GeneralCategoryRecommendationPagedQueryResponse(**data)
