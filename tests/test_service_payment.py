from commercetools import types


def test_payments_get_by_id(client):
    payment = client.payments.create(types.PaymentDraft(key="test-payment"))

    assert payment.id
    assert payment.key == "test-payment"
