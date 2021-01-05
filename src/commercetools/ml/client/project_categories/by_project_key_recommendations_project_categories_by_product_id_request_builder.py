# Generated file, please do not change!!!
import typing

from ...models.category_recommendations import (
    ProjectCategoryRecommendationPagedQueryResponse,
)


class ByProjectKeyRecommendationsProjectCategoriesByProductIdRequestBuilder:

    _client: "Client"
    _project_key: str
    _product_id: str

    def __init__(
        self,
        projectKey: str,
        productId: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._product_id = productId
        self._client = client

    def get(
        self,
        *,
        limit: "int" = None,
        offset: "int" = None,
        staged: "bool" = None,
        confidence_min: "float" = None,
        confidence_max: "float" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ProjectCategoryRecommendationPagedQueryResponse":
        """Response Representation: PagedQueryResult with a results array of ProjectCategoryrecommendation, sorted by confidence scores in descending order and the meta information of ProjectCategoryrecommendationMeta."""
        return self._client._get(
            endpoint=f"/{self._project_key}/recommendations/project-categories/{self._product_id}",
            params={
                "limit": limit,
                "offset": offset,
                "staged": staged,
                "confidenceMin": confidence_min,
                "confidenceMax": confidence_max,
            },
            response_class=ProjectCategoryRecommendationPagedQueryResponse,
            headers=headers,
        )
