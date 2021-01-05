# Generated file, please do not change!!!
import typing

from ...models.importrequests import CategoryImportRequest, ImportResponse
from ..import_operations.by_project_key_categories_import_sink_key_by_import_sink_key_import_operations_request_builder import (
    ByProjectKeyCategoriesImportSinkKeyByImportSinkKeyImportOperationsRequestBuilder,
)
from .by_project_key_categories_import_sink_key_by_import_sink_key_resource_key_by_resource_key_request_builder import (
    ByProjectKeyCategoriesImportSinkKeyByImportSinkKeyResourceKeyByResourceKeyRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyCategoriesImportSinkKeyByImportSinkKeyRequestBuilder:

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
    ) -> ByProjectKeyCategoriesImportSinkKeyByImportSinkKeyResourceKeyByResourceKeyRequestBuilder:
        return ByProjectKeyCategoriesImportSinkKeyByImportSinkKeyResourceKeyByResourceKeyRequestBuilder(
            resource_key=resource_key,
            project_key=self._project_key,
            import_sink_key=self._import_sink_key,
            client=self._client,
        )

    def import_operations(
        self,
    ) -> ByProjectKeyCategoriesImportSinkKeyByImportSinkKeyImportOperationsRequestBuilder:
        return ByProjectKeyCategoriesImportSinkKeyByImportSinkKeyImportOperationsRequestBuilder(
            project_key=self._project_key,
            import_sink_key=self._import_sink_key,
            client=self._client,
        )

    def post(
        self, body: "CategoryImportRequest", *, headers: typing.Dict[str, str] = None
    ) -> "ImportResponse":
        """Creates import request for creating new categories or updating existing ones."""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/categories/importSinkKey={self._import_sink_key}",
            params={},
            data_object=body,
            response_class=ImportResponse,
            headers={"Content-Type": "application/json", **headers},
        )
