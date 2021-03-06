# Generated file, please do not change!!!
import typing
import warnings

from ...models.importoperations import ImportOperationStatus

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyPricesImportSinkKeyByImportSinkKeyResourceKeyByResourceKeyRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _import_sink_key: str
    _resource_key: str

    def __init__(
        self,
        project_key: str,
        import_sink_key: str,
        resource_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._import_sink_key = import_sink_key
        self._resource_key = resource_key
        self._client = client

    def delete(
        self,
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> "ImportOperationStatus":
        """Deletes the price given by the resource key."""
        headers = {} if headers is None else headers
        response = self._client._delete(
            endpoint=f"/{self._project_key}/prices/importSinkKey={self._import_sink_key}/resourceKey={self._resource_key}",
            params={},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return ImportOperationStatus.deserialize(response.json())
        warnings.warn("Unhandled status code %d" % response.status_code)
