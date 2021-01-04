# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from .common import ImportResourceSchema

# Fields


# Marshmallow Schemas
class InventoryImportSchema(ImportResourceSchema):
    sku = marshmallow.fields.String(allow_none=True, missing=None)
    quantity_on_stock = marshmallow.fields.Float(
        allow_none=True, missing=None, data_key="quantityOnStock"
    )
    restockable_in_days = marshmallow.fields.Float(
        allow_none=True, missing=None, data_key="restockableInDays"
    )
    expected_delivery = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="expectedDelivery"
    )
    supply_channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.ChannelKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="supplyChannel",
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customfields.CustomSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.InventoryImport(**data)
