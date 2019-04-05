from commercetools import types


def test_get_by_id(client):
    customer_group = client.customer_groups.create(
        draft=types.CustomerGroupDraft(group_name="test customer group")
    )
    assert customer_group.id

    customer_group = client.customer_groups.get_by_id(customer_group.id)
    assert customer_group


def test_get_by_key(client):
    customer_group = client.customer_groups.create(
        draft=types.CustomerGroupDraft(
            group_name="test customer group", key="test-customer-group"
        )
    )
    assert customer_group.key

    customer_group = client.customer_groups.get_by_key(customer_group.key)
    assert customer_group


def test_query(client):
    client.customer_groups.create(
        draft=types.CustomerGroupDraft(key="test-customer-group-1")
    )
    client.customer_groups.create(
        draft=types.CustomerGroupDraft(key="test-customer-group-2")
    )

    result = client.customer_groups.query(sort="id asc", limit=10)
    assert len(result.results) == 2
    assert result.total == 2

    result = client.customer_groups.query(sort=["id asc", "name asc"], limit=1)
    assert len(result.results) == 1
    assert result.total == 2


def test_delete_by_id(client):
    customer_group = client.customer_groups.create(
        draft=types.CustomerGroupDraft(
            group_name="test customer group", key="test-customer-group"
        )
    )
    assert customer_group.id
    assert client.customer_groups.delete_by_id(
        customer_group.id, version=customer_group.version
    )


def test_delete_by_key(client):
    customer_group = client.customer_groups.create(
        draft=types.CustomerGroupDraft(
            group_name="test customer group", key="test-customer-group"
        )
    )
    assert customer_group.key
    assert client.customer_groups.delete_by_key(
        customer_group.key, version=customer_group.version
    )
