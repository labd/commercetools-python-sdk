import pytest

from commercetools.platform import models


def test_api_client_flow(old_client, api_client_draft):
    api_client = old_client.api_clients.create(api_client_draft)

    assert api_client.id

    deleted_api_client = old_client.api_clients.delete_by_id(api_client.id)

    assert api_client.id == deleted_api_client.id


@pytest.fixture
def api_client_draft():
    return models.ApiClientDraft(
        name="Test API Client", scope="manage_project:some_project_key"
    )
