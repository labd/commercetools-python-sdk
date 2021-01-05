# Generated file, please do not change!!!
import typing

from ...models.image_search_config import (
    ImageSearchConfigRequest,
    ImageSearchConfigResponse,
)


class ByProjectKeyImageSearchConfigRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def get(
        self, *, headers: typing.Dict[str, str] = None
    ) -> "ImageSearchConfigResponse":
        """Get the current image search config."""
        return self._client._get(
            endpoint=f"/{self._project_key}/image-search/config",
            params={},
            response_class=ImageSearchConfigResponse,
            headers=headers,
        )

    def post(
        self, body: "ImageSearchConfigRequest", *, headers: typing.Dict[str, str] = None
    ) -> "ImageSearchConfigResponse":
        """Endpoint to update the image search config."""
        return self._client._post(
            endpoint=f"/{self._project_key}/image-search/config",
            params={},
            data_object=body,
            response_class=ImageSearchConfigResponse,
            headers={"Content-Type": "application/json", **headers},
        )
