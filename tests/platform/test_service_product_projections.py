import pytest
from requests.exceptions import HTTPError

from commercetools.platform import models
from commercetools.platform.client import Client


def test_product_projections_with_id_get(ct_platform_client: Client):
    variant = models.ProductVariantDraft()
    product_create = (
        ct_platform_client.with_project_key("unittest")
        .products()
        .post(
            models.ProductDraft(
                key="test-product",
                product_type=models.ProductTypeResourceIdentifier(key="dummy"),
                name=models.LocalizedString(en=f"my-product"),
                slug=models.LocalizedString(en=f"my-product"),
                master_variant=variant,
                variants=[variant],
                publish=False,
            )
        )
    )

    product = (
        ct_platform_client.with_project_key("unittest")
        .product_projections()
        .with_id(product_create.id)
        .get(staged=True)
    )
    assert product
    assert product.id == product_create.id
    assert product.key == product_create.key


def test_product_projections_get_by_id_not_found(ct_platform_client: Client):
    with pytest.raises(HTTPError):
        ct_platform_client.with_project_key("unittest").products().with_id(
            "invalid"
        ).get()


def test_product_projections_get_by_key(ct_platform_client: Client):
    variant = models.ProductVariantDraft()
    product_create = (
        ct_platform_client.with_project_key("unittest")
        .products()
        .post(
            models.ProductDraft(
                key="test-product",
                product_type=models.ProductTypeResourceIdentifier(key="dummy"),
                name=models.LocalizedString(en=f"my-product"),
                slug=models.LocalizedString(en=f"my-product"),
                master_variant=variant,
                variants=[variant],
                publish=False,
            )
        )
    )
    product = (
        ct_platform_client.with_project_key("unittest")
        .product_projections()
        .with_key(product_create.key)
        .get(staged=True)
    )
    assert product
    assert product.id == product_create.id
    assert product.key == product_create.key


def test_product_projections_query_parameters_are_passed(
    ct_platform_client: Client, commercetools_api
):
    ct_platform_client.with_project_key("unittest").products().get(
        expand="productType", price_country="GB", price_currency="GBP"
    )

    last_request = commercetools_api.requests_mock.request_history[-1]

    for field in ["expand", "priceCurrency", "priceCountry"]:
        assert field in last_request.qs


def test_product_projections_get_by_key_not_found(ct_platform_client: Client):
    with pytest.raises(HTTPError):
        ct_platform_client.with_project_key("unittest").products().with_id(
            "invalid"
        ).get()


def test_product_projections_query(ct_platform_client: Client):
    client = ct_platform_client.with_project_key("unittest")

    for key in ["product-1", "product-2"]:
        variant = models.ProductVariantDraft()
        client.products().post(
            models.ProductDraft(
                key=key,
                product_type=models.ProductTypeResourceIdentifier(key="dummy"),
                name=models.LocalizedString(en=key),
                slug=models.LocalizedString(en=key),
                master_variant=variant,
                variants=[variant],
                publish=True,
            )
        )

    key = "product-3"
    client.products().post(
        models.ProductDraft(
            key=key,
            product_type=models.ProductTypeResourceIdentifier(key="dummy"),
            name=models.LocalizedString(en=key),
            slug=models.LocalizedString(en=key),
            master_variant=variant,
            variants=[variant],
            publish=False,
        )
    )

    # single sort query
    result = client.product_projections().get(
        sort="id asc", where=[f'slug(nl-NL="product-3")'], expand=["parent.category"]
    )
    assert result
    assert len(result.results) == 2
    assert result.total == 2
    assert result.results[0].key == "product-1"
    assert result.results[1].key == "product-2"

    # multiple sort queries
    result = client.product_projections().get(sort=["id asc", "name asc"])
    assert len(result.results) == 2
    assert result.total == 2
