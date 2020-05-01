import uuid

import pytest
from requests.exceptions import HTTPError

from commercetools import types


def test_products_create(client):
    custom_type = client.types.create(
        types.TypeDraft(
            name=types.LocalizedString(en="myType"),
            resource_type_ids=[types.ResourceTypeId.ASSET],
            field_definitions=[types.FieldDefinition(name="foo")],
        )
    )
    assert custom_type.id

    draft = types.ProductDraft(
        key="test-product",
        publish=True,
        master_variant=types.ProductVariantDraft(
            assets=[
                types.AssetDraft(
                    custom=types.CustomFieldsDraft(
                        type=types.TypeResourceIdentifier(id=custom_type.id),
                        fields=types.FieldContainer(foo="bar"),
                    )
                )
            ],
            prices=[
                types.PriceDraft(
                    value=types.CentPrecisionMoneyDraft(
                        cent_amount=1000, currency_code="EUR"
                    ),
                    country="NL",
                )
            ],
        ),
    )
    product = client.products.create(draft)
    assert product.id
    assert product.master_data.current.master_variant.assets
    assert product.master_data.current.master_variant.prices


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


def test_product_query_where(client):
    client.products.create(
        types.ProductDraft(
            key="test-product1",
            master_variant=types.ProductVariantDraft(
                prices=[
                    types.PriceDraft(
                        country="NL",
                        value=types.CentPrecisionMoneyDraft(
                            cent_amount=8750, currency_code="EUR"
                        ),
                    )
                ]
            ),
        )
    )
    client.products.create(
        types.ProductDraft(
            key="test-product-2",
            master_variant=types.ProductVariantDraft(
                prices=[
                    types.PriceDraft(
                        country="UK",
                        value=types.CentPrecisionMoneyDraft(
                            cent_amount=8750, currency_code="EUR"
                        ),
                    )
                ]
            ),
        )
    )
    client.products.create(types.ProductDraft(key="test-product2"))

    result = client.products.query(
        where="masterData(staged(masterVariant(prices(country='NL'))))"
    )
    assert len(result.results) == 1
    assert result.total == 1

    result = client.products.query(
        where="masterData(staged(masterVariant(prices(country='UK'))))"
    )
    assert len(result.results) == 1
    assert result.total == 1

    result = client.products.query(
        where="masterData(staged(masterVariant(prices(country='UK' or country='NL'))))"
    )
    assert len(result.results) == 2
    assert result.total == 2


def test_product_update(client):
    """Test the return value of the update methods.

    It doesn't test the actual update itself.
    TODO: See if this is worth testing since we're using a mocking backend
    """
    product = client.products.create(
        types.ProductDraft(
            key="test-product",
            master_variant=types.ProductVariantDraft(sku="1", key="1"),
        )
    )

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
    assert product.master_data.published is False

    product = client.products.update_by_id(
        id=product.id, version=product.version, actions=[types.ProductPublishAction()]
    )
    assert product.master_data.published is True

    assert not product.master_data.current.master_variant.prices
    product = client.products.update_by_id(
        id=product.id,
        version=product.version,
        actions=[
            types.ProductSetPricesAction(
                sku="1",
                prices=[
                    types.PriceDraft(
                        value=types.Money(cent_amount=1000, currency_code="GBP")
                    )
                ],
                staged=False,
            )
        ],
    )

    assert len(product.master_data.current.master_variant.prices) == 1

    product = client.products.update_by_key(
        key="test-product",
        version=product.version,
        actions=[
            types.ProductChangeSlugAction(slug=types.LocalizedString(nl="nl-slug2"))
        ],
    )
    assert product.key == "test-product"
