import pytest

from commercetools.contrib.pytest import commercetools_api

# Tricks flake8 into silencing redefining fixtures warnings.
__all__ = ["commercetools_api"]


@pytest.fixture(autouse=True)
def reset_token_cache():
    from commercetools.utils import DefaultTokenSaver
    DefaultTokenSaver.clear_cache()
