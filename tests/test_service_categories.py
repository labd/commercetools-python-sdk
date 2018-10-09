import pytest

from requests.exceptions import HTTPError

from commercetools.testing import mock_commercetools


@mock_commercetools
def test_category_get():
    from commercetools import Client, types

    client = Client(
        project_key="unittest",
        client_id="client-id",
        client_secret="client-secret",
        scope=[],
        url="https://api.sphere.io",
        token_url="https://auth.sphere.io/oauth/token",
    )

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


@mock_commercetools
def test_category_query():
    from commercetools import Client, types

    client = Client(
        project_key="unittest",
        client_id="client-id",
        client_secret="client-secret",
        scope=[],
        url="https://api.sphere.io",
        token_url="https://auth.sphere.io/oauth/token",
    )

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


@mock_commercetools
def test_category_update():
    from commercetools import Client, types

    client = Client(
        project_key="unittest",
        client_id="client-id",
        client_secret="client-secret",
        scope=[],
        url="https://api.sphere.io",
        token_url="https://auth.sphere.io/oauth/token",
    )

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
