# Generated file, please do not change!!!
import typing

from ...models.importsinks import ImportSink, ImportSinkDraft

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyImportSinksByImportSinkKeyRequestBuilder:

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

    def put(
        self, body: "ImportSinkDraft", *, headers: typing.Dict[str, str] = None
    ) -> "ImportSink":
        """Updates the import sink given by the key."""
        headers = {} if headers is None else headers
        return self._client._put(
            endpoint=f"/{self._project_key}/import-sinks/{self._import_sink_key}",
            params={},
            data_object=body,
            response_class=ImportSink,
            headers={"Content-Type": "application/json", **headers},
        )

    def get(self, *, headers: typing.Dict[str, str] = None) -> "ImportSink":
        """Retrieves the import sink given by the key."""
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/import-sinks/{self._import_sink_key}",
            params={},
            response_class=ImportSink,
            headers=headers,
        )

    def delete(self, *, headers: typing.Dict[str, str] = None) -> "ImportSink":
        """Deletes the import sink given by the key."""
        headers = {} if headers is None else headers
        return self._client._delete(
            endpoint=f"/{self._project_key}/import-sinks/{self._import_sink_key}",
            params={},
            response_class=ImportSink,
            headers=headers,
        )
