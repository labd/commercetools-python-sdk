# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
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
