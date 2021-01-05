# Generated file, please do not change!!!
import typing

from ...models.order import Order, OrderImportDraft

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyOrdersImportRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def post(
        self, body: "OrderImportDraft", *, headers: typing.Dict[str, str] = None
    ) -> "Order":
        """Create an Order by Import"""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/orders/import",
            params={},
            data_object=body,
            response_class=Order,
            headers={"Content-Type": "application/json", **headers},
        )
