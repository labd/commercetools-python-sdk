# Generated file, please do not change!!!
import typing

from ...models.missing_data import MissingImagesTaskStatus


class ByProjectKeyMissingDataImagesStatusByTaskIdRequestBuilder:

    _client: "Client"
    _project_key: str
    _task_id: str

    def __init__(self, projectKey: str, taskId: str, client: "Client"):
        self._project_key = projectKey
        self._task_id = taskId
        self._client = client

    def get(
        self, *, headers: typing.Dict[str, str] = None
    ) -> "MissingImagesTaskStatus":
        return self._client._get(
            endpoint=f"/{self._project_key}/missing-data/images/status/{self._task_id}",
            params={},
            response_object=MissingImagesTaskStatus,
            headers=headers,
        )
