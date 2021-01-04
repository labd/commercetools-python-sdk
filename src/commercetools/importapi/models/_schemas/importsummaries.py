# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models

# Fields


# Marshmallow Schemas
class ImportSummarySchema(marshmallow.Schema):
    states = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".OperationStatesSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    total = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ImportSummary(**data)


class OperationStatesSchema(marshmallow.Schema):
    validation_failed = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="ValidationFailed"
    )
    unresolved = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="Unresolved"
    )
    wait_for_master_variant = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="WaitForMasterVariant"
    )
    imported = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="Imported"
    )
    delete = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="Delete"
    )
    deleted = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="Deleted"
    )
    rejected = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="Rejected"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.OperationStates(**data)
