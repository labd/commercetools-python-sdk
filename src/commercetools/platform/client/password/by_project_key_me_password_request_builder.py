# Generated file, please do not change!!!
import typing

from ...models.me import MyCustomer
from ..reset.by_project_key_me_password_reset_request_builder import (
    ByProjectKeyMePasswordResetRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyMePasswordRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def reset(self) -> ByProjectKeyMePasswordResetRequestBuilder:
        return ByProjectKeyMePasswordResetRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def post(
        self, body: None, *, headers: typing.Dict[str, str] = None
    ) -> "MyCustomer":
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/me/password",
            params={},
            data_object=body,
            response_class=MyCustomer,
            headers={"Content-Type": "application/json", **headers},
        )
