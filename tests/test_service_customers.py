import datetime

from commercetools import types


def _get_draft_object(**kwargs):
    customer = {
        "first_name": "John",
        "last_name": "Doe",
        "title": "mr",
        "date_of_birth": datetime.date(year=1985, month=8, day=4),
    }
    customer.update(kwargs)
    return types.CustomerDraft(**customer)


def test_get_by_id(client):
    customer = client.customers.create(draft=_get_draft_object())
    assert customer.id

    customer = client.customers.get_by_id(customer.id)
    assert customer


def test_get_by_key(client):
    customer = client.customers.create(draft=_get_draft_object(key="test-customer"))
    assert customer.key

    customer = client.customers.get_by_key(customer.key)
    assert customer


def test_query(client):
    client.customers.create(draft=_get_draft_object(key="test-customer-1"))
    client.customers.create(draft=_get_draft_object(key="test-customer-2"))

    result = client.customers.query(sort="id asc", limit=10)
    assert len(result.results) == 2
    assert result.total == 2

    result = client.customers.query(sort=["id asc", "name asc"], limit=1)
    assert len(result.results) == 1
    assert result.total == 2


def test_delete_by_id(client):
    customer = client.customers.create(draft=_get_draft_object())
    assert customer.id
    assert client.customers.delete_by_id(customer.id, version=customer.version)


def test_delete_by_key(client):
    customer = client.customers.create(draft=_get_draft_object(key="test-customer"))
    assert customer.key
    assert client.customers.delete_by_key(customer.key, version=customer.version)
