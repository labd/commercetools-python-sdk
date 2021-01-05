# Generated file, please do not change!!!
import typing

from ...models.state import State, StateDraft, StatePagedQueryResponse
from .by_project_key_states_by_id_request_builder import (
    ByProjectKeyStatesByIDRequestBuilder,
)
from .by_project_key_states_key_by_key_request_builder import (
    ByProjectKeyStatesKeyByKeyRequestBuilder,
)


class ByProjectKeyStatesRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def withKey(self, key: str) -> ByProjectKeyStatesKeyByKeyRequestBuilder:
        return ByProjectKeyStatesKeyByKeyRequestBuilder(
            key=key,
            projectKey=self._project_key,
            client=self._client,
        )

    def withId(self, ID: str) -> ByProjectKeyStatesByIDRequestBuilder:
        return ByProjectKeyStatesByIDRequestBuilder(
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
    ) -> "StatePagedQueryResponse":
        """Query states"""
        return self._client._get(
            endpoint=f"/{self._project_key}/states",
            params={
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_class=StatePagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "StateDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "State":
        """Create State"""
        return self._client._post(
            endpoint=f"/{self._project_key}/states",
            params={"expand": expand},
            data_object=body,
            response_class=State,
            headers={"Content-Type": "application/json", **headers},
        )
