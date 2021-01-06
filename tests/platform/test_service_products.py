import uuid

import pytest
import requests_mock
from requests.exceptions import HTTPError

from commercetools.platform import models
from commercetools.platform.client import Client


def test_products_create(old_client):
    custom_type = old_client.types.create(
        models.TypeDraft(
            name=models.LocalizedString(en="myType"),
            key="my-type",
            resource_type_ids=[models.ResourceTypeId.ASSET],
            field_definitions=[
                models.FieldDefinition(
                    name="foo",
                    type=models.CustomFieldStringType(),
                    label=models.LocalizedString(en="foo"),
                    required=False,
                )
            ],
        )
    )
    assert custom_type.id

    draft = models.ProductDraft(
        key="test-product",
        publish=True,
        name=models.LocalizedString(en=f"my-product"),
        slug=models.LocalizedString(en=f"my-product"),
        product_type=models.ProductTypeResourceIdentifier(key="dummy"),
        master_variant=models.ProductVariantDraft(
            assets=[
                models.AssetDraft(
                    sources=[],
                    name=models.LocalizedString(en="something"),
                    custom=models.CustomFieldsDraft(
                        type=models.TypeResourceIdentifier(id=custom_type.id),
                        fields=models.FieldContainer(foo="bar"),
                    ),
                )
            ],
            prices=[
                models.PriceDraft(
                    value=models.CentPrecisionMoneyDraft(
                        cent_amount=1000, currency_code="EUR"
                    ),
                    country="NL",
                )
            ],
        ),
    )
    product = old_client.products.create(draft)
    assert product.id
    assert product.master_data.current.master_variant.assets
    assert product.master_data.current.master_variant.prices


def test_products_get_by_id(old_client):
    product = old_client.products.create(
        models.ProductDraft(
            key="test-product",
            product_type=models.ProductTypeResourceIdentifier(key="dummy"),
            name=models.LocalizedString(en="my-product"),
            slug=models.LocalizedString(en="my-product"),
            publish=True,
        )
    )

    assert product.id
    assert product.key == "test-product"

    product = old_client.products.get_by_id(product.id)
    assert product.id
    assert product.key == "test-product"

    with pytest.raises(HTTPError) as e:
        old_client.products.get_by_id("invalid")


def test_products_get_by_key(old_client):
    product = old_client.products.create(
        models.ProductDraft(
            key="test-product",
            product_type=models.ProductTypeResourceIdentifier(key="dummy"),
            name=models.LocalizedString(en="my-product"),
            slug=models.LocalizedString(en="my-product"),
            publish=True,
        )
    )

    assert product.id
    assert product.key == "test-product"

    product = old_client.products.get_by_key("test-product")
    assert product.id
    assert product.key == "test-product"

    with pytest.raises(HTTPError) as e:
        old_client.products.get_by_key("invalid")


def test_product_query(old_client):
    old_client.products.create(
        models.ProductDraft(
            key=f"product-1",
            product_type=models.ProductTypeResourceIdentifier(key="dummy"),
            name=models.LocalizedString(en=f"my-product-1"),
            slug=models.LocalizedString(en=f"my-product-1"),
            publish=True,
        )
    )
    old_client.products.create(
        models.ProductDraft(
            key=f"product-2",
            product_type=models.ProductTypeResourceIdentifier(key="dummy"),
            name=models.LocalizedString(en=f"my-product-2"),
            slug=models.LocalizedString(en=f"my-product-2"),
            publish=True,
        )
    )

    # single sort query
    result = old_client.products.query(sort="id asc", limit=2)
    assert len(result.results) == 2
    assert result.total == 2

    # multiple sort queries
    result = old_client.products.query(sort=["id asc", "name asc"])
    assert len(result.results) == 2
    assert result.total == 2


def test_product_query_where(ct_platform_client: Client):
    product_client = ct_platform_client.with_project_key("test").products()
    product_client.post(
        models.ProductDraft(
            key="test-product1",
            name=models.LocalizedString(en=f"my-product-1"),
            slug=models.LocalizedString(en=f"my-product-1"),
            product_type=models.ProductTypeResourceIdentifier(key="dummy"),
            master_variant=models.ProductVariantDraft(
                prices=[
                    models.PriceDraft(
                        country="NL",
                        value=models.CentPrecisionMoneyDraft(
                            cent_amount=8750, currency_code="EUR"
                        ),
                    )
                ]
            ),
        )
    )
    product_client.post(
        models.ProductDraft(
            key="test-product-2",
            name=models.LocalizedString(en=f"my-product-1"),
            slug=models.LocalizedString(en=f"my-product-1"),
            product_type=models.ProductTypeResourceIdentifier(key="dummy"),
            master_variant=models.ProductVariantDraft(
                prices=[
                    models.PriceDraft(
                        country="UK",
                        value=models.CentPrecisionMoneyDraft(
                            cent_amount=8750, currency_code="EUR"
                        ),
                    )
                ]
            ),
        )
    )
    product_client.post(
        models.ProductDraft(
            key="test-product2",
            name=models.LocalizedString(en=f"my-product-1"),
            slug=models.LocalizedString(en=f"my-product-1"),
            product_type=models.ProductTypeResourceIdentifier(key="dummy"),
        )
    )

    result = product_client.get(
        where="masterData(staged(masterVariant(prices(country='NL'))))"
    )
    assert len(result.results) == 1
    assert result.total == 1

    result = product_client.get(
        where="masterData(staged(masterVariant(prices(country='UK'))))"
    )
    assert len(result.results) == 1
    assert result.total == 1

    result = product_client.get(
        where="masterData(staged(masterVariant(prices(country='UK' or country='NL'))))"
    )
    assert len(result.results) == 2
    assert result.total == 2


