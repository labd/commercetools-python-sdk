import uuid

import pytest
import requests_mock
from requests.exceptions import HTTPError

from commercetools import types


def test_products_create(client):
    custom_type = client.types.create(
        types.TypeDraft(
            name=types.LocalizedString(en="myType"),
            key="my-type",
            resource_type_ids=[types.ResourceTypeId.ASSET],
            field_definitions=[
                types.FieldDefinition(
                    name="foo",
                    type=types.CustomFieldStringType(),
                    label=types.LocalizedString(en="foo"),
                    required=False,
                )
            ],
        )
    )
    assert custom_type.id

    draft = types.ProductDraft(
        key="test-product",
        publish=True,
        name=types.LocalizedString(en=f"my-product"),
        slug=types.LocalizedString(en=f"my-product"),
        product_type=types.ProductTypeResourceIdentifier(key="dummy"),
        master_variant=types.ProductVariantDraft(
            assets=[
                types.AssetDraft(
                    sources=[],
                    name=types.LocalizedString(en="something"),
                    custom=types.CustomFieldsDraft(
                        type=types.TypeResourceIdentifier(id=custom_type.id),
                        fields=types.FieldContainer(foo="bar"),
                    ),
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
    product = client.products.create(
        types.ProductDraft(
            key="test-product",
            product_type=types.ProductTypeResourceIdentifier(key="dummy"),
            name=types.LocalizedString(en="my-product"),
            slug=types.LocalizedString(en="my-product"),
            publish=True,
        )
    )

    assert product.id
    assert product.key == "test-product"

    product = client.products.get_by_id(product.id)
    assert product.id
    assert product.key == "test-product"

    with pytest.raises(HTTPError) as e:
        client.products.get_by_id("invalid")


def test_products_get_by_key(client):
    product = client.products.create(
        types.ProductDraft(
            key="test-product",
            product_type=types.ProductTypeResourceIdentifier(key="dummy"),
            name=types.LocalizedString(en="my-product"),
            slug=types.LocalizedString(en="my-product"),
            publish=True,
        )
    )

    assert product.id
    assert product.key == "test-product"

    product = client.products.get_by_key("test-product")
    assert product.id
    assert product.key == "test-product"

    with pytest.raises(HTTPError) as e:
        client.products.get_by_key("invalid")


def test_product_query(client):
    client.products.create(
        types.ProductDraft(
            key=f"product-1",
            product_type=types.ProductTypeResourceIdentifier(key="dummy"),
            name=types.LocalizedString(en=f"my-product-1"),
            slug=types.LocalizedString(en=f"my-product-1"),
            publish=True,
        )
    )
    client.products.create(
        types.ProductDraft(
            key=f"product-2",
            product_type=types.ProductTypeResourceIdentifier(key="dummy"),
            name=types.LocalizedString(en=f"my-product-2"),
            slug=types.LocalizedString(en=f"my-product-2"),
            publish=True,
        )
    )

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
            name=types.LocalizedString(en=f"my-product-1"),
            slug=types.LocalizedString(en=f"my-product-1"),
            product_type=types.ProductTypeResourceIdentifier(key="dummy"),
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
            name=types.LocalizedString(en=f"my-product-1"),
            slug=types.LocalizedString(en=f"my-product-1"),
            product_type=types.ProductTypeResourceIdentifier(key="dummy"),
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
    client.products.create(
        types.ProductDraft(
            key="test-product2",
            name=types.LocalizedString(en=f"my-product-1"),
            slug=types.LocalizedString(en=f"my-product-1"),
            product_type=types.ProductTypeResourceIdentifier(key="dummy"),
        )
    )

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
            name=types.LocalizedString(en=f"my-product-1"),
            slug=types.LocalizedString(en=f"my-product-1"),
            product_type=types.ProductTypeResourceIdentifier(key="dummy"),
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


def test_product_update_add_change_price_staged(client):
    product = client.products.create(
        types.ProductDraft(
            key="test-product",
            name=types.LocalizedString(en=f"my-product-1"),
            slug=types.LocalizedString(en=f"my-product-1"),
            product_type=types.ProductTypeResourceIdentifier(key="dummy"),
            master_variant=types.ProductVariantDraft(sku="1", key="1"),
        )
    )

    product = client.products.update_by_id(
        id=product.id,
        version=product.version,
        actions=[
            types.ProductAddPriceAction(
                sku="1",
                price=types.PriceDraft(
                    value=types.Money(cent_amount=1000, currency_code="GBP")
                ),
            )
        ],
    )

    assert product.master_data.current is None
    assert len(product.master_data.staged.master_variant.prices) == 1
    price = product.master_data.staged.master_variant.prices[0]
    assert price.value.cent_amount == 1000
    assert price.value.currency_code == "GBP"

    product = client.products.update_by_id(
        id=product.id,
        version=product.version,
        actions=[
            types.ProductChangePriceAction(
                price_id=price.id,
                price=types.PriceDraft(
                    value=types.Money(cent_amount=3000, currency_code="EUR")
                ),
            )
        ],
    )

    assert product.master_data.current is None
    assert len(product.master_data.staged.master_variant.prices) == 1
    price = product.master_data.staged.master_variant.prices[0]
    assert price.value.cent_amount == 3000
    assert price.value.currency_code == "EUR"


def test_product_update_add_price_current(client):
    product = client.products.create(
        types.ProductDraft(
            key="test-product",
            name=types.LocalizedString(en=f"my-product-1"),
            slug=types.LocalizedString(en=f"my-product-1"),
            product_type=types.ProductTypeResourceIdentifier(key="dummy"),
            master_variant=types.ProductVariantDraft(sku="1", key="1"),
            publish=True,
        )
    )

    product = client.products.update_by_id(
        id=product.id,
        version=product.version,
        actions=[
            types.ProductAddPriceAction(
                sku="1",
                staged=False,
                price=types.PriceDraft(
                    value=types.Money(cent_amount=1000, currency_code="GBP")
                ),
            )
        ],
    )

    assert product.master_data.staged is None
    assert len(product.master_data.current.master_variant.prices) == 1


def test_predicate_var(client):
    with requests_mock.Mocker(real_http=True, case_sensitive=True) as m:

        result = client.products.query(
            where="masterData(staged(masterVariant(prices(country='NL'))))",
            predicate_var={"foo": "bar"},
        )

        assert "var.foo" in m.request_history[0].qs
