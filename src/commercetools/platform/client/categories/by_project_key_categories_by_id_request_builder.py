# Generated file, please do not change!!!
import typing

from ...models.category import Category
from ...models.common import Update


class ByProjectKeyCategoriesByIDRequestBuilder:

    _client: "Client"
    _project_key: str
    _id: str

    def __init__(
        self,
        projectKey: str,
        ID: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._id = ID
        self._client = client

    def get(
        self, *, expand: "str" = None, headers: typing.Dict[str, str] = None
    ) -> "Category":
        """Get Category by ID"""
        return self._client._get(
            endpoint=f"/{self._project_key}/categories/{self._id}",
            params={"expand": expand},
            response_class=Category,
            headers=headers,
        )

    def post(
        self,
        body: "Update",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Category":
        """Update Category by ID"""
        return self._client._post(
            endpoint=f"/{self._project_key}/categories/{self._id}",
            params={"expand": expand},
            data_object=body,
            response_class=Category,
            headers={"Content-Type": "application/json", **headers},
        )

    def delete(
        self,
        *,
        version: "int",
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Category":
        """Delete Category by ID"""
        return self._client._delete(
            endpoint=f"/{self._project_key}/categories/{self._id}",
            params={"version": version, "expand": expand},
            response_class=Category,
            headers=headers,
        )
