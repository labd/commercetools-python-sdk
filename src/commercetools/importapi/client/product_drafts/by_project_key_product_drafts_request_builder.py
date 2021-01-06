# Generated file, please do not change!!!
import typing

from .by_project_key_product_drafts_import_sink_key_by_import_sink_key_request_builder import (
    ByProjectKeyProductDraftsImportSinkKeyByImportSinkKeyRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyProductDraftsRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def import_sink_key_with_import_sink_key_value(
        self, import_sink_key: str
    ) -> ByProjectKeyProductDraftsImportSinkKeyByImportSinkKeyRequestBuilder:
        return ByProjectKeyProductDraftsImportSinkKeyByImportSinkKeyRequestBuilder(
            import_sink_key=import_sink_key,
            project_key=self._project_key,
            client=self._client,
        )
