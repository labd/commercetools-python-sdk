from typing import List, Optional

from marshmallow import fields

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.typing import OptionalListStr

__all__ = ["ReviewService"]


class ReviewDeleteSchema(abstract.AbstractDeleteSchema):
    data_erasure = fields.Bool(data_key="dataErasure", required=False)


class ReviewQuerySchema(abstract.AbstractQuerySchema):
    pass


class ReviewService(abstract.AbstractService):
    def get_by_id(self, id: str, expand: OptionalListStr = None) -> types.Review:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._get(f"reviews/{id}", query_params, schemas.ReviewSchema)

    def get_by_key(self, key: str, expand: OptionalListStr = None) -> types.Review:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._get(
            f"reviews/key={key}", query_params, schemas.ReviewSchema
        )

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: OptionalListStr = None,
        limit: int = None,
        offset: int = None,
    ) -> types.ReviewPagedQueryResponse:
        params = ReviewQuerySchema().dump(
            {
                "where": where,
                "sort": sort,
                "expand": expand,
                "limit": limit,
                "offset": offset,
            }
        )
        return self._client._get(
            "reviews", params, schemas.ReviewPagedQueryResponseSchema
        )

    def create(
        self, draft: types.ReviewDraft, expand: OptionalListStr = None
    ) -> types.Review:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        return self._client._post(
            "reviews",
            query_params,
            draft,
            schemas.ReviewDraftSchema,
            schemas.ReviewSchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: List[types.ReviewUpdateAction],
        expand: OptionalListStr = None,
        *,
        force_update: bool = False,
    ) -> types.Review:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        update_action = types.ReviewUpdate(version=version, actions=actions)
        return self._client._post(
            f"reviews/{id}",
            params=query_params,
            data_object=update_action,
            request_schema_cls=schemas.ReviewUpdateSchema,
            response_schema_cls=schemas.ReviewSchema,
            force_update=force_update,
        )

    def update_by_key(
        self,
        key: str,
        version: int,
        actions: List[types.ReviewUpdateAction],
        expand: OptionalListStr = None,
        *,
        force_update: bool = False,
    ) -> types.Review:
        query_params = {}
        if expand:
            query_params["expand"] = expand
        update_action = types.ReviewUpdate(version=version, actions=actions)
        return self._client._post(
            f"reviews/key={key}",
            params=query_params,
            data_object=update_action,
            request_schema_cls=schemas.ReviewUpdateSchema,
            response_schema_cls=schemas.ReviewSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        data_erasure: bool = False,
        expand: OptionalListStr = None,
        *,
        force_delete: bool = False,
    ) -> types.Review:
        params = {"version": version, "data_erasure": data_erasure}
        if expand:
            params["expand"] = expand
        query_params = ReviewDeleteSchema().dump(params)
        return self._client._delete(
            f"reviews/{id}",
            params=query_params,
            response_schema_cls=schemas.ReviewSchema,
            force_delete=force_delete,
        )

    def delete_by_key(
        self,
        key: str,
        version: int,
        data_erasure: bool = False,
        expand: OptionalListStr = None,
        *,
        force_delete: bool = False,
    ) -> types.Review:
        params = {"version": version, "data_erasure": data_erasure}
        if expand:
            params["expand"] = expand
        query_params = ReviewDeleteSchema().dump(params)
        return self._client._delete(
            f"reviews/key={key}",
            params=query_params,
            response_schema_cls=schemas.ReviewSchema,
            force_delete=force_delete,
        )
