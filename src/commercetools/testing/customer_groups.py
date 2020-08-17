import datetime
import uuid
from typing import Optional

from commercetools import types
from commercetools._schemas._customer_group import (
    CustomerGroupDraftSchema,
    CustomerGroupPagedQueryResponseSchema,
    CustomerGroupSchema,
)
from commercetools._schemas._review import ReviewUpdateSchema
from commercetools.testing import abstract, utils


class CustomerGroupModel(abstract.BaseModel):
    _resource_schema = CustomerGroupSchema
    _primary_type_name = "customer-group"
    _unique_values = ["key"]

    def _create_from_draft(
        self, draft: types.CustomerGroupDraft, id: Optional[str] = None
    ) -> types.CustomerGroup:
        object_id = uuid.UUID(id) if id is not None else uuid.uuid4()
        return types.CustomerGroup(
            id=str(object_id),
            key=draft.key,
            version=1,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            last_modified_at=datetime.datetime.now(datetime.timezone.utc),
            name=draft.group_name,
            custom=utils.create_from_draft(draft.custom),
        )


class CustomerGroupBackend(abstract.ServiceBackend):
    service_path = "customer-groups"
    model_class = CustomerGroupModel

    _schema_draft = CustomerGroupDraftSchema
    _schema_update = ReviewUpdateSchema
    _schema_query_response = CustomerGroupPagedQueryResponseSchema

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
