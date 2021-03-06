# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..common import ReferenceTypeId
from .common import (
    BaseResourceSchema,
    KeyReferenceSchema,
    LocalizedStringField,
    ReferenceSchema,
    ResourceIdentifierSchema,
)

# Fields


# Marshmallow Schemas
class StoreSchema(BaseResourceSchema):
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
    name = LocalizedStringField(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    languages = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
    )
    distribution_channels = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelReferenceSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="distributionChannels",
    )
    supply_channels = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelReferenceSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="supplyChannels",
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Store(**data)


class StoreDraftSchema(helpers.BaseSchema):
    key = marshmallow.fields.String(allow_none=True, missing=None)
    name = LocalizedStringField(allow_none=True, missing=None)
    languages = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
    )
    distribution_channels = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelResourceIdentifierSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="distributionChannels",
    )
    supply_channels = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelResourceIdentifierSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="supplyChannels",
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.StoreDraft(**data)


class StoreKeyReferenceSchema(KeyReferenceSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.StoreKeyReference(**data)


class StorePagedQueryResponseSchema(helpers.BaseSchema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".StoreSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.StorePagedQueryResponse(**data)


class StoreReferenceSchema(ReferenceSchema):
    obj = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".StoreSchema"),
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
        return models.StoreReference(**data)


class StoreResourceIdentifierSchema(ResourceIdentifierSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.StoreResourceIdentifier(**data)


class StoreUpdateSchema(helpers.BaseSchema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addDistributionChannel": helpers.absmod(
                    __name__, ".StoreAddDistributionChannelActionSchema"
                ),
                "addSupplyChannel": helpers.absmod(
                    __name__, ".StoreAddSupplyChannelActionSchema"
                ),
                "removeDistributionChannel": helpers.absmod(
                    __name__, ".StoreRemoveDistributionChannelActionSchema"
                ),
                "removeSupplyChannel": helpers.absmod(
                    __name__, ".StoreRemoveSupplyChannelActionSchema"
                ),
                "setCustomField": helpers.absmod(
                    __name__, ".StoreSetCustomFieldActionSchema"
                ),
                "setCustomType": helpers.absmod(
                    __name__, ".StoreSetCustomTypeActionSchema"
                ),
                "setDistributionChannels": helpers.absmod(
                    __name__, ".StoreSetDistributionChannelsActionSchema"
                ),
                "setLanguages": helpers.absmod(
                    __name__, ".StoreSetLanguagesActionSchema"
                ),
                "setName": helpers.absmod(__name__, ".StoreSetNameActionSchema"),
                "setSupplyChannels": helpers.absmod(
                    __name__, ".StoreSetSupplyChannelsActionSchema"
                ),
            },
        ),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.StoreUpdate(**data)


class StoreUpdateActionSchema(helpers.BaseSchema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StoreUpdateAction(**data)


class StoreAddDistributionChannelActionSchema(StoreUpdateActionSchema):
    distribution_channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="distributionChannel",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StoreAddDistributionChannelAction(**data)


class StoreAddSupplyChannelActionSchema(StoreUpdateActionSchema):
    supply_channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="supplyChannel",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StoreAddSupplyChannelAction(**data)


class StoreRemoveDistributionChannelActionSchema(StoreUpdateActionSchema):
    distribution_channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="distributionChannel",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StoreRemoveDistributionChannelAction(**data)


class StoreRemoveSupplyChannelActionSchema(StoreUpdateActionSchema):
    supply_channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="supplyChannel",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StoreRemoveSupplyChannelAction(**data)


class StoreSetCustomFieldActionSchema(StoreUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StoreSetCustomFieldAction(**data)


class StoreSetCustomTypeActionSchema(StoreUpdateActionSchema):
    type = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.TypeResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    fields = marshmallow.fields.Raw(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StoreSetCustomTypeAction(**data)


class StoreSetDistributionChannelsActionSchema(StoreUpdateActionSchema):
    distribution_channels = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelResourceIdentifierSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="distributionChannels",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StoreSetDistributionChannelsAction(**data)


class StoreSetLanguagesActionSchema(StoreUpdateActionSchema):
    languages = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StoreSetLanguagesAction(**data)


class StoreSetNameActionSchema(StoreUpdateActionSchema):
    name = LocalizedStringField(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StoreSetNameAction(**data)


class StoreSetSupplyChannelsActionSchema(StoreUpdateActionSchema):
    supply_channels = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelResourceIdentifierSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="supplyChannels",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StoreSetSupplyChannelsAction(**data)
