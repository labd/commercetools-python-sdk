# Generated file, please do not change!!!
import typing

from ...models.zone import Zone, ZoneDraft, ZonePagedQueryResponse
from .by_project_key_zones_by_id_request_builder import (
    ByProjectKeyZonesByIDRequestBuilder,
)
from .by_project_key_zones_key_by_key_request_builder import (
    ByProjectKeyZonesKeyByKeyRequestBuilder,
)


class ByProjectKeyZonesRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(self, projectKey: str, client: "Client"):
        self._project_key = projectKey
        self._client = client

    def withKey(self, key: str) -> ByProjectKeyZonesKeyByKeyRequestBuilder:
        return ByProjectKeyZonesKeyByKeyRequestBuilder(
            key=key, projectKey=self._project_key, client=self._client
        )

    def withId(self, ID: str) -> ByProjectKeyZonesByIDRequestBuilder:
        return ByProjectKeyZonesByIDRequestBuilder(
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
    ) -> "ZonePagedQueryResponse":
        """Query zones
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/zones",
            params={
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_object=ZonePagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "ZoneDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Zone":
        """Create Zone
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/zones",
            params={"expand": expand},
            data_object=body,
            response_object=Zone,
            headers={"Content-Type": "application/json", **headers},
        )
