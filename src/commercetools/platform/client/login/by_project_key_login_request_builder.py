# Generated file, please do not change!!!
import typing

from ...models.customer import CustomerSignin, CustomerSignInResult


class ByProjectKeyLoginRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
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
        return self._client._post(
            endpoint=f"/{self._project_key}/login",
            params={},
            data_object=body,
            response_class=CustomerSignInResult,
            headers={"Content-Type": "application/json", **headers},
        )
