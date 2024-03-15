import datetime

from commercetools.platform import models


def test_orders_get_by_id(old_client):
    cart = old_client.carts.create(models.CartDraft(currency="EUR"))
    order = old_client.orders.create(
        models.OrderFromCartDraft(
            id=cart.id, cart=cart, version=1, order_number="test-order"
        )
    )

    assert order.id
    assert order.order_number == "test-order"


def test_orders_query(old_client):
    results = old_client.orders.query()
    assert results.total == 0

    cart = old_client.carts.create(models.CartDraft(currency="EUR"))
    order = old_client.orders.create(
        models.OrderFromCartDraft(
            id=cart.id, cart=cart, version=1, order_number="test-order"
        )
    )

    results = old_client.orders.query()
    assert results.total == 1


def test_orders_query_filter(commercetools_api, old_client):
    order = get_test_order()
    commercetools_api.orders.add_existing(order)
    where = [
        'custom(fields(shipwireServiceLevelCode="GD"))',
        'createdAt >= "2019-10-15T14:12:36.464465"',
    ]

    results = old_client.orders.query(where=where)
    assert results.total == 1


def test_orders_delete(commercetools_api, old_client):
    order = get_test_order()
    commercetools_api.orders.add_existing(order)

    deleted_order = old_client.orders.delete_by_id(order.id, order.version)
    assert order.id == deleted_order.id


def test_add_existing_order(commercetools_api, old_client):
    order = get_test_order()
    commercetools_api.orders.add_existing(order)

    assert old_client.orders.get_by_id(order.id).order_number == order.order_number


def test_update_order_state_action(commercetools_api, old_client):
    order = get_test_order()

    commercetools_api.orders.add_existing(order)

    updated_order = old_client.orders.update_by_id(
        order.id,
        order.version,
        actions=[
            models.OrderChangeOrderStateAction(order_state=models.OrderState.CONFIRMED)
        ],
    )

    assert updated_order.order_state == models.OrderState.CONFIRMED


def test_update_payment_state_action(commercetools_api, old_client):
    order = get_test_order()
    order.payment_state = None

    commercetools_api.orders.add_existing(order)

    updated_order = old_client.orders.update_by_id(
        order.id,
        order.version,
        actions=[
            models.OrderChangePaymentStateAction(payment_state=models.PaymentState.PAID)
        ],
    )

    assert updated_order.payment_state == models.PaymentState.PAID


def test_update_order_add_delivery(commercetools_api, old_client):
    order = get_test_order()

    commercetools_api.orders.add_existing(order)

    updated_order = old_client.orders.update_by_id(
        order.id,
        order.version,
        actions=[
            models.OrderSetBillingAddressAction(address=models.Address(country="NL")),
            models.OrderAddDeliveryAction(
                parcels=[
                    models.ParcelDraft(
                        tracking_data=models.TrackingData(
                            tracking_id="123", carrier="Test Carrier"
                        )
                    )
                ]
            ),
        ],
    )

    assert (
        updated_order.shipping_info.deliveries[0].parcels[0].tracking_data.tracking_id
        == "123"
    )


