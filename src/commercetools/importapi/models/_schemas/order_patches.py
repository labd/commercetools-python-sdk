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
from ..order_patches import ReturnShipmentState

# Fields


# Marshmallow Schemas


class ReturnItemDraftSchema(helpers.BaseSchema):
    quantity = marshmallow.fields.Float(allow_none=True, missing=None)
    line_item_id = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="lineItemId",
    )
    custom_line_item_id = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="customLineItemId",
    )
    comment = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    shipment_state = marshmallow_enum.EnumField(
        ReturnShipmentState,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="shipmentState",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ReturnItemDraft(**data)


class ReturnInfoSchema(helpers.BaseSchema):
    items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ReturnItemDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    return_tracking_id = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="returnTrackingId",
    )
    return_date = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="returnDate",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ReturnInfo(**data)


class DeliveryParcelSchema(helpers.BaseSchema):
    delivery_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="deliveryId"
    )
    measurements = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".orders.ParcelMeasurementsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    tracking_data = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".orders.TrackingDataSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="trackingData",
    )
    items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".orders.DeliveryItemSchema"),
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

        return models.DeliveryParcel(**data)


class DeliveryParcelDraftSchema(helpers.BaseSchema):
    measurements = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".orders.ParcelMeasurementsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    tracking_data = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".orders.TrackingDataSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="trackingData",
    )
    items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".orders.DeliveryItemSchema"),
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

        return models.DeliveryParcelDraft(**data)


class DeliveryDraftSchema(helpers.BaseSchema):
    items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".orders.DeliveryItemSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    parcels = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".DeliveryParcelDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.DeliveryDraft(**data)


class DeliveryAddressDraftSchema(helpers.BaseSchema):
    delivery_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="deliveryId"
    )
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

        return models.DeliveryAddressDraft(**data)


class ParcelMeasurementDraftSchema(helpers.BaseSchema):
    parcel_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="parcelId"
    )
    measurements = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".orders.ParcelMeasurementsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ParcelMeasurementDraft(**data)


class ParcelTrackingDataSchema(helpers.BaseSchema):
    parcel_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="parcelId"
    )
    tracking_data = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".orders.TrackingDataSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="trackingData",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ParcelTrackingData(**data)


class ParcelItemsSchema(helpers.BaseSchema):
    parcel_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="parcelId"
    )
    items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".orders.DeliveryItemSchema"),
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

        return models.ParcelItems(**data)


class RemoveDeliveryDraftSchema(helpers.BaseSchema):
    id = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.RemoveDeliveryDraft(**data)


class RemoveParcelFromDeliveryDraftSchema(helpers.BaseSchema):
    parcel_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="parcelId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.RemoveParcelFromDeliveryDraft(**data)


class OrderFieldSchema(helpers.BaseSchema):
    add_return_info = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ReturnInfoSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="addReturnInfo",
    )
    add_parcel_to_delivery = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".DeliveryParcelSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="addParcelToDelivery",
    )
    add_deliveries = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".DeliveryDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="addDeliveries",
    )
    remove_delivery = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".RemoveDeliveryDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="removeDelivery",
    )
    remove_parcel_from_delivery = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".RemoveParcelFromDeliveryDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="removeParcelFromDelivery",
    )
    set_delivery_address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".DeliveryAddressDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="setDeliveryAddress",
    )
    set_parcel_measurements = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ParcelMeasurementDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="setParcelMeasurements",
    )
    set_parcel_tracking_data = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ParcelTrackingDataSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="setParcelTrackingData",
    )
    set_parcel_items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ParcelItemsSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="setParcelItems",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.OrderField(**data)


class OrderPatchImportSchema(helpers.BaseSchema):
    order_number = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="orderNumber"
    )
    fields = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".OrderFieldSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.OrderPatchImport(**data)