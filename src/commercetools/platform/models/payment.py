# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import BaseResource, Reference, ReferenceTypeId, ResourceIdentifier

if typing.TYPE_CHECKING:
    from .common import (
        CreatedBy,
        LastModifiedBy,
        LocalizedString,
        Money,
        ReferenceTypeId,
        TypedMoney,
    )
    from .customer import CustomerReference, CustomerResourceIdentifier
    from .state import StateReference, StateResourceIdentifier
    from .type import (
        CustomFields,
        CustomFieldsDraft,
        FieldContainer,
        TypeResourceIdentifier,
    )

__all__ = [
    "Payment",
    "PaymentAddInterfaceInteractionAction",
    "PaymentAddTransactionAction",
    "PaymentChangeAmountPlannedAction",
    "PaymentChangeTransactionInteractionIdAction",
    "PaymentChangeTransactionStateAction",
    "PaymentChangeTransactionTimestampAction",
    "PaymentDraft",
    "PaymentMethodInfo",
    "PaymentPagedQueryResponse",
    "PaymentReference",
    "PaymentResourceIdentifier",
    "PaymentSetAmountPaidAction",
    "PaymentSetAmountRefundedAction",
    "PaymentSetAnonymousIdAction",
    "PaymentSetAuthorizationAction",
    "PaymentSetCustomFieldAction",
    "PaymentSetCustomTypeAction",
    "PaymentSetCustomerAction",
    "PaymentSetExternalIdAction",
    "PaymentSetInterfaceIdAction",
    "PaymentSetKeyAction",
    "PaymentSetMethodInfoInterfaceAction",
    "PaymentSetMethodInfoMethodAction",
    "PaymentSetMethodInfoNameAction",
    "PaymentSetStatusInterfaceCodeAction",
    "PaymentSetStatusInterfaceTextAction",
    "PaymentStatus",
    "PaymentStatusDraft",
    "PaymentTransitionStateAction",
    "PaymentUpdate",
    "PaymentUpdateAction",
    "Transaction",
    "TransactionDraft",
    "TransactionState",
    "TransactionType",
]


