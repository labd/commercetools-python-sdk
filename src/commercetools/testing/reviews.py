import datetime
import uuid
from typing import Optional

from commercetools.platform import models
from commercetools.platform.models._schemas.review import (
    ReviewDraftSchema,
    ReviewPagedQueryResponseSchema,
    ReviewSchema,
    ReviewUpdateSchema,
)
from commercetools.testing import abstract, utils


class ReviewModel(abstract.BaseModel):
    _resource_schema = ReviewSchema
    _primary_type_name = "review"
    _unique_values = ["key"]

    def _create_from_draft(
        self, draft: models.ReviewDraft, id: Optional[str] = None
    ) -> models.Review:
        object_id = uuid.UUID(id) if id is not None else uuid.uuid4()

        return models.Review(
            id=str(object_id),
            version=1,
            key=draft.key,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            last_modified_at=datetime.datetime.now(datetime.timezone.utc),
            uniqueness_value=draft.uniqueness_value,
            locale=draft.locale,
            author_name=draft.author_name,
            title=draft.title,
            text=draft.text,
            target=draft.target,
            included_in_statistics=False,
            rating=draft.rating,
            state=None,
            customer=draft.customer,
            custom=utils.create_from_draft(draft.custom),
        )


class ReviewsBackend(abstract.ServiceBackend):
    service_path = "reviews"
    model_class = ReviewModel
    _schema_draft = ReviewDraftSchema
    _schema_update = ReviewUpdateSchema
    _schema_query_response = ReviewPagedQueryResponseSchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^key=(?P<key>[^/]+)$", "GET", self.get_by_key),
            ("^key=(?P<key>[^/]+)$", "POST", self.update_by_key),
            ("^key=(?P<key>[^/]+)$", "DELETE", self.delete_by_key),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
            ("^(?P<id>[^/]+)$", "DELETE", self.delete_by_id),
        ]
