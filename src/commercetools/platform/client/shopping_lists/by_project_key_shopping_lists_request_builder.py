# Generated file, please do not change!!!
import typing

from ...models.shopping_list import (
    ShoppingList,
    ShoppingListDraft,
    ShoppingListPagedQueryResponse,
)
from .by_project_key_shopping_lists_by_id_request_builder import (
    ByProjectKeyShoppingListsByIDRequestBuilder,
)
from .by_project_key_shopping_lists_key_by_key_request_builder import (
    ByProjectKeyShoppingListsKeyByKeyRequestBuilder,
)


class ByProjectKeyShoppingListsRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def withKey(self, key: str) -> ByProjectKeyShoppingListsKeyByKeyRequestBuilder:
        return ByProjectKeyShoppingListsKeyByKeyRequestBuilder(
            key=key,
            projectKey=self._project_key,
            client=self._client,
        )

    def withId(self, ID: str) -> ByProjectKeyShoppingListsByIDRequestBuilder:
        return ByProjectKeyShoppingListsByIDRequestBuilder(
            ID=ID,
            projectKey=self._project_key,
            client=self._client,
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
    ) -> "ShoppingListPagedQueryResponse":
        """Query shopping-lists"""
        return self._client._get(
            endpoint=f"/{self._project_key}/shopping-lists",
            params={
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_class=ShoppingListPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "ShoppingListDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ShoppingList":
        """Create ShoppingList"""
        return self._client._post(
            endpoint=f"/{self._project_key}/shopping-lists",
            params={"expand": expand},
            data_object=body,
            response_class=ShoppingList,
            headers={"Content-Type": "application/json", **headers},
        )
