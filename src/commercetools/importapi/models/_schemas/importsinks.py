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
class ImportSinkSchema(helpers.BaseSchema):
    key = marshmallow.fields.String(allow_none=True, missing=None)
    resource_type = marshmallow_enum.EnumField(
        ImportResourceType,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="resourceType",
    )
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    created_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="createdAt"
    )
    last_modified_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="lastModifiedAt"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ImportSink(**data)


class ImportSinkDraftSchema(helpers.BaseSchema):
    version = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    key = marshmallow.fields.String(allow_none=True, missing=None)
    resource_type = marshmallow_enum.EnumField(
        ImportResourceType,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="resourceType",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ImportSinkDraft(**data)


class ImportSinkPagedResponseSchema(helpers.BaseSchema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ImportSinkSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ImportSinkPagedResponse(**data)
