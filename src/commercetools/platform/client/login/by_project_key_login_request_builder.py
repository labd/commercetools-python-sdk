# Generated file, please do not change!!!
import typing

from ...models.customer import CustomerSignin, CustomerSignInResult

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyLoginRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def post(
        self, body: "CustomerSignin", *, headers: typing.Dict[str, str] = None
    ) -> "CustomerSignInResult":
        """Authenticate Customer (Sign In). Retrieves the authenticated
        customer (a customer that matches the given email/password pair).
        If used with an access token for Anonymous Sessions,
        all orders and carts belonging to the anonymousId will be assigned to the newly created customer.
        If a cart is is returned as part of the CustomerSignInResult,
        it has been recalculated (It will have up-to-date prices, taxes and discounts,
        and invalid line items have been removed.).

        """
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/login",
            params={},
            data_object=body,
            response_class=CustomerSignInResult,
            headers={"Content-Type": "application/json", **headers},
        )
