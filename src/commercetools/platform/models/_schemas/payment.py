# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..common import ReferenceTypeId
from ..payment import TransactionState, TransactionType
from .common import (
    BaseResourceSchema,
    LocalizedStringField,
    ReferenceSchema,
    ResourceIdentifierSchema,
)
from .type import FieldContainerField

# Fields


# Marshmallow Schemas
class PaymentSchema(BaseResourceSchema):
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
    customer = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer.CustomerReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    anonymous_id = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="anonymousId",
    )
    external_id = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="externalId",
    )
    interface_id = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="interfaceId",
    )
    amount_planned = helpers.Discriminator(
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
        data_key="amountPlanned",
    )
    amount_authorized = helpers.Discriminator(
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
        metadata={"omit_empty": True},
        missing=None,
        data_key="amountAuthorized",
    )
    authorized_until = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="authorizedUntil",
    )
    amount_paid = helpers.Discriminator(
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
        metadata={"omit_empty": True},
        missing=None,
        data_key="amountPaid",
    )
    amount_refunded = helpers.Discriminator(
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
        metadata={"omit_empty": True},
        missing=None,
        data_key="amountRefunded",
    )
    payment_method_info = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".PaymentMethodInfoSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="paymentMethodInfo",
    )
    payment_status = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".PaymentStatusSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="paymentStatus",
    )
    transactions = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".TransactionSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    interface_interactions = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="interfaceInteractions",
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Payment(**data)


class PaymentDraftSchema(helpers.BaseSchema):
    customer = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer.CustomerResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    anonymous_id = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="anonymousId",
    )
    external_id = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="externalId",
    )
    interface_id = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="interfaceId",
    )
    amount_planned = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="amountPlanned",
    )
    amount_authorized = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="amountAuthorized",
    )
    authorized_until = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="authorizedUntil",
    )
    amount_paid = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="amountPaid",
    )
    amount_refunded = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="amountRefunded",
    )
    payment_method_info = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".PaymentMethodInfoSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="paymentMethodInfo",
    )
    payment_status = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".PaymentStatusDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="paymentStatus",
    )
    transactions = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".TransactionDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    interface_interactions = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="interfaceInteractions",
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.PaymentDraft(**data)


class PaymentMethodInfoSchema(helpers.BaseSchema):
    payment_interface = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="paymentInterface",
    )
    method = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    name = LocalizedStringField(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.PaymentMethodInfo(**data)


class PaymentPagedQueryResponseSchema(helpers.BaseSchema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".PaymentSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.PaymentPagedQueryResponse(**data)


class PaymentReferenceSchema(ReferenceSchema):
    obj = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".PaymentSchema"),
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
        return models.PaymentReference(**data)


class PaymentResourceIdentifierSchema(ResourceIdentifierSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.PaymentResourceIdentifier(**data)


class PaymentStatusSchema(helpers.BaseSchema):
    interface_code = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="interfaceCode",
    )
    interface_text = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="interfaceText",
    )
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.PaymentStatus(**data)


class PaymentStatusDraftSchema(helpers.BaseSchema):
    interface_code = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="interfaceCode",
    )
    interface_text = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="interfaceText",
    )
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.PaymentStatusDraft(**data)