def test_product_update(old_client):
    """Test the return value of the update methods.

    It doesn't test the actual update itself.
    TODO: See if this is worth testing since we're using a mocking backend
    """
    product = old_client.products.create(
        models.ProductDraft(
            key="test-product",
            name=models.LocalizedString(en=f"my-product-1"),
            slug=models.LocalizedString(en=f"my-product-1"),
            product_type=models.ProductTypeResourceIdentifier(key="dummy"),
            master_variant=models.ProductVariantDraft(sku="1", key="1"),
        )
    )

    assert uuid.UUID(product.id)
    assert product.key == "test-product"

    product = old_client.products.update_by_id(
        id=product.id,
        version=product.version,
        actions=[
            models.ProductChangeSlugAction(slug=models.LocalizedString(nl="nl-slug2"))
        ],
    )
    assert product.key == "test-product"
    assert product.master_data.published is False

    product = old_client.products.update_by_id(
        id=product.id, version=product.version, actions=[models.ProductPublishAction()]
    )
    assert product.master_data.published is True

    assert not product.master_data.current.master_variant.prices
    product = old_client.products.update_by_id(
        id=product.id,
        version=product.version,
        actions=[
            models.ProductSetPricesAction(
                sku="1",
                prices=[
                    models.PriceDraft(
                        value=models.Money(cent_amount=1000, currency_code="GBP")
                    )
                ],
                staged=False,
            )
        ],
    )

    assert len(product.master_data.current.master_variant.prices) == 1

    product = old_client.products.update_by_key(
        key="test-product",
        version=product.version,
        actions=[
            models.ProductChangeSlugAction(slug=models.LocalizedString(nl="nl-slug2"))
        ],
    )
    assert product.key == "test-product"


def test_product_update_add_change_price_staged(old_client):
    product = old_client.products.create(
        models.ProductDraft(
            key="test-product",
            name=models.LocalizedString(en=f"my-product-1"),
            slug=models.LocalizedString(en=f"my-product-1"),
            product_type=models.ProductTypeResourceIdentifier(key="dummy"),
            master_variant=models.ProductVariantDraft(sku="1", key="1"),
        )
    )

    product = old_client.products.update_by_id(
        id=product.id,
        version=product.version,
        actions=[
            models.ProductAddPriceAction(
                sku="1",
                price=models.PriceDraft(
                    value=models.Money(cent_amount=1000, currency_code="GBP")
                ),
            )
        ],
    )

    assert product.master_data.current is None
    assert len(product.master_data.staged.master_variant.prices) == 1
    price = product.master_data.staged.master_variant.prices[0]
    assert price.value.cent_amount == 1000
    assert price.value.currency_code == "GBP"

    product = old_client.products.update_by_id(
        id=product.id,
        version=product.version,
        actions=[
            models.ProductChangePriceAction(
                price_id=price.id,
                price=models.PriceDraft(
                    value=models.Money(cent_amount=3000, currency_code="EUR")
                ),
            )
        ],
    )

    assert product.master_data.current is None
    assert len(product.master_data.staged.master_variant.prices) == 1
    price = product.master_data.staged.master_variant.prices[0]
    assert price.value.cent_amount == 3000
    assert price.value.currency_code == "EUR"


def test_product_update_add_price_current(old_client):
    product = old_client.products.create(
        models.ProductDraft(
            key="test-product",
            name=models.LocalizedString(en=f"my-product-1"),
            slug=models.LocalizedString(en=f"my-product-1"),
            product_type=models.ProductTypeResourceIdentifier(key="dummy"),
            master_variant=models.ProductVariantDraft(sku="1", key="1"),
            publish=True,
        )
    )

    product = old_client.products.update_by_id(
        id=product.id,
        version=product.version,
        actions=[
            models.ProductAddPriceAction(
                sku="1",
                staged=False,
                price=models.PriceDraft(
                    value=models.Money(cent_amount=1000, currency_code="GBP")
                ),
            )
        ],
    )

    assert product.master_data.staged is None
    assert len(product.master_data.current.master_variant.prices) == 1


def test_predicate_var(old_client):
    with requests_mock.Mocker(real_http=True, case_sensitive=True) as m:

        result = old_client.products.query(
            where="masterData(staged(masterVariant(prices(country='NL'))))",
            predicate_var={"foo": "bar"},
        )

        assert "var.foo" in m.request_history[0].qs
