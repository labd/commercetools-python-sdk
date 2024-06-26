# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from .by_project_key_product_variants_import_containers_by_import_container_key_request_builder import (
    ByProjectKeyProductVariantsImportContainersByImportContainerKeyRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyProductVariantsImportContainersRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def with_import_container_key_value(
        self, import_container_key: str
    ) -> ByProjectKeyProductVariantsImportContainersByImportContainerKeyRequestBuilder:
        return ByProjectKeyProductVariantsImportContainersByImportContainerKeyRequestBuilder(
            import_container_key=import_container_key,
            project_key=self._project_key,
            client=self._client,
        )
