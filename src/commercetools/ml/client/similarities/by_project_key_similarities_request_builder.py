# Generated file, please do not change!!!
import typing
import warnings

from ..products.by_project_key_similarities_products_request_builder import (
    ByProjectKeySimilaritiesProductsRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeySimilaritiesRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def products(self) -> ByProjectKeySimilaritiesProductsRequestBuilder:
        return ByProjectKeySimilaritiesProductsRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )
