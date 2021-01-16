# Generated file, please do not change!!!
import typing

from ...models.error import ErrorResponse
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

    def get(
        self,
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["MyCart"]:
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/me/active-cart",
            params={},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return MyCart.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        raise ValueError("Unhandled status code %s", response.status_code)
