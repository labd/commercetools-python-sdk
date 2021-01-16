# Generated file, please do not change!!!
import typing

from ...models.importsummaries import ImportSummary

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyImportSummariesImportSinkKeyByImportSinkKeyRequestBuilder:

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

    def get(
        self,
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> "ImportSummary":
        """Retrieves an import summary for the given import sink.

        The import summary is calculated on demand.

        """
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/import-summaries/importSinkKey={self._import_sink_key}",
            params={},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return ImportSummary.deserialize(response.json())
        raise ValueError("Unhandled status code %s", response.status_code)
