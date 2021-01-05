import pytest
from requests.exceptions import HTTPError

from commercetools.platform import models


def test_category_get_by_id(old_client):
    category = old_client.categories.create(
        models.CategoryDraft(
            key="test-category",
            name=models.LocalizedString(en="category"),
            slug=models.LocalizedString(en="something"),
        )
    )

    assert category.id
    assert category.key == "test-category"

    category = old_client.categories.get_by_id(category.id)
    assert category.id
    assert category.key == "test-category"

    with pytest.raises(HTTPError):
        old_client.categories.get_by_id("invalid")


def test_category_get_by_key(old_client):
    category = old_client.categories.create(
        models.CategoryDraft(
            key="test-category",
            name=models.LocalizedString(en="category"),
            slug=models.LocalizedString(en="something"),
        )
    )

    assert category.id
    assert category.key == "test-category"

    category = old_client.categories.get_by_key("test-category")
    assert category.id
    assert category.key == "test-category"

    with pytest.raises(HTTPError):
        old_client.categories.get_by_key("invalid")


def test_category_query(old_client):
    category = old_client.categories.create(
        models.CategoryDraft(
            key="test-category1",
            name=models.LocalizedString(en="category"),
            slug=models.LocalizedString(en="something"),
        )
    )
    category = old_client.categories.create(
        models.CategoryDraft(
            key="test-category2",
            name=models.LocalizedString(en="category"),
            slug=models.LocalizedString(en="something"),
        )
    )

    # single sort query
    result = old_client.categories.query(sort="id asc", limit=10)
    assert len(result.results) == 2
    assert result.total == 2

    # multiple sort queries
    result = old_client.categories.query(sort=["id asc", "name asc"])
    assert len(result.results) == 2
    assert result.total == 2


def test_category_update(old_client):
    """Test the return value of the update methods.

    It doesn't test the actual update itself.
    TODO: See if this is worth testing since we're using a mocking backend
    """
    category = old_client.categories.create(
        models.CategoryDraft(
            key="test-category",
            slug=models.LocalizedString(nl="nl-slug"),
            name=models.LocalizedString(nl="category"),
        )
    )
    assert category.key == "test-category"

    category = old_client.categories.update_by_id(
        id=category.id,
        version=category.version,
        actions=[
            models.CategoryChangeSlugAction(slug=models.LocalizedString(nl="nl-slug2"))
        ],
    )
    assert category.key == "test-category"

    category = old_client.categories.update_by_key(
        key="test-category",
        version=category.version,
        actions=[
            models.CategoryChangeSlugAction(slug=models.LocalizedString(nl="nl-slug2"))
        ],
    )
    assert category.key == "test-category"
