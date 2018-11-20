import typing
import uuid
from urllib.parse import parse_qs

from requests_mock import create_response

from commercetools.testing.abstract import BaseBackend


class AuthModel:
    def __init__(self):
        self.tokens: typing.List[str] = []

    def add_token(self, token):
        self.tokens.append(token)


class AuthBackend(BaseBackend):
    path_prefix = r"/oauth/(?P<path>.*)"
    hostnames = ["auth.sphere.io", "localhost"]
    model_class = AuthModel

    def __init__(self, *args, **kwargs):
        self._expire_time = 172800
        super().__init__(*args, **kwargs)

    def set_expire_time(self, value):
        self._expire_time = value

    @property
    def url_prefix(self):
        return r"/oauth/(?P<path>.*)"

    def urls(self):
        return [("token", "POST", self.token)]

    def token(self, request):
        params = parse_qs(request.body)
        if not params.get("client_id") and not params.get("client_secret"):
            response = create_response(request, status_code=401)
            return response

        token = {
            "access_token": str(uuid.uuid4()),
            "expires_in": self._expire_time,
            "scope": params["scope"],
            "token_type": "Bearer",
        }
        self.model.add_token(token)
        response = create_response(request, json=token)
        return response