class Payment(BaseResource):
    #: Present on resources updated after 1/02/2019 except for events not tracked.
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Present on resources created after 1/02/2019 except for events not tracked.
    created_by: typing.Optional["CreatedBy"]
    #: A reference to the customer this payment belongs to.
    customer: typing.Optional["CustomerReference"]
    #: Identifies payments belonging to an anonymous session (the customer has not signed up/in yet).
    anonymous_id: typing.Optional[str]
    external_id: typing.Optional[str]
    #: The identifier that is used by the interface that manages the payment (usually the PSP).
    #: Cannot be changed once it has been set.
    #: The combination of this ID and the PaymentMethodInfo `paymentInterface` must be unique.
    interface_id: typing.Optional[str]
    #: How much money this payment intends to receive from the customer.
    #: The value usually matches the cart or order gross total.
    amount_planned: "TypedMoney"
    amount_authorized: typing.Optional["TypedMoney"]
    authorized_until: typing.Optional[str]
    amount_paid: typing.Optional["TypedMoney"]
    amount_refunded: typing.Optional["TypedMoney"]
    payment_method_info: "PaymentMethodInfo"
    payment_status: "PaymentStatus"
    #: A list of financial transactions of different TransactionTypes with different TransactionStates.
    transactions: typing.List["Transaction"]
    #: Interface interactions can be requests sent to the PSP, responses received from the PSP or notifications received from the PSP.
    #: Some interactions may result in a transaction.
    #: If so, the `interactionId` in the Transaction should be set to match the ID of the PSP for the interaction.
    #: Interactions are managed by the PSP integration and are usually neither written nor read by the user facing frontends or other services.
    interface_interactions: typing.List["CustomFields"]
    custom: typing.Optional["CustomFields"]
    #: User-specific unique identifier for the payment (max.
    #: 256 characters).
    key: typing.Optional[str]

    def __init__(
        self,
        *,
        id: str,
        version: int,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        customer: typing.Optional["CustomerReference"] = None,
        anonymous_id: typing.Optional[str] = None,
        external_id: typing.Optional[str] = None,
        interface_id: typing.Optional[str] = None,
        amount_planned: "TypedMoney",
        amount_authorized: typing.Optional["TypedMoney"] = None,
        authorized_until: typing.Optional[str] = None,
        amount_paid: typing.Optional["TypedMoney"] = None,
        amount_refunded: typing.Optional["TypedMoney"] = None,
        payment_method_info: "PaymentMethodInfo",
        payment_status: "PaymentStatus",
        transactions: typing.List["Transaction"],
        interface_interactions: typing.List["CustomFields"],
        custom: typing.Optional["CustomFields"] = None,
        key: typing.Optional[str] = None
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.customer = customer
        self.anonymous_id = anonymous_id
        self.external_id = external_id
        self.interface_id = interface_id
        self.amount_planned = amount_planned
        self.amount_authorized = amount_authorized
        self.authorized_until = authorized_until
        self.amount_paid = amount_paid
        self.amount_refunded = amount_refunded
        self.payment_method_info = payment_method_info
        self.payment_status = payment_status
        self.transactions = transactions
        self.interface_interactions = interface_interactions
        self.custom = custom
        self.key = key
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Payment":
        from ._schemas.payment import PaymentSchema

        return PaymentSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentSchema

        return PaymentSchema().dump(self)


class PaymentDraft(_BaseType):
    #: A reference to the customer this payment belongs to.
    customer: typing.Optional["CustomerResourceIdentifier"]
    #: Identifies payments belonging to an anonymous session (the customer has not signed up/in yet).
    anonymous_id: typing.Optional[str]
    external_id: typing.Optional[str]
    #: The identifier that is used by the interface that manages the payment (usually the PSP).
    #: Cannot be changed once it has been set.
    #: The combination of this ID and the PaymentMethodInfo `paymentInterface` must be unique.
    interface_id: typing.Optional[str]
    #: How much money this payment intends to receive from the customer.
    #: The value usually matches the cart or order gross total.
    amount_planned: "Money"
    amount_authorized: typing.Optional["Money"]
    authorized_until: typing.Optional[str]
    amount_paid: typing.Optional["Money"]
    amount_refunded: typing.Optional["Money"]
    payment_method_info: typing.Optional["PaymentMethodInfo"]
    payment_status: typing.Optional["PaymentStatusDraft"]
    #: A list of financial transactions of different TransactionTypes with different TransactionStates.
    transactions: typing.Optional[typing.List["TransactionDraft"]]
    #: Interface interactions can be requests send to the PSP, responses received from the PSP or notifications received from the PSP.
    #: Some interactions may result in a transaction.
    #: If so, the `interactionId` in the Transaction should be set to match the ID of the PSP for the interaction.
    #: Interactions are managed by the PSP integration and are usually neither written nor read by the user facing frontends or other services.
    interface_interactions: typing.Optional[typing.List["CustomFieldsDraft"]]
    custom: typing.Optional["CustomFieldsDraft"]
    #: User-specific unique identifier for the payment (max.
    #: 256 characters).
    key: typing.Optional[str]

    def __init__(
        self,
        *,
        customer: typing.Optional["CustomerResourceIdentifier"] = None,
        anonymous_id: typing.Optional[str] = None,
        external_id: typing.Optional[str] = None,
        interface_id: typing.Optional[str] = None,
        amount_planned: "Money",
        amount_authorized: typing.Optional["Money"] = None,
        authorized_until: typing.Optional[str] = None,
        amount_paid: typing.Optional["Money"] = None,
        amount_refunded: typing.Optional["Money"] = None,
        payment_method_info: typing.Optional["PaymentMethodInfo"] = None,
        payment_status: typing.Optional["PaymentStatusDraft"] = None,
        transactions: typing.Optional[typing.List["TransactionDraft"]] = None,
        interface_interactions: typing.Optional[
            typing.List["CustomFieldsDraft"]
        ] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        key: typing.Optional[str] = None
    ):
        self.customer = customer
        self.anonymous_id = anonymous_id
        self.external_id = external_id
        self.interface_id = interface_id
        self.amount_planned = amount_planned
        self.amount_authorized = amount_authorized
        self.authorized_until = authorized_until
        self.amount_paid = amount_paid
        self.amount_refunded = amount_refunded
        self.payment_method_info = payment_method_info
        self.payment_status = payment_status
        self.transactions = transactions
        self.interface_interactions = interface_interactions
        self.custom = custom
        self.key = key
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "PaymentDraft":
        from ._schemas.payment import PaymentDraftSchema

        return PaymentDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentDraftSchema

        return PaymentDraftSchema().dump(self)


class PaymentMethodInfo(_BaseType):
    #: The interface that handles the payment (usually a PSP).
    #: Cannot be changed once it has been set.
    #: The combination of Payment`interfaceId` and this field must be unique.
    payment_interface: typing.Optional[str]
    #: The payment method that is used, e.g.
    #: e.g.
    #: a conventional string representing Credit Card, Cash Advance etc.
    method: typing.Optional[str]
    #: A human-readable, localized name for the payment method, e.g.
    #: 'Credit Card'.
    name: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        payment_interface: typing.Optional[str] = None,
        method: typing.Optional[str] = None,
        name: typing.Optional["LocalizedString"] = None
    ):
        self.payment_interface = payment_interface
        self.method = method
        self.name = name
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "PaymentMethodInfo":
        from ._schemas.payment import PaymentMethodInfoSchema

        return PaymentMethodInfoSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentMethodInfoSchema

        return PaymentMethodInfoSchema().dump(self)


