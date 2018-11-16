import datetime
import typing
import uuid

from requests_mock import create_response

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.testing import utils
from commercetools.testing.abstract import BaseModel, ServiceBackend


class PaymentsModel(BaseModel):
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

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^key=(?P<key>[^/]+)$", "GET", self.get_by_key),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^key=(?P<key>[^/]+)$", "POST", self.update_by_key),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
        ]

    def query(self, request):
        params = utils.parse_request_params(abstract.AbstractQuerySchema, request)
        results = list(self.model.objects.values())
        if params.get("limit"):
            results = results[: params["limit"]]

        data = {
            "count": len(results),
            "total": len(self.model.objects),
            "offset": 0,
            "results": results,
        }
        content = schemas.PaymentPagedQueryResponseSchema().dumps(data)
        return create_response(request, text=content)

    def create(self, request):
        obj = schemas.PaymentDraftSchema().loads(request.body)
        data = self.model.add(obj)
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
