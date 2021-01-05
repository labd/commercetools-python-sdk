# Generated file, please do not change!!!
import typing

from ...models.cart import Cart, ReplicaCartDraft

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyCartsReplicateRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def post(
        self, body: "ReplicaCartDraft", *, headers: typing.Dict[str, str] = None
    ) -> "Cart":
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/carts/replicate",
            params={},
            data_object=body,
            response_class=Cart,
            headers={"Content-Type": "application/json", **headers},
        )
