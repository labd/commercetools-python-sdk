import time

import pytest
from freezegun import freeze_time

from commercetools.client import Client


@pytest.fixture()
def client_environment_settings(monkeypatch):
    monkeypatch.setenv("CTP_PROJECT_KEY", "project_key")
    monkeypatch.setenv("CTP_CLIENT_ID", "client_id")
    monkeypatch.setenv("CTP_CLIENT_SECRET", "client_secret")
    monkeypatch.setenv("CTP_CLIENT_SCOPES", "some_scope")
    monkeypatch.setenv("CTP_API_URL", "https://api.shere.io")
    monkeypatch.setenv("CTP_AUTH_URL", "https://auth.sphere.io/oauth/token")


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
