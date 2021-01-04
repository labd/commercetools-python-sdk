# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models

# Fields


# Marshmallow Schemas
class ImageSearchResponseSchema(marshmallow.Schema):
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Float(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ResultItemSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ImageSearchResponse(**data)


class ResultItemSchema(marshmallow.Schema):
    image_url = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="imageUrl"
    )
    product_variants = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.ProductVariantSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="productVariants",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ResultItem(**data)