def get_test_order():
    order = models.Order(
        id="20ad6c92-fe04-4983-877e-5f5f80b5e37b",
        version=10,
        created_at=datetime.datetime.now(datetime.timezone.utc),
        last_modified_at=datetime.datetime.now(datetime.timezone.utc),
        last_message_sequence_number=8,
        order_number="test-number",
        customer_email="d.weterings@labdigital.nl",
        anonymous_id="a706a9bf-4cd5-4bd0-b35d-b2373fb0c15e",
        locale="en",
        total_price=models.CentPrecisionMoney(
            cent_amount=2000, currency_code="GBP", fraction_digits=2
        ),
        taxed_price=models.TaxedPrice(
            total_net=models.CentPrecisionMoney(
                cent_amount=1666, currency_code="GBP", fraction_digits=2
            ),
            total_gross=models.CentPrecisionMoney(
                cent_amount=2000, currency_code="GBP", fraction_digits=2
            ),
            tax_portions=[
                models.TaxPortion(
                    rate=0.2,
                    amount=models.CentPrecisionMoney(
                        cent_amount=334, currency_code="GBP", fraction_digits=2
                    ),
                    name="GB",
                )
            ],
        ),
        country="GB",
        order_state=models.OrderState.OPEN,
        shipment_state=None,
        payment_state=models.PaymentState.PAID,
        shipping_info=models.ShippingInfo(
            shipping_method_name="Shipwire",
            price=models.CentPrecisionMoney(
                currency_code="GBP", cent_amount=1000, fraction_digits=2
            ),
            shipping_rate=models.ShippingRate(
                price=models.CentPrecisionMoney(
                    currency_code="GBP", cent_amount=1000, fraction_digits=2
                ),
                free_above=models.CentPrecisionMoney(
                    currency_code="GBP", cent_amount=5000, fraction_digits=2
                ),
                tiers=[],
            ),
            tax_rate=models.TaxRate(
                name="GB",
                amount=0.2,
                included_in_price=False,
                country="GB",
                id="8olFiIwX",
            ),
            tax_category=models.TaxCategoryReference(
                id="5e564356-d367-4718-a0bb-6a17c3b1fdeb"
            ),
            shipping_method=models.ShippingMethodReference(
                id="b0e88c41-8553-4904-a2d5-a096c5f6f09f"
            ),
            taxed_price=models.TaxedItemPrice(
                total_net=models.CentPrecisionMoney(
                    cent_amount=833, currency_code="GBP", fraction_digits=2
                ),
                total_gross=models.CentPrecisionMoney(
                    cent_amount=1000, currency_code="GBP", fraction_digits=2
                ),
                tax_portions=[]
            ),
            shipping_method_state=models.ShippingMethodState.MATCHES_CART,
        ),
        tax_mode=models.TaxMode.PLATFORM,
        tax_rounding_mode=models.RoundingMode.HALF_EVEN,
        tax_calculation_mode=models.TaxCalculationMode.LINE_ITEM_LEVEL,
        origin=models.CartOrigin.CUSTOMER,
        line_items=[
            models.LineItem(
                id="4e7e38f2-45c1-4672-9c41-9c74dbd911bd",
                product_id="b32d3cfd-6920-4788-a5ee-c0bcfd460c0d",
                name=models.LocalizedString({"en": "FRUIT MIX STAGE 1"}),
                product_type=models.ProductTypeReference(
                    id="9faf6335-7618-4f8b-a11d-c0f832b733c1"
                ),
                product_slug=models.LocalizedString({"en": "fruit-mix-stage-1"}),
                variant=models.ProductVariant(
                    id=1,
                    sku="982218931672529",
                    prices=[
                        models.Price(
                            id="fb424988-79b3-4418-8730-9f324025a13c",
                            value=models.CentPrecisionMoney(
                                cent_amount=1000, currency_code="GBP", fraction_digits=2
                            ),
                        )
                    ],
                ),
                price=models.Price(
                    id="fb424988-79b3-4418-8730-9f324025a13c",
                    value=models.CentPrecisionMoney(
                        cent_amount=1000, currency_code="GBP", fraction_digits=2
                    ),
                ),
                quantity=1,
                tax_rate=models.TaxRate(
                    name="GB",
                    amount=0.19,
                    included_in_price=False,
                    country="GB",
                    id="7JkeuGwo",
                ),
                taxed_price_portions=[],
                per_method_tax_rate=[],
                state=[
                    models.ItemState(
                        quantity=1,
                        state=models.StateReference(
                            id="0e59473e-1203-4135-8bcb-f1c5141ed5ad"
                        ),
                    )
                ],
                discounted_price_per_quantity=[],
                price_mode=models.LineItemPriceMode.PLATFORM,
                total_price=models.CentPrecisionMoney(
                    cent_amount=1000, currency_code="GBP", fraction_digits=2
                ),
                taxed_price=models.TaxedItemPrice(
                    total_net=models.CentPrecisionMoney(
                        cent_amount=1190, currency_code="GBP", fraction_digits=2
                    ),
                    total_gross=models.CentPrecisionMoney(
                        cent_amount=1190, currency_code="GBP", fraction_digits=2
                    ),
                    tax_portions=[]
                ),
                line_item_mode=models.LineItemMode.STANDARD,
            )
        ],
        custom_line_items=[],
        cart=models.CartReference(id="some cart id"),
        payment_info=models.PaymentInfo(
            payments=[
                models.PaymentReference(id="a433f3f8-5e27-406e-b2b0-d4a1f64592c4")
            ]
        ),
        custom=models.CustomFields(
            type=models.TypeReference(id="dummy"),
            fields=models.FieldContainer(
                {
                    "sentEmails": ["order_email_confirmed"],
                    "shipwireServiceLevelCode": "GD",
                }
            ),
        ),
        shipping=[],
        shipping_mode=models.ShippingMode.SINGLE,
        shipping_address=models.Address(
            first_name="David",
            last_name="Weterings",
            street_name="Kanaalweg",
            street_number="14",
            postal_code="3526KL",
            city="Utrecht",
            country="GB",
        ),
        billing_address=models.Address(
            first_name="David",
            last_name="Weterings",
            street_name="Kanaalweg",
            street_number="14",
            postal_code="3526KL",
            city="Utrecht",
            country="GB",
        ),
        sync_info=[],
        refused_gifts=[],
    )
    return order


