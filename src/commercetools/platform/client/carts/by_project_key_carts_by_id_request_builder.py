# Generated file, please do not change!!!
import typing

from ...models.cart import Cart
from ...models.common import Update

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyCartsByIDRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _id: str

    def __init__(
        self,
        project_key: str,
        id: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._id = id
        self._client = client

    def get(
        self, *, expand: str = None, headers: typing.Dict[str, str] = None
    ) -> "Cart":
        """The cart may not contain up-to-date prices, discounts etc.
        If you want to ensure they're up-to-date, send an Update request with the Recalculate update action instead.

        """
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/carts/{self._id}",
            params={"expand": expand},
            response_class=Cart,
            headers=headers,
        )

    def post(
        self,
        body: "Update",
        *,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Cart":
        """Update Cart by ID"""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/carts/{self._id}",
            params={"expand": expand},
            data_object=body,
            response_class=Cart,
            headers={"Content-Type": "application/json", **headers},
        )

    def delete(
        self,
        *,
        data_erasure: bool = None,
        version: int,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Cart":
        """Delete Cart by ID"""
        headers = {} if headers is None else headers
        return self._client._delete(
            endpoint=f"/{self._project_key}/carts/{self._id}",
            params={"dataErasure": data_erasure, "version": version, "expand": expand},
            response_class=Cart,
            headers=headers,
        )
