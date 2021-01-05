# Generated file, please do not change!!!
import typing

from ...models.common import TaskToken
from ...models.missing_data import MissingPricesSearchRequest
from ..status.by_project_key_missing_data_prices_status_request_builder import (
    ByProjectKeyMissingDataPricesStatusRequestBuilder,
)


class ByProjectKeyMissingDataPricesRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def status(self) -> ByProjectKeyMissingDataPricesStatusRequestBuilder:
        return ByProjectKeyMissingDataPricesStatusRequestBuilder(
            projectKey=self._project_key,
            client=self._client,
        )

    def post(
        self,
        body: "MissingPricesSearchRequest",
        *,
        headers: typing.Dict[str, str] = None,
    ) -> "TaskToken":
        return self._client._post(
            endpoint=f"/{self._project_key}/missing-data/prices",
            params={},
            data_object=body,
            response_class=TaskToken,
            headers={"Content-Type": "application/json", **headers},
        )