class PaymentPagedQueryResponse(_BaseType):
    limit: int
    count: int
    total: typing.Optional[int]
    offset: int
    results: typing.List["Payment"]

    def __init__(
        self,
        *,
        limit: int,
        count: int,
        total: typing.Optional[int] = None,
        offset: int,
        results: typing.List["Payment"]
    ):
        self.limit = limit
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentPagedQueryResponse":
        from ._schemas.payment import PaymentPagedQueryResponseSchema

        return PaymentPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentPagedQueryResponseSchema

        return PaymentPagedQueryResponseSchema().dump(self)


class PaymentReference(Reference):
    obj: typing.Optional["Payment"]

    def __init__(self, *, id: str, obj: typing.Optional["Payment"] = None):
        self.obj = obj
        super().__init__(id=id, type_id=ReferenceTypeId.PAYMENT)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "PaymentReference":
        from ._schemas.payment import PaymentReferenceSchema

        return PaymentReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentReferenceSchema

        return PaymentReferenceSchema().dump(self)


class PaymentResourceIdentifier(ResourceIdentifier):
    def __init__(
        self, *, id: typing.Optional[str] = None, key: typing.Optional[str] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.PAYMENT)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentResourceIdentifier":
        from ._schemas.payment import PaymentResourceIdentifierSchema

        return PaymentResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentResourceIdentifierSchema

        return PaymentResourceIdentifierSchema().dump(self)


class PaymentStatus(_BaseType):
    #: A code describing the current status returned by the interface that processes the payment.
    interface_code: typing.Optional[str]
    #: A text describing the current status returned by the interface that processes the payment.
    interface_text: typing.Optional[str]
    state: typing.Optional["StateReference"]

    def __init__(
        self,
        *,
        interface_code: typing.Optional[str] = None,
        interface_text: typing.Optional[str] = None,
        state: typing.Optional["StateReference"] = None
    ):
        self.interface_code = interface_code
        self.interface_text = interface_text
        self.state = state
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "PaymentStatus":
        from ._schemas.payment import PaymentStatusSchema

        return PaymentStatusSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentStatusSchema

        return PaymentStatusSchema().dump(self)


