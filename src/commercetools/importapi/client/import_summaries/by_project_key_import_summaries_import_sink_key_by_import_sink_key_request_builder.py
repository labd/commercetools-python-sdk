# Generated file, please do not change!!!
import typing

from ...models.importsummaries import ImportSummary


class ByProjectKeyImportSummariesImportSinkKeyByImportSinkKeyRequestBuilder:

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

    def get(self, *, headers: typing.Dict[str, str] = None) -> "ImportSummary":
        """Retrieves an import summary for the given import sink.

        The import summary is calculated on demand.

        """
        return self._client._get(
            endpoint=f"/{self._project_key}/import-summaries/importSinkKey={self._import_sink_key}",
            params={},
            response_class=ImportSummary,
            headers=headers,
        )
