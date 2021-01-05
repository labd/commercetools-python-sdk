# Generated file, please do not change!!!
import typing

from ...models.customer import CustomerSignInResult
from ...models.me import MyCustomerDraft

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyMeSignupRequestBuilder:

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
        self, body: "MyCustomerDraft", *, headers: typing.Dict[str, str] = None
    ) -> "CustomerSignInResult":
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/me/signup",
            params={},
            data_object=body,
            response_class=CustomerSignInResult,
            headers={"Content-Type": "application/json", **headers},
        )
