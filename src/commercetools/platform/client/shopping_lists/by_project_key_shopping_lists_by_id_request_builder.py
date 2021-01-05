# Generated file, please do not change!!!
import typing

from ...models.common import Update
from ...models.shopping_list import ShoppingList


class ByProjectKeyShoppingListsByIDRequestBuilder:

    _client: "Client"
    _project_key: str
    _id: str

    def __init__(self, projectKey: str, ID: str, client: "Client"):
        self._project_key = projectKey
        self._id = ID
        self._client = client

    def get(
        self, *, expand: "str" = None, headers: typing.Dict[str, str] = None
    ) -> "ShoppingList":
        """Gets a shopping list by ID.
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/shopping-lists/{self._id}",
            params={"expand": expand},
            response_object=ShoppingList,
            headers=headers,
        )

    def post(
        self,
        body: "Update",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ShoppingList":
        """Update ShoppingList by ID
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/shopping-lists/{self._id}",
            params={"expand": expand},
            data_object=body,
            response_object=ShoppingList,
            headers={"Content-Type": "application/json", **headers},
        )

    def delete(
        self,
        *,
        data_erasure: "bool" = None,
        version: "int",
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ShoppingList":
        """Delete ShoppingList by ID
        """
        return self._client._delete(
            endpoint=f"/{self._project_key}/shopping-lists/{self._id}",
            params={"dataErasure": data_erasure, "version": version, "expand": expand},
            response_object=ShoppingList,
            headers=headers,
        )