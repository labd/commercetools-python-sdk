import pytest

from requests.exceptions import HTTPError

from commercetools import types

def test_category_get(client):
    category = client.categories.create(types.CategoryDraft(key="test-category"))

    assert category.id
    assert category.key == "test-category"

    category = client.categories.get_by_id(category.id)
    assert category.id
    assert category.key == "test-category"

    with pytest.raises(HTTPError):
        client.categories.get_by_id("invalid")

    category = client.categories.get_by_key(category.key)
    assert category


def test_category_query(client):
    client.categories.create(types.CategoryDraft(key="test-category1"))
    client.categories.create(types.CategoryDraft(key="test-category2"))

    # single sort query
    result = client.categories.query(sort="id asc")
    assert len(result.results) == 2
    assert result.total == 2

    # multiple sort queries
    result = client.categories.query(sort=["id asc", "name asc"])
    assert len(result.results) == 2
    assert result.total == 2


def test_category_update(client):
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
