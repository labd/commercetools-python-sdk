# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..cart import CartOrigin, InventoryMode, RoundingMode, TaxCalculationMode, TaxMode
from ..common import ReferenceTypeId
from ..order import (
    OrderState,
    PaymentState,
    ReturnPaymentState,
    ReturnShipmentState,
    ShipmentState,
)
from .common import (
    BaseResourceSchema,
    LocalizedStringField,
    ReferenceSchema,
    ResourceIdentifierSchema,
)
from .order import OrderSchema, StagedOrderUpdateActionSchema
from .type import FieldContainerField

# Fields


# Marshmallow Schemas
class OrderEditSchema(BaseResourceSchema):
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
    resource = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.OrderReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    staged_actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addCustomLineItem": helpers.absmod(
                    __name__, ".StagedOrderAddCustomLineItemActionSchema"
                ),
                "addDelivery": helpers.absmod(
                    __name__, ".StagedOrderAddDeliveryActionSchema"
                ),
                "addDiscountCode": helpers.absmod(
                    __name__, ".StagedOrderAddDiscountCodeActionSchema"
                ),
                "addItemShippingAddress": helpers.absmod(
                    __name__, ".StagedOrderAddItemShippingAddressActionSchema"
                ),
                "addLineItem": helpers.absmod(
                    __name__, ".StagedOrderAddLineItemActionSchema"
                ),
                "addParcelToDelivery": helpers.absmod(
                    __name__, ".StagedOrderAddParcelToDeliveryActionSchema"
                ),
                "addPayment": helpers.absmod(
                    __name__, ".StagedOrderAddPaymentActionSchema"
                ),
                "addReturnInfo": helpers.absmod(
                    __name__, ".StagedOrderAddReturnInfoActionSchema"
                ),
                "addShoppingList": helpers.absmod(
                    __name__, ".StagedOrderAddShoppingListActionSchema"
                ),
                "changeCustomLineItemMoney": helpers.absmod(
                    __name__, ".StagedOrderChangeCustomLineItemMoneyActionSchema"
                ),
                "changeCustomLineItemQuantity": helpers.absmod(
                    __name__, ".StagedOrderChangeCustomLineItemQuantityActionSchema"
                ),
                "changeLineItemQuantity": helpers.absmod(
                    __name__, ".StagedOrderChangeLineItemQuantityActionSchema"
                ),
                "changeOrderState": helpers.absmod(
                    __name__, ".StagedOrderChangeOrderStateActionSchema"
                ),
                "changePaymentState": helpers.absmod(
                    __name__, ".StagedOrderChangePaymentStateActionSchema"
                ),
                "changeShipmentState": helpers.absmod(
                    __name__, ".StagedOrderChangeShipmentStateActionSchema"
                ),
                "changeTaxCalculationMode": helpers.absmod(
                    __name__, ".StagedOrderChangeTaxCalculationModeActionSchema"
                ),
                "changeTaxMode": helpers.absmod(
                    __name__, ".StagedOrderChangeTaxModeActionSchema"
                ),
                "changeTaxRoundingMode": helpers.absmod(
                    __name__, ".StagedOrderChangeTaxRoundingModeActionSchema"
                ),
                "importCustomLineItemState": helpers.absmod(
                    __name__, ".StagedOrderImportCustomLineItemStateActionSchema"
                ),
                "importLineItemState": helpers.absmod(
                    __name__, ".StagedOrderImportLineItemStateActionSchema"
                ),
                "removeCustomLineItem": helpers.absmod(
                    __name__, ".StagedOrderRemoveCustomLineItemActionSchema"
                ),
                "removeDelivery": helpers.absmod(
                    __name__, ".StagedOrderRemoveDeliveryActionSchema"
                ),
                "removeDiscountCode": helpers.absmod(
                    __name__, ".StagedOrderRemoveDiscountCodeActionSchema"
                ),
                "removeItemShippingAddress": helpers.absmod(
                    __name__, ".StagedOrderRemoveItemShippingAddressActionSchema"
                ),
                "removeLineItem": helpers.absmod(
                    __name__, ".StagedOrderRemoveLineItemActionSchema"
                ),
                "removeParcelFromDelivery": helpers.absmod(
                    __name__, ".StagedOrderRemoveParcelFromDeliveryActionSchema"
                ),
                "removePayment": helpers.absmod(
                    __name__, ".StagedOrderRemovePaymentActionSchema"
                ),
                "setBillingAddress": helpers.absmod(
                    __name__, ".StagedOrderSetBillingAddressActionSchema"
                ),
                "setCountry": helpers.absmod(
                    __name__, ".StagedOrderSetCountryActionSchema"
                ),
                "setCustomField": helpers.absmod(
                    __name__, ".StagedOrderSetCustomFieldActionSchema"
                ),
                "setCustomLineItemCustomField": helpers.absmod(
                    __name__, ".StagedOrderSetCustomLineItemCustomFieldActionSchema"
                ),
                "setCustomLineItemCustomType": helpers.absmod(
                    __name__, ".StagedOrderSetCustomLineItemCustomTypeActionSchema"
                ),
                "setCustomLineItemShippingDetails": helpers.absmod(
                    __name__, ".StagedOrderSetCustomLineItemShippingDetailsActionSchema"
                ),
                "setCustomLineItemTaxAmount": helpers.absmod(
                    __name__, ".StagedOrderSetCustomLineItemTaxAmountActionSchema"
                ),
                "setCustomLineItemTaxRate": helpers.absmod(
                    __name__, ".StagedOrderSetCustomLineItemTaxRateActionSchema"
                ),
                "setCustomShippingMethod": helpers.absmod(
                    __name__, ".StagedOrderSetCustomShippingMethodActionSchema"
                ),
                "setCustomType": helpers.absmod(
                    __name__, ".StagedOrderSetCustomTypeActionSchema"
                ),
                "setCustomerEmail": helpers.absmod(
                    __name__, ".StagedOrderSetCustomerEmailActionSchema"
                ),
                "setCustomerGroup": helpers.absmod(
                    __name__, ".StagedOrderSetCustomerGroupActionSchema"
                ),
                "setCustomerId": helpers.absmod(
                    __name__, ".StagedOrderSetCustomerIdActionSchema"
                ),
                "setDeliveryAddress": helpers.absmod(
                    __name__, ".StagedOrderSetDeliveryAddressActionSchema"
                ),
                "setDeliveryItems": helpers.absmod(
                    __name__, ".StagedOrderSetDeliveryItemsActionSchema"
                ),
                "setLineItemCustomField": helpers.absmod(
                    __name__, ".StagedOrderSetLineItemCustomFieldActionSchema"
                ),
                "setLineItemCustomType": helpers.absmod(
                    __name__, ".StagedOrderSetLineItemCustomTypeActionSchema"
                ),
                "setLineItemDistributionChannel": helpers.absmod(
                    __name__, ".StagedOrderSetLineItemDistributionChannelActionSchema"
                ),
                "setLineItemPrice": helpers.absmod(
                    __name__, ".StagedOrderSetLineItemPriceActionSchema"
                ),
                "setLineItemShippingDetails": helpers.absmod(
                    __name__, ".StagedOrderSetLineItemShippingDetailsActionSchema"
                ),
                "setLineItemTaxAmount": helpers.absmod(
                    __name__, ".StagedOrderSetLineItemTaxAmountActionSchema"
                ),
                "setLineItemTaxRate": helpers.absmod(
                    __name__, ".StagedOrderSetLineItemTaxRateActionSchema"
                ),
                "setLineItemTotalPrice": helpers.absmod(
                    __name__, ".StagedOrderSetLineItemTotalPriceActionSchema"
                ),
                "setLocale": helpers.absmod(
                    __name__, ".StagedOrderSetLocaleActionSchema"
                ),
                "setOrderNumber": helpers.absmod(
                    __name__, ".StagedOrderSetOrderNumberActionSchema"
                ),
                "setOrderTotalTax": helpers.absmod(
                    __name__, ".StagedOrderSetOrderTotalTaxActionSchema"
                ),
                "setParcelItems": helpers.absmod(
                    __name__, ".StagedOrderSetParcelItemsActionSchema"
                ),
                "setParcelMeasurements": helpers.absmod(
                    __name__, ".StagedOrderSetParcelMeasurementsActionSchema"
                ),
                "setParcelTrackingData": helpers.absmod(
                    __name__, ".StagedOrderSetParcelTrackingDataActionSchema"
                ),
                "setReturnPaymentState": helpers.absmod(
                    __name__, ".StagedOrderSetReturnPaymentStateActionSchema"
                ),
                "setReturnShipmentState": helpers.absmod(
                    __name__, ".StagedOrderSetReturnShipmentStateActionSchema"
                ),
                "setShippingAddress": helpers.absmod(
                    __name__, ".StagedOrderSetShippingAddressActionSchema"
                ),
                "setShippingAddressAndCustomShippingMethod": helpers.absmod(
                    __name__,
                    ".StagedOrderSetShippingAddressAndCustomShippingMethodActionSchema",
                ),
                "setShippingAddressAndShippingMethod": helpers.absmod(
                    __name__,
                    ".StagedOrderSetShippingAddressAndShippingMethodActionSchema",
                ),
                "setShippingMethod": helpers.absmod(
                    __name__, ".StagedOrderSetShippingMethodActionSchema"
                ),
                "setShippingMethodTaxAmount": helpers.absmod(
                    __name__, ".StagedOrderSetShippingMethodTaxAmountActionSchema"
                ),
                "setShippingMethodTaxRate": helpers.absmod(
                    __name__, ".StagedOrderSetShippingMethodTaxRateActionSchema"
                ),
                "setShippingRateInput": helpers.absmod(
                    __name__, ".StagedOrderSetShippingRateInputActionSchema"
                ),
                "transitionCustomLineItemState": helpers.absmod(
                    __name__, ".StagedOrderTransitionCustomLineItemStateActionSchema"
                ),
                "transitionLineItemState": helpers.absmod(
                    __name__, ".StagedOrderTransitionLineItemStateActionSchema"
                ),
                "transitionState": helpers.absmod(
                    __name__, ".StagedOrderTransitionStateActionSchema"
                ),
                "updateItemShippingAddress": helpers.absmod(
                    __name__, ".StagedOrderUpdateItemShippingAddressActionSchema"
                ),
                "updateSyncInfo": helpers.absmod(
                    __name__, ".StagedOrderUpdateSyncInfoActionSchema"
                ),
            },
        ),
        allow_none=True,
        missing=None,
        data_key="stagedActions",
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    result = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "Applied": helpers.absmod(__name__, ".OrderEditAppliedSchema"),
            "NotProcessed": helpers.absmod(__name__, ".OrderEditNotProcessedSchema"),
            "PreviewFailure": helpers.absmod(
                __name__, ".OrderEditPreviewFailureSchema"
            ),
            "PreviewSuccess": helpers.absmod(
                __name__, ".OrderEditPreviewSuccessSchema"
            ),
        },
        missing=None,
    )
    comment = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.OrderEdit(**data)


