# Generated file, please do not change!!!
import typing

from ...models.message import MessagePagedQueryResponse
from .by_project_key_messages_by_id_request_builder import (
    ByProjectKeyMessagesByIDRequestBuilder,
)


class ByProjectKeyMessagesRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def withId(self, ID: str) -> ByProjectKeyMessagesByIDRequestBuilder:
        return ByProjectKeyMessagesByIDRequestBuilder(
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
    ) -> "MessagePagedQueryResponse":
        """Query messages"""
        return self._client._get(
            endpoint=f"/{self._project_key}/messages",
            params={
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_class=MessagePagedQueryResponse,
            headers=headers,
        )
