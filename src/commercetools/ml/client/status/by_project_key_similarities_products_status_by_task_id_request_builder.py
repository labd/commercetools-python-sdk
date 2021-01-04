# Generated file, please do not change!!!
import typing

from ...models.similar_products import SimilarProductsTaskStatus


class ByProjectKeySimilaritiesProductsStatusByTaskIdRequestBuilder:

    _client: "Client"
    _project_key: str
    _task_id: str

    def __init__(self, projectKey: str, taskId: str, client: "Client"):
        self._project_key = projectKey
        self._task_id = taskId
        self._client = client

    def get(
        self, *, headers: typing.Dict[str, str] = None
    ) -> "SimilarProductsTaskStatus":
        return self._client._get(
            endpoint=f"/{self._project_key}/similarities/products/status/{self._task_id}",
            params={},
            response_object=SimilarProductsTaskStatus,
            headers=headers,
        )
