# Generated file, please do not change!!!
import typing

from ...models.importrequests import CategoryImportRequest, ImportResponse
from ..import_operations.by_project_key_categories_import_sink_key_by_import_sink_key_import_operations_request_builder import (
    ByProjectKeyCategoriesImportSinkKeyByImportSinkKeyImportOperationsRequestBuilder,
)
from .by_project_key_categories_import_sink_key_by_import_sink_key_resource_key_by_resource_key_request_builder import (
    ByProjectKeyCategoriesImportSinkKeyByImportSinkKeyResourceKeyByResourceKeyRequestBuilder,
)


class ByProjectKeyCategoriesImportSinkKeyByImportSinkKeyRequestBuilder:

    _client: "Client"
    _project_key: str
    _import_sink_key: str

    def __init__(self, projectKey: str, importSinkKey: str, client: "Client"):
        self._project_key = projectKey
        self._import_sink_key = importSinkKey
        self._client = client

    def resourceKeyWithResourceKeyValue(
        self, resourceKey: str
    ) -> ByProjectKeyCategoriesImportSinkKeyByImportSinkKeyResourceKeyByResourceKeyRequestBuilder:
        return ByProjectKeyCategoriesImportSinkKeyByImportSinkKeyResourceKeyByResourceKeyRequestBuilder(
            resourceKey=resourceKey,
            projectKey=self._project_key,
            importSinkKey=self._import_sink_key,
            client=self._client,
        )

    def importOperations(
        self
    ) -> ByProjectKeyCategoriesImportSinkKeyByImportSinkKeyImportOperationsRequestBuilder:
        return ByProjectKeyCategoriesImportSinkKeyByImportSinkKeyImportOperationsRequestBuilder(
            projectKey=self._project_key,
            importSinkKey=self._import_sink_key,
            client=self._client,
        )

    def post(
        self, body: "CategoryImportRequest", *, headers: typing.Dict[str, str] = None
    ) -> "ImportResponse":
        """Creates import request for creating new categories or updating existing ones.
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/categories/importSinkKey={self._import_sink_key}",
            params={},
            data_object=body,
            response_object=ImportResponse,
            headers={"Content-Type": "application/json", **headers},
        )
