# Generated file, please do not change!!!
import typing

from ...models.common import Update
from ...models.order import Order


class ByProjectKeyInStoreKeyByStoreKeyOrdersOrderNumberByOrderNumberRequestBuilder:

    _client: "Client"
    _project_key: str
    _store_key: str
    _order_number: str

    def __init__(
        self,
        projectKey: str,
        storeKey: str,
        orderNumber: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._store_key = storeKey
        self._order_number = orderNumber
        self._client = client

    def get(
        self, *, expand: "str" = None, headers: typing.Dict[str, str] = None
    ) -> "Order":
        """Returns an order by its order number from a specific Store.
        The {storeKey} path parameter maps to a Store's key.
        If the order exists in the commercetools project but does not have the store field,
        or the store field references a different store, this method returns a ResourceNotFound error.
        In case the orderNumber does not match the regular expression [a-zA-Z0-9_\-]+,
        it should be provided in URL-encoded format.

        """
        return self._client._get(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/orders/order-number={self._order_number}",
            params={"expand": expand},
            response_class=Order,
            headers=headers,
        )

    def post(
        self,
        body: "Update",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Order":
        """Updates an order in the store specified by {storeKey}. The {storeKey} path parameter maps to a Store's key.
        If the order exists in the commercetools project but does not have the store field,
        or the store field references a different store, this method returns a ResourceNotFound error.
        In case the orderNumber does not match the regular expression [a-zA-Z0-9_\-]+,
        it should be provided in URL-encoded format.

        """
        return self._client._post(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/orders/order-number={self._order_number}",
            params={"expand": expand},
            data_object=body,
            response_class=Order,
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
        """Delete Order by orderNumber"""
        return self._client._delete(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/orders/order-number={self._order_number}",
            params={"dataErasure": data_erasure, "version": version, "expand": expand},
            response_class=Order,
            headers=headers,
        )
