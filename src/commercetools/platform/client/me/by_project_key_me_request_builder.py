# Generated file, please do not change!!!
import typing

from ...models.common import Update
from ...models.me import MyCustomer
from ..active_cart.by_project_key_me_active_cart_request_builder import (
    ByProjectKeyMeActiveCartRequestBuilder,
)
from ..carts.by_project_key_me_carts_request_builder import (
    ByProjectKeyMeCartsRequestBuilder,
)
from ..confirm.by_project_key_me_email_confirm_request_builder import (
    ByProjectKeyMeEmailConfirmRequestBuilder,
)
from ..login.by_project_key_me_login_request_builder import (
    ByProjectKeyMeLoginRequestBuilder,
)
from ..orders.by_project_key_me_orders_request_builder import (
    ByProjectKeyMeOrdersRequestBuilder,
)
from ..password.by_project_key_me_password_request_builder import (
    ByProjectKeyMePasswordRequestBuilder,
)
from ..payments.by_project_key_me_payments_request_builder import (
    ByProjectKeyMePaymentsRequestBuilder,
)
from ..shopping_lists.by_project_key_me_shopping_lists_request_builder import (
    ByProjectKeyMeShoppingListsRequestBuilder,
)
from ..signup.by_project_key_me_signup_request_builder import (
    ByProjectKeyMeSignupRequestBuilder,
)


class ByProjectKeyMeRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def emailConfirm(self) -> ByProjectKeyMeEmailConfirmRequestBuilder:
        return ByProjectKeyMeEmailConfirmRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def password(self) -> ByProjectKeyMePasswordRequestBuilder:
        return ByProjectKeyMePasswordRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def signup(self) -> ByProjectKeyMeSignupRequestBuilder:
        return ByProjectKeyMeSignupRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def login(self) -> ByProjectKeyMeLoginRequestBuilder:
        return ByProjectKeyMeLoginRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def activeCart(self) -> ByProjectKeyMeActiveCartRequestBuilder:
        return ByProjectKeyMeActiveCartRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def carts(self) -> ByProjectKeyMeCartsRequestBuilder:
        """A shopping cart holds product variants and can be ordered."""
        return ByProjectKeyMeCartsRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def orders(self) -> ByProjectKeyMeOrdersRequestBuilder:
        """An order can be created from a cart, usually after a checkout process has been completed."""
        return ByProjectKeyMeOrdersRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def payments(self) -> ByProjectKeyMePaymentsRequestBuilder:
        """The My Payments endpoint creates and provides access to payments scoped to a specific user."""
        return ByProjectKeyMePaymentsRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def shoppingLists(self) -> ByProjectKeyMeShoppingListsRequestBuilder:
        """The My Shopping Lists endpoint creates and provides access to shopping lists scoped to a specific user."""
        return ByProjectKeyMeShoppingListsRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def get(
        self,
        *,
        sort: "str" = None,
        limit: "int" = None,
        offset: "int" = None,
        with_total: "bool" = None,
        expand: "str" = None,
        where: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "MyCustomer":
        return self._client._get(
            endpoint=f"/{self._project_key}/me",
            params={
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "expand": expand,
                "where": where,
            },
            response_class=MyCustomer,
            headers=headers,
        )

    def post(
        self, body: "Update", *, headers: typing.Dict[str, str] = None
    ) -> "MyCustomer":
        """Update my customer"""
        return self._client._post(
            endpoint=f"/{self._project_key}/me",
            params={},
            data_object=body,
            response_class=MyCustomer,
            headers={"Content-Type": "application/json", **headers},
        )

    def delete(
        self, *, version: "int", headers: typing.Dict[str, str] = None
    ) -> "MyCustomer":
        """Delete my Customer"""
        return self._client._delete(
            endpoint=f"/{self._project_key}/me",
            params={"version": version},
            response_class=MyCustomer,
            headers=headers,
        )
