# Generated file, please do not change!!!
import typing

from ...models.customer import Customer, CustomerChangePassword


class ByProjectKeyInStoreKeyByStoreKeyCustomersPasswordRequestBuilder:

    _client: "Client"
    _project_key: str
    _store_key: str

    def __init__(
        self,
        projectKey: str,
        storeKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._store_key = storeKey
        self._client = client

    def post(
        self, body: "CustomerChangePassword", *, headers: typing.Dict[str, str] = None
    ) -> "Customer":
        """Change a customers password"""
        return self._client._post(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/customers/password",
            params={},
            data_object=body,
            response_class=Customer,
            headers={"Content-Type": "application/json", **headers},
        )
