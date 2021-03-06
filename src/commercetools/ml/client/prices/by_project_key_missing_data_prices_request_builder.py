# Generated file, please do not change!!!
import typing
import warnings

from ...models.common import TaskToken
from ...models.missing_data import MissingPricesSearchRequest
from ..status.by_project_key_missing_data_prices_status_request_builder import (
    ByProjectKeyMissingDataPricesStatusRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyMissingDataPricesRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def status(self) -> ByProjectKeyMissingDataPricesStatusRequestBuilder:
        return ByProjectKeyMissingDataPricesStatusRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def post(
        self,
        body: "MissingPricesSearchRequest",
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> "TaskToken":
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/missing-data/prices",
            params={},
            json=body.serialize(),
            headers={"Content-Type": "application/json", **headers},
            options=options,
        )
        if response.status_code == 202:
            return TaskToken.deserialize(response.json())
        warnings.warn("Unhandled status code %d" % response.status_code)
