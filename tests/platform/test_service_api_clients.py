import pytest

from commercetools.platform import models
from commercetools.platform.client import Client


def test_api_client_flow(ct_platform_client: Client, api_client_draft):
    api_client = (
        ct_platform_client.with_project_key("test").api_clients().post(api_client_draft)
    )

    assert api_client
    assert api_client.id

    deleted_api_client = (
        ct_platform_client.with_project_key("test")
        .api_clients()
        .with_id(api_client.id)
        .delete()
    )

    assert deleted_api_client
    assert api_client.id == deleted_api_client.id


@pytest.fixture
def api_client_draft():
    return models.ApiClientDraft(
        name="Test API Client", scope="manage_project:some_project_key"
    )
