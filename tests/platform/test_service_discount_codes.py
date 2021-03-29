from datetime import datetime

import pytest
from freezegun import freeze_time
from requests.exceptions import HTTPError

from commercetools.platform import models


def test_discount_code_get_by_id(old_client):
    discount_code = old_client.discount_codes.create(
        models.DiscountCodeDraft(
            name=models.LocalizedString({"en": "test discount"}),
            code="1337",
            cart_discounts=[],
        )
    )

    assert discount_code.id
    assert discount_code.code == "1337"

    discount_code = old_client.discount_codes.get_by_id(discount_code.id)
    assert discount_code.id
    assert discount_code.code == "1337"

    with pytest.raises(HTTPError):
        old_client.discount_codes.get_by_id("invalid")


def test_discount_code_query(old_client):
    old_client.discount_codes.create(
        models.DiscountCodeDraft(
            name=models.LocalizedString({"en:": "test discount"}),
            code="1337",
            cart_discounts=[],
        )
    )
    old_client.discount_codes.create(
        models.DiscountCodeDraft(
            name=models.LocalizedString({"en:": "test discount"}),
            code="1338",
            cart_discounts=[],
        )
    )

    # single sort query
    result = old_client.discount_codes.query(sort="id asc")
    assert len(result.results) == 2
    assert result.total == 2

    # multiple sort queries
    result = old_client.discount_codes.query(sort=["id asc", "name asc"])
    assert len(result.results) == 2
    assert result.total == 2


def test_discount_code_update(old_client):
    discount_code = old_client.discount_codes.create(
        models.DiscountCodeDraft(
            name=models.LocalizedString(en="en-discount_code"),
            code="1337",
            is_active=True,
            cart_discounts=[],
        )
    )
    assert discount_code.code == "1337"

    discount_code = old_client.discount_codes.update_by_id(
        id=discount_code.id,
        version=discount_code.version,
        actions=[models.DiscountCodeChangeIsActiveAction(is_active=False)],
    )

    assert discount_code.is_active is False


def test_discount_code_delete(old_client):
    discount_code = old_client.discount_codes.create(
        models.DiscountCodeDraft(
            name=models.LocalizedString(en="en-discount_code"),
            code="1337",
            is_active=True,
            cart_discounts=[],
        )
    )
    assert discount_code.code == "1337"

    discount_code = old_client.discount_codes.delete_by_id(
        id=discount_code.id,
        version=discount_code.version,
    )

    assert discount_code.code == "1337"

    result = old_client.discount_codes.query()
    assert len(result.results) == 0


@freeze_time("2021-03-01 12:34:56")
def test_discount_code_set_valid_from(old_client):
    discount_code = old_client.discount_codes.create(
        models.DiscountCodeDraft(
            name=models.LocalizedString(en="en-discount_code"),
            code="1337",
            is_active=True,
            cart_discounts=[],
        )
    )
    assert discount_code.id
    assert discount_code.valid_from is None

    discount_code = old_client.discount_codes.update_by_id(
        id=discount_code.id,
        version=discount_code.version,
        actions=[models.DiscountCodeSetValidFromAction(valid_from=datetime.now())],
    )

    assert discount_code.valid_from == datetime.now()


@freeze_time("2021-03-01 12:34:56")
def test_discount_code_set_valid_until(old_client):
    discount_code = old_client.discount_codes.create(
        models.DiscountCodeDraft(
            name=models.LocalizedString(en="en-discount_code"),
            code="1337",
            is_active=True,
            cart_discounts=[],
        )
    )
    assert discount_code.id
    assert discount_code.valid_until is None

    discount_code = old_client.discount_codes.update_by_id(
        id=discount_code.id,
        version=discount_code.version,
        actions=[models.DiscountCodeSetValidUntilAction(valid_until=datetime.now())],
    )

    assert discount_code.version == 2
    assert discount_code.valid_until == datetime.now()


def test_discount_code_change_cart_discounts(old_client):
    discount_code = old_client.discount_codes.create(
        models.DiscountCodeDraft(
            name=models.LocalizedString(en="en-discount_code"),
            code="1337",
            is_active=True,
            cart_discounts=[],
        )
    )
    assert discount_code.id
    assert discount_code.cart_discounts == []

    cart_discount = old_client.cart_discounts.create(
        models.CartDiscountDraft(
            name=models.LocalizedString(en="cart-discount-test"),
            value=models.CartDiscountValueDraft(type="absolute"),
            cart_predicate="sku",
            sort_order="1",
            requires_discount_code=True,
        )
    )
    assert cart_discount.id

    discount_code = old_client.discount_codes.update_by_id(
        id=discount_code.id,
        version=discount_code.version,
        actions=[
            models.DiscountCodeChangeCartDiscountsAction(
                cart_discounts=[
                    models.CartDiscountResourceIdentifier(id=cart_discount.id)
                ]
            )
        ],
    )

    assert discount_code.version == 2
    assert discount_code.cart_discounts == [
        models.CartDiscountReference(id=cart_discount.id)
    ]
