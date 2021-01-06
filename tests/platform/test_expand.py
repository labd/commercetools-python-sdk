import commercetools
from commercetools.platform import models
from tests.platform.test_service_order import get_test_order


def test_unknown_expand_terms(old_client: commercetools.Client):
    cart = old_client.carts.create(models.CartDraft(currency="EUR"))

    order = old_client.orders.create(
        models.OrderFromCartDraft(id=cart.id, version=1, order_number="test-order"),
        expand="nonExisting",
    )

    assert order.id


def test_optional_expanded_terms(old_client, commercetools_api):
    order = get_test_order()
    commercetools_api.orders.add_existing(order)

    expanded_order = old_client.orders.get_by_id(
        order.id, expand="discountCodes[*].discountCode"
    )

    assert expanded_order.id
    assert expanded_order.discount_codes is None


def test_unknown_reference_expand_terms(old_client, commercetools_api):
    order = get_test_order()
    commercetools_api.orders.add_existing(order)

    expanded_order = old_client.orders.get_by_id(
        order.id, expand="shippingInfo.shippingMethod"
    )

    assert expanded_order.id
    assert expanded_order.shipping_info.shipping_method.obj is None


def test_multiple_expand(old_client, commercetools_api):
    shipping_method = old_client.shipping_methods.create(
        models.ShippingMethodDraft(
            key="test-shipping-method",
            name="test shipping method",
            tax_category=models.TaxCategoryResourceIdentifier(id="dummy"),
            zone_rates=[],
            is_default=False,
        )
    )

    payment = old_client.payments.create(
        models.PaymentDraft(
            key="test-payment",
            amount_planned=models.Money(cent_amount=2000, currency_code="GBP"),
            payment_method_info=models.PaymentMethodInfo(
                payment_interface="ADYEN", method="mc"
            ),
            transactions=[
                models.TransactionDraft(
                    type=models.TransactionType.CHARGE,
                    amount=models.Money(cent_amount=2000, currency_code="GBP"),
                    state=models.TransactionState.PENDING,
                )
            ],
        )
    )

    order = get_test_order()
    order.shipping_info.shipping_method.id = shipping_method.id
    order.payment_info.payments[0].id = payment.id
    commercetools_api.orders.add_existing(order)

    expanded_order = old_client.orders.get_by_id(
        order.id, expand=["shippingInfo.shippingMethod", "paymentInfo.payments[*]"]
    )

    assert expanded_order.id
    assert expanded_order.shipping_info.shipping_method.obj.id == shipping_method.id
    assert expanded_order.payment_info.payments[0].obj.id == payment.id

    expanded_order = old_client.orders.get_by_id(
        order.id, expand=["shippingInfo.shippingMethod"]
    )

    assert expanded_order.id
    assert expanded_order.shipping_info.shipping_method.obj.id == shipping_method.id
    assert expanded_order.payment_info.payments[0].obj is None

    query_results = old_client.orders.query(
        expand=["shippingInfo.shippingMethod", "paymentInfo.payments[*]"]
    )

    expanded_order = query_results.results[0]

    assert expanded_order.id
    assert expanded_order.shipping_info.shipping_method.obj.id == shipping_method.id
    assert expanded_order.payment_info.payments[0].obj.id == payment.id
