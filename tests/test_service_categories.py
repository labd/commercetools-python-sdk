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

    category = client.categories.create(
        types.CategoryDraft(key="test-category")
    )

    assert category.id
    assert category.key == "test-category"

    category = client.categories.get_by_id(category.id)
    assert category.id
    assert category.key == "test-category"

    with pytest.raises(HTTPError):
        client.categories.get_by_id('invalid')

    category = client.categories.get_by_key(category.key)
    assert category
