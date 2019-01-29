import datetime
import typing
import uuid

from commercetools import schemas, types
from commercetools.testing.abstract import BaseModel, ServiceBackend
from commercetools.types import CartOrigin, OrderState


class OrdersModel(BaseModel):
    _primary_type_name = "order"
    _resource_schema = schemas.OrderSchema

    def _create_from_draft(
        self, draft: types.OrderFromCartDraft, id: typing.Optional[str] = None
    ) -> types.Order:
        """
        Note this implementation needs further refinement. For example:
         - Copying fields from an existing cart
         - Setting custom type fields?
        """

        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        order = types.Order(
            id=str(object_id),
            version=1,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            last_modified_at=datetime.datetime.now(datetime.timezone.utc),
            order_number=draft.order_number,
            payment_state=draft.payment_state,
            order_state=OrderState.OPEN,
            origin=CartOrigin.CUSTOMER,
        )
        return order


class OrdersBackend(ServiceBackend):
    service_path = "orders"
    model_class = OrdersModel
    _schema_draft = schemas.OrderFromCartDraftSchema
    _schema_update = schemas.OrderUpdateSchema
    _schema_query_response = schemas.OrderPagedQueryResponseSchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^key=(?P<key>[^/]+)$", "GET", self.get_by_key),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^key=(?P<key>[^/]+)$", "POST", self.update_by_key),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
        ]
