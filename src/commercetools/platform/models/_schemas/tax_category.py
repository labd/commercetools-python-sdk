# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..common import ReferenceTypeId
from .common import BaseResourceSchema, ReferenceSchema, ResourceIdentifierSchema

# Fields


# Marshmallow Schemas
class SubRateSchema(marshmallow.Schema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    amount = marshmallow.fields.Float(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.SubRate(**data)


class TaxCategorySchema(BaseResourceSchema):
    last_modified_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.LastModifiedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="lastModifiedBy",
    )
    created_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.CreatedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="createdBy",
    )
    name = marshmallow.fields.String(allow_none=True, missing=None)
    description = marshmallow.fields.String(allow_none=True, missing=None)
    rates = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".TaxRateSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.TaxCategory(**data)


class TaxCategoryDraftSchema(marshmallow.Schema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    description = marshmallow.fields.String(allow_none=True, missing=None)
    rates = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".TaxRateDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.TaxCategoryDraft(**data)


class TaxCategoryPagedQueryResponseSchema(marshmallow.Schema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".TaxCategorySchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.TaxCategoryPagedQueryResponse(**data)


class TaxCategoryReferenceSchema(ReferenceSchema):
    obj = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".TaxCategorySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.TaxCategoryReference(**data)


class TaxCategoryResourceIdentifierSchema(ResourceIdentifierSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.TaxCategoryResourceIdentifier(**data)


class TaxCategoryUpdateSchema(marshmallow.Schema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addTaxRate": helpers.absmod(
                    __name__, ".TaxCategoryAddTaxRateActionSchema"
                ),
                "changeName": helpers.absmod(
                    __name__, ".TaxCategoryChangeNameActionSchema"
                ),
                "removeTaxRate": helpers.absmod(
                    __name__, ".TaxCategoryRemoveTaxRateActionSchema"
                ),
                "replaceTaxRate": helpers.absmod(
                    __name__, ".TaxCategoryReplaceTaxRateActionSchema"
                ),
                "setDescription": helpers.absmod(
                    __name__, ".TaxCategorySetDescriptionActionSchema"
                ),
                "setKey": helpers.absmod(__name__, ".TaxCategorySetKeyActionSchema"),
            },
        ),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.TaxCategoryUpdate(**data)


class TaxCategoryUpdateActionSchema(marshmallow.Schema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.TaxCategoryUpdateAction(**data)


class TaxRateSchema(marshmallow.Schema):
    id = marshmallow.fields.String(allow_none=True, missing=None)
    name = marshmallow.fields.String(allow_none=True, missing=None)
    amount = marshmallow.fields.Float(allow_none=True, missing=None)
    included_in_price = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="includedInPrice"
    )
    country = marshmallow.fields.String(allow_none=True, missing=None)
    state = marshmallow.fields.String(allow_none=True, missing=None)
    sub_rates = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".SubRateSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="subRates",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.TaxRate(**data)


class TaxRateDraftSchema(marshmallow.Schema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    amount = marshmallow.fields.Float(allow_none=True, missing=None)
    included_in_price = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="includedInPrice"
    )
    country = marshmallow.fields.String(allow_none=True, missing=None)
    state = marshmallow.fields.String(allow_none=True, missing=None)
    sub_rates = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".SubRateSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="subRates",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.TaxRateDraft(**data)


class TaxCategoryAddTaxRateActionSchema(TaxCategoryUpdateActionSchema):
    tax_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".TaxRateDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="taxRate",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.TaxCategoryAddTaxRateAction(**data)


class TaxCategoryChangeNameActionSchema(TaxCategoryUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.TaxCategoryChangeNameAction(**data)


class TaxCategoryRemoveTaxRateActionSchema(TaxCategoryUpdateActionSchema):
    tax_rate_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="taxRateId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.TaxCategoryRemoveTaxRateAction(**data)


class TaxCategoryReplaceTaxRateActionSchema(TaxCategoryUpdateActionSchema):
    tax_rate_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="taxRateId"
    )
    tax_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".TaxRateDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="taxRate",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.TaxCategoryReplaceTaxRateAction(**data)


class TaxCategorySetDescriptionActionSchema(TaxCategoryUpdateActionSchema):
    description = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.TaxCategorySetDescriptionAction(**data)


class TaxCategorySetKeyActionSchema(TaxCategoryUpdateActionSchema):
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.TaxCategorySetKeyAction(**data)