class OrderEditApplySchema(helpers.BaseSchema):
    edit_version = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="editVersion"
    )
    resource_version = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="resourceVersion"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.OrderEditApply(**data)


class OrderEditDraftSchema(helpers.BaseSchema):
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    resource = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.OrderReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    staged_actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addCustomLineItem": helpers.absmod(
                    __name__, ".StagedOrderAddCustomLineItemActionSchema"
                ),
                "addDelivery": helpers.absmod(
                    __name__, ".StagedOrderAddDeliveryActionSchema"
                ),
                "addDiscountCode": helpers.absmod(
                    __name__, ".StagedOrderAddDiscountCodeActionSchema"
                ),
                "addItemShippingAddress": helpers.absmod(
                    __name__, ".StagedOrderAddItemShippingAddressActionSchema"
                ),
                "addLineItem": helpers.absmod(
                    __name__, ".StagedOrderAddLineItemActionSchema"
                ),
                "addParcelToDelivery": helpers.absmod(
                    __name__, ".StagedOrderAddParcelToDeliveryActionSchema"
                ),
                "addPayment": helpers.absmod(
                    __name__, ".StagedOrderAddPaymentActionSchema"
                ),
                "addReturnInfo": helpers.absmod(
                    __name__, ".StagedOrderAddReturnInfoActionSchema"
                ),
                "addShoppingList": helpers.absmod(
                    __name__, ".StagedOrderAddShoppingListActionSchema"
                ),
                "changeCustomLineItemMoney": helpers.absmod(
                    __name__, ".StagedOrderChangeCustomLineItemMoneyActionSchema"
                ),
                "changeCustomLineItemQuantity": helpers.absmod(
                    __name__, ".StagedOrderChangeCustomLineItemQuantityActionSchema"
                ),
                "changeLineItemQuantity": helpers.absmod(
                    __name__, ".StagedOrderChangeLineItemQuantityActionSchema"
                ),
                "changeOrderState": helpers.absmod(
                    __name__, ".StagedOrderChangeOrderStateActionSchema"
                ),
                "changePaymentState": helpers.absmod(
                    __name__, ".StagedOrderChangePaymentStateActionSchema"
                ),
                "changeShipmentState": helpers.absmod(
                    __name__, ".StagedOrderChangeShipmentStateActionSchema"
                ),
                "changeTaxCalculationMode": helpers.absmod(
                    __name__, ".StagedOrderChangeTaxCalculationModeActionSchema"
                ),
                "changeTaxMode": helpers.absmod(
                    __name__, ".StagedOrderChangeTaxModeActionSchema"
                ),
                "changeTaxRoundingMode": helpers.absmod(
                    __name__, ".StagedOrderChangeTaxRoundingModeActionSchema"
                ),
                "importCustomLineItemState": helpers.absmod(
                    __name__, ".StagedOrderImportCustomLineItemStateActionSchema"
                ),
                "importLineItemState": helpers.absmod(
                    __name__, ".StagedOrderImportLineItemStateActionSchema"
                ),
                "removeCustomLineItem": helpers.absmod(
                    __name__, ".StagedOrderRemoveCustomLineItemActionSchema"
                ),
                "removeDelivery": helpers.absmod(
                    __name__, ".StagedOrderRemoveDeliveryActionSchema"
                ),
                "removeDiscountCode": helpers.absmod(
                    __name__, ".StagedOrderRemoveDiscountCodeActionSchema"
                ),
                "removeItemShippingAddress": helpers.absmod(
                    __name__, ".StagedOrderRemoveItemShippingAddressActionSchema"
                ),
                "removeLineItem": helpers.absmod(
                    __name__, ".StagedOrderRemoveLineItemActionSchema"
                ),
                "removeParcelFromDelivery": helpers.absmod(
                    __name__, ".StagedOrderRemoveParcelFromDeliveryActionSchema"
                ),
                "removePayment": helpers.absmod(
                    __name__, ".StagedOrderRemovePaymentActionSchema"
                ),
                "setBillingAddress": helpers.absmod(
                    __name__, ".StagedOrderSetBillingAddressActionSchema"
                ),
                "setCountry": helpers.absmod(
                    __name__, ".StagedOrderSetCountryActionSchema"
                ),
                "setCustomField": helpers.absmod(
                    __name__, ".StagedOrderSetCustomFieldActionSchema"
                ),
                "setCustomLineItemCustomField": helpers.absmod(
                    __name__, ".StagedOrderSetCustomLineItemCustomFieldActionSchema"
                ),
                "setCustomLineItemCustomType": helpers.absmod(
                    __name__, ".StagedOrderSetCustomLineItemCustomTypeActionSchema"
                ),
                "setCustomLineItemShippingDetails": helpers.absmod(
                    __name__, ".StagedOrderSetCustomLineItemShippingDetailsActionSchema"
                ),
                "setCustomLineItemTaxAmount": helpers.absmod(
                    __name__, ".StagedOrderSetCustomLineItemTaxAmountActionSchema"
                ),
                "setCustomLineItemTaxRate": helpers.absmod(
                    __name__, ".StagedOrderSetCustomLineItemTaxRateActionSchema"
                ),
                "setCustomShippingMethod": helpers.absmod(
                    __name__, ".StagedOrderSetCustomShippingMethodActionSchema"
                ),
                "setCustomType": helpers.absmod(
                    __name__, ".StagedOrderSetCustomTypeActionSchema"
                ),
                "setCustomerEmail": helpers.absmod(
                    __name__, ".StagedOrderSetCustomerEmailActionSchema"
                ),
                "setCustomerGroup": helpers.absmod(
                    __name__, ".StagedOrderSetCustomerGroupActionSchema"
                ),
                "setCustomerId": helpers.absmod(
                    __name__, ".StagedOrderSetCustomerIdActionSchema"
                ),
                "setDeliveryAddress": helpers.absmod(
                    __name__, ".StagedOrderSetDeliveryAddressActionSchema"
                ),
                "setDeliveryItems": helpers.absmod(
                    __name__, ".StagedOrderSetDeliveryItemsActionSchema"
                ),
                "setLineItemCustomField": helpers.absmod(
                    __name__, ".StagedOrderSetLineItemCustomFieldActionSchema"
                ),
                "setLineItemCustomType": helpers.absmod(
                    __name__, ".StagedOrderSetLineItemCustomTypeActionSchema"
                ),
                "setLineItemDistributionChannel": helpers.absmod(
                    __name__, ".StagedOrderSetLineItemDistributionChannelActionSchema"
                ),
                "setLineItemPrice": helpers.absmod(
                    __name__, ".StagedOrderSetLineItemPriceActionSchema"
                ),
                "setLineItemShippingDetails": helpers.absmod(
                    __name__, ".StagedOrderSetLineItemShippingDetailsActionSchema"
                ),
                "setLineItemTaxAmount": helpers.absmod(
                    __name__, ".StagedOrderSetLineItemTaxAmountActionSchema"
                ),
                "setLineItemTaxRate": helpers.absmod(
                    __name__, ".StagedOrderSetLineItemTaxRateActionSchema"
                ),
                "setLineItemTotalPrice": helpers.absmod(
                    __name__, ".StagedOrderSetLineItemTotalPriceActionSchema"
                ),
                "setLocale": helpers.absmod(
                    __name__, ".StagedOrderSetLocaleActionSchema"
                ),
                "setOrderNumber": helpers.absmod(
                    __name__, ".StagedOrderSetOrderNumberActionSchema"
                ),
                "setOrderTotalTax": helpers.absmod(
                    __name__, ".StagedOrderSetOrderTotalTaxActionSchema"
                ),
                "setParcelItems": helpers.absmod(
                    __name__, ".StagedOrderSetParcelItemsActionSchema"
                ),
                "setParcelMeasurements": helpers.absmod(
                    __name__, ".StagedOrderSetParcelMeasurementsActionSchema"
                ),
                "setParcelTrackingData": helpers.absmod(
                    __name__, ".StagedOrderSetParcelTrackingDataActionSchema"
                ),
                "setReturnPaymentState": helpers.absmod(
                    __name__, ".StagedOrderSetReturnPaymentStateActionSchema"
                ),
                "setReturnShipmentState": helpers.absmod(
                    __name__, ".StagedOrderSetReturnShipmentStateActionSchema"
                ),
                "setShippingAddress": helpers.absmod(
                    __name__, ".StagedOrderSetShippingAddressActionSchema"
                ),
                "setShippingAddressAndCustomShippingMethod": helpers.absmod(
                    __name__,
                    ".StagedOrderSetShippingAddressAndCustomShippingMethodActionSchema",
                ),
                "setShippingAddressAndShippingMethod": helpers.absmod(
                    __name__,
                    ".StagedOrderSetShippingAddressAndShippingMethodActionSchema",
                ),
                "setShippingMethod": helpers.absmod(
                    __name__, ".StagedOrderSetShippingMethodActionSchema"
                ),
                "setShippingMethodTaxAmount": helpers.absmod(
                    __name__, ".StagedOrderSetShippingMethodTaxAmountActionSchema"
                ),
                "setShippingMethodTaxRate": helpers.absmod(
                    __name__, ".StagedOrderSetShippingMethodTaxRateActionSchema"
                ),
                "setShippingRateInput": helpers.absmod(
                    __name__, ".StagedOrderSetShippingRateInputActionSchema"
                ),
                "transitionCustomLineItemState": helpers.absmod(
                    __name__, ".StagedOrderTransitionCustomLineItemStateActionSchema"
                ),
                "transitionLineItemState": helpers.absmod(
                    __name__, ".StagedOrderTransitionLineItemStateActionSchema"
                ),
                "transitionState": helpers.absmod(
                    __name__, ".StagedOrderTransitionStateActionSchema"
                ),
                "updateItemShippingAddress": helpers.absmod(
                    __name__, ".StagedOrderUpdateItemShippingAddressActionSchema"
                ),
                "updateSyncInfo": helpers.absmod(
                    __name__, ".StagedOrderUpdateSyncInfoActionSchema"
                ),
            },
        ),
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="stagedActions",
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    comment = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    dry_run = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None, data_key="dryRun"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.OrderEditDraft(**data)


