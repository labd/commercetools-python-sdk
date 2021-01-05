import pytest
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
