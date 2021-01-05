# Generated file, please do not change!!!
import typing

from ...models.common import Update
from ...models.shopping_list import MyShoppingList


class ByProjectKeyMeShoppingListsKeyByKeyRequestBuilder:

    _client: "Client"
    _project_key: str
    _key: str

    def __init__(
        self,
        projectKey: str,
        key: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._key = key
        self._client = client

    def get(
        self, *, expand: "str" = None, headers: typing.Dict[str, str] = None
    ) -> "MyShoppingList":
        """Get MyShoppingList by key"""
        return self._client._get(
            endpoint=f"/{self._project_key}/me/shopping-lists/key={self._key}",
            params={"expand": expand},
            response_class=MyShoppingList,
            headers=headers,
        )

    def post(
        self,
        body: "Update",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "MyShoppingList":
        """Update MyShoppingList by key"""
        return self._client._post(
            endpoint=f"/{self._project_key}/me/shopping-lists/key={self._key}",
            params={"expand": expand},
            data_object=body,
            response_class=MyShoppingList,
            headers={"Content-Type": "application/json", **headers},
        )

    def delete(
        self,
        *,
        version: "int",
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "MyShoppingList":
        """Delete MyShoppingList by key"""
        return self._client._delete(
            endpoint=f"/{self._project_key}/me/shopping-lists/key={self._key}",
            params={"version": version, "expand": expand},
            response_class=MyShoppingList,
            headers=headers,
        )
