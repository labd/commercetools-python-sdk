# Generated file, please do not change!!!
import typing

from ...models.importrequests import ImportResponse, OrderImportRequest
from ..import_operations.by_project_key_orders_import_sink_key_by_import_sink_key_import_operations_request_builder import (
    ByProjectKeyOrdersImportSinkKeyByImportSinkKeyImportOperationsRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyOrdersImportSinkKeyByImportSinkKeyRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _import_sink_key: str

    def __init__(
        self,
        project_key: str,
        import_sink_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._import_sink_key = import_sink_key
        self._client = client

    def import_operations(
        self,
    ) -> ByProjectKeyOrdersImportSinkKeyByImportSinkKeyImportOperationsRequestBuilder:
        return ByProjectKeyOrdersImportSinkKeyByImportSinkKeyImportOperationsRequestBuilder(
            project_key=self._project_key,
            import_sink_key=self._import_sink_key,
            client=self._client,
        )

    def post(
        self, body: "OrderImportRequest", *, headers: typing.Dict[str, str] = None
    ) -> "ImportResponse":
        """Creates import request for creating new orders or updating existing ones."""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/orders/importSinkKey={self._import_sink_key}",
            params={},
            data_object=body,
            response_class=ImportResponse,
            headers={"Content-Type": "application/json", **headers},
        )
