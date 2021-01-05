# Generated file, please do not change!!!
import typing

from ...models.order import Order, OrderImportDraft


class ByProjectKeyOrdersImportRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def post(
        self, body: "OrderImportDraft", *, headers: typing.Dict[str, str] = None
    ) -> "Order":
        """Create an Order by Import"""
        return self._client._post(
            endpoint=f"/{self._project_key}/orders/import",
            params={},
            data_object=body,
            response_class=Order,
            headers={"Content-Type": "application/json", **headers},
        )
