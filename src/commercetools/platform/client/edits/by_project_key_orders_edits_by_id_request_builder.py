# Generated file, please do not change!!!
import typing

from ...models.common import Update
from ...models.order_edit import OrderEdit
from ..apply.by_project_key_orders_edits_by_id_apply_request_builder import (
    ByProjectKeyOrdersEditsByIDApplyRequestBuilder,
)


class ByProjectKeyOrdersEditsByIDRequestBuilder:

    _client: "Client"
    _project_key: str
    _id: str

    def __init__(self, projectKey: str, ID: str, client: "Client"):
        self._project_key = projectKey
        self._id = ID
        self._client = client

    def apply(self) -> ByProjectKeyOrdersEditsByIDApplyRequestBuilder:
        return ByProjectKeyOrdersEditsByIDApplyRequestBuilder(
            projectKey=self._project_key, ID=self._id, client=self._client
        )

    def get(
        self, *, expand: "str" = None, headers: typing.Dict[str, str] = None
    ) -> "OrderEdit":
        """Get OrderEdit by ID
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/orders/edits/{self._id}",
            params={"expand": expand},
            response_object=OrderEdit,
            headers=headers,
        )

    def post(
        self,
        body: "Update",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "OrderEdit":
        """Update OrderEdit by ID
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/orders/edits/{self._id}",
            params={"expand": expand},
            data_object=body,
            response_object=OrderEdit,
            headers={"Content-Type": "application/json", **headers},
        )

    def delete(
        self,
        *,
        version: "int",
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "OrderEdit":
        """Delete OrderEdit by ID
        """
        return self._client._delete(
            endpoint=f"/{self._project_key}/orders/edits/{self._id}",
            params={"version": version, "expand": expand},
            response_object=OrderEdit,
            headers=headers,
        )
