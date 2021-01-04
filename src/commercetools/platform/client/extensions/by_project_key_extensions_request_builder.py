# Generated file, please do not change!!!
import typing

from ...models.extension import Extension, ExtensionDraft, ExtensionPagedQueryResponse
from .by_project_key_extensions_by_id_request_builder import (
    ByProjectKeyExtensionsByIDRequestBuilder,
)
from .by_project_key_extensions_key_by_key_request_builder import (
    ByProjectKeyExtensionsKeyByKeyRequestBuilder,
)


class ByProjectKeyExtensionsRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(self, projectKey: str, client: "Client"):
        self._project_key = projectKey
        self._client = client

    def withKey(self, key: str) -> ByProjectKeyExtensionsKeyByKeyRequestBuilder:
        return ByProjectKeyExtensionsKeyByKeyRequestBuilder(
            key=key, projectKey=self._project_key, client=self._client
        )

    def withId(self, ID: str) -> ByProjectKeyExtensionsByIDRequestBuilder:
        return ByProjectKeyExtensionsByIDRequestBuilder(
            ID=ID, projectKey=self._project_key, client=self._client
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
    ) -> "ExtensionPagedQueryResponse":
        """Query extensions
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/extensions",
            params={
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_object=ExtensionPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "ExtensionDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Extension":
        """Currently, a maximum of 25 extensions can be created per project.
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/extensions",
            params={"expand": expand},
            data_object=body,
            response_object=Extension,
            headers={"Content-Type": "application/json", **headers},
        )
