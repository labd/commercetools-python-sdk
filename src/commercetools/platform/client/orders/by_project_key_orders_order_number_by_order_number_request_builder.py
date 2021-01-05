# Generated file, please do not change!!!
import typing

from ...models.common import Update
from ...models.order import Order

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyOrdersOrderNumberByOrderNumberRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _order_number: str

    def __init__(
        self,
        project_key: str,
        order_number: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._order_number = order_number
        self._client = client

    def get(
        self, *, expand: str = None, headers: typing.Dict[str, str] = None
    ) -> "Order":
        """In case the orderNumber does not match the regular expression [a-zA-Z0-9_\-]+,
        it should be provided in URL-encoded format.

        """
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/orders/order-number={self._order_number}",
            params={"expand": expand},
            response_class=Order,
            headers=headers,
        )

    def post(
        self,
        body: "Update",
        *,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Order":
        """Update Order by orderNumber"""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/orders/order-number={self._order_number}",
            params={"expand": expand},
            data_object=body,
            response_class=Order,
            headers={"Content-Type": "application/json", **headers},
        )

    def delete(
        self,
        *,
        data_erasure: bool = None,
        version: int,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Order":
        """Delete Order by orderNumber"""
        headers = {} if headers is None else headers
        return self._client._delete(
            endpoint=f"/{self._project_key}/orders/order-number={self._order_number}",
            params={"dataErasure": data_erasure, "version": version, "expand": expand},
            response_class=Order,
            headers=headers,
        )
