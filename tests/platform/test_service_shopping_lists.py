from commercetools.platform import models
from commercetools.platform.client import Client


def test_get_with_id(ct_platform_client: Client):
    product = (
        ct_platform_client.with_project_key("unittest")
        .products()
        .post(
            models.ProductDraft(
                master_variant=models.ProductVariantDraft(sku="123"),
                publish=True,
                name=models.LocalizedString(nl="Test product"),
                slug=models.LocalizedString(en=f"my-product"),
                product_type=models.ProductTypeResourceIdentifier(key="dummy"),
            )
        )
    )

    shopping_list = (
        ct_platform_client.with_project_key("unittest")
        .shopping_lists()
        .post(
            models.ShoppingListDraft(
                name=models.LocalizedString({"nl": "Verlanglijstje"}),
                description=models.LocalizedString({"nl": "Verlanglijstje van LabD"}),
                line_items=[
                    models.ShoppingListLineItemDraft(product_id=product.id, quantity=1)
                ],
            )
        )
    )
    assert shopping_list
    assert shopping_list.id

    shopping_list = (
        ct_platform_client.with_project_key("unittest")
        .shopping_lists()
        .with_id(shopping_list.id)
        .get()
    )
    assert shopping_list
    assert shopping_list.name["nl"] == "Verlanglijstje"
    assert shopping_list.description["nl"] == "Verlanglijstje van LabD"
    assert shopping_list.line_items[0].product_id == product.id
    assert shopping_list.line_items[0].quantity == 1


def test_get_by_key(ct_platform_client: Client):
    product = (
        ct_platform_client.with_project_key("unittest")
        .products()
        .post(
            models.ProductDraft(
                master_variant=models.ProductVariantDraft(sku="123"),
                publish=True,
                name=models.LocalizedString(nl="Test product"),
                slug=models.LocalizedString(en="my-product"),
                product_type=models.ProductTypeResourceIdentifier(key="dummy"),
            )
        )
    )

    variant = product.master_data.current.master_variant
    shopping_list = (
        ct_platform_client.with_project_key("unittest")
        .shopping_lists()
        .post(
            models.ShoppingListDraft(
                key="test-shopping-list",
                name=models.LocalizedString({"nl": "Verlanglijstje"}),
                description=models.LocalizedString({"nl": "Verlanglijstje van LabD"}),
                line_items=[
                    models.ShoppingListLineItemDraft(sku=variant.sku, quantity=1)
                ],
            )
        )
    )
    assert shopping_list.key

    shopping_list = (
        ct_platform_client.with_project_key("unittest")
        .shopping_lists()
        .with_key("test-shopping-list")
        .get()
    )
    assert shopping_list.name["nl"] == "Verlanglijstje"
    assert shopping_list.description["nl"] == "Verlanglijstje van LabD"
    assert shopping_list.line_items[0].variant.sku == "123"
    assert shopping_list.line_items[0].quantity == 1


def test_query(ct_platform_client: Client):
    shopping_list_draft = models.ShoppingListDraft(
        key="test-shopping-list",
        name=models.LocalizedString({"nl": "Verlanglijstje"}),
        description=models.LocalizedString({"nl": "Verlanglijstje van LabD"}),
    )

    ct_platform_client.with_project_key("unittest").shopping_lists().post(
        shopping_list_draft
    )

    # Update the key and create another one.
    shopping_list_draft.key = "test-shopping-list2"
    ct_platform_client.with_project_key("unittest").shopping_lists().post(
        shopping_list_draft
    )

    result = (
        ct_platform_client.with_project_key("unittest")
        .shopping_lists()
        .get(sort="id asc", limit=10)
    )
    assert len(result.results) == 2
    assert result.total == 2

    result = (
        ct_platform_client.with_project_key("unittest")
        .shopping_lists()
        .get(sort=["id asc", "name asc"], limit=1)
    )
    assert len(result.results) == 1
    assert result.total == 2


def test_delete_by_id(ct_platform_client: Client):
    shopping_list = (
        ct_platform_client.with_project_key("unittest")
        .shopping_lists()
        .post(
            models.ShoppingListDraft(
                key="test-shopping-list",
                name=models.LocalizedString({"nl": "Verlanglijstje"}),
                description=models.LocalizedString({"nl": "Verlanglijstje van LabD"}),
            )
        )
    )
    assert shopping_list.id

    shopping_list = (
        ct_platform_client.with_project_key("unittest")
        .shopping_lists()
        .with_id(shopping_list.id)
        .delete(version=shopping_list.version)
    )


def test_delete_by_key(ct_platform_client: Client):
    shopping_list = (
        ct_platform_client.with_project_key("unittest")
        .shopping_lists()
        .post(
            models.ShoppingListDraft(
                key="test-shopping-list",
                name=models.LocalizedString({"nl": "Verlanglijstje"}),
                description=models.LocalizedString({"nl": "Verlanglijstje van LabD"}),
            )
        )
    )
    assert shopping_list.id

    shopping_list = (
        ct_platform_client.with_project_key("unittest")
        .shopping_lists()
        .with_key(shopping_list.key)
        .delete(version=shopping_list.version)
    )
