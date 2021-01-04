# Generated file, please do not change!!!
import typing

from ...models.tax_category import (
    TaxCategory,
    TaxCategoryDraft,
    TaxCategoryPagedQueryResponse,
)
from .by_project_key_tax_categories_by_id_request_builder import (
    ByProjectKeyTaxCategoriesByIDRequestBuilder,
)
from .by_project_key_tax_categories_key_by_key_request_builder import (
    ByProjectKeyTaxCategoriesKeyByKeyRequestBuilder,
)


class ByProjectKeyTaxCategoriesRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(self, projectKey: str, client: "Client"):
        self._project_key = projectKey
        self._client = client

    def withKey(self, key: str) -> ByProjectKeyTaxCategoriesKeyByKeyRequestBuilder:
        return ByProjectKeyTaxCategoriesKeyByKeyRequestBuilder(
            key=key, projectKey=self._project_key, client=self._client
        )

    def withId(self, ID: str) -> ByProjectKeyTaxCategoriesByIDRequestBuilder:
        return ByProjectKeyTaxCategoriesByIDRequestBuilder(
            ID=ID, projectKey=self._project_key, client=self._client
        )

    def get(
        self,
        *,
        expand: "str" = None,
        sort: "str" = None,
        limit: "int" = None,
        offset: "int" = None,
        with_total: "bool" = None,
        where: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "TaxCategoryPagedQueryResponse":
        """Query tax-categories
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/tax-categories",
            params={
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_object=TaxCategoryPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "TaxCategoryDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "TaxCategory":
        """Create TaxCategory
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/tax-categories",
            params={"expand": expand},
            data_object=body,
            response_object=TaxCategory,
            headers={"Content-Type": "application/json", **headers},
        )
