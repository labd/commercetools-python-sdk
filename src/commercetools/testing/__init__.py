from contextlib import contextmanager

import requests_mock
import wrapt

from commercetools.testing.auth import AuthBackend
from commercetools.testing.categories import CategoriesBackend
from commercetools.testing.channels import ChannelsBackend
from commercetools.testing.payments import PaymentsBackend
from commercetools.testing.product_projections import ProductProjectionsBackend
from commercetools.testing.product_types import ProductTypesBackend
from commercetools.testing.products import ProductsBackend


class BackendRepository:
    def __init__(self):
        self.auth = AuthBackend()
        self.categories = CategoriesBackend()
        self.channels = ChannelsBackend()
        self.payments = PaymentsBackend()
        self.products = ProductsBackend()
        self.product_projections = ProductProjectionsBackend(model=self.products.model)
        self.product_types = ProductTypesBackend()

    def register(self, adapter):
        backends = [
            "auth",
            "categories",
            "channels",
            "payments",
            "products",
            "product_projections",
            "product_types",
        ]
        for backend_name in backends:
            backend = getattr(self, backend_name)
            backend.register(adapter)
        self.requests_mock = adapter


@contextmanager
def backend_mocker(*args, **kwargs):
    with requests_mock.Mocker() as m:
        repo = BackendRepository()
        repo.register(m)
        yield repo


@wrapt.decorator
def mock_commercetools(wrapped, instance, args, kwargs):
    with backend_mocker():
        return wrapped(*args, **kwargs)
