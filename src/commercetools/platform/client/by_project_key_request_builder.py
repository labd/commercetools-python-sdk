# Generated file, please do not change!!!
import typing

from ..models.common import Update
from ..models.project import Project
from .api_clients.by_project_key_api_clients_request_builder import (
    ByProjectKeyApiClientsRequestBuilder,
)
from .cart_discounts.by_project_key_cart_discounts_request_builder import (
    ByProjectKeyCartDiscountsRequestBuilder,
)
from .carts.by_project_key_carts_request_builder import ByProjectKeyCartsRequestBuilder
from .categories.by_project_key_categories_request_builder import (
    ByProjectKeyCategoriesRequestBuilder,
)
from .channels.by_project_key_channels_request_builder import (
    ByProjectKeyChannelsRequestBuilder,
)
from .custom_objects.by_project_key_custom_objects_request_builder import (
    ByProjectKeyCustomObjectsRequestBuilder,
)
from .customer_groups.by_project_key_customer_groups_request_builder import (
    ByProjectKeyCustomerGroupsRequestBuilder,
)
from .customers.by_project_key_customers_request_builder import (
    ByProjectKeyCustomersRequestBuilder,
)
from .discount_codes.by_project_key_discount_codes_request_builder import (
    ByProjectKeyDiscountCodesRequestBuilder,
)
from .extensions.by_project_key_extensions_request_builder import (
    ByProjectKeyExtensionsRequestBuilder,
)
from .graphql.by_project_key_graphql_request_builder import (
    ByProjectKeyGraphqlRequestBuilder,
)
from .in_store.by_project_key_in_store_key_by_store_key_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyRequestBuilder,
)
from .inventory.by_project_key_inventory_request_builder import (
    ByProjectKeyInventoryRequestBuilder,
)
from .login.by_project_key_login_request_builder import ByProjectKeyLoginRequestBuilder
from .me.by_project_key_me_request_builder import ByProjectKeyMeRequestBuilder
from .messages.by_project_key_messages_request_builder import (
    ByProjectKeyMessagesRequestBuilder,
)
from .orders.by_project_key_orders_request_builder import (
    ByProjectKeyOrdersRequestBuilder,
)
from .payments.by_project_key_payments_request_builder import (
    ByProjectKeyPaymentsRequestBuilder,
)
from .product_discounts.by_project_key_product_discounts_request_builder import (
    ByProjectKeyProductDiscountsRequestBuilder,
)
from .product_projections.by_project_key_product_projections_request_builder import (
    ByProjectKeyProductProjectionsRequestBuilder,
)
from .product_types.by_project_key_product_types_request_builder import (
    ByProjectKeyProductTypesRequestBuilder,
)
from .products.by_project_key_products_request_builder import (
    ByProjectKeyProductsRequestBuilder,
)
from .reviews.by_project_key_reviews_request_builder import (
    ByProjectKeyReviewsRequestBuilder,
)
from .shipping_methods.by_project_key_shipping_methods_request_builder import (
    ByProjectKeyShippingMethodsRequestBuilder,
)
from .shopping_lists.by_project_key_shopping_lists_request_builder import (
    ByProjectKeyShoppingListsRequestBuilder,
)
from .states.by_project_key_states_request_builder import (
    ByProjectKeyStatesRequestBuilder,
)
from .stores.by_project_key_stores_request_builder import (
    ByProjectKeyStoresRequestBuilder,
)
from .subscriptions.by_project_key_subscriptions_request_builder import (
    ByProjectKeySubscriptionsRequestBuilder,
)
from .tax_categories.by_project_key_tax_categories_request_builder import (
    ByProjectKeyTaxCategoriesRequestBuilder,
)
from .types.by_project_key_types_request_builder import ByProjectKeyTypesRequestBuilder
from .zones.by_project_key_zones_request_builder import ByProjectKeyZonesRequestBuilder


class ByProjectKeyRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def categories(self) -> ByProjectKeyCategoriesRequestBuilder:
        """Categories are used to organize products in a hierarchical structure."""
        return ByProjectKeyCategoriesRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def carts(self) -> ByProjectKeyCartsRequestBuilder:
        """A shopping cart holds product variants and can be ordered."""
        return ByProjectKeyCartsRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def cartDiscounts(self) -> ByProjectKeyCartDiscountsRequestBuilder:
        """Cart discounts are used to change the prices of different elements within a cart."""
        return ByProjectKeyCartDiscountsRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def channels(self) -> ByProjectKeyChannelsRequestBuilder:
        """Channels represent a source or destination of different entities. They can be used to model warehouses or stores."""
        return ByProjectKeyChannelsRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def customers(self) -> ByProjectKeyCustomersRequestBuilder:
        """A customer is a person purchasing products. customers, Orders, Comments and Reviews can be associated to a customer."""
        return ByProjectKeyCustomersRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def customerGroups(self) -> ByProjectKeyCustomerGroupsRequestBuilder:
        """customer-groups are used to evaluate products and channels."""
        return ByProjectKeyCustomerGroupsRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def customObjects(self) -> ByProjectKeyCustomObjectsRequestBuilder:
        """Store custom JSON values."""
        return ByProjectKeyCustomObjectsRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def discountCodes(self) -> ByProjectKeyDiscountCodesRequestBuilder:
        """Discount codes can be added to a discount-code to enable certain discount-code discounts."""
        return ByProjectKeyDiscountCodesRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def graphql(self) -> ByProjectKeyGraphqlRequestBuilder:
        """The commercetools™ platform provides a GraphQL API"""
        return ByProjectKeyGraphqlRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def inventory(self) -> ByProjectKeyInventoryRequestBuilder:
        """Inventory allows you to track stock quantities."""
        return ByProjectKeyInventoryRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def login(self) -> ByProjectKeyLoginRequestBuilder:
        """Retrieves the authenticated customer."""
        return ByProjectKeyLoginRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def messages(self) -> ByProjectKeyMessagesRequestBuilder:
        """A message represents a change or an action performed on a resource (like an Order or a Product)."""
        return ByProjectKeyMessagesRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def orders(self) -> ByProjectKeyOrdersRequestBuilder:
        """An order can be created from a order, usually after a checkout process has been completed."""
        return ByProjectKeyOrdersRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def payments(self) -> ByProjectKeyPaymentsRequestBuilder:
        """Payments hold information about the current state of receiving and/or refunding money"""
        return ByProjectKeyPaymentsRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def products(self) -> ByProjectKeyProductsRequestBuilder:
        """Products are the sellable goods in an e-commerce project on CTP. This document explains some design concepts
        of products on CTP and describes the available HTTP APIs for working with them.

        """
        return ByProjectKeyProductsRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def productDiscounts(self) -> ByProjectKeyProductDiscountsRequestBuilder:
        """Product discounts are used to change certain product prices."""
        return ByProjectKeyProductDiscountsRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def productProjections(self) -> ByProjectKeyProductProjectionsRequestBuilder:
        """A projected representation of a product shows the product with its current or staged data. The current or staged
        representation of a product in a catalog is called a product projection.

        """
        return ByProjectKeyProductProjectionsRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def productTypes(self) -> ByProjectKeyProductTypesRequestBuilder:
        """Product Types are used to describe common characteristics, most importantly common custom attributes,
        of many concrete products.

        """
        return ByProjectKeyProductTypesRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def reviews(self) -> ByProjectKeyReviewsRequestBuilder:
        """Reviews are used to evaluate products and channels."""
        return ByProjectKeyReviewsRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def shippingMethods(self) -> ByProjectKeyShippingMethodsRequestBuilder:
        """Shipping Methods define where orders can be shipped and what the costs are."""
        return ByProjectKeyShippingMethodsRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def shoppingLists(self) -> ByProjectKeyShoppingListsRequestBuilder:
        """shopping-lists e.g. for wishlist support"""
        return ByProjectKeyShoppingListsRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def states(self) -> ByProjectKeyStatesRequestBuilder:
        """The commercetools platform allows you to model states of certain objects, such as orders, line items, products,
        reviews, and payments in order to define finite state machines reflecting the business logic you'd like to
        implement.

        """
        return ByProjectKeyStatesRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def subscriptions(self) -> ByProjectKeySubscriptionsRequestBuilder:
        """Subscriptions allow you to be notified of new messages or changes via a Message Queue of your choice"""
        return ByProjectKeySubscriptionsRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def taxCategories(self) -> ByProjectKeyTaxCategoriesRequestBuilder:
        """Tax Categories define how products are to be taxed in different countries."""
        return ByProjectKeyTaxCategoriesRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def types(self) -> ByProjectKeyTypesRequestBuilder:
        """Types define custom fields that are used to enhance resources as you need."""
        return ByProjectKeyTypesRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def zones(self) -> ByProjectKeyZonesRequestBuilder:
        """Zones allow defining ShippingRates for specific Locations."""
        return ByProjectKeyZonesRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def me(self) -> ByProjectKeyMeRequestBuilder:
        return ByProjectKeyMeRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def extensions(self) -> ByProjectKeyExtensionsRequestBuilder:
        """Extend the behavior of an API with your business logic"""
        return ByProjectKeyExtensionsRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def apiClients(self) -> ByProjectKeyApiClientsRequestBuilder:
        """Manage your API Clients via an API. Useful for Infrastructure-as-Code tooling, and regularly rotating API secrets."""
        return ByProjectKeyApiClientsRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def stores(self) -> ByProjectKeyStoresRequestBuilder:
        """Stores let you model the context your customers shop in."""
        return ByProjectKeyStoresRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def inStoreKeyWithStoreKeyValue(
        self, storeKey: str
    ) -> ByProjectKeyInStoreKeyByStoreKeyRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyRequestBuilder(
            storeKey=storeKey,
            projectKey=self._project_key,
            client=self._client,
        )

    def get(self, *, headers: typing.Dict[str, str] = None) -> "Project":
        """The Endpoint is responding a limited set of information about settings and configuration of the project."""
        return self._client._get(
            endpoint=f"/{self._project_key}",
            params={},
            response_class=Project,
            headers=headers,
        )

    def post(
        self, body: "Update", *, headers: typing.Dict[str, str] = None
    ) -> "Project":
        """Update project"""
        return self._client._post(
            endpoint=f"/{self._project_key}",
            params={},
            data_object=body,
            response_class=Project,
            headers={"Content-Type": "application/json", **headers},
        )
