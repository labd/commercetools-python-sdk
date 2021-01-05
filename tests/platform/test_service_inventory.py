from commercetools.platform import models


def test_inventory_create(old_client):
    inventory = old_client.inventory.create(
        models.InventoryEntryDraft(sku="1", quantity_on_stock=10)
    )

    assert inventory.id
    assert inventory.quantity_on_stock == 10


def test_inventory_get_by_id(old_client):
    inventory = old_client.inventory.create(
        models.InventoryEntryDraft(sku="1", quantity_on_stock=10)
    )

    assert inventory.id
    assert inventory.quantity_on_stock == 10

    inventory = old_client.inventory.get_by_id(inventory.id)
    assert inventory.id
    assert inventory.quantity_on_stock == 10


def test_inventory_update_by_id(old_client):
    inventory = old_client.inventory.create(
        models.InventoryEntryDraft(sku="1", quantity_on_stock=10)
    )

    assert inventory.id
    assert inventory.quantity_on_stock == 10

    inventory = old_client.inventory.update_by_id(
        inventory.id,
        version=inventory.version,
        actions=[models.InventoryEntryRemoveQuantityAction(quantity=10)],
    )
    assert inventory.id
    assert inventory.quantity_on_stock == 0
