from commercetools import types


def test_payments_get_by_id(client):
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
                    interaction_id="8525483242578266",
                    state=types.TransactionState.SUCCESS,
                )
            ],
            interface_interactions=[
                types.CustomFieldsDraft(
                    fields=types.FieldContainer(
                        {
                            "operations": "CANCEL,CAPTURE,REFUND",
                            "success": True,
                            "psp_reference": "8525483242578266",
                            "merchant_reference": "some reference",
                            "reason": "82132:0005:10/2020",
                            "amount": 2000,
                            "payment_method": "mc",
                            "event_date": "2019-01-24T11:04:17.000000Z",
                            "currency_code": "GBP",
                            "event_code": "AUTHORISATION",
                            "merchant_account_code": "TestMerchant",
                        }
                    )
                )
            ],
        )
    )

    assert payment.id
    assert payment.key == "test-payment"


def test_update_actions(client):
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

    existing_transaction = payment.transactions[0]

    payment = client.payments.update_by_id(
        payment.id,
        payment.version,
        actions=[
            types.PaymentAddInterfaceInteractionAction(
                fields=types.FieldContainer({"pspRef": "1337"})
            ),
            types.PaymentChangeTransactionInteractionIdAction(
                transaction_id=existing_transaction.id, interaction_id="1337"
            ),
            types.PaymentAddTransactionAction(
                transaction=types.TransactionDraft(
                    type=types.TransactionType.CHARGE,
                    amount=types.Money(currency_code="GBP", cent_amount=1000),
                    interaction_id="123",
                    state=types.TransactionState.INITIAL,
                )
            ),
            types.PaymentChangeTransactionStateAction(
                transaction_id=existing_transaction.id,
                state=types.TransactionState.SUCCESS,
            ),
        ],
    )

    assert payment.interface_interactions[0].fields == {"pspRef": "1337"}
    assert payment.transactions[0].interaction_id == "1337"
    assert len(payment.transactions) == 2
    assert payment.transactions[0].state == types.TransactionState.SUCCESS
