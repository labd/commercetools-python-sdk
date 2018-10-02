import json

from requests_mock import create_response

from commercetools.testing.abstract import BaseBackend


class AuthBackend(BaseBackend):
    path_prefix = r"/oauth/(?P<path>.*)"
    hostnames = ["auth.sphere.io"]

    @property
    def url_prefix(self):
        return r"/oauth/(?P<path>.*)"

    def urls(self):
        return [("token", "POST", self.token)]

    def token(self, request):
        response = create_response(request)
        response._content = json.dumps(
            {
                "access_token": "dummy",
                "expires_in": 172800,
                "scope": "manage_project:unittest",
                "token_type": "Bearer",
            }
        ).encode("utf-8")
        return response
