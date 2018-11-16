import uuid

import pytest
import requests_mock
from requests.exceptions import HTTPError

from commercetools import types


def test_products_get_by_id(client):
    product = client.products.create(types.ProductDraft(key="test-product"))

    assert product.id
    assert product.key == "test-product"

    product = client.products.get_by_id(product.id)
    assert product.id
    assert product.key == "test-product"

    with pytest.raises(HTTPError) as e:
        client.products.get_by_id("invalid")


def test_products_get_by_key(client):
    product = client.products.create(types.ProductDraft(key="test-product"))

    assert product.id
    assert product.key == "test-product"

    product = client.products.get_by_key("test-product")
    assert product.id
    assert product.key == "test-product"

    with pytest.raises(HTTPError) as e:
        client.products.get_by_key("invalid")


def test_product_query(client):
    client.products.create(types.ProductDraft(key="test-product1"))
    client.products.create(types.ProductDraft(key="test-product2"))

    # single sort query
    result = client.products.query(sort="id asc", limit=2)
    assert len(result.results) == 2
    assert result.total == 2

    # multiple sort queries
    result = client.products.query(sort=["id asc", "name asc"])
    assert len(result.results) == 2
    assert result.total == 2


def test_product_update(client):
    """Test the return value of the update methods.

    It doesn't test the actual update itself.
    TODO: See if this is worth testing since we're using a mocking backend
    """
    product = client.products.create(types.ProductDraft(key="test-product"))

    assert uuid.UUID(product.id)
    assert product.key == "test-product"

    product = client.products.update_by_id(
        id=product.id,
        version=product.version,
        actions=[
            types.ProductChangeSlugAction(slug=types.LocalizedString(nl="nl-slug2"))
        ],
    )
    assert product.key == "test-product"

    product = client.products.update_by_key(
        key="test-product",
        version=product.version,
        actions=[
            types.ProductChangeSlugAction(slug=types.LocalizedString(nl="nl-slug2"))
        ],
    )
    assert product.key == "test-product"
