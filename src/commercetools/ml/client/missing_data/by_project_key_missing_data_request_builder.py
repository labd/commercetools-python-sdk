# Generated file, please do not change!!!
import typing

from ..attributes.by_project_key_missing_data_attributes_request_builder import (
    ByProjectKeyMissingDataAttributesRequestBuilder,
)
from ..images.by_project_key_missing_data_images_request_builder import (
    ByProjectKeyMissingDataImagesRequestBuilder,
)
from ..prices.by_project_key_missing_data_prices_request_builder import (
    ByProjectKeyMissingDataPricesRequestBuilder,
)


class ByProjectKeyMissingDataRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(self, projectKey: str, client: "Client"):
        self._project_key = projectKey
        self._client = client

    def attributes(self) -> ByProjectKeyMissingDataAttributesRequestBuilder:
        return ByProjectKeyMissingDataAttributesRequestBuilder(
            projectKey=self._project_key, client=self._client
        )

    def images(self) -> ByProjectKeyMissingDataImagesRequestBuilder:
        return ByProjectKeyMissingDataImagesRequestBuilder(
            projectKey=self._project_key, client=self._client
        )

    def prices(self) -> ByProjectKeyMissingDataPricesRequestBuilder:
        return ByProjectKeyMissingDataPricesRequestBuilder(
            projectKey=self._project_key, client=self._client
        )
