import datetime
import uuid

from requests_mock import create_response

from commercetools import abstract, schemas, types
from commercetools.testing.abstract import BaseModel, ServiceBackend


class PaymentsModel(BaseModel):
    def add(self, id, obj):
        obj = self.convert_payment_draft(obj)
        self.objects[obj.id] = obj
        return obj

    def convert_payment_draft(self, obj: types.PaymentDraft) -> types.Payment:
        payment = types.Payment(
            id=str(uuid.uuid4()),
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
                self.convert_transaction_draft(transaction)
                for transaction in obj.transactions or []
            ],
        )
        return payment

    def convert_transaction_draft(
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

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^key=(?P<key>[^/]+)$", "GET", self.get_by_key),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^key=(?P<key>[^/]+)$", "POST", self.update_by_key),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
        ]

    @property
    def path_prefix(self):
        return r"/(?P<project>[^/]+)/payments/?(?P<path>.*)?"

    def query(self, request):
        obj = abstract.AbstractQuerySchema().load(request.qs)
        data = {
            "count": len(self.model.objects),
            "total": len(self.model.objects),
            "offset": 0,
            "results": self.model.objects.values(),
        }
        content = schemas.PaymentPagedQueryResponseSchema().dumps(data)
        return create_response(request, text=content)

    def create(self, request):
        obj = schemas.PaymentDraftSchema().loads(request.body)
        data = self.model.add(id, obj)
        content = schemas.PaymentSchema().dumps(data)
        return create_response(request, text=content)

    def get_by_id(self, request, id):
        obj = self.model.get_by_id(id)
        if obj:
            content = schemas.PaymentSchema().dumps(obj)
            return create_response(request, text=content)
        return create_response(request, status_code=404)

    def get_by_key(self, request, key):
        obj = self.model.get_by_key(key)
        if obj:
            content = schemas.PaymentSchema().dumps(obj)
            return create_response(request, text=content)
        return create_response(request, status_code=404)

    def update_by_id(self, request, id):
        obj = self.model.get_by_id(id)
        if obj:
            schemas.PaymentSchema().loads(request.body)
            content = schemas.PaymentSchema().dumps(obj)
            return create_response(request, text=content)
        return create_response(request, status_code=404)

    def update_by_key(self, request, key):
        obj = self.model.get_by_key(key)
        if obj:
            schemas.PaymentSchema().loads(request.body)
            content = schemas.PaymentSchema().dumps(obj)
            return create_response(request, text=content)
        return create_response(request, status_code=404)