class PaymentStatusDraft(_BaseType):
    interface_code: typing.Optional[str]
    interface_text: typing.Optional[str]
    state: typing.Optional["StateResourceIdentifier"]

    def __init__(
        self,
        *,
        interface_code: typing.Optional[str] = None,
        interface_text: typing.Optional[str] = None,
        state: typing.Optional["StateResourceIdentifier"] = None
    ):
        self.interface_code = interface_code
        self.interface_text = interface_text
        self.state = state
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "PaymentStatusDraft":
        from ._schemas.payment import PaymentStatusDraftSchema

        return PaymentStatusDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentStatusDraftSchema

        return PaymentStatusDraftSchema().dump(self)


class PaymentUpdate(_BaseType):
    version: int
    actions: typing.List["PaymentUpdateAction"]

    def __init__(self, *, version: int, actions: typing.List["PaymentUpdateAction"]):
        self.version = version
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "PaymentUpdate":
        from ._schemas.payment import PaymentUpdateSchema

        return PaymentUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentUpdateSchema

        return PaymentUpdateSchema().dump(self)


class PaymentUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "PaymentUpdateAction":
        if data["action"] == "addInterfaceInteraction":
            from ._schemas.payment import PaymentAddInterfaceInteractionActionSchema

            return PaymentAddInterfaceInteractionActionSchema().load(data)
        if data["action"] == "addTransaction":
            from ._schemas.payment import PaymentAddTransactionActionSchema

            return PaymentAddTransactionActionSchema().load(data)
        if data["action"] == "changeAmountPlanned":
            from ._schemas.payment import PaymentChangeAmountPlannedActionSchema

            return PaymentChangeAmountPlannedActionSchema().load(data)
        if data["action"] == "changeTransactionInteractionId":
            from ._schemas.payment import (
                PaymentChangeTransactionInteractionIdActionSchema,
            )

            return PaymentChangeTransactionInteractionIdActionSchema().load(data)
        if data["action"] == "changeTransactionState":
            from ._schemas.payment import PaymentChangeTransactionStateActionSchema

            return PaymentChangeTransactionStateActionSchema().load(data)
        if data["action"] == "changeTransactionTimestamp":
            from ._schemas.payment import PaymentChangeTransactionTimestampActionSchema

            return PaymentChangeTransactionTimestampActionSchema().load(data)
        if data["action"] == "setAmountPaid":
            from ._schemas.payment import PaymentSetAmountPaidActionSchema

            return PaymentSetAmountPaidActionSchema().load(data)
        if data["action"] == "setAmountRefunded":
            from ._schemas.payment import PaymentSetAmountRefundedActionSchema

            return PaymentSetAmountRefundedActionSchema().load(data)
        if data["action"] == "setAnonymousId":
            from ._schemas.payment import PaymentSetAnonymousIdActionSchema

            return PaymentSetAnonymousIdActionSchema().load(data)
        if data["action"] == "setAuthorization":
            from ._schemas.payment import PaymentSetAuthorizationActionSchema

            return PaymentSetAuthorizationActionSchema().load(data)
        if data["action"] == "setCustomField":
            from ._schemas.payment import PaymentSetCustomFieldActionSchema

            return PaymentSetCustomFieldActionSchema().load(data)
        if data["action"] == "setCustomType":
            from ._schemas.payment import PaymentSetCustomTypeActionSchema

            return PaymentSetCustomTypeActionSchema().load(data)
        if data["action"] == "setCustomer":
            from ._schemas.payment import PaymentSetCustomerActionSchema

            return PaymentSetCustomerActionSchema().load(data)
        if data["action"] == "setExternalId":
            from ._schemas.payment import PaymentSetExternalIdActionSchema

            return PaymentSetExternalIdActionSchema().load(data)
        if data["action"] == "setInterfaceId":
            from ._schemas.payment import PaymentSetInterfaceIdActionSchema

            return PaymentSetInterfaceIdActionSchema().load(data)
        if data["action"] == "setKey":
            from ._schemas.payment import PaymentSetKeyActionSchema

            return PaymentSetKeyActionSchema().load(data)
        if data["action"] == "setMethodInfoInterface":
            from ._schemas.payment import PaymentSetMethodInfoInterfaceActionSchema

            return PaymentSetMethodInfoInterfaceActionSchema().load(data)
        if data["action"] == "setMethodInfoMethod":
            from ._schemas.payment import PaymentSetMethodInfoMethodActionSchema

            return PaymentSetMethodInfoMethodActionSchema().load(data)
        if data["action"] == "setMethodInfoName":
            from ._schemas.payment import PaymentSetMethodInfoNameActionSchema

            return PaymentSetMethodInfoNameActionSchema().load(data)
        if data["action"] == "setStatusInterfaceCode":
            from ._schemas.payment import PaymentSetStatusInterfaceCodeActionSchema

            return PaymentSetStatusInterfaceCodeActionSchema().load(data)
        if data["action"] == "setStatusInterfaceText":
            from ._schemas.payment import PaymentSetStatusInterfaceTextActionSchema

            return PaymentSetStatusInterfaceTextActionSchema().load(data)
        if data["action"] == "transitionState":
            from ._schemas.payment import PaymentTransitionStateActionSchema

            return PaymentTransitionStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentUpdateActionSchema

        return PaymentUpdateActionSchema().dump(self)


class Transaction(_BaseType):
    #: The unique ID of this object.
    id: str
    #: The time at which the transaction took place.
    timestamp: typing.Optional[datetime.datetime]
    #: The type of this transaction.
    type: "TransactionType"
    amount: "TypedMoney"
    #: The identifier that is used by the interface that managed the transaction (usually the PSP).
    #: If a matching interaction was logged in the `interfaceInteractions` array, the corresponding interaction should be findable with this ID.
    interaction_id: typing.Optional[str]
    #: The state of this transaction.
    state: typing.Optional["TransactionState"]

    def __init__(
        self,
        *,
        id: str,
        timestamp: typing.Optional[datetime.datetime] = None,
        type: "TransactionType",
        amount: "TypedMoney",
        interaction_id: typing.Optional[str] = None,
        state: typing.Optional["TransactionState"] = None
    ):
        self.id = id
        self.timestamp = timestamp
        self.type = type
        self.amount = amount
        self.interaction_id = interaction_id
        self.state = state
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Transaction":
        from ._schemas.payment import TransactionSchema

        return TransactionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import TransactionSchema

        return TransactionSchema().dump(self)


class TransactionDraft(_BaseType):
    #: The time at which the transaction took place.
    timestamp: typing.Optional[datetime.datetime]
    #: The type of this transaction.
    type: "TransactionType"
    amount: "Money"
    #: The identifier that is used by the interface that managed the transaction (usually the PSP).
    #: If a matching interaction was logged in the `interfaceInteractions` array, the corresponding interaction should be findable with this ID.
    interaction_id: typing.Optional[str]
    #: The state of this transaction.
    #: If not set, defaults to `Initial`.
    state: typing.Optional["TransactionState"]

    def __init__(
        self,
        *,
        timestamp: typing.Optional[datetime.datetime] = None,
        type: "TransactionType",
        amount: "Money",
        interaction_id: typing.Optional[str] = None,
        state: typing.Optional["TransactionState"] = None
    ):
        self.timestamp = timestamp
        self.type = type
        self.amount = amount
        self.interaction_id = interaction_id
        self.state = state
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TransactionDraft":
        from ._schemas.payment import TransactionDraftSchema

        return TransactionDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import TransactionDraftSchema

        return TransactionDraftSchema().dump(self)


class TransactionState(enum.Enum):
    INITIAL = "Initial"
    PENDING = "Pending"
    SUCCESS = "Success"
    FAILURE = "Failure"


class TransactionType(enum.Enum):
    AUTHORIZATION = "Authorization"
    CANCEL_AUTHORIZATION = "CancelAuthorization"
    CHARGE = "Charge"
    REFUND = "Refund"
    CHARGEBACK = "Chargeback"


