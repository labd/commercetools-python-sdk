import pytest

from commercetools import types


def test_api_client_flow(client, api_client_draft):
    api_client = client.api_clients.create(api_client_draft)

    assert api_client.id

    deleted_api_client = client.api_clients.delete_by_id(api_client.id)

    assert api_client.id == deleted_api_client.id


@pytest.fixture
def api_client_draft():
    return types.ApiClientDraft(
        name="Test API Client", scope="manage_project:some_project_key"
    )
