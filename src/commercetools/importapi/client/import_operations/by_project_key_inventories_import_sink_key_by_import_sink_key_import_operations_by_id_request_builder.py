# Generated file, please do not change!!!
import typing

from ...models.importoperations import ImportOperation


class ByProjectKeyInventoriesImportSinkKeyByImportSinkKeyImportOperationsByIdRequestBuilder:

    _client: "Client"
    _project_key: str
    _import_sink_key: str
    _id: str

    def __init__(self, projectKey: str, importSinkKey: str, id: str, client: "Client"):
        self._project_key = projectKey
        self._import_sink_key = importSinkKey
        self._id = id
        self._client = client

    def get(self, *, headers: typing.Dict[str, str] = None) -> "ImportOperation":
        """Retrieves the import operation with the given id.
        
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/inventories/importSinkKey={self._import_sink_key}/import-operations/{self._id}",
            params={},
            response_object=ImportOperation,
            headers=headers,
        )
