# Generated file, please do not change!!!
import typing

from .by_project_key_import_summaries_import_sink_key_by_import_sink_key_request_builder import (
    ByProjectKeyImportSummariesImportSinkKeyByImportSinkKeyRequestBuilder,
)


class ByProjectKeyImportSummariesRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(self, projectKey: str, client: "Client"):
        self._project_key = projectKey
        self._client = client

    def importSinkKeyWithImportSinkKeyValue(
        self, importSinkKey: str
    ) -> ByProjectKeyImportSummariesImportSinkKeyByImportSinkKeyRequestBuilder:
        return ByProjectKeyImportSummariesImportSinkKeyByImportSinkKeyRequestBuilder(
            importSinkKey=importSinkKey,
            projectKey=self._project_key,
            client=self._client,
        )
