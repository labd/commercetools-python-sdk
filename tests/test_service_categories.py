import pytest
from requests.exceptions import HTTPError

from commercetools import types


def test_category_get_by_id(client):
    category = client.categories.create(types.CategoryDraft(key="test-category"))

    assert category.id
    assert category.key == "test-category"

    category = client.categories.get_by_id(category.id)
    assert category.id
    assert category.key == "test-category"

    with pytest.raises(HTTPError):
        client.categories.get_by_id("invalid")


def test_category_get_by_key(client):
    category = client.categories.create(types.CategoryDraft(key="test-category"))

    assert category.id
    assert category.key == "test-category"

    category = client.categories.get_by_key("test-category")
    assert category.id
    assert category.key == "test-category"

    with pytest.raises(HTTPError):
        client.categories.get_by_key("invalid")


def test_category_query(client):
    client.categories.create(types.CategoryDraft(key="test-category1"))
    client.categories.create(types.CategoryDraft(key="test-category2"))

    # single sort query
    result = client.categories.query(sort="id asc", limit=10)
    assert len(result.results) == 2
    assert result.total == 2

    # multiple sort queries
    result = client.categories.query(sort=["id asc", "name asc"])
    assert len(result.results) == 2
    assert result.total == 2


def test_category_update(client):
    """Test the return value of the update methods.

    It doesn't test the actual update itself.
    TODO: See if this is worth testing since we're using a mocking backend
    """
    category = client.categories.create(
        types.CategoryDraft(
            key="test-category", slug=types.LocalizedString(nl="nl-slug")
        )
    )
    assert category.key == "test-category"

    category = client.categories.update_by_id(
        id=category.id,
        version=category.version,
        actions=[
            types.CategoryChangeSlugAction(slug=types.LocalizedString(nl="nl-slug2"))
        ],
    )
    assert category.key == "test-category"

    category = client.categories.update_by_key(
        key="test-category",
        version=category.version,
        actions=[
            types.CategoryChangeSlugAction(slug=types.LocalizedString(nl="nl-slug2"))
        ],
    )
    assert category.key == "test-category"
