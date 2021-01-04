# Generated file, please do not change!!!
import typing

from ...models.customer import Customer, CustomerChangePassword


class ByProjectKeyCustomersPasswordRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(self, projectKey: str, client: "Client"):
        self._project_key = projectKey
        self._client = client

    def post(
        self, body: "CustomerChangePassword", *, headers: typing.Dict[str, str] = None
    ) -> "Customer":
        """Change a customers password
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/customers/password",
            params={},
            data_object=body,
            response_object=Customer,
            headers={"Content-Type": "application/json", **headers},
        )
