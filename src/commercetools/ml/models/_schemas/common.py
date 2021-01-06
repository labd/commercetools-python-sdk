# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..common import ReferenceTypeId


# Fields
class LocalizedStringField(marshmallow.fields.Dict):
    def _deserialize(self, value, attr, data, **kwargs):
        result = super()._deserialize(value, attr, data)
        return models.LocalizedString(**result)


# Marshmallow Schemas
class MoneySchema(helpers.BaseSchema):
    cent_amount = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="centAmount"
    )
    currency_code = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="currencyCode"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Money(**data)


class ReferenceSchema(helpers.BaseSchema):
    type_id = marshmallow_enum.EnumField(
        ReferenceTypeId, by_value=True, allow_none=True, missing=None, data_key="typeId"
    )
    id = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.Reference(**data)


class CategoryReferenceSchema(ReferenceSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.CategoryReference(**data)


class ProductReferenceSchema(ReferenceSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.ProductReference(**data)


class ProductTypeReferenceSchema(ReferenceSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.ProductTypeReference(**data)


class ProductVariantSchema(helpers.BaseSchema):
    product = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    staged = marshmallow.fields.Boolean(allow_none=True, missing=None)
    variant_id = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="variantId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductVariant(**data)


class TaskTokenSchema(helpers.BaseSchema):
    task_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="taskId"
    )
    uri_path = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="uriPath"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.TaskToken(**data)
