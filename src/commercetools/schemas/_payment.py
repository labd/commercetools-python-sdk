# DO NOT EDIT! This file is automatically generated

import marshmallow
import marshmallow_enum

from commercetools import helpers, types
from commercetools.schemas._common import (
    LocalizedStringField,
    LoggedResourceSchema,
    ReferenceSchema,
    ResourceIdentifierSchema,
)
from commercetools.schemas._type import FieldContainerField

__all__ = [
    "PaymentAddInterfaceInteractionActionSchema",
    "PaymentAddTransactionActionSchema",
    "PaymentChangeAmountPlannedActionSchema",
    "PaymentChangeTransactionInteractionIdActionSchema",
    "PaymentChangeTransactionStateActionSchema",
    "PaymentChangeTransactionTimestampActionSchema",
    "PaymentDraftSchema",
    "PaymentMethodInfoSchema",
    "PaymentPagedQueryResponseSchema",
    "PaymentReferenceSchema",
    "PaymentResourceIdentifierSchema",
    "PaymentSchema",
    "PaymentSetAmountPaidActionSchema",
    "PaymentSetAmountRefundedActionSchema",
    "PaymentSetAnonymousIdActionSchema",
    "PaymentSetAuthorizationActionSchema",
    "PaymentSetCustomFieldActionSchema",
    "PaymentSetCustomTypeActionSchema",
    "PaymentSetCustomerActionSchema",
    "PaymentSetExternalIdActionSchema",
    "PaymentSetInterfaceIdActionSchema",
    "PaymentSetKeyActionSchema",
    "PaymentSetMethodInfoInterfaceActionSchema",
    "PaymentSetMethodInfoMethodActionSchema",
    "PaymentSetMethodInfoNameActionSchema",
    "PaymentSetStatusInterfaceCodeActionSchema",
    "PaymentSetStatusInterfaceTextActionSchema",
    "PaymentStatusDraftSchema",
    "PaymentStatusSchema",
    "PaymentTransitionStateActionSchema",
    "PaymentUpdateActionSchema",
    "PaymentUpdateSchema",
    "TransactionDraftSchema",
    "TransactionSchema",
]


class PaymentDraftSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.PaymentDraft`."
    customer = marshmallow.fields.Nested(
        nested="commercetools.schemas._customer.CustomerResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    anonymous_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="anonymousId"
    )
    external_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="externalId"
    )
    interface_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="interfaceId"
    )
    amount_planned = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.MoneySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        data_key="amountPlanned",
    )
    amount_authorized = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.MoneySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="amountAuthorized",
    )
    authorized_until = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="authorizedUntil"
    )
    amount_paid = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.MoneySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="amountPaid",
    )
    amount_refunded = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.MoneySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="amountRefunded",
    )
    payment_method_info = marshmallow.fields.Nested(
        nested="commercetools.schemas._payment.PaymentMethodInfoSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="paymentMethodInfo",
    )
    payment_status = marshmallow.fields.Nested(
        nested="commercetools.schemas._payment.PaymentStatusDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="paymentStatus",
    )
    transactions = marshmallow.fields.Nested(
        nested="commercetools.schemas._payment.TransactionDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        missing=None,
    )
    interface_interactions = marshmallow.fields.Nested(
        nested="commercetools.schemas._type.CustomFieldsDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        missing=None,
        data_key="interfaceInteractions",
    )
    custom = marshmallow.fields.Nested(
        nested="commercetools.schemas._type.CustomFieldsDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.PaymentDraft(**data)


class PaymentMethodInfoSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.PaymentMethodInfo`."
    payment_interface = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="paymentInterface"
    )
    method = marshmallow.fields.String(allow_none=True, missing=None)
    name = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.PaymentMethodInfo(**data)


class PaymentPagedQueryResponseSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.PaymentPagedQueryResponse`."
    count = marshmallow.fields.Integer(allow_none=True)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True)
    results = marshmallow.fields.Nested(
        nested="commercetools.schemas._payment.PaymentSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.PaymentPagedQueryResponse(**data)


class PaymentReferenceSchema(ReferenceSchema):
    "Marshmallow schema for :class:`commercetools.types.PaymentReference`."
    obj = marshmallow.fields.Nested(
        nested="commercetools.schemas._payment.PaymentSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["type_id"]
        return types.PaymentReference(**data)


class PaymentResourceIdentifierSchema(ResourceIdentifierSchema):
    "Marshmallow schema for :class:`commercetools.types.PaymentResourceIdentifier`."

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["type_id"]
        return types.PaymentResourceIdentifier(**data)


class PaymentSchema(LoggedResourceSchema):
    "Marshmallow schema for :class:`commercetools.types.Payment`."
    customer = marshmallow.fields.Nested(
        nested="commercetools.schemas._customer.CustomerReferenceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    anonymous_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="anonymousId"
    )
    external_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="externalId"
    )
    interface_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="interfaceId"
    )
    amount_planned = helpers.Discriminator(
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "centPrecision": "commercetools.schemas._common.CentPrecisionMoneySchema",
            "highPrecision": "commercetools.schemas._common.HighPrecisionMoneySchema",
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        data_key="amountPlanned",
    )
    amount_authorized = helpers.Discriminator(
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "centPrecision": "commercetools.schemas._common.CentPrecisionMoneySchema",
            "highPrecision": "commercetools.schemas._common.HighPrecisionMoneySchema",
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="amountAuthorized",
    )
    authorized_until = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="authorizedUntil"
    )
    amount_paid = helpers.Discriminator(
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "centPrecision": "commercetools.schemas._common.CentPrecisionMoneySchema",
            "highPrecision": "commercetools.schemas._common.HighPrecisionMoneySchema",
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="amountPaid",
    )
    amount_refunded = helpers.Discriminator(
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "centPrecision": "commercetools.schemas._common.CentPrecisionMoneySchema",
            "highPrecision": "commercetools.schemas._common.HighPrecisionMoneySchema",
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="amountRefunded",
    )
    payment_method_info = marshmallow.fields.Nested(
        nested="commercetools.schemas._payment.PaymentMethodInfoSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        data_key="paymentMethodInfo",
    )
    payment_status = marshmallow.fields.Nested(
        nested="commercetools.schemas._payment.PaymentStatusSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        data_key="paymentStatus",
    )
    transactions = marshmallow.fields.Nested(
        nested="commercetools.schemas._payment.TransactionSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )
    interface_interactions = marshmallow.fields.Nested(
        nested="commercetools.schemas._type.CustomFieldsSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        data_key="interfaceInteractions",
    )
    custom = marshmallow.fields.Nested(
        nested="commercetools.schemas._type.CustomFieldsSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.Payment(**data)


class PaymentStatusDraftSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.PaymentStatusDraft`."
    interface_code = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="interfaceCode"
    )
    interface_text = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="interfaceText"
    )
    state = marshmallow.fields.Nested(
        nested="commercetools.schemas._state.StateResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.PaymentStatusDraft(**data)


class PaymentStatusSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.PaymentStatus`."
    interface_code = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="interfaceCode"
    )
    interface_text = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="interfaceText"
    )
    state = marshmallow.fields.Nested(
        nested="commercetools.schemas._state.StateReferenceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.PaymentStatus(**data)


class PaymentUpdateActionSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.PaymentUpdateAction`."
    action = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.PaymentUpdateAction(**data)


class PaymentUpdateSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.PaymentUpdate`."
    version = marshmallow.fields.Integer(allow_none=True)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addInterfaceInteraction": "commercetools.schemas._payment.PaymentAddInterfaceInteractionActionSchema",
                "addTransaction": "commercetools.schemas._payment.PaymentAddTransactionActionSchema",
                "changeAmountPlanned": "commercetools.schemas._payment.PaymentChangeAmountPlannedActionSchema",
                "changeTransactionInteractionId": "commercetools.schemas._payment.PaymentChangeTransactionInteractionIdActionSchema",
                "changeTransactionState": "commercetools.schemas._payment.PaymentChangeTransactionStateActionSchema",
                "changeTransactionTimestamp": "commercetools.schemas._payment.PaymentChangeTransactionTimestampActionSchema",
                "setAmountPaid": "commercetools.schemas._payment.PaymentSetAmountPaidActionSchema",
                "setAmountRefunded": "commercetools.schemas._payment.PaymentSetAmountRefundedActionSchema",
                "setAnonymousId": "commercetools.schemas._payment.PaymentSetAnonymousIdActionSchema",
                "setAuthorization": "commercetools.schemas._payment.PaymentSetAuthorizationActionSchema",
                "setCustomField": "commercetools.schemas._payment.PaymentSetCustomFieldActionSchema",
                "setCustomType": "commercetools.schemas._payment.PaymentSetCustomTypeActionSchema",
                "setCustomer": "commercetools.schemas._payment.PaymentSetCustomerActionSchema",
                "setExternalId": "commercetools.schemas._payment.PaymentSetExternalIdActionSchema",
                "setInterfaceId": "commercetools.schemas._payment.PaymentSetInterfaceIdActionSchema",
                "setKey": "commercetools.schemas._payment.PaymentSetKeyActionSchema",
                "setMethodInfoInterface": "commercetools.schemas._payment.PaymentSetMethodInfoInterfaceActionSchema",
                "setMethodInfoMethod": "commercetools.schemas._payment.PaymentSetMethodInfoMethodActionSchema",
                "setMethodInfoName": "commercetools.schemas._payment.PaymentSetMethodInfoNameActionSchema",
                "setStatusInterfaceCode": "commercetools.schemas._payment.PaymentSetStatusInterfaceCodeActionSchema",
                "setStatusInterfaceText": "commercetools.schemas._payment.PaymentSetStatusInterfaceTextActionSchema",
                "transitionState": "commercetools.schemas._payment.PaymentTransitionStateActionSchema",
            },
            unknown=marshmallow.EXCLUDE,
            allow_none=True,
        ),
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.PaymentUpdate(**data)


class TransactionDraftSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.TransactionDraft`."
    timestamp = marshmallow.fields.DateTime(allow_none=True, missing=None)
    type = marshmallow_enum.EnumField(types.TransactionType, by_value=True)
    amount = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.MoneySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    interaction_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="interactionId"
    )
    state = marshmallow_enum.EnumField(
        types.TransactionState, by_value=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.TransactionDraft(**data)


class TransactionSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.Transaction`."
    id = marshmallow.fields.String(allow_none=True)
    timestamp = marshmallow.fields.DateTime(allow_none=True, missing=None)
    type = marshmallow_enum.EnumField(types.TransactionType, by_value=True)
    amount = helpers.Discriminator(
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "centPrecision": "commercetools.schemas._common.CentPrecisionMoneySchema",
            "highPrecision": "commercetools.schemas._common.HighPrecisionMoneySchema",
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    interaction_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="interactionId"
    )
    state = marshmallow_enum.EnumField(
        types.TransactionState, by_value=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.Transaction(**data)


class PaymentAddInterfaceInteractionActionSchema(PaymentUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.PaymentAddInterfaceInteractionAction`."
    type = marshmallow.fields.Nested(
        nested="commercetools.schemas._type.TypeResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    fields = FieldContainerField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.PaymentAddInterfaceInteractionAction(**data)


class PaymentAddTransactionActionSchema(PaymentUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.PaymentAddTransactionAction`."
    transaction = marshmallow.fields.Nested(
        nested="commercetools.schemas._payment.TransactionDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.PaymentAddTransactionAction(**data)


class PaymentChangeAmountPlannedActionSchema(PaymentUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.PaymentChangeAmountPlannedAction`."
    amount = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.MoneySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.PaymentChangeAmountPlannedAction(**data)


class PaymentChangeTransactionInteractionIdActionSchema(PaymentUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.PaymentChangeTransactionInteractionIdAction`."
    transaction_id = marshmallow.fields.String(
        allow_none=True, data_key="transactionId"
    )
    interaction_id = marshmallow.fields.String(
        allow_none=True, data_key="interactionId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.PaymentChangeTransactionInteractionIdAction(**data)


class PaymentChangeTransactionStateActionSchema(PaymentUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.PaymentChangeTransactionStateAction`."
    transaction_id = marshmallow.fields.String(
        allow_none=True, data_key="transactionId"
    )
    state = marshmallow_enum.EnumField(types.TransactionState, by_value=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.PaymentChangeTransactionStateAction(**data)


class PaymentChangeTransactionTimestampActionSchema(PaymentUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.PaymentChangeTransactionTimestampAction`."
    transaction_id = marshmallow.fields.String(
        allow_none=True, data_key="transactionId"
    )
    timestamp = marshmallow.fields.DateTime(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.PaymentChangeTransactionTimestampAction(**data)


class PaymentSetAmountPaidActionSchema(PaymentUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.PaymentSetAmountPaidAction`."
    amount = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.MoneySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.PaymentSetAmountPaidAction(**data)


class PaymentSetAmountRefundedActionSchema(PaymentUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.PaymentSetAmountRefundedAction`."
    amount = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.MoneySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.PaymentSetAmountRefundedAction(**data)


class PaymentSetAnonymousIdActionSchema(PaymentUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.PaymentSetAnonymousIdAction`."
    anonymous_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="anonymousId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.PaymentSetAnonymousIdAction(**data)


class PaymentSetAuthorizationActionSchema(PaymentUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.PaymentSetAuthorizationAction`."
    amount = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.MoneySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    until = marshmallow.fields.DateTime(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.PaymentSetAuthorizationAction(**data)


class PaymentSetCustomFieldActionSchema(PaymentUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.PaymentSetCustomFieldAction`."
    name = marshmallow.fields.String(allow_none=True)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.PaymentSetCustomFieldAction(**data)


class PaymentSetCustomTypeActionSchema(PaymentUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.PaymentSetCustomTypeAction`."
    type = marshmallow.fields.Nested(
        nested="commercetools.schemas._type.TypeResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    fields = FieldContainerField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.PaymentSetCustomTypeAction(**data)


class PaymentSetCustomerActionSchema(PaymentUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.PaymentSetCustomerAction`."
    customer = marshmallow.fields.Nested(
        nested="commercetools.schemas._customer.CustomerResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.PaymentSetCustomerAction(**data)


class PaymentSetExternalIdActionSchema(PaymentUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.PaymentSetExternalIdAction`."
    external_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="externalId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.PaymentSetExternalIdAction(**data)


class PaymentSetInterfaceIdActionSchema(PaymentUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.PaymentSetInterfaceIdAction`."
    interface_id = marshmallow.fields.String(allow_none=True, data_key="interfaceId")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.PaymentSetInterfaceIdAction(**data)


class PaymentSetKeyActionSchema(PaymentUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.PaymentSetKeyAction`."
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.PaymentSetKeyAction(**data)


class PaymentSetMethodInfoInterfaceActionSchema(PaymentUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.PaymentSetMethodInfoInterfaceAction`."
    interface = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.PaymentSetMethodInfoInterfaceAction(**data)


class PaymentSetMethodInfoMethodActionSchema(PaymentUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.PaymentSetMethodInfoMethodAction`."
    method = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.PaymentSetMethodInfoMethodAction(**data)


class PaymentSetMethodInfoNameActionSchema(PaymentUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.PaymentSetMethodInfoNameAction`."
    name = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.PaymentSetMethodInfoNameAction(**data)


class PaymentSetStatusInterfaceCodeActionSchema(PaymentUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.PaymentSetStatusInterfaceCodeAction`."
    interface_code = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="interfaceCode"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.PaymentSetStatusInterfaceCodeAction(**data)


class PaymentSetStatusInterfaceTextActionSchema(PaymentUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.PaymentSetStatusInterfaceTextAction`."
    interface_text = marshmallow.fields.String(
        allow_none=True, data_key="interfaceText"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.PaymentSetStatusInterfaceTextAction(**data)


class PaymentTransitionStateActionSchema(PaymentUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.PaymentTransitionStateAction`."
    state = marshmallow.fields.Nested(
        nested="commercetools.schemas._state.StateResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    force = marshmallow.fields.Bool(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.PaymentTransitionStateAction(**data)
