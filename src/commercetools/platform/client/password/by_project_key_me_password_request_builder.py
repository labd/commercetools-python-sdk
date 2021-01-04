# Generated file, please do not change!!!
import typing

from ...models.me import MyCustomer
from ..reset.by_project_key_me_password_reset_request_builder import (
    ByProjectKeyMePasswordResetRequestBuilder,
)


class ByProjectKeyMePasswordRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(self, projectKey: str, client: "Client"):
        self._project_key = projectKey
        self._client = client

    def reset(self) -> ByProjectKeyMePasswordResetRequestBuilder:
        return ByProjectKeyMePasswordResetRequestBuilder(
            projectKey=self._project_key, client=self._client
        )

    def post(
        self, body: None, *, headers: typing.Dict[str, str] = None
    ) -> "MyCustomer":
        return self._client._post(
            endpoint=f"/{self._project_key}/me/password",
            params={},
            data_object=body,
            response_object=MyCustomer,
            headers={"Content-Type": "application/json", **headers},
        )
