# Generated file, please do not change!!!
import typing

from ...models.shipping_method import ShippingMethodPagedQueryResponse

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyShippingMethodsMatchingOrdereditRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def get(
        self,
        *,
        order_edit_id: str,
        country: str,
        state: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ShippingMethodPagedQueryResponse":
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/shipping-methods/matching-orderedit",
            params={"orderEditId": order_edit_id, "country": country, "state": state},
            response_class=ShippingMethodPagedQueryResponse,
            headers=headers,
        )
