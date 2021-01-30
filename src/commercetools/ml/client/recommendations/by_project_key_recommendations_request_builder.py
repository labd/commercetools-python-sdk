# Generated file, please do not change!!!
import typing
import warnings

from ..general_categories.by_project_key_recommendations_general_categories_request_builder import (
    ByProjectKeyRecommendationsGeneralCategoriesRequestBuilder,
)
from ..project_categories.by_project_key_recommendations_project_categories_request_builder import (
    ByProjectKeyRecommendationsProjectCategoriesRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyRecommendationsRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def project_categories(
        self,
    ) -> ByProjectKeyRecommendationsProjectCategoriesRequestBuilder:
        return ByProjectKeyRecommendationsProjectCategoriesRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def general_categories(
        self,
    ) -> ByProjectKeyRecommendationsGeneralCategoriesRequestBuilder:
        return ByProjectKeyRecommendationsGeneralCategoriesRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )
