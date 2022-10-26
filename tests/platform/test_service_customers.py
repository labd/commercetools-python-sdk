import datetime

from commercetools.platform import models
from commercetools.platform.client import Client


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


def test_with_id_get(ct_platform_client: Client):
    draft = _get_draft_object()
    result = ct_platform_client.with_project_key("unittest").customers().post(draft)
    assert result.customer.id
    customer = (
        ct_platform_client.with_project_key("unittest")
        .customers()
        .with_id(result.customer.id)
        .get()
    )
    assert customer


def test_get_by_key(ct_platform_client: Client):
    draft = _get_draft_object(key="test-customer")
    result = ct_platform_client.with_project_key("unittest").customers().post(draft)
    assert result.customer.key
    assert result.cart is None

    customer = (
        ct_platform_client.with_project_key("unittest")
        .customers()
        .with_key(result.customer.key)
        .get()
    )
    assert customer


def test_query(ct_platform_client: Client):
    ct_platform_client.with_project_key("unittest").customers().post(
        _get_draft_object(key="test-customer-1")
    )
    ct_platform_client.with_project_key("unittest").customers().post(
        _get_draft_object(key="test-customer-2")
    )

    result = (
        ct_platform_client.with_project_key("unittest")
        .customers()
        .get(sort="id asc", limit=10)
    )
    assert len(result.results) == 2
    assert result.total == 2

    result = (
        ct_platform_client.with_project_key("unittest")
        .customers()
        .get(sort=["id asc", "name asc"], limit=1)
    )
    assert len(result.results) == 1
    assert result.total == 2


def test_delete_by_id(ct_platform_client: Client):
    draft = _get_draft_object()
    result = ct_platform_client.with_project_key("unittest").customers().post(draft)
    assert result.customer.id
    assert (
        ct_platform_client.with_project_key("unittest")
        .customers()
        .with_id(result.customer.id)
        .delete(version=result.customer.version)
    )


def test_delete_by_key(ct_platform_client: Client):
    result = (
        ct_platform_client.with_project_key("unittest")
        .customers()
        .post(_get_draft_object(key="test-customer"))
    )
    assert result and result.customer
    assert result.customer.key
    assert (
        ct_platform_client.with_project_key("unittest")
        .customers()
        .with_key(result.customer.key)
        .delete(version=result.customer.version)
    )
