# Generated file, please do not change!!!
import typing

from ...models.common import Update
from ...models.order_edit import OrderEdit
from ..apply.by_project_key_orders_edits_by_id_apply_request_builder import (
    ByProjectKeyOrdersEditsByIDApplyRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyOrdersEditsByIDRequestBuilder:

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

    def apply(self) -> ByProjectKeyOrdersEditsByIDApplyRequestBuilder:
        return ByProjectKeyOrdersEditsByIDApplyRequestBuilder(
            project_key=self._project_key,
            id=self._id,
            client=self._client,
        )

    def get(
        self, *, expand: str = None, headers: typing.Dict[str, str] = None
    ) -> "OrderEdit":
        """Get OrderEdit by ID"""
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/orders/edits/{self._id}",
            params={"expand": expand},
            response_class=OrderEdit,
            headers=headers,
        )

    def post(
        self,
        body: "Update",
        *,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "OrderEdit":
        """Update OrderEdit by ID"""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/orders/edits/{self._id}",
            params={"expand": expand},
            data_object=body,
            response_class=OrderEdit,
            headers={"Content-Type": "application/json", **headers},
        )

    def delete(
        self, *, version: int, expand: str = None, headers: typing.Dict[str, str] = None
    ) -> "OrderEdit":
        """Delete OrderEdit by ID"""
        headers = {} if headers is None else headers
        return self._client._delete(
            endpoint=f"/{self._project_key}/orders/edits/{self._id}",
            params={"version": version, "expand": expand},
            response_class=OrderEdit,
            headers=headers,
        )
