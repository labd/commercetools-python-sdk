from commercetools.platform import models


def test_tax_category_create(old_client):
    tax_category = old_client.tax_categories.create(
        models.TaxCategoryDraft(name="Hoog", rates=[])
    )

    assert tax_category.id
    assert tax_category.name == "Hoog"


def test_tax_category_get_by_id(old_client):
    tax_category = old_client.tax_categories.create(
        models.TaxCategoryDraft(name="Hoog", rates=[])
    )

    assert tax_category.id
    assert tax_category.name == "Hoog"

    tax_category = old_client.tax_categories.get_by_id(tax_category.id)
    assert tax_category.id
    assert tax_category.name == "Hoog"


def test_tax_category_update_by_id(old_client):
    tax_category = old_client.tax_categories.create(
        models.TaxCategoryDraft(name="Hoog", rates=[])
    )

    assert tax_category.id
    assert tax_category.name == "Hoog"

    tax_category = old_client.tax_categories.update_by_id(
        tax_category.id,
        version=tax_category.version,
        actions=[models.TaxCategorySetDescriptionAction(description="Some text")],
    )
    assert tax_category.id
    assert tax_category.name == "Hoog"
