# Generated file, please do not change!!!
import typing

from ...models.customer import CustomerSignInResult
from ...models.me import MyCustomerDraft


class ByProjectKeyMeSignupRequestBuilder:

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
        self, body: "MyCustomerDraft", *, headers: typing.Dict[str, str] = None
    ) -> "CustomerSignInResult":
        return self._client._post(
            endpoint=f"/{self._project_key}/me/signup",
            params={},
            data_object=body,
            response_class=CustomerSignInResult,
            headers={"Content-Type": "application/json", **headers},
        )
