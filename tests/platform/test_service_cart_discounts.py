from datetime import datetime

import pytest
from freezegun import freeze_time
from requests.exceptions import HTTPError

from commercetools.platform import models
from commercetools.platform.client import Client


def test_cart_discount_with_id(ct_platform_client: Client):
    cart_discount = (
        ct_platform_client.with_project_key("unittest")
        .cart_discounts()
        .post(
            models.CartDiscountDraft(
                name=models.LocalizedString({"en": "test discount"}),
                value=models.CartDiscountValueRelative(permyriad=10),
                cart_predicate="",
                sort_order="",
                requires_discount_code=False,
            )
        )
    )

    assert cart_discount.id

    cart_discount = (
        ct_platform_client.with_project_key("unittest")
        .cart_discounts()
        .with_id(cart_discount.id)
        .get()
    )
    assert cart_discount.id

    with pytest.raises(HTTPError):
        (
            ct_platform_client.with_project_key("unittest")
            .cart_discounts()
            .with_id("invalid")
            .get()
        )


def test_cart_discount_query(ct_platform_client: Client):
    ct_platform_client.with_project_key("unittest").cart_discounts().post(
        models.CartDiscountDraft(
            name=models.LocalizedString({"en:": "test discount"}),
            value=models.CartDiscountValueRelative(permyriad=10),
            cart_predicate="",
            sort_order="",
            requires_discount_code=False,
        )
    )
    ct_platform_client.with_project_key("unittest").cart_discounts().post(
        models.CartDiscountDraft(
            name=models.LocalizedString({"en:": "test discount"}),
            value=models.CartDiscountValueRelative(permyriad=10),
            cart_predicate="",
            sort_order="",
            requires_discount_code=False,
        )
    )

    # single sort query
    result = (
        ct_platform_client.with_project_key("unittest")
        .cart_discounts()
        .get(sort="id asc")
    )
    assert len(result.results) == 2
    assert result.total == 2

    # multiple sort queries
    result = (
        ct_platform_client.with_project_key("unittest")
        .cart_discounts()
        .get(sort=["id asc", "name asc"])
    )
    assert len(result.results) == 2
    assert result.total == 2


def test_cart_discount_update(ct_platform_client: Client):
    cart_discount = (
        ct_platform_client.with_project_key("unittest")
        .cart_discounts()
        .post(
            models.CartDiscountDraft(
                name=models.LocalizedString(en="en-cart_discount"),
                value=models.CartDiscountValueRelative(permyriad=10),
                is_active=True,
                cart_predicate="",
                sort_order="",
                requires_discount_code=False,
            )
        )
    )
    assert cart_discount.is_active is True

    cart_discount = (
        ct_platform_client.with_project_key("unittest")
        .cart_discounts()
        .with_id(cart_discount.id)
        .post(
            models.CartDiscountUpdate(
                version=cart_discount.version,
                actions=[models.CartDiscountChangeIsActiveAction(is_active=False)],
            )
        )
    )

    assert cart_discount.is_active is False


@freeze_time("2021-03-01 12:34:56")
def test_cart_discount_set_valid_from(ct_platform_client: Client):
    cart_discount = (
        ct_platform_client.with_project_key("unittest")
        .cart_discounts()
        .post(
            models.CartDiscountDraft(
                name=models.LocalizedString(en="en-cart_discount"),
                value=models.CartDiscountValueRelative(permyriad=10),
                is_active=True,
                cart_predicate="",
                sort_order="",
                requires_discount_code=False,
            )
        )
    )
    assert cart_discount.id
    assert cart_discount.valid_from is None

    cart_discount = (
        ct_platform_client.with_project_key("unittest")
        .cart_discounts()
        .with_id(cart_discount.id)
        .post(
            models.CartDiscountUpdate(
                version=cart_discount.version,
                actions=[
                    models.CartDiscountSetValidFromAction(valid_from=datetime.now())
                ],
            )
        )
    )

    assert cart_discount.valid_from == datetime.now()


@freeze_time("2021-03-01 12:34:56")
def test_cart_discount_set_valid_until(ct_platform_client: Client):
    cart_discount = (
        ct_platform_client.with_project_key("unittest")
        .cart_discounts()
        .post(
            models.CartDiscountDraft(
                name=models.LocalizedString(en="en-cart_discount"),
                value=models.CartDiscountValueRelative(permyriad=10),
                is_active=True,
                cart_predicate="",
                sort_order="",
                requires_discount_code=False,
            )
        )
    )
    assert cart_discount.id
    assert cart_discount.valid_until is None

    cart_discount = (
        ct_platform_client.with_project_key("unittest")
        .cart_discounts()
        .with_id(cart_discount.id)
        .post(
            models.CartDiscountUpdate(
                version=cart_discount.version,
                actions=[
                    models.CartDiscountSetValidUntilAction(valid_until=datetime.now())
                ],
            )
        )
    )

    assert cart_discount.valid_until == datetime.now()
