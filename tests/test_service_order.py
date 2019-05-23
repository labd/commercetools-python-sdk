import datetime

from commercetools import types


def test_orders_get_by_id(client):
    order = client.orders.create(types.OrderFromCartDraft(order_number="test-order"))

    assert order.id
    assert order.order_number == "test-order"


def test_orders_query(client):
    results = client.orders.query()
    assert results.total == 0

    client.orders.create(types.OrderFromCartDraft(order_number="test-order"))

    results = client.orders.query()
    assert results.total == 1


def test_orders_delete(commercetools_api, client):
    order = get_test_order()
    commercetools_api.orders.add_existing(order)

    deleted_order = client.orders.delete_by_id(order.id, order.version)
    assert order.id == deleted_order.id


def test_add_existing_order(commercetools_api, client):
    order = get_test_order()
    commercetools_api.orders.add_existing(order)

    assert client.orders.get_by_id(order.id).order_number == order.order_number


def test_update_order_state_action(commercetools_api, client):
    order = get_test_order()

    commercetools_api.orders.add_existing(order)

    updated_order = client.orders.update_by_id(
        order.id,
        order.version,
        actions=[
            types.OrderChangeOrderStateAction(order_state=types.OrderState.CONFIRMED)
        ],
    )

    assert updated_order.order_state == types.OrderState.CONFIRMED


def test_update_order_add_delivery(commercetools_api, client):
    order = get_test_order()

    commercetools_api.orders.add_existing(order)

    updated_order = client.orders.update_by_id(
        order.id,
        order.version,
        actions=[
            types.OrderAddDeliveryAction(
                parcels=[
                    types.ParcelDraft(
                        tracking_data=types.TrackingData(
                            tracking_id="123", carrier="Test Carrier"
                        )
                    )
                ]
            )
        ],
    )

    assert (
        updated_order.shipping_info.deliveries[0].parcels[0].tracking_data.tracking_id
        == "123"
    )


