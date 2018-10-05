import pytest

from requests.exceptions import HTTPError

from commercetools.testing import mock_commercetools


@mock_commercetools
def test_products_get():
    from commercetools import Client, types

    client = Client(
        project_key="unittest",
        client_id="client-id",
        client_secret="client-secret",
        scope=[],
        url="https://api.sphere.io",
        token_url="https://auth.sphere.io/oauth/token",
    )

    product = client.products.create(
        types.ProductDraft(key="test-product")
    )

    assert product.id
    assert product.key == "test-product"

    product = client.products.get_by_id(product.id)
    assert product.id
    assert product.key == "test-product"

    with pytest.raises(HTTPError) as e:
        client.products.get_by_id('invalid')

    product = client.products.get_by_key(product.key)
    assert product


@mock_commercetools
def test_product_update():
    from commercetools import Client, types

    client = Client(
        project_key="unittest",
        client_id="client-id",
        client_secret="client-secret",
        scope=[],
        url="https://api.sphere.io",
        token_url="https://auth.sphere.io/oauth/token",
    )

    product = client.products.create(
        types.ProductDraft(key="test-product")
    )

    assert product.id
    assert product.key == "test-product"

    product = client.products.update_by_id(
        id=product.id,
        version=product.version,
        actions=[
            types.ProductChangeSlugAction(slug=types.LocalizedString(nl='nl-slug2'))
        ]
    )
    assert product.key == 'test-product'

    product = client.products.update_by_key(
        key='test-product',
        version=product.version,
        actions=[
            types.ProductChangeSlugAction(slug=types.LocalizedString(nl='nl-slug2'))
        ]
    )
    assert product.key == 'test-product'

