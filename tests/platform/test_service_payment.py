from commercetools.platform import models
from commercetools.platform.client import Client


def test_payments_with_id_get(ct_platform_client: Client):
    custom_type = (
        ct_platform_client.with_project_key("unittest")
        .types()
        .post(
            models.TypeDraft(
                name=models.LocalizedString(en="myType"),
                key="payment-info",
                resource_type_ids=[models.ResourceTypeId.PAYMENT_INTERFACE_INTERACTION],
                field_definitions=[
                    models.FieldDefinition(
                        type=models.CustomFieldStringType(),
                        name="operations",
                        label=models.LocalizedString(en="Operation"),
                        required=False,
                    )
                ],
            )
        )
    )

    payment = (
        ct_platform_client.with_project_key("unittest")
        .payments()
        .post(
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
                        interaction_id="8525483242578266",
                        state=models.TransactionState.SUCCESS,
                    )
                ],
                interface_interactions=[
                    models.CustomFieldsDraft(
                        type=models.TypeResourceIdentifier(id=custom_type.id),
                        fields=models.FieldContainer(
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
                        ),
                    )
                ],
            )
        )
    )
    assert payment
    assert payment.id
    assert payment.key == "test-payment"


def test_update_actions(ct_platform_client: Client):
    custom_type = (
        ct_platform_client.with_project_key("unittest")
        .types()
        .post(
            models.TypeDraft(
                name=models.LocalizedString(en="myType"),
                key="payment-info",
                resource_type_ids=[models.ResourceTypeId.PAYMENT_INTERFACE_INTERACTION],
                field_definitions=[
                    models.FieldDefinition(
                        type=models.CustomFieldStringType(),
                        name="operations",
                        label=models.LocalizedString(en="Operation"),
                        required=False,
                    )
                ],
            )
        )
    )

    payment = (
        ct_platform_client.with_project_key("unittest")
        .payments()
        .post(
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
    )

    existing_transaction = payment.transactions[0]

    payment = (
        ct_platform_client.with_project_key("unittest")
        .payments()
        .with_id(payment.id)
        .post(
            models.PaymentUpdate(
                version=payment.version,
                actions=[
                    models.PaymentAddInterfaceInteractionAction(
                        type=models.TypeResourceIdentifier(id=custom_type.id),
                        fields=models.FieldContainer({"pspRef": "1337"}),
                    ),
                    models.PaymentChangeTransactionInteractionIdAction(
                        transaction_id=existing_transaction.id, interaction_id="1337"
                    ),
                    models.PaymentAddTransactionAction(
                        transaction=models.TransactionDraft(
                            type=models.TransactionType.CHARGE,
                            amount=models.Money(currency_code="GBP", cent_amount=1000),
                            interaction_id="123",
                            state=models.TransactionState.INITIAL,
                        )
                    ),
                    models.PaymentChangeTransactionStateAction(
                        transaction_id=existing_transaction.id,
                        state=models.TransactionState.SUCCESS,
                    ),
                ],
            )
        )
    )

    assert payment.interface_interactions[0].fields == {"pspRef": "1337"}
    assert payment.transactions[0].interaction_id == "1337"
    assert len(payment.transactions) == 2
    assert payment.transactions[0].state == models.TransactionState.SUCCESS