class OrderEditPagedQueryResponseSchema(helpers.BaseSchema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".OrderEditSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.OrderEditPagedQueryResponse(**data)


class OrderEditReferenceSchema(ReferenceSchema):
    obj = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".OrderEditSchema"),
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
        return models.OrderEditReference(**data)


class OrderEditResourceIdentifierSchema(ResourceIdentifierSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.OrderEditResourceIdentifier(**data)


class OrderEditResultSchema(helpers.BaseSchema):
    type = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderEditResult(**data)


class OrderEditAppliedSchema(OrderEditResultSchema):
    applied_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="appliedAt"
    )
    excerpt_before_edit = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".OrderExcerptSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="excerptBeforeEdit",
    )
    excerpt_after_edit = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".OrderExcerptSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="excerptAfterEdit",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderEditApplied(**data)


class OrderEditNotProcessedSchema(OrderEditResultSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderEditNotProcessed(**data)


class OrderEditPreviewFailureSchema(OrderEditResultSchema):
    errors = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("code", "code"),
            discriminator_schemas={
                "access_denied": helpers.absmod(
                    __name__, ".error.AccessDeniedErrorSchema"
                ),
                "AnonymousIdAlreadyInUse": helpers.absmod(
                    __name__, ".error.AnonymousIdAlreadyInUseErrorSchema"
                ),
                "AttributeDefinitionAlreadyExists": helpers.absmod(
                    __name__, ".error.AttributeDefinitionAlreadyExistsErrorSchema"
                ),
                "AttributeDefinitionTypeConflict": helpers.absmod(
                    __name__, ".error.AttributeDefinitionTypeConflictErrorSchema"
                ),
                "AttributeNameDoesNotExist": helpers.absmod(
                    __name__, ".error.AttributeNameDoesNotExistErrorSchema"
                ),
                "ConcurrentModification": helpers.absmod(
                    __name__, ".error.ConcurrentModificationErrorSchema"
                ),
                "DiscountCodeNonApplicable": helpers.absmod(
                    __name__, ".error.DiscountCodeNonApplicableErrorSchema"
                ),
                "DuplicateAttributeValue": helpers.absmod(
                    __name__, ".error.DuplicateAttributeValueErrorSchema"
                ),
                "DuplicateAttributeValues": helpers.absmod(
                    __name__, ".error.DuplicateAttributeValuesErrorSchema"
                ),
                "DuplicateEnumValues": helpers.absmod(
                    __name__, ".error.DuplicateEnumValuesErrorSchema"
                ),
                "DuplicateField": helpers.absmod(
                    __name__, ".error.DuplicateFieldErrorSchema"
                ),
                "DuplicateFieldWithConflictingResource": helpers.absmod(
                    __name__, ".error.DuplicateFieldWithConflictingResourceErrorSchema"
                ),
                "DuplicatePriceScope": helpers.absmod(
                    __name__, ".error.DuplicatePriceScopeErrorSchema"
                ),
                "DuplicateVariantValues": helpers.absmod(
                    __name__, ".error.DuplicateVariantValuesErrorSchema"
                ),
                "EditPreviewFailed": helpers.absmod(
                    __name__, ".error.EditPreviewFailedErrorSchema"
                ),
                "EnumKeyAlreadyExists": helpers.absmod(
                    __name__, ".error.EnumKeyAlreadyExistsErrorSchema"
                ),
                "EnumKeyDoesNotExist": helpers.absmod(
                    __name__, ".error.EnumKeyDoesNotExistErrorSchema"
                ),
                "EnumValueIsUsed": helpers.absmod(
                    __name__, ".error.EnumValueIsUsedErrorSchema"
                ),
                "EnumValuesMustMatch": helpers.absmod(
                    __name__, ".error.EnumValuesMustMatchErrorSchema"
                ),
                "ExtensionBadResponse": helpers.absmod(
                    __name__, ".error.ExtensionBadResponseErrorSchema"
                ),
                "ExtensionNoResponse": helpers.absmod(
                    __name__, ".error.ExtensionNoResponseErrorSchema"
                ),
                "ExtensionUpdateActionsFailed": helpers.absmod(
                    __name__, ".error.ExtensionUpdateActionsFailedErrorSchema"
                ),
                "ExternalOAuthFailed": helpers.absmod(
                    __name__, ".error.ExternalOAuthFailedErrorSchema"
                ),
                "FeatureRemoved": helpers.absmod(
                    __name__, ".error.FeatureRemovedErrorSchema"
                ),
                "General": helpers.absmod(__name__, ".error.GeneralErrorSchema"),
                "insufficient_scope": helpers.absmod(
                    __name__, ".error.InsufficientScopeErrorSchema"
                ),
                "InternalConstraintViolated": helpers.absmod(
                    __name__, ".error.InternalConstraintViolatedErrorSchema"
                ),
                "InvalidCredentials": helpers.absmod(
                    __name__, ".error.InvalidCredentialsErrorSchema"
                ),
                "InvalidCurrentPassword": helpers.absmod(
                    __name__, ".error.InvalidCurrentPasswordErrorSchema"
                ),
                "InvalidField": helpers.absmod(
                    __name__, ".error.InvalidFieldErrorSchema"
                ),
                "InvalidInput": helpers.absmod(
                    __name__, ".error.InvalidInputErrorSchema"
                ),
                "InvalidItemShippingDetails": helpers.absmod(
                    __name__, ".error.InvalidItemShippingDetailsErrorSchema"
                ),
                "InvalidJsonInput": helpers.absmod(
                    __name__, ".error.InvalidJsonInputErrorSchema"
                ),
                "InvalidOperation": helpers.absmod(
                    __name__, ".error.InvalidOperationErrorSchema"
                ),
                "InvalidSubject": helpers.absmod(
                    __name__, ".error.InvalidSubjectErrorSchema"
                ),
                "invalid_token": helpers.absmod(
                    __name__, ".error.InvalidTokenErrorSchema"
                ),
                "LanguageUsedInStores": helpers.absmod(
                    __name__, ".error.LanguageUsedInStoresErrorSchema"
                ),
                "MatchingPriceNotFound": helpers.absmod(
                    __name__, ".error.MatchingPriceNotFoundErrorSchema"
                ),
                "MaxResourceLimitExceeded": helpers.absmod(
                    __name__, ".error.MaxResourceLimitExceededErrorSchema"
                ),
                "MissingRoleOnChannel": helpers.absmod(
                    __name__, ".error.MissingRoleOnChannelErrorSchema"
                ),
                "MissingTaxRateForCountry": helpers.absmod(
                    __name__, ".error.MissingTaxRateForCountryErrorSchema"
                ),
                "NoMatchingProductDiscountFound": helpers.absmod(
                    __name__, ".error.NoMatchingProductDiscountFoundErrorSchema"
                ),
                "NotEnabled": helpers.absmod(__name__, ".error.NotEnabledErrorSchema"),
                "ObjectNotFound": helpers.absmod(
                    __name__, ".error.ObjectNotFoundErrorSchema"
                ),
                "OutOfStock": helpers.absmod(__name__, ".error.OutOfStockErrorSchema"),
                "OverCapacity": helpers.absmod(
                    __name__, ".error.OverCapacityErrorSchema"
                ),
                "PendingOperation": helpers.absmod(
                    __name__, ".error.PendingOperationErrorSchema"
                ),
                "PriceChanged": helpers.absmod(
                    __name__, ".error.PriceChangedErrorSchema"
                ),
                "ProjectNotConfiguredForLanguages": helpers.absmod(
                    __name__, ".error.ProjectNotConfiguredForLanguagesErrorSchema"
                ),
                "QueryComplexityLimitExceeded": helpers.absmod(
                    __name__, ".error.QueryComplexityLimitExceededErrorSchema"
                ),
                "QueryTimedOut": helpers.absmod(
                    __name__, ".error.QueryTimedOutErrorSchema"
                ),
                "ReferenceExists": helpers.absmod(
                    __name__, ".error.ReferenceExistsErrorSchema"
                ),
                "ReferencedResourceNotFound": helpers.absmod(
                    __name__, ".error.ReferencedResourceNotFoundErrorSchema"
                ),
                "RequiredField": helpers.absmod(
                    __name__, ".error.RequiredFieldErrorSchema"
                ),
                "ResourceNotFound": helpers.absmod(
                    __name__, ".error.ResourceNotFoundErrorSchema"
                ),
                "ResourceSizeLimitExceeded": helpers.absmod(
                    __name__, ".error.ResourceSizeLimitExceededErrorSchema"
                ),
                "SearchExecutionFailure": helpers.absmod(
                    __name__, ".error.SearchExecutionFailureErrorSchema"
                ),
                "SearchFacetPathNotFound": helpers.absmod(
                    __name__, ".error.SearchFacetPathNotFoundErrorSchema"
                ),
                "SemanticError": helpers.absmod(
                    __name__, ".error.SemanticErrorErrorSchema"
                ),
                "ShippingMethodDoesNotMatchCart": helpers.absmod(
                    __name__, ".error.ShippingMethodDoesNotMatchCartErrorSchema"
                ),
                "SyntaxError": helpers.absmod(
                    __name__, ".error.SyntaxErrorErrorSchema"
                ),
                "WeakPassword": helpers.absmod(
                    __name__, ".error.WeakPasswordErrorSchema"
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
        del data["type"]
        return models.OrderEditPreviewFailure(**data)


class OrderEditPreviewSuccessSchema(OrderEditResultSchema):
    preview = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".StagedOrderSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    message_payloads = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("type", "type"),
            discriminator_schemas={
                "CategoryCreated": helpers.absmod(
                    __name__, ".message.CategoryCreatedMessagePayloadSchema"
                ),
                "CategorySlugChanged": helpers.absmod(
                    __name__, ".message.CategorySlugChangedMessagePayloadSchema"
                ),
                "CustomLineItemStateTransition": helpers.absmod(
                    __name__,
                    ".message.CustomLineItemStateTransitionMessagePayloadSchema",
                ),
                "CustomerAddressAdded": helpers.absmod(
                    __name__, ".message.CustomerAddressAddedMessagePayloadSchema"
                ),
                "CustomerAddressChanged": helpers.absmod(
                    __name__, ".message.CustomerAddressChangedMessagePayloadSchema"
                ),
                "CustomerAddressRemoved": helpers.absmod(
                    __name__, ".message.CustomerAddressRemovedMessagePayloadSchema"
                ),
                "CustomerCompanyNameSet": helpers.absmod(
                    __name__, ".message.CustomerCompanyNameSetMessagePayloadSchema"
                ),
                "CustomerCreated": helpers.absmod(
                    __name__, ".message.CustomerCreatedMessagePayloadSchema"
                ),
                "CustomerDateOfBirthSet": helpers.absmod(
                    __name__, ".message.CustomerDateOfBirthSetMessagePayloadSchema"
                ),
                "CustomerEmailChanged": helpers.absmod(
                    __name__, ".message.CustomerEmailChangedMessagePayloadSchema"
                ),
                "CustomerEmailVerified": helpers.absmod(
                    __name__, ".message.CustomerEmailVerifiedMessagePayloadSchema"
                ),
                "CustomerGroupSet": helpers.absmod(
                    __name__, ".message.CustomerGroupSetMessagePayloadSchema"
                ),
                "DeliveryAdded": helpers.absmod(
                    __name__, ".message.DeliveryAddedMessagePayloadSchema"
                ),
                "DeliveryAddressSet": helpers.absmod(
                    __name__, ".message.DeliveryAddressSetMessagePayloadSchema"
                ),
                "DeliveryItemsUpdated": helpers.absmod(
                    __name__, ".message.DeliveryItemsUpdatedMessagePayloadSchema"
                ),
                "DeliveryRemoved": helpers.absmod(
                    __name__, ".message.DeliveryRemovedMessagePayloadSchema"
                ),
                "InventoryEntryCreated": helpers.absmod(
                    __name__, ".message.InventoryEntryCreatedMessagePayloadSchema"
                ),
                "InventoryEntryDeleted": helpers.absmod(
                    __name__, ".message.InventoryEntryDeletedMessagePayloadSchema"
                ),
                "InventoryEntryQuantitySet": helpers.absmod(
                    __name__, ".message.InventoryEntryQuantitySetMessagePayloadSchema"
                ),
                "LineItemStateTransition": helpers.absmod(
                    __name__, ".message.LineItemStateTransitionMessagePayloadSchema"
                ),
                "OrderBillingAddressSet": helpers.absmod(
                    __name__, ".message.OrderBillingAddressSetMessagePayloadSchema"
                ),
                "OrderCreated": helpers.absmod(
                    __name__, ".message.OrderCreatedMessagePayloadSchema"
                ),
                "OrderCustomLineItemDiscountSet": helpers.absmod(
                    __name__,
                    ".message.OrderCustomLineItemDiscountSetMessagePayloadSchema",
                ),
                "OrderCustomerEmailSet": helpers.absmod(
                    __name__, ".message.OrderCustomerEmailSetMessagePayloadSchema"
                ),
                "OrderCustomerGroupSet": helpers.absmod(
                    __name__, ".message.OrderCustomerGroupSetMessagePayloadSchema"
                ),
                "OrderCustomerSet": helpers.absmod(
                    __name__, ".message.OrderCustomerSetMessagePayloadSchema"
                ),
                "OrderDeleted": helpers.absmod(
                    __name__, ".message.OrderDeletedMessagePayloadSchema"
                ),
                "OrderDiscountCodeAdded": helpers.absmod(
                    __name__, ".message.OrderDiscountCodeAddedMessagePayloadSchema"
                ),
                "OrderDiscountCodeRemoved": helpers.absmod(
                    __name__, ".message.OrderDiscountCodeRemovedMessagePayloadSchema"
                ),
                "OrderDiscountCodeStateSet": helpers.absmod(
                    __name__, ".message.OrderDiscountCodeStateSetMessagePayloadSchema"
                ),
                "OrderEditApplied": helpers.absmod(
                    __name__, ".message.OrderEditAppliedMessagePayloadSchema"
                ),
                "OrderImported": helpers.absmod(
                    __name__, ".message.OrderImportedMessagePayloadSchema"
                ),
                "OrderLineItemAdded": helpers.absmod(
                    __name__, ".message.OrderLineItemAddedMessagePayloadSchema"
                ),
                "OrderLineItemDiscountSet": helpers.absmod(
                    __name__, ".message.OrderLineItemDiscountSetMessagePayloadSchema"
                ),
                "OrderPaymentStateChanged": helpers.absmod(
                    __name__, ".message.OrderPaymentStateChangedMessagePayloadSchema"
                ),
                "ReturnInfoAdded": helpers.absmod(
                    __name__, ".message.OrderReturnInfoAddedMessagePayloadSchema"
                ),
                "OrderReturnShipmentStateChanged": helpers.absmod(
                    __name__,
                    ".message.OrderReturnShipmentStateChangedMessagePayloadSchema",
                ),
                "OrderShipmentStateChanged": helpers.absmod(
                    __name__, ".message.OrderShipmentStateChangedMessagePayloadSchema"
                ),
                "OrderShippingAddressSet": helpers.absmod(
                    __name__, ".message.OrderShippingAddressSetMessagePayloadSchema"
                ),
                "OrderShippingInfoSet": helpers.absmod(
                    __name__, ".message.OrderShippingInfoSetMessagePayloadSchema"
                ),
                "OrderShippingRateInputSet": helpers.absmod(
                    __name__, ".message.OrderShippingRateInputSetMessagePayloadSchema"
                ),
                "OrderStateChanged": helpers.absmod(
                    __name__, ".message.OrderStateChangedMessagePayloadSchema"
                ),
                "OrderStateTransition": helpers.absmod(
                    __name__, ".message.OrderStateTransitionMessagePayloadSchema"
                ),
                "OrderStoreSet": helpers.absmod(
                    __name__, ".message.OrderStoreSetMessagePayloadSchema"
                ),
                "ParcelAddedToDelivery": helpers.absmod(
                    __name__, ".message.ParcelAddedToDeliveryMessagePayloadSchema"
                ),
                "ParcelItemsUpdated": helpers.absmod(
                    __name__, ".message.ParcelItemsUpdatedMessagePayloadSchema"
                ),
                "ParcelMeasurementsUpdated": helpers.absmod(
                    __name__, ".message.ParcelMeasurementsUpdatedMessagePayloadSchema"
                ),
                "ParcelRemovedFromDelivery": helpers.absmod(
                    __name__, ".message.ParcelRemovedFromDeliveryMessagePayloadSchema"
                ),
                "ParcelTrackingDataUpdated": helpers.absmod(
                    __name__, ".message.ParcelTrackingDataUpdatedMessagePayloadSchema"
                ),
                "PaymentCreated": helpers.absmod(
                    __name__, ".message.PaymentCreatedMessagePayloadSchema"
                ),
                "PaymentInteractionAdded": helpers.absmod(
                    __name__, ".message.PaymentInteractionAddedMessagePayloadSchema"
                ),
                "PaymentStatusInterfaceCodeSet": helpers.absmod(
                    __name__,
                    ".message.PaymentStatusInterfaceCodeSetMessagePayloadSchema",
                ),
                "PaymentStatusStateTransition": helpers.absmod(
                    __name__,
                    ".message.PaymentStatusStateTransitionMessagePayloadSchema",
                ),
                "PaymentTransactionAdded": helpers.absmod(
                    __name__, ".message.PaymentTransactionAddedMessagePayloadSchema"
                ),
                "PaymentTransactionStateChanged": helpers.absmod(
                    __name__,
                    ".message.PaymentTransactionStateChangedMessagePayloadSchema",
                ),
                "ProductAddedToCategory": helpers.absmod(
                    __name__, ".message.ProductAddedToCategoryMessagePayloadSchema"
                ),
                "ProductCreated": helpers.absmod(
                    __name__, ".message.ProductCreatedMessagePayloadSchema"
                ),
                "ProductDeleted": helpers.absmod(
                    __name__, ".message.ProductDeletedMessagePayloadSchema"
                ),
                "ProductImageAdded": helpers.absmod(
                    __name__, ".message.ProductImageAddedMessagePayloadSchema"
                ),
                "ProductPriceDiscountsSet": helpers.absmod(
                    __name__, ".message.ProductPriceDiscountsSetMessagePayloadSchema"
                ),
                "ProductPriceExternalDiscountSet": helpers.absmod(
                    __name__,
                    ".message.ProductPriceExternalDiscountSetMessagePayloadSchema",
                ),
                "ProductPublished": helpers.absmod(
                    __name__, ".message.ProductPublishedMessagePayloadSchema"
                ),
                "ProductRemovedFromCategory": helpers.absmod(
                    __name__, ".message.ProductRemovedFromCategoryMessagePayloadSchema"
                ),
                "ProductRevertedStagedChanges": helpers.absmod(
                    __name__,
                    ".message.ProductRevertedStagedChangesMessagePayloadSchema",
                ),
                "ProductSlugChanged": helpers.absmod(
                    __name__, ".message.ProductSlugChangedMessagePayloadSchema"
                ),
                "ProductStateTransition": helpers.absmod(
                    __name__, ".message.ProductStateTransitionMessagePayloadSchema"
                ),
                "ProductUnpublished": helpers.absmod(
                    __name__, ".message.ProductUnpublishedMessagePayloadSchema"
                ),
                "ProductVariantAdded": helpers.absmod(
                    __name__, ".message.ProductVariantAddedMessagePayloadSchema"
                ),
                "ProductVariantDeleted": helpers.absmod(
                    __name__, ".message.ProductVariantDeletedMessagePayloadSchema"
                ),
                "ReviewCreated": helpers.absmod(
                    __name__, ".message.ReviewCreatedMessagePayloadSchema"
                ),
                "ReviewRatingSet": helpers.absmod(
                    __name__, ".message.ReviewRatingSetMessagePayloadSchema"
                ),
                "ReviewStateTransition": helpers.absmod(
                    __name__, ".message.ReviewStateTransitionMessagePayloadSchema"
                ),
            },
        ),
        allow_none=True,
        missing=None,
        data_key="messagePayloads",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderEditPreviewSuccess(**data)


class OrderEditUpdateSchema(helpers.BaseSchema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addStagedAction": helpers.absmod(
                    __name__, ".OrderEditAddStagedActionActionSchema"
                ),
                "setComment": helpers.absmod(
                    __name__, ".OrderEditSetCommentActionSchema"
                ),
                "setCustomField": helpers.absmod(
                    __name__, ".OrderEditSetCustomFieldActionSchema"
                ),
                "setCustomType": helpers.absmod(
                    __name__, ".OrderEditSetCustomTypeActionSchema"
                ),
                "setKey": helpers.absmod(__name__, ".OrderEditSetKeyActionSchema"),
                "setStagedActions": helpers.absmod(
                    __name__, ".OrderEditSetStagedActionsActionSchema"
                ),
            },
        ),
        allow_none=True,
        missing=None,
    )
    dry_run = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None, data_key="dryRun"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.OrderEditUpdate(**data)


