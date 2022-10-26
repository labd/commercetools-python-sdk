from commercetools.platform import models
from commercetools.platform.client import Client


def test_with_id_get(ct_platform_client: Client):
    customer_group = (
        ct_platform_client.with_project_key("unittest")
        .customer_groups()
        .post(models.CustomerGroupDraft(group_name="test customer group"))
    )
    assert customer_group.id

    customer_group = (
        ct_platform_client.with_project_key("unittest")
        .customer_groups()
        .with_id(customer_group.id)
        .get()
    )
    assert customer_group


def test_get_by_key(ct_platform_client: Client):
    customer_group = (
        ct_platform_client.with_project_key("unittest")
        .customer_groups()
        .post(
            models.CustomerGroupDraft(
                group_name="test customer group", key="test-customer-group"
            )
        )
    )
    assert customer_group.key

    customer_group = (
        ct_platform_client.with_project_key("unittest")
        .customer_groups()
        .with_key(customer_group.key)
        .get()
    )
    assert customer_group


def test_query(ct_platform_client: Client):
    ct_platform_client.with_project_key("unittest").customer_groups().post(
        models.CustomerGroupDraft(key="test-customer-group-1", group_name="group-1")
    )
    ct_platform_client.with_project_key("unittest").customer_groups().post(
        models.CustomerGroupDraft(key="test-customer-group-2", group_name="group-2")
    )

    result = (
        ct_platform_client.with_project_key("unittest")
        .customer_groups()
        .get(sort="id asc", limit=10)
    )
    assert len(result.results) == 2
    assert result.total == 2

    result = (
        ct_platform_client.with_project_key("unittest")
        .customer_groups()
        .get(sort=["id asc", "name asc"], limit=1)
    )
    assert len(result.results) == 1
    assert result.total == 2


def test_delete_by_id(ct_platform_client: Client):
    customer_group = (
        ct_platform_client.with_project_key("unittest")
        .customer_groups()
        .post(
            models.CustomerGroupDraft(
                group_name="test customer group", key="test-customer-group"
            )
        )
    )
    assert customer_group.id
    assert (
        ct_platform_client.with_project_key("unittest")
        .customer_groups()
        .with_id(customer_group.id)
        .delete(version=customer_group.version)
    )


def test_delete_by_key(ct_platform_client: Client):
    customer_group = (
        ct_platform_client.with_project_key("unittest")
        .customer_groups()
        .post(
            models.CustomerGroupDraft(
                group_name="test customer group", key="test-customer-group"
            )
        )
    )
    assert customer_group.key
    assert (
        ct_platform_client.with_project_key("unittest")
        .customer_groups()
        .with_key(customer_group.key)
        .delete(version=customer_group.version)
    )
