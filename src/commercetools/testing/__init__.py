import typing
import uuid
from contextlib import contextmanager

import requests_mock
import wrapt

from commercetools.testing.abstract import BaseBackend
from commercetools.testing.api_clients import ApiClientsBackend
from commercetools.testing.auth import AuthBackend
from commercetools.testing.cart_discounts import CartDiscountsBackend
from commercetools.testing.carts import CartsBackend
from commercetools.testing.categories import CategoriesBackend
from commercetools.testing.channels import ChannelsBackend
from commercetools.testing.custom_objects import CustomObjectsBackend
from commercetools.testing.customer_groups import CustomerGroupBackend
from commercetools.testing.customers import CustomerBackend
from commercetools.testing.discount_codes import DiscountCodesBackend
from commercetools.testing.extensions import ExtensionsBackend
from commercetools.testing.internal import InternalBackend
from commercetools.testing.inventory import InventoryEntryBackend
from commercetools.testing.orders import OrdersBackend
from commercetools.testing.payments import PaymentsBackend
from commercetools.testing.product_discounts import ProductDiscountsBackend
from commercetools.testing.product_projections import ProductProjectionsBackend
from commercetools.testing.product_types import ProductTypesBackend
from commercetools.testing.products import ProductsBackend
from commercetools.testing.project import ProjectBackend
from commercetools.testing.reviews import ReviewsBackend
from commercetools.testing.shipping_methods import ShippingMethodsBackend
from commercetools.testing.shopping_lists import ShoppingListsBackend
from commercetools.testing.states import StatesBackend
from commercetools.testing.stores import StoresBackend
from commercetools.testing.subscriptions import SubscriptionsBackend
from commercetools.testing.tax_categories import TaxCategoryBackend
from commercetools.testing.types import TypesBackend
from commercetools.testing.zones import ZonesBackend

requests_mock.mock.case_sensitive = True


class Storage:
    def __init__(self):
        self._stores: typing.Dict[str, typing.Dict[uuid.UUID, typing.Any]] = {}

    def init_store(self, name: str) -> typing.Dict[uuid.UUID, typing.Any]:
        return self._stores.setdefault(name, {})

    def get_by_resource_identifier(
        self, obj: typing.Any
    ) -> typing.Optional[typing.Any]:
        store = self._stores[obj.type_id.value]

        try:
            if obj.id:
                key = uuid.UUID(obj.id)
                return store[key]
        except KeyError:
            raise ValueError("No resource found with id %r", obj.id)
        if obj.key:
            for item in store.values():
                if item.key == obj.key:
                    return item
        raise ValueError("No resource found")


class BackendRepository:
    def __init__(self):

        self._storage = Storage()
        self.internal = InternalBackend()

        self.api_clients = ApiClientsBackend(self._storage)
        self.auth = AuthBackend()
        self.carts = CartsBackend(self._storage)
        self.categories = CategoriesBackend(self._storage)
        self.channels = ChannelsBackend(self._storage)
        self.cart_discounts = CartDiscountsBackend(self._storage)
        self.custom_objects = CustomObjectsBackend(self._storage)
        self.customer_groups = CustomerGroupBackend(self._storage)
        self.customers = CustomerBackend(self._storage)
        self.discount_codes = DiscountCodesBackend(self._storage)
        self.extensions = ExtensionsBackend(self._storage)
        self.inventory = InventoryEntryBackend(self._storage)
        self.orders = OrdersBackend(self._storage)
        self.payments = PaymentsBackend(self._storage)
        self.project = ProjectBackend(self._storage)
        self.products = ProductsBackend(self._storage)
        self.product_discounts = ProductDiscountsBackend(self._storage)
        self.product_projections = ProductProjectionsBackend(
            self._storage, model=self.products.model
        )
        self.product_types = ProductTypesBackend(self._storage)
        self.reviews = ReviewsBackend(self._storage)
        self.shipping_methods = ShippingMethodsBackend(self._storage)
        self.shopping_lists = ShoppingListsBackend(self._storage)
        self.states = StatesBackend(self._storage)
        self.stores = StoresBackend(self._storage)
        self.tax_categories = TaxCategoryBackend(self._storage)
        self.types = TypesBackend(self._storage)
        self.subscriptions = SubscriptionsBackend(self._storage)
        self.zones = ZonesBackend(self._storage)

    def register(self, adapter):
        # Bit of a hack, but it works and makes life easier so hey :-)
        for name, value in self.__dict__.items():
            if isinstance(value, BaseBackend):
                value.register(adapter)

        if isinstance(adapter, requests_mock.mocker.Mocker):
            self.requests_mock = adapter


@contextmanager
def backend_mocker(*args, **kwargs):
    with requests_mock.Mocker(real_http=True) as m:
        repo = BackendRepository()
        repo.register(m)
        yield repo


@wrapt.decorator
def mock_commercetools(wrapped, instance, args, kwargs):
    with backend_mocker():
        return wrapped(*args, **kwargs)
