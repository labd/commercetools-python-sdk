# Generated file, please do not change!!!
import typing

from ...models.similar_products import SimilarProductsTaskStatus

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeySimilaritiesProductsStatusByTaskIdRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _task_id: str

    def __init__(
        self,
        project_key: str,
        task_id: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._task_id = task_id
        self._client = client

    def get(
        self, *, headers: typing.Dict[str, str] = None
    ) -> "SimilarProductsTaskStatus":
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/similarities/products/status/{self._task_id}",
            params={},
            response_class=SimilarProductsTaskStatus,
            headers=headers,
        )
