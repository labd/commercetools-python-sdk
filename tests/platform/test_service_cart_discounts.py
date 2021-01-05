import pytest
from requests.exceptions import HTTPError

from commercetools.platform import models


def test_cart_discount_get_by_id(old_client):
    cart_discount = old_client.cart_discounts.create(
        models.CartDiscountDraft(
            name=models.LocalizedString({"en": "test discount"}),
            value=models.CartDiscountValueRelative(permyriad=10),
            cart_predicate="",
            sort_order="",
            requires_discount_code=False,
        )
    )

    assert cart_discount.id

    cart_discount = old_client.cart_discounts.get_by_id(cart_discount.id)
    assert cart_discount.id

    with pytest.raises(HTTPError):
        old_client.cart_discounts.get_by_id("invalid")


def test_cart_discount_query(old_client):
    old_client.cart_discounts.create(
        models.CartDiscountDraft(
            name=models.LocalizedString({"en:": "test discount"}),
            value=models.CartDiscountValueRelative(permyriad=10),
            cart_predicate="",
            sort_order="",
            requires_discount_code=False,
        )
    )
    old_client.cart_discounts.create(
        models.CartDiscountDraft(
            name=models.LocalizedString({"en:": "test discount"}),
            value=models.CartDiscountValueRelative(permyriad=10),
            cart_predicate="",
            sort_order="",
            requires_discount_code=False,
        )
    )

    # single sort query
    result = old_client.cart_discounts.query(sort="id asc")
    assert len(result.results) == 2
    assert result.total == 2

    # multiple sort queries
    result = old_client.cart_discounts.query(sort=["id asc", "name asc"])
    assert len(result.results) == 2
    assert result.total == 2


def test_cart_discount_update(old_client):
    cart_discount = old_client.cart_discounts.create(
        models.CartDiscountDraft(
            name=models.LocalizedString(en="en-cart_discount"),
            value=models.CartDiscountValueRelative(permyriad=10),
            is_active=True,
            cart_predicate="",
            sort_order="",
            requires_discount_code=False,
        )
    )
    assert cart_discount.is_active is True

    cart_discount = old_client.cart_discounts.update_by_id(
        id=cart_discount.id,
        version=cart_discount.version,
        actions=[models.CartDiscountChangeIsActiveAction(is_active=False)],
    )

    assert cart_discount.is_active is False