class OrderEditUpdateActionSchema(helpers.BaseSchema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderEditUpdateAction(**data)


class OrderExcerptSchema(helpers.BaseSchema):
    total_price = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "centPrecision": helpers.absmod(
                __name__, ".common.CentPrecisionMoneySchema"
            ),
            "highPrecision": helpers.absmod(
                __name__, ".common.HighPrecisionMoneySchema"
            ),
        },
        missing=None,
        data_key="totalPrice",
    )
    taxed_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.TaxedPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="taxedPrice",
    )
    version = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.OrderExcerpt(**data)


class StagedOrderSchema(OrderSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.StagedOrder(**data)


class OrderEditAddStagedActionActionSchema(OrderEditUpdateActionSchema):
    staged_action = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("action", "action"),
        discriminator_schemas={
            "addCustomLineItem": helpers.absmod(
                __name__, ".StagedOrderAddCustomLineItemActionSchema"
            ),
            "addDelivery": helpers.absmod(
                __name__, ".StagedOrderAddDeliveryActionSchema"
            ),
            "addDiscountCode": helpers.absmod(
                __name__, ".StagedOrderAddDiscountCodeActionSchema"
            ),
            "addItemShippingAddress": helpers.absmod(
                __name__, ".StagedOrderAddItemShippingAddressActionSchema"
            ),
            "addLineItem": helpers.absmod(
                __name__, ".StagedOrderAddLineItemActionSchema"
            ),
            "addParcelToDelivery": helpers.absmod(
                __name__, ".StagedOrderAddParcelToDeliveryActionSchema"
            ),
            "addPayment": helpers.absmod(
                __name__, ".StagedOrderAddPaymentActionSchema"
            ),
            "addReturnInfo": helpers.absmod(
                __name__, ".StagedOrderAddReturnInfoActionSchema"
            ),
            "addShoppingList": helpers.absmod(
                __name__, ".StagedOrderAddShoppingListActionSchema"
            ),
            "changeCustomLineItemMoney": helpers.absmod(
                __name__, ".StagedOrderChangeCustomLineItemMoneyActionSchema"
            ),
            "changeCustomLineItemQuantity": helpers.absmod(
                __name__, ".StagedOrderChangeCustomLineItemQuantityActionSchema"
            ),
            "changeLineItemQuantity": helpers.absmod(
                __name__, ".StagedOrderChangeLineItemQuantityActionSchema"
            ),
            "changeOrderState": helpers.absmod(
                __name__, ".StagedOrderChangeOrderStateActionSchema"
            ),
            "changePaymentState": helpers.absmod(
                __name__, ".StagedOrderChangePaymentStateActionSchema"
            ),
            "changeShipmentState": helpers.absmod(
                __name__, ".StagedOrderChangeShipmentStateActionSchema"
            ),
            "changeTaxCalculationMode": helpers.absmod(
                __name__, ".StagedOrderChangeTaxCalculationModeActionSchema"
            ),
            "changeTaxMode": helpers.absmod(
                __name__, ".StagedOrderChangeTaxModeActionSchema"
            ),
            "changeTaxRoundingMode": helpers.absmod(
                __name__, ".StagedOrderChangeTaxRoundingModeActionSchema"
            ),
            "importCustomLineItemState": helpers.absmod(
                __name__, ".StagedOrderImportCustomLineItemStateActionSchema"
            ),
            "importLineItemState": helpers.absmod(
                __name__, ".StagedOrderImportLineItemStateActionSchema"
            ),
            "removeCustomLineItem": helpers.absmod(
                __name__, ".StagedOrderRemoveCustomLineItemActionSchema"
            ),
            "removeDelivery": helpers.absmod(
                __name__, ".StagedOrderRemoveDeliveryActionSchema"
            ),
            "removeDiscountCode": helpers.absmod(
                __name__, ".StagedOrderRemoveDiscountCodeActionSchema"
            ),
            "removeItemShippingAddress": helpers.absmod(
                __name__, ".StagedOrderRemoveItemShippingAddressActionSchema"
            ),
            "removeLineItem": helpers.absmod(
                __name__, ".StagedOrderRemoveLineItemActionSchema"
            ),
            "removeParcelFromDelivery": helpers.absmod(
                __name__, ".StagedOrderRemoveParcelFromDeliveryActionSchema"
            ),
            "removePayment": helpers.absmod(
                __name__, ".StagedOrderRemovePaymentActionSchema"
            ),
            "setBillingAddress": helpers.absmod(
                __name__, ".StagedOrderSetBillingAddressActionSchema"
            ),
            "setCountry": helpers.absmod(
                __name__, ".StagedOrderSetCountryActionSchema"
            ),
            "setCustomField": helpers.absmod(
                __name__, ".StagedOrderSetCustomFieldActionSchema"
            ),
            "setCustomLineItemCustomField": helpers.absmod(
                __name__, ".StagedOrderSetCustomLineItemCustomFieldActionSchema"
            ),
            "setCustomLineItemCustomType": helpers.absmod(
                __name__, ".StagedOrderSetCustomLineItemCustomTypeActionSchema"
            ),
            "setCustomLineItemShippingDetails": helpers.absmod(
                __name__, ".StagedOrderSetCustomLineItemShippingDetailsActionSchema"
            ),
            "setCustomLineItemTaxAmount": helpers.absmod(
                __name__, ".StagedOrderSetCustomLineItemTaxAmountActionSchema"
            ),
            "setCustomLineItemTaxRate": helpers.absmod(
                __name__, ".StagedOrderSetCustomLineItemTaxRateActionSchema"
            ),
            "setCustomShippingMethod": helpers.absmod(
                __name__, ".StagedOrderSetCustomShippingMethodActionSchema"
            ),
            "setCustomType": helpers.absmod(
                __name__, ".StagedOrderSetCustomTypeActionSchema"
            ),
            "setCustomerEmail": helpers.absmod(
                __name__, ".StagedOrderSetCustomerEmailActionSchema"
            ),
            "setCustomerGroup": helpers.absmod(
                __name__, ".StagedOrderSetCustomerGroupActionSchema"
            ),
            "setCustomerId": helpers.absmod(
                __name__, ".StagedOrderSetCustomerIdActionSchema"
            ),
            "setDeliveryAddress": helpers.absmod(
                __name__, ".StagedOrderSetDeliveryAddressActionSchema"
            ),
            "setDeliveryItems": helpers.absmod(
                __name__, ".StagedOrderSetDeliveryItemsActionSchema"
            ),
            "setLineItemCustomField": helpers.absmod(
                __name__, ".StagedOrderSetLineItemCustomFieldActionSchema"
            ),
            "setLineItemCustomType": helpers.absmod(
                __name__, ".StagedOrderSetLineItemCustomTypeActionSchema"
            ),
            "setLineItemDistributionChannel": helpers.absmod(
                __name__, ".StagedOrderSetLineItemDistributionChannelActionSchema"
            ),
            "setLineItemPrice": helpers.absmod(
                __name__, ".StagedOrderSetLineItemPriceActionSchema"
            ),
            "setLineItemShippingDetails": helpers.absmod(
                __name__, ".StagedOrderSetLineItemShippingDetailsActionSchema"
            ),
            "setLineItemTaxAmount": helpers.absmod(
                __name__, ".StagedOrderSetLineItemTaxAmountActionSchema"
            ),
            "setLineItemTaxRate": helpers.absmod(
                __name__, ".StagedOrderSetLineItemTaxRateActionSchema"
            ),
            "setLineItemTotalPrice": helpers.absmod(
                __name__, ".StagedOrderSetLineItemTotalPriceActionSchema"
            ),
            "setLocale": helpers.absmod(__name__, ".StagedOrderSetLocaleActionSchema"),
            "setOrderNumber": helpers.absmod(
                __name__, ".StagedOrderSetOrderNumberActionSchema"
            ),
            "setOrderTotalTax": helpers.absmod(
                __name__, ".StagedOrderSetOrderTotalTaxActionSchema"
            ),
            "setParcelItems": helpers.absmod(
                __name__, ".StagedOrderSetParcelItemsActionSchema"
            ),
            "setParcelMeasurements": helpers.absmod(
                __name__, ".StagedOrderSetParcelMeasurementsActionSchema"
            ),
            "setParcelTrackingData": helpers.absmod(
                __name__, ".StagedOrderSetParcelTrackingDataActionSchema"
            ),
            "setReturnPaymentState": helpers.absmod(
                __name__, ".StagedOrderSetReturnPaymentStateActionSchema"
            ),
            "setReturnShipmentState": helpers.absmod(
                __name__, ".StagedOrderSetReturnShipmentStateActionSchema"
            ),
            "setShippingAddress": helpers.absmod(
                __name__, ".StagedOrderSetShippingAddressActionSchema"
            ),
            "setShippingAddressAndCustomShippingMethod": helpers.absmod(
                __name__,
                ".StagedOrderSetShippingAddressAndCustomShippingMethodActionSchema",
            ),
            "setShippingAddressAndShippingMethod": helpers.absmod(
                __name__, ".StagedOrderSetShippingAddressAndShippingMethodActionSchema"
            ),
            "setShippingMethod": helpers.absmod(
                __name__, ".StagedOrderSetShippingMethodActionSchema"
            ),
            "setShippingMethodTaxAmount": helpers.absmod(
                __name__, ".StagedOrderSetShippingMethodTaxAmountActionSchema"
            ),
            "setShippingMethodTaxRate": helpers.absmod(
                __name__, ".StagedOrderSetShippingMethodTaxRateActionSchema"
            ),
            "setShippingRateInput": helpers.absmod(
                __name__, ".StagedOrderSetShippingRateInputActionSchema"
            ),
            "transitionCustomLineItemState": helpers.absmod(
                __name__, ".StagedOrderTransitionCustomLineItemStateActionSchema"
            ),
            "transitionLineItemState": helpers.absmod(
                __name__, ".StagedOrderTransitionLineItemStateActionSchema"
            ),
            "transitionState": helpers.absmod(
                __name__, ".StagedOrderTransitionStateActionSchema"
            ),
            "updateItemShippingAddress": helpers.absmod(
                __name__, ".StagedOrderUpdateItemShippingAddressActionSchema"
            ),
            "updateSyncInfo": helpers.absmod(
                __name__, ".StagedOrderUpdateSyncInfoActionSchema"
            ),
        },
        missing=None,
        data_key="stagedAction",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderEditAddStagedActionAction(**data)


class OrderEditSetCommentActionSchema(OrderEditUpdateActionSchema):
    comment = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderEditSetCommentAction(**data)


class OrderEditSetCustomFieldActionSchema(OrderEditUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderEditSetCustomFieldAction(**data)


class OrderEditSetCustomTypeActionSchema(OrderEditUpdateActionSchema):
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
        return models.OrderEditSetCustomTypeAction(**data)


class OrderEditSetKeyActionSchema(OrderEditUpdateActionSchema):
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderEditSetKeyAction(**data)


class OrderEditSetStagedActionsActionSchema(OrderEditUpdateActionSchema):
    staged_actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addCustomLineItem": helpers.absmod(
                    __name__, ".StagedOrderAddCustomLineItemActionSchema"
                ),
                "addDelivery": helpers.absmod(
                    __name__, ".StagedOrderAddDeliveryActionSchema"
                ),
                "addDiscountCode": helpers.absmod(
                    __name__, ".StagedOrderAddDiscountCodeActionSchema"
                ),
                "addItemShippingAddress": helpers.absmod(
                    __name__, ".StagedOrderAddItemShippingAddressActionSchema"
                ),
                "addLineItem": helpers.absmod(
                    __name__, ".StagedOrderAddLineItemActionSchema"
                ),
                "addParcelToDelivery": helpers.absmod(
                    __name__, ".StagedOrderAddParcelToDeliveryActionSchema"
                ),
                "addPayment": helpers.absmod(
                    __name__, ".StagedOrderAddPaymentActionSchema"
                ),
                "addReturnInfo": helpers.absmod(
                    __name__, ".StagedOrderAddReturnInfoActionSchema"
                ),
                "addShoppingList": helpers.absmod(
                    __name__, ".StagedOrderAddShoppingListActionSchema"
                ),
                "changeCustomLineItemMoney": helpers.absmod(
                    __name__, ".StagedOrderChangeCustomLineItemMoneyActionSchema"
                ),
                "changeCustomLineItemQuantity": helpers.absmod(
                    __name__, ".StagedOrderChangeCustomLineItemQuantityActionSchema"
                ),
                "changeLineItemQuantity": helpers.absmod(
                    __name__, ".StagedOrderChangeLineItemQuantityActionSchema"
                ),
                "changeOrderState": helpers.absmod(
                    __name__, ".StagedOrderChangeOrderStateActionSchema"
                ),
                "changePaymentState": helpers.absmod(
                    __name__, ".StagedOrderChangePaymentStateActionSchema"
                ),
                "changeShipmentState": helpers.absmod(
                    __name__, ".StagedOrderChangeShipmentStateActionSchema"
                ),
                "changeTaxCalculationMode": helpers.absmod(
                    __name__, ".StagedOrderChangeTaxCalculationModeActionSchema"
                ),
                "changeTaxMode": helpers.absmod(
                    __name__, ".StagedOrderChangeTaxModeActionSchema"
                ),
                "changeTaxRoundingMode": helpers.absmod(
                    __name__, ".StagedOrderChangeTaxRoundingModeActionSchema"
                ),
                "importCustomLineItemState": helpers.absmod(
                    __name__, ".StagedOrderImportCustomLineItemStateActionSchema"
                ),
                "importLineItemState": helpers.absmod(
                    __name__, ".StagedOrderImportLineItemStateActionSchema"
                ),
                "removeCustomLineItem": helpers.absmod(
                    __name__, ".StagedOrderRemoveCustomLineItemActionSchema"
                ),
                "removeDelivery": helpers.absmod(
                    __name__, ".StagedOrderRemoveDeliveryActionSchema"
                ),
                "removeDiscountCode": helpers.absmod(
                    __name__, ".StagedOrderRemoveDiscountCodeActionSchema"
                ),
                "removeItemShippingAddress": helpers.absmod(
                    __name__, ".StagedOrderRemoveItemShippingAddressActionSchema"
                ),
                "removeLineItem": helpers.absmod(
                    __name__, ".StagedOrderRemoveLineItemActionSchema"
                ),
                "removeParcelFromDelivery": helpers.absmod(
                    __name__, ".StagedOrderRemoveParcelFromDeliveryActionSchema"
                ),
                "removePayment": helpers.absmod(
                    __name__, ".StagedOrderRemovePaymentActionSchema"
                ),
                "setBillingAddress": helpers.absmod(
                    __name__, ".StagedOrderSetBillingAddressActionSchema"
                ),
                "setCountry": helpers.absmod(
                    __name__, ".StagedOrderSetCountryActionSchema"
                ),
                "setCustomField": helpers.absmod(
                    __name__, ".StagedOrderSetCustomFieldActionSchema"
                ),
                "setCustomLineItemCustomField": helpers.absmod(
                    __name__, ".StagedOrderSetCustomLineItemCustomFieldActionSchema"
                ),
                "setCustomLineItemCustomType": helpers.absmod(
                    __name__, ".StagedOrderSetCustomLineItemCustomTypeActionSchema"
                ),
                "setCustomLineItemShippingDetails": helpers.absmod(
                    __name__, ".StagedOrderSetCustomLineItemShippingDetailsActionSchema"
                ),
                "setCustomLineItemTaxAmount": helpers.absmod(
                    __name__, ".StagedOrderSetCustomLineItemTaxAmountActionSchema"
                ),
                "setCustomLineItemTaxRate": helpers.absmod(
                    __name__, ".StagedOrderSetCustomLineItemTaxRateActionSchema"
                ),
                "setCustomShippingMethod": helpers.absmod(
                    __name__, ".StagedOrderSetCustomShippingMethodActionSchema"
                ),
                "setCustomType": helpers.absmod(
                    __name__, ".StagedOrderSetCustomTypeActionSchema"
                ),
                "setCustomerEmail": helpers.absmod(
                    __name__, ".StagedOrderSetCustomerEmailActionSchema"
                ),
                "setCustomerGroup": helpers.absmod(
                    __name__, ".StagedOrderSetCustomerGroupActionSchema"
                ),
                "setCustomerId": helpers.absmod(
                    __name__, ".StagedOrderSetCustomerIdActionSchema"
                ),
                "setDeliveryAddress": helpers.absmod(
                    __name__, ".StagedOrderSetDeliveryAddressActionSchema"
                ),
                "setDeliveryItems": helpers.absmod(
                    __name__, ".StagedOrderSetDeliveryItemsActionSchema"
                ),
                "setLineItemCustomField": helpers.absmod(
                    __name__, ".StagedOrderSetLineItemCustomFieldActionSchema"
                ),
                "setLineItemCustomType": helpers.absmod(
                    __name__, ".StagedOrderSetLineItemCustomTypeActionSchema"
                ),
                "setLineItemDistributionChannel": helpers.absmod(
                    __name__, ".StagedOrderSetLineItemDistributionChannelActionSchema"
                ),
                "setLineItemPrice": helpers.absmod(
                    __name__, ".StagedOrderSetLineItemPriceActionSchema"
                ),
                "setLineItemShippingDetails": helpers.absmod(
                    __name__, ".StagedOrderSetLineItemShippingDetailsActionSchema"
                ),
                "setLineItemTaxAmount": helpers.absmod(
                    __name__, ".StagedOrderSetLineItemTaxAmountActionSchema"
                ),
                "setLineItemTaxRate": helpers.absmod(
                    __name__, ".StagedOrderSetLineItemTaxRateActionSchema"
                ),
                "setLineItemTotalPrice": helpers.absmod(
                    __name__, ".StagedOrderSetLineItemTotalPriceActionSchema"
                ),
                "setLocale": helpers.absmod(
                    __name__, ".StagedOrderSetLocaleActionSchema"
                ),
                "setOrderNumber": helpers.absmod(
                    __name__, ".StagedOrderSetOrderNumberActionSchema"
                ),
                "setOrderTotalTax": helpers.absmod(
                    __name__, ".StagedOrderSetOrderTotalTaxActionSchema"
                ),
                "setParcelItems": helpers.absmod(
                    __name__, ".StagedOrderSetParcelItemsActionSchema"
                ),
                "setParcelMeasurements": helpers.absmod(
                    __name__, ".StagedOrderSetParcelMeasurementsActionSchema"
                ),
                "setParcelTrackingData": helpers.absmod(
                    __name__, ".StagedOrderSetParcelTrackingDataActionSchema"
                ),
                "setReturnPaymentState": helpers.absmod(
                    __name__, ".StagedOrderSetReturnPaymentStateActionSchema"
                ),
                "setReturnShipmentState": helpers.absmod(
                    __name__, ".StagedOrderSetReturnShipmentStateActionSchema"
                ),
                "setShippingAddress": helpers.absmod(
                    __name__, ".StagedOrderSetShippingAddressActionSchema"
                ),
                "setShippingAddressAndCustomShippingMethod": helpers.absmod(
                    __name__,
                    ".StagedOrderSetShippingAddressAndCustomShippingMethodActionSchema",
                ),
                "setShippingAddressAndShippingMethod": helpers.absmod(
                    __name__,
                    ".StagedOrderSetShippingAddressAndShippingMethodActionSchema",
                ),
                "setShippingMethod": helpers.absmod(
                    __name__, ".StagedOrderSetShippingMethodActionSchema"
                ),
                "setShippingMethodTaxAmount": helpers.absmod(
                    __name__, ".StagedOrderSetShippingMethodTaxAmountActionSchema"
                ),
                "setShippingMethodTaxRate": helpers.absmod(
                    __name__, ".StagedOrderSetShippingMethodTaxRateActionSchema"
                ),
                "setShippingRateInput": helpers.absmod(
                    __name__, ".StagedOrderSetShippingRateInputActionSchema"
                ),
                "transitionCustomLineItemState": helpers.absmod(
                    __name__, ".StagedOrderTransitionCustomLineItemStateActionSchema"
                ),
                "transitionLineItemState": helpers.absmod(
                    __name__, ".StagedOrderTransitionLineItemStateActionSchema"
                ),
                "transitionState": helpers.absmod(
                    __name__, ".StagedOrderTransitionStateActionSchema"
                ),
                "updateItemShippingAddress": helpers.absmod(
                    __name__, ".StagedOrderUpdateItemShippingAddressActionSchema"
                ),
                "updateSyncInfo": helpers.absmod(
                    __name__, ".StagedOrderUpdateSyncInfoActionSchema"
                ),
            },
        ),
        allow_none=True,
        missing=None,
        data_key="stagedActions",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.OrderEditSetStagedActionsAction(**data)


