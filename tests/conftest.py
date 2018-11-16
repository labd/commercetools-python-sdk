import pytest

from commercetools import Client
from commercetools.contrib.pytest import commercetools_api
from commercetools.testing import backend_mocker

# Tricks flake8 into silencing redefining fixtures warnings.
__all__ = ["commercetools_api"]


@pytest.fixture(autouse=True)
def reset_token_cache():
    from commercetools.utils import DefaultTokenSaver

    DefaultTokenSaver.clear_cache()


@pytest.fixture
def client():
    with backend_mocker():
        yield Client(
            project_key="unittest",
            client_id="client-id",
            client_secret="client-secret",
            scope=[],
            url="https://api.sphere.io",
            token_url="https://auth.sphere.io",
        )
