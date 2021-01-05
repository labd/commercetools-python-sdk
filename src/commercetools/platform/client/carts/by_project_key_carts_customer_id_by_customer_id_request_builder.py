# Generated file, please do not change!!!
import typing

from ...models.cart import Cart

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
        self, *, expand: str = None, headers: typing.Dict[str, str] = None
    ) -> "Cart":
        """Retrieves the active cart of the customer that has been modified most recently.
        It does not consider carts with CartOrigin Merchant. If no active cart exists, a 404 Not Found error is returned.

        The cart may not contain up-to-date prices, discounts etc. If you want to ensure they're up-to-date,
        send an Update request with the Recalculate update action instead.

        """
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/carts/customer-id={self._customer_id}",
            params={"expand": expand},
            response_class=Cart,
            headers=headers,
        )