class StagedOrderAddCustomLineItemActionSchema(StagedOrderUpdateActionSchema):
    money = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    name = LocalizedStringField(allow_none=True, missing=None)
    quantity = marshmallow.fields.Float(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    slug = marshmallow.fields.String(allow_none=True, missing=None)
    tax_category = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".tax_category.TaxCategoryResourceIdentifierSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="taxCategory",
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    external_tax_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ExternalTaxRateDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="externalTaxRate",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderAddCustomLineItemAction(**data)


class StagedOrderAddDeliveryActionSchema(StagedOrderUpdateActionSchema):
    items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.DeliveryItemSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
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
        nested=helpers.absmod(__name__, ".order.ParcelDraftSchema"),
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
        del data["action"]
        return models.StagedOrderAddDeliveryAction(**data)


class StagedOrderAddDiscountCodeActionSchema(StagedOrderUpdateActionSchema):
    code = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderAddDiscountCodeAction(**data)


class StagedOrderAddItemShippingAddressActionSchema(StagedOrderUpdateActionSchema):
    address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderAddItemShippingAddressAction(**data)


class StagedOrderAddLineItemActionSchema(StagedOrderUpdateActionSchema):
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    distribution_channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="distributionChannel",
    )
    external_tax_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ExternalTaxRateDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="externalTaxRate",
    )
    product_id = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="productId",
    )
    variant_id = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="variantId",
    )
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    quantity = marshmallow.fields.Float(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    added_at = marshmallow.fields.DateTime(
        allow_none=True, metadata={"omit_empty": True}, missing=None, data_key="addedAt"
    )
    supply_channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="supplyChannel",
    )
    external_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="externalPrice",
    )
    external_total_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ExternalLineItemTotalPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="externalTotalPrice",
    )
    shipping_details = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ItemShippingDetailsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="shippingDetails",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderAddLineItemAction(**data)


