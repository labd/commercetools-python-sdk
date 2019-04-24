import base64
import typing
import uuid
from urllib.parse import parse_qs

from commercetools.testing.abstract import BaseBackend
from commercetools.testing.utils import create_commercetools_response


class AuthModel:
    def __init__(self):
        self.tokens: typing.List[str] = []

    def add_token(self, token):
        self.tokens.append(token)

    def is_valid(self, client_id, client_secret):
        return True


class AuthBackend(BaseBackend):
    path_prefix = r"/oauth/(?P<path>.*)"
    hostnames = ["auth.sphere.io", "localhost"]
    model_class = AuthModel

    def __init__(self, *args, **kwargs):
        self._expire_time = 172800
        super().__init__()

    def set_expire_time(self, value):
        self._expire_time = value

    @property
    def url_prefix(self):
        return r"/oauth/(?P<path>.*)"

    def urls(self):
        return [("token", "POST", self.token)]

    def token(self, request):
        params = parse_qs(request.body)

        client_id: typing.Optional[str] = None
        client_secret: typing.Optional[str] = None

        if request.headers.get("Authorization"):
            auth_type, auth_info = request.headers["Authorization"].split()
            if auth_type != "Basic":
                response = create_commercetools_response(request, status_code=401)
                return response

            client_id, client_secret = str(base64.b64decode(auth_info)).split(":")
        elif params.get("client_id") and params.get("client_secret"):
            client_id = params.get("client_id")
            client_secret = params.get("client_secret")
        else:
            response = create_commercetools_response(request, status_code=401)
            return response

        scope = params.get("scope", "manage_project:todo")

        if self.model.is_valid(client_id, client_secret):
            token = {
                "access_token": str(uuid.uuid4()),
                "expires_in": self._expire_time,
                "scope": scope,
                "token_type": "Bearer",
            }
            self.model.add_token(token)
            response = create_commercetools_response(request, json=token)
            return response
