from contextlib import contextmanager

import requests_mock
import wrapt

from commercetools.testing.abstract import BaseBackend
from commercetools.testing.auth import AuthBackend
from commercetools.testing.categories import CategoriesBackend
from commercetools.testing.channels import ChannelsBackend
from commercetools.testing.custom_objects import CustomObjectsBackend
from commercetools.testing.inventory import InventoryEntryBackend
from commercetools.testing.payments import PaymentsBackend
from commercetools.testing.product_projections import ProductProjectionsBackend
from commercetools.testing.product_types import ProductTypesBackend
from commercetools.testing.products import ProductsBackend
from commercetools.testing.project import ProjectBackend
from commercetools.testing.tax_categories import TaxCategoryBackend
from commercetools.testing.types import TypesBackend


class BackendRepository:
    def __init__(self):
        self.auth = AuthBackend()
        self.categories = CategoriesBackend()
        self.channels = ChannelsBackend()
        self.custom_objects = CustomObjectsBackend()
        self.inventory = InventoryEntryBackend()
        self.payments = PaymentsBackend()
        self.project = ProjectBackend()
        self.products = ProductsBackend()
        self.product_projections = ProductProjectionsBackend(model=self.products.model)
        self.product_types = ProductTypesBackend()
        self.tax_categories = TaxCategoryBackend()
        self.types = TypesBackend()

    def register(self, adapter):
        # Bit of a hack, but it works and makes life easier so hey :-)
        for name, value in self.__dict__.items():
            if isinstance(value, BaseBackend):
                value.register(adapter)
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
