# Generated file, please do not change!!!
import typing

from ...models.customer import CustomerSignInResult


class ByProjectKeyMeLoginRequestBuilder:

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
        self, body: None, *, headers: typing.Dict[str, str] = None
    ) -> "CustomerSignInResult":
        return self._client._post(
            endpoint=f"/{self._project_key}/me/login",
            params={},
            data_object=body,
            response_class=CustomerSignInResult,
            headers={"Content-Type": "application/json", **headers},
        )
