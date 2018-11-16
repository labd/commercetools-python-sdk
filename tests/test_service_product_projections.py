import pytest
from requests.exceptions import HTTPError

from commercetools import types


def test_product_projections_get_by_id(client):
    product_create = client.products.create(
        types.ProductDraft(key="test-product1", publish=False)
    )
    product = client.product_projections.get_by_id(product_create.id)
    assert product.id == product_create.id
    assert product.key == product_create.key


def test_product_projections_get_by_id_not_found(client):
    with pytest.raises(HTTPError):
        client.products.get_by_id("invalid")


def test_product_projections_get_by_key(client):
    product_create = client.products.create(
        types.ProductDraft(key="test-product1", publish=False)
    )
    product = client.product_projections.get_by_key(product_create.key)
    assert product.id == product_create.id
    assert product.key == product_create.key


def test_product_projections_get_by_key_not_found(client):
    with pytest.raises(HTTPError):
        client.products.get_by_key("invalid")


def test_product_projections_query(client):
    for key in ["product-1", "product-2"]:
        client.products.create(types.ProductDraft(key=key, publish=True))
    client.products.create(types.ProductDraft(key="product-3", publish=False))

    # single sort query
    result = client.product_projections.query(
        sort="id asc", where=[f'slug(nl-NL="product-3")'], expand=["parent.category"]
    )
    assert len(result.results) == 2
    assert result.total == 2
    assert result.results[0].key == "product-1"
    assert result.results[1].key == "product-2"

    # multiple sort queries
    result = client.product_projections.query(sort=["id asc", "name asc"])
    assert len(result.results) == 2
    assert result.total == 2
