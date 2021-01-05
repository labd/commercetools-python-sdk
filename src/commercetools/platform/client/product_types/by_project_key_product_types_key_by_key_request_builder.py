# Generated file, please do not change!!!
import typing

from ...models.common import Update
from ...models.product_type import ProductType

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyProductTypesKeyByKeyRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _key: str

    def __init__(
        self,
        project_key: str,
        key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._key = key
        self._client = client

    def get(
        self, *, expand: str = None, headers: typing.Dict[str, str] = None
    ) -> "ProductType":
        """Get ProductType by key"""
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/product-types/key={self._key}",
            params={"expand": expand},
            response_class=ProductType,
            headers=headers,
        )

    def post(
        self,
        body: "Update",
        *,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ProductType":
        """Update ProductType by key"""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/product-types/key={self._key}",
            params={"expand": expand},
            data_object=body,
            response_class=ProductType,
            headers={"Content-Type": "application/json", **headers},
        )

    def delete(
        self, *, version: int, expand: str = None, headers: typing.Dict[str, str] = None
    ) -> "ProductType":
        """Delete ProductType by key"""
        headers = {} if headers is None else headers
        return self._client._delete(
            endpoint=f"/{self._project_key}/product-types/key={self._key}",
            params={"version": version, "expand": expand},
            response_class=ProductType,
            headers=headers,
        )
