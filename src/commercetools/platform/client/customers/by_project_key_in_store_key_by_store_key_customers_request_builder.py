# Generated file, please do not change!!!
import typing

from ...models.customer import (
    CustomerDraft,
    CustomerPagedQueryResponse,
    CustomerSignInResult,
)
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


class ByProjectKeyInStoreKeyByStoreKeyCustomersRequestBuilder:

    _client: "Client"
    _project_key: str
    _store_key: str

    def __init__(
        self,
        projectKey: str,
        storeKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._store_key = storeKey
        self._client = client

    def withPasswordToken(
        self, passwordToken: str
    ) -> ByProjectKeyInStoreKeyByStoreKeyCustomersPasswordTokenByPasswordTokenRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyCustomersPasswordTokenByPasswordTokenRequestBuilder(
            passwordToken=passwordToken,
            projectKey=self._project_key,
            storeKey=self._store_key,
            client=self._client,
        )

    def withEmailToken(
        self, emailToken: str
    ) -> ByProjectKeyInStoreKeyByStoreKeyCustomersEmailTokenByEmailTokenRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyCustomersEmailTokenByEmailTokenRequestBuilder(
            emailToken=emailToken,
            projectKey=self._project_key,
            storeKey=self._store_key,
            client=self._client,
        )

    def emailToken(
        self,
    ) -> ByProjectKeyInStoreKeyByStoreKeyCustomersEmailTokenRequestBuilder:
        """To verify a customer's email, an email token can be created. This should be embedded in a link and sent to the
        customer via email. When the customer clicks on the link,
        the "verify customer's email" endpoint should be called,
        which sets customer's isVerifiedEmail field to true.

        """
        return ByProjectKeyInStoreKeyByStoreKeyCustomersEmailTokenRequestBuilder(
            projectKey=self._project_key,
            storeKey=self._store_key,
            client=self._client,
        )

    def emailConfirm(
        self,
    ) -> ByProjectKeyInStoreKeyByStoreKeyCustomersEmailConfirmRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyCustomersEmailConfirmRequestBuilder(
            projectKey=self._project_key,
            storeKey=self._store_key,
            client=self._client,
        )

    def password(
        self,
    ) -> ByProjectKeyInStoreKeyByStoreKeyCustomersPasswordRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyCustomersPasswordRequestBuilder(
            projectKey=self._project_key,
            storeKey=self._store_key,
            client=self._client,
        )

    def passwordReset(
        self,
    ) -> ByProjectKeyInStoreKeyByStoreKeyCustomersPasswordResetRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyCustomersPasswordResetRequestBuilder(
            projectKey=self._project_key,
            storeKey=self._store_key,
            client=self._client,
        )

    def passwordToken(
        self,
    ) -> ByProjectKeyInStoreKeyByStoreKeyCustomersPasswordTokenRequestBuilder:
        """The following workflow can be used to reset the customer's password:

        * Create a password reset token and send it embedded in a link to the customer.
        * When the customer clicks on the link, the customer is retrieved with the token.
        * The customer enters a new password and the "reset customer's password" endpoint is called.

        """
        return ByProjectKeyInStoreKeyByStoreKeyCustomersPasswordTokenRequestBuilder(
            projectKey=self._project_key,
            storeKey=self._store_key,
            client=self._client,
        )

    def withKey(
        self, key: str
    ) -> ByProjectKeyInStoreKeyByStoreKeyCustomersKeyByKeyRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyCustomersKeyByKeyRequestBuilder(
            key=key,
            projectKey=self._project_key,
            storeKey=self._store_key,
            client=self._client,
        )

    def withId(
        self, ID: str
    ) -> ByProjectKeyInStoreKeyByStoreKeyCustomersByIDRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyCustomersByIDRequestBuilder(
            ID=ID,
            projectKey=self._project_key,
            storeKey=self._store_key,
            client=self._client,
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
        """Query customers"""
        return self._client._get(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/customers",
            params={
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_class=CustomerPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "CustomerDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "CustomerSignInResult":
        """Creates a customer in a specific Store. The {storeKey} path parameter maps to a Store's key.
        When using this endpoint, if omitted,
        the customer's stores field is set to the store specified in the path parameter.
        If an anonymous cart is passed in as when using this method,
        then the cart is assigned to the created customer and the version number of the Cart increases.
        If the ID of an anonymous session is given, all carts and orders will be assigned to the created customer and
        the store specified. If you pass in a cart with a store field specified,
        the store field must reference the same store specified in the {storeKey} path parameter.

        """
        return self._client._post(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/customers",
            params={"expand": expand},
            data_object=body,
            response_class=CustomerSignInResult,
            headers={"Content-Type": "application/json", **headers},
        )