def get_test_order():
    order = types.Order(
        id="20ad6c92-fe04-4983-877e-5f5f80b5e37b",
        version=10,
        created_at=datetime.datetime.now(datetime.timezone.utc),
        last_message_sequence_number=8,
        order_number="test-number",
        customer_email="d.weterings@labdigital.nl",
        anonymous_id="a706a9bf-4cd5-4bd0-b35d-b2373fb0c15e",
        locale="en",
        total_price=types.Money(cent_amount=2000, currency_code="GBP"),
        taxed_price=types.TaxedPrice(
            total_net=types.Money(cent_amount=1666, currency_code="GBP"),
            total_gross=types.Money(cent_amount=2000, currency_code="GBP"),
            tax_portions=[
                types.TaxPortion(
                    rate=0.2,
                    amount=types.Money(cent_amount=334, currency_code="GBP"),
                    name="GB",
                )
            ],
        ),
        country="GB",
        order_state=types.OrderState.OPEN,
        shipment_state=None,
        payment_state=types.PaymentState.PAID,
        shipping_info=types.ShippingInfo(
            shipping_method_name="Shipwire",
            price=types.TypedMoney(
                currency_code="GBP",
                cent_amount=1000,
                type=types.MoneyType.CENT_PRECISION,
                fraction_digits=2,
            ),
            shipping_rate=types.ShippingRate(
                price=types.TypedMoney(
                    currency_code="GBP",
                    cent_amount=1000,
                    type=types.MoneyType.CENT_PRECISION,
                    fraction_digits=2,
                ),
                free_above=types.TypedMoney(
                    currency_code="GBP",
                    cent_amount=5000,
                    type=types.MoneyType.CENT_PRECISION,
                    fraction_digits=2,
                ),
                tiers=[],
            ),
            tax_rate=types.TaxRate(
                name="GB",
                amount=0.2,
                included_in_price=False,
                country="GB",
                id="8olFiIwX",
            ),
            tax_category=types.TaxCategoryReference(
                type_id=types.ReferenceTypeId.TAX_CATEGORY,
                id="5e564356-d367-4718-a0bb-6a17c3b1fdeb",
            ),
            shipping_method=types.ShippingMethodReference(
                id="b0e88c41-8553-4904-a2d5-a096c5f6f09f"
            ),
            taxed_price=types.TaxedItemPrice(
                total_net=types.TypedMoney(
                    cent_amount=833,
                    currency_code="GBP",
                    type=types.MoneyType.CENT_PRECISION,
                    fraction_digits=2,
                ),
                total_gross=types.TypedMoney(
                    cent_amount=1000,
                    currency_code="GBP",
                    type=types.MoneyType.CENT_PRECISION,
                    fraction_digits=2,
                ),
            ),
            shipping_method_state=types.ShippingMethodState.MATCHES_CART,
        ),
        tax_mode=types.TaxMode.PLATFORM,
        tax_rounding_mode=types.RoundingMode.HALF_EVEN,
        tax_calculation_mode=types.TaxCalculationMode.LINE_ITEM_LEVEL,
        origin=types.CartOrigin.CUSTOMER,
        line_items=[
            types.LineItem(
                id="4e7e38f2-45c1-4672-9c41-9c74dbd911bd",
                product_id="b32d3cfd-6920-4788-a5ee-c0bcfd460c0d",
                name=types.LocalizedString({"en": "FRUIT MIX STAGE 1"}),
                product_type=types.ProductTypeReference(
                    id="9faf6335-7618-4f8b-a11d-c0f832b733c1"
                ),
                product_slug=types.LocalizedString({"en": "fruit-mix-stage-1"}),
                variant=types.ProductVariant(
                    id=1,
                    sku="982218931672529",
                    prices=[
                        types.Price(
                            id="fb424988-79b3-4418-8730-9f324025a13c",
                            value=types.Money(cent_amount=1000, currency_code="GBP"),
                        )
                    ],
                ),
                price=types.Price(
                    id="fb424988-79b3-4418-8730-9f324025a13c",
                    value=types.Money(cent_amount=1000, currency_code="GBP"),
                ),
                quantity=1,
                tax_rate=types.TaxRate(
                    name="GB",
                    amount=0.19,
                    included_in_price=False,
                    country="GB",
                    id="7JkeuGwo",
                ),
                state=[
                    types.ItemState(
                        quantity=1,
                        state=types.StateReference(
                            id="0e59473e-1203-4135-8bcb-f1c5141ed5ad"
                        ),
                    )
                ],
                price_mode=types.LineItemPriceMode.PLATFORM,
                total_price=types.Money(cent_amount=1000, currency_code="GBP"),
                taxed_price=types.TaxedItemPrice(
                    total_net=types.TypedMoney(
                        cent_amount=1190,
                        currency_code="GBP",
                        type=types.MoneyType.CENT_PRECISION,
                        fraction_digits=2,
                    ),
                    total_gross=types.TypedMoney(
                        cent_amount=1190,
                        currency_code="GBP",
                        type=types.MoneyType.CENT_PRECISION,
                        fraction_digits=2,
                    ),
                ),
                line_item_mode=types.LineItemMode.STANDARD,
            )
        ],
        cart=types.CartReference(id="some cart id"),
        payment_info=types.PaymentInfo(
            payments=[types.PaymentReference(id="a433f3f8-5e27-406e-b2b0-d4a1f64592c4")]
        ),
        custom=types.CustomFields(
            fields=types.FieldContainer(
                {
                    "sentEmails": ["order_email_confirmed"],
                    "shipwireServiceLevelCode": "GD",
                }
            )
        ),
        shipping_address=types.Address(
            first_name="David",
            last_name="Weterings",
            street_name="Kanaalweg",
            street_number="14",
            postal_code="3526KL",
            city="Utrecht",
            country="GB",
        ),
        billing_address=types.Address(
            first_name="David",
            last_name="Weterings",
            street_name="Kanaalweg",
            street_number="14",
            postal_code="3526KL",
            city="Utrecht",
            country="GB",
        ),
    )
    return order
