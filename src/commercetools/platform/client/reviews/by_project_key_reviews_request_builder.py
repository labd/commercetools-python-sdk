# Generated file, please do not change!!!
import typing

from ...models.review import Review, ReviewDraft, ReviewPagedQueryResponse
from .by_project_key_reviews_by_id_request_builder import (
    ByProjectKeyReviewsByIDRequestBuilder,
)
from .by_project_key_reviews_key_by_key_request_builder import (
    ByProjectKeyReviewsKeyByKeyRequestBuilder,
)


class ByProjectKeyReviewsRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def withKey(self, key: str) -> ByProjectKeyReviewsKeyByKeyRequestBuilder:
        return ByProjectKeyReviewsKeyByKeyRequestBuilder(
            key=key,
            projectKey=self._project_key,
            client=self._client,
        )

    def withId(self, ID: str) -> ByProjectKeyReviewsByIDRequestBuilder:
        return ByProjectKeyReviewsByIDRequestBuilder(
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
    ) -> "ReviewPagedQueryResponse":
        """Query reviews"""
        return self._client._get(
            endpoint=f"/{self._project_key}/reviews",
            params={
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_class=ReviewPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "ReviewDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Review":
        """Create Review"""
        return self._client._post(
            endpoint=f"/{self._project_key}/reviews",
            params={"expand": expand},
            data_object=body,
            response_class=Review,
            headers={"Content-Type": "application/json", **headers},
        )
