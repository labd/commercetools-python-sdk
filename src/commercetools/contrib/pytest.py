import pytest

from commercetools import Client
from commercetools.testing import backend_mocker


@pytest.fixture()
def commercetools_api():
    with backend_mocker() as m:
        yield m


@pytest.fixture
def commercetools_client(commercetools_api) -> Client:
    yield Client(
        project_key="unittest",
        client_id="client-id",
        client_secret="client-secret",
        scope=[],
        url="https://api.sphere.io",
        token_url="https://auth.sphere.io",
    )
