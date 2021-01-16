# Generated file, please do not change!!!
import typing

from ...models.common import Update
from ...models.error import ErrorResponse
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

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyMeRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def email_confirm(self) -> ByProjectKeyMeEmailConfirmRequestBuilder:
        return ByProjectKeyMeEmailConfirmRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def password(self) -> ByProjectKeyMePasswordRequestBuilder:
        return ByProjectKeyMePasswordRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def signup(self) -> ByProjectKeyMeSignupRequestBuilder:
        return ByProjectKeyMeSignupRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def login(self) -> ByProjectKeyMeLoginRequestBuilder:
        return ByProjectKeyMeLoginRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def active_cart(self) -> ByProjectKeyMeActiveCartRequestBuilder:
        return ByProjectKeyMeActiveCartRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def carts(self) -> ByProjectKeyMeCartsRequestBuilder:
        """A shopping cart holds product variants and can be ordered."""
        return ByProjectKeyMeCartsRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def orders(self) -> ByProjectKeyMeOrdersRequestBuilder:
        """An order can be created from a cart, usually after a checkout process has been completed."""
        return ByProjectKeyMeOrdersRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def payments(self) -> ByProjectKeyMePaymentsRequestBuilder:
        """The My Payments endpoint creates and provides access to payments scoped to a specific user."""
        return ByProjectKeyMePaymentsRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def shopping_lists(self) -> ByProjectKeyMeShoppingListsRequestBuilder:
        """The My Shopping Lists endpoint creates and provides access to shopping lists scoped to a specific user."""
        return ByProjectKeyMeShoppingListsRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def get(
        self,
        *,
        sort: typing.List["str"] = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        expand: typing.List["str"] = None,
        where: typing.List["str"] = None,
        predicate_var: typing.Dict[str, typing.List["str"]] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["MyCustomer"]:
        params = {
            "sort": sort,
            "limit": limit,
            "offset": offset,
            "withTotal": with_total,
            "expand": expand,
            "where": where,
        }
        predicate_var and params.update(
            {f"var.{k}": v for k, v in predicate_var.items()}
        )
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/me",
            params=params,
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return MyCustomer.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        raise ValueError("Unhandled status code %s", response.status_code)

    def post(
        self,
        body: "Update",
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["MyCustomer"]:
        """Update my customer"""
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/me",
            params={},
            json=body.serialize(),
            headers={"Content-Type": "application/json", **headers},
            options=options,
        )
        if response.status_code == 200:
            return MyCustomer.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        raise ValueError("Unhandled status code %s", response.status_code)

    def delete(
        self,
        *,
        version: int,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["MyCustomer"]:
        """Delete my Customer"""
        headers = {} if headers is None else headers
        response = self._client._delete(
            endpoint=f"/{self._project_key}/me",
            params={"version": version},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return MyCustomer.deserialize(response.json())
        elif response.status_code in (409, 400, 401, 403, 500, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        raise ValueError("Unhandled status code %s", response.status_code)
