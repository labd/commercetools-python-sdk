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
from ..common import ReferenceTypeId
from .common import (
    BaseResourceSchema,
    LocalizedStringField,
    ReferenceSchema,
    ResourceIdentifierSchema,
)

# Fields


# Marshmallow Schemas
class ProductTailoringSchema(BaseResourceSchema):
    last_modified_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.LastModifiedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="lastModifiedBy",
    )
    created_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.CreatedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="createdBy",
    )
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    store = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".store.StoreKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    product = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".product.ProductReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    published = marshmallow.fields.Boolean(allow_none=True, load_default=None)
    current = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductTailoringDataSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    staged = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductTailoringDataSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    has_staged_changes = marshmallow.fields.Boolean(
        allow_none=True, load_default=None, data_key="hasStagedChanges"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductTailoring(**data)


class ProductTailoringDataSchema(helpers.BaseSchema):
    name = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
    )
    description = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
    )
    meta_title = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
        data_key="metaTitle",
    )
    meta_description = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
        data_key="metaDescription",
    )
    meta_keywords = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
        data_key="metaKeywords",
    )
    slug = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductTailoringData(**data)


class ProductTailoringDraftSchema(helpers.BaseSchema):
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    store = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".store.StoreResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    product = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".product.ProductResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    name = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
    )
    description = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
    )
    meta_title = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
        data_key="metaTitle",
    )
    meta_description = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
        data_key="metaDescription",
    )
    meta_keywords = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
        data_key="metaKeywords",
    )
    slug = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
    )
    publish = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductTailoringDraft(**data)


class ProductTailoringInStoreDraftSchema(helpers.BaseSchema):
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    product = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".product.ProductResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    name = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
    )
    description = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
    )
    meta_title = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
        data_key="metaTitle",
    )
    meta_description = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
        data_key="metaDescription",
    )
    meta_keywords = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
        data_key="metaKeywords",
    )
    slug = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
    )
    publish = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductTailoringInStoreDraft(**data)


class ProductTailoringPagedQueryResponseSchema(helpers.BaseSchema):
    limit = marshmallow.fields.Integer(allow_none=True, load_default=None)
    offset = marshmallow.fields.Integer(allow_none=True, load_default=None)
    count = marshmallow.fields.Integer(allow_none=True, load_default=None)
    total = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductTailoringSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductTailoringPagedQueryResponse(**data)


class ProductTailoringReferenceSchema(ReferenceSchema):
    obj = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductTailoringSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.ProductTailoringReference(**data)


class ProductTailoringResourceIdentifierSchema(ResourceIdentifierSchema):

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.ProductTailoringResourceIdentifier(**data)


class ProductTailoringUpdateActionSchema(helpers.BaseSchema):
    action = marshmallow.fields.String(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTailoringUpdateAction(**data)


class ProductTailoringPublishActionSchema(ProductTailoringUpdateActionSchema):

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTailoringPublishAction(**data)


class ProductTailoringSetDescriptionActionSchema(ProductTailoringUpdateActionSchema):
    description = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTailoringSetDescriptionAction(**data)


class ProductTailoringSetMetaAttributesActionSchema(ProductTailoringUpdateActionSchema):
    meta_title = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
        data_key="metaTitle",
    )
    meta_description = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
        data_key="metaDescription",
    )
    meta_keywords = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
        data_key="metaKeywords",
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTailoringSetMetaAttributesAction(**data)


class ProductTailoringSetMetaDescriptionActionSchema(
    ProductTailoringUpdateActionSchema
):
    meta_description = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
        data_key="metaDescription",
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTailoringSetMetaDescriptionAction(**data)


class ProductTailoringSetMetaKeywordsActionSchema(ProductTailoringUpdateActionSchema):
    meta_keywords = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
        data_key="metaKeywords",
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTailoringSetMetaKeywordsAction(**data)


class ProductTailoringSetMetaTitleActionSchema(ProductTailoringUpdateActionSchema):
    meta_title = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
        data_key="metaTitle",
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTailoringSetMetaTitleAction(**data)


class ProductTailoringSetNameActionSchema(ProductTailoringUpdateActionSchema):
    name = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTailoringSetNameAction(**data)


class ProductTailoringSetSlugActionSchema(ProductTailoringUpdateActionSchema):
    slug = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTailoringSetSlugAction(**data)


class ProductTailoringUnpublishActionSchema(ProductTailoringUpdateActionSchema):

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTailoringUnpublishAction(**data)
