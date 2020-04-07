import datetime
import uuid
from typing import Optional

from commercetools import schemas, types
from commercetools.testing import abstract, utils


class ReviewModel(abstract.BaseModel):
    _resource_schema = schemas.ReviewSchema
    _primary_type_name = "review"
    _unique_values = ["key"]

    def _create_from_draft(
        self, draft: types.ReviewDraft, id: Optional[str] = None
    ) -> types.Review:
        object_id = uuid.UUID(id) if id is not None else uuid.uuid4()

        return types.Review(
            id=str(object_id),
            version=1,
            key=draft.key,
            created_at=datetime.datetime.now(datetime.timezone.utc),
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
    _schema_draft = schemas.ReviewDraftSchema
    _schema_update = schemas.ReviewUpdateSchema
    _schema_query_response = schemas.ReviewPagedQueryResponseSchema

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
