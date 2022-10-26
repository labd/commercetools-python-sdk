import pytest
from requests.exceptions import HTTPError

from commercetools.platform import models
from commercetools.platform.client import Client


def test_category_with_id_get(ct_platform_client: Client):
    category = (
        ct_platform_client.with_project_key("unittest")
        .categories()
        .post(
            models.CategoryDraft(
                key="test-category",
                name=models.LocalizedString(en="category"),
                slug=models.LocalizedString(en="something"),
            )
        )
    )

    assert category.id
    assert category.key == "test-category"

    category = (
        ct_platform_client.with_project_key("unittest")
        .categories()
        .with_id(category.id)
        .get()
    )
    assert category.id
    assert category.key == "test-category"

    with pytest.raises(HTTPError):
        ct_platform_client.with_project_key("unittest").categories().with_id(
            "invalid"
        ).get()


def test_category_get_by_key(ct_platform_client: Client):
    category = (
        ct_platform_client.with_project_key("unittest")
        .categories()
        .post(
            models.CategoryDraft(
                key="test-category",
                name=models.LocalizedString(en="category"),
                slug=models.LocalizedString(en="something"),
            )
        )
    )

    assert category.id
    assert category.key == "test-category"

    category = (
        ct_platform_client.with_project_key("unittest")
        .categories()
        .with_key("test-category")
        .get()
    )
    assert category.id
    assert category.key == "test-category"

    with pytest.raises(HTTPError):
        ct_platform_client.with_project_key("unittest").categories().with_key(
            "invalid"
        ).get()


def test_category_query(ct_platform_client: Client):
    category = (
        ct_platform_client.with_project_key("unittest")
        .categories()
        .post(
            models.CategoryDraft(
                key="test-category1",
                name=models.LocalizedString(en="category"),
                slug=models.LocalizedString(en="something"),
            )
        )
    )
    category = (
        ct_platform_client.with_project_key("unittest")
        .categories()
        .post(
            models.CategoryDraft(
                key="test-category2",
                name=models.LocalizedString(en="category"),
                slug=models.LocalizedString(en="something"),
            )
        )
    )

    # single sort query
    result = (
        ct_platform_client.with_project_key("unittest")
        .categories()
        .get(sort="id asc", limit=10)
    )
    assert len(result.results) == 2
    assert result.total == 2

    # multiple sort queries
    result = (
        ct_platform_client.with_project_key("unittest")
        .categories()
        .get(sort=["id asc", "name asc"])
    )
    assert len(result.results) == 2
    assert result.total == 2


def test_category_update(ct_platform_client: Client):
    """Test the return value of the update methods.

    It doesn't test the actual update itself.
    TODO: See if this is worth testing since we're using a mocking backend
    """
    parent_category = (
        ct_platform_client.with_project_key("unittest")
        .categories()
        .post(
            models.CategoryDraft(
                key="parent-test-category",
                slug=models.LocalizedString(nl="nl-slug-parent"),
                name=models.LocalizedString(nl="parent-category"),
            )
        )
    )

    category = (
        ct_platform_client.with_project_key("unittest")
        .categories()
        .post(
            models.CategoryDraft(
                key="test-category",
                slug=models.LocalizedString(nl="nl-slug"),
                name=models.LocalizedString(nl="category"),
                parent=models.CategoryResourceIdentifier(id=parent_category.id),
                order_hint="0.00001",
                description=models.LocalizedString(nl="description-nl"),
            )
        )
    )
    assert category.key == "test-category"
    assert category.order_hint == "0.00001"
    assert getattr(category.parent, "id") == parent_category.id

    category = (
        ct_platform_client.with_project_key("unittest")
        .categories()
        .with_id(category.id)
        .post(
            models.CategoryUpdate(
                version=category.version,
                actions=[
                    models.CategoryChangeSlugAction(
                        slug=models.LocalizedString(nl="nl-slug2")
                    ),
                    models.CategorySetDescriptionAction(
                        description=models.LocalizedString(nl="updated-description-nl")
                    ),
                ],
            )
        )
    )
    assert category.key == "test-category"
    assert category.description == models.LocalizedString(nl="updated-description-nl")

    category = (
        ct_platform_client.with_project_key("unittest")
        .categories()
        .with_key("test-category")
        .post(
            models.CategoryUpdate(
                version=category.version,
                actions=[
                    models.CategoryChangeSlugAction(
                        slug=models.LocalizedString(nl="nl-slug2")
                    )
                ],
            )
        )
    )
    assert category.key == "test-category"
