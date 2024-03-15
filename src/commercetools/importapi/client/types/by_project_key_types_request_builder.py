# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from ..import_containers.by_project_key_types_import_containers_request_builder import (
    ByProjectKeyTypesImportContainersRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyTypesRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def import_containers(self) -> ByProjectKeyTypesImportContainersRequestBuilder:
        return ByProjectKeyTypesImportContainersRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )
