import threading
import time
import typing

import pytest
import requests

from commercetools import Client
from commercetools.testing import backend_mocker
from commercetools.testing.server import Server


@pytest.fixture(autouse=True)
def reset_token_cache():
    from commercetools.utils import DefaultTokenSaver

    DefaultTokenSaver.clear_cache()


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
    is_running = threading.Event()
    server = Server(commercetools_api)

    def serve():
        from werkzeug.serving import run_simple

        is_running.set()
        server.api_url = "http://localhost:8989"
        run_simple("localhost", port=8989, application=server)

    thread = threading.Thread(target=serve, daemon=True)
    thread.start()

    if is_running.wait():
        for i in range(0, 5):
            response = requests.get(server.api_url + "/-/health")
            if response.status_code == 200:
                break
            time.sleep(0.5)

        yield server

    thread.join(timeout=0)
