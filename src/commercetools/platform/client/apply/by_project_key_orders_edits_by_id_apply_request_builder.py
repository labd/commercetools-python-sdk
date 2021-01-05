# Generated file, please do not change!!!
import typing

from ...models.order_edit import OrderEditApply

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyOrdersEditsByIDApplyRequestBuilder:

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

    def post(
        self, body: "OrderEditApply", *, headers: typing.Dict[str, str] = None
    ) -> None:
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/orders/edits/{self._id}/apply",
            params={},
            data_object=body,
            response_class=None,
            headers={"Content-Type": "application/json", **headers},
        )
