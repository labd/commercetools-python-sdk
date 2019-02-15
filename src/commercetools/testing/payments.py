import copy
import datetime
import typing
import uuid

from commercetools import schemas, types
from commercetools.testing import utils
from commercetools.testing.abstract import BaseModel, ServiceBackend
from commercetools.testing.utils import update_attribute_add_item


class PaymentsModel(BaseModel):
    _primary_type_name = "payment"
    _resource_schema = schemas.PaymentSchema

    def _create_from_draft(
        self, draft: types.PaymentDraft, id: typing.Optional[str] = None
    ) -> types.Payment:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        payment = types.Payment(
            id=str(object_id),
            key=draft.key,
            version=1,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            last_modified_at=datetime.datetime.now(datetime.timezone.utc),
            customer=draft.customer,
            amount_authorized=draft.amount_authorized,
            amount_paid=utils._money_to_typed(draft.amount_paid),
            amount_planned=utils._money_to_typed(draft.amount_planned),
            amount_refunded=utils._money_to_typed(draft.amount_refunded),
            anonymous_id=draft.anonymous_id,
            payment_method_info=draft.payment_method_info,
            payment_status=draft.payment_status,
            transactions=[
                self._create_transaction_draft(transaction)
                for transaction in draft.transactions or []
            ],
            custom=utils.create_from_draft(draft.custom),
        )
        return payment

    def _create_transaction_draft(
        self, draft: types.TransactionDraft
    ) -> types.Transaction:
        return types.Transaction(
            id=str(uuid.uuid4()),
            timestamp=draft.timestamp,
            type=draft.type,
            amount=utils._money_to_typed(draft.amount),
            interaction_id=draft.interaction_id,
            state=draft.state,
        )


def add_transaction():
    def updater(self, obj, action):
        draft: types.TransactionDraft = getattr(action, "transaction")
        transaction = types.Transaction(
            id=str(uuid.uuid4()),
            timestamp=draft.timestamp,
            type=draft.type,
            amount=utils._money_to_typed(draft.amount),
            interaction_id=draft.interaction_id,
            state=draft.state,
        )
        transaction = schemas.TransactionSchema().dump(transaction)
        if not obj["transactions"]:
            obj["transactions"] = []
        new = copy.deepcopy(obj)
        new["transactions"].append(transaction)
        return new

    return updater


def change_transaction_state():
    def updater(self, obj, action):
        transaction_id = getattr(action, "transaction_id")
        transaction_state = getattr(action, "state")
        for index, transaction in enumerate(obj["transactions"]):
            if transaction["id"] == transaction_id:
                new = copy.deepcopy(obj)
                new["transactions"][index]["state"] = transaction_state.value
                return new
        raise ValueError("Could not find transaction with id %s" % transaction_id)

    return updater


def change_transaction_interaction_id():
    def updater(self, obj, action):
        transaction_id = getattr(action, "transaction_id")
        interaction_id = getattr(action, "interaction_id")
        for index, transaction in enumerate(obj["transactions"]):
            if transaction["id"] == transaction_id:
                new = copy.deepcopy(obj)
                new["transactions"][index]["interactionId"] = interaction_id
                return new
        raise ValueError("Could not find transaction with id %s" % transaction_id)

    return updater


def add_interface_interaction():
    def updater(self, obj, action):
        value = types.CustomFields(fields=getattr(action, "fields"))
        value = schemas.CustomFieldsSchema().dump(value)
        if not obj["interfaceInteractions"]:
            obj["interfaceInteractions"] = []
        if value not in obj["interfaceInteractions"]:
            new = copy.deepcopy(obj)
            new["interfaceInteractions"].append(value)
            return new
        return obj

    return updater


class PaymentsBackend(ServiceBackend):
    service_path = "payments"
    model_class = PaymentsModel
    _schema_draft = schemas.PaymentDraftSchema
    _schema_update = schemas.PaymentUpdateSchema
    _schema_query_response = schemas.PaymentPagedQueryResponseSchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^key=(?P<key>[^/]+)$", "GET", self.get_by_key),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^key=(?P<key>[^/]+)$", "POST", self.update_by_key),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
        ]

    _actions = {
        "addInterfaceInteraction": add_interface_interaction(),
        "changeTransactionInteractionId": change_transaction_interaction_id(),
        "addTransaction": add_transaction(),
        "changeTransactionState": change_transaction_state(),
    }
