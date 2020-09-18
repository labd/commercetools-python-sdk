import pytest
from requests.exceptions import HTTPError

from commercetools import types


def test_product_projections_get_by_id(client):
    variant = types.ProductVariantDraft()
    product_create = client.products.create(
        types.ProductDraft(
            key="test-product",
            product_type=types.ProductTypeResourceIdentifier(key="dummy"),
            name=types.LocalizedString(en=f"my-product"),
            slug=types.LocalizedString(en=f"my-product"),
            master_variant=variant,
            variants=[variant],
            publish=False,
        )
    )

    product = client.product_projections.get_by_id(product_create.id, staged=True)
    assert product.id == product_create.id
    assert product.key == product_create.key


def test_product_projections_get_by_id_not_found(client):
    with pytest.raises(HTTPError):
        client.products.get_by_id("invalid")


def test_product_projections_get_by_key(client):
    variant = types.ProductVariantDraft()
    product_create = client.products.create(
        types.ProductDraft(
            key="test-product",
            product_type=types.ProductTypeResourceIdentifier(key="dummy"),
            name=types.LocalizedString(en=f"my-product"),
            slug=types.LocalizedString(en=f"my-product"),
            master_variant=variant,
            variants=[variant],
            publish=False,
        )
    )
    product = client.product_projections.get_by_key(product_create.key, staged=True)
    assert product.id == product_create.id
    assert product.key == product_create.key


def test_product_projections_query_parameters_are_passed(client, commercetools_api):
    client.products.query(
        expand="productType", price_country="GB", price_currency="GBP"
    )

    last_request = commercetools_api.requests_mock.request_history[-1]

    for field in ["expand", "priceCurrency", "priceCountry"]:
        assert field in last_request.qs


def test_product_projections_get_by_key_not_found(client):
    with pytest.raises(HTTPError):
        client.products.get_by_key("invalid")


def test_product_projections_query(client):
    for key in ["product-1", "product-2"]:
        variant = types.ProductVariantDraft()
        client.products.create(
            types.ProductDraft(
                key=key,
                product_type=types.ProductTypeResourceIdentifier(key="dummy"),
                name=types.LocalizedString(en=key),
                slug=types.LocalizedString(en=key),
                master_variant=variant,
                variants=[variant],
                publish=True,
            )
        )

    key = "product-3"
    client.products.create(
        types.ProductDraft(
            key=key,
            product_type=types.ProductTypeResourceIdentifier(key="dummy"),
            name=types.LocalizedString(en=key),
            slug=types.LocalizedString(en=key),
            master_variant=variant,
            variants=[variant],
            publish=False,
        )
    )

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