class PaymentAddInterfaceInteractionAction(PaymentUpdateAction):
    type: "TypeResourceIdentifier"
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        type: "TypeResourceIdentifier",
        fields: typing.Optional["FieldContainer"] = None
    ):
        self.type = type
        self.fields = fields
        super().__init__(action="addInterfaceInteraction")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentAddInterfaceInteractionAction":
        from ._schemas.payment import PaymentAddInterfaceInteractionActionSchema

        return PaymentAddInterfaceInteractionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentAddInterfaceInteractionActionSchema

        return PaymentAddInterfaceInteractionActionSchema().dump(self)


class PaymentAddTransactionAction(PaymentUpdateAction):
    transaction: "TransactionDraft"

    def __init__(self, *, transaction: "TransactionDraft"):
        self.transaction = transaction
        super().__init__(action="addTransaction")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentAddTransactionAction":
        from ._schemas.payment import PaymentAddTransactionActionSchema

        return PaymentAddTransactionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentAddTransactionActionSchema

        return PaymentAddTransactionActionSchema().dump(self)


class PaymentChangeAmountPlannedAction(PaymentUpdateAction):
    amount: "Money"

    def __init__(self, *, amount: "Money"):
        self.amount = amount
        super().__init__(action="changeAmountPlanned")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentChangeAmountPlannedAction":
        from ._schemas.payment import PaymentChangeAmountPlannedActionSchema

        return PaymentChangeAmountPlannedActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentChangeAmountPlannedActionSchema

        return PaymentChangeAmountPlannedActionSchema().dump(self)


class PaymentChangeTransactionInteractionIdAction(PaymentUpdateAction):
    transaction_id: str
    interaction_id: str

    def __init__(self, *, transaction_id: str, interaction_id: str):
        self.transaction_id = transaction_id
        self.interaction_id = interaction_id
        super().__init__(action="changeTransactionInteractionId")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentChangeTransactionInteractionIdAction":
        from ._schemas.payment import PaymentChangeTransactionInteractionIdActionSchema

        return PaymentChangeTransactionInteractionIdActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentChangeTransactionInteractionIdActionSchema

        return PaymentChangeTransactionInteractionIdActionSchema().dump(self)


class PaymentChangeTransactionStateAction(PaymentUpdateAction):
    transaction_id: str
    state: "TransactionState"

    def __init__(self, *, transaction_id: str, state: "TransactionState"):
        self.transaction_id = transaction_id
        self.state = state
        super().__init__(action="changeTransactionState")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentChangeTransactionStateAction":
        from ._schemas.payment import PaymentChangeTransactionStateActionSchema

        return PaymentChangeTransactionStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentChangeTransactionStateActionSchema

        return PaymentChangeTransactionStateActionSchema().dump(self)


class PaymentChangeTransactionTimestampAction(PaymentUpdateAction):
    transaction_id: str
    timestamp: datetime.datetime

    def __init__(self, *, transaction_id: str, timestamp: datetime.datetime):
        self.transaction_id = transaction_id
        self.timestamp = timestamp
        super().__init__(action="changeTransactionTimestamp")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentChangeTransactionTimestampAction":
        from ._schemas.payment import PaymentChangeTransactionTimestampActionSchema

        return PaymentChangeTransactionTimestampActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentChangeTransactionTimestampActionSchema

        return PaymentChangeTransactionTimestampActionSchema().dump(self)


class PaymentSetAmountPaidAction(PaymentUpdateAction):
    amount: typing.Optional["Money"]

    def __init__(self, *, amount: typing.Optional["Money"] = None):
        self.amount = amount
        super().__init__(action="setAmountPaid")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentSetAmountPaidAction":
        from ._schemas.payment import PaymentSetAmountPaidActionSchema

        return PaymentSetAmountPaidActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentSetAmountPaidActionSchema

        return PaymentSetAmountPaidActionSchema().dump(self)


class PaymentSetAmountRefundedAction(PaymentUpdateAction):
    amount: typing.Optional["Money"]

    def __init__(self, *, amount: typing.Optional["Money"] = None):
        self.amount = amount
        super().__init__(action="setAmountRefunded")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentSetAmountRefundedAction":
        from ._schemas.payment import PaymentSetAmountRefundedActionSchema

        return PaymentSetAmountRefundedActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentSetAmountRefundedActionSchema

        return PaymentSetAmountRefundedActionSchema().dump(self)


