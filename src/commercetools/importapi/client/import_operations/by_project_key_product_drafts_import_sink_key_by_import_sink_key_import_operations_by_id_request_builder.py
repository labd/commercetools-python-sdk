# Generated file, please do not change!!!
import typing

from ...models.importoperations import ImportOperation

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyProductDraftsImportSinkKeyByImportSinkKeyImportOperationsByIdRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _import_sink_key: str
    _id: str

    def __init__(
        self,
        project_key: str,
        import_sink_key: str,
        id: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._import_sink_key = import_sink_key
        self._id = id
        self._client = client

    def get(self, *, headers: typing.Dict[str, str] = None) -> "ImportOperation":
        """Retrieves the import operation with the given id."""
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/product-drafts/importSinkKey={self._import_sink_key}/import-operations/{self._id}",
            params={},
            response_class=ImportOperation,
            headers=headers,
        )
