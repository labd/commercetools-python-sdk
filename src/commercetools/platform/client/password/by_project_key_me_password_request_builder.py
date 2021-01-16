# Generated file, please do not change!!!
import typing

from ...models.error import ErrorResponse
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
        self,
        body: None,
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["MyCustomer"]:
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/me/password",
            params={},
            headers={"Content-Type": "application/json", **headers},
            options=options,
        )
        if response.status_code == 200:
            return MyCustomer.deserialize(response.json())
        elif response.status_code in (409, 400, 401, 403, 500, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        raise ValueError("Unhandled status code %s", response.status_code)
