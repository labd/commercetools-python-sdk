import pytest
from requests.exceptions import HTTPError

from commercetools import types


def test_cart_discount_get_by_id(client):
    cart_discount = client.cart_discounts.create(
        types.CartDiscountDraft(
            name=types.LocalizedString({"en": "test discount"}),
            value=types.CartDiscountValueRelative(permyriad=10)
        )
    )

    assert cart_discount.id

    cart_discount = client.cart_discounts.get_by_id(cart_discount.id)
    assert cart_discount.id

    with pytest.raises(HTTPError):
        client.cart_discounts.get_by_id("invalid")


def test_cart_discount_query(client):
    client.cart_discounts.create(
        types.CartDiscountDraft(
            name=types.LocalizedString({"en:": "test discount"}),
            value=types.CartDiscountValueRelative(permyriad=10)
        )
    )
    client.cart_discounts.create(
        types.CartDiscountDraft(
            name=types.LocalizedString({"en:": "test discount"}),
            value=types.CartDiscountValueRelative(permyriad=10)
        )
    )

    # single sort query
    result = client.cart_discounts.query(sort="id asc")
    assert len(result.results) == 2
    assert result.total == 2

    # multiple sort queries
    result = client.cart_discounts.query(sort=["id asc", "name asc"])
    assert len(result.results) == 2
    assert result.total == 2


def test_cart_discount_update(client):
    cart_discount = client.cart_discounts.create(
        types.CartDiscountDraft(
            name=types.LocalizedString(en="en-cart_discount"),
            value=types.CartDiscountValueRelative(permyriad=10),
            is_active=True,
        )
    )
    assert cart_discount.is_active is True

    cart_discount = client.cart_discounts.update_by_id(
        id=cart_discount.id,
        version=cart_discount.version,
        actions=[
            types.CartDiscountChangeIsActiveAction(is_active=False)
        ],
    )

    assert cart_discount.is_active is False