class StagedOrderAddParcelToDeliveryActionSchema(StagedOrderUpdateActionSchema):
    delivery_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="deliveryId"
    )
    measurements = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.ParcelMeasurementsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    tracking_data = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.TrackingDataSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="trackingData",
    )
    items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.DeliveryItemSchema"),
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
        del data["action"]
        return models.StagedOrderAddParcelToDeliveryAction(**data)


class StagedOrderAddPaymentActionSchema(StagedOrderUpdateActionSchema):
    payment = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".payment.PaymentResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderAddPaymentAction(**data)


class StagedOrderAddReturnInfoActionSchema(StagedOrderUpdateActionSchema):
    return_tracking_id = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="returnTrackingId",
    )
    items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.ReturnItemDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
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
        del data["action"]
        return models.StagedOrderAddReturnInfoAction(**data)


class StagedOrderAddShoppingListActionSchema(StagedOrderUpdateActionSchema):
    shopping_list = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".shopping_list.ShoppingListResourceIdentifierSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="shoppingList",
    )
    supply_channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="supplyChannel",
    )
    distribution_channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="distributionChannel",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderAddShoppingListAction(**data)


class StagedOrderChangeCustomLineItemMoneyActionSchema(StagedOrderUpdateActionSchema):
    custom_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customLineItemId"
    )
    money = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderChangeCustomLineItemMoneyAction(**data)


