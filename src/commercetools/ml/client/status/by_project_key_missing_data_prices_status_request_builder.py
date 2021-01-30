# Generated file, please do not change!!!
import typing
import warnings

from .by_project_key_missing_data_prices_status_by_task_id_request_builder import (
    ByProjectKeyMissingDataPricesStatusByTaskIdRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyMissingDataPricesStatusRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def with_task_id(
        self, task_id: str
    ) -> ByProjectKeyMissingDataPricesStatusByTaskIdRequestBuilder:
        return ByProjectKeyMissingDataPricesStatusByTaskIdRequestBuilder(
            task_id=task_id,
            project_key=self._project_key,
            client=self._client,
        )
