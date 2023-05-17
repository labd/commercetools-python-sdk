# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from ...models.cart import Cart, ReplicaCartDraft
from ...models.error import ErrorResponse

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyInStoreKeyByStoreKeyCartsReplicateRequestBuilder:
    _client: "BaseClient"
    _project_key: str
    _store_key: str

    def __init__(
        self,
        project_key: str,
        store_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._store_key = store_key
        self._client = client

    def post(
        self,
        body: "ReplicaCartDraft",
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["Cart"]:
        """Creates a new Cart by replicating an existing Cart or Order. Can be useful in cases where a customer wants to cancel a recent order to make some changes or reorder a previous order.

        The replicated Cart preserves Customer information, Line Items and Custom Line Items, Custom Fields, Discount Codes, and other settings of the Cart or Order. If the Line Items become invalid, for example, due to removed Products or Prices, they are removed from the new Cart. If the Customer switches to another Customer Group, the new Cart is updated with the new value. It has up-to-date Tax Rates, Prices, and Line Item product data and is in `Active` [CartState](ctp:api:type:CartState).

        The new Cart does not contain payments or deliveries. The [State](ctp:api:type:ItemState) of Line Items and Custom Line Items is reset to `initial`.

        """
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/carts/replicate",
            params={},
            json=body.serialize(),
            headers={"Content-Type": "application/json", **headers},
            options=options,
        )
        if response.status_code in (201, 200):
            return Cart.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        warnings.warn("Unhandled status code %d" % response.status_code)