class StagedOrderChangeCustomLineItemQuantityActionSchema(
    StagedOrderUpdateActionSchema
):
    custom_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customLineItemId"
    )
    quantity = marshmallow.fields.Float(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderChangeCustomLineItemQuantityAction(**data)


class StagedOrderChangeLineItemQuantityActionSchema(StagedOrderUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    quantity = marshmallow.fields.Float(allow_none=True, missing=None)
    external_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="externalPrice",
    )
    external_total_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ExternalLineItemTotalPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="externalTotalPrice",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderChangeLineItemQuantityAction(**data)


class StagedOrderChangeOrderStateActionSchema(StagedOrderUpdateActionSchema):
    order_state = marshmallow_enum.EnumField(
        OrderState, by_value=True, allow_none=True, missing=None, data_key="orderState"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderChangeOrderStateAction(**data)


class StagedOrderChangePaymentStateActionSchema(StagedOrderUpdateActionSchema):
    payment_state = marshmallow_enum.EnumField(
        PaymentState,
        by_value=True,
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="paymentState",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderChangePaymentStateAction(**data)


class StagedOrderChangeShipmentStateActionSchema(StagedOrderUpdateActionSchema):
    shipment_state = marshmallow_enum.EnumField(
        ShipmentState,
        by_value=True,
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="shipmentState",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderChangeShipmentStateAction(**data)


class StagedOrderChangeTaxCalculationModeActionSchema(StagedOrderUpdateActionSchema):
    tax_calculation_mode = marshmallow_enum.EnumField(
        TaxCalculationMode,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="taxCalculationMode",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderChangeTaxCalculationModeAction(**data)


class StagedOrderChangeTaxModeActionSchema(StagedOrderUpdateActionSchema):
    tax_mode = marshmallow_enum.EnumField(
        TaxMode, by_value=True, allow_none=True, missing=None, data_key="taxMode"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderChangeTaxModeAction(**data)


class StagedOrderChangeTaxRoundingModeActionSchema(StagedOrderUpdateActionSchema):
    tax_rounding_mode = marshmallow_enum.EnumField(
        RoundingMode,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="taxRoundingMode",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderChangeTaxRoundingModeAction(**data)


class StagedOrderImportCustomLineItemStateActionSchema(StagedOrderUpdateActionSchema):
    custom_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customLineItemId"
    )
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.ItemStateSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderImportCustomLineItemStateAction(**data)


class StagedOrderImportLineItemStateActionSchema(StagedOrderUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.ItemStateSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderImportLineItemStateAction(**data)


class StagedOrderRemoveCustomLineItemActionSchema(StagedOrderUpdateActionSchema):
    custom_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customLineItemId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderRemoveCustomLineItemAction(**data)


class StagedOrderRemoveDeliveryActionSchema(StagedOrderUpdateActionSchema):
    delivery_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="deliveryId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderRemoveDeliveryAction(**data)


class StagedOrderRemoveDiscountCodeActionSchema(StagedOrderUpdateActionSchema):
    discount_code = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".discount_code.DiscountCodeReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="discountCode",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderRemoveDiscountCodeAction(**data)


class StagedOrderRemoveItemShippingAddressActionSchema(StagedOrderUpdateActionSchema):
    address_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderRemoveItemShippingAddressAction(**data)


class StagedOrderRemoveLineItemActionSchema(StagedOrderUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    quantity = marshmallow.fields.Float(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    external_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="externalPrice",
    )
    external_total_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ExternalLineItemTotalPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="externalTotalPrice",
    )
    shipping_details_to_remove = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ItemShippingDetailsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="shippingDetailsToRemove",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderRemoveLineItemAction(**data)


class StagedOrderRemoveParcelFromDeliveryActionSchema(StagedOrderUpdateActionSchema):
    parcel_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="parcelId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderRemoveParcelFromDeliveryAction(**data)


class StagedOrderRemovePaymentActionSchema(StagedOrderUpdateActionSchema):
    payment = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".payment.PaymentResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderRemovePaymentAction(**data)


class StagedOrderSetBillingAddressActionSchema(StagedOrderUpdateActionSchema):
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
        return models.StagedOrderSetBillingAddressAction(**data)


class StagedOrderSetCountryActionSchema(StagedOrderUpdateActionSchema):
    country = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderSetCountryAction(**data)


class StagedOrderSetCustomFieldActionSchema(StagedOrderUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderSetCustomFieldAction(**data)


class StagedOrderSetCustomLineItemCustomFieldActionSchema(
    StagedOrderUpdateActionSchema
):
    custom_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customLineItemId"
    )
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderSetCustomLineItemCustomFieldAction(**data)


class StagedOrderSetCustomLineItemCustomTypeActionSchema(StagedOrderUpdateActionSchema):
    custom_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customLineItemId"
    )
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
        return models.StagedOrderSetCustomLineItemCustomTypeAction(**data)


class StagedOrderSetCustomLineItemShippingDetailsActionSchema(
    StagedOrderUpdateActionSchema
):
    custom_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customLineItemId"
    )
    shipping_details = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ItemShippingDetailsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="shippingDetails",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderSetCustomLineItemShippingDetailsAction(**data)


class StagedOrderSetCustomLineItemTaxAmountActionSchema(StagedOrderUpdateActionSchema):
    custom_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customLineItemId"
    )
    external_tax_amount = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ExternalTaxAmountDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="externalTaxAmount",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderSetCustomLineItemTaxAmountAction(**data)


class StagedOrderSetCustomLineItemTaxRateActionSchema(StagedOrderUpdateActionSchema):
    custom_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customLineItemId"
    )
    external_tax_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ExternalTaxRateDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="externalTaxRate",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderSetCustomLineItemTaxRateAction(**data)


class StagedOrderSetCustomShippingMethodActionSchema(StagedOrderUpdateActionSchema):
    shipping_method_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="shippingMethodName"
    )
    shipping_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".shipping_method.ShippingRateDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="shippingRate",
    )
    tax_category = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".tax_category.TaxCategoryResourceIdentifierSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="taxCategory",
    )
    external_tax_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ExternalTaxRateDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="externalTaxRate",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderSetCustomShippingMethodAction(**data)


