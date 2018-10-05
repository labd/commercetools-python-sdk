import pytest

from commercetools.testing import backend_mocker


@pytest.fixture()
def commercetools_api():
    with backend_mocker() as m:
        yield m
