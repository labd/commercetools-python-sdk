import pytest

from commercetools.client import Client


@pytest.fixture()
def client_environment_settings(monkeypatch):
    monkeypatch.setenv("CTP_PROJECT_KEY", "project_key")
    monkeypatch.setenv("CTP_CLIENT_ID", "client_id")
    monkeypatch.setenv("CTP_CLIENT_SECRET", "client_secret")
    monkeypatch.setenv("CTP_CLIENT_SCOPES", "some_scope")
    monkeypatch.setenv("CTP_API_URL", "https://api.shere.io")
    monkeypatch.setenv("CTP_AUTH_URL", "https://auth.sphere.io")


def test_client_with_environment_settings_is_setup(client_environment_settings, commercetools_api):
    Client()
    assert len(commercetools_api.requests_mock.request_history) == 1

