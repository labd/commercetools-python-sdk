from commercetools.platform import models
from commercetools.platform.client import Client


def test_tax_category_create(ct_platform_client: Client):
    tax_category = (
        ct_platform_client.with_project_key("unittest")
        .tax_categories()
        .post(models.TaxCategoryDraft(name="Hoog", rates=[]))
    )
    assert tax_category
    assert tax_category.id
    assert tax_category.name == "Hoog"


def test_tax_category_get_with_id(ct_platform_client: Client):
    tax_category = (
        ct_platform_client.with_project_key("unittest")
        .tax_categories()
        .post(models.TaxCategoryDraft(name="Hoog", rates=[]))
    )

    assert tax_category
    assert tax_category.id
    assert tax_category.name == "Hoog"

    tax_category = (
        ct_platform_client.with_project_key("unittest")
        .tax_categories()
        .with_id(tax_category.id)
        .get()
    )
    assert tax_category
    assert tax_category.id
    assert tax_category.name == "Hoog"


def test_tax_category_create_with_id(ct_platform_client: Client):
    tax_category = (
        ct_platform_client.with_project_key("unittest")
        .tax_categories()
        .post(models.TaxCategoryDraft(name="Hoog", rates=[]))
    )

    assert tax_category.id
    assert tax_category.name == "Hoog"

    tax_category = (
        ct_platform_client.with_project_key("unittest")
        .tax_categories()
        .with_id(
            tax_category.id,
        )
        .post(
            models.TaxCategoryUpdate(
                version=tax_category.version,
                actions=[
                    models.TaxCategorySetDescriptionAction(description="Some text")
                ],
            )
        )
    )
    assert tax_category
    assert tax_category.id
    assert tax_category.name == "Hoog"
