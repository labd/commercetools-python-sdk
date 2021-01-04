# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from .common import ImportResourceSchema, LocalizedStringField

# Fields


# Marshmallow Schemas
class CategoryImportSchema(ImportResourceSchema):
    name = LocalizedStringField(allow_none=True, missing=None)
    slug = LocalizedStringField(allow_none=True, missing=None)
    description = LocalizedStringField(allow_none=True, missing=None)
    parent = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.CategoryKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    order_hint = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="orderHint"
    )
    external_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="externalId"
    )
    meta_title = LocalizedStringField(
        allow_none=True, missing=None, data_key="metaTitle"
    )
    meta_description = LocalizedStringField(
        allow_none=True, missing=None, data_key="metaDescription"
    )
    meta_keywords = LocalizedStringField(
        allow_none=True, missing=None, data_key="metaKeywords"
    )
    assets = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AssetSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customfields.CustomSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CategoryImport(**data)
