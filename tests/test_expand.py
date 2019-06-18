from commercetools import types
from tests.test_service_order import get_test_order


def test_unknown_expand_terms(client):
    order = client.orders.create(types.OrderFromCartDraft(order_number="test-order"), expand="nonExisting")

    assert order.id


def test_optional_expanded_terms(client, commercetools_api):
    order = get_test_order()
    commercetools_api.orders.add_existing(order)

    expanded_order = client.orders.get_by_id(order.id, expand="discountCodes[*].discountCode")

    assert expanded_order.id
    assert expanded_order.discount_codes is None


def test_unknown_reference_expand_terms(client, commercetools_api):
    order = get_test_order()
    commercetools_api.orders.add_existing(order)

    expanded_order = client.orders.get_by_id(order.id, expand="shippingInfo.shippingMethod")

    assert expanded_order.id
    assert expanded_order.shipping_info.shipping_method.obj is None


def test_multiple_expand(client, commercetools_api):
    shipping_method = client.shipping_methods.create(
        types.ShippingMethodDraft(
            key="test-shipping-method", name="test shipping method"
        )
    )

    payment = client.payments.create(
        types.PaymentDraft(
            key="test-payment",
            amount_planned=types.Money(cent_amount=2000, currency_code="GBP"),
            payment_method_info=types.PaymentMethodInfo(
                payment_interface="ADYEN", method="mc"
            ),
            transactions=[
                types.TransactionDraft(
                    type=types.TransactionType.CHARGE,
                    amount=types.Money(cent_amount=2000, currency_code="GBP"),
                    state=types.TransactionState.PENDING,
                )
            ],
        )
    )

    order = get_test_order()
    order.shipping_info.shipping_method.id = shipping_method.id
    order.payment_info.payments[0].id = payment.id
    commercetools_api.orders.add_existing(order)

    expanded_order = client.orders.get_by_id(order.id,
                                             expand=["shippingInfo.shippingMethod", "paymentInfo.payments[*]"])

    assert expanded_order.id
    assert expanded_order.shipping_info.shipping_method.obj.id == shipping_method.id
    assert expanded_order.payment_info.payments[0].obj.id == payment.id

    expanded_order = client.orders.get_by_id(order.id, expand=["shippingInfo.shippingMethod"])

    assert expanded_order.id
    assert expanded_order.shipping_info.shipping_method.obj.id == shipping_method.id
    assert expanded_order.payment_info.payments[0].obj is None

    query_results = client.orders.query(expand=["shippingInfo.shippingMethod", "paymentInfo.payments[*]"])

    expanded_order = query_results.results[0]

    assert expanded_order.id
    assert expanded_order.shipping_info.shipping_method.obj.id == shipping_method.id
    assert expanded_order.payment_info.payments[0].obj.id == payment.id
