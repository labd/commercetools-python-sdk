# Generated file, please do not change!!!
import typing

from ...models.common import Update
from ...models.product_type import ProductType


class ByProjectKeyProductTypesByIDRequestBuilder:

    _client: "Client"
    _project_key: str
    _id: str

    def __init__(self, projectKey: str, ID: str, client: "Client"):
        self._project_key = projectKey
        self._id = ID
        self._client = client

    def get(
        self, *, expand: "str" = None, headers: typing.Dict[str, str] = None
    ) -> "ProductType":
        """Get ProductType by ID
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/product-types/{self._id}",
            params={"expand": expand},
            response_object=ProductType,
            headers=headers,
        )

    def post(
        self,
        body: "Update",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ProductType":
        """Update ProductType by ID
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/product-types/{self._id}",
            params={"expand": expand},
            data_object=body,
            response_object=ProductType,
            headers={"Content-Type": "application/json", **headers},
        )

    def delete(
        self,
        *,
        version: "int",
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ProductType":
        """Delete ProductType by ID
        """
        return self._client._delete(
            endpoint=f"/{self._project_key}/product-types/{self._id}",
            params={"version": version, "expand": expand},
            response_object=ProductType,
            headers=headers,
        )