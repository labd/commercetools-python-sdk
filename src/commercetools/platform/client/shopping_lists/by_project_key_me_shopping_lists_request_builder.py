# Generated file, please do not change!!!
import typing

from ...models.me import MyShoppingListDraft
from ...models.shopping_list import MyShoppingList, ShoppingListPagedQueryResponse
from .by_project_key_me_shopping_lists_by_id_request_builder import (
    ByProjectKeyMeShoppingListsByIDRequestBuilder,
)
from .by_project_key_me_shopping_lists_key_by_key_request_builder import (
    ByProjectKeyMeShoppingListsKeyByKeyRequestBuilder,
)


class ByProjectKeyMeShoppingListsRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(self, projectKey: str, client: "Client"):
        self._project_key = projectKey
        self._client = client

    def withId(self, ID: str) -> ByProjectKeyMeShoppingListsByIDRequestBuilder:
        return ByProjectKeyMeShoppingListsByIDRequestBuilder(
            ID=ID, projectKey=self._project_key, client=self._client
        )

    def withKey(self, key: str) -> ByProjectKeyMeShoppingListsKeyByKeyRequestBuilder:
        return ByProjectKeyMeShoppingListsKeyByKeyRequestBuilder(
            key=key, projectKey=self._project_key, client=self._client
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
        """Query shopping-lists
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/me/shopping-lists",
            params={
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_object=ShoppingListPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "MyShoppingListDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "MyShoppingList":
        """Create MyShoppingList
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/me/shopping-lists",
            params={"expand": expand},
            data_object=body,
            response_object=MyShoppingList,
            headers={"Content-Type": "application/json", **headers},
        )
