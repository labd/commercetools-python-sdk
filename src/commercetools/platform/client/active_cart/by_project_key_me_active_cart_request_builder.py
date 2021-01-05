# Generated file, please do not change!!!
import typing

from ...models.me import MyCart


class ByProjectKeyMeActiveCartRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def get(self, *, headers: typing.Dict[str, str] = None) -> "MyCart":
        return self._client._get(
            endpoint=f"/{self._project_key}/me/active-cart",
            params={},
            response_class=MyCart,
            headers=headers,
        )
