# Generated file, please do not change!!!
import typing

from ..general_categories.by_project_key_recommendations_general_categories_request_builder import (
    ByProjectKeyRecommendationsGeneralCategoriesRequestBuilder,
)
from ..project_categories.by_project_key_recommendations_project_categories_request_builder import (
    ByProjectKeyRecommendationsProjectCategoriesRequestBuilder,
)


class ByProjectKeyRecommendationsRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def projectCategories(
        self,
    ) -> ByProjectKeyRecommendationsProjectCategoriesRequestBuilder:
        return ByProjectKeyRecommendationsProjectCategoriesRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def generalCategories(
        self,
    ) -> ByProjectKeyRecommendationsGeneralCategoriesRequestBuilder:
        return ByProjectKeyRecommendationsGeneralCategoriesRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )
