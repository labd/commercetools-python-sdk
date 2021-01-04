# Generated file, please do not change!!!
import typing

from .by_project_key_recommendations_project_categories_by_product_id_request_builder import (
    ByProjectKeyRecommendationsProjectCategoriesByProductIdRequestBuilder,
)


class ByProjectKeyRecommendationsProjectCategoriesRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(self, projectKey: str, client: "Client"):
        self._project_key = projectKey
        self._client = client

    def withProductId(
        self, productId: str
    ) -> ByProjectKeyRecommendationsProjectCategoriesByProductIdRequestBuilder:
        return ByProjectKeyRecommendationsProjectCategoriesByProductIdRequestBuilder(
            productId=productId, projectKey=self._project_key, client=self._client
        )
