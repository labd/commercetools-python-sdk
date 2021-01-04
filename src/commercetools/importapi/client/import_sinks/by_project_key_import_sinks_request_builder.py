# Generated file, please do not change!!!
import typing

from ...models.importsinks import ImportSink, ImportSinkDraft, ImportSinkPagedResponse
from .by_project_key_import_sinks_by_import_sink_key_request_builder import (
    ByProjectKeyImportSinksByImportSinkKeyRequestBuilder,
)


class ByProjectKeyImportSinksRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(self, projectKey: str, client: "Client"):
        self._project_key = projectKey
        self._client = client

    def withImportSinkKeyValue(
        self, importSinkKey: str
    ) -> ByProjectKeyImportSinksByImportSinkKeyRequestBuilder:
        return ByProjectKeyImportSinksByImportSinkKeyRequestBuilder(
            importSinkKey=importSinkKey,
            projectKey=self._project_key,
            client=self._client,
        )

    def post(
        self, body: "ImportSinkDraft", *, headers: typing.Dict[str, str] = None
    ) -> "ImportSink":
        """Creates a new import sink.
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/import-sinks",
            params={},
            data_object=body,
            response_object=ImportSink,
            headers={"Content-Type": "application/json", **headers},
        )

    def get(
        self, *, limit: "float", offset: "float", headers: typing.Dict[str, str] = None
    ) -> "ImportSinkPagedResponse":
        """Retrieves all import sinks of a project key.
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/import-sinks",
            params={"limit": limit, "offset": offset},
            response_object=ImportSinkPagedResponse,
            headers=headers,
        )
