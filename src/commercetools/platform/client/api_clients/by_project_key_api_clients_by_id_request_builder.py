# Generated file, please do not change!!!
import typing

from ...models.api_client import ApiClient

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyApiClientsByIDRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _id: str

    def __init__(
        self,
        project_key: str,
        id: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._id = id
        self._client = client

    def get(self, *, headers: typing.Dict[str, str] = None) -> "ApiClient":
        """Get ApiClient by ID"""
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/api-clients/{self._id}",
            params={},
            response_class=ApiClient,
            headers=headers,
        )

    def delete(self, *, headers: typing.Dict[str, str] = None) -> "ApiClient":
        """Delete ApiClient by ID"""
        headers = {} if headers is None else headers
        return self._client._delete(
            endpoint=f"/{self._project_key}/api-clients/{self._id}",
            params={},
            response_class=ApiClient,
            headers=headers,
        )
