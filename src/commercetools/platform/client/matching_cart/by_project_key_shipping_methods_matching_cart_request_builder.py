# Generated file, please do not change!!!
import typing

from ...models.shipping_method import ShippingMethodPagedQueryResponse


class ByProjectKeyShippingMethodsMatchingCartRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def get(
        self,
        *,
        cart_id: "str",
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ShippingMethodPagedQueryResponse":
        return self._client._get(
            endpoint=f"/{self._project_key}/shipping-methods/matching-cart",
            params={"cartId": cart_id, "expand": expand},
            response_class=ShippingMethodPagedQueryResponse,
            headers=headers,
        )
