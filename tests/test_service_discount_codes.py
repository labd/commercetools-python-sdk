import pytest
from requests.exceptions import HTTPError

from commercetools import types


def test_discount_code_get_by_id(client):
    discount_code = client.discount_codes.create(
        types.DiscountCodeDraft(
            name=types.LocalizedString({"en": "test discount"}), code="1337"
        )
    )

    assert discount_code.id
    assert discount_code.code == "1337"

    discount_code = client.discount_codes.get_by_id(discount_code.id)
    assert discount_code.id
    assert discount_code.code == "1337"

    with pytest.raises(HTTPError):
        client.discount_codes.get_by_id("invalid")


def test_discount_code_query(client):
    client.discount_codes.create(
        types.DiscountCodeDraft(
            name=types.LocalizedString({"en:": "test discount"}), code="1337"
        )
    )
    client.discount_codes.create(
        types.DiscountCodeDraft(
            name=types.LocalizedString({"en:": "test discount"}), code="1338"
        )
    )

    # single sort query
    result = client.discount_codes.query(sort="id asc")
    assert len(result.results) == 2
    assert result.total == 2

    # multiple sort queries
    result = client.discount_codes.query(sort=["id asc", "name asc"])
    assert len(result.results) == 2
    assert result.total == 2


def test_discount_code_update(client):
    discount_code = client.discount_codes.create(
        types.DiscountCodeDraft(
            name=types.LocalizedString(en="en-discount_code"),
            code="1337",
            is_active=True,
        )
    )
    assert discount_code.code == "1337"

    discount_code = client.discount_codes.update_by_id(
        id=discount_code.id,
        version=discount_code.version,
        actions=[types.DiscountCodeChangeIsActiveAction(is_active=False)],
    )

    assert discount_code.is_active is False
