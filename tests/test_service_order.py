from commercetools import types
from commercetools.types import OrderState


def test_orders_get_by_id(client):
    order = client.orders.create(types.OrderFromCartDraft(
        order_number="test-order",
    ))

    assert order.id
    assert order.order_number == "test-order"
