# Generated file, please do not change!!!
import typing

from ...models.general_category_recommendations import (
    GeneralCategoryRecommendationPagedQueryResponse,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyRecommendationsGeneralCategoriesRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def get(
        self,
        *,
        product_image_url: str = None,
        product_name: str,
        limit: int = None,
        offset: int = None,
        confidence_min: float = None,
        confidence_max: float = None,
        headers: typing.Dict[str, str] = None,
    ) -> "GeneralCategoryRecommendationPagedQueryResponse":
        """This endpoint takes arbitrary product names or image URLs and generates recommendations from a general set of categories, which cover a broad range of industries. The full list of supported categories can be found [here](https://docs.commercetools.com/category_recommendations_supported_categories.txt). These are independent of the categories that are actually defined in your project. The main  purpose of this API is to provide a quick way to test the behavior of the category recommendations engine for different names and images. In contrast to the [project-specific endpoint](https://docs.commercetools.com/http-api-projects-categoryrecommendations#project-specific-category-recommendations), this endpoint does not have [activation criteria](https://docs.commercetools.com/http-api-projects-categoryrecommendations#activating-the-api) and is enabled for all projects."""
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/recommendations/general-categories",
            params={
                "productImageUrl": product_image_url,
                "productName": product_name,
                "limit": limit,
                "offset": offset,
                "confidenceMin": confidence_min,
                "confidenceMax": confidence_max,
            },
            response_class=GeneralCategoryRecommendationPagedQueryResponse,
            headers=headers,
        )
