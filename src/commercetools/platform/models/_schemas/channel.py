# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..channel import ChannelRoleEnum
from ..common import ReferenceTypeId
from .common import (
    BaseResourceSchema,
    LocalizedStringField,
    ReferenceSchema,
    ResourceIdentifierSchema,
)
from .type import FieldContainerField

# Fields


# Marshmallow Schemas
class ChannelSchema(BaseResourceSchema):
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
    key = marshmallow.fields.String(allow_none=True, missing=None)
    roles = marshmallow.fields.List(
        marshmallow_enum.EnumField(ChannelRoleEnum, by_value=True, allow_none=True),
        allow_none=True,
        missing=None,
    )
    name = LocalizedStringField(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    description = LocalizedStringField(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    review_rating_statistics = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".review.ReviewRatingStatisticsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="reviewRatingStatistics",
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    geo_location = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "Point": helpers.absmod(__name__, ".common.GeoJsonPointSchema")
        },
        metadata={"omit_empty": True},
        missing=None,
        data_key="geoLocation",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Channel(**data)


class ChannelDraftSchema(helpers.BaseSchema):
    key = marshmallow.fields.String(allow_none=True, missing=None)
    roles = marshmallow.fields.List(
        marshmallow_enum.EnumField(ChannelRoleEnum, by_value=True, allow_none=True),
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
    )
    name = LocalizedStringField(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    description = LocalizedStringField(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    geo_location = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "Point": helpers.absmod(__name__, ".common.GeoJsonPointSchema")
        },
        metadata={"omit_empty": True},
        missing=None,
        data_key="geoLocation",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ChannelDraft(**data)


class ChannelPagedQueryResponseSchema(helpers.BaseSchema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ChannelSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ChannelPagedQueryResponse(**data)


class ChannelReferenceSchema(ReferenceSchema):
    obj = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ChannelSchema"),
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
        return models.ChannelReference(**data)


class ChannelResourceIdentifierSchema(ResourceIdentifierSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.ChannelResourceIdentifier(**data)


class ChannelUpdateSchema(helpers.BaseSchema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addRoles": helpers.absmod(__name__, ".ChannelAddRolesActionSchema"),
                "changeDescription": helpers.absmod(
                    __name__, ".ChannelChangeDescriptionActionSchema"
                ),
                "changeKey": helpers.absmod(__name__, ".ChannelChangeKeyActionSchema"),
                "changeName": helpers.absmod(
                    __name__, ".ChannelChangeNameActionSchema"
                ),
                "removeRoles": helpers.absmod(
                    __name__, ".ChannelRemoveRolesActionSchema"
                ),
                "setAddress": helpers.absmod(
                    __name__, ".ChannelSetAddressActionSchema"
                ),
                "setCustomField": helpers.absmod(
                    __name__, ".ChannelSetCustomFieldActionSchema"
                ),
                "setCustomType": helpers.absmod(
                    __name__, ".ChannelSetCustomTypeActionSchema"
                ),
                "setGeoLocation": helpers.absmod(
                    __name__, ".ChannelSetGeoLocationActionSchema"
                ),
                "setRoles": helpers.absmod(__name__, ".ChannelSetRolesActionSchema"),
            },
        ),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ChannelUpdate(**data)


class ChannelUpdateActionSchema(helpers.BaseSchema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ChannelUpdateAction(**data)


class ChannelAddRolesActionSchema(ChannelUpdateActionSchema):
    roles = marshmallow.fields.List(
        marshmallow_enum.EnumField(ChannelRoleEnum, by_value=True, allow_none=True),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ChannelAddRolesAction(**data)


class ChannelChangeDescriptionActionSchema(ChannelUpdateActionSchema):
    description = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ChannelChangeDescriptionAction(**data)


class ChannelChangeKeyActionSchema(ChannelUpdateActionSchema):
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ChannelChangeKeyAction(**data)


class ChannelChangeNameActionSchema(ChannelUpdateActionSchema):
    name = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ChannelChangeNameAction(**data)


class ChannelRemoveRolesActionSchema(ChannelUpdateActionSchema):
    roles = marshmallow.fields.List(
        marshmallow_enum.EnumField(ChannelRoleEnum, by_value=True, allow_none=True),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ChannelRemoveRolesAction(**data)


class ChannelSetAddressActionSchema(ChannelUpdateActionSchema):
    address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ChannelSetAddressAction(**data)


class ChannelSetCustomFieldActionSchema(ChannelUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ChannelSetCustomFieldAction(**data)


class ChannelSetCustomTypeActionSchema(ChannelUpdateActionSchema):
    type = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.TypeResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    fields = FieldContainerField(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ChannelSetCustomTypeAction(**data)


class ChannelSetGeoLocationActionSchema(ChannelUpdateActionSchema):
    geo_location = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "Point": helpers.absmod(__name__, ".common.GeoJsonPointSchema")
        },
        metadata={"omit_empty": True},
        missing=None,
        data_key="geoLocation",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ChannelSetGeoLocationAction(**data)


class ChannelSetRolesActionSchema(ChannelUpdateActionSchema):
    roles = marshmallow.fields.List(
        marshmallow_enum.EnumField(ChannelRoleEnum, by_value=True, allow_none=True),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ChannelSetRolesAction(**data)
