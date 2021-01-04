# Generated file, please do not change!!!
import typing

from .image_search.by_project_key_image_search_request_builder import (
    ByProjectKeyImageSearchRequestBuilder,
)
from .missing_data.by_project_key_missing_data_request_builder import (
    ByProjectKeyMissingDataRequestBuilder,
)
from .recommendations.by_project_key_recommendations_request_builder import (
    ByProjectKeyRecommendationsRequestBuilder,
)
from .similarities.by_project_key_similarities_request_builder import (
    ByProjectKeySimilaritiesRequestBuilder,
)


class ByProjectKeyRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(self, projectKey: str, client: "Client"):
        self._project_key = projectKey
        self._client = client

    def imageSearch(self) -> ByProjectKeyImageSearchRequestBuilder:
        """Search for similar products using an image as search input.
        
        """
        return ByProjectKeyImageSearchRequestBuilder(
            projectKey=self._project_key, client=self._client
        )

    def recommendations(self) -> ByProjectKeyRecommendationsRequestBuilder:
        return ByProjectKeyRecommendationsRequestBuilder(
            projectKey=self._project_key, client=self._client
        )

    def missingData(self) -> ByProjectKeyMissingDataRequestBuilder:
        return ByProjectKeyMissingDataRequestBuilder(
            projectKey=self._project_key, client=self._client
        )

    def similarities(self) -> ByProjectKeySimilaritiesRequestBuilder:
        return ByProjectKeySimilaritiesRequestBuilder(
            projectKey=self._project_key, client=self._client
        )
