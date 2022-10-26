import pytest
from requests.exceptions import HTTPError

from commercetools.platform import models
from commercetools.platform.client import Client


def test_shipping_method_with_id_get(ct_platform_client: Client):
    shipping_method = (
        ct_platform_client.with_project_key("unittest")
        .shipping_methods()
        .post(
            models.ShippingMethodDraft(
                key="test-shipping-method",
                name="test shipping method",
                tax_category=models.TaxCategoryResourceIdentifier(id="dummy"),
                zone_rates=[],
                is_default=False,
            )
        )
    )
    assert shipping_method
    assert shipping_method.id
    assert shipping_method.key == "test-shipping-method"
    assert shipping_method.name == "test shipping method"

    shipping_method = (
        ct_platform_client.with_project_key("unittest")
        .shipping_methods()
        .with_id(shipping_method.id)
        .get()
    )
    assert shipping_method
    assert shipping_method.id
    assert shipping_method.key == "test-shipping-method"

    with pytest.raises(HTTPError):
        ct_platform_client.with_project_key("unittest").shipping_methods().with_id(
            "invalid"
        ).get()


def test_shipping_method_query(ct_platform_client: Client):
    ct_platform_client.with_project_key("unittest").shipping_methods().post(
        models.ShippingMethodDraft(
            key="test-shipping_method1",
            name="test shipping method1",
            tax_category=models.TaxCategoryResourceIdentifier(id="dummy"),
            zone_rates=[],
            is_default=False,
        )
    )
    ct_platform_client.with_project_key("unittest").shipping_methods().post(
        models.ShippingMethodDraft(
            key="test-shipping_method2",
            name="test shipping method2",
            tax_category=models.TaxCategoryResourceIdentifier(id="dummy"),
            zone_rates=[],
            is_default=False,
        )
    )

    # single sort query
    result = (
        ct_platform_client.with_project_key("unittest")
        .shipping_methods()
        .get(sort="id asc")
    )
    assert len(result.results) == 2
    assert result.total == 2

    # multiple sort queries
    result = (
        ct_platform_client.with_project_key("unittest")
        .shipping_methods()
        .get(sort=["id asc", "name asc"])
    )
    assert len(result.results) == 2
    assert result.total == 2


def test_shipping_method_update(ct_platform_client: Client):
    """Test the return value of the update methods.

    It doesn't test the actual update itself.
    TODO: See if this is worth testing since we're using a mocking backend
    """
    shipping_method = (
        ct_platform_client.with_project_key("unittest")
        .shipping_methods()
        .post(
            models.ShippingMethodDraft(
                key="test-shipping-method",
                name="test shipping method",
                tax_category=models.TaxCategoryResourceIdentifier(id="dummy"),
                zone_rates=[],
                is_default=False,
            )
        )
    )
    assert shipping_method.key == "test-shipping-method"

    shipping_method = (
        ct_platform_client.with_project_key("unittest")
        .shipping_methods()
        .with_id(shipping_method.id)
        .post(
            models.ShippingMethodUpdate(
                version=shipping_method.version,
                actions=[
                    models.ShippingMethodChangeNameAction(name="shipping-method-2")
                ],
            )
        )
    )

    assert shipping_method.key == "test-shipping-method"


def test_shipping_method_update_two(ct_platform_client: Client):
    shipping_method = (
        ct_platform_client.with_project_key("unittest")
        .shipping_methods()
        .post(
            models.ShippingMethodDraft(
                key="test-shipping-method",
                name="test shipping method",
                tax_category=models.TaxCategoryResourceIdentifier(id="dummy"),
                zone_rates=[],
                is_default=False,
            )
        )
    )

    assert shipping_method.id
    assert shipping_method.localized_description is None

    shipping_method = (
        ct_platform_client.with_project_key("unittest")
        .shipping_methods()
        .with_id(shipping_method.id)
        .post(
            models.ShippingMethodUpdate(
                version=shipping_method.version,
                actions=[
                    models.ShippingMethodSetLocalizedDescriptionAction(
                        localized_description=models.LocalizedString(
                            {"en": "a new lstring"}
                        )
                    )
                ],
            )
        )
    )

    assert shipping_method.localized_description == models.LocalizedString(
        {"en": "a new lstring"}
    )
