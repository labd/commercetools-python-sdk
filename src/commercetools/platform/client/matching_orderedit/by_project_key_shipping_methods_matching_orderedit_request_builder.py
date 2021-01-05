# Generated file, please do not change!!!
import typing

from ...models.shipping_method import ShippingMethodPagedQueryResponse


class ByProjectKeyShippingMethodsMatchingOrdereditRequestBuilder:

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
        order_edit_id: "str",
        country: "str",
        state: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ShippingMethodPagedQueryResponse":
        return self._client._get(
            endpoint=f"/{self._project_key}/shipping-methods/matching-orderedit",
            params={"orderEditId": order_edit_id, "country": country, "state": state},
            response_class=ShippingMethodPagedQueryResponse,
            headers=headers,
        )
