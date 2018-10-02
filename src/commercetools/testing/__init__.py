import wrapt
import requests_mock

from commercetools.testing.auth import AuthBackend
from commercetools.testing.categories import CategoriesBackend
from commercetools.testing.products import ProductsBackend


class BackendRepository:
    def __init__(self):
        self.auth = AuthBackend()
        self.categories = CategoriesBackend()
        self.products = ProductsBackend()

    def register(self, adapter):
        for backend in self.__dict__.values():
            backend.register(adapter)


@wrapt.decorator
def mock_commercetools(wrapped, instance, args, kwargs):
    def callback(request, context):
        print("X")
        pass

    with requests_mock.Mocker() as m:
        repo = BackendRepository()
        repo.register(m)
        return wrapped(*args, **kwargs)