class PaymentSetAnonymousIdAction(PaymentUpdateAction):
    #: Anonymous ID of the anonymous customer that this payment belongs to.
    #: If this field is not set any existing `anonymousId` is removed.
    anonymous_id: typing.Optional[str]

    def __init__(self, *, anonymous_id: typing.Optional[str] = None):
        self.anonymous_id = anonymous_id
        super().__init__(action="setAnonymousId")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentSetAnonymousIdAction":
        from ._schemas.payment import PaymentSetAnonymousIdActionSchema

        return PaymentSetAnonymousIdActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentSetAnonymousIdActionSchema

        return PaymentSetAnonymousIdActionSchema().dump(self)


class PaymentSetAuthorizationAction(PaymentUpdateAction):
    amount: typing.Optional["Money"]
    until: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        amount: typing.Optional["Money"] = None,
        until: typing.Optional[datetime.datetime] = None
    ):
        self.amount = amount
        self.until = until
        super().__init__(action="setAuthorization")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentSetAuthorizationAction":
        from ._schemas.payment import PaymentSetAuthorizationActionSchema

        return PaymentSetAuthorizationActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentSetAuthorizationActionSchema

        return PaymentSetAuthorizationActionSchema().dump(self)


class PaymentSetCustomFieldAction(PaymentUpdateAction):
    name: str
    value: typing.Optional[typing.Any]

    def __init__(self, *, name: str, value: typing.Optional[typing.Any] = None):
        self.name = name
        self.value = value
        super().__init__(action="setCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentSetCustomFieldAction":
        from ._schemas.payment import PaymentSetCustomFieldActionSchema

        return PaymentSetCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentSetCustomFieldActionSchema

        return PaymentSetCustomFieldActionSchema().dump(self)


class PaymentSetCustomTypeAction(PaymentUpdateAction):
    #: If set, the custom type is set to this new value.
    #: If absent, the custom type and any existing custom fields are removed.
    type: typing.Optional["TypeResourceIdentifier"]
    #: Sets the custom fields to this value.
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        type: typing.Optional["TypeResourceIdentifier"] = None,
        fields: typing.Optional["FieldContainer"] = None
    ):
        self.type = type
        self.fields = fields
        super().__init__(action="setCustomType")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentSetCustomTypeAction":
        from ._schemas.payment import PaymentSetCustomTypeActionSchema

        return PaymentSetCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentSetCustomTypeActionSchema

        return PaymentSetCustomTypeActionSchema().dump(self)


class PaymentSetCustomerAction(PaymentUpdateAction):
    #: A reference to the customer this payment belongs to.
    customer: typing.Optional["CustomerResourceIdentifier"]

    def __init__(
        self, *, customer: typing.Optional["CustomerResourceIdentifier"] = None
    ):
        self.customer = customer
        super().__init__(action="setCustomer")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentSetCustomerAction":
        from ._schemas.payment import PaymentSetCustomerActionSchema

        return PaymentSetCustomerActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentSetCustomerActionSchema

        return PaymentSetCustomerActionSchema().dump(self)


class PaymentSetExternalIdAction(PaymentUpdateAction):
    external_id: typing.Optional[str]

    def __init__(self, *, external_id: typing.Optional[str] = None):
        self.external_id = external_id
        super().__init__(action="setExternalId")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentSetExternalIdAction":
        from ._schemas.payment import PaymentSetExternalIdActionSchema

        return PaymentSetExternalIdActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentSetExternalIdActionSchema

        return PaymentSetExternalIdActionSchema().dump(self)


class PaymentSetInterfaceIdAction(PaymentUpdateAction):
    interface_id: str

    def __init__(self, *, interface_id: str):
        self.interface_id = interface_id
        super().__init__(action="setInterfaceId")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentSetInterfaceIdAction":
        from ._schemas.payment import PaymentSetInterfaceIdActionSchema

        return PaymentSetInterfaceIdActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentSetInterfaceIdActionSchema

        return PaymentSetInterfaceIdActionSchema().dump(self)


