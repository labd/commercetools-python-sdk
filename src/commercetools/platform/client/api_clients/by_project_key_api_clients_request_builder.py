# Generated file, please do not change!!!
import typing

from ...models.api_client import ApiClient, ApiClientDraft, ApiClientPagedQueryResponse
from .by_project_key_api_clients_by_id_request_builder import (
    ByProjectKeyApiClientsByIDRequestBuilder,
)


class ByProjectKeyApiClientsRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def withId(self, ID: str) -> ByProjectKeyApiClientsByIDRequestBuilder:
        return ByProjectKeyApiClientsByIDRequestBuilder(
            ID=ID,
            projectKey=self._project_key,
            client=self._client,
        )

    def get(
        self,
        *,
        expand: "str" = None,
        sort: "str" = None,
        limit: "int" = None,
        offset: "int" = None,
        with_total: "bool" = None,
        where: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ApiClientPagedQueryResponse":
        """Query api-clients"""
        return self._client._get(
            endpoint=f"/{self._project_key}/api-clients",
            params={
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_class=ApiClientPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "ApiClientDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ApiClient":
        """Create ApiClient"""
        return self._client._post(
            endpoint=f"/{self._project_key}/api-clients",
            params={"expand": expand},
            data_object=body,
            response_class=ApiClient,
            headers={"Content-Type": "application/json", **headers},
        )