class StagedOrderSetCustomTypeActionSchema(StagedOrderUpdateActionSchema):
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
        return models.StagedOrderSetCustomTypeAction(**data)


class StagedOrderSetCustomerEmailActionSchema(StagedOrderUpdateActionSchema):
    email = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderSetCustomerEmailAction(**data)


class StagedOrderSetCustomerGroupActionSchema(StagedOrderUpdateActionSchema):
    customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".customer_group.CustomerGroupResourceIdentifierSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="customerGroup",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderSetCustomerGroupAction(**data)


class StagedOrderSetCustomerIdActionSchema(StagedOrderUpdateActionSchema):
    customer_id = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="customerId",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderSetCustomerIdAction(**data)


class StagedOrderSetDeliveryAddressActionSchema(StagedOrderUpdateActionSchema):
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
        del data["action"]
        return models.StagedOrderSetDeliveryAddressAction(**data)


class StagedOrderSetDeliveryItemsActionSchema(StagedOrderUpdateActionSchema):
    delivery_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="deliveryId"
    )
    items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.DeliveryItemSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderSetDeliveryItemsAction(**data)


class StagedOrderSetLineItemCustomFieldActionSchema(StagedOrderUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderSetLineItemCustomFieldAction(**data)


class StagedOrderSetLineItemCustomTypeActionSchema(StagedOrderUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
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
        return models.StagedOrderSetLineItemCustomTypeAction(**data)


class StagedOrderSetLineItemDistributionChannelActionSchema(
    StagedOrderUpdateActionSchema
):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    distribution_channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="distributionChannel",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderSetLineItemDistributionChannelAction(**data)


class StagedOrderSetLineItemPriceActionSchema(StagedOrderUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    external_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="externalPrice",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderSetLineItemPriceAction(**data)


class StagedOrderSetLineItemShippingDetailsActionSchema(StagedOrderUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    shipping_details = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ItemShippingDetailsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="shippingDetails",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderSetLineItemShippingDetailsAction(**data)


class StagedOrderSetLineItemTaxAmountActionSchema(StagedOrderUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    external_tax_amount = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ExternalTaxAmountDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="externalTaxAmount",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderSetLineItemTaxAmountAction(**data)


class StagedOrderSetLineItemTaxRateActionSchema(StagedOrderUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    external_tax_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ExternalTaxRateDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="externalTaxRate",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderSetLineItemTaxRateAction(**data)


class StagedOrderSetLineItemTotalPriceActionSchema(StagedOrderUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    external_total_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ExternalLineItemTotalPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="externalTotalPrice",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderSetLineItemTotalPriceAction(**data)


class StagedOrderSetLocaleActionSchema(StagedOrderUpdateActionSchema):
    locale = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderSetLocaleAction(**data)


class StagedOrderSetOrderNumberActionSchema(StagedOrderUpdateActionSchema):
    order_number = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="orderNumber",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderSetOrderNumberAction(**data)


class StagedOrderSetOrderTotalTaxActionSchema(StagedOrderUpdateActionSchema):
    external_total_gross = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="externalTotalGross",
    )
    external_tax_portions = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.TaxPortionDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="externalTaxPortions",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderSetOrderTotalTaxAction(**data)


class StagedOrderSetParcelItemsActionSchema(StagedOrderUpdateActionSchema):
    parcel_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="parcelId"
    )
    items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.DeliveryItemSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderSetParcelItemsAction(**data)


class StagedOrderSetParcelMeasurementsActionSchema(StagedOrderUpdateActionSchema):
    parcel_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="parcelId"
    )
    measurements = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.ParcelMeasurementsSchema"),
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
        return models.StagedOrderSetParcelMeasurementsAction(**data)


class StagedOrderSetParcelTrackingDataActionSchema(StagedOrderUpdateActionSchema):
    parcel_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="parcelId"
    )
    tracking_data = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.TrackingDataSchema"),
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
        del data["action"]
        return models.StagedOrderSetParcelTrackingDataAction(**data)


class StagedOrderSetReturnPaymentStateActionSchema(StagedOrderUpdateActionSchema):
    return_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="returnItemId"
    )
    payment_state = marshmallow_enum.EnumField(
        ReturnPaymentState,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="paymentState",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderSetReturnPaymentStateAction(**data)


class StagedOrderSetReturnShipmentStateActionSchema(StagedOrderUpdateActionSchema):
    return_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="returnItemId"
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
        del data["action"]
        return models.StagedOrderSetReturnShipmentStateAction(**data)


class StagedOrderSetShippingAddressActionSchema(StagedOrderUpdateActionSchema):
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
        return models.StagedOrderSetShippingAddressAction(**data)


class StagedOrderSetShippingAddressAndCustomShippingMethodActionSchema(
    StagedOrderUpdateActionSchema
):
    address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    shipping_method_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="shippingMethodName"
    )
    shipping_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".shipping_method.ShippingRateDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="shippingRate",
    )
    tax_category = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".tax_category.TaxCategoryResourceIdentifierSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="taxCategory",
    )
    external_tax_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ExternalTaxRateDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="externalTaxRate",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderSetShippingAddressAndCustomShippingMethodAction(**data)


class StagedOrderSetShippingAddressAndShippingMethodActionSchema(
    StagedOrderUpdateActionSchema
):
    address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    shipping_method = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".shipping_method.ShippingMethodResourceIdentifierSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="shippingMethod",
    )
    external_tax_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ExternalTaxRateDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="externalTaxRate",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderSetShippingAddressAndShippingMethodAction(**data)


class StagedOrderSetShippingMethodActionSchema(StagedOrderUpdateActionSchema):
    shipping_method = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".shipping_method.ShippingMethodResourceIdentifierSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="shippingMethod",
    )
    external_tax_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ExternalTaxRateDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="externalTaxRate",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderSetShippingMethodAction(**data)


class StagedOrderSetShippingMethodTaxAmountActionSchema(StagedOrderUpdateActionSchema):
    external_tax_amount = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ExternalTaxAmountDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="externalTaxAmount",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderSetShippingMethodTaxAmountAction(**data)


class StagedOrderSetShippingMethodTaxRateActionSchema(StagedOrderUpdateActionSchema):
    external_tax_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ExternalTaxRateDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="externalTaxRate",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderSetShippingMethodTaxRateAction(**data)


class StagedOrderSetShippingRateInputActionSchema(StagedOrderUpdateActionSchema):
    shipping_rate_input = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "Classification": helpers.absmod(
                __name__, ".cart.ClassificationShippingRateInputDraftSchema"
            ),
            "Score": helpers.absmod(
                __name__, ".cart.ScoreShippingRateInputDraftSchema"
            ),
        },
        metadata={"omit_empty": True},
        missing=None,
        data_key="shippingRateInput",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderSetShippingRateInputAction(**data)


class StagedOrderTransitionCustomLineItemStateActionSchema(
    StagedOrderUpdateActionSchema
):
    custom_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customLineItemId"
    )
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)
    from_state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="fromState",
    )
    to_state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="toState",
    )
    actual_transition_date = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="actualTransitionDate",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderTransitionCustomLineItemStateAction(**data)


class StagedOrderTransitionLineItemStateActionSchema(StagedOrderUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)
    from_state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="fromState",
    )
    to_state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="toState",
    )
    actual_transition_date = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="actualTransitionDate",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderTransitionLineItemStateAction(**data)


class StagedOrderTransitionStateActionSchema(StagedOrderUpdateActionSchema):
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    force = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderTransitionStateAction(**data)


class StagedOrderUpdateItemShippingAddressActionSchema(StagedOrderUpdateActionSchema):
    address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderUpdateItemShippingAddressAction(**data)


class StagedOrderUpdateSyncInfoActionSchema(StagedOrderUpdateActionSchema):
    channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    external_id = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="externalId",
    )
    synced_at = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="syncedAt",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StagedOrderUpdateSyncInfoAction(**data)
