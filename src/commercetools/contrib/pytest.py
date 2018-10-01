import pytest

from commercetools.testing import backend_mocker


@pytest.fixture()
def mock_backend():
    with backend_mocker() as m:
        yield m
