from commercetools.platform import models
from commercetools.platform.client import Client


def test_inventory_create(ct_platform_client: Client):
    inventory = (
        ct_platform_client.with_project_key("unittest")
        .inventory()
        .post(models.InventoryEntryDraft(sku="1", quantity_on_stock=10))
    )

    assert inventory.id
    assert inventory.quantity_on_stock == 10


def test_inventory_with_id_get(ct_platform_client: Client):
    inventory = (
        ct_platform_client.with_project_key("unittest")
        .inventory()
        .post(models.InventoryEntryDraft(sku="1", quantity_on_stock=10))
    )

    assert inventory.id
    assert inventory.quantity_on_stock == 10

    inventory = (
        ct_platform_client.with_project_key("unittest")
        .inventory()
        .with_id(inventory.id)
        .get()
    )
    assert inventory.id
    assert inventory.quantity_on_stock == 10


def test_inventory_with_id_post(ct_platform_client: Client):
    inventory = (
        ct_platform_client.with_project_key("unittest")
        .inventory()
        .post(models.InventoryEntryDraft(sku="1", quantity_on_stock=10))
    )

    assert inventory.id
    assert inventory.quantity_on_stock == 10

    inventory = (
        ct_platform_client.with_project_key("unittest")
        .inventory()
        .with_id(inventory.id)
        .post(
            models.InventoryEntryUpdate(
                version=inventory.version,
                actions=[models.InventoryEntryRemoveQuantityAction(quantity=10)],
            )
        )
    )
    assert inventory.id
    assert inventory.quantity_on_stock == 0
