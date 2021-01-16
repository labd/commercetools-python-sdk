# Generated file, please do not change!!!
import typing

from ...models.customer import CustomerSignin, CustomerSignInResult
from ...models.error import ErrorResponse

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
        self,
        body: "CustomerSignin",
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["CustomerSignInResult"]:
        """Authenticate Customer (Sign In). Retrieves the authenticated
        customer (a customer that matches the given email/password pair).
        If used with an access token for Anonymous Sessions,
        all orders and carts belonging to the anonymousId will be assigned to the newly created customer.
        If a cart is is returned as part of the CustomerSignInResult,
        it has been recalculated (It will have up-to-date prices, taxes and discounts,
        and invalid line items have been removed.).

        """
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/login",
            params={},
            json=body.serialize(),
            headers={"Content-Type": "application/json", **headers},
            options=options,
        )
        if response.status_code == 201:
            return CustomerSignInResult.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        elif response.status_code == 200:
            return None
        raise ValueError("Unhandled status code %s", response.status_code)
