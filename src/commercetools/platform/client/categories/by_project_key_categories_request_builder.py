# Generated file, please do not change!!!
import typing

from ...models.category import Category, CategoryDraft, CategoryPagedQueryResponse
from .by_project_key_categories_by_id_request_builder import (
    ByProjectKeyCategoriesByIDRequestBuilder,
)
from .by_project_key_categories_key_by_key_request_builder import (
    ByProjectKeyCategoriesKeyByKeyRequestBuilder,
)


class ByProjectKeyCategoriesRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(self, projectKey: str, client: "Client"):
        self._project_key = projectKey
        self._client = client

    def withKey(self, key: str) -> ByProjectKeyCategoriesKeyByKeyRequestBuilder:
        return ByProjectKeyCategoriesKeyByKeyRequestBuilder(
            key=key, projectKey=self._project_key, client=self._client
        )

    def withId(self, ID: str) -> ByProjectKeyCategoriesByIDRequestBuilder:
        return ByProjectKeyCategoriesByIDRequestBuilder(
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
    ) -> "CategoryPagedQueryResponse":
        """Query categories
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/categories",
            params={
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_object=CategoryPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "CategoryDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Category":
        """Creating a category produces the CategoryCreated message.
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/categories",
            params={"expand": expand},
            data_object=body,
            response_object=Category,
            headers={"Content-Type": "application/json", **headers},
        )
