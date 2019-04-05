from commercetools import types


def test_get_by_id(client):
    product = client.products.create(
        types.ProductDraft(
            master_variant=types.ProductVariantDraft(sku="123"),
            publish=True,
            name=types.LocalizedString(nl="Test product"),
        )
    )

    shopping_list = client.shopping_lists.create(
        draft=types.ShoppingListDraft(
            name=types.LocalizedString({"nl": "Verlanglijstje"}),
            description=types.LocalizedString({"nl": "Verlanglijstje van LabD"}),
            line_items=[
                types.ShoppingListLineItemDraft(product_id=product.id, quantity=1)
            ],
        )
    )
    assert shopping_list.id

    shopping_list = client.shopping_lists.get_by_id(shopping_list.id)
    assert shopping_list.name["nl"] == "Verlanglijstje"
    assert shopping_list.description["nl"] == "Verlanglijstje van LabD"
    assert shopping_list.line_items[0].product_id == product.id
    assert shopping_list.line_items[0].quantity == 1


def test_get_by_key(client):
    product = client.products.create(
        types.ProductDraft(
            master_variant=types.ProductVariantDraft(sku="123"),
            publish=True,
            name=types.LocalizedString(nl="Test product"),
        )
    )

    variant = product.master_data.current.master_variant
    shopping_list = client.shopping_lists.create(
        draft=types.ShoppingListDraft(
            key="test-shopping-list",
            name=types.LocalizedString({"nl": "Verlanglijstje"}),
            description=types.LocalizedString({"nl": "Verlanglijstje van LabD"}),
            line_items=[types.ShoppingListLineItemDraft(sku=variant.sku, quantity=1)],
        )
    )
    assert shopping_list.key

    shopping_list = client.shopping_lists.get_by_key("test-shopping-list")
    assert shopping_list.name["nl"] == "Verlanglijstje"
    assert shopping_list.description["nl"] == "Verlanglijstje van LabD"
    assert shopping_list.line_items[0].variant.sku == "123"
    assert shopping_list.line_items[0].quantity == 1


def test_query(client):
    shopping_list_draft = types.ShoppingListDraft(
        key="test-shopping-list",
        name=types.LocalizedString({"nl": "Verlanglijstje"}),
        description=types.LocalizedString({"nl": "Verlanglijstje van LabD"}),
    )

    client.shopping_lists.create(draft=shopping_list_draft)

    # Update the key and create another one.
    shopping_list_draft.key = "test-shopping-list2"
    client.shopping_lists.create(draft=shopping_list_draft)

    result = client.shopping_lists.query(sort="id asc", limit=10)
    assert len(result.results) == 2
    assert result.total == 2

    result = client.shopping_lists.query(sort=["id asc", "name asc"], limit=1)
    assert len(result.results) == 1
    assert result.total == 2


def test_delete_by_id(client):
    shopping_list = client.shopping_lists.create(
        draft=types.ShoppingListDraft(
            key="test-shopping-list",
            name=types.LocalizedString({"nl": "Verlanglijstje"}),
            description=types.LocalizedString({"nl": "Verlanglijstje van LabD"}),
        )
    )
    assert shopping_list.id

    shopping_list = client.shopping_lists.delete_by_id(
        shopping_list.id, version=shopping_list.version
    )


def test_delete_by_key(client):
    shopping_list = client.shopping_lists.create(
        draft=types.ShoppingListDraft(
            key="test-shopping-list",
            name=types.LocalizedString({"nl": "Verlanglijstje"}),
            description=types.LocalizedString({"nl": "Verlanglijstje van LabD"}),
        )
    )
    assert shopping_list.id

    shopping_list = client.shopping_lists.delete_by_key(
        shopping_list.key, version=shopping_list.version
    )
