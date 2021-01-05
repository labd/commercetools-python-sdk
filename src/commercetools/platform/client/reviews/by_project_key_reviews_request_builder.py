# Generated file, please do not change!!!
import typing

from ...models.review import Review, ReviewDraft, ReviewPagedQueryResponse
from .by_project_key_reviews_by_id_request_builder import (
    ByProjectKeyReviewsByIDRequestBuilder,
)
from .by_project_key_reviews_key_by_key_request_builder import (
    ByProjectKeyReviewsKeyByKeyRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyReviewsRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def with_key(self, key: str) -> ByProjectKeyReviewsKeyByKeyRequestBuilder:
        return ByProjectKeyReviewsKeyByKeyRequestBuilder(
            key=key,
            project_key=self._project_key,
            client=self._client,
        )

    def with_id(self, id: str) -> ByProjectKeyReviewsByIDRequestBuilder:
        return ByProjectKeyReviewsByIDRequestBuilder(
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
    ) -> "ReviewPagedQueryResponse":
        """Query reviews"""
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
            endpoint=f"/{self._project_key}/reviews",
            params=params,
            response_class=ReviewPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "ReviewDraft",
        *,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Review":
        """Create Review"""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/reviews",
            params={"expand": expand},
            data_object=body,
            response_class=Review,
            headers={"Content-Type": "application/json", **headers},
        )