def test_where_query_state(commercetools_api, old_client):
    order = get_test_order()
    commercetools_api.orders.add_existing(order)

    result = old_client.orders.query(where='orderState in ("Open")')

    assert result.results[0].id == order.id


def test_error_handling():
    data = {
        "statusCode": 400,
        "message": "The value '-1' is not valid for field 'quantity'. Negative quantity is not allowed.",
        "errors": [
            {
                "code": "InvalidField",
                "message": "The value '-1' is not valid for field 'quantity'. Negative quantity is not allowed.",
                "action": {
                    "action": "addDelivery",
                    "items": [
                        {"id": "7920d15b-9444-4555-aa17-e11b4d6316a6", "quantity": -1},
                        {"id": "073b6814-b08f-4753-aa05-7baabba2aa3d", "quantity": -1},
                        {"id": "4830dcf5-bdf8-4ada-a1d0-9c525a8a2292", "quantity": -1},
                    ],
                    "parcels": [
                        {
                            "trackingData": {
                                "trackingId": "not a shipment!",
                                "isReturn": False,
                            },
                            "items": [],
                        }
                    ],
                },
                "actionIndex": 4,
                "invalidValue": -1,
                "field": "quantity",
            },
            {
                "code": "InvalidField",
                "message": "The value '-1' is not valid for field 'quantity'. Negative quantity is not allowed.",
                "action": {
                    "action": "addDelivery",
                    "items": [
                        {"id": "7920d15b-9444-4555-aa17-e11b4d6316a6", "quantity": -1},
                        {"id": "073b6814-b08f-4753-aa05-7baabba2aa3d", "quantity": -1},
                        {"id": "4830dcf5-bdf8-4ada-a1d0-9c525a8a2292", "quantity": -1},
                    ],
                    "parcels": [
                        {
                            "trackingData": {
                                "trackingId": "not a shipment!",
                                "isReturn": False,
                            },
                            "items": [],
                        }
                    ],
                },
                "actionIndex": 4,
                "invalidValue": -1,
                "field": "quantity",
            },
            {
                "code": "InvalidField",
                "message": "The value '-1' is not valid for field 'quantity'. Negative quantity is not allowed.",
                "action": {
                    "action": "addDelivery",
                    "items": [
                        {"id": "7920d15b-9444-4555-aa17-e11b4d6316a6", "quantity": -1},
                        {"id": "073b6814-b08f-4753-aa05-7baabba2aa3d", "quantity": -1},
                        {"id": "4830dcf5-bdf8-4ada-a1d0-9c525a8a2292", "quantity": -1},
                    ],
                    "parcels": [
                        {
                            "trackingData": {
                                "trackingId": "not a shipment!",
                                "isReturn": False,
                            },
                            "items": [],
                        }
                    ],
                },
                "actionIndex": 4,
                "invalidValue": -1,
                "field": "quantity",
            },
        ],
    }
