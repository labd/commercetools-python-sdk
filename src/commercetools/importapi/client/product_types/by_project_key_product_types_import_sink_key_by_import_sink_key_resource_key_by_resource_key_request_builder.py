# Generated file, please do not change!!!
import typing

from ...models.importoperations import ImportOperationStatus


class ByProjectKeyProductTypesImportSinkKeyByImportSinkKeyResourceKeyByResourceKeyRequestBuilder:

    _client: "Client"
    _project_key: str
    _import_sink_key: str
    _resource_key: str

    def __init__(
        self, projectKey: str, importSinkKey: str, resourceKey: str, client: "Client"
    ):
        self._project_key = projectKey
        self._import_sink_key = importSinkKey
        self._resource_key = resourceKey
        self._client = client

    def delete(
        self, *, headers: typing.Dict[str, str] = None
    ) -> "ImportOperationStatus":
        """Deletes the product type given by the resource key.
        """
        return self._client._delete(
            endpoint=f"/{self._project_key}/product-types/importSinkKey={self._import_sink_key}/resourceKey={self._resource_key}",
            params={},
            response_object=ImportOperationStatus,
            headers=headers,
        )
