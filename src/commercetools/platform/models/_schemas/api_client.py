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

# Fields


# Marshmallow Schemas
class ApiClientSchema(helpers.BaseSchema):
    id = marshmallow.fields.String(allow_none=True, load_default=None)
    name = marshmallow.fields.String(allow_none=True, load_default=None)
    scope = marshmallow.fields.String(allow_none=True, load_default=None)
    secret = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    last_used_at = marshmallow.fields.Date(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="lastUsedAt",
    )
    delete_at = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="deleteAt",
    )
    created_at = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="createdAt",
    )
    access_token_validity_seconds = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="accessTokenValiditySeconds",
    )
    refresh_token_validity_seconds = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="refreshTokenValiditySeconds",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ApiClient(**data)


class ApiClientDraftSchema(helpers.BaseSchema):
    name = marshmallow.fields.String(allow_none=True, load_default=None)
    scope = marshmallow.fields.String(allow_none=True, load_default=None)
    delete_days_after_creation = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="deleteDaysAfterCreation",
    )
    access_token_validity_seconds = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="accessTokenValiditySeconds",
    )
    refresh_token_validity_seconds = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="refreshTokenValiditySeconds",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ApiClientDraft(**data)


class ApiClientPagedQueryResponseSchema(helpers.BaseSchema):
    limit = marshmallow.fields.Integer(allow_none=True, load_default=None)
    offset = marshmallow.fields.Integer(allow_none=True, load_default=None)
    count = marshmallow.fields.Integer(allow_none=True, load_default=None)
    total = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ApiClientSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ApiClientPagedQueryResponse(**data)
