# Generated file, please do not change!!!
import typing

from ...models.importrequests import CustomerImportRequest, ImportResponse
from ..import_operations.by_project_key_customers_import_sink_key_by_import_sink_key_import_operations_request_builder import (
    ByProjectKeyCustomersImportSinkKeyByImportSinkKeyImportOperationsRequestBuilder,
)
from .by_project_key_customers_import_sink_key_by_import_sink_key_resource_key_by_resource_key_request_builder import (
    ByProjectKeyCustomersImportSinkKeyByImportSinkKeyResourceKeyByResourceKeyRequestBuilder,
)


class ByProjectKeyCustomersImportSinkKeyByImportSinkKeyRequestBuilder:

    _client: "Client"
    _project_key: str
    _import_sink_key: str

    def __init__(self, projectKey: str, importSinkKey: str, client: "Client"):
        self._project_key = projectKey
        self._import_sink_key = importSinkKey
        self._client = client

    def resourceKeyWithResourceKeyValue(
        self, resourceKey: str
    ) -> ByProjectKeyCustomersImportSinkKeyByImportSinkKeyResourceKeyByResourceKeyRequestBuilder:
        return ByProjectKeyCustomersImportSinkKeyByImportSinkKeyResourceKeyByResourceKeyRequestBuilder(
            resourceKey=resourceKey,
            projectKey=self._project_key,
            importSinkKey=self._import_sink_key,
            client=self._client,
        )

    def importOperations(
        self
    ) -> ByProjectKeyCustomersImportSinkKeyByImportSinkKeyImportOperationsRequestBuilder:
        return ByProjectKeyCustomersImportSinkKeyByImportSinkKeyImportOperationsRequestBuilder(
            projectKey=self._project_key,
            importSinkKey=self._import_sink_key,
            client=self._client,
        )

    def post(
        self, body: "CustomerImportRequest", *, headers: typing.Dict[str, str] = None
    ) -> "ImportResponse":
        """Creates import request for creating new customers or updating existing ones.
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/customers/importSinkKey={self._import_sink_key}",
            params={},
            data_object=body,
            response_object=ImportResponse,
            headers={"Content-Type": "application/json", **headers},
        )
