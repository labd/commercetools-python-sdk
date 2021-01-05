# Generated file, please do not change!!!
import typing

from ...models.customer import Customer, CustomerResetPassword


class ByProjectKeyCustomersPasswordResetRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(self, projectKey: str, client: "Client"):
        self._project_key = projectKey
        self._client = client

    def post(
        self, body: "CustomerResetPassword", *, headers: typing.Dict[str, str] = None
    ) -> "Customer":
        """Set a new password using a token.
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/customers/password/reset",
            params={},
            data_object=body,
            response_object=Customer,
            headers={"Content-Type": "application/json", **headers},
        )