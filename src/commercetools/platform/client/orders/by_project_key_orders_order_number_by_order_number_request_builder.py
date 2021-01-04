# Generated file, please do not change!!!
import typing

from ...models.common import Update
from ...models.order import Order


class ByProjectKeyOrdersOrderNumberByOrderNumberRequestBuilder:

    _client: "Client"
    _project_key: str
    _order_number: str

    def __init__(self, projectKey: str, orderNumber: str, client: "Client"):
        self._project_key = projectKey
        self._order_number = orderNumber
        self._client = client

    def get(
        self, *, expand: "str" = None, headers: typing.Dict[str, str] = None
    ) -> "Order":
        """In case the orderNumber does not match the regular expression [a-zA-Z0-9_\-]+,
        it should be provided in URL-encoded format.
        
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/orders/order-number={self._order_number}",
            params={"expand": expand},
            response_object=Order,
            headers=headers,
        )

    def post(
        self,
        body: "Update",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Order":
        """Update Order by orderNumber
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/orders/order-number={self._order_number}",
            params={"expand": expand},
            data_object=body,
            response_object=Order,
            headers={"Content-Type": "application/json", **headers},
        )

    def delete(
        self,
        *,
        data_erasure: "bool" = None,
        version: "int",
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Order":
        """Delete Order by orderNumber
        """
        return self._client._delete(
            endpoint=f"/{self._project_key}/orders/order-number={self._order_number}",
            params={"dataErasure": data_erasure, "version": version, "expand": expand},
            response_object=Order,
            headers=headers,
        )