class PaymentUpdateSchema(helpers.BaseSchema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addInterfaceInteraction": helpers.absmod(
                    __name__, ".PaymentAddInterfaceInteractionActionSchema"
                ),
                "addTransaction": helpers.absmod(
                    __name__, ".PaymentAddTransactionActionSchema"
                ),
                "changeAmountPlanned": helpers.absmod(
                    __name__, ".PaymentChangeAmountPlannedActionSchema"
                ),
                "changeTransactionInteractionId": helpers.absmod(
                    __name__, ".PaymentChangeTransactionInteractionIdActionSchema"
                ),
                "changeTransactionState": helpers.absmod(
                    __name__, ".PaymentChangeTransactionStateActionSchema"
                ),
                "changeTransactionTimestamp": helpers.absmod(
                    __name__, ".PaymentChangeTransactionTimestampActionSchema"
                ),
                "setAmountPaid": helpers.absmod(
                    __name__, ".PaymentSetAmountPaidActionSchema"
                ),
                "setAmountRefunded": helpers.absmod(
                    __name__, ".PaymentSetAmountRefundedActionSchema"
                ),
                "setAnonymousId": helpers.absmod(
                    __name__, ".PaymentSetAnonymousIdActionSchema"
                ),
                "setAuthorization": helpers.absmod(
                    __name__, ".PaymentSetAuthorizationActionSchema"
                ),
                "setCustomField": helpers.absmod(
                    __name__, ".PaymentSetCustomFieldActionSchema"
                ),
                "setCustomType": helpers.absmod(
                    __name__, ".PaymentSetCustomTypeActionSchema"
                ),
                "setCustomer": helpers.absmod(
                    __name__, ".PaymentSetCustomerActionSchema"
                ),
                "setExternalId": helpers.absmod(
                    __name__, ".PaymentSetExternalIdActionSchema"
                ),
                "setInterfaceId": helpers.absmod(
                    __name__, ".PaymentSetInterfaceIdActionSchema"
                ),
                "setKey": helpers.absmod(__name__, ".PaymentSetKeyActionSchema"),
                "setMethodInfoInterface": helpers.absmod(
                    __name__, ".PaymentSetMethodInfoInterfaceActionSchema"
                ),
                "setMethodInfoMethod": helpers.absmod(
                    __name__, ".PaymentSetMethodInfoMethodActionSchema"
                ),
                "setMethodInfoName": helpers.absmod(
                    __name__, ".PaymentSetMethodInfoNameActionSchema"
                ),
                "setStatusInterfaceCode": helpers.absmod(
                    __name__, ".PaymentSetStatusInterfaceCodeActionSchema"
                ),
                "setStatusInterfaceText": helpers.absmod(
                    __name__, ".PaymentSetStatusInterfaceTextActionSchema"
                ),
                "transitionState": helpers.absmod(
                    __name__, ".PaymentTransitionStateActionSchema"
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

        return models.PaymentUpdate(**data)


class PaymentUpdateActionSchema(helpers.BaseSchema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.PaymentUpdateAction(**data)


class TransactionSchema(helpers.BaseSchema):
    id = marshmallow.fields.String(allow_none=True, missing=None)
    timestamp = marshmallow.fields.DateTime(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    type = marshmallow_enum.EnumField(
        TransactionType, by_value=True, allow_none=True, missing=None
    )
    amount = helpers.Discriminator(
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
    )
    interaction_id = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="interactionId",
    )
    state = marshmallow_enum.EnumField(
        TransactionState,
        by_value=True,
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Transaction(**data)


class TransactionDraftSchema(helpers.BaseSchema):
    timestamp = marshmallow.fields.DateTime(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    type = marshmallow_enum.EnumField(
        TransactionType, by_value=True, allow_none=True, missing=None
    )
    amount = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    interaction_id = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="interactionId",
    )
    state = marshmallow_enum.EnumField(
        TransactionState,
        by_value=True,
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.TransactionDraft(**data)


class PaymentAddInterfaceInteractionActionSchema(PaymentUpdateActionSchema):
    type = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.TypeResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
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
        return models.PaymentAddInterfaceInteractionAction(**data)


class PaymentAddTransactionActionSchema(PaymentUpdateActionSchema):
    transaction = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".TransactionDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.PaymentAddTransactionAction(**data)


class PaymentChangeAmountPlannedActionSchema(PaymentUpdateActionSchema):
    amount = helpers.LazyNestedField(
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
        return models.PaymentChangeAmountPlannedAction(**data)


class PaymentChangeTransactionInteractionIdActionSchema(PaymentUpdateActionSchema):
    transaction_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="transactionId"
    )
    interaction_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="interactionId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.PaymentChangeTransactionInteractionIdAction(**data)


class PaymentChangeTransactionStateActionSchema(PaymentUpdateActionSchema):
    transaction_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="transactionId"
    )
    state = marshmallow_enum.EnumField(
        TransactionState, by_value=True, allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.PaymentChangeTransactionStateAction(**data)


class PaymentChangeTransactionTimestampActionSchema(PaymentUpdateActionSchema):
    transaction_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="transactionId"
    )
    timestamp = marshmallow.fields.DateTime(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.PaymentChangeTransactionTimestampAction(**data)


class PaymentSetAmountPaidActionSchema(PaymentUpdateActionSchema):
    amount = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
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
        return models.PaymentSetAmountPaidAction(**data)


class PaymentSetAmountRefundedActionSchema(PaymentUpdateActionSchema):
    amount = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
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
        return models.PaymentSetAmountRefundedAction(**data)


class PaymentSetAnonymousIdActionSchema(PaymentUpdateActionSchema):
    anonymous_id = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="anonymousId",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.PaymentSetAnonymousIdAction(**data)


class PaymentSetAuthorizationActionSchema(PaymentUpdateActionSchema):
    amount = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    until = marshmallow.fields.DateTime(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.PaymentSetAuthorizationAction(**data)


class PaymentSetCustomFieldActionSchema(PaymentUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.PaymentSetCustomFieldAction(**data)


class PaymentSetCustomTypeActionSchema(PaymentUpdateActionSchema):
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
        return models.PaymentSetCustomTypeAction(**data)


class PaymentSetCustomerActionSchema(PaymentUpdateActionSchema):
    customer = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer.CustomerResourceIdentifierSchema"),
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
        return models.PaymentSetCustomerAction(**data)


class PaymentSetExternalIdActionSchema(PaymentUpdateActionSchema):
    external_id = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="externalId",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.PaymentSetExternalIdAction(**data)


class PaymentSetInterfaceIdActionSchema(PaymentUpdateActionSchema):
    interface_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="interfaceId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.PaymentSetInterfaceIdAction(**data)


class PaymentSetKeyActionSchema(PaymentUpdateActionSchema):
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.PaymentSetKeyAction(**data)


class PaymentSetMethodInfoInterfaceActionSchema(PaymentUpdateActionSchema):
    interface = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.PaymentSetMethodInfoInterfaceAction(**data)


class PaymentSetMethodInfoMethodActionSchema(PaymentUpdateActionSchema):
    method = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.PaymentSetMethodInfoMethodAction(**data)


class PaymentSetMethodInfoNameActionSchema(PaymentUpdateActionSchema):
    name = LocalizedStringField(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.PaymentSetMethodInfoNameAction(**data)


class PaymentSetStatusInterfaceCodeActionSchema(PaymentUpdateActionSchema):
    interface_code = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="interfaceCode",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.PaymentSetStatusInterfaceCodeAction(**data)


class PaymentSetStatusInterfaceTextActionSchema(PaymentUpdateActionSchema):
    interface_text = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="interfaceText"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.PaymentSetStatusInterfaceTextAction(**data)


class PaymentTransitionStateActionSchema(PaymentUpdateActionSchema):
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
        return models.PaymentTransitionStateAction(**data)
