import threading
import typing

import pytest

from commercetools import Client
from commercetools.testing import backend_mocker
from commercetools.testing.server import Server


@pytest.fixture()
def commercetools_api():
    with backend_mocker() as m:
        yield m


@pytest.fixture
def commercetools_client(commercetools_api) -> typing.Generator[Client, None, None]:
    yield Client(
        project_key="unittest",
        client_id="client-id",
        client_secret="client-secret",
        scope=[],
        url="https://api.sphere.io",
        token_url="https://auth.sphere.io/oauth/token",
    )


@pytest.fixture()
def commercetools_http_server(commercetools_api):
    server = Server(commercetools_api)
    thread = threading.Thread(target=server.run, daemon=True)
    thread.start()

    if server.is_running.wait():
        yield server

    thread.join(timeout=0)
