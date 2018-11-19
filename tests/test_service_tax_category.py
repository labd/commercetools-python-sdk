from commercetools import types


def test_tax_category_create(client):
    tax_category = client.tax_categories.create(types.TaxCategoryDraft(name="Hoog"))

    assert tax_category.id
    assert tax_category.name == "Hoog"


def test_tax_category_get_by_id(client):
    tax_category = client.tax_categories.create(types.TaxCategoryDraft(name="Hoog"))

    assert tax_category.id
    assert tax_category.name == "Hoog"

    tax_category = client.tax_categories.get_by_id(tax_category.id)
    assert tax_category.id
    assert tax_category.name == "Hoog"


def test_tax_category_update_by_id(client):
    tax_category = client.tax_categories.create(types.TaxCategoryDraft(name="Hoog"))

    assert tax_category.id
    assert tax_category.name == "Hoog"

    tax_category = client.tax_categories.update_by_id(
        tax_category.id,
        version=tax_category.version,
        actions=[types.TaxCategorySetDescriptionAction(description="Some text")],
    )
    assert tax_category.id
    assert tax_category.name == "Hoog"
