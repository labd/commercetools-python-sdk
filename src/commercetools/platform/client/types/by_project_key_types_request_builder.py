# Generated file, please do not change!!!
import typing

from ...models.type import Type, TypeDraft, TypePagedQueryResponse
from .by_project_key_types_by_id_request_builder import (
    ByProjectKeyTypesByIDRequestBuilder,
)
from .by_project_key_types_key_by_key_request_builder import (
    ByProjectKeyTypesKeyByKeyRequestBuilder,
)


class ByProjectKeyTypesRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(self, projectKey: str, client: "Client"):
        self._project_key = projectKey
        self._client = client

    def withKey(self, key: str) -> ByProjectKeyTypesKeyByKeyRequestBuilder:
        return ByProjectKeyTypesKeyByKeyRequestBuilder(
            key=key, projectKey=self._project_key, client=self._client
        )

    def withId(self, ID: str) -> ByProjectKeyTypesByIDRequestBuilder:
        return ByProjectKeyTypesByIDRequestBuilder(
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
    ) -> "TypePagedQueryResponse":
        """Query types
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/types",
            params={
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_object=TypePagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "TypeDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Type":
        """Create Type
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/types",
            params={"expand": expand},
            data_object=body,
            response_object=Type,
            headers={"Content-Type": "application/json", **headers},
        )
