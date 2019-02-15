import uuid

import pytest

from commercetools import types


def test_cart_get_by_id(client, cart_draft):
    cart = client.carts.create(cart_draft)

    assert cart.id


@pytest.fixture
def cart_draft():
    return types.CartDraft(
        customer_id=str(uuid.uuid4()),
        customer_email="foo@example.com",
        currency="GBP",
        anonymous_id=str(uuid.uuid4()),
        country="GB",
        inventory_mode=types.InventoryMode.NONE,
        tax_mode=types.TaxMode.PLATFORM,
        tax_rounding_mode=types.RoundingMode.HALF_EVEN,
        tax_calculation_mode=types.TaxCalculationMode.LINE_ITEM_LEVEL,
        line_items=[
            types.LineItemDraft(sku="123", quantity=2),
            types.LineItemDraft(sku="124", quantity=1),
        ],
        locale="en",
        origin=types.CartOrigin.CUSTOMER,
    )


def test_update_actions(commercetools_api, client, cart_draft):
    cart = client.carts.create(cart_draft)
    payment_reference = types.PaymentReference(
        type_id=types.ReferenceTypeId.PAYMENT, id=str(uuid.uuid4())
    )
    updated_cart = client.carts.update_by_id(
        cart.id,
        cart.version,
        actions=[types.CartAddPaymentAction(payment=payment_reference)],
    )

    assert updated_cart.payment_info.payments[0] == payment_reference
