# Generated file, please do not change!!!
import typing

from .by_project_key_similarities_products_status_by_task_id_request_builder import (
    ByProjectKeySimilaritiesProductsStatusByTaskIdRequestBuilder,
)


class ByProjectKeySimilaritiesProductsStatusRequestBuilder:

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
    ) -> ByProjectKeySimilaritiesProductsStatusByTaskIdRequestBuilder:
        return ByProjectKeySimilaritiesProductsStatusByTaskIdRequestBuilder(
            taskId=taskId,
            projectKey=self._project_key,
            client=self._client,
        )
