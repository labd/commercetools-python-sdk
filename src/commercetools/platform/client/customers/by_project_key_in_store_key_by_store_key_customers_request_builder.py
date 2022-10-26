# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from ...models.customer import (
    CustomerDraft,
    CustomerPagedQueryResponse,
    CustomerSignInResult,
)
from ...models.error import ErrorResponse
from ..confirm.by_project_key_in_store_key_by_store_key_customers_email_confirm_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyCustomersEmailConfirmRequestBuilder,
)
from ..email_token.by_project_key_in_store_key_by_store_key_customers_email_token_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyCustomersEmailTokenRequestBuilder,
)
from ..password.by_project_key_in_store_key_by_store_key_customers_password_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyCustomersPasswordRequestBuilder,
)
from ..password_token.by_project_key_in_store_key_by_store_key_customers_password_token_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyCustomersPasswordTokenRequestBuilder,
)
from ..reset.by_project_key_in_store_key_by_store_key_customers_password_reset_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyCustomersPasswordResetRequestBuilder,
)
from .by_project_key_in_store_key_by_store_key_customers_by_id_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyCustomersByIDRequestBuilder,
)
from .by_project_key_in_store_key_by_store_key_customers_email_token_by_email_token_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyCustomersEmailTokenByEmailTokenRequestBuilder,
)
from .by_project_key_in_store_key_by_store_key_customers_key_by_key_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyCustomersKeyByKeyRequestBuilder,
)
from .by_project_key_in_store_key_by_store_key_customers_password_token_by_password_token_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyCustomersPasswordTokenByPasswordTokenRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyInStoreKeyByStoreKeyCustomersRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _store_key: str

    def __init__(
        self,
        project_key: str,
        store_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._store_key = store_key
        self._client = client

    def with_password_token(
        self, password_token: str
    ) -> ByProjectKeyInStoreKeyByStoreKeyCustomersPasswordTokenByPasswordTokenRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyCustomersPasswordTokenByPasswordTokenRequestBuilder(
            password_token=password_token,
            project_key=self._project_key,
            store_key=self._store_key,
            client=self._client,
        )

    def with_email_token(
        self, email_token: str
    ) -> ByProjectKeyInStoreKeyByStoreKeyCustomersEmailTokenByEmailTokenRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyCustomersEmailTokenByEmailTokenRequestBuilder(
            email_token=email_token,
            project_key=self._project_key,
            store_key=self._store_key,
            client=self._client,
        )

    def email_token(
        self,
    ) -> ByProjectKeyInStoreKeyByStoreKeyCustomersEmailTokenRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyCustomersEmailTokenRequestBuilder(
            project_key=self._project_key,
            store_key=self._store_key,
            client=self._client,
        )

    def email_confirm(
        self,
    ) -> ByProjectKeyInStoreKeyByStoreKeyCustomersEmailConfirmRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyCustomersEmailConfirmRequestBuilder(
            project_key=self._project_key,
            store_key=self._store_key,
            client=self._client,
        )

    def password(
        self,
    ) -> ByProjectKeyInStoreKeyByStoreKeyCustomersPasswordRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyCustomersPasswordRequestBuilder(
            project_key=self._project_key,
            store_key=self._store_key,
            client=self._client,
        )

    def password_reset(
        self,
    ) -> ByProjectKeyInStoreKeyByStoreKeyCustomersPasswordResetRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyCustomersPasswordResetRequestBuilder(
            project_key=self._project_key,
            store_key=self._store_key,
            client=self._client,
        )

    def password_token(
        self,
    ) -> ByProjectKeyInStoreKeyByStoreKeyCustomersPasswordTokenRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyCustomersPasswordTokenRequestBuilder(
            project_key=self._project_key,
            store_key=self._store_key,
            client=self._client,
        )

    def with_key(
        self, key: str
    ) -> ByProjectKeyInStoreKeyByStoreKeyCustomersKeyByKeyRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyCustomersKeyByKeyRequestBuilder(
            key=key,
            project_key=self._project_key,
            store_key=self._store_key,
            client=self._client,
        )

    def with_id(
        self, id: str
    ) -> ByProjectKeyInStoreKeyByStoreKeyCustomersByIDRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyCustomersByIDRequestBuilder(
            id=id,
            project_key=self._project_key,
            store_key=self._store_key,
            client=self._client,
        )

    def get(
        self,
        *,
        expand: typing.List["str"] = None,
        sort: typing.List["str"] = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        where: typing.List["str"] = None,
        predicate_var: typing.Dict[str, typing.List["str"]] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["CustomerPagedQueryResponse"]:
        params = {
            "expand": expand,
            "sort": sort,
            "limit": limit,
            "offset": offset,
            "withTotal": with_total,
            "where": where,
        }
        predicate_var and params.update(
            {f"var.{k}": v for k, v in predicate_var.items()}
        )
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/customers",
            params=params,
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return CustomerPagedQueryResponse.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            raise self._client._create_exception(None, response)
        warnings.warn("Unhandled status code %d" % response.status_code)

    def head(
        self,
        *,
        where: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional[None]:
        """Checks if a Customer exists for a given Query Predicate. Returns a `200 OK` status if any Customers match the Query Predicate or a `404 Not Found` otherwise."""
        headers = {} if headers is None else headers
        response = self._client._head(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/customers",
            params={"where": where},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return None
        elif response.status_code == 404:
            return None
        elif response.status_code in (400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        warnings.warn("Unhandled status code %d" % response.status_code)

    def post(
        self,
        body: "CustomerDraft",
        *,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["CustomerSignInResult"]:
        """When using this endpoint, if omitted, the Customer `stores` field is set to the [Store](ctp:api:type:Store) specified in the path parameter.

        If the `anonymousCart` field is set on the [CustomerDraft](ctp:api:type:CustomerDraft), then the newly created Customer will be assigned to that [Cart](ctp:api:type:Cart).
        Similarly, if the `anonymousId` field is set, the Customer will be set on all [Carts](ctp:api:type:Cart), [Orders](ctp:api:type:Order), [ShoppingLists](ctp:api:type:ShoppingList) and [Payments](ctp:api:type:Payment) with the same `anonymousId`.
        If a Cart with a `store` field specified, the `store` field must reference the same [Store](ctp:api:type:Store) specified in the `{storeKey}` path parameter.
        Creating a Customer produces the [CustomerCreated](ctp:api:type:CustomerCreatedMessage) Message.

        """
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/customers",
            params={"expand": expand},
            json=body.serialize(),
            headers={"Content-Type": "application/json", **headers},
            options=options,
        )
        if response.status_code in (201, 200):
            return CustomerSignInResult.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            raise self._client._create_exception(None, response)
        warnings.warn("Unhandled status code %d" % response.status_code)
