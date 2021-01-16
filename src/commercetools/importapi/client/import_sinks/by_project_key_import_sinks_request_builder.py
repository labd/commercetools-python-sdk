# Generated file, please do not change!!!
import typing

from ...models.errors import ErrorResponse
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
        self,
        body: "ImportSinkDraft",
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> "ImportSink":
        """Creates a new import sink."""
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/import-sinks",
            params={},
            json=body.serialize(),
            headers={"Content-Type": "application/json", **headers},
            options=options,
        )
        if response.status_code == 201:
            return ImportSink.deserialize(response.json())
        elif response.status_code == 400:
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        raise ValueError("Unhandled status code %s", response.status_code)

    def get(
        self,
        *,
        limit: float,
        offset: float,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> "ImportSinkPagedResponse":
        """Retrieves all import sinks of a project key."""
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/import-sinks",
            params={"limit": limit, "offset": offset},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return ImportSinkPagedResponse.deserialize(response.json())
        raise ValueError("Unhandled status code %s", response.status_code)
