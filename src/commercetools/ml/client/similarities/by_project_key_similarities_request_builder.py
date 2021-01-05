# Generated file, please do not change!!!
import typing

from ..products.by_project_key_similarities_products_request_builder import (
    ByProjectKeySimilaritiesProductsRequestBuilder,
)


class ByProjectKeySimilaritiesRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def products(self) -> ByProjectKeySimilaritiesProductsRequestBuilder:
        return ByProjectKeySimilaritiesProductsRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )
