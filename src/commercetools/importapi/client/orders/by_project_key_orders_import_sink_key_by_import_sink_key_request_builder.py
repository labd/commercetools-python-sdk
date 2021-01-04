# Generated file, please do not change!!!
import typing

from ...models.importrequests import ImportResponse, OrderImportRequest
from ..import_operations.by_project_key_orders_import_sink_key_by_import_sink_key_import_operations_request_builder import (
    ByProjectKeyOrdersImportSinkKeyByImportSinkKeyImportOperationsRequestBuilder,
)


class ByProjectKeyOrdersImportSinkKeyByImportSinkKeyRequestBuilder:

    _client: "Client"
    _project_key: str
    _import_sink_key: str

    def __init__(self, projectKey: str, importSinkKey: str, client: "Client"):
        self._project_key = projectKey
        self._import_sink_key = importSinkKey
        self._client = client

    def importOperations(
        self
    ) -> ByProjectKeyOrdersImportSinkKeyByImportSinkKeyImportOperationsRequestBuilder:
        return ByProjectKeyOrdersImportSinkKeyByImportSinkKeyImportOperationsRequestBuilder(
            projectKey=self._project_key,
            importSinkKey=self._import_sink_key,
            client=self._client,
        )

    def post(
        self, body: "OrderImportRequest", *, headers: typing.Dict[str, str] = None
    ) -> "ImportResponse":
        """Creates import request for creating new orders or updating existing ones.
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/orders/importSinkKey={self._import_sink_key}",
            params={},
            data_object=body,
            response_object=ImportResponse,
            headers={"Content-Type": "application/json", **headers},
        )
