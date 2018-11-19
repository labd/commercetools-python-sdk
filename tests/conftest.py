import pytest

# Tricks flake8 into silencing redefining fixtures warnings.
pytest_plugins = ["commercetools.contrib.pytest"]


@pytest.fixture(autouse=True)
def reset_token_cache():
    from commercetools.utils import DefaultTokenSaver

    DefaultTokenSaver.clear_cache()


@pytest.fixture
def client(commercetools_client):
    return commercetools_client
