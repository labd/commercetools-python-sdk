# Generated file, please do not change!!!
import typing

from ...models.channel import Channel, ChannelDraft, ChannelPagedQueryResponse
from .by_project_key_channels_by_id_request_builder import (
    ByProjectKeyChannelsByIDRequestBuilder,
)


class ByProjectKeyChannelsRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(self, projectKey: str, client: "Client"):
        self._project_key = projectKey
        self._client = client

    def withId(self, ID: str) -> ByProjectKeyChannelsByIDRequestBuilder:
        return ByProjectKeyChannelsByIDRequestBuilder(
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
    ) -> "ChannelPagedQueryResponse":
        """Query channels
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/channels",
            params={
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_object=ChannelPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "ChannelDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Channel":
        """Create Channel
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/channels",
            params={"expand": expand},
            data_object=body,
            response_object=Channel,
            headers={"Content-Type": "application/json", **headers},
        )
