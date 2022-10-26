import uuid

import pytest

from commercetools.platform import models
from commercetools.platform.client import Client


def test_cart_with_id_get(ct_platform_client: Client, cart_draft):
    cart = ct_platform_client.with_project_key("unittest").carts().post(cart_draft)

    assert cart.id


@pytest.fixture
def cart_draft(ct_platform_client: Client):
    client = ct_platform_client.with_project_key("unittest")
    product_1 = client.products().post(
        models.ProductDraft(
            key="product-1",
            product_type=models.ProductTypeResourceIdentifier(key="dummy"),
            name=models.LocalizedString(en=f"my-product-1"),
            slug=models.LocalizedString(en=f"my-product-1"),
            publish=True,
        )
    )
    product_2 = client.products().post(
        models.ProductDraft(
            key="product-2",
            product_type=models.ProductTypeResourceIdentifier(key="dummy"),
            name=models.LocalizedString(en=f"my-product-2"),
            slug=models.LocalizedString(en=f"my-product-2"),
            publish=True,
        )
    )

    return models.CartDraft(
        customer_id=str(uuid.uuid4()),
        customer_email="foo@example.com",
        currency="GBP",
        anonymous_id=str(uuid.uuid4()),
        country="GB",
        inventory_mode=models.InventoryMode.NONE,
        tax_mode=models.TaxMode.PLATFORM,
        tax_rounding_mode=models.RoundingMode.HALF_EVEN,
        tax_calculation_mode=models.TaxCalculationMode.LINE_ITEM_LEVEL,
        line_items=[
            models.LineItemDraft(product_id=product_1.id, quantity=1),
            models.LineItemDraft(product_id=product_2.id, quantity=2),
        ],
        locale="en",
        origin=models.CartOrigin.CUSTOMER,
    )


def test_update_actions(commercetools_api, ct_platform_client, cart_draft):
    client = ct_platform_client.with_project_key("unittest")
    cart = client.carts().post(cart_draft)

    payment_reference = models.PaymentReference(id=str(uuid.uuid4()))
    cart = (
        client.carts()
        .with_id(cart.id)
        .post(
            models.CartUpdate(
                version=cart.version,
                actions=[models.CartAddPaymentAction(payment=payment_reference)],
            )
        )
    )

    type_draft = models.TypeDraft(
        key="foobar",
        resource_type_ids=[models.ResourceTypeId.ORDER],
        name={"en-US": "test"},
        field_definitions=[
            models.FieldDefinition(
                type=models.CustomFieldStringType(),
                name="foo1",
                label={"en-US": "foo-1"},
                required=False,
            ),
            models.FieldDefinition(
                type=models.CustomFieldSetType(element_type=None),
                name="foo2",
                label={"en-US": "foo-2"},
                required=False,
            ),
            models.FieldDefinition(
                type=models.CustomFieldBooleanType(),
                name="foo3",
                label={"en-US": "foo-3"},
                required=False,
            ),
        ],
    )
    custom_type = client.types().post(type_draft)
    assert custom_type.id

    assert cart.payment_info.payments[0] == payment_reference
    cart = (
        client.carts()
        .with_id(cart.id)
        .post(
            models.CartUpdate(
                version=cart.version,
                actions=[
                    models.CartSetCustomTypeAction(
                        type=models.TypeResourceIdentifier(id=custom_type.id)
                    )
                ],
            )
        )
    )

    cart = (
        client.carts()
        .with_id(cart.id)
        .post(
            models.CartUpdate(
                version=cart.version,
                actions=[
                    models.CartSetCustomFieldAction(name="foo1", value="bar"),
                    models.CartSetCustomFieldAction(name="foo2", value=["bar"]),
                    models.CartSetCustomFieldAction(name="foo3", value=False),
                ],
            )
        )
    )

    cart = client.carts().with_id(cart.id).get()

    assert all(key in cart.custom.fields for key in ["foo1", "foo2", "foo3"])
    assert cart.custom.fields["foo1"] == "bar"
    assert cart.custom.fields["foo2"] == ["bar"]
    assert cart.custom.fields["foo3"] is False
