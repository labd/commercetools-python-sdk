# Generated file, please do not change!!!
import typing

from ...models.cart import Cart, ReplicaCartDraft


class ByProjectKeyCartsReplicateRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def post(
        self, body: "ReplicaCartDraft", *, headers: typing.Dict[str, str] = None
    ) -> "Cart":
        return self._client._post(
            endpoint=f"/{self._project_key}/carts/replicate",
            params={},
            data_object=body,
            response_class=Cart,
            headers={"Content-Type": "application/json", **headers},
        )
