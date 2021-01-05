# Generated file, please do not change!!!
import typing

from ...models.extension import Extension, ExtensionDraft, ExtensionPagedQueryResponse
from .by_project_key_extensions_by_id_request_builder import (
    ByProjectKeyExtensionsByIDRequestBuilder,
)
from .by_project_key_extensions_key_by_key_request_builder import (
    ByProjectKeyExtensionsKeyByKeyRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyExtensionsRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def with_key(self, key: str) -> ByProjectKeyExtensionsKeyByKeyRequestBuilder:
        return ByProjectKeyExtensionsKeyByKeyRequestBuilder(
            key=key,
            project_key=self._project_key,
            client=self._client,
        )

    def with_id(self, id: str) -> ByProjectKeyExtensionsByIDRequestBuilder:
        return ByProjectKeyExtensionsByIDRequestBuilder(
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
    ) -> "ExtensionPagedQueryResponse":
        """Query extensions"""
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
            endpoint=f"/{self._project_key}/extensions",
            params=params,
            response_class=ExtensionPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "ExtensionDraft",
        *,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Extension":
        """Currently, a maximum of 25 extensions can be created per project."""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/extensions",
            params={"expand": expand},
            data_object=body,
            response_class=Extension,
            headers={"Content-Type": "application/json", **headers},
        )
