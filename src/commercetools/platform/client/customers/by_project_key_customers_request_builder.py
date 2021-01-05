# Generated file, please do not change!!!
import typing

from ...models.customer import (
    CustomerDraft,
    CustomerPagedQueryResponse,
    CustomerSignInResult,
)
from ..confirm.by_project_key_customers_email_confirm_request_builder import (
    ByProjectKeyCustomersEmailConfirmRequestBuilder,
)
from ..email_token.by_project_key_customers_email_token_request_builder import (
    ByProjectKeyCustomersEmailTokenRequestBuilder,
)
from ..password.by_project_key_customers_password_request_builder import (
    ByProjectKeyCustomersPasswordRequestBuilder,
)
from ..password_token.by_project_key_customers_password_token_request_builder import (
    ByProjectKeyCustomersPasswordTokenRequestBuilder,
)
from ..reset.by_project_key_customers_password_reset_request_builder import (
    ByProjectKeyCustomersPasswordResetRequestBuilder,
)
from .by_project_key_customers_by_id_request_builder import (
    ByProjectKeyCustomersByIDRequestBuilder,
)
from .by_project_key_customers_email_token_by_email_token_request_builder import (
    ByProjectKeyCustomersEmailTokenByEmailTokenRequestBuilder,
)
from .by_project_key_customers_key_by_key_request_builder import (
    ByProjectKeyCustomersKeyByKeyRequestBuilder,
)
from .by_project_key_customers_password_token_by_password_token_request_builder import (
    ByProjectKeyCustomersPasswordTokenByPasswordTokenRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyCustomersRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def with_password_token(
        self, password_token: str
    ) -> ByProjectKeyCustomersPasswordTokenByPasswordTokenRequestBuilder:
        return ByProjectKeyCustomersPasswordTokenByPasswordTokenRequestBuilder(
            password_token=password_token,
            project_key=self._project_key,
            client=self._client,
        )

    def with_email_token(
        self, email_token: str
    ) -> ByProjectKeyCustomersEmailTokenByEmailTokenRequestBuilder:
        return ByProjectKeyCustomersEmailTokenByEmailTokenRequestBuilder(
            email_token=email_token,
            project_key=self._project_key,
            client=self._client,
        )

    def email_token(self) -> ByProjectKeyCustomersEmailTokenRequestBuilder:
        """To verify a customer's email, an email token can be created. This should be embedded in a link and sent to the
        customer via email. When the customer clicks on the link, the "verify customer's email" endpoint should be called,
        which sets customer's isVerifiedEmail field to true.

        """
        return ByProjectKeyCustomersEmailTokenRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def email_confirm(self) -> ByProjectKeyCustomersEmailConfirmRequestBuilder:
        return ByProjectKeyCustomersEmailConfirmRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def password(self) -> ByProjectKeyCustomersPasswordRequestBuilder:
        return ByProjectKeyCustomersPasswordRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def password_reset(self) -> ByProjectKeyCustomersPasswordResetRequestBuilder:
        return ByProjectKeyCustomersPasswordResetRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def password_token(self) -> ByProjectKeyCustomersPasswordTokenRequestBuilder:
        """The following workflow can be used to reset the customer's password:

        * Create a password reset token and send it embedded in a link to the customer.
        * When the customer clicks on the link, the customer is retrieved with the token.
        * The customer enters a new password and the "reset customer's password" endpoint is called.

        """
        return ByProjectKeyCustomersPasswordTokenRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def with_key(self, key: str) -> ByProjectKeyCustomersKeyByKeyRequestBuilder:
        return ByProjectKeyCustomersKeyByKeyRequestBuilder(
            key=key,
            project_key=self._project_key,
            client=self._client,
        )

    def with_id(self, id: str) -> ByProjectKeyCustomersByIDRequestBuilder:
        return ByProjectKeyCustomersByIDRequestBuilder(
            id=id,
            project_key=self._project_key,
            client=self._client,
        )

    def get(
        self,
        *,
        expand: str = None,
        sort: str = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        where: str = None,
        predicate_var: typing.Dict[str, str] = None,
        headers: typing.Dict[str, str] = None,
    ) -> "CustomerPagedQueryResponse":
        """Query customers"""
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
        return self._client._get(
            endpoint=f"/{self._project_key}/customers",
            params=params,
            response_class=CustomerPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "CustomerDraft",
        *,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "CustomerSignInResult":
        """Creates a customer. If an anonymous cart is passed in,
        then the cart is assigned to the created customer and the version number of the Cart will increase.
        If the ID of an anonymous session is given, all carts and orders will be assigned to the created customer.

        """
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/customers",
            params={"expand": expand},
            data_object=body,
            response_class=CustomerSignInResult,
            headers={"Content-Type": "application/json", **headers},
        )
