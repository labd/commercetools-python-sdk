import pytest

from commercetools import types


@pytest.fixture
def shopping_list_draft():
    return types.ShoppingListDraft(
        key="test-shopping-list",
        name=types.LocalizedString({"nl": "Verlanglijstje"}),
        description=types.LocalizedString({"nl": "Verlanglijstje van LabD"}),
        line_items=[
            types.ShoppingListLineItemDraft(sku="123", quantity=2),
            types.ShoppingListLineItemDraft(sku="124", quantity=1),
        ],
    )


def test_get_by_id(client, shopping_list_draft):
    shopping_list = client.shopping_lists.create(shopping_list_draft)
    assert shopping_list.id

    shopping_list_id = shopping_list.id
    shopping_list = client.shopping_lists.get_by_id(shopping_list_id)
    assert type(shopping_list) == types.ShoppingList
    assert shopping_list.id == shopping_list_id


def test_get_by_key(client, shopping_list_draft):
    shopping_list = client.shopping_lists.create(shopping_list_draft)

    assert shopping_list.id
    assert shopping_list.key

    shopping_list = client.shopping_lists.get_by_key(shopping_list.key)
    assert type(shopping_list) == types.ShoppingList
    assert shopping_list.key == "test-shopping-list"


def test_query(client, shopping_list_draft):
    client.shopping_lists.create(shopping_list_draft)
    shopping_list_draft.key = "test-shopping-list2"
    client.shopping_lists.create(shopping_list_draft)

    result = client.shopping_lists.query(sort="id asc", limit=10)
    assert len(result.results) == 2
    assert result.total == 2

    result = client.shopping_lists.query(sort=["id asc", "name asc"], limit=1)
    assert len(result.results) == 1
    assert result.total == 2


def test_delete_by_id(client, shopping_list_draft):
    shopping_list = client.shopping_lists.create(shopping_list_draft)
    assert shopping_list.id

    shopping_list = client.shopping_lists.delete_by_id(
        shopping_list.id, version=shopping_list.version
    )


def test_delete_by_key(client, shopping_list_draft):
    shopping_list = client.shopping_lists.create(shopping_list_draft)
    assert shopping_list.id

    shopping_list = client.shopping_lists.delete_by_key(
        shopping_list.key, version=shopping_list.version
    )