class PaymentSetKeyAction(PaymentUpdateAction):
    #: User-specific unique identifier for the payment (max.
    #: 256 characters).
    #: If not provided an existing key will be removed.
    key: typing.Optional[str]

    def __init__(self, *, key: typing.Optional[str] = None):
        self.key = key
        super().__init__(action="setKey")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "PaymentSetKeyAction":
        from ._schemas.payment import PaymentSetKeyActionSchema

        return PaymentSetKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentSetKeyActionSchema

        return PaymentSetKeyActionSchema().dump(self)


class PaymentSetMethodInfoInterfaceAction(PaymentUpdateAction):
    interface: str

    def __init__(self, *, interface: str):
        self.interface = interface
        super().__init__(action="setMethodInfoInterface")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentSetMethodInfoInterfaceAction":
        from ._schemas.payment import PaymentSetMethodInfoInterfaceActionSchema

        return PaymentSetMethodInfoInterfaceActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentSetMethodInfoInterfaceActionSchema

        return PaymentSetMethodInfoInterfaceActionSchema().dump(self)


class PaymentSetMethodInfoMethodAction(PaymentUpdateAction):
    #: If not provided, the method is unset.
    method: typing.Optional[str]

    def __init__(self, *, method: typing.Optional[str] = None):
        self.method = method
        super().__init__(action="setMethodInfoMethod")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentSetMethodInfoMethodAction":
        from ._schemas.payment import PaymentSetMethodInfoMethodActionSchema

        return PaymentSetMethodInfoMethodActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentSetMethodInfoMethodActionSchema

        return PaymentSetMethodInfoMethodActionSchema().dump(self)


class PaymentSetMethodInfoNameAction(PaymentUpdateAction):
    #: If not provided, the name is unset.
    name: typing.Optional["LocalizedString"]

    def __init__(self, *, name: typing.Optional["LocalizedString"] = None):
        self.name = name
        super().__init__(action="setMethodInfoName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentSetMethodInfoNameAction":
        from ._schemas.payment import PaymentSetMethodInfoNameActionSchema

        return PaymentSetMethodInfoNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentSetMethodInfoNameActionSchema

        return PaymentSetMethodInfoNameActionSchema().dump(self)


class PaymentSetStatusInterfaceCodeAction(PaymentUpdateAction):
    interface_code: typing.Optional[str]

    def __init__(self, *, interface_code: typing.Optional[str] = None):
        self.interface_code = interface_code
        super().__init__(action="setStatusInterfaceCode")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentSetStatusInterfaceCodeAction":
        from ._schemas.payment import PaymentSetStatusInterfaceCodeActionSchema

        return PaymentSetStatusInterfaceCodeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentSetStatusInterfaceCodeActionSchema

        return PaymentSetStatusInterfaceCodeActionSchema().dump(self)


class PaymentSetStatusInterfaceTextAction(PaymentUpdateAction):
    interface_text: str

    def __init__(self, *, interface_text: str):
        self.interface_text = interface_text
        super().__init__(action="setStatusInterfaceText")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentSetStatusInterfaceTextAction":
        from ._schemas.payment import PaymentSetStatusInterfaceTextActionSchema

        return PaymentSetStatusInterfaceTextActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentSetStatusInterfaceTextActionSchema

        return PaymentSetStatusInterfaceTextActionSchema().dump(self)


class PaymentTransitionStateAction(PaymentUpdateAction):
    state: "StateResourceIdentifier"
    force: typing.Optional[bool]

    def __init__(
        self, *, state: "StateResourceIdentifier", force: typing.Optional[bool] = None
    ):
        self.state = state
        self.force = force
        super().__init__(action="transitionState")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "PaymentTransitionStateAction":
        from ._schemas.payment import PaymentTransitionStateActionSchema

        return PaymentTransitionStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.payment import PaymentTransitionStateActionSchema

        return PaymentTransitionStateActionSchema().dump(self)
