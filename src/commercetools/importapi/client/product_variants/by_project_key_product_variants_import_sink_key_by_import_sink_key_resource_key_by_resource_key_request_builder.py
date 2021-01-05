# Generated file, please do not change!!!
import typing

from ...models.importoperations import ImportOperationStatus


class ByProjectKeyProductVariantsImportSinkKeyByImportSinkKeyResourceKeyByResourceKeyRequestBuilder:

    _client: "Client"
    _project_key: str
    _import_sink_key: str
    _resource_key: str

    def __init__(
        self,
        projectKey: str,
        importSinkKey: str,
        resourceKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._import_sink_key = importSinkKey
        self._resource_key = resourceKey
        self._client = client

    def delete(
        self, *, headers: typing.Dict[str, str] = None
    ) -> "ImportOperationStatus":
        """Deletes the product variant given by the resource key."""
        return self._client._delete(
            endpoint=f"/{self._project_key}/product-variants/importSinkKey={self._import_sink_key}/resourceKey={self._resource_key}",
            params={},
            response_class=ImportOperationStatus,
            headers=headers,
        )
