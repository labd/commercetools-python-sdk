from commercetools.testing.abstract import BaseBackend, BaseModel
from commercetools.testing.utils import create_commercetools_response


class InternalBackend(BaseBackend):
    path_prefix = r"/-/(?P<path>.*)"
    hostnames = ["auth.sphere.io", "localhost"]

    def urls(self):
        return [("^health$", "GET", self.health)]

    def health(self, request):
        response = create_commercetools_response(request, json={})
        return response
