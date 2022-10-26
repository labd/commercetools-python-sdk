from datetime import datetime

import pytest
from freezegun import freeze_time
from requests.exceptions import HTTPError

from commercetools.platform import models
from commercetools.platform.client import Client


def test_discount_code_with_id_get(ct_platform_client: Client):
    discount_code = (
        ct_platform_client.with_project_key("unittest")
        .discount_codes()
        .post(
            models.DiscountCodeDraft(
                name=models.LocalizedString({"en": "test discount"}),
                code="1337",
                cart_discounts=[],
            )
        )
    )

    assert discount_code
    assert discount_code.id
    assert discount_code.code == "1337"

    discount_code = (
        ct_platform_client.with_project_key("unittest")
        .discount_codes()
        .with_id(discount_code.id)
        .get()
    )
    assert discount_code
    assert discount_code.id
    assert discount_code.code == "1337"

    with pytest.raises(HTTPError):
        ct_platform_client.with_project_key("unittest").discount_codes().with_id(
            "invalid"
        ).get()


def test_discount_code_query(ct_platform_client: Client):
    ct_platform_client.with_project_key("unittest").discount_codes().post(
        models.DiscountCodeDraft(
            name=models.LocalizedString({"en:": "test discount"}),
            code="1337",
            cart_discounts=[],
        )
    )
    ct_platform_client.with_project_key("unittest").discount_codes().post(
        models.DiscountCodeDraft(
            name=models.LocalizedString({"en:": "test discount"}),
            code="1338",
            cart_discounts=[],
        )
    )

    # single sort query
    result = (
        ct_platform_client.with_project_key("unittest")
        .discount_codes()
        .get(sort="id asc")
    )
    assert result
    assert len(result.results) == 2
    assert result.total == 2

    # multiple sort queries
    result = (
        ct_platform_client.with_project_key("unittest")
        .discount_codes()
        .get(sort=["id asc", "name asc"])
    )
    assert result
    assert len(result.results) == 2
    assert result.total == 2


def test_discount_code_update(ct_platform_client: Client):
    discount_code = (
        ct_platform_client.with_project_key("unittest")
        .discount_codes()
        .post(
            models.DiscountCodeDraft(
                name=models.LocalizedString(en="en-discount_code"),
                code="1337",
                is_active=True,
                cart_discounts=[],
            )
        )
    )
    assert discount_code.code == "1337"

    discount_code = (
        ct_platform_client.with_project_key("unittest")
        .discount_codes()
        .with_id(discount_code.id)
        .post(
            models.DiscountCodeUpdate(
                version=discount_code.version,
                actions=[models.DiscountCodeChangeIsActiveAction(is_active=False)],
            )
        )
    )

    assert discount_code.is_active is False


def test_discount_code_delete(ct_platform_client: Client):
    discount_code = (
        ct_platform_client.with_project_key("unittest")
        .discount_codes()
        .post(
            models.DiscountCodeDraft(
                name=models.LocalizedString(en="en-discount_code"),
                code="1337",
                is_active=True,
                cart_discounts=[],
            )
        )
    )
    assert discount_code.code == "1337"

    discount_code = (
        ct_platform_client.with_project_key("unittest")
        .discount_codes()
        .with_id(discount_code.id)
        .delete(
            version=discount_code.version,
        )
    )

    assert discount_code.code == "1337"

    result = ct_platform_client.with_project_key("unittest").discount_codes().get()
    assert len(result.results) == 0


@freeze_time("2021-03-01 12:34:56")
def test_discount_code_set_valid_from(ct_platform_client: Client):
    discount_code = (
        ct_platform_client.with_project_key("unittest")
        .discount_codes()
        .post(
            models.DiscountCodeDraft(
                name=models.LocalizedString(en="en-discount_code"),
                code="1337",
                is_active=True,
                cart_discounts=[],
            )
        )
    )
    assert discount_code.id
    assert discount_code.valid_from is None

    discount_code = (
        ct_platform_client.with_project_key("unittest")
        .discount_codes()
        .with_id(discount_code.id)
        .post(
            models.DiscountCodeUpdate(
                version=discount_code.version,
                actions=[
                    models.DiscountCodeSetValidFromAction(valid_from=datetime.now())
                ],
            )
        )
    )

    assert discount_code.valid_from == datetime.now()


@freeze_time("2021-03-01 12:34:56")
def test_discount_code_set_valid_until(ct_platform_client: Client):
    discount_code = (
        ct_platform_client.with_project_key("unittest")
        .discount_codes()
        .post(
            models.DiscountCodeDraft(
                name=models.LocalizedString(en="en-discount_code"),
                code="1337",
                is_active=True,
                cart_discounts=[],
            )
        )
    )
    assert discount_code.id
    assert discount_code.valid_until is None

    discount_code = (
        ct_platform_client.with_project_key("unittest")
        .discount_codes()
        .with_id(discount_code.id)
        .post(
            models.DiscountCodeUpdate(
                version=discount_code.version,
                actions=[
                    models.DiscountCodeSetValidUntilAction(valid_until=datetime.now())
                ],
            )
        )
    )

    assert discount_code.version == 2
    assert discount_code.valid_until == datetime.now()


def test_discount_code_change_cart_discounts(ct_platform_client: Client):
    discount_code = (
        ct_platform_client.with_project_key("unittest")
        .discount_codes()
        .post(
            models.DiscountCodeDraft(
                name=models.LocalizedString(en="en-discount_code"),
                code="1337",
                is_active=True,
                cart_discounts=[],
            )
        )
    )
    assert discount_code.id
    assert discount_code.cart_discounts == []

    cart_discount = (
        ct_platform_client.with_project_key("unittest")
        .cart_discounts()
        .post(
            models.CartDiscountDraft(
                name=models.LocalizedString(en="cart-discount-test"),
                value=models.CartDiscountValueDraft(type="absolute"),
                cart_predicate="sku",
                sort_order="1",
                requires_discount_code=True,
            )
        )
    )
    assert cart_discount.id

    discount_code = (
        ct_platform_client.with_project_key("unittest")
        .discount_codes()
        .with_id(discount_code.id)
        .post(
            models.DiscountCodeUpdate(
                version=discount_code.version,
                actions=[
                    models.DiscountCodeChangeCartDiscountsAction(
                        cart_discounts=[
                            models.CartDiscountResourceIdentifier(id=cart_discount.id)
                        ]
                    )
                ],
            )
        )
    )

    assert discount_code
    assert discount_code.version == 2
    assert discount_code.cart_discounts == [
        models.CartDiscountReference(id=cart_discount.id)
    ]
