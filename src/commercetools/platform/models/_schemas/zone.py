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
class LocationSchema(helpers.BaseSchema):
    country = marshmallow.fields.String(allow_none=True, missing=None)
    state = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Location(**data)


class ZoneSchema(BaseResourceSchema):
    last_modified_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.LastModifiedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="lastModifiedBy",
    )
    created_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.CreatedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="createdBy",
    )
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    name = marshmallow.fields.String(allow_none=True, missing=None)
    description = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    locations = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".LocationSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Zone(**data)


class ZoneDraftSchema(helpers.BaseSchema):
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    name = marshmallow.fields.String(allow_none=True, missing=None)
    description = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    locations = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".LocationSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ZoneDraft(**data)


class ZonePagedQueryResponseSchema(helpers.BaseSchema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ZoneSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ZonePagedQueryResponse(**data)


class ZoneReferenceSchema(ReferenceSchema):
    obj = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ZoneSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.ZoneReference(**data)


class ZoneResourceIdentifierSchema(ResourceIdentifierSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.ZoneResourceIdentifier(**data)


class ZoneUpdateSchema(helpers.BaseSchema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addLocation": helpers.absmod(__name__, ".ZoneAddLocationActionSchema"),
                "changeName": helpers.absmod(__name__, ".ZoneChangeNameActionSchema"),
                "removeLocation": helpers.absmod(
                    __name__, ".ZoneRemoveLocationActionSchema"
                ),
                "setDescription": helpers.absmod(
                    __name__, ".ZoneSetDescriptionActionSchema"
                ),
                "setKey": helpers.absmod(__name__, ".ZoneSetKeyActionSchema"),
            },
        ),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ZoneUpdate(**data)


class ZoneUpdateActionSchema(helpers.BaseSchema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ZoneUpdateAction(**data)


class ZoneAddLocationActionSchema(ZoneUpdateActionSchema):
    location = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".LocationSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ZoneAddLocationAction(**data)


class ZoneChangeNameActionSchema(ZoneUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ZoneChangeNameAction(**data)


class ZoneRemoveLocationActionSchema(ZoneUpdateActionSchema):
    location = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".LocationSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ZoneRemoveLocationAction(**data)


class ZoneSetDescriptionActionSchema(ZoneUpdateActionSchema):
    description = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ZoneSetDescriptionAction(**data)


class ZoneSetKeyActionSchema(ZoneUpdateActionSchema):
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ZoneSetKeyAction(**data)
