import pytest
from requests.exceptions import HTTPError


def test_product_projections_get_by_id(client):
    product = client.product_projections.get_by_id("0001")
    assert product.id == "0001"
    assert product.key == "product-1"

    with pytest.raises(HTTPError) as e:
        client.products.get_by_id("invalid")


def test_product_projections_get_by_key(client):
    product = client.product_projections.get_by_key("product-1")
    assert product.id == "0001"
    assert product.key == "product-1"

    with pytest.raises(HTTPError) as e:
        client.products.get_by_key("invalid")


def test_product_projections_query(client):
    # single sort query
    result = client.product_projections.query(sort="id asc")
    assert len(result.results) == 2
    assert result.total == 2

    # multiple sort queries
    result = client.product_projections.query(sort=["id asc", "name asc"])
    assert len(result.results) == 2
    assert result.total == 2
