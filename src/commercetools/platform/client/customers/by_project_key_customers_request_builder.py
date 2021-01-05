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


class ByProjectKeyCustomersRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(self, projectKey: str, client: "Client"):
        self._project_key = projectKey
        self._client = client

    def withPasswordToken(
        self, passwordToken: str
    ) -> ByProjectKeyCustomersPasswordTokenByPasswordTokenRequestBuilder:
        return ByProjectKeyCustomersPasswordTokenByPasswordTokenRequestBuilder(
            passwordToken=passwordToken,
            projectKey=self._project_key,
            client=self._client,
        )

    def withEmailToken(
        self, emailToken: str
    ) -> ByProjectKeyCustomersEmailTokenByEmailTokenRequestBuilder:
        return ByProjectKeyCustomersEmailTokenByEmailTokenRequestBuilder(
            emailToken=emailToken, projectKey=self._project_key, client=self._client
        )

    def emailToken(self) -> ByProjectKeyCustomersEmailTokenRequestBuilder:
        """To verify a customer's email, an email token can be created. This should be embedded in a link and sent to the
        customer via email. When the customer clicks on the link, the "verify customer's email" endpoint should be called,
        which sets customer's isVerifiedEmail field to true.
        
        """
        return ByProjectKeyCustomersEmailTokenRequestBuilder(
            projectKey=self._project_key, client=self._client
        )

    def emailConfirm(self) -> ByProjectKeyCustomersEmailConfirmRequestBuilder:
        return ByProjectKeyCustomersEmailConfirmRequestBuilder(
            projectKey=self._project_key, client=self._client
        )

    def password(self) -> ByProjectKeyCustomersPasswordRequestBuilder:
        return ByProjectKeyCustomersPasswordRequestBuilder(
            projectKey=self._project_key, client=self._client
        )

    def passwordReset(self) -> ByProjectKeyCustomersPasswordResetRequestBuilder:
        return ByProjectKeyCustomersPasswordResetRequestBuilder(
            projectKey=self._project_key, client=self._client
        )

    def passwordToken(self) -> ByProjectKeyCustomersPasswordTokenRequestBuilder:
        """The following workflow can be used to reset the customer's password:
        
        * Create a password reset token and send it embedded in a link to the customer.
        * When the customer clicks on the link, the customer is retrieved with the token.
        * The customer enters a new password and the "reset customer's password" endpoint is called.
        
        """
        return ByProjectKeyCustomersPasswordTokenRequestBuilder(
            projectKey=self._project_key, client=self._client
        )

    def withKey(self, key: str) -> ByProjectKeyCustomersKeyByKeyRequestBuilder:
        return ByProjectKeyCustomersKeyByKeyRequestBuilder(
            key=key, projectKey=self._project_key, client=self._client
        )

    def withId(self, ID: str) -> ByProjectKeyCustomersByIDRequestBuilder:
        return ByProjectKeyCustomersByIDRequestBuilder(
            ID=ID, projectKey=self._project_key, client=self._client
        )

    def get(
        self,
        *,
        expand: "str" = None,
        sort: "str" = None,
        limit: "int" = None,
        offset: "int" = None,
        with_total: "bool" = None,
        where: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "CustomerPagedQueryResponse":
        """Query customers
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/customers",
            params={
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_object=CustomerPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "CustomerDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "CustomerSignInResult":
        """Creates a customer. If an anonymous cart is passed in,
        then the cart is assigned to the created customer and the version number of the Cart will increase.
        If the ID of an anonymous session is given, all carts and orders will be assigned to the created customer.
        
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/customers",
            params={"expand": expand},
            data_object=body,
            response_object=CustomerSignInResult,
            headers={"Content-Type": "application/json", **headers},
        )