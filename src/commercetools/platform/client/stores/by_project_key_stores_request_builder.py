# Generated file, please do not change!!!
import typing

from ...models.store import Store, StoreDraft, StorePagedQueryResponse
from .by_project_key_stores_by_id_request_builder import (
    ByProjectKeyStoresByIDRequestBuilder,
)
from .by_project_key_stores_key_by_key_request_builder import (
    ByProjectKeyStoresKeyByKeyRequestBuilder,
)


class ByProjectKeyStoresRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def withKey(self, key: str) -> ByProjectKeyStoresKeyByKeyRequestBuilder:
        return ByProjectKeyStoresKeyByKeyRequestBuilder(
            key=key,
            projectKey=self._project_key,
            client=self._client,
        )

    def withId(self, ID: str) -> ByProjectKeyStoresByIDRequestBuilder:
        return ByProjectKeyStoresByIDRequestBuilder(
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
    ) -> "StorePagedQueryResponse":
        """Query stores"""
        return self._client._get(
            endpoint=f"/{self._project_key}/stores",
            params={
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_class=StorePagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "StoreDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Store":
        """Create Store"""
        return self._client._post(
            endpoint=f"/{self._project_key}/stores",
            params={"expand": expand},
            data_object=body,
            response_class=Store,
            headers={"Content-Type": "application/json", **headers},
        )
