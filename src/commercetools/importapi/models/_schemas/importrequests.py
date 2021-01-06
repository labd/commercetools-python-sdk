# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..common import ImportResourceType

# Fields


# Marshmallow Schemas
class ImportRequestSchema(helpers.BaseSchema):
    type = marshmallow_enum.EnumField(
        ImportResourceType, by_value=True, allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ImportRequest(**data)


class ImportResponseSchema(helpers.BaseSchema):
    operation_status = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".importoperations.ImportOperationStatusSchema"
        ),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="operationStatus",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ImportResponse(**data)


class CategoryImportRequestSchema(ImportRequestSchema):
    resources = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".categories.CategoryImportSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CategoryImportRequest(**data)


class ProductImportRequestSchema(ImportRequestSchema):
    resources = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".products.ProductImportSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductImportRequest(**data)


class ProductDraftImportRequestSchema(ImportRequestSchema):
    resources = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".productdrafts.ProductDraftImportSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductDraftImportRequest(**data)


class ProductTypeImportRequestSchema(ImportRequestSchema):
    resources = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".producttypes.ProductTypeImportSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductTypeImportRequest(**data)


class ProductVariantImportRequestSchema(ImportRequestSchema):
    resources = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".productvariants.ProductVariantImportSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductVariantImportRequest(**data)


class PriceImportRequestSchema(ImportRequestSchema):
    resources = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".prices.PriceImportSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.PriceImportRequest(**data)


class OrderImportRequestSchema(ImportRequestSchema):
    resources = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".orders.OrderImportSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderImportRequest(**data)


class ProductVariantPatchRequestSchema(ImportRequestSchema):
    patches = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".productvariants.ProductVariantPatchSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductVariantPatchRequest(**data)


class CustomerImportRequestSchema(ImportRequestSchema):
    resources = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customers.CustomerImportSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CustomerImportRequest(**data)


class InventoryImportRequestSchema(ImportRequestSchema):
    resources = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".inventories.InventoryImportSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.InventoryImportRequest(**data)
