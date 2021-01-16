# Generated file, please do not change!!!
import typing

from ...models.category_recommendations import (
    ProjectCategoryRecommendationPagedQueryResponse,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyRecommendationsProjectCategoriesByProductIdRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _product_id: str

    def __init__(
        self,
        project_key: str,
        product_id: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._product_id = product_id
        self._client = client

    def get(
        self,
        *,
        limit: int = None,
        offset: int = None,
        staged: bool = None,
        confidence_min: float = None,
        confidence_max: float = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> "ProjectCategoryRecommendationPagedQueryResponse":
        """Response Representation: PagedQueryResult with a results array of ProjectCategoryrecommendation, sorted by confidence scores in descending order and the meta information of ProjectCategoryrecommendationMeta."""
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/recommendations/project-categories/{self._product_id}",
            params={
                "limit": limit,
                "offset": offset,
                "staged": staged,
                "confidenceMin": confidence_min,
                "confidenceMax": confidence_max,
            },
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return ProjectCategoryRecommendationPagedQueryResponse.deserialize(
                response.json()
            )
        raise ValueError("Unhandled status code %s", response.status_code)
