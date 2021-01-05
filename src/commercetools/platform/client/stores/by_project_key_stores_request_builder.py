# Generated file, please do not change!!!
import typing

from ...models.store import Store, StoreDraft, StorePagedQueryResponse
from .by_project_key_stores_by_id_request_builder import (
    ByProjectKeyStoresByIDRequestBuilder,
)
from .by_project_key_stores_key_by_key_request_builder import (
    ByProjectKeyStoresKeyByKeyRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyStoresRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def with_key(self, key: str) -> ByProjectKeyStoresKeyByKeyRequestBuilder:
        return ByProjectKeyStoresKeyByKeyRequestBuilder(
            key=key,
            project_key=self._project_key,
            client=self._client,
        )

    def with_id(self, id: str) -> ByProjectKeyStoresByIDRequestBuilder:
        return ByProjectKeyStoresByIDRequestBuilder(
            id=id,
            project_key=self._project_key,
            client=self._client,
        )

    def get(
        self,
        *,
        expand: str = None,
        sort: str = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        where: str = None,
        predicate_var: typing.Dict[str, str] = None,
        headers: typing.Dict[str, str] = None,
    ) -> "StorePagedQueryResponse":
        """Query stores"""
        params = {
            "expand": expand,
            "sort": sort,
            "limit": limit,
            "offset": offset,
            "withTotal": with_total,
            "where": where,
        }
        predicate_var and params.update(
            {f"var.{k}": v for k, v in predicate_var.items()}
        )
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/stores",
            params=params,
            response_class=StorePagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "StoreDraft",
        *,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Store":
        """Create Store"""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/stores",
            params={"expand": expand},
            data_object=body,
            response_class=Store,
            headers={"Content-Type": "application/json", **headers},
        )
