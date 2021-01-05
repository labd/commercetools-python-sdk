# Generated file, please do not change!!!
import typing

from ...models.me import MyCart

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyMeActiveCartRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def get(self, *, headers: typing.Dict[str, str] = None) -> "MyCart":
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/me/active-cart",
            params={},
            response_class=MyCart,
            headers=headers,
        )
