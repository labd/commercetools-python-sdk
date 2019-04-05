import datetime
import uuid
from typing import Optional

from commercetools import schemas, types
from commercetools.testing import abstract, utils


class CustomerGroupModel(abstract.BaseModel):
    _resource_schema = schemas.CustomerGroupSchema
    _primary_type_name = "customer-group"

    def _create_from_draft(
        self, draft: types.CustomerGroupDraft, id: Optional[str] = None
    ) -> types.CustomerGroup:
        object_id = uuid.UUID(id) if id is not None else uuid.uuid4()
        return types.CustomerGroup(
            id=str(object_id),
            key=draft.key,
            version=1,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            name=draft.group_name,
            custom=utils.create_from_draft(draft.custom),
        )


class CustomerGroupBackend(abstract.ServiceBackend):
    service_path = "customer-groups"
    model_class = CustomerGroupModel

    _schema_draft = schemas.CustomerGroupDraftSchema
    _schema_update = schemas.ReviewUpdateSchema
    _schema_query_response = schemas.CustomerGroupPagedQueryResponseSchema

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
