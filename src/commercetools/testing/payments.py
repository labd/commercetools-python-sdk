import datetime
import typing
import uuid

from commercetools import schemas, types
from commercetools.testing import utils
from commercetools.testing.abstract import BaseModel, ServiceBackend


class PaymentsModel(BaseModel):
    _primary_type_name = "payment"
    _resource_schema = schemas.PaymentSchema

    def _create_from_draft(
        self, obj: types.PaymentDraft, id: typing.Optional[str] = None
    ) -> types.Payment:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        payment = types.Payment(
            id=str(object_id),
            key=obj.key,
            version=1,
            created_at=datetime.datetime.now(),
            last_modified_at=datetime.datetime.now(),
            customer=obj.customer,
            amount_authorized=obj.amount_authorized,
            amount_paid=obj.amount_paid,
            amount_planned=obj.amount_planned,
            amount_refunded=obj.amount_refunded,
            anonymous_id=obj.anonymous_id,
            payment_method_info=obj.payment_method_info,
            payment_status=obj.payment_status,
            transactions=[
                self._create_transaction_draft(transaction)
                for transaction in obj.transactions or []
            ],
            custom=utils.create_from_draft(obj.custom),
        )
        return payment

    def _create_transaction_draft(
        self, obj: types.TransactionDraft
    ) -> types.Transaction:
        return types.Transaction(
            id=str(uuid.uuid4()),
            timestamp=obj.timestamp,
            type=obj.type,
            amount=obj.amount,
            interaction_id=obj.interaction_id,
            state=obj.state,
        )


class PaymentsBackend(ServiceBackend):
    service_path = "payments"
    model_class = PaymentsModel
    _schema_draft = schemas.PaymentDraftSchema
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
