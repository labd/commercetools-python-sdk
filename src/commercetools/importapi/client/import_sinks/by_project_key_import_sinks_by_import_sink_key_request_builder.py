# Generated file, please do not change!!!
import typing

from ...models.importsinks import ImportSink, ImportSinkDraft


class ByProjectKeyImportSinksByImportSinkKeyRequestBuilder:

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

    def put(
        self, body: "ImportSinkDraft", *, headers: typing.Dict[str, str] = None
    ) -> "ImportSink":
        """Updates the import sink given by the key."""
        return self._client._put(
            endpoint=f"/{self._project_key}/import-sinks/{self._import_sink_key}",
            params={},
            data_object=body,
            response_class=ImportSink,
            headers={"Content-Type": "application/json", **headers},
        )

    def get(self, *, headers: typing.Dict[str, str] = None) -> "ImportSink":
        """Retrieves the import sink given by the key."""
        return self._client._get(
            endpoint=f"/{self._project_key}/import-sinks/{self._import_sink_key}",
            params={},
            response_class=ImportSink,
            headers=headers,
        )

    def delete(self, *, headers: typing.Dict[str, str] = None) -> "ImportSink":
        """Deletes the import sink given by the key."""
        return self._client._delete(
            endpoint=f"/{self._project_key}/import-sinks/{self._import_sink_key}",
            params={},
            response_class=ImportSink,
            headers=headers,
        )
