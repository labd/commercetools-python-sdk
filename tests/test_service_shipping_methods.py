import pytest
from requests.exceptions import HTTPError

from commercetools import types


def test_shipping_method_get_by_id(client):
    shipping_method = client.shipping_methods.create(
        types.ShippingMethodDraft(
            key="test-shipping-method", name="test shipping method"
        )
    )

    assert shipping_method.id
    assert shipping_method.key == "test-shipping-method"
    assert shipping_method.name == "test shipping method"

    shipping_method = client.shipping_methods.get_by_id(shipping_method.id)
    assert shipping_method.id
    assert shipping_method.key == "test-shipping-method"

    with pytest.raises(HTTPError):
        client.shipping_methods.get_by_id("invalid")


def test_shipping_method_query(client):
    client.shipping_methods.create(
        types.ShippingMethodDraft(
            key="test-shipping_method1", name="test shipping method1"
        )
    )
    client.shipping_methods.create(
        types.ShippingMethodDraft(
            key="test-shipping_method2", name="test shipping method2"
        )
    )

    # single sort query
    result = client.shipping_methods.query(sort="id asc")
    assert len(result.results) == 2
    assert result.total == 2

    # multiple sort queries
    result = client.shipping_methods.query(sort=["id asc", "name asc"])
    assert len(result.results) == 2
    assert result.total == 2


def test_shipping_method_update(client):
    """Test the return value of the update methods.

    It doesn't test the actual update itself.
    TODO: See if this is worth testing since we're using a mocking backend
    """
    shipping_method = client.shipping_methods.create(
        types.ShippingMethodDraft(
            key="test-shipping-method", name="test shipping method"
        )
    )
    assert shipping_method.key == "test-shipping-method"

    shipping_method = client.shipping_methods.update_by_id(
        id=shipping_method.id,
        version=shipping_method.version,
        actions=[types.ShippingMethodChangeNameAction(name="shipping-method-2")],
    )

    assert shipping_method.key == "test-shipping-method"
