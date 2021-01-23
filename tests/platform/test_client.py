import time
import uuid

import pytest
from requests_mock.adapter import Adapter

from commercetools import CommercetoolsError
from commercetools.client import Client
from commercetools.platform import models


@pytest.fixture()
def client_environment_settings(monkeypatch):
    monkeypatch.setenv("CTP_PROJECT_KEY", "project_key")
    monkeypatch.setenv("CTP_CLIENT_ID", "client_id")
    monkeypatch.setenv("CTP_CLIENT_SECRET", "client_secret")
    monkeypatch.setenv("CTP_CLIENT_SCOPES", "some_scope")
    monkeypatch.setenv("CTP_API_URL", "https://api.shere.io")
    monkeypatch.setenv("CTP_AUTH_URL", "https://auth.sphere.io")


def test_client_with_environment_settings_is_setup(
    client_environment_settings, commercetools_api
):
    Client()
    assert len(commercetools_api.requests_mock.request_history) == 1


def test_auto_refresh(commercetools_api):
    commercetools_api.auth.set_expire_time(1)

    client = Client(
        client_id="unittest",
        client_secret="mysecret",
        project_key="test",
        url="https://api.sphere.io",
        token_url="https://auth.sphere.io/oauth/token",
    )
    client.products.query()
    time.sleep(1)
    client.products.query()
    client.products.query()

    auth_headers = set()
    for request in commercetools_api.requests_mock.request_history:
        if request.url.startswith("https://api.sphere.io/"):
            auth_headers.add(request.headers["Authorization"])

    assert len(auth_headers) == 2
    assert len(commercetools_api.auth.model.tokens) == 2


def test_cache_token(commercetools_api):
    Client(
        client_id="unittest",
        client_secret="none",
        project_key="test",
        url="https://api.sphere.io",
        token_url="https://auth.sphere.io/oauth/token",
    )
    assert len(commercetools_api.requests_mock.request_history) == 1

    Client(
        client_id="unittest",
        client_secret="none",
        project_key="test",
        url="https://api.sphere.io",
        token_url="https://auth.sphere.io/oauth/token",
    )
    assert len(commercetools_api.requests_mock.request_history) == 1


def test_allows_passing_custom_http_adapter():
    my_adapter = Adapter()
    my_adapter.register_uri(
        "POST",
        "https://auth.sphere.io/oauth/token",
        json=dict(access_token="my_mock_access_token"),
    )
    Client(
        client_id="unittest",
        client_secret="none",
        project_key="test",
        url="https://api.sphere.io",
        token_url="https://auth.sphere.io/oauth/token",
        http_adapter=my_adapter,
    )
    assert len(my_adapter.request_history) == 1


def test_resource_update_conflict(old_client):
    """Test the return value of the update methods.

    It doesn't test the actual update itself.
    TODO: See if this is worth testing since we're using a mocking backend
    """
    product = old_client.products.create(
        models.ProductDraft(
            key="test-product",
            product_type=models.ProductTypeResourceIdentifier(key="dummy"),
            name={"en": "my-product"},
            slug={"en": "foo-bar"},
        )
    )

    assert product.version == 1
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
    assert product.version == 2

    # This should raise a version conflict error
    with pytest.raises(CommercetoolsError) as exc:
        product = old_client.products.update_by_id(
            id=product.id,
            version=1,
            actions=[
                models.ProductChangeSlugAction(
                    slug=models.LocalizedString(nl="nl-slug3")
                )
            ],
        )
    assert exc.value.response.status_code == 409
    assert exc.value.response.errors[0].current_version == 2

    # Force it
    product = old_client.products.update_by_id(
        id=product.id,
        version=1,
        actions=[
            models.ProductChangeSlugAction(slug=models.LocalizedString(nl="nl-slug2"))
        ],
        force_update=True,
    )


def test_resource_delete_conflict(old_client):
    """Test the return value of the delete methods.

    It doesn't test the actual delete itself.
    TODO: See if this is worth testing since we're using a mocking backend
    """
    product = old_client.products.create(
        models.ProductDraft(
            key="test-product",
            product_type=models.ProductTypeResourceIdentifier(key="dummy"),
            name={"en": "my-product"},
            slug={"en": "foo-bar"},
        )
    )

    product = old_client.products.update_by_id(
        id=product.id,
        version=product.version,
        actions=[
            models.ProductChangeSlugAction(slug=models.LocalizedString(nl="nl-slug2"))
        ],
    )
    assert product.version == 2

    # This should raise a version conflict error
    with pytest.raises(CommercetoolsError) as exc:
        product = old_client.products.delete_by_id(id=product.id, version=1)

    assert exc.value.response.status_code == 409
    assert exc.value.response.errors[0].current_version == 2

    # Force it
    old_client.products.delete_by_id(id=product.id, version=1, force_delete=True)
