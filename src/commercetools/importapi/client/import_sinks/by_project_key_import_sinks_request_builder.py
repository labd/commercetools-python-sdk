# Generated file, please do not change!!!
import typing

from ...models.importsinks import ImportSink, ImportSinkDraft, ImportSinkPagedResponse
from .by_project_key_import_sinks_by_import_sink_key_request_builder import (
    ByProjectKeyImportSinksByImportSinkKeyRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyImportSinksRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def with_import_sink_key_value(
        self, import_sink_key: str
    ) -> ByProjectKeyImportSinksByImportSinkKeyRequestBuilder:
        return ByProjectKeyImportSinksByImportSinkKeyRequestBuilder(
            import_sink_key=import_sink_key,
            project_key=self._project_key,
            client=self._client,
        )

    def post(
        self, body: "ImportSinkDraft", *, headers: typing.Dict[str, str] = None
    ) -> "ImportSink":
        """Creates a new import sink."""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/import-sinks",
            params={},
            data_object=body,
            response_class=ImportSink,
            headers={"Content-Type": "application/json", **headers},
        )

    def get(
        self,
        *,
        limit: float = None,
        offset: float = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ImportSinkPagedResponse":
        """Retrieves all import sinks of a project key."""
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/import-sinks",
            params={"limit": limit, "offset": offset},
            response_class=ImportSinkPagedResponse,
            headers=headers,
        )
