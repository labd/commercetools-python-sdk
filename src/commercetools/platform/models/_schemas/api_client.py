# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models

# Fields


# Marshmallow Schemas
class ApiClientSchema(helpers.BaseSchema):
    id = marshmallow.fields.String(allow_none=True, missing=None)
    name = marshmallow.fields.String(allow_none=True, missing=None)
    scope = marshmallow.fields.String(allow_none=True, missing=None)
    created_at = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="createdAt",
    )
    last_used_at = marshmallow.fields.Date(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="lastUsedAt",
    )
    delete_at = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="deleteAt",
    )
    secret = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ApiClient(**data)


class ApiClientDraftSchema(helpers.BaseSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    scope = marshmallow.fields.String(allow_none=True, missing=None)
    delete_days_after_creation = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="deleteDaysAfterCreation",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ApiClientDraft(**data)


class ApiClientPagedQueryResponseSchema(helpers.BaseSchema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ApiClientSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ApiClientPagedQueryResponse(**data)
