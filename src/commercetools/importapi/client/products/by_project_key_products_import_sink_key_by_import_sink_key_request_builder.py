# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from ...models.importrequests import ImportResponse, ProductImportRequest
from ..import_operations.by_project_key_products_import_sink_key_by_import_sink_key_import_operations_request_builder import (
    ByProjectKeyProductsImportSinkKeyByImportSinkKeyImportOperationsRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyProductsImportSinkKeyByImportSinkKeyRequestBuilder:

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

    def import_operations(
        self,
    ) -> ByProjectKeyProductsImportSinkKeyByImportSinkKeyImportOperationsRequestBuilder:
        return ByProjectKeyProductsImportSinkKeyByImportSinkKeyImportOperationsRequestBuilder(
            project_key=self._project_key,
            import_sink_key=self._import_sink_key,
            client=self._client,
        )

    def post(
        self,
        body: "ProductImportRequest",
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> "ImportResponse":
        """Creates import request for creating new products or updating existing ones."""
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/products/importSinkKey={self._import_sink_key}",
            params={},
            json=body.serialize(),
            headers={"Content-Type": "application/json", **headers},
            options=options,
        )
        if response.status_code in (201, 200):
            return ImportResponse.deserialize(response.json())
        warnings.warn("Unhandled status code %d" % response.status_code)
