# Generated file, please do not change!!!
import typing

from ...models.common import TaskToken
from ...models.similar_products import SimilarProductSearchRequest
from ..status.by_project_key_similarities_products_status_request_builder import (
    ByProjectKeySimilaritiesProductsStatusRequestBuilder,
)


class ByProjectKeySimilaritiesProductsRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(self, projectKey: str, client: "Client"):
        self._project_key = projectKey
        self._client = client

    def status(self) -> ByProjectKeySimilaritiesProductsStatusRequestBuilder:
        return ByProjectKeySimilaritiesProductsStatusRequestBuilder(
            projectKey=self._project_key, client=self._client
        )

    def post(
        self,
        body: "SimilarProductSearchRequest",
        *,
        headers: typing.Dict[str, str] = None,
    ) -> "TaskToken":
        return self._client._post(
            endpoint=f"/{self._project_key}/similarities/products",
            params={},
            data_object=body,
            response_object=TaskToken,
            headers={"Content-Type": "application/json", **headers},
        )
