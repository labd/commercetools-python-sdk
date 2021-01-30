# Generated file, please do not change!!!
import typing
import warnings

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
        self,
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> "SimilarProductsTaskStatus":
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/similarities/products/status/{self._task_id}",
            params={},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return SimilarProductsTaskStatus.deserialize(response.json())
        warnings.warn("Unhandled status code %d" % response.status_code)
