import copy
import datetime
import typing
import uuid

from commercetools.platform import models
from commercetools.platform.models import CartOrigin, OrderState
from commercetools.platform.models._schemas.cart import CartSchema, ShippingInfoSchema
from commercetools.platform.models._schemas.order import (
    DeliverySchema,
    OrderFromCartDraftSchema,
    OrderPagedQueryResponseSchema,
    OrderSchema,
    OrderUpdateSchema,
)
from commercetools.platform.models._schemas.payment import PaymentReferenceSchema
from commercetools.testing.abstract import BaseModel, ServiceBackend
from commercetools.testing.utils import (
    set_custom_field,
    update_attribute,
    update_enum_attribute,
)


class OrdersModel(BaseModel):
    _primary_type_name = "order"
    _resource_schema = OrderSchema

    def _create_from_draft(
        self, draft: models.OrderFromCartDraft, id: typing.Optional[str] = None
    ) -> models.Order:
        """
        Note this implementation needs further refinement. For example:
         - Copying fields from an existing cart
         - Setting custom type fields?
        """

        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        cart_identifier = models.CartResourceIdentifier(id=draft.id)

        cart_data = self._storage.get_by_resource_identifier(cart_identifier)
        cart = None
        if cart_data:
            cart: models.Cart = CartSchema().load(cart_data)

        order = models.Order(
            id=str(object_id),
            version=1,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            last_modified_at=datetime.datetime.now(datetime.timezone.utc),
            line_items=[],
            custom_line_items=[],
            total_price=copy.deepcopy(cart.total_price),
            sync_info=[],
            last_message_sequence_number=0,
            refused_gifts=[],
            order_number=draft.order_number,
            payment_state=draft.payment_state,
            order_state=OrderState.OPEN,
            origin=CartOrigin.CUSTOMER,
        )
        return order


def add_delivery():
    def updater(self, obj, action):
        parcels: typing.List[models.ParcelDraft] = getattr(action, "parcels")
        delivery = models.Delivery(
            id=str(uuid.uuid4()),
            created_at=datetime.datetime.now(datetime.timezone.utc),
            items=[],
            parcels=[
                models.Parcel(
                    id=str(uuid.uuid4()),
                    created_at=datetime.datetime.now(datetime.timezone.utc),
                    measurements=parcel_draft.measurements,
                    tracking_data=parcel_draft.tracking_data,
                    items=parcel_draft.items,
                )
                for parcel_draft in parcels
            ],
        )

        if not obj["shippingInfo"]:
            obj["shippingInfo"] = ShippingInfoSchema().dump(
                models.ShippingInfo(
                    shipping_method_name="dummy",
                    price=models.CentPrecisionMoney(
                        fraction_digits=0, cent_amount=0, currency_code="EUR"
                    ),
                    shipping_rate=models.ShippingRate(
                        price=models.CentPrecisionMoney(
                            fraction_digits=0, cent_amount=0, currency_code="EUR"
                        ),
                        tiers=[],
                    ),
                    shipping_method_state=models.ShippingMethodState(value=None),
                    deliveries=[],
                )
            )
        elif not obj["shippingInfo"].get("deliveries"):
            obj["shippingInfo"]["deliveries"] = []

        value = DeliverySchema().dump(delivery)
        if value not in obj["shippingInfo"]["deliveries"]:
            new = copy.deepcopy(obj)
            new["shippingInfo"]["deliveries"].append(value)
            return new
        return obj

    return updater


def add_payment():
    def updater(self, obj, action):
        obj = copy.deepcopy(obj)
        if "paymentInfo" in obj and obj["paymentInfo"]:
            payments = obj["paymentInfo"]["payments"]
        else:
            payments = []

        payments.append(PaymentReferenceSchema().dump(action.payment))
        obj["paymentInfo"] = {"payments": payments}
        return obj

    return updater


class OrdersBackend(ServiceBackend):
    service_path = "orders"
    model_class = OrdersModel
    _schema_draft = OrderFromCartDraftSchema
    _schema_update = OrderUpdateSchema
    _schema_query_response = OrderPagedQueryResponseSchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^key=(?P<key>[^/]+)$", "GET", self.get_by_key),
            ("^key=(?P<key>[^/]+)$", "POST", self.update_by_key),
            ("^key=(?P<key>[^/]+)$", "DELETE", self.delete_by_key),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
            ("^(?P<id>[^/]+)$", "DELETE", self.delete_by_id),
        ]

    _actions = {
        "changeOrderState": update_enum_attribute("orderState", "order_state"),
        "changePaymentState": update_enum_attribute("paymentState", "payment_state"),
        "changeShipmentState": update_enum_attribute("shipmentState", "shipment_state"),
        "addDelivery": add_delivery(),
        "setShippingAddress": update_attribute("shippingAddress", "address"),
        "setBillingAddress": update_attribute("billingAddress", "address"),
        "setCustomerEmail": update_attribute("customerEmail", "email"),
        "setCustomField": set_custom_field(),
        "addPayment": add_payment(),
    }
