# Generated file, please do not change!!!
import typing

from ...models.importrequests import ImportResponse, ProductTypeImportRequest
from ..import_operations.by_project_key_product_types_import_sink_key_by_import_sink_key_import_operations_request_builder import (
    ByProjectKeyProductTypesImportSinkKeyByImportSinkKeyImportOperationsRequestBuilder,
)
from .by_project_key_product_types_import_sink_key_by_import_sink_key_resource_key_by_resource_key_request_builder import (
    ByProjectKeyProductTypesImportSinkKeyByImportSinkKeyResourceKeyByResourceKeyRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyProductTypesImportSinkKeyByImportSinkKeyRequestBuilder:

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

    def resource_key_with_resource_key_value(
        self, resource_key: str
    ) -> ByProjectKeyProductTypesImportSinkKeyByImportSinkKeyResourceKeyByResourceKeyRequestBuilder:
        return ByProjectKeyProductTypesImportSinkKeyByImportSinkKeyResourceKeyByResourceKeyRequestBuilder(
            resource_key=resource_key,
            project_key=self._project_key,
            import_sink_key=self._import_sink_key,
            client=self._client,
        )

    def import_operations(
        self,
    ) -> ByProjectKeyProductTypesImportSinkKeyByImportSinkKeyImportOperationsRequestBuilder:
        return ByProjectKeyProductTypesImportSinkKeyByImportSinkKeyImportOperationsRequestBuilder(
            project_key=self._project_key,
            import_sink_key=self._import_sink_key,
            client=self._client,
        )

    def post(
        self,
        body: "ProductTypeImportRequest",
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> "ImportResponse":
        """Creates import request for creating new product types or updating existing ones."""
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/product-types/importSinkKey={self._import_sink_key}",
            params={},
            json=body.serialize(),
            headers={"Content-Type": "application/json", **headers},
            options=options,
        )
        if response.status_code == 201:
            return ImportResponse.deserialize(response.json())
        raise ValueError("Unhandled status code %s", response.status_code)
