# Generated file, please do not change!!!
import typing

from ...models.me import MyCustomer

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyMePasswordResetRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def post(self, *, headers: typing.Dict[str, str] = None) -> "MyCustomer":
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/me/password/reset",
            params={},
            response_class=MyCustomer,
            headers=headers,
        )
