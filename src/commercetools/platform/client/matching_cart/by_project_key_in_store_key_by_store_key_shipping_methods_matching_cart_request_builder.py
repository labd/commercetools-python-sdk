# Generated file, please do not change!!!
import typing

from ...models.shipping_method import ShippingMethodPagedQueryResponse

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyInStoreKeyByStoreKeyShippingMethodsMatchingCartRequestBuilder:

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

    def get(
        self, *, cart_id: str, expand: str = None, headers: typing.Dict[str, str] = None
    ) -> "ShippingMethodPagedQueryResponse":
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/shipping-methods/matching-cart",
            params={"cartId": cart_id, "expand": expand},
            response_class=ShippingMethodPagedQueryResponse,
            headers=headers,
        )
