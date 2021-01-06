# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models

# Fields


# Marshmallow Schemas
class GraphQLErrorSchema(helpers.BaseSchema):
    message = marshmallow.fields.String(allow_none=True, missing=None)
    locations = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".GraphQLErrorLocationSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    path = marshmallow.fields.List(
        marshmallow.fields.Raw(allow_none=True), allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.GraphQLError(**data)


class GraphQLErrorLocationSchema(helpers.BaseSchema):
    line = marshmallow.fields.Integer(allow_none=True, missing=None)
    column = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.GraphQLErrorLocation(**data)


class GraphQLRequestSchema(helpers.BaseSchema):
    query = marshmallow.fields.String(allow_none=True, missing=None)
    operation_name = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="operationName",
    )
    variables = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".GraphQLVariablesMapSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.GraphQLRequest(**data)


class GraphQLResponseSchema(helpers.BaseSchema):
    data = marshmallow.fields.Raw(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    errors = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".GraphQLErrorSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.GraphQLResponse(**data)


class GraphQLVariablesMapSchema(helpers.BaseSchema):
    _regex = helpers.RegexField(
        unknown=marshmallow.EXCLUDE,
        pattern=re.compile(""),
        type=helpers.LazyNestedField(
            nested=helpers.absmod(__name__, "...marshmallow.fields.Raw"),
            unknown=marshmallow.EXCLUDE,
            allow_none=True,
            many=True,
        ),
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        data = typing.cast(helpers.RegexField, self.fields["_regex"]).postprocess(data)
        return models.GraphQLVariablesMap(**data)

    @marshmallow.pre_load
    def pre_load(self, data, **kwargs):
        data = typing.cast(helpers.RegexField, self.fields["_regex"]).preprocess(data)
        return data

    @marshmallow.pre_dump
    def pre_dump(self, data, **kwargs):
        data = typing.cast(helpers.RegexField, self.fields["_regex"]).preprocess(data)
        return data

    @marshmallow.post_dump
    def post_dump(self, data, **kwargs):
        data = typing.cast(helpers.RegexField, self.fields["_regex"]).postprocess(data)
        return data
