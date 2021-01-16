# Generated file, please do not change!!!
import typing

from ...models.image_search_config import (
    ImageSearchConfigRequest,
    ImageSearchConfigResponse,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyImageSearchConfigRequestBuilder:

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
    ) -> "ImageSearchConfigResponse":
        """Get the current image search config."""
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/image-search/config",
            params={},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return ImageSearchConfigResponse.deserialize(response.json())
        raise ValueError("Unhandled status code %s", response.status_code)

    def post(
        self,
        body: "ImageSearchConfigRequest",
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> "ImageSearchConfigResponse":
        """Endpoint to update the image search config."""
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/image-search/config",
            params={},
            json=body.serialize(),
            headers={"Content-Type": "application/json", **headers},
            options=options,
        )
        if response.status_code == 200:
            return ImageSearchConfigResponse.deserialize(response.json())
        raise ValueError("Unhandled status code %s", response.status_code)
