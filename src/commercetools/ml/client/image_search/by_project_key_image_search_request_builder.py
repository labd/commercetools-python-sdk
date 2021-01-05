# Generated file, please do not change!!!
import typing

from ...models.image_search import ImageSearchResponse
from ..config.by_project_key_image_search_config_request_builder import (
    ByProjectKeyImageSearchConfigRequestBuilder,
)


class ByProjectKeyImageSearchRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def config(self) -> ByProjectKeyImageSearchConfigRequestBuilder:
        return ByProjectKeyImageSearchConfigRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def post(
        self,
        body: "Buffer",
        *,
        limit: "int" = None,
        offset: "int" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ImageSearchResponse":
        """Accepts an image file and returns similar products from product catalogue."""
        return self._client._post(
            endpoint=f"/{self._project_key}/image-search",
            params={"limit": limit, "offset": offset},
            data_object=body,
            response_class=ImageSearchResponse,
            headers={"Content-Type": "multipart/form-data", **headers},
        )
