# Generated file, please do not change!!!
import typing

from ...models.common import ProcessingState
from ...models.importoperations import ImportOperationPagedResponse
from .by_project_key_products_import_sink_key_by_import_sink_key_import_operations_by_id_request_builder import (
    ByProjectKeyProductsImportSinkKeyByImportSinkKeyImportOperationsByIdRequestBuilder,
)


class ByProjectKeyProductsImportSinkKeyByImportSinkKeyImportOperationsRequestBuilder:

    _client: "Client"
    _project_key: str
    _import_sink_key: str

    def __init__(
        self,
        projectKey: str,
        importSinkKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._import_sink_key = importSinkKey
        self._client = client

    def withIdValue(
        self, id: str
    ) -> ByProjectKeyProductsImportSinkKeyByImportSinkKeyImportOperationsByIdRequestBuilder:
        return ByProjectKeyProductsImportSinkKeyByImportSinkKeyImportOperationsByIdRequestBuilder(
            id=id,
            projectKey=self._project_key,
            importSinkKey=self._import_sink_key,
            client=self._client,
        )

    def get(
        self,
        *,
        limit: "float" = None,
        offset: "float" = None,
        sort: typing.List["str"] = None,
        resource_key: "str" = None,
        state: "ProcessingState" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ImportOperationPagedResponse":
        """Retrieves all product import operations of an import sink key."""
        return self._client._get(
            endpoint=f"/{self._project_key}/products/importSinkKey={self._import_sink_key}/import-operations",
            params={
                "limit": limit,
                "offset": offset,
                "sort": sort,
                "resourceKey": resource_key,
                "state": state,
            },
            response_class=ImportOperationPagedResponse,
            headers=headers,
        )
