import uuid

import pytest

from commercetools import types


def test_cart_get_by_id(client, cart_draft):
    cart = client.carts.create(cart_draft)

    assert cart.id


@pytest.fixture
def cart_draft(client):
    product_1 = client.products.create(
        types.ProductDraft(
            key=f"product-1",
            product_type=types.ProductTypeResourceIdentifier(key="dummy"),
            name=types.LocalizedString(en=f"my-product-1"),
            slug=types.LocalizedString(en=f"my-product-1"),
            publish=True,
        )
    )
    product_2 = client.products.create(
        types.ProductDraft(
            key=f"product-2",
            product_type=types.ProductTypeResourceIdentifier(key="dummy"),
            name=types.LocalizedString(en=f"my-product-2"),
            slug=types.LocalizedString(en=f"my-product-2"),
            publish=True,
        )
    )

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
            types.LineItemDraft(product_id=product_1.id, quantity=1),
            types.LineItemDraft(product_id=product_2.id, quantity=2),
        ],
        locale="en",
        origin=types.CartOrigin.CUSTOMER,
    )


def test_update_actions(commercetools_api, client, cart_draft):
    cart = client.carts.create(cart_draft)
    payment_reference = types.PaymentReference(id=str(uuid.uuid4()))
    cart = client.carts.update_by_id(
        cart.id,
        cart.version,
        actions=[types.CartAddPaymentAction(payment=payment_reference)],
    )

    type_draft = types.TypeDraft(
        key="foobar",
        resource_type_ids=[types.ResourceTypeId.ORDER],
        name={"en-US": "test"},
        field_definitions=[
            types.FieldDefinition(
                type=types.CustomFieldStringType(),
                name="foo1",
                label={"en-US": "foo-1"},
                required=False,
            ),
            types.FieldDefinition(
                type=types.CustomFieldSetType(element_type=None),
                name="foo2",
                label={"en-US": "foo-2"},
                required=False,
            ),
            types.FieldDefinition(
                type=types.CustomFieldBooleanType(),
                name="foo3",
                label={"en-US": "foo-3"},
                required=False,
            ),
        ],
    )
    custom_type = client.types.create(type_draft)
    assert custom_type.id

    assert cart.payment_info.payments[0] == payment_reference
    cart = client.carts.update_by_id(
        cart.id,
        cart.version,
        actions=[
            types.CartSetCustomTypeAction(
                type=types.TypeResourceIdentifier(id=custom_type.id)
            )
        ],
    )

    client.carts.update_by_id(
        cart.id,
        cart.version,
        actions=[
            types.CartSetCustomFieldAction(name="foo1", value="bar"),
            types.CartSetCustomFieldAction(name="foo2", value=["bar"]),
            types.CartSetCustomFieldAction(name="foo3", value=False),
        ],
    )

    cart = client.carts.get_by_id(cart.id)

    assert all(key in cart.custom.fields for key in ["foo1", "foo2", "foo3"])
    assert cart.custom.fields["foo1"] == "bar"
    assert cart.custom.fields["foo2"] == ["bar"]
    assert cart.custom.fields["foo3"] is False
