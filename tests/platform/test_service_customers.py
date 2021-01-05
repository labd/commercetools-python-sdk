import datetime

from commercetools.platform import models


def _get_draft_object(**kwargs):
    customer = {
        "first_name": "John",
        "last_name": "Doe",
        "title": "mr",
        "date_of_birth": datetime.date(year=1985, month=8, day=4),
        "email": "info@example.org",
        "password": "notsosecret",
    }
    customer.update(kwargs)
    return models.CustomerDraft(**customer)


def test_get_by_id(old_client):
    result = old_client.customers.create(draft=_get_draft_object())
    assert result.customer.id

    customer = old_client.customers.get_by_id(result.customer.id)
    assert customer


def test_get_by_key(old_client):
    result = old_client.customers.create(draft=_get_draft_object(key="test-customer"))
    assert result.customer.key
    assert result.cart is None

    customer = old_client.customers.get_by_key(result.customer.key)
    assert customer


def test_query(old_client):
    old_client.customers.create(draft=_get_draft_object(key="test-customer-1"))
    old_client.customers.create(draft=_get_draft_object(key="test-customer-2"))

    result = old_client.customers.query(sort="id asc", limit=10)
    assert len(result.results) == 2
    assert result.total == 2

    result = old_client.customers.query(sort=["id asc", "name asc"], limit=1)
    assert len(result.results) == 1
    assert result.total == 2


def test_delete_by_id(old_client):
    result = old_client.customers.create(draft=_get_draft_object())
    assert result.customer.id
    assert old_client.customers.delete_by_id(
        result.customer.id, version=result.customer.version
    )


def test_delete_by_key(old_client):
    result = old_client.customers.create(draft=_get_draft_object(key="test-customer"))
    assert result.customer.key
    assert old_client.customers.delete_by_key(
        result.customer.key, version=result.customer.version
    )
