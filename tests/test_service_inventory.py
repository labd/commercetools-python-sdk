from commercetools import types


def test_inventory_create(client):
    inventory = client.inventory.create(types.InventoryEntryDraft(quantity_on_stock=10))

    assert inventory.id
    assert inventory.quantity_on_stock == 10


def test_inventory_get_by_id(client):
    inventory = client.inventory.create(types.InventoryEntryDraft(quantity_on_stock=10))

    assert inventory.id
    assert inventory.quantity_on_stock == 10

    inventory = client.inventory.get_by_id(inventory.id)
    assert inventory.id
    assert inventory.quantity_on_stock == 10


def test_inventory_update_by_id(client):
    inventory = client.inventory.create(types.InventoryEntryDraft(quantity_on_stock=10))

    assert inventory.id
    assert inventory.quantity_on_stock == 10

    inventory = client.inventory.update_by_id(
        inventory.id,
        version=inventory.version,
        actions=[types.InventoryEntryRemoveQuantityAction(quantity=10)],
    )
    assert inventory.id
    assert inventory.quantity_on_stock == 0
