# Generated file, please do not change!!!
import typing

from .by_project_key_products_import_sink_key_by_import_sink_key_request_builder import (
    ByProjectKeyProductsImportSinkKeyByImportSinkKeyRequestBuilder,
)


class ByProjectKeyProductsRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def importSinkKeyWithImportSinkKeyValue(
        self, importSinkKey: str
    ) -> ByProjectKeyProductsImportSinkKeyByImportSinkKeyRequestBuilder:
        return ByProjectKeyProductsImportSinkKeyByImportSinkKeyRequestBuilder(
            importSinkKey=importSinkKey,
            projectKey=self._project_key,
            client=self._client,
        )
