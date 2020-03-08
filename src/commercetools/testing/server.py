import logging
import typing

import requests
import webob
import webob.exc
from requests.packages.urllib3.response import HTTPResponse
from requests_mock.request import _RequestObjectProxy

from commercetools.testing import BackendRepository
from commercetools.testing.internal import InternalBackend

logger = logging.getLogger(__name__)


class HttpAdapter:
    def __init__(self):
        self._matchers: typing.Any = []

    def add_matcher(self, matcher) -> None:
        self._matchers.append(matcher)

    def match(self, request: _RequestObjectProxy) -> typing.Optional[HTTPResponse]:
        for matcher in self._matchers:
            response = matcher(request, skip_port_check=True)
            if response is not None:
                return response
        return None


class Server:
    """Run a real HTTP server with the mocked endpoints."""

    def __init__(self, repository=None):
        self.adapter = HttpAdapter()
        self.repository = repository or BackendRepository()
        self.repository.register(self.adapter)
        self.api_url = "http://localhost:8989"

    def __call__(self, environ, start_response):
        request = self._create_request(environ)
        request_mock = _RequestObjectProxy(request.prepare())

        if request_mock.body is None:
            request_mock.body = ""

        response = self.adapter.match(request_mock)
        response = self._create_response(response)
        return response(environ, start_response)

    def _create_request(self, environ: dict) -> requests.Request:
        req = webob.Request(environ)
        req.make_body_seekable()
        return requests.Request(
            method=req.method,
            url=req.url,
            headers=req.headers,
            data=req.body,
            params=req.GET,
            cookies=req.cookies,
        )

    def _create_response(self, response) -> webob.Response:
        if response is not None:
            return webob.Response(
                body=response.text,
                charset="utf-8",
                status=response.status_code,
                headerlist=list(response.headers.items()),
            )
        return webob.exc.HTTPNotFound()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    server = Server()
    from werkzeug.serving import run_simple

    run_simple("0.0.0.0", port=8989, application=server, use_reloader=True)
