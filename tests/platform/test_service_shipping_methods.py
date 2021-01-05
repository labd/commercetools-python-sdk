import pytest
from requests.exceptions import HTTPError

from commercetools.platform import models


def test_shipping_method_get_by_id(old_client):
    shipping_method = old_client.shipping_methods.create(
        models.ShippingMethodDraft(
            key="test-shipping-method",
            name="test shipping method",
            tax_category=models.TaxCategoryResourceIdentifier(id="dummy"),
            zone_rates=[],
            is_default=False,
        )
    )

    assert shipping_method.id
    assert shipping_method.key == "test-shipping-method"
    assert shipping_method.name == "test shipping method"

    shipping_method = old_client.shipping_methods.get_by_id(shipping_method.id)
    assert shipping_method.id
    assert shipping_method.key == "test-shipping-method"

    with pytest.raises(HTTPError):
        old_client.shipping_methods.get_by_id("invalid")


def test_shipping_method_query(old_client):
    old_client.shipping_methods.create(
        models.ShippingMethodDraft(
            key="test-shipping_method1",
            name="test shipping method1",
            tax_category=models.TaxCategoryResourceIdentifier(id="dummy"),
            zone_rates=[],
            is_default=False,
        )
    )
    old_client.shipping_methods.create(
        models.ShippingMethodDraft(
            key="test-shipping_method2",
            name="test shipping method2",
            tax_category=models.TaxCategoryResourceIdentifier(id="dummy"),
            zone_rates=[],
            is_default=False,
        )
    )

    # single sort query
    result = old_client.shipping_methods.query(sort="id asc")
    assert len(result.results) == 2
    assert result.total == 2

    # multiple sort queries
    result = old_client.shipping_methods.query(sort=["id asc", "name asc"])
    assert len(result.results) == 2
    assert result.total == 2


def test_shipping_method_update(old_client):
    """Test the return value of the update methods.

    It doesn't test the actual update itself.
    TODO: See if this is worth testing since we're using a mocking backend
    """
    shipping_method = old_client.shipping_methods.create(
        models.ShippingMethodDraft(
            key="test-shipping-method",
            name="test shipping method",
            tax_category=models.TaxCategoryResourceIdentifier(id="dummy"),
            zone_rates=[],
            is_default=False,
        )
    )
    assert shipping_method.key == "test-shipping-method"

    shipping_method = old_client.shipping_methods.update_by_id(
        id=shipping_method.id,
        version=shipping_method.version,
        actions=[models.ShippingMethodChangeNameAction(name="shipping-method-2")],
    )

    assert shipping_method.key == "test-shipping-method"
