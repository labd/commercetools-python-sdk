# Generated file, please do not change!!!
import typing

from ...models.errors import ErrorResponse
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
        self,
        body: "ImportSinkDraft",
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> "ImportSink":
        """Updates the import sink given by the key."""
        headers = {} if headers is None else headers
        response = self._client._put(
            endpoint=f"/{self._project_key}/import-sinks/{self._import_sink_key}",
            params={},
            json=body.serialize(),
            headers={"Content-Type": "application/json", **headers},
            options=options,
        )
        if response.status_code == 200:
            return ImportSink.deserialize(response.json())
        elif response.status_code == 409:
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        raise ValueError("Unhandled status code %s", response.status_code)

    def get(
        self,
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> "ImportSink":
        """Retrieves the import sink given by the key."""
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/import-sinks/{self._import_sink_key}",
            params={},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return ImportSink.deserialize(response.json())
        elif response.status_code == 404:
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        raise ValueError("Unhandled status code %s", response.status_code)

    def delete(
        self,
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> "ImportSink":
        """Deletes the import sink given by the key."""
        headers = {} if headers is None else headers
        response = self._client._delete(
            endpoint=f"/{self._project_key}/import-sinks/{self._import_sink_key}",
            params={},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return ImportSink.deserialize(response.json())
        elif response.status_code == 404:
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        raise ValueError("Unhandled status code %s", response.status_code)
