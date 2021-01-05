# Generated file, please do not change!!!
import typing

from ...models.api_client import ApiClient


class ByProjectKeyApiClientsByIDRequestBuilder:

    _client: "Client"
    _project_key: str
    _id: str

    def __init__(
        self,
        projectKey: str,
        ID: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._id = ID
        self._client = client

    def get(self, *, headers: typing.Dict[str, str] = None) -> "ApiClient":
        """Get ApiClient by ID"""
        return self._client._get(
            endpoint=f"/{self._project_key}/api-clients/{self._id}",
            params={},
            response_class=ApiClient,
            headers=headers,
        )

    def delete(self, *, headers: typing.Dict[str, str] = None) -> "ApiClient":
        """Delete ApiClient by ID"""
        return self._client._delete(
            endpoint=f"/{self._project_key}/api-clients/{self._id}",
            params={},
            response_class=ApiClient,
            headers=headers,
        )
