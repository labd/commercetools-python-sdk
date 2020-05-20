import pytest

# Tricks flake8 into silencing redefining fixtures warnings.
pytest_plugins = ["commercetools.contrib.pytest"]


@pytest.fixture
def client(commercetools_client):
    return commercetools_client
