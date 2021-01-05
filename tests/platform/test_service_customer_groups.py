from commercetools.platform import models


def test_get_by_id(old_client):
    customer_group = old_client.customer_groups.create(
        draft=models.CustomerGroupDraft(group_name="test customer group")
    )
    assert customer_group.id

    customer_group = old_client.customer_groups.get_by_id(customer_group.id)
    assert customer_group


def test_get_by_key(old_client):
    customer_group = old_client.customer_groups.create(
        draft=models.CustomerGroupDraft(
            group_name="test customer group", key="test-customer-group"
        )
    )
    assert customer_group.key

    customer_group = old_client.customer_groups.get_by_key(customer_group.key)
    assert customer_group


def test_query(old_client):
    old_client.customer_groups.create(
        draft=models.CustomerGroupDraft(
            key="test-customer-group-1", group_name="group-1"
        )
    )
    old_client.customer_groups.create(
        draft=models.CustomerGroupDraft(
            key="test-customer-group-2", group_name="group-2"
        )
    )

    result = old_client.customer_groups.query(sort="id asc", limit=10)
    assert len(result.results) == 2
    assert result.total == 2

    result = old_client.customer_groups.query(sort=["id asc", "name asc"], limit=1)
    assert len(result.results) == 1
    assert result.total == 2


def test_delete_by_id(old_client):
    customer_group = old_client.customer_groups.create(
        draft=models.CustomerGroupDraft(
            group_name="test customer group", key="test-customer-group"
        )
    )
    assert customer_group.id
    assert old_client.customer_groups.delete_by_id(
        customer_group.id, version=customer_group.version
    )


def test_delete_by_key(old_client):
    customer_group = old_client.customer_groups.create(
        draft=models.CustomerGroupDraft(
            group_name="test customer group", key="test-customer-group"
        )
    )
    assert customer_group.key
    assert old_client.customer_groups.delete_by_key(
        customer_group.key, version=customer_group.version
    )
