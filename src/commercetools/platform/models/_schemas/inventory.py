# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..common import ReferenceTypeId
from .common import BaseResourceSchema, ReferenceSchema, ResourceIdentifierSchema
from .type import FieldContainerField

# Fields


# Marshmallow Schemas
class InventoryEntrySchema(BaseResourceSchema):
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
    sku = marshmallow.fields.String(allow_none=True, missing=None)
    supply_channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="supplyChannel",
    )
    quantity_on_stock = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="quantityOnStock"
    )
    available_quantity = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="availableQuantity"
    )
    restockable_in_days = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="restockableInDays",
    )
    expected_delivery = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="expectedDelivery",
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

        return models.InventoryEntry(**data)


class InventoryEntryDraftSchema(helpers.BaseSchema):
    sku = marshmallow.fields.String(allow_none=True, missing=None)
    supply_channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="supplyChannel",
    )
    quantity_on_stock = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="quantityOnStock"
    )
    restockable_in_days = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="restockableInDays",
    )
    expected_delivery = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="expectedDelivery",
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

        return models.InventoryEntryDraft(**data)


class InventoryEntryReferenceSchema(ReferenceSchema):
    obj = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".InventoryEntrySchema"),
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
        return models.InventoryEntryReference(**data)


class InventoryEntryResourceIdentifierSchema(ResourceIdentifierSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.InventoryEntryResourceIdentifier(**data)


class InventoryEntryUpdateSchema(helpers.BaseSchema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addQuantity": helpers.absmod(
                    __name__, ".InventoryEntryAddQuantityActionSchema"
                ),
                "changeQuantity": helpers.absmod(
                    __name__, ".InventoryEntryChangeQuantityActionSchema"
                ),
                "removeQuantity": helpers.absmod(
                    __name__, ".InventoryEntryRemoveQuantityActionSchema"
                ),
                "setCustomField": helpers.absmod(
                    __name__, ".InventoryEntrySetCustomFieldActionSchema"
                ),
                "setCustomType": helpers.absmod(
                    __name__, ".InventoryEntrySetCustomTypeActionSchema"
                ),
                "setExpectedDelivery": helpers.absmod(
                    __name__, ".InventoryEntrySetExpectedDeliveryActionSchema"
                ),
                "setRestockableInDays": helpers.absmod(
                    __name__, ".InventoryEntrySetRestockableInDaysActionSchema"
                ),
                "setSupplyChannel": helpers.absmod(
                    __name__, ".InventoryEntrySetSupplyChannelActionSchema"
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

        return models.InventoryEntryUpdate(**data)


class InventoryEntryUpdateActionSchema(helpers.BaseSchema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.InventoryEntryUpdateAction(**data)


class InventoryPagedQueryResponseSchema(helpers.BaseSchema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".InventoryEntrySchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.InventoryPagedQueryResponse(**data)


class InventoryEntryAddQuantityActionSchema(InventoryEntryUpdateActionSchema):
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.InventoryEntryAddQuantityAction(**data)


class InventoryEntryChangeQuantityActionSchema(InventoryEntryUpdateActionSchema):
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.InventoryEntryChangeQuantityAction(**data)


class InventoryEntryRemoveQuantityActionSchema(InventoryEntryUpdateActionSchema):
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.InventoryEntryRemoveQuantityAction(**data)


class InventoryEntrySetCustomFieldActionSchema(InventoryEntryUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.InventoryEntrySetCustomFieldAction(**data)


class InventoryEntrySetCustomTypeActionSchema(InventoryEntryUpdateActionSchema):
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
        return models.InventoryEntrySetCustomTypeAction(**data)


class InventoryEntrySetExpectedDeliveryActionSchema(InventoryEntryUpdateActionSchema):
    expected_delivery = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="expectedDelivery",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.InventoryEntrySetExpectedDeliveryAction(**data)


class InventoryEntrySetRestockableInDaysActionSchema(InventoryEntryUpdateActionSchema):
    restockable_in_days = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="restockableInDays",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.InventoryEntrySetRestockableInDaysAction(**data)


class InventoryEntrySetSupplyChannelActionSchema(InventoryEntryUpdateActionSchema):
    supply_channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="supplyChannel",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.InventoryEntrySetSupplyChannelAction(**data)
