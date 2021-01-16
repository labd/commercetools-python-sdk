# Generated file, please do not change!!!
import typing

from ...models.cart import Cart
from ...models.error import ErrorResponse

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyCartsCustomerIdByCustomerIdRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _customer_id: str

    def __init__(
        self,
        project_key: str,
        customer_id: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._customer_id = customer_id
        self._client = client

    def get(
        self,
        *,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["Cart"]:
        """Retrieves the active cart of the customer that has been modified most recently.
        It does not consider carts with CartOrigin Merchant. If no active cart exists, a 404 Not Found error is returned.

        The cart may not contain up-to-date prices, discounts etc. If you want to ensure they're up-to-date,
        send an Update request with the Recalculate update action instead.

        """
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/carts/customer-id={self._customer_id}",
            params={"expand": expand},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return Cart.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        raise ValueError("Unhandled status code %s", response.status_code)
