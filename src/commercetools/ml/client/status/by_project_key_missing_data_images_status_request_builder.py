# Generated file, please do not change!!!
import typing

from .by_project_key_missing_data_images_status_by_task_id_request_builder import (
    ByProjectKeyMissingDataImagesStatusByTaskIdRequestBuilder,
)


class ByProjectKeyMissingDataImagesStatusRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def withTaskId(
        self, taskId: str
    ) -> ByProjectKeyMissingDataImagesStatusByTaskIdRequestBuilder:
        return ByProjectKeyMissingDataImagesStatusByTaskIdRequestBuilder(
            taskId=taskId,
            projectKey=self._project_key,
            client=self._client,
        )
