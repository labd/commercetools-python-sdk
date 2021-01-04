# Generated file, please do not change!!!
import typing

from ...models.order_edit import OrderEditApply


class ByProjectKeyOrdersEditsByIDApplyRequestBuilder:

    _client: "Client"
    _project_key: str
    _id: str

    def __init__(self, projectKey: str, ID: str, client: "Client"):
        self._project_key = projectKey
        self._id = ID
        self._client = client

    def post(
        self, body: "OrderEditApply", *, headers: typing.Dict[str, str] = None
    ) -> None:
        return self._client._post(
            endpoint=f"/{self._project_key}/orders/edits/{self._id}/apply",
            params={},
            data_object=body,
            response_object=None,
            headers={"Content-Type": "application/json", **headers},
        )
